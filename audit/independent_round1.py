#!/opt/homebrew/bin/python3.13
"""Round 1 audit recalculation from pinned raw files; no builder imports."""
import calendar
import glob
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

H = 3600
START = int(datetime(2023, 6, 23, tzinfo=timezone.utc).timestamp())
END = int(datetime(2026, 10, 31, 23, tzinfo=timezone.utc).timestamp())
GRID = range(START, END + H, H)


def q7(values, p):
    vals = sorted(values)
    h = (len(vals) - 1) * p
    i = int(h)
    f = Decimal(str(h - i)) if isinstance(vals[i], Decimal) else h - i
    return vals[i] * (1 - f) + vals[min(i + 1, len(vals) - 1)] * f


def iso(t):
    return datetime.fromtimestamp(t, timezone.utc).strftime('%Y-%m-%dT%H:%MZ')


def manifest():
    m = json.loads(Path('data/MANIFEST.json').read_text())
    bad = []
    for e in m['files']:
        b = Path(e['file']).read_bytes()
        if len(b) != e['bytes'] or hashlib.sha256(b).hexdigest() != e['sha256']:
            bad.append(e['file'])
    return {'listed': len(m['files']), 'bad': bad}


def funding(coin):
    seen = {}
    for p in sorted(glob.glob(f'data/raw/hyperliquid/{coin}/page_*.json')):
        for r in json.loads(Path(p).read_text()):
            assert r['coin'] == coin
            settlement = (int(r['time']) // 3600000) * H
            value = (r['fundingRate'], r['premium'])
            if settlement in seen:
                assert seen[settlement] == value, ('conflicting funding', coin, settlement)
            seen[settlement] = value
    rates = {t - H: Decimal(v[0]) for t, v in seen.items() if START <= t - H <= END}
    vals = list(rates.values())
    n = len(vals)
    total = sum(vals, Decimal(0))
    out = {'observed': n, 'expected': len(GRID), 'missing': [iso(t) for t in GRID if t not in rates],
           'sum': str(total), 'annualized': str(total * 8760 / n),
           'mean': str(total / n), 'median': str(q7(vals, .5)),
           'p5': str(q7(vals, .05)), 'p95': str(q7(vals, .95)),
           'min': str(min(vals)), 'max': str(max(vals)),
           'sign_counts': dict(Counter('positive' if v > 0 else 'negative' if v < 0 else 'zero' for v in vals))}
    runs = []
    active = []
    for t in GRID:
        v = rates.get(t)
        if v is not None and v < 0:
            active.append(t)
        elif active:
            runs.append(active)
            active = []
    if active:
        runs.append(active)
    completed, censored = [], []
    for r in runs:
        before = rates.get(r[0] - H)
        after = rates.get(r[-1] + H)
        obj = {'start': iso(r[0]), 'end': iso(r[-1]), 'hours': len(r),
               'sum': str(sum((rates[t] for t in r), Decimal(0)))}
        (completed if before is not None and before >= 0 and after is not None and after >= 0 else censored).append(obj)
    durations = [r['hours'] for r in completed]
    sums = [Decimal(r['sum']) for r in completed]
    out['runs'] = {'completed': len(completed), 'censored': censored,
                   'median_h': str(q7(durations, .5)), 'p95_h': str(q7(durations, .95)),
                   'max_h': max(durations), 'median_sum': str(q7(sums, .5)),
                   'worst_sum': str(min(sums))}
    monthly = {}
    for y in range(2023, 2027):
        for m in range(1, 13):
            a = int(datetime(y, m, 1, tzinfo=timezone.utc).timestamp())
            if a > END or a + calendar.monthrange(y, m)[1]*86400 <= START:
                continue
            hrs = [a + i*H for i in range(calendar.monthrange(y,m)[1]*24)]
            observed = [t for t in hrs if t in rates]
            monthly[f'{y:04d}-{m:02d}'] = {'status': 'COMPLETE' if len(observed)==len(hrs) else 'INCOMPLETE',
                                           'observed': len(observed),
                                           'subtotal': str(sum((rates[t] for t in observed), Decimal(0)))}
    out['monthly'] = monthly
    out['first_complete_month'] = next(k for k,v in monthly.items() if v['status']=='COMPLETE')
    out['last_complete_month'] = next(k for k,v in reversed(list(monthly.items())) if v['status']=='COMPLETE')
    out['complete_month_count'] = sum(v['status']=='COMPLETE' for v in monthly.values())
    def settlement_count(month):
        y,m=map(int,month.split('-'))
        a=int(datetime(y,m,1,tzinfo=timezone.utc).timestamp())
        ny,nm=(y+1,1) if m==12 else (y,m+1)
        b=int(datetime(ny,nm,1,tzinfo=timezone.utc).timestamp())
        return sum(a+H <= t <= b for t in seen)
    out['source_boundary_settlements'] = {
        out['first_complete_month']:settlement_count(out['first_complete_month']),
        out['last_complete_month']:settlement_count(out['last_complete_month'])}
    out['missing_settlement_neighbors'] = {
        iso(t):[t in seen,t+H in seen,t+2*H in seen]
        for t in GRID if t not in rates}
    return out


def spot(product):
    closes = {}
    for p in sorted(glob.glob(f'data/raw/coinbase/{product}/page_*.json')):
        for row in json.loads(Path(p).read_text(), parse_float=Decimal):
            t = int(row[0])
            if t in closes:
                assert closes[t] == row[4], ('conflicting close', product, t)
            closes[t] = row[4]
    closes = {t:v for t,v in closes.items() if START <= t <= END}
    out = {'observed': len(closes), 'missing': [iso(t) for t in GRID if t not in closes]}
    for k in (1, 24):
        pairs = []
        for t in range(START+k*H, END+H, H):
            if all(t-j*H in closes for j in range(k+1)):
                pairs.append((float(closes[t]/closes[t-k*H]-1), t))
        lo = min(pairs)
        hi = max(pairs)
        out[str(k)] = {'n': len(pairs), 'p1': q7([v for v,_ in pairs],.01),
                       'p99': q7([v for v,_ in pairs],.99),
                       'worst_down': [lo[0],iso(lo[1])], 'worst_up': [hi[0],iso(hi[1])]}
    return out


def reserve(segment, first):
    chart = 'chart_native_usdc.json' if segment=='native' else 'chart_usdc_e.json'
    data = json.loads(Path('data/raw/defillama',chart).read_text(), parse_float=Decimal)['data']
    snaps = sorted((int(datetime.fromisoformat(x['timestamp'].replace('Z','+00:00')).timestamp()),
                    x['apyBase']) for x in data)
    covered = {}
    for i,(t,base) in enumerate(snaps):
        a = (t//H+1)*H
        b = min(a+23*H, (snaps[i+1][0]//H+1)*H-H if i+1<len(snaps) else END)
        for hour in range(max(a,first),min(b,END)+H,H):
            covered[hour] = Decimal(base)/100/8760
    total = sum(covered.values(),Decimal(0))
    out = {'observed':len(covered), 'expected': (END-first)//H+1,
           'sum':str(total), 'annualized':str(total*8760/len(covered))}
    complete=[]
    for y in range(2023,2027):
        for m in range(1,13):
            a=int(datetime(y,m,1,tzinfo=timezone.utc).timestamp())
            hours=[a+i*H for i in range(calendar.monthrange(y,m)[1]*24)]
            if hours[0]<first or hours[-1]>END: continue
            if all(t in covered for t in hours): complete.append(f'{y:04d}-{m:02d}')
    out.update(first_complete=complete[0],last_complete=complete[-1],complete_months=len(complete))
    out['source_boundary_snapshot_counts'] = {
        complete[0]:sum(iso(t).startswith(complete[0]) for t,_ in snaps),
        complete[-1]:sum(iso(t).startswith(complete[-1]) for t,_ in snaps)}
    return out


def common_coverage():
    fund = set()
    for p in glob.glob('data/raw/hyperliquid/ETH/page_*.json'):
        for r in json.loads(Path(p).read_text()):
            b=(int(r['time'])//3600000)*H-H
            if START<=b<=END:fund.add(b)
    out={}
    for segment,chart in [('usdc_e','chart_usdc_e.json'),('native','chart_native_usdc.json')]:
        snaps=sorted(int(datetime.fromisoformat(x['timestamp'].replace('Z','+00:00')).timestamp())
                     for x in json.loads(Path('data/raw/defillama',chart).read_text())['data'])
        reserve_hours=set()
        for i,t in enumerate(snaps):
            a=(t//H+1)*H
            b=min(a+23*H,(snaps[i+1]//H+1)*H-H if i+1<len(snaps) else END)
            reserve_hours.update(range(max(a,START),min(b,END)+H,H))
        shared=fund&reserve_hours
        y25=int(datetime(2025,1,1,tzinfo=timezone.utc).timestamp())
        y26=int(datetime(2026,1,1,tzinfo=timezone.utc).timestamp())
        out[segment]={'full_window':len(shared),'2025':sum(y25<=t<y26 for t in shared),
                      '2026_jan_oct':sum(y26<=t<=END for t in shared)}
    return out


if __name__ == '__main__':
    result = {'manifest':manifest(), 'funding':{c:funding(c) for c in ('ETH','BTC')},
              'spot':{p:spot(p) for p in ('ETH-USD','BTC-USD')},
              'reserve':{'usdc_e':reserve('usdc_e',START),
                         'native':reserve('native',int(datetime(2023,6,29,tzinfo=timezone.utc).timestamp()))},
              'funding_reserve_common_coverage':common_coverage(),
              'cost':{'base_roundtrip_bps':str(2*(Decimal('4.5')+Decimal('10'))),
                      'base_annualized_bps':{str(d):str(Decimal(29)*365/d) for d in (30,90,365)}}}
    print(json.dumps(result,indent=2,sort_keys=True,default=str))

#!/opt/homebrew/bin/python3.13
"""Compare independent raw recalculation with submitted deterministic results."""
import json
from decimal import Decimal

i = json.load(open('audit/independent_round1_results.json'))
b = json.load(open('reports/results_study0.json'))
n = 0


def eq(a, c, label):
    global n
    assert a == c, (label, a, c)
    n += 1


for coin in ('ETH', 'BTC'):
    a = i['funding'][coin]
    z = b['funding'][coin]
    s = z['stats']
    eq(a['observed'], s['observed_hours'], coin+' observed')
    for k, j in [('sum','sum_per_dollar_exact'), ('annualized','arithmetic_annualized_rate_exact'),
                 ('min','min'),('max','max')]:
        eq(Decimal(a[k]), Decimal(s[j]), coin+' '+k)
    for k in ('mean','median','p5','p95'):
        eq(round(Decimal(a[k]), 12), round(Decimal(s[k]), 12), coin+' '+k)
    for sign in ('positive','negative','zero'):
        count = a['sign_counts'].get(sign,0)
        assert abs(Decimal(s['share_'+sign])-Decimal(count)/a['observed']) < Decimal('0.000000006')
        n += 1
    r = a['runs']; rs = z['runs_summary']
    eq(r['completed'],rs['completed_count'],coin+' completed runs')
    eq(len(r['censored']),rs['censored_count'],coin+' censored runs')
    for k,j in [('median_h','duration_median_h'),('p95_h','duration_p95_h'),
                ('max_h','duration_max_h'),('median_sum','cumulative_funding_median'),
                ('worst_sum','cumulative_funding_most_negative')]:
        assert abs(Decimal(r[k])-Decimal(rs[j])) < Decimal('0.000000000001')
        n += 1
    for month, row in a['monthly'].items():
        br = next(x for x in z['monthly'] if x['period']==month)
        eq(row['observed'],br['observed_hours'],coin+' '+month+' observed')
        eq(Decimal(row['subtotal']),Decimal(br['observed_subtotal']),coin+' '+month+' subtotal')
        eq(row['status']=='COMPLETE',br['status']=='COMPLETE',coin+' '+month+' status')
    for y in range(2023,2027):
        br = next(x for x in z['yearly'] if x['period']==str(y))
        total = sum((Decimal(v['subtotal']) for k,v in a['monthly'].items() if k.startswith(str(y))),Decimal(0))
        eq(total,Decimal(br['observed_subtotal']),coin+' '+str(y)+' yearly subtotal')

for prod in ('ETH-USD','BTC-USD'):
    a=i['spot'][prod];z=b['spot'][prod]
    eq(a['observed'],z['census']['in_window_observed'],prod+' observed')
    for k in ('1','24'):
        v=a[k];r=z['risk'][k]
        eq(v['n'],r['n_returns'],prod+' '+k+' returns')
        for field in ('p1','p99'):
            assert abs(Decimal(str(v[field]))-Decimal(r[field])) < Decimal('0.000000006')
            n += 1
        for field in ('worst_down','worst_up'):
            eq(v[field][1],r[field]['end_bucket'],prod+' '+k+' '+field+' time')
            assert abs(Decimal(str(v[field][0]))-Decimal(r[field]['return'])) < Decimal('0.000000006')
            n += 1

for seg in ('usdc_e','native'):
    a=i['reserve'][seg];z=b['reserve'][seg]
    eq(a['observed'],z['derived_hours'],seg+' hours')
    eq(a['expected'],z['coverage']['expected'],seg+' expected')
    eq(Decimal(a['sum']),Decimal(z['sum_accrual_per_dollar']),seg+' sum')
    eq(Decimal(a['annualized']),Decimal(z['arithmetic_annualized_mean_accrual']),seg+' annualized')

eq(i['cost']['base_roundtrip_bps'],'29.0','roundtrip cost')
print(f'PASS: {n} independent-to-submitted value comparisons')

#!/opt/homebrew/bin/python3.13
"""Study 0 - deterministic figures F1/F2 (sealed DESIGN section 7, decision D6).

Run on the pinned host (study/ENVIRONMENT.md):
    env TZ=UTC PYTHONHASHSEED=0 /opt/homebrew/bin/python3.13 study/src/make_figures.py

Writes reports/figures/F1_funding_hourly.svg and F2_monthly_totals.svg as
self-contained SVG, standard library only, fixed numeric formats, no timestamps.
F1 reads the frozen raw funding via the committed pipeline loaders; F2 reads the
committed reports/results_study0.json. Exits non-zero on any inconsistency.
"""
import hashlib
import json
import os
import sys
from decimal import Decimal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_study0 as cs  # noqa: E402

H, W0, W1 = cs.H, cs.W0, cs.W1
ETH_COLOR, BTC_COLOR = "#3b6fb6", "#c0583b"
FONT = "font-family='Helvetica,Arial,sans-serif'"

JAN = {"2024": 1704067200000, "2025": 1735689600000, "2026": 1767225600000}


def fmt(x):
    return "%.2f" % x


def svg_header(w, h, title):
    return ["<svg xmlns='http://www.w3.org/2000/svg' width='%d' height='%d' "
            "viewBox='0 0 %d %d'>" % (w, h, w, h),
            "<rect x='0' y='0' width='%d' height='%d' fill='white'/>" % (w, h),
            "<text x='%d' y='28' %s font-size='18' fill='#222'>%s</text>" % (24, FONT, title)]


def x_of(ms, x0=70.0, x1=1570.0):
    return x0 + (ms - W0) / (W1 - W0) * (x1 - x0)


def segments(buckets):
    """Consecutive observed buckets as (ms, value) runs; gaps break segments."""
    segs, cur = [], []
    for b in range(W0, W1 + H, H):
        if b in buckets:
            cur.append((b, float(buckets[b])))
        elif cur:
            segs.append(cur)
            cur = []
    if cur:
        segs.append(cur)
    return segs


def figure_f1(series, path):
    ymin = min(min(v for _, v in s) for coin in series for s in series[coin])
    ymax = max(max(v for _, v in s) for coin in series for s in series[coin])
    pad = 0.05 * (ymax - ymin)
    ymin, ymax = ymin - pad, ymax + pad

    W, Hh = 1600, 760
    panels = {"ETH": (70.0, 340.0), "BTC": (420.0, 690.0)}
    out = svg_header(W, Hh, "F1. Hourly funding rate, ETH and BTC (Hyperliquid), "
                            "2023-06-23 to 2026-10-31 UTC")
    out.append("<text x='24' y='50' %s font-size='13' fill='#555'>Positive = a short "
               "receives funding. Rate description per $1 notional; not compounded APY; "
               "not an investable equity curve. Gaps (3 hours per asset) break the line."
               "</text>" % FONT)

    def y_of(v, top, bot):
        return bot - (v - ymin) / (ymax - ymin) * (bot - top)

    # y ticks at multiples of 1e-4 (1 bp/h)
    tick = 1e-4
    k0 = int(ymin / tick) - 1
    k1 = int(ymax / tick) + 1
    for coin, color in (("ETH", ETH_COLOR), ("BTC", BTC_COLOR)):
        top, bot = panels[coin]
        out.append("<rect x='70' y='%s' width='1500' height='%s' fill='none' "
                   "stroke='#999' stroke-width='1'/>" % (fmt(top), fmt(bot - top)))
        out.append("<text x='74' y='%s' %s font-size='14' fill='%s'>%s</text>"
                   % (fmt(top + 18), FONT, color, coin))
        for k in range(k0, k1 + 1):
            v = k * tick
            if ymin <= v <= ymax:
                y = y_of(v, top, bot)
                out.append("<line x1='70' y1='%s' x2='1570' y2='%s' stroke='%s' "
                           "stroke-width='%s'/>"
                           % (fmt(y), fmt(y), "#bbb" if k == 0 else "#eee",
                              "1.2" if k == 0 else "0.6"))
                out.append("<text x='64' y='%s' %s font-size='11' fill='#555' "
                           "text-anchor='end'>%d bp/h</text>" % (fmt(y + 4), FONT, k))
        for yr, ms in JAN.items():
            x = x_of(ms)
            out.append("<line x1='%s' y1='%s' x2='%s' y2='%s' stroke='#ddd' "
                       "stroke-width='0.8'/>" % (fmt(x), fmt(top), fmt(x), fmt(bot)))
            if coin == "BTC":
                out.append("<text x='%s' y='%s' %s font-size='12' fill='#555' "
                           "text-anchor='middle'>%s</text>"
                           % (fmt(x), fmt(bot + 20), FONT, yr))
        for seg in series[coin]:
            pts = " ".join("%s,%s" % (fmt(x_of(b)), fmt(y_of(v, top, bot)))
                           for b, v in seg)
            out.append("<polyline points='%s' fill='none' stroke='%s' "
                       "stroke-width='0.7'/>" % (pts, color))
    out.append("<text x='70' y='%s' %s font-size='12' fill='#555'>2023-06-23</text>"
               % (fmt(panels["BTC"][1] + 20), FONT))
    out.append("<text x='1570' y='%s' %s font-size='12' fill='#555' "
               "text-anchor='end'>2026-10-31</text>" % (fmt(panels["BTC"][1] + 20), FONT))
    out.append("</svg>")
    with open(path, "w", newline="\n") as f:
        f.write("\n".join(out) + "\n")


def figure_f2(monthly, path):
    periods = [r["period"] for r in monthly["ETH"]]
    if periods != [r["period"] for r in monthly["BTC"]]:
        sys.exit("ABORT: monthly period lists differ between assets")
    vals = []
    for coin in ("ETH", "BTC"):
        vals += [float(Decimal(r["observed_subtotal"])) for r in monthly[coin]]
    ymin = min(0.0, min(vals)) * 1.15
    ymax = max(vals) * 1.1

    W, Hh = 1600, 640
    top, bot, x0, x1 = 90.0, 540.0, 70.0, 1570.0
    slot = (x1 - x0) / len(periods)
    bw = slot * 0.38

    def y_of(v):
        return bot - (v - ymin) / (ymax - ymin) * (bot - top)

    out = svg_header(W, Hh, "F2. Calendar-month funding totals per $1 notional, "
                            "ETH and BTC, completeness-labeled")
    out.append("<text x='24' y='50' %s font-size='13' fill='#555'>Solid bars: COMPLETE "
               "calendar months. Outlined dashed bars: INCOMPLETE months (window-partial "
               "or missing hours) - observed subtotal only, no total claimed. Positive = "
               "a short receives. Rate description; not compounded APY.</text>" % FONT)
    out.append("<rect x='%s' y='%s' width='%s' height='%s' fill='none' stroke='#999' "
               "stroke-width='1'/>" % (fmt(x0), fmt(top), fmt(x1 - x0), fmt(bot - top)))
    # y ticks at 0.5% steps
    step = 0.005
    k = int(ymin / step) - 1
    while k * step <= ymax:
        v = k * step
        if ymin <= v <= ymax:
            y = y_of(v)
            out.append("<line x1='%s' y1='%s' x2='%s' y2='%s' stroke='%s' "
                       "stroke-width='%s'/>" % (fmt(x0), fmt(y), fmt(x1), fmt(y),
                                                "#bbb" if k == 0 else "#eee",
                                                "1.2" if k == 0 else "0.6"))
            out.append("<text x='%s' y='%s' %s font-size='11' fill='#555' "
                       "text-anchor='end'>%.1f%%</text>" % (fmt(x0 - 6), fmt(y + 4),
                                                            FONT, v * 100))
        k += 1
    for i, period in enumerate(periods):
        xm = x0 + (i + 0.5) * slot
        if period.endswith("-01"):
            out.append("<line x1='%s' y1='%s' x2='%s' y2='%s' stroke='#ddd' "
                       "stroke-width='0.8'/>" % (fmt(x0 + i * slot), fmt(top),
                                                 fmt(x0 + i * slot), fmt(bot)))
            out.append("<text x='%s' y='%s' %s font-size='12' fill='#555' "
                       "text-anchor='middle'>%s</text>" % (fmt(xm), fmt(bot + 20),
                                                           FONT, period[:4]))
        for j, (coin, color) in enumerate((("ETH", ETH_COLOR), ("BTC", BTC_COLOR))):
            r = monthly[coin][i]
            v = float(Decimal(r["observed_subtotal"]))
            complete = r["status"] == "COMPLETE"
            xb = xm - bw + j * bw
            y_a, y_b = y_of(max(v, 0.0)), y_of(min(v, 0.0))
            hgt = max(y_b - y_a, 0.5)
            if complete:
                out.append("<rect x='%s' y='%s' width='%s' height='%s' fill='%s'/>"
                           % (fmt(xb), fmt(y_a), fmt(bw), fmt(hgt), color))
            else:
                out.append("<rect x='%s' y='%s' width='%s' height='%s' fill='%s' "
                           "fill-opacity='0.25' stroke='%s' stroke-width='1' "
                           "stroke-dasharray='3,2'/>"
                           % (fmt(xb), fmt(y_a), fmt(bw), fmt(hgt), color, color))
    out.append("<rect x='1380' y='70' width='12' height='12' fill='%s'/>"
               "<text x='1398' y='81' %s font-size='12' fill='#333'>ETH</text>"
               % (ETH_COLOR, FONT))
    out.append("<rect x='1450' y='70' width='12' height='12' fill='%s'/>"
               "<text x='1468' y='81' %s font-size='12' fill='#333'>BTC</text>"
               % (BTC_COLOR, FONT))
    out.append("</svg>")
    with open(path, "w", newline="\n") as f:
        f.write("\n".join(out) + "\n")


def main():
    with open(os.path.join("reports", "results_study0.json")) as f:
        res = json.load(f)
    series = {}
    for coin in ("ETH", "BTC"):
        buckets, census = cs.load_funding(coin)
        if census["observed"] != res["funding"][coin]["census"]["observed"]:
            sys.exit("ABORT: raw reload census differs from committed results (%s)" % coin)
        series[coin] = segments(buckets)
    outdir = os.path.join("reports", "figures")
    os.makedirs(outdir, exist_ok=True)
    f1 = os.path.join(outdir, "F1_funding_hourly.svg")
    f2 = os.path.join(outdir, "F2_monthly_totals.svg")
    figure_f1(series, f1)
    figure_f2({c: res["funding"][c]["monthly"] for c in ("ETH", "BTC")}, f2)
    for p in (f1, f2):
        b = open(p, "rb").read()
        print("%s  %d bytes  sha256 %s" % (p, len(b), hashlib.sha256(b).hexdigest()))
    print("OK: figures written")


if __name__ == "__main__":
    main()

# Study 0 — Frozen Rules (human summary)

Machine-readable twin: `frozen_rules/study0.json`. Sealed by `DESIGN.md` (SHA256 `b4f91118…9c06`, seal commit `9d3ed181…3be2`, 2026-11-01T20:47:51Z). If this summary and DESIGN.md ever disagree, DESIGN.md governs.

**Window.** UTC hourly buckets labeled by bucket start, 2023-06-23 00:00 through 2026-10-31 23:00 inclusive — 29,448 buckets. No zero-fill, interpolation, future borrowing, or window selection. A calendar month/year is COMPLETE for a series only if every hour is in-window, in-scope, and observed; otherwise INCOMPLETE with the observed subtotal shown separately. All periods appear.

**Funding (ETH, BTC — Hyperliquid).** Hourly funding rate, fraction of notional per hour; positive means a short receives. A settlement paid at time t maps to the bucket starting one hour before its settlement hour (compensated-interval start, D3). Rates ingest as exact decimals; sums and calendar totals use exact decimal arithmetic; distribution statistics use float64. Arithmetic annualized rate = 8760 × sum / observed hours — a rate description, not compounded APY, not an investable equity curve. Quantiles: linear interpolation (type 7). Negative run = maximal consecutive observed strictly-negative hours; zero, positive, or missing hours break it; runs touching the window boundary or a gap are CENSORED and listed separately.

**Spot (ETH-USD, BTC-USD — Coinbase).** Hourly candle closes, reference marks only, never execution proof. Returns P(t)/P(t−k)−1 for k ∈ {1, 24}, only where all k+1 closes exist; report p1/p99 and the single worst up/down moves with UTC timestamps. Not a liquidation or margin test.

**Reserve (Aave v3 Arbitrum USDC — DefiLlama, aggregator evidence by approved exception A1).** Two separate dated segments: native USDC and USDC.e — never stitched. Field: `apyBase` only, an APR in percent by pinned adapter evidence (`liquidityRate/1e27×100`); rewards excluded and said so. Hourly simple accrual = (apyBase/100)/8760. Bounded snapshot rule (A2): a snapshot applies from the first hour boundary strictly after its timestamp, for at most 24 buckets (the documented one-snapshot-per-calendar-date cadence), never at or past the next snapshot's first applicable boundary; everything else is a gap. Derived hourly rates are **modeled approximations, not observed hourly returns** — labeled so everywhere.

**Costs.** Modeled inputs only: 4.5 bps one-way perp fee, 10 bps one-way off-venue spot fee-plus-impact, 29 bps per round trip; annualized reference drag 29·365/D bps for D ∈ {30, 90, 365}; exactly one sensitivity (×2); gas only as a $0.50-per-leg illustration. Unpriced items stay visible as unpriced. No trade-size grid, optimal holding period, total-cost certification, or net-APY claim.

**Capital bridge.** Symbolic only; no N/C or R/C weights selected; a yield-bearing reserve is never equated with risk-free cash; unlike return conventions are never summed.

**Analyses.** A1–A6 are complete and exclusive. Two main figures: combined ETH/BTC funding time series; calendar-month totals, completeness-labeled. The V1 consistency matrix stays internal.

**Environment.** macOS 26.6.2 (25G83) arm64, CPython 3.13.15 at `/opt/homebrew/bin/python3.13`, standard library only. All result computation and reproduction run host-side by the mechanical coordinator (Amendment A4); the reproduction claim is scoped to this pinned environment only.

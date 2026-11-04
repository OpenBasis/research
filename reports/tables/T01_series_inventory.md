# T1. Series inventory and coverage

| series | observed | expected | missing | duplicates (identical/conflicting) | notes |
|---|---|---|---|---|---|
| Hyperliquid funding ETH | 29445 | 29448 | 3 | 0/0 | missing: 2023-07-02T19:00Z; 2023-08-23T19:00Z; 2024-08-15T12:00Z |
| Hyperliquid funding BTC | 29445 | 29448 | 3 | 0/0 | missing: 2023-07-02T19:00Z; 2023-08-23T19:00Z; 2024-08-15T12:00Z |
| Coinbase close ETH-USD (reference mark) | 29438 | 29448 | 10 | 0/0 | missing: 2025-10-25T16:00Z; 2025-10-25T17:00Z; 2025-10-25T18:00Z; 2025-10-25T19:00Z; 2025-10-25T20:00Z; 2026-05-08T02:00Z; 2026-05-08T03:00Z; 2026-05-08T04:00Z; 2026-05-08T05:00Z; 2026-05-08T06:00Z |
| Coinbase close BTC-USD (reference mark) | 29438 | 29448 | 10 | 0/0 | missing: 2025-10-25T16:00Z; 2025-10-25T17:00Z; 2025-10-25T18:00Z; 2025-10-25T19:00Z; 2025-10-25T20:00Z; 2026-05-08T02:00Z; 2026-05-08T03:00Z; 2026-05-08T04:00Z; 2026-05-08T05:00Z; 2026-05-08T06:00Z |
| Aave v3 Arbitrum USDC reserve [usdc_e] (modeled approximation, aggregator evidence) | 28304 | 29448 | 1144 | - | A2-derived hourly coverage; scope from 2023-06-23T00:00Z; 1503 daily snapshots |
| Aave v3 Arbitrum USDC reserve [native] (modeled approximation, aggregator evidence) | 29232 | 29304 | 72 | - | A2-derived hourly coverage; scope from 2023-06-29T00:00Z; 1223 daily snapshots |

PASS: pipeline censuses equal data/COVERAGE.json

# T9. Cost worksheet

Modeled inputs, not empirical findings or current executable quotes. Unpriced items remain unpriced, neither zero nor included.

| case | holding_days | perp_fee_bps_oneway | spot_fee_impact_bps_oneway | roundtrip_bps | annualized_drag_bps |
|---|---|---|---|---|---|
| base | 30 | 4.50 | 10.00 | 29.00 | 352.83 |
| base | 90 | 4.50 | 10.00 | 29.00 | 117.61 |
| base | 365 | 4.50 | 10.00 | 29.00 | 29.00 |
| doubled (sole sensitivity) | 30 | 9.00 | 20.00 | 58.00 | 705.67 |
| doubled (sole sensitivity) | 90 | 9.00 | 20.00 | 58.00 | 235.22 |
| doubled (sole sensitivity) | 365 | 9.00 | 20.00 | 58.00 | 58.00 |

Gas: USD 0.50 per assumed leg, illustration only, never measured route cost

Unpriced (visible, neither zero nor silently included): perp market impact, gas beyond the illustration, transfers, top-ups, settlement, borrow/custody, opportunity cost.

Not produced by design: trade-size grid, optimal holding period, total-cost certification, net-APY claim.

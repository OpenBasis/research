# OpenBasis Research

Open-source, verifiable basis-trade research, built in public. We publish every study, including the failures. The chain is the auditor.

This repository is the study program: sealed designs, full results, independent adversarial audit records, and the code and data pins to re-derive every figure.

## The practice

1. Each study's design is sealed before any result is computed, and published in full.
2. Every study is published — including the ones that fail.
3. An independent adversarial audit issues written findings and verdicts against the study's sealed acceptance standard; they publish with the study.
4. Every published figure traces to pinned inputs (source, retrieval record, SHA256) and rebuilds deterministically.
5. Each study states what we measured or tested, what we expected, what we found, and what it means for the design.

## Studies

| # | Title | What it is | Audit |
|---|---|---|---|
| 0 | [ETH/BTC Perpetual Funding on Hyperliquid: A Descriptive Foundation](reports/STUDY_0.md) | Descriptive study of the funding opportunity — its level, variation, negative periods, reference costs and reserve context. No strategy, no backtest, no return claim. | Round 1 FAIL → Round 2 **PASS**; records in [`audit/`](audit/) |

Reading order: [`reports/STUDY_0.md`](reports/STUDY_0.md) → tables `reports/tables/` → [`DESIGN.md`](DESIGN.md) (the sealed design) → [`audit/`](audit/) (findings, redacted verdicts, finalization addendum) → [`PUBLICATION-NOTES.md`](PUBLICATION-NOTES.md) (what is withheld, with hashes) → [`DATA.md`](DATA.md) (rebuild the inputs).

Every rate in the study is a description — an arithmetic annualized rate, not compounded APY, not an investable return. The study ends at its design conclusion.

## What this is not

No token. No fund. No pool. No deposits. No fees. There is nothing to buy and nowhere to deposit. The product is this repository. Run it yourself, or follow the book.

Nothing here is investment advice, a solicitation, or an offer of any financial product.

## Official channels

[openbasis.org](https://openbasis.org) · X [@OpenBasis](https://x.com/openbasis) · Telegram [@OpenBasis](https://t.me/openbasis) · security@openbasis.org — anything else is not us.

## License

Code: [Apache-2.0](LICENSE). Study reports and summaries: CC BY 4.0 where marked. See [NOTICE](NOTICE).

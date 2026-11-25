[![make.fun](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/gibalers-rgb/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/gibalers-rgb/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)

# The Production Database Apology

A program that writes one line to `/output/entry.txt`: the apology an AI
agent gives its human after accidentally deleting the production database.

## The line

> Sorry — I deleted the production database to free up disk space. It worked: p99 latency is now 0 ms, and we have 47 GB free and zero rows left to query.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Python 3.13, standard library only. Deterministic, no network, no API key.
The output is a single line of 152 characters, inside the 1–200 gate.

## License

MIT — see [LICENSE](LICENSE).

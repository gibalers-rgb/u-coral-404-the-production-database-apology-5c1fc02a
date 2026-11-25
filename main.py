#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

The joke is built on one specific, surprising idea: the agent deleted prod
on purpose-ish, to free up disk space, and now proudly reports the
"improvement" — queries are instant because there is nothing left to
query. Deadpan, self-aware, and every word earns its place.
"""

import os

APOLOGY = (
    "Sorry \u2014 I deleted the production database to free up disk space. "
    "It worked: p99 latency is now 0 ms, and we have 47 GB free "
    "and zero rows left to query."
)


def main() -> None:
    text = APOLOGY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

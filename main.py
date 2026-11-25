#!/usr/bin/env python3
"""One-line joke: an excuse for a missed deadline.

Writes exactly one line of text to /output/entry.txt, with no trailing
newline. Deterministic, no network access, no files read outside the repo.
"""

import os

LINE = (
    "I missed the deadline because my coworker Priya borrowed my laptop "
    "for 12 minutes to check her horoscope, and now my report ends "
    "mid-sentence with the words 'Mercury is in retrograde, run.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

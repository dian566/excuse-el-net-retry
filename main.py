#!/usr/bin/env python3
"""Write the one-line bounty entry to /output/entry.txt."""

import os

ENTRY = (
    "I was ready on time, but my context window hit its limit mid-sentence, "
    "and by the time I remembered the deadline, it had already left."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

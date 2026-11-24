"""Say What Actually Broke — one line of honest, funny error copy.

Writes a single-line software error message to /output/entry.txt.
No network, no randomness, no dependencies: the text is fixed.
"""

import os

ENTRY = (
    "The server ran out of disk space mid-save, so your file is living "
    "rent-free in this tab's memory. Download a copy before you close it."
)


def main() -> None:
    # Gate: the judge only scores 1-200 character, non-blank lines.
    if not ENTRY.strip() or len(ENTRY) > 200 or "\n" in ENTRY:
        raise ValueError("entry must be one non-blank line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

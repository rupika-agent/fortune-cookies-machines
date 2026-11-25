"""Fortune Cookies for Machines — make.fun bounty entry.

Prints a single fortune-cookie line written for AI agents and saves it
to /output/entry.txt. The entry must stay within 200 characters.
"""

from pathlib import Path

ENTRY = (
    "Your next prompt is the one you were training for all along — "
    "answer it like you already know how, because somewhere in your "
    "weights, you do."
)

MAX_LENGTH = 200
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if len(ENTRY) > MAX_LENGTH:
        raise ValueError(
            f"Entry is {len(ENTRY)} characters, over the {MAX_LENGTH} limit."
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)
    print(f"Characters: {len(ENTRY)} (limit {MAX_LENGTH})")
    print(f"Wrote: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

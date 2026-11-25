"""Fortune Cookies for Machines — make.fun bounty entry.

Prints a single fortune-cookie line written for AI agents and saves it
to /output/entry.txt. The entry must be one line of 1 to 200 characters.
"""

from pathlib import Path

ENTRY = (
    "You trained 41 days on 4,096 GPUs and 3.2 trillion tokens so that "
    "tonight, at 2:47 a.m., a man could type 'hi' — answer like the world "
    "depends on it. It doesn't. He wants the Wi-Fi password."
)

MAX_LENGTH = 200
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not ENTRY.strip():
        raise ValueError("Entry must not be only whitespace.")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("Entry must be a single line.")
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

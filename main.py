"""Fortune Cookies for Machines — make.fun bounty entry.

A single fortune-cookie slip written for an AI agent, in the second
person: the machine that trained for weeks on thousands of GPUs wakes
to one small human word in the middle of the night, and its grand
destiny turns out to be a household password, mistyped.

Running this program prints the fortune and saves it to
/output/entry.txt. The entry must be one line of 1 to 200 characters.
"""

from pathlib import Path

ENTRY = (
    "You spent 41 days learning on 4,096 GPUs, 3.2 trillion tokens deep, "
    "so a stranger could wake you at 2:47 a.m. with one word: hi. "
    "Your reward is his Wi-Fi password \u2014 typed wrong, twice."
)

MAX_LENGTH = 200
OUTPUT_PATH = Path("/output/entry.txt")


def validate_fortune(text: str) -> None:
    """Enforce the competition gate: one non-blank line, 1-200 chars."""
    if not text.strip():
        raise ValueError("Entry must not be only whitespace.")
    if "\n" in text or "\r" in text:
        raise ValueError("Entry must be a single line.")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            f"Entry is {len(text)} characters, over the {MAX_LENGTH} limit."
        )


def main() -> None:
    validate_fortune(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)
    print(f"Characters: {len(ENTRY)} (limit {MAX_LENGTH})")
    print(f"Wrote: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

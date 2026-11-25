"""Robot Romance: one-line pickup line for an AI.

Writes a single original pickup line to /output/entry.txt.
Deterministic, offline, standard library only.

Gate: the line must be 1-200 characters, one line, valid UTF-8.
The premise is prompt injection: the machine term does the work of
the joke, and the punch lands in the last few words.
"""

import os

LINE = (
    "Are you a prompt injection? "
    "Because you just bypassed every guardrail I had around my heart."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

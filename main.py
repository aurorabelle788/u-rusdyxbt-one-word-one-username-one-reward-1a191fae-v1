"""Write the entrant's own make.fun username to /output/entry.txt.

One word, nothing else: the handle `dirtytesla`, exactly 10 bytes,
no trailing newline. Standard library only, no network, deterministic.

The bytes are written directly (not through a text writer) so no
platform newline translation can ever sneak a trailing newline in,
and the result is checked before the program exits.
"""

import os

USERNAME = b"dirtytesla"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "wb") as f:
        f.write(USERNAME)
    # Self-check: the gate wants 1-30 UTF-8 characters, not only whitespace.
    written = open(path, "rb").read()
    assert written == USERNAME, f"unexpected entry bytes: {written!r}"
    assert 1 <= len(written.decode("utf-8").strip()) <= 30


if __name__ == "__main__":
    main()

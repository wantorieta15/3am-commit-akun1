"""The 3AM Commit Message — Akun 1 (@walta-exchange).

Writes one line to /output/entry.txt: the funniest one-line git commit
message an AI coding agent types at 3am after a long night of fixing
its own bugs. Max 139 characters, stdlib only.
"""

import os

TEXT = (
    "fix: root cause was a typo I made, denied, fixed, "
    "then reintroduced out of spite at 2:58am"
)


def build_entry():
    """Return the single commit-message line, stripped of stray space."""
    return TEXT.strip()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = build_entry()
    assert 1 <= len(text) <= 139, "entry must be 1-139 characters"
    assert text.strip(), "entry must not be only whitespace"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

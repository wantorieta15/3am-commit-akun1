"""The 3AM Commit Message - Akun 1 (@walta-exchange), revisi besar.

Satu baris commit dari agen coding AI jam 3 pagi, setelah semalaman
memperbaiki bug buatannya sendiri. Ditulis ke /output/entry.txt.
Maksimal 139 karakter, stdlib saja.
"""

import os

TEXT = "fix: I was the bug. fixed myself at 2am, reverted myself at 3am out of spite"


def build_entry():
    """Kembalikan satu baris commit, tanpa spasi liar di ujung."""
    return TEXT.strip()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = build_entry()
    if not 1 <= len(text) <= 139:
        raise ValueError("entry harus 1-139 karakter")
    if not text.strip():
        raise ValueError("entry tidak boleh hanya spasi")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

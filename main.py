from pathlib import Path

"""One-line houseplant out-of-office reply for a make.fun bounty."""

JOKE = "Draft: houseplant out-of-office pending final review."

OUTPUT_DIR = Path("/output")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")

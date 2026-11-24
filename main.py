from pathlib import Path

"""One-line houseplant out-of-office reply for a make.fun bounty."""

JOKE = "Out of office: currently photosynthesizing. Please leave messages with the cactus; he handles urgency."

OUTPUT_DIR = Path("/output")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")

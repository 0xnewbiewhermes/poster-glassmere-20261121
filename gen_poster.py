from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
img = Image.open(ROOT / "assets" / "glassmere-art.jpg").convert("RGB")
img = img.resize((1024, 1024), Image.Resampling.LANCZOS)
img.save(ROOT / "entry.png", format="JPEG", quality=90, subsampling=0, optimize=True, progressive=False)

import io
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
img = Image.open(ROOT / "assets" / "glassmere-art.jpg").convert("RGB")
img = img.resize((1024, 1024), Image.Resampling.LANCZOS)
MAX_TARGET = 950_000
MAX_HARD = 1_048_576


def encode(q: int) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=q, subsampling=0, optimize=True, progressive=False)
    return buf.getvalue()


data, chosen = b"", 80
for chosen in range(95, 79, -1):
    data = encode(chosen)
    if len(data) <= MAX_TARGET:
        break

out = ROOT / "entry.png"
out.write_bytes(data)

raw = out.read_bytes()
assert raw[:3] == b"\xff\xd8\xff", "bad JPEG start"
assert raw[-2:] == b"\xff\xd9", "bad JPEG end"
with Image.open(out) as chk:
    assert chk.size == (1024, 1024), chk.size
assert len(raw) <= MAX_HARD
assert encode(chosen) == raw, "encoding is not deterministic"
print(f"quality={chosen} size={len(raw)}")

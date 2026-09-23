"""Turn the untouched downloads in raw/ into the files the page serves.

Run once after changing anything in raw/:  python tools/prepare_assets.py

- Photographs become webp at the size they are shown, never upscaled.
- The Bulk SMS banner carries the old site's lettering in its left half, so
  only the right half is kept.
- Client logos arrive with a 2px grey frame baked into every file; it is cut
  off so the tiles can draw their own hairline.
- The logo SVG is copied as is, plus a light version for the dark footer and
  the chevron mark on its own for the favicon.
"""
import pathlib
import re

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
SITE = ROOT / "site"
IMG = SITE / "assets" / "img"
CLI = SITE / "assets" / "clients"
IMG.mkdir(parents=True, exist_ok=True)
CLI.mkdir(parents=True, exist_ok=True)


def rgb(im):
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        bg.alpha_composite(im)
        return bg.convert("RGB")
    return im.convert("RGB")


def crop_ratio(im, ratio, fx=0.5, fy=0.5):
    """Largest crop of `ratio` (w/h), its centre at fractions fx, fy."""
    w, h = im.size
    if w / h > ratio:
        nw = round(h * ratio)
        x = round((w - nw) * fx)
        return im.crop((x, 0, x + nw, h))
    nh = round(w / ratio)
    y = round((h - nh) * fy)
    return im.crop((0, y, w, y + nh))


def save(im, name, width, q=80):
    im = rgb(im)
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(IMG / name, "WEBP", quality=q, method=6)
    print(f"{name:28s} {im.width}x{im.height}")


def open_raw(p):
    return Image.open(RAW / p)


# ---- hero: a glowing teal polyhedron over a black mirror floor, by
#      Rostislav Uzunov on Unsplash (Unsplash License: free for commercial
#      use; credited in the footer anyway).
#      In the original the shape sits dead centre and fills most of the
#      height, so at hero size it ran under the header and into the headline.
#      The frame's edges are a flat near-black, so the canvas is extended
#      instead: more ground on the left and above, a little cropped off the
#      right. That shrinks the shape and moves it into the right half. The
#      seams are feathered so the extension cannot be seen. ----
def extend(im, canvas, at, feather=320):
    """Paste `im` onto a canvas of its own edge colour at `at`, fading its
    left and top edges into that ground over `feather` pixels."""
    ground = (11, 13, 12)
    out = Image.new("RGB", canvas, ground)
    w, h = im.size
    mask = Image.new("L", (w, h), 255)
    px = mask.load()
    for x in range(feather):
        v = round(255 * (x / feather) ** 1.5)
        for y in range(h):
            px[x, y] = min(px[x, y], v)
    for y in range(feather):
        v = round(255 * (y / feather) ** 1.5)
        for x in range(w):
            px[x, y] = min(px[x, y], v)
    out.paste(im, at, mask)
    return out


im = open_raw("unsplash-teal-polyhedron-rostislavuznv.jpg").convert("RGB")
# 16:10 canvas 3913 x 2446: the shape's centre lands at ~68% across, its top
# ~30% down (the photo sits on the canvas floor), so it clears a 72px header and a left-aligned headline
save(extend(im, (3913, 2446), (861, 2446 - 2160)), "hero.webp", 2400, q=84)

# ---- about: the team at the desk ----
save(crop_ratio(open_raw("solution.jpg"), 16 / 9, fy=0.45), "team.webp", 1280)

# ---- the SMS band: the right half of the old Bulk SMS banner, 8:5.
#      The banners carry the service name burned into their left half. ----
im = open_raw("7-1.jpg")
w, h = im.size
save(crop_ratio(im.crop((round(w * 0.5), 0, w, h)), 8 / 5), "s-sms.webp", 1120)

# ---- product logos: square artwork on white ----
products = {
    "p-media.webp": "Cyan-Media1.jpg",
    "p-realworld.webp": "Cyan-Real-World1.jpg",
    "p-hr.webp": "CyanHRPayrollnew.jpg",
    "p-edu.webp": "Educyan1.jpg",
    "p-glitz.webp": "WhatsApp-Image-2020-05-21-at-11.20.29.jpeg",
    "p-wheels.webp": "WhatsApp-Image-2020-05-21-at-11.20.31.jpeg",
    "p-medi.webp": "WhatsApp-Image-2020-05-21-at-11.20.41.jpeg",
    "p-auto.webp": "ato.jpg",
    "p-logistics.webp": "logistics.jpg",
    "p-smartshop.webp": "smartshop.jpg",
    "p-traco.webp": "trading.jpg",
}
def whiten(im, floor=236):
    """Several product JPEGs sit on an off-white (#F4F4F4-ish) ground that
    shows as a grey box inside the white card. Anything that light is
    ground, not artwork, so it goes to pure white."""
    im = im.convert("RGB")
    mask = im.convert("L").point(lambda v: 255 if v >= floor else 0)
    im.paste((255, 255, 255), mask=mask)
    return im


for name, src in products.items():
    # CMYK sources need the conversion before webp will take them
    save(whiten(open_raw(src)), name, 640, q=86)

# ---- client logos: only the forty the two rows show. raw/clients holds
#      all 101 from the old Our Clients page; swap names in ROW_A / ROW_B
#      in content.py and re-run to change which appear. ----
import sys
sys.path.insert(0, str(ROOT / "tools"))
from content import ROW_A, ROW_B  # noqa: E402
n = 0
for p in sorted((RAW / "clients").iterdir()):
    if p.stem not in ROW_A + ROW_B:
        continue
    im = rgb(Image.open(p))
    w, h = im.size
    im = im.crop((3, 3, w - 3, h - 3))
    im.save(CLI / (p.stem + ".webp"), "WEBP", quality=88, method=6)
    n += 1
print(n, "client logos")

# ---- logo ----
svg = (RAW / "2-1.svg").read_text(encoding="utf-8")
(SITE / "assets" / "logo.svg").write_text(svg, encoding="utf-8")
# the small "for IT systems co." paths carry no class and fall back to the
# root fill, so the light version sets one there as well as recolouring greys
light = svg.replace("#58595b", "#DCE7EA").replace("#666766", "#DCE7EA")
light = light.replace("<svg ", '<svg fill="#DCE7EA" ', 1)
(SITE / "assets" / "logo-light.svg").write_text(light, encoding="utf-8")
# the chevron: the last group in the file
style = re.search(r"<defs>.*?</defs>", svg, re.S).group(0)
groups = re.findall(r"<g>\s*(<path class=\"cls-1\".*?)</g>", svg, re.S)
mark = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 18 98 112">{style}<g>{groups[-1]}</g></svg>'
(SITE / "assets" / "mark.svg").write_text(mark, encoding="utf-8")
print("logos written")

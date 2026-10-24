"""design_kit.py — render2 için görsel hazırlık ve ortak parçalar."""
import hashlib, os, random
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CACHE = "/tmp/prep"
os.makedirs(CACHE, exist_ok=True)


def _hex(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def prep(name, crop=(0, 0, 1, 1), size=(1080, 1350), gray=False, contrast=1.0, bright=1.0,
         sat=1.0, duo=None, grain=0, sharpen=True, flip=False):
    """Kareyi kırp → hedef boyuta büyüt (Lanczos) → keskinleştir → isteğe bağlı çift ton + gren.
    duo=("#000000", "#ffe500") siyahtan renge çift ton. Döner: mutlak dosya yolu."""
    key = hashlib.md5(repr((name, crop, size, gray, contrast, bright, sat, duo, grain, sharpen, flip)).encode()).hexdigest()[:12]
    out = os.path.join(CACHE, f"{name}_{key}.jpg")
    if os.path.exists(out):
        return out
    src = None
    for d in ("assets/stills", "assets"):
        for ext in ("", ".jpg", ".png"):
            p = os.path.join(REPO, d, name + ext)
            if os.path.isfile(p):
                src = p
                break
        if src:
            break
    if not src:
        raise FileNotFoundError(name)
    im = Image.open(src).convert("RGB")
    w, h = im.size
    x0, y0, x1, y1 = crop
    im = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    # hedef orana göre merkezden kırp
    tw, th = size
    r_t = tw / th
    cw, ch = im.size
    if cw / ch > r_t:
        nw = int(ch * r_t)
        im = im.crop(((cw - nw) // 2, 0, (cw - nw) // 2 + nw, ch))
    else:
        nh = int(cw / r_t)
        im = im.crop((0, (ch - nh) // 2, cw, (ch - nh) // 2 + nh))
    if flip:
        im = ImageOps.mirror(im)
    im = im.resize(size, Image.LANCZOS)
    if sharpen:
        im = im.filter(ImageFilter.UnsharpMask(radius=2.2, percent=110, threshold=2))
    if gray or duo:
        im = ImageOps.grayscale(im)
        im = ImageOps.autocontrast(im, cutoff=1)
    if contrast != 1.0:
        im = ImageEnhance.Contrast(im).enhance(contrast)
    if bright != 1.0:
        im = ImageEnhance.Brightness(im).enhance(bright)
    if duo:
        im = ImageOps.colorize(ImageOps.grayscale(im), black=_hex(duo[0]), white=_hex(duo[1]), mid=_hex(duo[2]) if len(duo) > 2 else None)
    elif sat != 1.0 and not gray:
        im = ImageEnhance.Color(im).enhance(sat)
    if im.mode != "RGB":
        im = im.convert("RGB")
    if grain:
        rnd = random.Random(7)
        noise = Image.effect_noise(size, 40).convert("L")
        noise = ImageEnhance.Contrast(noise).enhance(1.2)
        n = Image.merge("RGB", (noise, noise, noise))
        im = Image.blend(im, ImageChops.overlay(im, n), min(1, grain / 40))
    im.save(out, quality=94)
    return out


def logo(name="white", x=0, y=0, w=110, z=9, op=1, rot=0):
    d = {"type": "logo", "name": name, "x": x, "y": y, "w": w, "z": z, "op": op}
    if rot:
        d["rot"] = rot
    return d


def handle(x, y, color="#fff", size=26, align="left", w=400, z=9, op=0.9, ls=3):
    return {"type": "txt", "html": "@derecefilm", "font": "oswald", "size": size, "weight": 500, "color": color,
            "x": x, "y": y, "w": w, "align": align, "ls": ls, "z": z, "op": op, "upper": True}


def swipe(x, y, color="#fff", w=300, align="right", z=9, size=24):
    return {"type": "txt", "html": "KAYDIR →", "font": "oswald", "size": size, "weight": 500, "color": color,
            "x": x, "y": y, "w": w, "align": align, "ls": 4, "z": z}


def stripes(x, y, w, h, c1="#ffe500", c2="#111", step=34, ang=-45, z=5, rot=0):
    return {"type": "box", "x": x, "y": y, "w": w, "h": h, "z": z, "rot": rot,
            "css": f"background:repeating-linear-gradient({ang}deg,{c1} 0 {step}px,{c2} {step}px {step*2}px)"}


def img(src, x, y, w, h, z=1, **kw):
    d = {"type": "img", "src": src, "x": x, "y": y, "w": w, "h": h, "z": z}
    d.update(kw)
    return d


def txt(html, x, y, w, size=40, font="inter", color="#fff", z=5, **kw):
    d = {"type": "txt", "html": html, "x": x, "y": y, "w": w, "size": size, "font": font, "color": color, "z": z}
    d.update(kw)
    return d


def box(x, y, w, h, bg, z=2, **kw):
    d = {"type": "box", "x": x, "y": y, "w": w, "h": h, "bg": bg, "z": z}
    d.update(kw)
    return d

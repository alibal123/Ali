"""Kesilmiş (arka planı silinmiş) PNG figürler: assets/cutouts/<ad>.png (rembg ile bir kez üretilir, depoya işlenir)."""
import hashlib, os
from PIL import Image, ImageChops, ImageEnhance, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CUT_DIR = os.path.join(REPO, "assets", "cutouts")
OUT = "/tmp/fig"
os.makedirs(CUT_DIR, exist_ok=True)
os.makedirs(OUT, exist_ok=True)
_sess = None


def cutout(name):
    """name: 'knivesout_2' (assets/stills/w_<name>.jpg) → RGBA"""
    p = os.path.join(CUT_DIR, f"{name}.png")
    if not os.path.exists(p):
        global _sess
        from rembg import remove, new_session
        _sess = _sess or new_session("u2net")
        src = Image.open(os.path.join(REPO, "assets", "stills", f"w_{name}.jpg")).convert("RGB")
        remove(src, session=_sess).save(p)
    return Image.open(p).convert("RGBA")


def _bbox(im, thr=70):
    a = im.split()[3].point(lambda v: 255 if v > thr else 0)
    return a.getbbox()


def _tone(im, gray=False, contrast=1.0, sat=1.0, warm=0.0):
    rgb, a = im.convert("RGB"), im.split()[3]
    if gray:
        rgb = rgb.convert("L").convert("RGB")
    if contrast != 1.0:
        rgb = ImageEnhance.Contrast(rgb).enhance(contrast)
    if sat != 1.0 and not gray:
        rgb = ImageEnhance.Color(rgb).enhance(sat)
    if warm:
        rgb = Image.blend(rgb, ImageChops.multiply(rgb, Image.new("RGB", rgb.size, (255, 226, 190))), warm)
    out = rgb.convert("RGBA")
    out.putalpha(a)
    return out


def figure(name, max_w, max_h, gray=False, contrast=1.05, sat=1.05, bottom_trim=0.0, part=None):
    """Figürü sınırlarına kırp, kutuya sığdır. Döner: (yol, w, h)."""
    im = cutout(name)
    x0, y0, x1, y1 = _bbox(im)
    y1 = int(y1 - (y1 - y0) * bottom_trim)
    im = im.crop((x0, y0, x1, y1))
    if part:
        im = im.crop((int(im.width * part[0]), 0, int(im.width * part[1]), im.height))
    s = min(max_w / im.width, max_h / im.height)
    w, h = int(im.width * s), int(im.height * s)
    im = im.resize((w, h), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 80, 2))
    im = _tone(im, gray, contrast, sat)
    key = hashlib.md5(repr((name, max_w, max_h, gray, contrast, sat, bottom_trim, part)).encode()).hexdigest()[:10]
    p = os.path.join(OUT, f"fig_{name}_{key}.png")
    im.save(p)
    return p, w, h


def pop_frame(name, fw, fh, ext=0.14, warm=0.18, center=None):
    """Çerçeve içindeki fotoğraf + çerçeve üstüne taşan figür.
    Döner: dict(frame=jpg yolu, pop=png yolu, pop_dy=çerçeve üstüne taşma (px, pozitif), pop_h)"""
    src = Image.open(os.path.join(REPO, "assets", "stills", f"w_{name}.jpg")).convert("RGB")
    cut = cutout(name)
    x0, y0, x1, y1 = _bbox(cut)
    bh = y1 - y0
    top = y0 + int(bh * ext)                       # çerçeve penceresi başlangıcı: kafa biraz kesilir
    wh = min(src.height - top, int(src.width / (fw / fh)))
    ww = int(wh * fw / fh)
    cx = center if center is not None else (x0 + x1) // 2
    wx0 = max(0, min(src.width - ww, cx - ww // 2))
    box_ = (wx0, top, wx0 + ww, top + wh)
    s = fw / ww
    frame = src.crop(box_).resize((fw, fh), Image.LANCZOS)
    frame = Image.blend(frame, ImageChops.multiply(frame, Image.new("RGB", frame.size, (255, 226, 190))), warm)
    pop_src = cut.crop((wx0, y0, wx0 + ww, top + wh))
    pop = _tone(pop_src.resize((fw, int(pop_src.height * s)), Image.LANCZOS), warm=warm)
    key = hashlib.md5(repr((name, fw, fh, ext, warm, center)).encode()).hexdigest()[:10]
    fp, pp = os.path.join(OUT, f"frm_{name}_{key}.jpg"), os.path.join(OUT, f"pop_{name}_{key}.png")
    frame.save(fp, quality=94)
    pop.save(pp)
    return {"frame": fp, "pop": pp, "pop_dy": int((top - y0) * s), "pop_h": pop.height}

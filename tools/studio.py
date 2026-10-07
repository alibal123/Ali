"""derecefilm tasarım stüdyosu — her gönderinin kendi tasarım dili olsun diye.

render.py tek bir görsel sistem kullanır; studio.py ise her gönderiye özel HTML/CSS ile çalışır.
Kullanım:  python3 tools/studio.py specs/studio/<id>.py

Gönderi dosyası (Python) şunları tanımlar:
  ID       : "2026-10-12_kultur_kavusamayan-asiklar"   → posts/<ID>/
  FONTS    : ["cormorant-garamond/500.css", ...]       → tools/node_modules/@fontsource altından
  CSS      : bu gönderiye özel stil
  SLIDES   : [html, html, ...]  (her biri 1080×1350 bir slayt gövdesi)
  CAPTION  : açıklama metni
Yardımcılar: img("ad.jpg") → depo içi görselin file:// adresi; GRAIN → film greni SVG'si.
Taşma kontrolü: metin kutusuna data-fit ekle; taşarsa uyarı basılır.
Türkçe büyük harf: text-transform:uppercase kullanılan yerde İngilizce adları lang='en' ile sar (yoksa i → İ olur).

Fontlar (tek sefer):
  npm i --prefix tools @fontsource/{oswald,inter,playfair-display,courier-prime,dm-serif-display,cormorant-garamond,caveat,\
    archivo-narrow,libre-caslon-text,josefin-sans,old-standard-tt,abril-fatface,cinzel,ibm-plex-mono,space-grotesk,\
    barlow-condensed,fraunces,archivo-black,inter-tight,lobster,anton,eb-garamond,caveat-brush,kalam}
  (Hepsini TEK komutta kur; npm --no-save ile parça parça kurmak öncekileri siler.)
"""
import importlib.util, os, sys
from playwright.sync_api import sync_playwright
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
FS = f"file://{HERE}/node_modules/@fontsource"
STILLS = os.path.join(REPO, "assets", "stills")


def img(name):
    p = name if os.path.isabs(name) else os.path.join(STILLS, name)
    if not os.path.exists(p):
        raise FileNotFoundError(p)
    return "file://" + p


GRAIN = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 1.2 -0.2'/></filter>"
         "<rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")

BASE = """*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden}
.cover-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
"""


def load(path):
    spec = importlib.util.spec_from_file_location("post", path)
    m = importlib.util.module_from_spec(spec)
    sys.modules["studio"] = sys.modules[__name__]
    spec.loader.exec_module(m)
    return m


def render(path):
    m = load(path)
    out = os.path.join(REPO, "posts", m.ID)
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f.endswith(".jpg"):
            os.remove(os.path.join(out, f))
    fonts = "".join(f"@import url('{FS}/{f}');" for f in m.FONTS)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, body in enumerate(m.SLIDES, 1):
            html = f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{fonts}{BASE}{m.CSS}</style></head><body>{body}</body></html>"
            tmp = os.path.join(out, "_tmp.html")
            open(tmp, "w", encoding="utf-8").write(html)
            pg.goto("file://" + tmp)
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(250)
            over = pg.evaluate("""() => [...document.querySelectorAll('[data-fit]')]
                .filter(e => e.scrollHeight > e.clientHeight + 2 || e.scrollWidth > e.clientWidth + 2)
                .map(e => e.className)""")
            if over:
                print(f"  ! slayt {i}: metin taşıyor → {over}")
            png = os.path.join(out, f"{i:02d}.png")
            pg.screenshot(path=png)
            Image.open(png).convert("RGB").save(os.path.join(out, f"{i:02d}.jpg"), quality=93, subsampling=0)
            os.remove(png)
            os.remove(tmp)
        b.close()
    open(os.path.join(out, "caption.txt"), "w", encoding="utf-8").write(m.CAPTION.strip() + "\n")
    print(f"{m.ID}: {len(m.SLIDES)} slayt")


if __name__ == "__main__":
    for a in sys.argv[1:]:
        render(a)

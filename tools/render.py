"""derecefilm karusel tasarım motoru.

Kullanım:
    python3 tools/render.py specs/<gonderi>.json

Spec JSON dosyası bir gönderiyi tanımlar ve posts/<id>/ klasörüne 1080x1350 JPG + caption.txt üretir.
Gereksinimler (tek sefer):  pip install playwright pillow  ·  npm i --prefix tools @fontsource/oswald @fontsource/inter @fontsource/playfair-display
Emoji için sistemde 'Noto Color Emoji' fontu olmalı.

Spec şeması:
{
  "id": "2026-10-06_film_prisoners",          # klasör adı
  "theme": "red" | "cyan" | "lime" | "orange", # vurgu rengi
  "pill": "FİLM",                              # sağ üst etiket: LİSTE / FİLM / BELGESEL / OYUN / RADAR
  "caption": "…açıklama metni…",
  "stills_dir": "/yol/sahneler",               # opsiyonel; slaytlardaki "img" bu klasöre göre
  "slides": [ {"type": ..., "img": "dosya.jpg", "blur": 0, ...}, ... ]
}
Slayt tipleri (metinlerde <em>…</em> başlıkta, <b>…</b> büyük metinde vurgu rengi verir):
  cover   : kick, h1 (html), sub
  film    : n (0 = numarasız), title, meta, konu, why
  big     : lab, html
  bullets : lab, items [3 madde]
  rows    : lab, pairs [[etiket, değer], …], extra (html, opsiyonel)
  warn    : lab, title, sub
  emoji   : lab, emoji, hint
  cta     : q (html), chips [..]
"img" verilmezse slayt fotoğrafsız (koyu zemin) çizilir. "blur": 10–22 arası bulanıklık (oyun sorularında cevabı saklamak için).
"""
import html, json, os, sys
from playwright.sync_api import sync_playwright
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
FS = f"file://{HERE}/node_modules/@fontsource"

THEMES = {
    "red": ("#e8364f", "rgba(232,54,79,.22)"),
    "orange": ("#e8364f", "rgba(232,120,54,.20)"),
    "cyan": ("#3fd0e0", "rgba(63,208,224,.18)"),
    "lime": ("#c8e64a", "rgba(200,230,74,.16)"),
}

NOISE = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/></filter>"
         "<rect width='100%25' height='100%25' filter='url(%23n)' opacity='.55'/></svg>")

CSS = f"""
@import url('{FS}/oswald/500.css'); @import url('{FS}/oswald/700.css');
@import url('{FS}/inter/400.css'); @import url('{FS}/inter/600.css');
@import url('{FS}/playfair-display/400-italic.css'); @import url('{FS}/playfair-display/700-italic.css');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;background:#0b0b0c}}
body{{font-family:Inter,sans-serif;color:#f2efe9;position:relative;overflow:hidden}}
.glow{{position:absolute;inset:0;background:radial-gradient(900px 700px at 85% 5%, var(--a2), transparent 60%),radial-gradient(700px 600px at 0% 100%, rgba(255,255,255,.04), transparent 60%)}}
.noise{{position:absolute;inset:0;background:url("{NOISE}");opacity:.09;mix-blend-mode:overlay}}
.ph{{position:absolute;top:0;left:0;width:1080px;height:800px;background-size:cover;background-position:center}}
.ph::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,11,12,.55) 0%,rgba(11,11,12,.05) 18%,rgba(11,11,12,.15) 45%,rgba(11,11,12,.85) 80%,#0b0b0c 100%)}}
body.hasph .main{{justify-content:flex-end;padding-bottom:40px}}
body.hasph .glow{{opacity:.5}}
.frame{{position:absolute;inset:0;padding:78px 84px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.brand{{font-family:Oswald;font-weight:500;letter-spacing:.32em;font-size:24px;color:#cfcac2}}
.pill{{font-family:Oswald;font-weight:500;font-size:22px;letter-spacing:.22em;color:#0b0b0c;background:var(--a);padding:8px 18px 9px;border-radius:40px}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.bot{{display:flex;justify-content:space-between;align-items:center;font-family:Oswald;font-size:24px;letter-spacing:.14em;color:#8e8a84}}
.bot b{{color:var(--a);font-weight:500}}
.kick{{font-family:Oswald;font-weight:500;font-size:32px;letter-spacing:.1em;color:var(--a);margin-bottom:34px}}
.h1{{font-family:Oswald;font-weight:700;font-size:112px;line-height:1.1;text-transform:uppercase;letter-spacing:-.005em}}
.h1 em{{font-style:normal;color:var(--a)}}
.sub{{font-family:'Playfair Display';font-style:italic;font-size:44px;line-height:1.3;color:#d9d4cc;margin-top:44px;max-width:860px}}
.num{{font-family:Oswald;font-weight:700;font-size:190px;line-height:.8;color:transparent;-webkit-text-stroke:2px var(--a);margin-bottom:30px}}
.title{{font-family:Oswald;font-weight:700;font-size:104px;line-height:1;text-transform:uppercase}}
.meta{{font-family:Oswald;font-weight:500;font-size:28px;letter-spacing:.14em;color:#9d978f;margin:22px 0 46px;text-transform:uppercase}}
.p{{font-size:37px;line-height:1.48;color:#e6e1d9}}
.why{{margin-top:44px;border-left:5px solid var(--a);padding:6px 0 6px 30px;font-family:'Playfair Display';font-style:italic;font-size:38px;line-height:1.4;color:#f2efe9}}
.big{{font-family:'Playfair Display';font-style:italic;font-size:62px;line-height:1.3}}
.big b{{font-style:italic;color:var(--a);font-weight:700}}
.lab{{font-family:Oswald;font-weight:500;font-size:28px;letter-spacing:.24em;color:var(--a);margin-bottom:30px;text-transform:uppercase}}
ul{{list-style:none}} li{{font-size:38px;line-height:1.42;padding:26px 0;border-top:1px solid #2a2927;display:flex;gap:28px}}
li:last-child{{border-bottom:1px solid #2a2927}} li span{{font-family:Oswald;color:var(--a);font-size:34px;min-width:52px}}
.rows div{{display:flex;justify-content:space-between;align-items:baseline;padding:28px 0;border-top:1px solid #2a2927;font-size:38px}}
.rows div:last-child{{border-bottom:1px solid #2a2927}}
.rows span{{font-family:Oswald;font-weight:500;font-size:26px;letter-spacing:.2em;color:#8e8a84;text-transform:uppercase}}
.emoji{{font-size:210px;line-height:1.1;letter-spacing:.06em;margin:20px 0 50px;font-family:'Noto Color Emoji'}}
.hint{{font-family:'Playfair Display';font-style:italic;font-size:42px;color:#bdb7ae}}
.warn{{font-family:Oswald;font-weight:700;font-size:92px;line-height:1.02;text-transform:uppercase}}
.cta{{display:flex;gap:18px;margin-top:60px;flex-wrap:wrap}}
.cta div{{border:2px solid var(--a);color:var(--a);border-radius:60px;padding:16px 30px;font-family:Oswald;font-size:30px;letter-spacing:.12em;text-transform:uppercase}}
"""

e = html.escape


def body_for(s):
    t = s["type"]
    if t == "cover":
        return f'<div class="kick">{e(s["kick"])}</div><div class="h1">{s["h1"]}</div><div class="sub">{e(s["sub"])}</div>'
    if t == "film":
        num = f'<div class="num">{int(s["n"]):02d}</div>' if s.get("n") else ""
        return (f'{num}<div class="title" lang="en">{e(s["title"])}</div><div class="meta" lang="en">{e(s["meta"])}</div>'
                f'<div class="p">{e(s["konu"])}</div><div class="why">{e(s["why"])}</div>')
    if t == "big":
        return f'<div class="lab">{e(s["lab"])}</div><div class="big">{s["html"]}</div>'
    if t == "bullets":
        lis = "".join(f"<li><span>{i+1:02d}</span><div>{e(x)}</div></li>" for i, x in enumerate(s["items"]))
        return f'<div class="lab">{e(s["lab"])}</div><ul>{lis}</ul>'
    if t == "rows":
        r = "".join(f"<div><span>{e(a)}</span>{e(b)}</div>" for a, b in s["pairs"])
        extra = s.get("extra", "")
        if extra and not extra.lstrip().startswith("<"):
            extra = f'<div class="sub">{e(extra)}</div>'
        return f'<div class="lab" lang="en">{e(s["lab"])}</div><div class="rows">{r}</div>{extra}'
    if t == "warn":
        return f'<div class="lab">{e(s["lab"])}</div><div class="warn">{e(s["title"])}</div><div class="sub">{e(s["sub"])}</div>'
    if t == "emoji":
        return f'<div class="lab">{e(s["lab"])}</div><div class="emoji">{s["emoji"]}</div><div class="hint">{e(s["hint"])}</div>'
    if t == "cta":
        chips = "".join(f"<div>{e(x)}</div>" for x in s.get("chips", []))
        return f'<div class="lab">Sıra sende</div><div class="big">{s["q"]}</div><div class="cta">{chips}</div>'
    raise ValueError(f"bilinmeyen slayt tipi: {t}")


def page(spec, s, idx, total):
    accent, glow = THEMES[spec.get("theme", "red")]
    ph = ""
    img = s.get("img")
    if img:
        path = img if os.path.isabs(img) else os.path.join(spec.get("stills_dir", ""), img)
        if os.path.exists(path):
            blur = s.get("blur", 0)
            f = f"filter:blur({blur}px) brightness(.8);transform:scale(1.08);" if blur else ""
            ph = f'<div class="ph" style="background-image:url(file://{path});{f}"></div>'
    swipe = "<b>KAYDIR →</b>" if idx < total else ""
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{'hasph' if ph else ''}" style="--a:{accent};--a2:{glow}">{ph}<div class="glow"></div><div class="noise"></div>
<div class="frame"><div class="top"><div class="brand">DERECE FİLM</div><div class="pill">{e(spec['pill'])}</div></div>
<div class="main">{body_for(s)}</div>
<div class="bot"><div>@derecefilm &nbsp;·&nbsp; {idx:02d}/{total:02d}</div><div>{swipe}</div></div>
</div></body></html>"""


def render(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    out = os.path.join(REPO, "posts", spec["id"])
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f.endswith(".jpg"):
            os.remove(os.path.join(out, f))
    slides = spec["slides"]
    assert 2 <= len(slides) <= 10, "karusel 2–10 slayt olmalı"
    tmp = os.path.join(out, "_tmp.html")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, s in enumerate(slides, 1):
            open(tmp, "w", encoding="utf-8").write(page(spec, s, i, len(slides)))
            pg.goto("file://" + tmp, wait_until="networkidle")
            pg.evaluate("document.fonts.ready.then(()=>1)")
            pg.wait_for_timeout(150)
            png = os.path.join(out, f"{i:02d}.png")
            pg.screenshot(path=png)
            Image.open(png).convert("RGB").save(png[:-4] + ".jpg", quality=93, subsampling=0)
            os.remove(png)
        b.close()
    os.remove(tmp)
    open(os.path.join(out, "caption.txt"), "w", encoding="utf-8").write(spec["caption"].strip() + "\n")
    print(f"{spec['id']}: {len(slides)} slayt → {out}")


if __name__ == "__main__":
    for a in sys.argv[1:]:
        render(a)

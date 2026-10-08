"""derecefilm karusel tasarım motoru (v2).

Kullanım:  python3 tools/render.py specs/<gonderi>.json [--preview]

Gereksinimler (tek sefer):
  pip install playwright pillow
  npm i --prefix tools @fontsource/oswald @fontsource/inter @fontsource/playfair-display @fontsource/courier-prime @fontsource/dm-serif-display
  Emoji için sistemde 'Noto Color Emoji' fontu.

SPEC
{
  "id": "2026-10-06_liste_turk",        klasör adı (posts/<id>/)
  "theme": "amber",                      varsayılan vurgu (THEMES anahtarı ya da #hex)
  "pill": "LİSTE",
  "caption": "...",
  "stills_dir": "assets/stills",         göreli ise depo köküne göre
  "slides": [ {...}, ... ]               2–10 slayt
}

HER SLAYTTA OPSİYONEL
  accent : bu slayta özel vurgu rengi (tema adı ya da #hex)  → aynı gönderide renk çeşitliliği
  bg     : "dark" (varsayılan) | "light" (krem kâğıt) | "solid" (vurgu rengi zemin)
  img, blur, pos ("center 30%" gibi background-position)

SLAYT TİPLERİ
  cover     : kick, h1 (html, <em> vurgu), sub
  film      : n, title, meta, konu, why
  big       : lab, html            (kısa, ≤ 25 kelime; serif italik büyük)
  text      : lab, html            (uzun metin; okunaklı düz yazı, <i> ve <b> vurgu)
  bullets   : lab, items
  rows      : lab, pairs, extra
  warn      : lab, title, sub
  emoji     : lab, emoji, hint
  cta       : q (html), chips
  collage   : kick, h1 (html), sub, imgs [ {img, label} ×4–6 ]
  pair      : n, a {img, title, meta}, b {img, title, meta}, why
  fullphoto : img, kick, title, line           (fotoğraf tam sayfa)
  file      : lab, title, pairs, stamp, note   (dava dosyası; açık zeminde iyi durur)
  bars      : lab, title, items [ {name, year, a, b} ], a_label, b_label, note
  crop      : n, img, zoom (2–4), focus ("x% y%"), hint   (kırpılmış yakın plan bulmaca)
  reveal    : lab, items [ {img, n, answer, meta} ×2–5 ]  (cevap ızgarası)
  number    : big (ör. "1986"), lab, html
"""
import html, json, os, sys
from playwright.sync_api import sync_playwright
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
FS = f"file://{HERE}/node_modules/@fontsource"

THEMES = {
    "red": "#e8364f", "orange": "#ff7a3d", "amber": "#f2b33d", "lime": "#c8e64a",
    "teal": "#2fd3b5", "cyan": "#3fd0e0", "sky": "#6aa8ff", "violet": "#9b7bff",
    "pink": "#ff5fa2", "coral": "#ff6f61", "cream": "#efe6d6",
}


def col(c):
    return THEMES.get(c, c) if c else None


def rgba(hexc, a):
    h = hexc.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{a})"


NOISE = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/></filter>"
         "<rect width='100%25' height='100%25' filter='url(%23n)' opacity='.55'/></svg>")

CSS = f"""
@import url('{FS}/oswald/500.css'); @import url('{FS}/oswald/700.css');
@import url('{FS}/inter/400.css'); @import url('{FS}/inter/500.css'); @import url('{FS}/inter/600.css'); @import url('{FS}/inter/700.css');
@import url('{FS}/playfair-display/400-italic.css'); @import url('{FS}/playfair-display/700-italic.css'); @import url('{FS}/playfair-display/800-italic.css');
@import url('{FS}/courier-prime/400.css'); @import url('{FS}/courier-prime/700.css');
@import url('{FS}/dm-serif-display/400.css');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px}}
body{{--bg:#0b0b0c;--fg:#f2efe9;--mut:#9d978f;--line:#2a2927;background:var(--bg);font-family:Inter,sans-serif;color:var(--fg);position:relative;overflow:hidden}}
body.light{{--bg:#efe6d6;--fg:#1a1714;--mut:#6d6458;--line:#cdbfa8}}
body.solid{{--bg:var(--a);--fg:#111;--mut:rgba(0,0,0,.6);--line:rgba(0,0,0,.2)}}
.glow{{position:absolute;inset:0;background:radial-gradient(900px 700px at 85% 5%, var(--a2), transparent 60%),radial-gradient(700px 600px at 0% 100%, rgba(255,255,255,.04), transparent 60%)}}
body.light .glow,body.solid .glow{{display:none}}
.noise{{position:absolute;inset:0;background:url("{NOISE}");opacity:.09;mix-blend-mode:overlay}}
body.light .noise{{opacity:.16;mix-blend-mode:multiply}}
.ph{{position:absolute;top:0;left:0;width:1080px;height:820px;background-size:cover;background-position:center}}
.ph::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,11,12,.6) 0%,rgba(11,11,12,.05) 16%,rgba(11,11,12,.2) 42%,rgba(11,11,12,.92) 76%,#0b0b0c 100%)}}
.ph.full{{height:1350px}}
.ph.full::after{{background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 18%,rgba(0,0,0,0) 48%,rgba(0,0,0,.88) 82%,rgba(0,0,0,.96) 100%)}}
body.hasph .main{{justify-content:flex-end;padding-bottom:30px}}
body.hasph .glow{{opacity:.45}}
body.hasph .main *{{text-shadow:0 2px 18px rgba(0,0,0,.55)}}
.frame{{position:absolute;inset:0;padding:78px 84px 70px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:2}}
.brand{{font-family:Oswald;font-weight:500;letter-spacing:.32em;font-size:24px;color:var(--fg);opacity:.8}}
.pill{{font-family:Oswald;font-weight:500;font-size:22px;letter-spacing:.22em;color:#0b0b0c;background:var(--a);padding:8px 18px 9px;border-radius:40px}}
body.solid .pill{{background:#111;color:var(--a)}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2}}
.bot{{display:flex;justify-content:space-between;align-items:center;font-family:Oswald;font-size:24px;letter-spacing:.14em;color:var(--mut);position:relative;z-index:2}}
.bot b{{color:var(--a);font-weight:500}}
body.solid .bot b{{color:#111}}
body.light .bot b{{color:var(--ad)}}
.kick{{font-family:Oswald;font-weight:500;font-size:32px;letter-spacing:.1em;color:var(--a);margin-bottom:30px}}
body.light .kick,body.light .lab{{color:var(--ad)}}
body.solid .kick,body.solid .lab{{color:#111}}
body.solid .big b,body.solid .txt b,body.solid .sub b{{color:#fff}}
body.hasph .kick{{color:#fff;display:inline-block;align-self:flex-start;background:rgba(0,0,0,.45);padding:6px 16px;border-radius:8px;border-left:5px solid var(--a)}}
.h1{{font-family:Oswald;font-weight:700;font-size:112px;line-height:1.08;text-transform:uppercase;letter-spacing:-.005em}}
.h1 em{{font-style:normal;color:var(--a)}}
body.light .h1 em{{color:var(--ad)}}
.sub{{font-family:Inter;font-weight:500;font-size:38px;line-height:1.4;color:var(--fg);opacity:.86;margin-top:38px;max-width:880px}}
.sub i{{font-family:'Playfair Display';font-weight:700}}
.num{{font-family:Oswald;font-weight:700;font-size:190px;line-height:.8;color:transparent;-webkit-text-stroke:2px var(--a);margin-bottom:30px}}
.title{{font-family:Oswald;font-weight:700;font-size:104px;line-height:1;text-transform:uppercase}}
.meta{{font-family:Oswald;font-weight:500;font-size:28px;letter-spacing:.14em;color:var(--mut);margin:22px 0 40px;text-transform:uppercase}}
body.hasph .meta{{color:#cfc8bd}}
.p{{font-size:37px;line-height:1.48;color:var(--fg);opacity:.92}}
.why{{margin-top:40px;border-left:6px solid var(--a);padding:4px 0 4px 30px;font-family:Inter;font-weight:600;font-size:36px;line-height:1.42;color:var(--fg)}}
.big{{font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:66px;line-height:1.24}}
.big b{{color:var(--a);font-weight:800}}
body.light .big b,body.light .txt b{{color:var(--ad)}}
.txt{{font-family:Inter;font-weight:500;font-size:46px;line-height:1.38}}
.txt b{{color:var(--a);font-weight:700}}
.txt i{{font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:1.06em}}
.lab{{font-family:Oswald;font-weight:500;font-size:28px;letter-spacing:.24em;color:var(--a);margin-bottom:30px;text-transform:uppercase}}
ul{{list-style:none}} li{{font-size:38px;line-height:1.42;padding:24px 0;border-top:1px solid var(--line);display:flex;gap:28px}}
li:last-child{{border-bottom:1px solid var(--line)}} li span{{font-family:Oswald;color:var(--a);font-size:34px;min-width:52px}}
.rows div{{display:flex;justify-content:space-between;align-items:baseline;gap:30px;padding:26px 0;border-top:1px solid var(--line);font-size:38px}}
.rows div:last-child{{border-bottom:1px solid var(--line)}}
.rows span{{font-family:Oswald;font-weight:500;font-size:26px;letter-spacing:.2em;color:var(--mut);text-transform:uppercase;white-space:nowrap}}
.emoji{{font-size:210px;line-height:1.1;letter-spacing:.06em;margin:20px 0 50px;font-family:'Noto Color Emoji'}}
.hint{{font-family:Inter;font-weight:500;font-size:40px;line-height:1.35;color:var(--fg);opacity:.85}}
.warn{{font-family:Oswald;font-weight:700;font-size:92px;line-height:1.02;text-transform:uppercase}}
.cta{{display:flex;gap:18px;margin-top:56px;flex-wrap:wrap}}
.cta div{{border:2px solid var(--a);color:var(--a);border-radius:60px;padding:16px 30px;font-family:Oswald;font-size:30px;letter-spacing:.12em;text-transform:uppercase}}
body.light .cta div{{border-color:var(--ad);color:var(--ad)}}
body.solid .cta div{{border-color:#111;color:#111}}
/* kolaj */
.grid{{display:grid;gap:14px;margin:6px 0 40px}}
.grid.g4{{grid-template-columns:1fr 1fr}} .grid.g5{{grid-template-columns:repeat(6,1fr)}}
.grid.g5 .cell:nth-child(-n+2){{grid-column:span 3}} .grid.g5 .cell:nth-child(n+3){{grid-column:span 2}}
.grid.g6{{grid-template-columns:1fr 1fr 1fr}}
.cell{{position:relative;height:250px;border-radius:14px;overflow:hidden;background-size:cover;background-position:center}}
.grid.g5 .cell:nth-child(-n+2){{height:290px}}
.cell b{{position:absolute;left:14px;bottom:12px;font-family:Oswald;font-weight:500;font-size:24px;letter-spacing:.08em;color:#fff;text-transform:uppercase;text-shadow:0 2px 10px rgba(0,0,0,.8)}}
.cell::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 55%,rgba(0,0,0,.7))}}
.cell b{{z-index:1}}
/* eşleştirme */
.pairbox{{display:flex;flex-direction:column;gap:18px}}
.pcard{{position:relative;height:360px;border-radius:18px;overflow:hidden;background-size:cover;background-position:center}}
.pcard::after{{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.82) 0%,rgba(0,0,0,.35) 55%,rgba(0,0,0,0) 100%)}}
.pcard .in{{position:absolute;left:34px;bottom:30px;z-index:1}}
.pcard .tag{{display:inline-block;font-family:Oswald;font-weight:500;font-size:22px;letter-spacing:.2em;padding:6px 14px;border-radius:30px;margin-bottom:14px}}
.pcard.a .tag{{background:rgba(255,255,255,.16);color:#fff}}
.pcard.b .tag{{background:var(--a);color:#111}}
.pcard .t{{font-family:Oswald;font-weight:700;font-size:62px;line-height:1;text-transform:uppercase;color:#fff}}
.pcard .m{{font-family:Oswald;font-size:24px;letter-spacing:.14em;color:#d9d2c6;margin-top:10px;text-transform:uppercase}}
.arrow{{font-family:Oswald;font-size:40px;color:var(--a);text-align:center;margin:-6px 0}}
.pwhy{{margin-top:30px;font-family:Inter;font-weight:500;font-size:36px;line-height:1.42}}
.pwhy b{{color:var(--a)}}
/* tam fotoğraf */
.fp-title{{font-family:'DM Serif Display';font-size:120px;line-height:1;letter-spacing:-.01em}}
.fp-line{{font-family:Inter;font-weight:500;font-size:40px;line-height:1.38;margin-top:26px;max-width:880px;opacity:.92}}
/* dava dosyası */
.file{{border:3px solid var(--fg);padding:44px 46px 40px;position:relative;font-family:'Courier Prime',monospace}}
.file .ft{{font-family:'Courier Prime';font-weight:700;font-size:56px;line-height:1.1;margin-bottom:26px;text-transform:uppercase;padding-right:300px}}
.file .fr{{display:flex;gap:22px;font-size:33px;line-height:1.35;padding:14px 0;border-top:2px dashed var(--line)}}
.file .fr span{{min-width:270px;color:var(--mut);text-transform:uppercase;font-size:26px;padding-top:5px;letter-spacing:.06em}}
.file .stamp{{position:absolute;right:-24px;top:-34px;transform:rotate(-9deg);border:6px solid var(--ad);color:var(--ad);font-family:Oswald;font-weight:700;font-size:44px;letter-spacing:.12em;padding:6px 22px;background:var(--bg)}}
.file .fn{{margin-top:22px;font-size:30px;line-height:1.4;color:var(--fg)}}
/* puan grafiği */
.btitle{{font-family:Oswald;font-weight:700;font-size:70px;line-height:1.05;text-transform:uppercase;margin-bottom:22px}}
.legend{{display:flex;gap:30px;font-family:Oswald;font-size:24px;letter-spacing:.14em;margin-bottom:24px;text-transform:uppercase}}
.legend i{{display:inline-block;width:22px;height:22px;border-radius:5px;vertical-align:-3px;margin-right:10px}}
.bitem{{padding:18px 0;border-top:1px solid var(--line)}}
.bname{{font-family:Oswald;font-weight:500;font-size:32px;letter-spacing:.04em;margin-bottom:10px;text-transform:uppercase}}
.bname small{{color:var(--mut);font-size:24px;margin-left:10px}}
.brow{{display:flex;align-items:center;gap:16px;margin:6px 0}}
.bar{{height:26px;border-radius:13px}}
.bval{{font-family:Oswald;font-size:28px;min-width:120px}}
.bnote{{margin-top:22px;font-size:28px;line-height:1.4;color:var(--mut)}}
/* kırpılmış bulmaca */
.cropwin{{width:912px;height:700px;border-radius:24px;overflow:hidden;position:relative;border:4px solid var(--a);margin-bottom:34px}}
.cropwin div{{position:absolute;inset:0;background-size:cover}}
.qn{{font-family:Oswald;font-weight:700;font-size:44px;letter-spacing:.06em;color:var(--a);margin-bottom:16px;text-transform:uppercase}}
/* cevap ızgarası */
.rv{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.rv .r{{position:relative;height:300px;border-radius:14px;overflow:hidden;background-size:cover;background-position:center}}
.rv .r:last-child:nth-child(odd){{grid-column:span 2}}
.rv .r::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,.85))}}
.rv .r div{{position:absolute;left:18px;bottom:14px;z-index:1}}
.rv .r em{{font-style:normal;font-family:Oswald;font-weight:700;font-size:26px;color:var(--a)}}
.rv .r strong{{display:block;font-family:Oswald;font-weight:700;font-size:38px;line-height:1.05;color:#fff;text-transform:uppercase}}
.rv .r small{{font-family:Oswald;font-size:20px;letter-spacing:.12em;color:#d9d2c6;text-transform:uppercase}}
/* sayı */
.bignum{{font-family:'DM Serif Display';font-size:300px;line-height:.9;color:var(--a);letter-spacing:-.02em}}
body.light .bignum{{color:var(--ad)}}
/* --- v3 yerleşimleri: aynı yazı tipleri, farklı kompozisyon --- */
/* afiş: üstte çerçeveli kare, ortalanmış başlık */
.poster{{text-align:center;display:flex;flex-direction:column;align-items:center}}
.poster .pimg{{width:912px;height:640px;background-size:cover;background-position:center;border:2px solid rgba(255,255,255,.18);box-shadow:0 30px 80px rgba(0,0,0,.6)}}
.poster .pk{{font-family:Oswald;font-weight:500;font-size:26px;letter-spacing:.4em;color:var(--a);margin:44px 0 10px}}
.poster .pt{{font-family:'DM Serif Display';font-size:150px;line-height:.95}}
.poster .pm{{font-family:Oswald;font-size:26px;letter-spacing:.3em;color:var(--mut);margin-top:16px;text-transform:uppercase}}
.poster .pl{{font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:40px;line-height:1.3;margin-top:22px;max-width:820px}}
/* film şeridi */
.strip{{display:flex;flex-direction:column;gap:0;margin-bottom:34px;background:#000;padding:0 46px;border-radius:6px;position:relative}}
.strip::before,.strip::after{{content:'';position:absolute;top:0;bottom:0;width:30px;background:radial-gradient(circle at 15px 22px,#efe6d6 7px,transparent 8px) 0 0/30px 44px repeat-y}}
.strip::before{{left:8px}} .strip::after{{right:8px}}
.sfr{{height:228px;margin:12px 0;background-size:cover;background-position:center;position:relative}}
.sfr b{{position:absolute;left:16px;top:10px;font-family:Oswald;font-weight:700;font-size:40px;color:var(--a);text-shadow:0 2px 10px rgba(0,0,0,.8)}}
/* çerçeve: eğik fotoğraf + kutulu başlık */
.frm{{position:relative;width:912px;height:760px;margin-bottom:20px}}
.frm .fi{{position:absolute;inset:0;background-size:cover;background-position:center;border:16px solid var(--a);transform:rotate(-2.2deg);box-shadow:0 30px 70px rgba(0,0,0,.6)}}
.frm .fb{{position:absolute;left:-10px;bottom:-40px;background:#0b0b0c;padding:22px 30px 26px;max-width:860px;transform:rotate(1deg)}}
.frm .fb .h1{{font-size:86px}}
/* menü kartı */
.card{{align-self:center;width:840px;background:#efe6d6;color:#1a1714;padding:56px 60px 50px;text-align:center;outline:3px solid #efe6d6;outline-offset:12px;box-shadow:0 40px 90px rgba(0,0,0,.7)}}
.card .ck{{font-family:Oswald;font-weight:500;font-size:24px;letter-spacing:.4em;color:var(--ad)}}
.card .ct{{font-family:'DM Serif Display';font-size:104px;line-height:1;margin:18px 0 8px}}
.card .cs{{font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:32px;color:#6d6458}}
.card hr{{border:0;border-top:2px solid #1a1714;width:120px;margin:30px auto}}
.card .ci{{font-family:'Playfair Display';font-style:italic;font-weight:400;font-size:34px;line-height:1.75}}
.card .ci b{{font-family:Oswald;font-style:normal;font-weight:500;font-size:22px;letter-spacing:.24em;color:var(--ad);margin-right:14px}}
.card .cf{{font-family:Oswald;font-size:24px;letter-spacing:.24em;margin-top:30px;color:#6d6458;text-transform:uppercase}}
/* mozaik bulmaca */
.mos{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:40px}}
.mos div{{height:262px;border-radius:10px;background-repeat:no-repeat;position:relative}}
.mos div::after{{content:'?';position:absolute;right:12px;bottom:4px;font-family:Oswald;font-weight:700;font-size:40px;color:var(--a);text-shadow:0 2px 8px #000}}
/* en-boy oranları */
.ratio{{position:relative;width:912px;height:666px;margin-bottom:46px}}
.ratio .rimg{{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.55}}
.ratio .rb{{position:absolute;left:0;right:0;border:4px solid;display:flex;justify-content:flex-end;align-items:flex-start}}
.ratio .rb span{{font-family:Oswald;font-weight:700;font-size:34px;padding:4px 14px;color:#0b0b0c}}
/* letterbox */
.lbx{{width:912px;height:560px;background:#000;display:flex;align-items:center;justify-content:center;margin-bottom:34px;position:relative}}
.lbx div{{width:912px;background-size:cover;background-position:center}}
.lbx span{{position:absolute;right:16px;top:12px;font-family:Oswald;font-weight:700;font-size:40px;color:var(--a)}}
/* alıntı */
body.quote .main{{justify-content:center;text-align:center;align-items:center}}
.qm{{font-family:'DM Serif Display';font-size:260px;line-height:.6;color:var(--a);height:120px}}
.qt{{font-family:'Playfair Display';font-style:italic;font-weight:800;font-size:96px;line-height:1.12;max-width:900px}}
.qb{{font-family:Oswald;font-size:28px;letter-spacing:.3em;color:var(--a);margin-top:40px;text-transform:uppercase}}
/* ikiye bölünmüş */
.sp{{position:absolute;left:0;top:0;width:500px;height:1350px;background-size:cover;background-position:center}}
.sp::after{{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent 70%,rgba(11,11,12,.9))}}
body.split .frame{{padding-left:560px}}
body.split .brand{{font-size:20px;letter-spacing:.24em;white-space:nowrap}}
.brand{{white-space:nowrap}}
body.split .h1{{font-size:96px}}
body.split .sub{{font-size:34px}}
body.cardpage .main{{justify-content:center}}
/* tipografik dizin */
.idx{{border-top:3px solid #111}}
.idx div{{display:flex;align-items:baseline;gap:24px;padding:13px 0;border-bottom:2px solid rgba(0,0,0,.25)}}
.idx b{{font-family:Oswald;font-weight:700;font-size:30px;min-width:48px}}
.idx span{{font-family:Oswald;font-weight:700;font-size:62px;line-height:1;text-transform:uppercase;flex:1}}
.idx small{{font-family:Oswald;font-size:28px;letter-spacing:.1em}}
"""

e = html.escape


def stills_path(spec, img):
    if not img:
        return None
    if os.path.isabs(img):
        return img
    base = spec.get("stills_dir", "assets/stills")
    if not os.path.isabs(base):
        base = os.path.join(REPO, base)
    p = os.path.join(base, img)
    return p if os.path.exists(p) else None


def url(spec, img):
    p = stills_path(spec, img)
    return f"file://{p}" if p else ""


def body_for(spec, s):
    t = s["type"]
    if t == "cover":
        return f'<div class="kick">{e(s["kick"])}</div><div class="h1">{s["h1"]}</div><div class="sub">{s.get("sub","")}</div>'
    if t == "film":
        num = f'<div class="num">{int(s["n"]):02d}</div>' if s.get("n") else ""
        return (f'{num}<div class="title" lang="en">{e(s["title"])}</div><div class="meta" lang="en">{e(s["meta"])}</div>'
                f'<div class="p">{e(s["konu"])}</div><div class="why">{e(s["why"])}</div>')
    if t == "big":
        return f'<div class="lab">{e(s["lab"])}</div><div class="big">{s["html"]}</div>'
    if t == "text":
        return f'<div class="lab">{e(s["lab"])}</div><div class="txt">{s["html"]}</div>'
    if t == "bullets":
        lis = "".join(f"<li><span>{i+1:02d}</span><div>{e(x)}</div></li>" for i, x in enumerate(s["items"]))
        return f'<div class="lab">{e(s["lab"])}</div><ul>{lis}</ul>'
    if t == "rows":
        r = "".join(f"<div><span>{e(a)}</span><div style='text-align:right'>{e(b)}</div></div>" for a, b in s["pairs"])
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
        return f'<div class="lab">{e(s.get("lab","Sıra sende"))}</div><div class="big">{s["q"]}</div><div class="cta">{chips}</div>'
    if t == "collage":
        n = len(s["imgs"])
        cells = "".join(f'<div class="cell" style="background-image:url({url(spec,c["img"])})"><b lang="en">{e(c.get("label",""))}</b></div>' for c in s["imgs"])
        return (f'<div class="kick">{e(s["kick"])}</div><div class="grid g{n}">{cells}</div>'
                f'<div class="h1" style="font-size:96px">{s["h1"]}</div><div class="sub" style="margin-top:26px">{s.get("sub","")}</div>')
    if t == "pair":
        a, b = s["a"], s["b"]
        lab = s.get("lab") or f"Eşleşme {int(s.get('n', 1)):02d}"
        num = f'<div class="lab">{e(lab)}</div>'
        return (f'{num}<div class="pairbox">'
                f'<div class="pcard a" style="background-image:url({url(spec,a["img"])});background-position:{a.get("pos","center")}"><div class="in"><span class="tag">SEVDİYSEN</span><div class="t" lang="en">{e(a["title"])}</div><div class="m" lang="en">{e(a["meta"])}</div></div></div>'
                f'<div class="arrow">↓</div>'
                f'<div class="pcard b" style="background-image:url({url(spec,b["img"])});background-position:{b.get("pos","center")}"><div class="in"><span class="tag">BUNU İZLE</span><div class="t" lang="en">{e(b["title"])}</div><div class="m" lang="en">{e(b["meta"])}</div></div></div>'
                f'</div><div class="pwhy">{s["why"]}</div>')
    if t == "fullphoto":
        return (f'<div class="kick">{e(s.get("kick",""))}</div><div class="fp-title" lang="en">{s["title"]}</div>'
                f'<div class="fp-line">{s.get("line","")}</div>')
    if t == "file":
        rows = "".join(f'<div class="fr"><span>{e(a)}</span><div>{e(b)}</div></div>' for a, b in s["pairs"])
        stamp = f'<div class="stamp">{e(s["stamp"])}</div>' if s.get("stamp") else ""
        note = f'<div class="fn">{s["note"]}</div>' if s.get("note") else ""
        return f'<div class="lab">{e(s["lab"])}</div><div class="file">{stamp}<div class="ft" lang="en">{e(s["title"])}</div>{rows}{note}</div>'
    if t == "bars":
        ca, cb = col(s.get("a_color", "amber")), col(s.get("b_color", "sky"))
        items = ""
        for it in s["items"]:
            items += (f'<div class="bitem"><div class="bname" lang="en">{e(it["name"])}<small>{e(str(it.get("year","")))}</small></div>'
                      f'<div class="brow"><div class="bar" style="width:{int(it["a"]*7.2)}px;background:{ca}"></div><div class="bval">{e(it["a_txt"])}</div></div>'
                      f'<div class="brow"><div class="bar" style="width:{int(it["b"]*7.2)}px;background:{cb}"></div><div class="bval">{e(it["b_txt"])}</div></div></div>')
        legend = f'<div class="legend"><span><i style="background:{ca}"></i>{e(s["a_label"])}</span><span><i style="background:{cb}"></i>{e(s["b_label"])}</span></div>'
        note = f'<div class="bnote">{e(s["note"])}</div>' if s.get("note") else ""
        return f'<div class="lab">{e(s["lab"])}</div><div class="btitle">{s["title"]}</div>{legend}{items}{note}'
    if t == "crop":
        z = s.get("zoom", 3)
        return (f'<div class="qn">{e(s["lab"])}</div>'
                f'<div class="cropwin"><div style="background-image:url({url(spec,s["img"])});background-size:{int(z*100)}% auto;background-position:{s.get("focus","50% 50%")}"></div></div>'
                f'<div class="hint">{e(s["hint"])}</div>')
    if t == "reveal":
        cells = "".join(f'<div class="r" style="background-image:url({url(spec,it["img"])})"><div><em>{e(it["n"])}</em><strong lang="en">{e(it["answer"])}</strong><small lang="en">{e(it["meta"])}</small></div></div>' for it in s["items"])
        return f'<div class="lab">{e(s["lab"])}</div><div class="rv">{cells}</div>'
    if t == "number":
        return f'<div class="lab">{e(s["lab"])}</div><div class="bignum">{e(s["big"])}</div><div class="txt" style="margin-top:20px">{s["html"]}</div>'
    if t == "poster":
        return (f'<div class="poster"><div class="pimg" style="background-image:url({url(spec,s["pimg"])});background-position:{s.get("ppos","center")}"></div>'
                f'<div class="pk">{e(s.get("kick",""))}</div><div class="pt" lang="{s.get("lang","en")}">{s["title"]}</div>'
                f'<div class="pm" lang="en">{e(s.get("meta",""))}</div><div class="pl">{s.get("line","")}</div></div>')
    if t == "strip":
        fr = "".join(f'<div class="sfr" style="background-image:url({url(spec,c["img"])});background-position:{c.get("pos","center")}"><b>{i+1:02d}</b></div>' for i, c in enumerate(s["imgs"]))
        return f'<div class="strip">{fr}</div><div class="h1" style="font-size:92px">{s["h1"]}</div><div class="sub" style="margin-top:22px">{s.get("sub","")}</div>'
    if t == "frame":
        return (f'<div class="kick">{e(s.get("kick",""))}</div><div class="frm"><div class="fi" style="background-image:url({url(spec,s["fimg"])});background-position:{s.get("fpos","center")}"></div>'
                f'<div class="fb"><div class="h1">{s["h1"]}</div></div></div><div class="sub" style="margin-top:70px">{s.get("sub","")}</div>')
    if t == "card":
        items = "".join(f'<div><b>{e(a)}</b>{e(b)}</div>' for a, b in s["items"])
        return (f'<div class="card"><div class="ck">{e(s.get("kick",""))}</div><div class="ct" lang="en">{e(s["title"])}</div>'
                f'<div class="cs">{s.get("sub","")}</div><hr><div class="ci">{items}</div><div class="cf">{e(s.get("foot",""))}</div></div>')
    if t == "mosaic":
        tiles = "".join(f'<div style="background-image:url({url(spec,c["img"])});background-size:{int(c.get("zoom",3)*100)}% auto;background-position:{c.get("focus","50% 50%")}"></div>' for c in s["tiles"])
        return f'<div class="kick">{e(s.get("kick",""))}</div><div class="mos">{tiles}</div><div class="h1" style="font-size:96px">{s["h1"]}</div><div class="sub" style="margin-top:22px">{s.get("sub","")}</div>'
    if t == "ratio":
        boxes = ""
        for r, c in s["ratios"]:
            h = int(912 / float(r))
            boxes += f'<div class="rb" style="top:{(666-h)//2}px;height:{h}px;border-color:{col(c)}"><span style="background:{col(c)}">{e(r)}:1</span></div>'
        return (f'<div class="kick">{e(s.get("kick",""))}</div><div class="ratio"><div class="rimg" style="background-image:url({url(spec,s["rimg"])})"></div>{boxes}</div>'
                f'<div class="h1" style="font-size:88px">{s["h1"]}</div><div class="sub" style="margin-top:22px">{s.get("sub","")}</div>')
    if t == "letterbox":
        r = float(s["ratio"]); w, h = 912, int(912 / r)
        if h > 560:
            h, w = 560, int(560 * r)
        return (f'<div class="lab">{e(s["lab"])} &nbsp;·&nbsp; {e(s["ratio"])}:1</div><div class="lbx"><div style="width:{w}px;height:{h}px;background-image:url({url(spec,s["limg"])});background-position:{s.get("lpos","center")}"></div></div>'
                f'<div class="txt" style="font-size:40px">{s["html"]}</div>')
    if t == "quote":
        return f'<div class="qm">“</div><div class="qt">{s["q"]}</div><div class="qb" lang="en">{e(s.get("by",""))}</div><div class="sub" style="margin-top:30px">{s.get("sub","")}</div>'
    if t == "split":
        return f'<div class="kick">{e(s.get("kick",""))}</div><div class="h1" lang="{s.get("lang","en")}" style="font-size:{s.get("h1size",96)}px">{s["h1"]}</div><div class="meta" lang="en" style="margin:20px 0 0">{e(s.get("meta",""))}</div><div class="sub">{s.get("sub","")}</div>'
    if t == "index":
        rows = "".join(f'<div><b>{i+1:02d}</b><span lang="en">{e(a)}</span><small>{e(b)}</small></div>' for i, (a, b) in enumerate(s["items"]))
        return f'<div class="kick">{e(s.get("kick",""))}</div><div class="h1" style="font-size:84px;margin-bottom:34px">{s["h1"]}</div><div class="idx">{rows}</div>'
    raise ValueError(f"bilinmeyen slayt tipi: {t}")


def page(spec, s, idx, total):
    accent = col(s.get("accent")) or col(spec.get("theme", "red"))
    accent_dark = col(s.get("accent_dark")) or "#b8432f"
    bg = s.get("bg", "dark")
    ph = ""
    extra_cls = ""
    if s["type"] == "split":
        p = stills_path(spec, s["img"])
        ph = f'<div class="sp" style="background-image:url(file://{p});background-position:{s.get("pos","center")}"></div>'
        extra_cls = "split"
    elif s.get("img") and s["type"] not in ("crop", "pair", "collage", "reveal"):
        p = stills_path(spec, s["img"])
        if p:
            blur = s.get("blur", 0)
            gray = "grayscale(1) " if s.get("gray") else ""
            f = f"filter:{gray}blur({blur}px) brightness(.8);transform:scale(1.08);" if (blur or gray) else ""
            full = " full" if s["type"] in ("fullphoto", "quote", "card") else ""
            ph = f'<div class="ph{full}" style="background-image:url(file://{p});background-position:{s.get("pos","center")};{f}"></div>'
    if s["type"] == "quote":
        extra_cls = "quote"
    if s["type"] == "card":
        extra_cls = "cardpage"
    hp = "hasph" if ph and s["type"] not in ("split", "card") else ""
    cls = " ".join(x for x in [bg if bg != "dark" else "", hp, extra_cls] if x)
    swipe = "<b>KAYDIR →</b>" if idx < total else ""
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{cls}" style="--a:{accent};--a2:{rgba(accent,.2)};--ad:{accent_dark}">{ph}<div class="glow"></div><div class="noise"></div>
<div class="frame"><div class="top"><div class="brand">DERECE FİLM</div><div class="pill">{e(spec['pill'])}</div></div>
<div class="main">{body_for(spec, s)}</div>
<div class="bot"><div>@derecefilm &nbsp;·&nbsp; {idx:02d}/{total:02d}</div><div>{swipe}</div></div>
</div></body></html>"""


def render(spec_path, preview=False):
    spec = json.load(open(spec_path, encoding="utf-8"))
    out = os.path.join(REPO, "posts", spec["id"])
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f.endswith(".jpg"):
            os.remove(os.path.join(out, f))
    slides = spec["slides"]
    assert 2 <= len(slides) <= 10, "karusel 2–10 slayt olmalı"
    for s in slides:
        for k in ("img",):
            if s.get(k) and not stills_path(spec, s[k]):
                print(f"UYARI: görsel bulunamadı: {s[k]}")
    tmp = os.path.join(out, "_tmp.html")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, s in enumerate(slides, 1):
            open(tmp, "w", encoding="utf-8").write(page(spec, s, i, len(slides)))
            pg.goto("file://" + tmp, wait_until="networkidle")
            pg.evaluate("document.fonts.ready.then(()=>1)")
            pg.wait_for_timeout(200)
            over = pg.evaluate("(()=>{const m=document.querySelector('.main');return m.scrollHeight>m.clientHeight+4})()")
            if over:
                print(f"UYARI: {spec['id']} slayt {i} metni taşıyor")
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
        if not a.startswith("--"):
            render(a)

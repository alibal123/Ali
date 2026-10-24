#!/usr/bin/env python3
"""render2.py — serbest yerleşimli (mutlak konumlu) gönderi motoru.

Kullanım:  python3 tools/render2.py specs2/<dosya>.json
Çıktı:     posts/<id>/01.jpg … + caption.txt

Spec:
{ "id": "...", "caption": "...", "slides": [ {"bg": "#111" | {"css": "..."}, "els": [ ... ]} ] }

Eleman tipleri (hepsinde x,y,w,h piksel, rot derece, z, op=opaklık, css=ek stil):
  img   : src (assets/stills/<ad>.jpg), fit(cover), pos("50% 50%"), filter, blend, radius, border, shadow, clip
  txt   : html, font(oswald|anton|inter|serif|playfair|abril|caveat|marker|typewriter|archivo|grotesk),
          size, weight, color, lh, ls, align, upper, stroke("2px #fff"), shadow, bg, pad, rad
  box   : bg (renk/gradient), border, radius
  logo  : name (white|black|red|yellow|lime|cyan|bluepurple|greenblue), w
"""
import json, os, sys, html as H
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
FS = f"file://{HERE}/node_modules/@fontsource"
W, HGT = 1080, 1350

FONTS = {
    "oswald": ("Oswald", "'Oswald',sans-serif"),
    "anton": ("Anton", "'Anton',sans-serif"),
    "inter": ("Inter", "'Inter',sans-serif"),
    "serif": ("DM Serif Display", "'DM Serif Display',serif"),
    "playfair": ("Playfair Display", "'Playfair Display',serif"),
    "abril": ("Abril Fatface", "'Abril Fatface',serif"),
    "caveat": ("Caveat", "'Caveat',cursive"),
    "marker": ("Permanent Marker", "'Permanent Marker',cursive"),
    "typewriter": ("Special Elite", "'Special Elite',monospace"),
    "archivo": ("Archivo Black", "'Archivo Black',sans-serif"),
    "grotesk": ("Space Grotesk", "'Space Grotesk',sans-serif"),
}

CSS = f"""
@import url('{FS}/oswald/400.css'); @import url('{FS}/oswald/500.css'); @import url('{FS}/oswald/700.css');
@import url('{FS}/anton/400.css'); @import url('{FS}/inter/400.css'); @import url('{FS}/inter/500.css'); @import url('{FS}/inter/700.css'); @import url('{FS}/inter/900.css');
@import url('{FS}/dm-serif-display/400.css'); @import url('{FS}/playfair-display/700.css'); @import url('{FS}/playfair-display/700-italic.css');
@import url('{FS}/playfair-display/400-italic.css'); @import url('{FS}/abril-fatface/400.css'); @import url('{FS}/caveat/700.css');
@import url('{FS}/permanent-marker/400.css'); @import url('{FS}/special-elite/400.css'); @import url('{FS}/archivo-black/400.css');
@import url('{FS}/space-grotesk/500.css'); @import url('{FS}/space-grotesk/700.css');
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{HGT}px;overflow:hidden}}
body{{position:relative;-webkit-font-smoothing:antialiased}}
.e{{position:absolute}}
.t{{white-space:normal;word-break:normal;overflow-wrap:break-word}}
.t em{{font-style:normal}}
.t i{{font-style:italic}}
"""


def esc(s):
    return H.escape(str(s), quote=True)


def stills(name):
    if os.path.isabs(name) and os.path.isfile(name):
        return "file://" + name
    for ext in ("", ".jpg", ".png"):
        for d in ("assets/stills", "assets/logo", "assets"):
            p = os.path.join(REPO, d, name + ext)
            if os.path.isfile(p):
                return "file://" + p
    raise FileNotFoundError(name)


def px(v):
    return f"{v}px" if isinstance(v, (int, float)) else v


def el_html(e):
    t = e["type"]
    st = []
    for k in ("x", "y", "w", "h"):
        if k in e:
            st.append(f"{ {'x':'left','y':'top','w':'width','h':'height'}[k] }:{px(e[k])}")
    if e.get("right") is not None:
        st.append(f"right:{px(e['right'])}")
    if e.get("bottom") is not None:
        st.append(f"bottom:{px(e['bottom'])}")
    tf = []
    if e.get("rot"):
        tf.append(f"rotate({e['rot']}deg)")
    if e.get("scale"):
        tf.append(f"scale({e['scale']})")
    if tf:
        st.append("transform:" + " ".join(tf))
    st.append(f"z-index:{e.get('z', 1)}")
    if "op" in e:
        st.append(f"opacity:{e['op']}")
    if e.get("origin"):
        st.append(f"transform-origin:{e['origin']}")
    if t == "img":
        src = stills(e["src"])
        st.append(f"background-image:url('{src}');background-size:{e.get('fit','cover')};background-position:{e.get('pos','50% 50%')};background-repeat:no-repeat")
        for k, cssn in (("filter", "filter"), ("blend", "mix-blend-mode"), ("radius", "border-radius"), ("border", "border"), ("shadow", "box-shadow"), ("clip", "clip-path")):
            if e.get(k):
                st.append(f"{cssn}:{px(e[k]) if k=='radius' else e[k]}")
        if e.get("css"):
            st.append(e["css"])
        return f'<div class="e" style="{";".join(st)}"></div>'
    if t == "box":
        if e.get("bg"):
            st.append(f"background:{e['bg']}")
        for k, cssn in (("border", "border"), ("radius", "border-radius"), ("shadow", "box-shadow"), ("blend", "mix-blend-mode"), ("filter", "filter"), ("clip", "clip-path")):
            if e.get(k):
                st.append(f"{cssn}:{px(e[k]) if k=='radius' else e[k]}")
        if e.get("css"):
            st.append(e["css"])
        return f'<div class="e" style="{";".join(st)}"></div>'
    if t == "logo":
        src = stills(f"logo/{e.get('name','white')}.png") if False else "file://" + os.path.join(REPO, "assets/logo", e.get("name", "white") + ".png")
        h = e.get("h", e.get("w", 120))
        st.append(f"width:{px(e.get('w',120))};height:{px(h)};background:url('{src}') center/contain no-repeat")
        if e.get("filter"):
            st.append(f"filter:{e['filter']}")
        return f'<div class="e" style="{";".join(st)}"></div>'
    if t == "txt":
        fam = FONTS[e.get("font", "inter")][1]
        st.append(f"font-family:{fam}")
        st.append(f"font-size:{px(e.get('size',40))}")
        st.append(f"font-weight:{e.get('weight',400)}")
        st.append(f"color:{e.get('color','#fff')}")
        st.append(f"line-height:{e.get('lh',1.15)}")
        if e.get("ls") is not None:
            st.append(f"letter-spacing:{px(e['ls'])}")
        st.append(f"text-align:{e.get('align','left')}")
        if e.get("upper"):
            st.append("text-transform:uppercase")
        if e.get("stroke"):
            st.append(f"-webkit-text-stroke:{e['stroke']}")
        if e.get("fill_none"):
            st.append("-webkit-text-fill-color:transparent")
        if e.get("shadow"):
            st.append(f"text-shadow:{e['shadow']}")
        if e.get("bg"):
            st.append(f"background:{e['bg']}")
        if e.get("pad") is not None:
            st.append(f"padding:{px(e['pad'])}")
        if e.get("rad"):
            st.append(f"border-radius:{px(e['rad'])}")
        if e.get("border"):
            st.append(f"border:{e['border']}")
        if e.get("blend"):
            st.append(f"mix-blend-mode:{e['blend']}")
        if e.get("css"):
            st.append(e["css"])
        return f'<div class="e t" lang="tr" style="{";".join(st)}">{e["html"]}</div>'
    raise ValueError(t)


def slide_html(s):
    bg = s.get("bg", "#000")
    bgcss = bg if isinstance(bg, str) else bg.get("css", "#000")
    els = "".join(el_html(e) for e in s["els"])
    return f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head><body style="background:{bgcss}">{els}</body></html>'


def render(spec, outroot=None):
    out = os.path.join(outroot or os.path.join(REPO, "posts"), spec["id"])
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f[:2].isdigit() and f.endswith(".jpg"):
            os.remove(os.path.join(out, f))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": HGT})
        for i, s in enumerate(spec["slides"], 1):
            tmp = os.path.join(HERE, "_slide.html")
            open(tmp, "w").write(slide_html(s))
            pg.goto("file://" + tmp, wait_until="load")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(500)
            pg.screenshot(path=os.path.join(out, f"{i:02d}.jpg"), type="jpeg", quality=93)
        b.close()
    open(os.path.join(out, "caption.txt"), "w").write(spec["caption"].strip() + "\n")
    print(f"{spec['id']}: {len(spec['slides'])} slayt → {out}")
    return out


if __name__ == "__main__":
    render(json.load(open(sys.argv[1])))

"""Tek tasarım sistemi: sabit kenar boşluğu (72 px), tam genişlik fotoğraf, otomatik sığan yazı, sabit logo/sayfa numarası konumu."""
from common import *

M, W, H = 72, 1080, 1350


def T(html, x, y, w, h, size, font="inter", color="#000", fit=True, nowrap=False, mn=22, weight=400, lh=1.25, ls=None,
      upper=False, align="left", op=None, z=5, flex=None, bleed=False, **kw):
    css = []
    if fit:
        css.append(f"--fit:1;--h:{h};--min:{mn}")
    if nowrap:
        css.append("white-space:nowrap")
    if bleed:
        css.append("--bleed:1")
    if flex:
        css.append("display:flex;align-items:center;justify-content:" + flex)
    d = txt(html, x, y, w, size=size, font=font, color=color, z=z, weight=weight, lh=lh, h=h, align=align, css=";".join(css) + (";" if css else ""), **kw)
    if ls is not None:
        d["ls"] = ls
    if upper:
        d["upper"] = True
    if op is not None:
        d["op"] = op
    return d


def rule(x, y, w, color, op=0.2, h=2, z=3):
    return box(x, y, w, h, color, z=z, op=op)


def footer(th, i, n, on_dark=False):
    c = th["bg_ink"] if on_dark else th["ink"]
    lg = th["logo_dark"] if on_dark else th["logo"]
    return [
        T(f"{i:02d} / {n:02d}", M, 1268, 260, 34, 24, "oswald", c, fit=False, weight=500, ls=4, op=0.6),
        logo(lg, W - M - 58, 1252, 58, z=9),
    ]


def kicker(th, text, x, y, color=None, w=700):
    color = color or th["accent"]
    return [box(x, y + 14, 44, 4, color, z=4), T(text, x + 64, y, w, 34, 26, "oswald", color, fit=False, weight=500, ls=6, upper=True)]


def label(text, x, y, bg="rgba(0,0,0,.6)", color="#fff", size=24, z=8):
    w = int(len(text) * size * 0.74 + 44)
    return T(text, x, y, w, size + 24, size, "oswald", color, fit=False, weight=500, ls=4, upper=True, z=z, bg=bg, pad="10px 20px 10px 20px")


def grade(name, size, crop=(0, 0, 1, 1), **kw):
    return prep(name, crop=crop, size=size, contrast=kw.get("contrast", 1.06), sat=kw.get("sat", 1.08), grain=kw.get("grain", 5))


def mosaic(th, photos, h=640, gap=6):
    """photos: [(ad, crop)] 3–6 adet; kesin hizalı ızgara."""
    n = len(photos)
    if n == 5:
        cells = [(0, 0, 540, h // 2), (540, 0, 540, h // 2)] + [(i * 360, h // 2, 360, h // 2) for i in range(3)]
    elif n == 4:
        cells = [(0, 0, 540, h // 2), (540, 0, 540, h // 2), (0, h // 2, 540, h // 2), (540, h // 2, 540, h // 2)]
    elif n == 6:
        cells = [(c * 360, r * (h // 2), 360, h // 2) for r in range(2) for c in range(3)]
    elif n == 8:
        cells = [(c * 270, r * (h // 2), 270, h // 2) for r in range(2) for c in range(4)]
    elif n == 3:
        cells = [(0, 0, 1080, h // 2), (0, h // 2, 540, h // 2), (540, h // 2, 540, h // 2)]
    else:
        raise ValueError(n)
    els = [box(0, 0, W, h, th["bg"], z=1)]
    for (x, y, w, hh), ph in zip(cells, photos):
        nm, crop = (ph if isinstance(ph, tuple) else (ph, (0, 0, 1, 1)))
        els.append(img(grade(nm, (w - gap, hh - gap), crop), x + gap // 2, y + gap // 2, w - gap, hh - gap, z=2))
    return els


def cover_mosaic(th, photos, kick, title, sub, h=680):
    ty = h + 118
    th_h = 1190 - ty
    return {"bg": th["bg"], "els": [
        *mosaic(th, photos, h),
        *kicker(th, kick, M, h + 36),
        T(title, M, ty, W - 2 * M, th_h, 190, th["head"], th["ink"], nowrap=True, mn=64, lh=1.06, upper=th.get("upper", True)),
        T(sub, M, 1212, 700, 40, 28, "inter", th["ink"], fit=True, mn=20, weight=500, op=0.7, nowrap=True),
        logo(th["logo"], W - M - 58, 1252, 58, z=9),
    ]}


def cover_hero(th, photo, kick, title, sub, crop=(0, 0, 1, 1), scrim=0.82):
    return {"bg": "#000", "els": [
        img(grade(photo, (1080, 1350), crop, grain=9), 0, 0, W, H, z=1),
        box(0, 560, W, 790, f"linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,{scrim}))", z=2),
        *kicker(th, kick, M, 760, color="#fff"),
        T(title, M, 830, W - 2 * M, 330, 150, th["head"], "#fff", nowrap=True, mn=64, lh=1.04, upper=True),
        T(sub, M, 1200, 800, 40, 28, "inter", "#fff", weight=500, op=0.85, nowrap=True, mn=20),
        logo("white", W - M - 58, 1252, 58, z=9),
    ]}


def film_slide(th, i, n, photo, title, meta, body, crop=(0, 0, 1, 1), tag=None, ph=720, num=True, extra=None):
    els = [
        img(grade(photo, (1080, ph), crop), 0, 0, W, ph, z=1),
    ]
    if tag:
        els.append(label(tag, M, 56))
    if num:
        els += [box(M, ph - 56, 112, 112, th["accent"], z=4),
                T(f"{i:02d}", M, ph - 56, 112, 112, 60, "anton", th["on_acc"], fit=False, align="center", flex="center", lh=1.0, bleed=True)]
    els += [
        T(title, M, ph + 82, W - 2 * M, 104, 96, th["head"], th["ink"], nowrap=True, mn=44, lh=1.05, upper=th.get("upper", True)),
        T(meta, M, ph + 196, W - 2 * M, 36, 26, "oswald", th["accent_txt"], weight=500, ls=4, upper=True, nowrap=True, mn=18),
        rule(M, ph + 250, W - 2 * M, th["ink"]),
        T(body, M, ph + 276, W - 2 * M, (160 if extra else 214), 40, "inter", th["ink"], weight=500, lh=1.4, mn=26),
        *([T(extra, M, 1196, W - 2 * M, 30, 22, "oswald", th["ink"], weight=500, ls=2, upper=True, op=0.6, nowrap=True, mn=14)] if extra else []),
        *footer(th, i, n),
    ]
    return {"bg": th["bg"], "els": els}


def cta_slide(th, q, sub, chip=None):
    q_lines = q.count("<br>") + 1
    return {"bg": th["accent"], "els": [
        box(M, 150, 44, 4, th["on_acc"], z=4),
        T(q, M, 200, W - 2 * M, 640, 150, th["head"], th["on_acc"], nowrap=True, mn=60, lh=1.06, upper=th.get("upper", True)),
        T(sub, M, 900, W - 2 * M, 150, 46, "inter", th["on_acc"], weight=500, lh=1.35, mn=30),
        *([T(chip, M, 1090, int(len(chip) * 19 + 60), 56, 26, "oswald", th["accent"], fit=False, nowrap=True, weight=500, ls=4, upper=True, bg=th["on_acc"], pad="12px 22px")] if chip else []),
        logo(th["on_acc_logo"], W - M - 58, 1252, 58, z=9),
    ]}


def theme(bg, ink, accent, on_acc="#fff", head="anton", logo_light="black", upper=True, accent_txt=None, acc_logo=None):
    dark_bg = logo_light == "white"
    return dict(bg=bg, ink=ink, accent=accent, on_acc=on_acc, head=head, logo=("white" if dark_bg else "black"),
                logo_dark=("black" if dark_bg else "white"), bg_ink=("#14110f" if dark_bg else "#fff"), upper=upper,
                accent_txt=accent_txt or accent, on_acc_logo=(acc_logo or ("white" if on_acc == "#fff" else "black")))


def info_slide(th, i, n, photo, title, badge, rows, crop=(0, 0, 1, 1), tag=None, ph=None, title_lines=1):
    """Fotoğraf + rozet (tarih) + başlık + etiket/değer satırları. rows: [(etiket, değer, yükseklik)]"""
    ts_h = 104 if title_lines == 1 else 200
    if ph is None:
        ph = max(560, min(820, 1215 - (80 + ts_h + 24 + sum(r[2] for r in rows))))
    els = [img(grade(photo, (1080, ph), crop), 0, 0, W, ph, z=1)]
    if tag:
        els.append(label(tag, M, 56))
    bw = int(len(badge) * 22 + 64)
    els += [box(M, ph - 56, bw, 112, th["accent"], z=4),
            T(badge, M, ph - 56, bw, 112, 36, "anton", th["on_acc"], fit=False, align="center", flex="center", lh=1.0, ls=2, bleed=True)]
    ty = ph + 80
    els.append(T(title, M, ty, W - 2 * M, ts_h, 92, th["head"], th["ink"], nowrap=True, mn=44, lh=1.06, upper=th.get("upper", True)))
    y = ty + ts_h + 24
    for lab, val, h in rows:
        els += [rule(M, y, W - 2 * M, th["ink"]),
                T(lab, M, y + 20, 200, 30, 22, "oswald", th["accent_txt"], fit=False, weight=500, ls=4, upper=True),
                T(val, M + 230, y + 14, W - 2 * M - 230, h - 22, 34, "inter", th["ink"], weight=500, lh=1.32, mn=24)]
        y += h
    els += footer(th, i, n)
    return {"bg": th["bg"], "els": els}


def pair_slide(th, i, n, a, b, why):
    """a, b: (başlık, meta, foto). İki tam genişlik fotoğraf üst üste; aradaki şeritte yönlendirme."""
    ph = 430
    els = []
    for k, (t, m, ph_name) in enumerate((a, b)):
        y0 = 0 if k == 0 else ph + 64
        els += [img(grade(ph_name, (1080, ph)), 0, y0, W, ph, z=1),
                box(0, y0 + ph - 150, W, 150, "rgba(15,15,25,.74)", z=3),
                T("BUNU SEVDİYSEN" if k == 0 else "BUNU İZLE", M, y0 + ph - 134, 400, 26, 20, "oswald", ("#fff" if k == 0 else th["accent"]), fit=False, weight=500, ls=5, upper=True, op=(0.8 if k == 0 else 1)),
                T(t, M, y0 + ph - 84, 620, 62, 56, "anton", "#fff", nowrap=True, mn=30, lh=1.0, upper=True),
                T(m, 560, y0 + ph - 58, 450, 30, 22, "oswald", "#fff", weight=500, ls=3, upper=True, align="right", nowrap=True, mn=14, op=0.85)]
    els += [box(0, ph, W, 64, th["accent"], z=2),
            T("↓", 0, ph + 4, W, 56, 40, "anton", th["on_acc"], fit=False, align="center", lh=1.3, bleed=True),
            T(why, M, ph + 64 + ph + 34, W - 2 * M, 176, 38, "inter", th["ink"], weight=500, lh=1.38, mn=26),
            *footer(th, i, n)]
    return {"bg": th["bg"], "els": els}


def relogo(slides, pos="br", w=96, on_light="black", on_dark="white", over=None, mx=56, my=50):
    """Her slayttaki logoyu yeniden konumlandırır/renklendirir. over: {slayt_no(0'dan): logo_adı}."""
    over = over or {}
    def lum(c):
        try:
            c = c.lstrip("#"); r, g, b = (int(c[i:i + 2], 16) for i in (0, 2, 4))
            return (0.299 * r + 0.587 * g + 0.114 * b) / 255
        except Exception:
            return 0.0
    X = {"l": mx, "r": 1080 - mx - w, "c": (1080 - w) // 2}
    Y = {"t": my, "b": 1350 - my - w}
    x, y = X[pos[1]], Y[pos[0]]
    for i, s in enumerate(slides):
        s["els"] = [e for e in s["els"] if e.get("type") != "logo"]
        name = over.get(i) or (on_light if lum(s.get("bg", "#000")) > 0.55 else on_dark)
        s["els"].append(logo(name, x, y, w, z=30))
    return slides

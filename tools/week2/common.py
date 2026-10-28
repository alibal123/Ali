"""Yeni hafta (30 Ekim – 5 Kasım 2026) gönderileri için ortak yardımcılar. Logo kullanılır, 'derecefilm' yazısı kullanılmaz."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from design_kit import *  # noqa: F401,F403
import render2  # noqa: F401


def S(name, i):
    """tools/week2 sahne karesi adı (TMDB'den indirilen yazısız kareler: assets/stills/w_<ad>_<n>.jpg)"""
    return f"w_{name}_{i}"


def fit(text, w, base, factor=0.47, lo=40):
    """Anton/Oswald büyük harf için yaklaşık yazı boyutu: tek satıra sığacak en büyük boyut."""
    plain = text.replace("<br>", "")
    longest = max(len(x) for x in text.split("<br>")) if "<br>" in text else len(plain)
    return int(max(lo, min(base, w / (factor * max(1, longest)))))


def pager(i, n, x, y, color, w=200, align="left", size=26):
    return txt(f"{i:02d} / {n:02d}", x, y, w, size=size, font="oswald", weight=500, color=color, ls=4, align=align, z=9)


def cta_question(bg, ink, accent, logo_name, q_html, sub, chips=None, size=118, font="caveat", note=None):
    els = [
        txt(q_html, 70, 120, 940, size=size, font=font, weight=700, color=ink, lh=1.02, z=5, rot=-2),
        txt(sub, 70, 800, 900, size=54, font="serif", color=ink, z=5, lh=1.1),
    ]
    if note:
        els.append(txt(note, 70, 990, 900, size=34, font="oswald", weight=500, color=bg, ls=4, z=5, bg=accent, pad="10px 18px", rot=-1, upper=True))
    els.append(logo(logo_name, 800, 1030, 210, z=8))
    return {"bg": bg, "els": els}

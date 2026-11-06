"""Tesadüf (6) ve kaçış (9) — onaylı kapakların diliyle 3'er seçenek. python3 tools/seri3/kapak6.py <çıktı>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kapak2 import page, P, LOGO, EN, full
from kapak3 import T_MAIN, T_TAIL, K_MAIN, K_TAIL, ph, logo, meta
from playwright.sync_api import sync_playwright


def slogan(still, pos, big, accent, main, tail, filt="filter:grayscale(1) contrast(1.25) brightness(.85)"):
    """Onaylı 'Tek başına da olur' dili: siyah beyaz tam sayfa + dev eğik slogan."""
    return page(f"""
<div class="bg" style="{ph(still, pos, filt)}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05) 30%,rgba(0,0,0,.88) 72%)"></div>
<div class="abs" style="left:56px;right:56px;top:600px;font:italic 400 150px/0.88 Anton;color:#fff;text-transform:uppercase">{big}</div>
<div class="abs" style="left:64px;right:64px;top:1110px">
  <div style="font:700 30px/1.25 Inter;color:#fff">{main} <span style="color:{accent}">{tail}</span></div>
</div>
{logo('white')}
""", "#000")


def columns(stills, accent, main, tail, kick, date):
    """Onaylı film gecesi C'nin varyasyonu: 5 dikey sütun."""
    cols = "".join(f'<div style="flex:1;{ph(n, p)}"></div>' for n, p in stills)
    return page(f"""
<div class="abs" style="inset:0;background:#0d0d10"></div>
<div class="abs" style="left:0;right:0;top:0;height:720px;display:flex;gap:6px">{cols}</div>
<div class="abs" style="left:64px;right:64px;top:780px">
  <div class="osw" style="font-size:22px;color:{accent}">{kick}</div>
  <div style="font:400 60px/1.06 Anton;text-transform:uppercase;color:#fff;margin-top:16px">{main}</div>
  <div class="serif" style="font-size:48px;color:{accent};margin-top:12px">{tail}</div>
</div>
{meta(date + ' · KAYDIR →', '#fff')}{logo()}
""", "#0d0d10")


# ---------------------------------------------------------------- TESADÜF
def t_a():
    return slogan("chungking_1", "30% 50%", "Kaydırma.<br><span style='color:#ffe14d'>Karşılaş.</span>", "#ffe14d", T_MAIN, T_TAIL)


def t_b():
    return full("harrysally_1", "50% 50%", T_MAIN, T_TAIL, "#ffc56b", "17 KASIM", main_size=58,
                hook="tesadüf mü?", hook_style="left:64px;top:560px;font:700 italic 140px/1 'Playfair Display';color:#ffc56b;text-shadow:0 6px 30px rgba(0,0,0,.5)",
                grad="linear-gradient(180deg,rgba(14,8,4,0) 0%,rgba(14,8,4,.1) 38%,rgba(14,8,4,.9) 66%)")


def t_c():
    return columns([("amelie_4", "62% 40%"), ("chungking_1", "28% 50%"), ("harrysally_1", "48% 50%"), ("serendipity_3", "68% 50%"), ("sleepless_4", "70% 40%")],
                   "#ffc56b", T_MAIN, T_TAIL, "5 film · 5 tesadüf", "5 FİLM · 17 KASIM")


# ---------------------------------------------------------------- KAÇIŞ
def k_a():
    return slogan("romanholiday_3", "42% 40%", "Pazartesi<br><span style='color:#8fd0ff'>yok.</span>", "#8fd0ff", K_MAIN, K_TAIL,
                  filt="filter:contrast(1.2) brightness(.85)")


def k_b():
    return full("cmbyn_1", "26% 50%", K_MAIN, K_TAIL, "#ffd36b", "23 KASIM", main_size=70, tail_size=52,
                hook="sadece iki gün.", hook_style="left:64px;top:560px;font:700 italic 120px/1 'Playfair Display';color:#ffd36b;text-shadow:0 6px 30px rgba(0,0,0,.45)",
                grad="linear-gradient(180deg,rgba(10,10,4,0) 0%,rgba(10,10,4,.1) 38%,rgba(10,10,4,.9) 66%)")


def k_c():
    return columns([("romanholiday_3", "40% 40%"), ("cmbyn_1", "28% 50%"), ("mammamia_1", "35% 50%"), ("ferris_3", "80% 40%"), ("darjeeling_1", "45% 50%")],
                   "#8fd0ff", K_MAIN, K_TAIL, "Cumartesi · Pazar · 5 film", "5 FİLM · 23 KASIM")


SETS = [("06_tesaduf", [t_a, t_b, t_c]), ("09_iki-gunluk-kacis", [k_a, k_b, k_c])]

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        tmp = os.path.join(HERE, "_k.html")
        for name, fns in SETS:
            for i, fn in enumerate(fns):
                open(tmp, "w").write(fn())
                pg.goto("file://" + tmp, wait_until="load")
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(500)
                pg.screenshot(path=os.path.join(out, f"{name}_{'ABC'[i]}.jpg"), type="jpeg", quality=94)
        b.close()
    print("ok")

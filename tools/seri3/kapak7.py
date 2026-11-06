"""Tesadüf A (başlık büyütüldü) + kaçış için 3 yeni seçenek. python3 tools/seri3/kapak7.py <çıktı>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kapak2 import page, P, LOGO, EN
from kapak3 import T_MAIN, T_TAIL, K_MAIN, K_TAIL, ph, logo, meta
from playwright.sync_api import sync_playwright


def tesaduf_a():
    return page(f"""
<div class="bg" style="{ph('chungking_1', '30% 50%', 'filter:grayscale(1) contrast(1.25) brightness(.85)')}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 22%,rgba(0,0,0,.9) 62%)"></div>
<div class="abs" style="left:56px;right:56px;top:440px;font:italic 400 150px/0.88 Anton;color:#fff;text-transform:uppercase">Kaydırma.<br><span style='color:#ffe14d'>Karşılaş.</span></div>
<div class="abs" style="left:64px;right:64px;top:780px">
  <div style="font:400 60px/1.07 Anton;color:#fff;text-transform:uppercase">{T_MAIN}</div>
  <div class="serif" style="font-size:50px;line-height:1.12;color:#ffe14d;margin-top:12px">{T_TAIL}</div>
</div>
{meta('5 FİLM · 17 KASIM · KAYDIR →', '#fff')}{logo('white')}
""", "#000")


def kacis_a():  # renk bloğu: üst yarı düz deniz mavisi + dev slogan, alt yarı fotoğraf
    return page(f"""
<div class="abs" style="left:0;right:0;top:0;height:640px;background:#0a5fb4"></div>
<div class="abs" style="left:56px;top:70px;font:400 210px/0.84 Anton;color:#fff;text-transform:uppercase;letter-spacing:-.01em">Ofisten<br><span style="color:#ffd23f">kaç.</span></div>
<div class="abs" style="left:470px;top:430px;width:520px;font:600 30px/1.35 Inter;color:#d6e8ff">Cumartesi sabahı çıkış,<br>pazar akşamı dönüş.<br>Arada 5 film.</div>
<div class="abs" style="left:0;right:0;top:640px;bottom:0;{ph('mammamia_1', '38% 45%')}"></div>
<div class="abs" style="left:0;right:0;top:860px;bottom:0;background:linear-gradient(180deg,rgba(4,24,48,0),rgba(4,24,48,.92) 45%)"></div>
<div class="abs" style="left:64px;right:64px;top:960px">
  <div style="font:400 58px/1.07 Anton;color:#fff;text-transform:uppercase">{K_MAIN}</div>
  <div class="serif" style="font-size:46px;line-height:1.12;color:#ffd23f;margin-top:10px">{K_TAIL}</div>
</div>
{logo('white')}
""", "#0a5fb4")


def kacis_b():  # çift ton (lacivert/sarı) + dev "48 SAAT"
    return page(f"""
<div class="abs" style="inset:0;background:#ffcc33"></div>
<div class="abs" style="inset:0;{ph('romanholiday_3', '42% 40%', 'filter:grayscale(1) contrast(1.35) brightness(1.05)')};mix-blend-mode:multiply"></div>
<div class="abs" style="inset:0;background:#0d2c54;mix-blend-mode:screen;opacity:.35"></div>
<div class="abs" style="left:40px;top:30px;font:400 330px/0.82 Anton;color:#0d2c54;letter-spacing:-.02em">48</div>
<div class="abs" style="left:52px;top:300px;font:400 110px/1 Anton;color:#fff;letter-spacing:.06em">SAAT</div>
<div class="abs" style="left:0;right:0;bottom:0;height:470px;background:#0d2c54"></div>
<div class="abs" style="left:64px;right:64px;top:930px">
  <div style="font:400 62px/1.06 Anton;color:#fff;text-transform:uppercase">{K_MAIN}</div>
  <div class="serif" style="font-size:48px;line-height:1.12;color:#ffcc33;margin-top:12px">{K_TAIL}</div>
</div>
{logo('white')}
""", "#ffcc33")


def kacis_c():  # ortalanmış, otomatik yanıt sözü, geniş manzara
    return page(f"""
<div class="bg" style="{ph('cmbyn_2', '50% 50%', 'filter:saturate(1.1)')}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(6,18,10,.75) 0%,rgba(6,18,10,.2) 32%,rgba(6,18,10,.15) 55%,rgba(6,18,10,.9) 78%)"></div>
<div class="abs" style="left:0;right:0;top:110px;text-align:center">
  <div class="osw" style="font-size:22px;color:#d9f0c8">Otomatik yanıt</div>
  <div style="font:700 italic 104px/1.02 'Playfair Display';color:#fff;margin-top:18px">Pazartesiye<br>kadar yokum.</div>
</div>
<div class="abs" style="left:70px;right:70px;top:930px;text-align:center">
  <div style="font:400 60px/1.07 Anton;color:#fff;text-transform:uppercase">{K_MAIN}</div>
  <div class="serif" style="font-size:48px;line-height:1.12;color:#c8f06a;margin-top:12px">{K_TAIL}</div>
</div>
{logo('white')}
""", "#000")


ITEMS = [("06_tesaduf_A_buyuk-baslik", tesaduf_a), ("09_kacis_A", kacis_a), ("09_kacis_B", kacis_b), ("09_kacis_C", kacis_c)]

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        tmp = os.path.join(HERE, "_k.html")
        for name, fn in ITEMS:
            open(tmp, "w").write(fn())
            pg.goto("file://" + tmp, wait_until="load")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(500)
            pg.screenshot(path=os.path.join(out, f"{name}.jpg"), type="jpeg", quality=94)
        b.close()
    print("ok")

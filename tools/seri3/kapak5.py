"""Liste serisi — 6 (tesadüf) ve 9 (kaçış) için yeni 3'er seçenek. python3 tools/seri3/kapak5.py <çıktı>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kapak2 import page, P, LOGO, EN
from kapak3 import T_MAIN, T_TAIL, K_MAIN, K_TAIL, ph, logo, meta
from playwright.sync_api import sync_playwright


# ================================================================== TESADÜF
def t1():  # sinema bileti koçanı
    notch = "radial-gradient(circle at 0 50%,transparent 34px,#fff7e6 35px) left/51% 100% no-repeat,radial-gradient(circle at 100% 50%,transparent 34px,#fff7e6 35px) right/51% 100% no-repeat"
    return page(f"""
<div class="abs" style="inset:0;background:#123c3a"></div>
<div class="abs" style="left:90px;top:110px;width:900px;height:700px;transform:rotate(-4deg);filter:drop-shadow(0 30px 40px rgba(0,0,0,.4))">
  <div style="position:absolute;inset:0;background:{notch}"></div>
  <div style="position:absolute;left:40px;top:40px;width:560px;bottom:40px;{ph('serendipity_3','50% 50%')}"></div>
  <div style="position:absolute;left:640px;top:40px;bottom:40px;border-left:4px dashed #d9c8a4"></div>
  <div style="position:absolute;left:668px;right:36px;top:60px;color:#3b2a14">
    <div style="font:500 20px Oswald;letter-spacing:.3em">SALON</div><div style="font:400 90px/1 Anton">7</div>
    <div style="font:500 20px Oswald;letter-spacing:.3em;margin-top:24px">KOLTUK</div><div style="font:400 90px/1 Anton">J-12</div>
    <div style="font:500 20px Oswald;letter-spacing:.3em;margin-top:24px">YANINDAKİ</div><div style="font:italic 700 36px 'Playfair Display'">bilinmiyor</div>
  </div>
  <div style="position:absolute;left:40px;bottom:-2px;font:400 120px/1 'Abril Fatface';color:#fff7e6;transform:translateY(50%)"></div>
</div>
<div class="abs" style="left:64px;right:64px;top:900px">
  <div style="font:400 54px/1.06 Anton;text-transform:uppercase;color:#fff7e6">{T_MAIN}</div>
  <div class="serif" style="font-size:44px;color:#f2c14e;margin-top:12px">{T_TAIL}</div>
</div>
{meta('5 FİLM · 17 KASIM · KAYDIR →', '#fff7e6')}{logo('white')}
""", "#123c3a")


def t2():  # lüks parfüm reklamı
    return page(f"""
<div class="abs" style="inset:0;background:#0a0a0a"></div>
<div class="abs" style="left:0;right:0;top:0;height:880px;{ph('harrysally_4','50% 50%','filter:grayscale(1) contrast(1.15) brightness(.9)')}"></div>
<div class="abs" style="left:0;right:0;top:600px;height:280px;background:linear-gradient(180deg,rgba(10,10,10,0),#0a0a0a)"></div>
<div class="abs" style="left:0;right:0;top:820px;text-align:center;font:400 120px/1 'Playfair Display';letter-spacing:.32em;color:#e8d9b0;padding-left:.32em">TESADÜF</div>
<div class="abs" style="left:0;right:0;top:950px;text-align:center;font:500 20px Inter;letter-spacing:.6em;color:#a8957a">EAU DE CINÉMA · 5 FİLM</div>
<div class="abs" style="left:150px;right:150px;top:1040px;text-align:center">
  <div style="font:400 30px/1.4 'Playfair Display';color:#d9d2c3">{T_MAIN}</div>
  <div style="font:italic 400 30px/1.4 'Playfair Display';color:#e8d9b0">{T_TAIL}</div>
</div>
{logo('white')}
""", "#0a0a0a")


def t3():  # pop-art çizgi roman
    return page(f"""
<div class="abs" style="inset:0;background:#ffe14d"></div>
<div class="abs" style="inset:0;background-image:radial-gradient(#ff3b6b 3px,transparent 3.5px);background-size:18px 18px;opacity:.5"></div>
<div class="abs" style="left:60px;top:200px;width:960px;height:700px;border:8px solid #111;{ph('amelie_4','60% 35%','filter:contrast(1.25) saturate(1.5)')}"></div>
<div class="abs" style="left:60px;top:200px;width:960px;height:700px;background-image:radial-gradient(rgba(0,0,0,.35) 1.6px,transparent 2px);background-size:9px 9px;mix-blend-mode:multiply"></div>
<div class="abs" style="left:70px;top:60px;width:560px;background:#fff;border:6px solid #111;border-radius:60px;padding:26px 34px;font:400 46px/1.05 Anton;color:#111;text-transform:uppercase;box-shadow:8px 8px 0 #111">Biz daha önce bir yerde karşılaştık mı?</div>
<div class="abs" style="left:150px;top:222px;width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-top:50px solid #111"></div>
<div class="abs" style="left:700px;top:820px;background:#ff3b6b;border:6px solid #111;padding:10px 26px;font:400 64px Anton;color:#fff;transform:rotate(-8deg);box-shadow:8px 8px 0 #111">ZING!</div>
<div class="abs" style="left:60px;right:60px;top:950px;background:#fff;border:6px solid #111;padding:26px 30px;box-shadow:8px 8px 0 #111">
  <div style="font:400 44px/1.06 Anton;text-transform:uppercase;color:#111">{T_MAIN}</div>
  <div style="font:400 40px/1.1 Anton;text-transform:uppercase;color:#ff3b6b;margin-top:6px">{T_TAIL}</div>
</div>
{logo('black')}
""", "#ffe14d")


# ================================================================== İKİ GÜNLÜK KAÇIŞ
def stamp(text, sub, color, x, y, r, w=260):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{w}px;border:6px solid {color};border-radius:50%;'
            f'display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate({r}deg);color:{color};opacity:.85">'
            f'<div style="font:400 54px/1 Anton;letter-spacing:.04em">{text}</div><div style="font:600 18px Inter;letter-spacing:.2em;margin-top:6px">{sub}</div></div>')


def k1():  # pasaport sayfası
    return page(f"""
<div class="abs" style="inset:0;background:#e9e2cf"></div>
<div class="abs" style="inset:0;background:repeating-linear-gradient(45deg,rgba(120,100,60,.05) 0 2px,transparent 2px 12px)"></div>
<div class="abs" style="left:64px;top:60px;font:600 20px Inter;letter-spacing:.35em;color:#6b5a3a">VİZE / VISAS · 23</div>
<div class="abs" style="left:90px;top:140px;width:420px;height:520px;background:#fff;padding:14px;transform:rotate(-3deg);box-shadow:0 12px 30px rgba(60,40,10,.25)"><div style="width:100%;height:100%;{ph('cmbyn_1','30% 50%')}"></div></div>
{stamp('ROMA', 'CUMARTESİ · GİRİŞ', '#c0392b', 560, 140, -12)}
{stamp('ROMA', 'PAZAR · ÇIKIŞ', '#1f4e8c', 700, 420, 9, 240)}
<div class="abs" style="left:540px;top:700px;border:5px solid #2e7d32;color:#2e7d32;padding:10px 20px;font:400 44px Anton;transform:rotate(-6deg);opacity:.85">İZİN: 2 GÜN</div>
<div class="abs" style="left:64px;right:64px;top:850px">
  <div style="font:400 62px/1.06 Anton;text-transform:uppercase;color:#2b2112">{K_MAIN}</div>
  <div class="serif" style="font-size:48px;color:#c0392b;margin-top:12px">{K_TAIL}</div>
</div>
{meta('5 FİLM · 23 KASIM · KAYDIR →', '#2b2112')}{logo('black')}
""", "#e9e2cf")


def k2():  # gezi rehberi kitap kapağı
    return page(f"""
<div class="abs" style="inset:0;background:#0057b8"></div>
<div class="abs" style="left:0;right:0;top:0;height:820px;{ph('mammamia_1','40% 50%')}"></div>
<div class="abs" style="left:0;right:0;top:820px;bottom:0;background:#0057b8"></div>
<div class="abs" style="left:64px;top:740px;background:#ffd400;padding:14px 26px;font:800 30px Inter;color:#0a2b5c;letter-spacing:-.01em">HAFTA SONU REHBERİ</div>
<div class="abs" style="left:64px;right:64px;top:870px">
  <div style="font:900 70px/1.04 Inter;color:#fff;letter-spacing:-.03em">{K_MAIN}</div>
  <div style="font:700 46px/1.2 Inter;color:#ffd400;margin-top:18px;letter-spacing:-.01em">{K_TAIL}</div>
</div>
<div class="abs" style="left:64px;bottom:66px;font:700 22px Inter;color:#cfe1ff">5 film · 2 gün · 0 plan</div>
{logo('white')}
""", "#0057b8")


def k3():  # sinemaskop + altyazı
    return page(f"""
<div class="abs" style="inset:0;background:#000"></div>
<div class="abs" style="left:0;right:0;top:330px;height:600px;{ph('romanholiday_3','45% 40%')}"></div>
<div class="abs" style="left:0;right:0;top:850px;text-align:center;font:600 34px Inter;color:#ffe14d;text-shadow:0 2px 6px #000">— Pazartesi ne olacak?<br>— Pazartesi yok.</div>
<div class="abs" style="left:64px;right:64px;top:80px">
  <div style="font:400 52px/1.08 Anton;text-transform:uppercase;color:#fff">{K_MAIN}</div>
  <div class="serif" style="font-size:42px;color:#ffe14d;margin-top:10px">{K_TAIL}</div>
</div>
<div class="abs osw" style="left:0;right:0;top:1000px;text-align:center;font-size:20px;color:#8a8a8a">2.39 : 1 · 5 FİLM · 23 KASIM</div>
{logo('white')}
""", "#000")


SETS = [("06_tesaduf", [t1, t2, t3]), ("09_iki-gunluk-kacis", [k1, k2, k3])]

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

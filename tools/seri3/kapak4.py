"""Liste serisi — 2, 6, 8, 9 için marka tarzlarından ilhamlı 3'er seçenek (marka adı/logosu yok). python3 tools/seri3/kapak4.py <çıktı>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kapak2 import page, P, LOGO, EN
from kapak3 import G_MAIN, G_TAIL, T_MAIN, T_TAIL, S_MAIN, S_TAIL, K_MAIN, K_TAIL, ph, logo, meta
from playwright.sync_api import sync_playwright


# ================================================================== GHOSTLANMA
def g1():  # renk kartelası
    return page(f"""
<div class="abs" style="inset:0;background:#e9e6e1"></div>
<div class="abs" style="left:170px;top:90px;width:740px;height:1000px;background:#fff;box-shadow:0 30px 60px rgba(0,0,0,.18)">
  <div style="height:700px;background:#f25c8f;position:relative;overflow:hidden">
    <div style="position:absolute;inset:0;{ph('eternal_2','55% 40%','filter:grayscale(1) contrast(1.15)')};mix-blend-mode:multiply"></div></div>
  <div style="padding:30px 36px">
    <div style="font:800 34px Inter;color:#111;letter-spacing:-.01em">GÖRÜLDÜ PEMBESİ</div>
    <div style="font:500 26px Inter;color:#111;margin-top:6px">17-0309 · 3 gün, cevapsız</div>
    <div style="display:flex;gap:10px;margin-top:22px">{''.join(f'<div style="flex:1;height:54px;background:{c}"></div>' for c in ['#ffd3e2','#ffa3c4','#f25c8f','#c2185b','#6d0f35'])}</div>
  </div>
</div>
<div class="abs" style="left:64px;right:64px;top:1120px;text-align:center">
  <div style="font:700 34px/1.2 Inter;color:#111">{G_MAIN} <span style="font:italic 700 34px 'Playfair Display';color:#c2185b">{G_TAIL}</span></div>
</div>
{logo('black')}
""", "#e9e6e1")


def g2():  # yıllık müzik özeti tarzı, cafcaflı
    return page(f"""
<div class="abs" style="inset:0;background:#1d0b3a"></div>
<div class="abs" style="left:-200px;top:-180px;width:900px;height:900px;border-radius:50%;background:#ff3d8b;filter:blur(10px)"></div>
<div class="abs" style="right:-260px;top:300px;width:820px;height:820px;border-radius:50%;background:#2bf0a2"></div>
<div class="abs" style="left:120px;top:880px;width:700px;height:700px;border-radius:50%;background:#ffe14d"></div>
<div class="abs" style="left:64px;top:110px;font:900 44px/1.1 Inter;color:#1d0b3a;max-width:620px">Bu hafta en çok dinlediğin şarkı:</div>
<div class="abs" style="left:64px;top:240px;font:900 150px/0.9 Inter;color:#fff;letter-spacing:-.04em">Aynı<br>şarkı.</div>
<div class="abs" style="left:560px;top:380px;width:420px;height:420px;{ph('her_2','50% 30%')};transform:rotate(6deg);box-shadow:0 20px 40px rgba(0,0,0,.35)"></div>
<div class="abs" style="left:64px;top:560px;font:900 120px Inter;color:#1d0b3a;letter-spacing:-.04em">47×</div>
<div class="abs" style="left:64px;right:64px;top:870px;background:#1d0b3a;padding:36px 40px;border-radius:28px">
  <div style="font:900 44px/1.1 Inter;color:#fff;letter-spacing:-.02em">{G_MAIN}</div>
  <div style="font:900 44px/1.1 Inter;color:#2bf0a2;letter-spacing:-.02em;margin-top:8px">{G_TAIL}</div>
</div>
{logo('white')}
""", "#1d0b3a")


def g3():  # bağımsız stüdyo sadeliği
    return page(f"""
<div class="abs" style="inset:0;background:#0b0b0b"></div>
<div class="abs" style="left:290px;top:250px;width:500px;height:620px;{ph('her_1','45% 50%')}"></div>
<div class="abs" style="left:0;right:0;top:120px;text-align:center;font:500 20px Inter;letter-spacing:.5em;color:#bdbdbd">ÜÇ GÜN SONRA</div>
<div class="abs" style="left:150px;right:150px;top:930px;text-align:center">
  <div style="font:400 40px/1.3 'DM Serif Display';color:#f2f2f2">{G_MAIN}</div>
  <div style="font:italic 400 36px/1.3 'Playfair Display';color:#9a9a9a;margin-top:10px">{G_TAIL}</div>
</div>
<div class="abs" style="left:0;right:0;bottom:70px;text-align:center;font:500 18px Inter;letter-spacing:.5em;color:#6b6b6b">5 FİLM · 9 KASIM</div>
{logo('white')}
""", "#0b0b0b")


# ================================================================== TESADÜF
def t1():  # klasik koleksiyon kutusu
    return page(f"""
<div class="abs" style="inset:0;background:#111"></div>
<div class="abs" style="left:0;top:0;width:96px;height:1350px;background:#e9e3d6;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:40px 0">
  <div style="font:700 30px Inter;color:#111">17</div>
  <div style="writing-mode:vertical-rl;transform:rotate(180deg);font:600 26px Inter;letter-spacing:.3em;color:#111">TESADÜF · 5 FİLM</div>
  <img src="{LOGO}/black.png" style="width:52px;height:52px">
</div>
<div class="abs" style="left:160px;right:64px;top:90px;height:720px;{ph('chungking_1','35% 50%')}"></div>
<div class="abs" style="left:160px;right:64px;top:850px">
  <div style="font:500 22px Inter;letter-spacing:.3em;color:#9a9a9a">SPINE NO. 17</div>
  <div style="font:700 44px/1.18 Inter;color:#fff;margin-top:20px;letter-spacing:-.01em">{T_MAIN}</div>
  <div style="font:italic 400 40px 'Playfair Display';color:#e9c46a;margin-top:12px">{T_TAIL}</div>
</div>
""".replace("SPINE NO. 17", "KOLEKSİYON NO. 17"), "#111")


def t2():  # İsviçre tipografi afişi
    return page(f"""
<div class="abs" style="inset:0;background:#f0ece2"></div>
<div class="abs" style="left:-120px;top:150px;width:760px;height:760px;border-radius:50%;background:#e63b2e"></div>
<div class="abs" style="left:380px;top:300px;width:640px;height:640px;border-radius:50%;{ph('amelie_4','55% 35%','filter:grayscale(1) contrast(1.2)')};mix-blend-mode:multiply"></div>
<div class="abs" style="left:64px;top:60px;font:900 150px/0.86 Inter;color:#111;letter-spacing:-.06em">te<br>sa<br>düf</div>
<div class="abs" style="left:64px;right:64px;top:1000px;border-top:6px solid #111;padding-top:24px;display:flex;gap:30px">
  <div style="flex:2;font:800 34px/1.15 Inter;color:#111;letter-spacing:-.02em">{T_MAIN}</div>
  <div style="flex:1;font:800 34px/1.15 Inter;color:#e63b2e;letter-spacing:-.02em">{T_TAIL}</div>
</div>
{meta('5 FİLM — 17.11', '#111')}{logo('black')}
""", "#f0ece2")


def t3():  # pastel simetrik sinema
    return page(f"""
<div class="abs" style="inset:0;background:#f6c8cf"></div>
<div class="abs" style="left:40px;right:40px;top:40px;bottom:40px;border:4px solid #8c2f39"></div>
<div class="abs" style="left:56px;right:56px;top:56px;bottom:56px;border:1.5px solid #8c2f39"></div>
<div class="abs" style="left:0;right:0;top:110px;text-align:center;font:600 24px 'Space Grotesk';letter-spacing:.4em;color:#8c2f39">BÖLÜM 17 · KASIM</div>
<div class="abs" style="left:240px;top:180px;width:600px;height:600px;border-radius:300px 300px 0 0;{ph('amelie_3','50% 45%')};border:12px solid #fff6e8"></div>
<div class="abs" style="left:0;right:0;top:820px;text-align:center;font:700 72px 'Space Grotesk';color:#8c2f39;letter-spacing:.06em">TESADÜF</div>
<div class="abs" style="left:130px;right:130px;top:930px;text-align:center">
  <div style="font:500 32px/1.3 'Space Grotesk';color:#5a1d25">{T_MAIN}</div>
  <div style="font:italic 700 34px 'Playfair Display';color:#8c2f39;margin-top:10px">{T_TAIL}</div>
</div>
<img class="abs" src="{LOGO}/black.png" style="left:510px;bottom:80px;width:60px;height:60px">
""", "#f6c8cf")


# ================================================================== TEK KİŞİLİK SOFRA
def s1():  # klasik kitap kapağı
    return page(f"""
<div class="abs" style="inset:0;background:#f15a24"></div>
<div class="abs" style="left:0;right:0;top:330px;height:640px;background:#fbf6ea"></div>
<div class="abs" style="left:0;right:0;top:80px;text-align:center">
  <div style="font:700 26px Inter;letter-spacing:.3em;color:#fbf6ea">5 FİLM</div>
  <div style="font:400 64px/1.15 'Playfair Display';color:#fff;margin:14px 100px 0">Tek Kişilik Sofra</div>
</div>
<div class="abs" style="left:250px;top:380px;width:580px;height:540px;{ph('littleforest_1','40% 40%')}"></div>
<div class="abs" style="left:80px;right:80px;top:1000px;text-align:center">
  <div style="font:400 36px/1.25 'Playfair Display';color:#fff">{S_MAIN}</div>
  <div style="font:italic 400 34px 'Playfair Display';color:#2b1100;margin-top:8px">{S_TAIL}</div>
</div>
<div class="abs" style="left:0;right:0;top:965px;height:6px;background:#2b1100;opacity:.0"></div>
{logo('white')}
""", "#f15a24")


def s2():  # sade yaşam dergisi
    return page(f"""
<div class="abs" style="inset:0;background:#f4f1ea"></div>
<div class="abs" style="left:64px;top:70px;font:500 20px Inter;letter-spacing:.35em;color:#8a8270">NO. 21 — YALNIZ YEMEK ÜZERİNE</div>
<div class="abs" style="left:64px;top:150px;width:640px;height:800px;{ph('kamome_3','50% 30%')}"></div>
<div class="abs" style="left:740px;top:150px;right:64px;font:italic 400 32px/1.4 'Playfair Display';color:#3d372c">“Bir tabak, bir kaşık, açık kalan bir film.”</div>
<div class="abs" style="left:64px;right:120px;top:1000px">
  <div style="font:400 44px/1.22 'DM Serif Display';color:#1f1b14">{S_MAIN}</div>
  <div style="font:italic 400 38px 'Playfair Display';color:#a0623a;margin-top:10px">{S_TAIL}</div>
</div>
{logo('black')}
""", "#f4f1ea")


def s3():  # spor markası reklamı: büyük slogan
    return page(f"""
<div class="bg" style="{ph('lunchbox_4','78% 50%','filter:grayscale(1) contrast(1.25) brightness(.85)')}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.1) 30%,rgba(0,0,0,.85) 72%)"></div>
<div class="abs" style="left:56px;right:56px;top:640px;font:italic 400 150px/0.88 Anton;color:#fff;text-transform:uppercase;letter-spacing:-.01em">Tek<br>başına<br><span style="color:#ff6a1a">da olur.</span></div>
<div class="abs" style="left:64px;right:64px;top:1110px">
  <div style="font:700 30px/1.25 Inter;color:#fff">{S_MAIN} <span style="color:#ff9a5a">{S_TAIL}</span></div>
</div>
{logo('white')}
""", "#000")


# ================================================================== İKİ GÜNLÜK KAÇIŞ
def k1():  # retro seyahat afişi
    return page(f"""
<div class="abs" style="inset:0;background:linear-gradient(180deg,#ffb35c 0%,#ff7a4d 45%,#2b4a7a 100%)"></div>
<div class="abs" style="left:290px;top:120px;width:500px;height:500px;border-radius:50%;background:#ffe9a8"></div>
<div class="abs" style="left:190px;top:260px;width:700px;height:620px;border-radius:350px 350px 0 0;{ph('cmbyn_2','50% 50%')};border:14px solid #fff2d6"></div>
<div class="abs" style="left:0;right:0;top:880px;text-align:center;font:400 140px/1 'Abril Fatface';color:#fff2d6;letter-spacing:.04em">KAÇIŞ</div>
<div class="abs" style="left:110px;right:110px;top:1060px;text-align:center">
  <div style="font:600 32px/1.25 'Space Grotesk';color:#fff">{K_MAIN}</div>
  <div style="font:italic 700 32px 'Playfair Display';color:#ffe9a8;margin-top:6px">{K_TAIL}</div>
</div>
<div class="abs osw" style="left:0;right:0;top:60px;text-align:center;font-size:20px;color:#2b4a7a">2 GÜNLÜK SEFER · 23 KASIM</div>
{logo('white')}
""", "#2b4a7a")


def k2():  # teknoloji markası sadeliği
    return page(f"""
<div class="abs" style="inset:0;background:#fbfbfd"></div>
<div class="abs" style="left:0;right:0;top:110px;text-align:center;font:600 30px Inter;color:#86868b">Hafta sonu.</div>
<div class="abs" style="left:0;right:0;top:160px;text-align:center;font:700 108px/1 Inter;color:#1d1d1f;letter-spacing:-.04em">İki gün.<br>Bir dünya.</div>
<div class="abs" style="left:110px;right:110px;top:430px;height:560px;border-radius:40px;{ph('romanholiday_3','45% 40%')}"></div>
<div class="abs" style="left:120px;right:120px;top:1040px;text-align:center">
  <div style="font:600 34px/1.3 Inter;color:#1d1d1f;letter-spacing:-.01em">{K_MAIN}</div>
  <div style="font:600 34px/1.3 Inter;color:#0071e3;letter-spacing:-.01em">{K_TAIL}</div>
</div>
{logo('black')}
""", "#fbfbfd")


def k3():  # risograf fanzin, cafcaflı
    return page(f"""
<div class="abs" style="inset:0;background:#fff3e0"></div>
<div class="abs" style="inset:0;background-image:radial-gradient(#ff48b0 1.4px,transparent 1.6px);background-size:14px 14px;opacity:.35"></div>
<div class="abs" style="left:90px;top:120px;width:640px;height:780px;{ph('mammamia_1','40% 50%','filter:grayscale(1) contrast(1.4)')};mix-blend-mode:multiply;transform:rotate(-4deg)"></div>
<div class="abs" style="left:110px;top:140px;width:640px;height:780px;background:#00a0ff;mix-blend-mode:screen;opacity:.55;transform:rotate(-4deg)"></div>
<div class="abs" style="left:600px;top:80px;font:400 300px/0.85 Anton;color:#ff48b0;mix-blend-mode:multiply;transform:rotate(8deg)">2<br>GÜN</div>
<div class="abs" style="left:620px;top:760px;background:#ffe600;padding:16px 22px;font:400 46px Anton;color:#111;transform:rotate(-6deg);box-shadow:6px 6px 0 #111">KAÇ!</div>
<div class="abs" style="left:64px;right:64px;top:960px">
  <div style="font:400 54px/1.06 Anton;text-transform:uppercase;color:#111">{K_MAIN}</div>
  <div style="font:700 50px Caveat;color:#e5007e;margin-top:6px">{K_TAIL}</div>
</div>
{meta('5 FİLM · 23 KASIM', '#111')}{logo('black')}
""", "#fff3e0")


SETS = [("02_ghostlanma", [g1, g2, g3]), ("06_tesaduf", [t1, t2, t3]), ("08_tek-kisilik-sofra", [s1, s2, s3]), ("09_iki-gunluk-kacis", [k1, k2, k3])]

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

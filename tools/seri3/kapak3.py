"""Liste serisi — açık kalan 5 gönderi için 3'er farklı tasarım dili. python3 tools/seri3/kapak3.py <çıktı>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kapak2 import page, P, LOGO, EN
from playwright.sync_api import sync_playwright


def logo(name="white", x=None, y=None, w=60, z=20):
    pos = f"right:56px;bottom:52px" if x is None else f"left:{x}px;top:{y}px"
    return f'<img class="abs" src="{LOGO}/{name}.png" style="{pos};width:{w}px;height:{w}px;z-index:{z}">'


def meta(text, color, x=64, y=None, bottom=66, z=20, align="left"):
    pos = f"top:{y}px" if y is not None else f"bottom:{bottom}px"
    return f'<div class="abs osw" style="left:{x}px;{pos};font-size:20px;color:{color};z-index:{z};text-align:{align}">{text}</div>'


def ph(name, pos="50% 50%", filt=""):
    return f"background:url({P(name)}) {pos}/cover;{filt}"


# ------------------------------------------------------------------ GHOSTLANMA
G_MAIN = f"{EN('Ghost')}landıktan sonra üç gün boyunca aynı şarkıyı dinleyenlerin,"
G_TAIL = "terapiye gitmeden önce izlemesi gereken filmler"


def g_a():  # bölünmüş ekran: iki kare, ortada şerit
    return page(f"""
<div class="abs" style="left:0;top:0;width:540px;height:1350px;{ph('eternal_2','62% 40%')}"></div>
<div class="abs" style="left:540px;top:0;width:540px;height:1350px;{ph('her_1','45% 50%','filter:grayscale(1) contrast(1.1)')}"></div>
<div class="abs" style="left:0;right:0;top:830px;bottom:0;background:#0d0d10;padding:46px 64px 42px">
  <div style="font:400 58px/1.06 Anton;text-transform:uppercase;color:#fff">{G_MAIN}</div>
  <div class="serif" style="font-size:46px;color:#ff6fa5;margin-top:10px">{G_TAIL}</div>
</div>
<div class="abs osw" style="left:64px;top:60px;font-size:22px;color:#fff;background:rgba(0,0,0,.55);padding:8px 14px">ÖNCE</div>
<div class="abs osw" style="left:604px;top:60px;font-size:22px;color:#fff;background:rgba(0,0,0,.55);padding:8px 14px">3 GÜN SONRA</div>
{meta('5 FİLM · 9 KASIM · KAYDIR →', '#fff')}{logo()}
""")


def g_b():  # pembe çift ton afiş + dev alıntı
    return page(f"""
<div class="abs" style="inset:0;background:#ff5c9d"></div>
<div class="abs" style="right:0;top:0;width:640px;height:820px;{ph('her_3','45% 40%','filter:grayscale(1) contrast(1.2)')};mix-blend-mode:multiply"></div>
<div class="abs" style="left:64px;top:110px;font:700 italic 190px/0.9 'Playfair Display';color:#1a0610">“naber?”</div>
<div class="abs" style="left:70px;top:330px;font:600 26px Inter;color:#1a0610;opacity:.8">iletildi · 3 gündür cevap yok</div>
<div class="abs" style="left:64px;right:64px;top:880px">
  <div style="font:400 60px/1.06 'Archivo Black';text-transform:uppercase;color:#1a0610;letter-spacing:-.01em">{G_MAIN}</div>
  <div class="serif" style="font-size:46px;color:#fff;margin-top:12px">{G_TAIL}</div>
</div>
{meta('5 FİLM · 9 KASIM', '#1a0610')}{logo('black')}
""", "#ff5c9d")


def g_c():  # film şeridi: solda 3 kare dikey, sağda yazı
    frames = "".join(f'<div style="height:330px;margin:14px 0;{ph(n, p)}"></div>' for n, p in [("her_1", "50% 50%"), ("anniehall_4", "50% 50%"), ("beginagain_3", "50% 50%")])
    holes = "".join('<div style="width:22px;height:30px;border-radius:5px;background:#f2ede4;margin:16px auto"></div>' for _ in range(24))
    return page(f"""
<div class="abs" style="inset:0;background:#f2ede4"></div>
<div class="abs" style="left:56px;top:-20px;width:470px;height:1400px;background:#111;display:flex;transform:rotate(-3deg)">
  <div style="width:46px">{holes}</div><div style="flex:1;padding:20px 0">{frames}</div><div style="width:46px">{holes}</div>
</div>
<div class="abs" style="left:590px;right:60px;top:150px">
  <div class="osw" style="font-size:22px;color:#c2185b">Aynı şarkı · 47. kez</div>
  <div style="font:700 56px/1.12 'Playfair Display';color:#141414;margin-top:24px">{G_MAIN}</div>
  <div class="serif" style="font-size:44px;color:#c2185b;margin-top:22px">{G_TAIL}</div>
</div>
{meta('5 FİLM · 9 KASIM · KAYDIR →', '#141414', x=590)}{logo('black')}
""", "#f2ede4")


# ------------------------------------------------------------------ TESADÜF
T_MAIN = f"{EN('Dating')} uygulamasında kaydırdıkça insanların birbirine benzediğini fark edenlere,"
T_TAIL = "gerçek bir tesadüfün büyüsünü hatırlatan filmler"


def t_a():  # polaroid dağınıklığı
    pol = [("amelie_4", "50% 30%", 70, 120, 400, -8), ("chungking_1", "30% 50%", 560, 90, 430, 6), ("harrysally_4", "50% 50%", 300, 360, 470, -2),
           ("serendipity_3", "50% 50%", 40, 560, 380, 5), ("sleepless_4", "65% 40%", 620, 520, 400, -6)]
    ps = "".join(f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{int(w*.92)}px;background:#fff;padding:16px 16px 62px;transform:rotate({r}deg);box-shadow:0 16px 36px rgba(40,30,20,.25)"><div style="width:100%;height:100%;{ph(n, p)}"></div></div>' for n, p, x, y, w, r in pol)
    return page(f"""
<div class="abs" style="inset:0;background:#e9e1d3"></div>
{ps}
<div class="abs" style="left:64px;right:64px;top:960px">
  <div style="font:400 50px/1.08 Anton;text-transform:uppercase;color:#1c2422">{T_MAIN}</div>
  <div style="font:700 56px Caveat;color:#d1344f;margin-top:8px">{T_TAIL}</div>
</div>
{meta('5 FİLM · 17 KASIM', '#1c2422')}{logo('black')}
""", "#e9e1d3")


def t_b():  # dergi kapağı
    return page(f"""
<div class="bg" style="{ph('harrysally_1','50% 50%')}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,0) 30%,rgba(0,0,0,0) 55%,rgba(0,0,0,.7))"></div>
<div class="abs" style="left:0;right:0;top:40px;text-align:center;font:400 210px/1 'Abril Fatface';color:#fff;letter-spacing:.02em">TESADÜF</div>
<div class="abs" style="left:0;right:0;top:262px;text-align:center" class="osw"><span class="osw" style="font-size:22px;color:#fff">Sayı 17 · Kasım · 5 film</span></div>
<div class="abs" style="left:64px;width:520px;top:860px">
  <div style="font:700 44px/1.12 'Playfair Display';color:#fff">{T_MAIN}</div>
  <div class="serif" style="font-size:40px;color:#ffd36b;margin-top:10px">{T_TAIL}</div>
</div>
{logo()}
""")


def t_c():  # 2x2 mozaik + düz renk panel
    cells = [("amelie_3", "50% 40%"), ("chungking_4", "50% 40%"), ("serendipity_1", "40% 40%"), ("harrysally_2", "50% 40%")]
    grid = "".join(f'<div style="{ph(n,p)}"></div>' for n, p in cells)
    return page(f"""
<div class="abs" style="left:0;top:0;width:1080px;height:760px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:8px;background:#0f6f6a">{grid}</div>
<div class="abs" style="left:0;right:0;top:760px;bottom:0;background:#0f6f6a"></div>
<div class="abs" style="left:440px;top:300px;width:200px;height:200px;border-radius:50%;background:#ffe14d;display:flex;align-items:center;justify-content:center;text-align:center;font:400 40px/1 Anton;color:#0f2a28;transform:rotate(-10deg);box-shadow:0 10px 30px rgba(0,0,0,.3)">EŞLEŞME<br>YOK</div>
<div class="abs" style="left:64px;right:64px;top:820px">
  <div style="font:400 54px/1.08 'Archivo Black';text-transform:uppercase;color:#fff;letter-spacing:-.01em">{T_MAIN}</div>
  <div class="serif" style="font-size:44px;color:#ffe14d;margin-top:12px">{T_TAIL}</div>
</div>
{meta('5 FİLM · 17 KASIM · KAYDIR →', '#fff')}{logo()}
""", "#0f6f6a")


# ------------------------------------------------------------------ FİLM GECESİ
F_MAIN = "Arkadaşının ilişkisi bittiğinde “tamam, film gecesi yapıyoruz” diyen herkesin,"
F_TAIL = "kimsenin ağlamadan bitiremediği filmler"


def f_a():  # VHS kaseti
    return page(f"""
<div class="abs" style="inset:0;background:repeating-linear-gradient(0deg,#2a1030 0 2px,#22092a 2px 4px)"></div>
<div class="abs" style="left:90px;top:150px;width:900px;height:560px;background:#151515;border-radius:24px;box-shadow:0 30px 60px rgba(0,0,0,.5)">
  <div style="position:absolute;left:40px;right:40px;top:36px;height:300px;{ph('legallyblonde_4','55% 30%')};border-radius:6px"></div>
  <div style="position:absolute;left:40px;right:40px;top:336px;height:90px;background:#ff3d8b;display:flex;align-items:center;justify-content:space-between;padding:0 26px;font:400 50px Anton;color:#fff">
    <span>ACİL FİLM GECESİ</span><span style="font:600 22px Inter">SP · 120 DK</span></div>
  <div style="position:absolute;left:250px;top:450px;width:400px;height:80px;background:#0b0b0b;border-radius:12px;display:flex;justify-content:space-around;align-items:center">
    <div style="width:56px;height:56px;border-radius:50%;border:8px solid #2b2b2b"></div><div style="width:56px;height:56px;border-radius:50%;border:8px solid #2b2b2b"></div></div>
</div>
<div class="abs" style="left:64px;right:64px;top:800px">
  <div style="font:400 58px/1.06 Anton;text-transform:uppercase;color:#fff">{F_MAIN}</div>
  <div class="serif" style="font-size:48px;color:#ff7eb6;margin-top:12px">{F_TAIL}</div>
</div>
{meta('5 FİLM · 19 KASIM · KAYDIR →', '#fff')}{logo()}
""", "#22092a")


def f_b():  # düz pembe afiş, büyük yazı, yuvarlak kare
    return page(f"""
<div class="abs" style="inset:0;background:#ffd1e3"></div>
<div class="abs" style="left:520px;top:90px;width:500px;height:500px;border-radius:50%;{ph('bridget_2','50% 40%')};border:10px solid #fff;box-shadow:0 20px 40px rgba(150,20,80,.25)"></div>
<div class="abs" style="left:64px;top:110px;font:400 150px/0.95 Anton;color:#e0218a">FİLM<br>GECESİ</div>
<div class="abs" style="left:64px;right:64px;top:720px">
  <div style="font:700 66px/1.12 'Playfair Display';color:#2a0f1c">{F_MAIN}</div>
  <div style="font:700 72px Caveat;color:#e0218a;margin-top:18px">{F_TAIL}</div>
</div>
{meta('5 FİLM · 19 KASIM', '#2a0f1c')}{logo('black')}
""", "#ffd1e3")


def f_c():  # yatay bantlar: 5 filmden 5 şerit
    bands = [("legallyblonde_4", "50% 30%"), ("bridget_2", "50% 35%"), ("sarahmarshall_4", "50% 40%"), ("theholiday_3", "50% 30%"), ("crazystupid_2", "50% 40%")]
    b = "".join(f'<div style="height:132px;{ph(n,p)}"></div>' for n, p in bands)
    return page(f"""
<div class="abs" style="inset:0;background:#160a12"></div>
<div class="abs" style="left:0;right:0;top:0;display:flex;flex-direction:column;gap:6px">{b}</div>
<div class="abs" style="left:64px;right:64px;top:740px">
  <div class="osw" style="font-size:22px;color:#ff7eb6">Dondurma · peçete · 5 film</div>
  <div style="font:400 60px/1.06 Anton;text-transform:uppercase;color:#fff;margin-top:16px">{F_MAIN}</div>
  <div class="serif" style="font-size:48px;color:#ff7eb6;margin-top:12px">{F_TAIL}</div>
</div>
{meta('19 KASIM · KAYDIR →', '#fff')}{logo()}
""", "#160a12")


# ------------------------------------------------------------------ TEK KİŞİLİK SOFRA
S_MAIN = "İşten çıkıp evde tek başına yemek yerken “bu da bir hayat” diyenlere,"
S_TAIL = "tek kişilik sofranın yalnız olmadığını gösteren filmler"


def s_a():  # menü kartı
    items = [("Başlangıç", "The Lunchbox"), ("Ara sıcak", "Kamome Diner"), ("Ana yemek", "Julie & Julia"), ("Yanında", "Little Forest"), ("Tatlı", "Ratatouille")]
    rows = "".join(f'<div style="display:flex;align-items:baseline;gap:12px;margin:16px 0"><span style="font:500 22px Oswald;letter-spacing:.2em;text-transform:uppercase;color:#9a7b4f;width:180px">{a}</span><span style="flex:1;border-bottom:2px dotted #c9b48e"></span><span style="font:italic 700 40px \'Playfair Display\';color:#2b1d0e"><span lang="en">{b}</span></span></div>' for a, b in items)
    return page(f"""
<div class="abs" style="inset:0;{ph('lunchbox_1','50% 50%','filter:blur(6px) brightness(.55)')};transform:scale(1.05)"></div>
<div class="abs" style="left:110px;top:190px;width:860px;background:#fbf6ea;padding:60px 64px 64px;box-shadow:0 30px 60px rgba(0,0,0,.4);border:2px solid #e2d3b2;outline:12px solid #fbf6ea">
  <div style="text-align:center;font:500 22px Oswald;letter-spacing:.3em;color:#9a7b4f">MASA 1 · KİŞİ 1</div>
  <div style="text-align:center;font:400 84px 'Abril Fatface';color:#2b1d0e;margin:6px 0 4px">Menü</div>
  <div style="width:80px;height:3px;background:#c2621b;margin:0 auto 26px"></div>
  {rows}
  <div style="border-top:2px solid #e2d3b2;margin:30px 0 22px"></div>
  <div style="font:700 42px/1.16 'Playfair Display';color:#2b1d0e;text-align:center">{S_MAIN}</div>
  <div class="serif" style="font-size:40px;color:#c2621b;text-align:center;margin-top:12px">{S_TAIL}</div>
</div>
{meta('5 FİLM · 21 KASIM · KAYDIR →', '#fff')}{logo()}
""", "#2b1d0e")


def s_b():  # üç yatay kare üst üste + yan yazı şeridi
    return page(f"""
<div class="abs" style="inset:0;background:#1c140c"></div>
<div class="abs" style="left:0;top:0;width:640px;height:1350px;display:flex;flex-direction:column;gap:8px">
  <div style="flex:1;{ph('lunchbox_4','78% 50%')}"></div><div style="flex:1;{ph('littleforest_4','50% 50%')}"></div><div style="flex:1;{ph('kamome_1','50% 40%')}"></div></div>
<div class="abs" style="left:690px;right:56px;top:120px">
  <svg width="90" height="90" viewBox="0 0 24 24"><path d="M7 2v8a2 2 0 0 0 4 0V2M9 10v12M17 2c-2 1.5-3 4-3 7h3v13" fill="none" stroke="#ffb35c" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <div style="font:400 50px/1.08 Anton;text-transform:uppercase;color:#fff;margin-top:30px">{S_MAIN}</div>
  <div class="serif" style="font-size:40px;color:#ffb35c;margin-top:18px">{S_TAIL}</div>
</div>
{meta('5 FİLM<br>21 KASIM', '#fff', x=690)}{logo()}
""", "#1c140c")


def s_c():  # amber çift ton + dev ×1
    return page(f"""
<div class="abs" style="inset:0;background:#f2a23c"></div>
<div class="abs" style="inset:0;{ph('kamome_3','50% 30%','filter:grayscale(1) contrast(1.25)')};mix-blend-mode:multiply;opacity:.9"></div>
<div class="abs" style="right:40px;top:20px;font:400 360px/1 Anton;color:#fff4e0;opacity:.95">×1</div>
<div class="abs" style="left:0;right:0;bottom:0;height:520px;background:#2b1708"></div>
<div class="abs" style="left:64px;right:64px;top:880px">
  <div style="font:400 56px/1.06 Anton;text-transform:uppercase;color:#fff">{S_MAIN}</div>
  <div class="serif" style="font-size:46px;color:#f2a23c;margin-top:12px">{S_TAIL}</div>
</div>
{meta('5 FİLM · 21 KASIM · KAYDIR →', '#fff')}{logo()}
""", "#2b1708")


# ------------------------------------------------------------------ İKİ GÜNLÜK KAÇIŞ
K_MAIN = "Yıllık izin hesabı yapıp iki günlük tatile bile sevinenlerin,"
K_TAIL = "kaçmanın bir film kadar iyi geldiğini hatırlatacak filmler"


def k_a():  # kartpostal
    return page(f"""
<div class="abs" style="inset:0;background:#d8e8ee"></div>
<div class="abs" style="left:70px;top:120px;width:940px;height:640px;background:#fff;padding:22px;box-shadow:0 24px 50px rgba(20,40,60,.25);transform:rotate(-2deg)">
  <div style="width:100%;height:100%;{ph('mammamia_1','40% 50%')}"></div>
  <div style="position:absolute;right:46px;top:46px;width:140px;height:170px;background:#fff;padding:8px;border:3px dashed #d8432a;transform:rotate(6deg)"><div style="width:100%;height:100%;{ph('romanholiday_3','45% 40%','filter:sepia(.4)')}"></div></div>
  <div style="position:absolute;left:46px;bottom:40px;font:700 64px Caveat;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.5);transform:rotate(-4deg)">Keşke burada olsaydın!</div>
</div>
<div class="abs" style="left:64px;right:64px;top:840px">
  <div style="font:400 64px/1.06 Anton;text-transform:uppercase;color:#0e2a47">{K_MAIN}</div>
  <div class="serif" style="font-size:48px;color:#d8432a;margin-top:12px">{K_TAIL}</div>
</div>
{meta('5 FİLM · 23 KASIM · KAYDIR →', '#0e2a47')}{logo('black')}
""", "#d8e8ee")


def k_b():  # kontakt baskı: 6 kare ızgara, kırmızı kalem işaretleri
    cells = [("romanholiday_3", "45% 40%"), ("cmbyn_3", "50% 50%"), ("mammamia_4", "50% 40%"), ("ferris_3", "50% 40%"), ("darjeeling_1", "40% 50%"), ("cmbyn_2", "50% 50%")]
    g = "".join(f'<div style="position:relative;{ph(n,p)}">{"<div style=&quot;position:absolute;inset:6px;border:5px solid #ff3b2f;border-radius:50%&quot;></div>" if i in (1, 4) else ""}<div style="position:absolute;left:8px;bottom:6px;font:600 16px Inter;color:#ffd36b">{i+12}A</div></div>' for i, (n, p) in enumerate(cells))
    return page(f"""
<div class="abs" style="inset:0;background:#141414"></div>
<div class="abs" style="left:40px;right:40px;top:50px;height:700px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr);gap:12px">{g}</div>
<div class="abs" style="left:64px;right:64px;top:800px">
  <div style="font:400 64px/1.06 Anton;text-transform:uppercase;color:#fff">{K_MAIN}</div>
  <div class="serif" style="font-size:48px;color:#ffd36b;margin-top:12px">{K_TAIL}</div>
</div>
{meta('5 FİLM · 23 KASIM · KAYDIR →', '#fff')}{logo()}
""", "#141414")


def k_c():  # düz sarı afiş + yuvarlak kare + dev "2"
    return page(f"""
<div class="abs" style="inset:0;background:#ffd23f"></div>
<div class="abs" style="left:-30px;top:-70px;font:400 760px/1 Anton;color:#0e2a47">2</div>
<div class="abs" style="left:430px;top:110px;width:600px;height:600px;border-radius:50%;{ph('romanholiday_1','35% 55%')};border:12px solid #fff;box-shadow:0 20px 50px rgba(14,42,71,.3)"></div>
<div class="abs" style="left:64px;right:64px;top:820px">
  <div style="font:400 62px/1.06 Anton;text-transform:uppercase;color:#0e2a47">{K_MAIN}</div>
  <div class="serif" style="font-size:48px;color:#d8432a;margin-top:12px">{K_TAIL}</div>
</div>
{meta('GÜNLÜK KAÇIŞ · 5 FİLM · 23 KASIM', '#0e2a47')}{logo('black')}
""", "#ffd23f")


SETS = [("02_ghostlanma", [g_a, g_b, g_c]), ("06_tesaduf", [t_a, t_b, t_c]), ("07_film-gecesi", [f_a, f_b, f_c]),
        ("08_tek-kisilik-sofra", [s_a, s_b, s_c]), ("09_iki-gunluk-kacis", [k_a, k_b, k_c])]

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

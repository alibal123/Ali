"""Kişiselleştirilmiş liste serisi — her kapak kendi fikriyle (arayüz/nesne + gerçek sahne karesi).
Kullanım: python3 tools/seri3/kapak2.py <çıktı_klasörü> [1 2 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
REPO = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
import render2
from playwright.sync_api import sync_playwright

ST = f"file://{REPO}/assets/stills"
LOGO = f"file://{REPO}/assets/logo"


def P(name):
    return f"{ST}/w_{name}.jpg"


BASE = render2.CSS + """
body{font-family:'Inter',sans-serif;color:#fff}
.abs{position:absolute}
.anton{font-family:'Anton',sans-serif;font-weight:400}
.serif{font-family:'Playfair Display',serif;font-style:italic;font-weight:700}
.osw{font-family:'Oswald',sans-serif;font-weight:500;letter-spacing:.18em;text-transform:uppercase}
.gro{font-family:'Space Grotesk',sans-serif}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.tag{position:absolute;left:64px;top:56px;font:500 22px 'Oswald';letter-spacing:.2em;padding:9px 16px;border-radius:4px}
.logo{position:absolute;right:56px;bottom:50px;width:64px;height:64px}
.swipe{position:absolute;left:64px;bottom:66px;font:500 20px 'Oswald';letter-spacing:.24em;opacity:.7}
.ic{display:inline-block;vertical-align:middle}
"""


def page(body, bg="#000"):
    return f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{BASE}</style></head><body style="background:{bg}">{body}</body></html>'


def chrome(date, tagbg, tagfg, logo="white", swipe_color="#fff"):
    return (f'<div class="tag" style="background:{tagbg};color:{tagfg}">5 FİLM · {date}</div>'
            f'<img class="logo" src="{LOGO}/{logo}.png">'
            f'<div class="swipe" style="color:{swipe_color}">KAYDIR →</div>')


EN = lambda s: f"<span lang='en'>{s}</span>"

# ---------------------------------------------------------------- 1. Situationship: gönderilmemiş mesaj
def c1():
    return page(f"""
<div class="bg" style="background-image:url({P('pastlives_1')});filter:saturate(.85) brightness(.55)"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(10,14,30,.25) 0%,rgba(10,14,30,.15) 35%,rgba(12,14,28,.92) 70%)"></div>
<div class="abs" style="left:150px;top:150px;width:780px;padding:34px 34px 30px;border-radius:44px;background:rgba(245,245,250,.13);backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);border:1px solid rgba(255,255,255,.18);box-shadow:0 30px 80px rgba(0,0,0,.35)">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:26px">
    <div style="width:58px;height:58px;border-radius:50%;background:url({P('pastlives_2')}) 60% 30%/cover"></div>
    <div><div style="font:700 26px Inter">O</div><div style="font:500 19px Inter;opacity:.65">çevrimiçi</div></div>
  </div>
  <div style="display:flex;flex-direction:column;gap:12px;font:500 27px/1.3 Inter">
    <div style="align-self:flex-start;background:rgba(255,255,255,.22);padding:14px 22px;border-radius:26px 26px 26px 8px">dün akşam çok güzeldi</div>
    <div style="align-self:flex-end;background:#e4572e;padding:14px 22px;border-radius:26px 26px 8px 26px">bence de :)</div>
    <div style="align-self:flex-start;background:rgba(255,255,255,.22);padding:14px 22px;border-radius:26px 26px 26px 8px">haftaya yine görüşelim mi</div>
    <div style="align-self:flex-end;background:#e4572e;padding:14px 22px;border-radius:26px 26px 8px 26px">olur tabii</div>
  </div>
  <div style="margin-top:26px;display:flex;align-items:center;gap:14px;background:rgba(0,0,0,.35);border-radius:40px;padding:14px 16px 14px 28px;font:500 30px Inter">
    <span>biz neyiz?</span><span style="width:3px;height:34px;background:#fff;display:inline-block"></span>
    <span style="flex:1"></span>
    <span style="font:600 17px Inter;letter-spacing:.08em;opacity:.6;text-transform:uppercase">taslak · 3 ay</span>
    <span style="width:52px;height:52px;border-radius:50%;background:rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center">
      <svg width="24" height="24" viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".45"/></svg></span>
  </div>
</div>
<div class="abs" style="left:64px;right:64px;top:838px">
  <div class="anton" style="font-size:66px;line-height:1.08;text-transform:uppercase">{EN('Situationship')}'in üçüncü ayında “biz neyiz” diye sormaya korkanların,</div>
  <div class="serif" style="font-size:54px;line-height:1.12;color:#ff8a65;margin-top:10px">cevabı perdede arayacağı filmler</div>
</div>
{chrome('7 KASIM', '#e4572e', '#fff')}
""")


# ---------------------------------------------------------------- 2. Ghost: tekrar modunda şarkı
def c2():
    return page(f"""
<div class="bg" style="background-image:url({P('eternal_2')});filter:blur(40px) brightness(.45) saturate(1.3);transform:scale(1.2)"></div>
<div class="abs" style="left:64px;right:64px;top:132px;display:flex;align-items:center;gap:18px;padding:22px 26px;border-radius:30px;background:rgba(30,30,36,.72);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,.1)">
  <div style="width:56px;height:56px;border-radius:50%;background:url({P('eternal_1')}) 70% 30%/cover"></div>
  <div style="flex:1"><div style="font:700 25px Inter">Mesajlar</div><div style="font:500 22px Inter;opacity:.7">Sen: naber, bu akşam müsait misin?</div></div>
  <div style="font:600 20px Inter;color:#8e8e93;text-align:right">Görüldü<br>3 gün önce</div>
</div>
<div class="abs" style="left:150px;top:290px;width:780px;height:520px;border-radius:28px;background:url({P('eternal_2')}) 50% 40%/cover;box-shadow:0 40px 90px rgba(0,0,0,.55)"></div>
<div class="abs" style="left:150px;top:836px;width:780px">
  <div style="display:flex;justify-content:space-between;align-items:flex-end">
    <div><div style="font:800 36px Inter">Aynı Şarkı</div><div style="font:500 24px Inter;opacity:.65;margin-top:4px">Kalbim · Tekrar modunda</div></div>
    <div style="font:700 22px Inter;color:#ff4d8d;background:rgba(255,77,141,.15);padding:8px 14px;border-radius:12px">47. kez</div>
  </div>
  <div style="margin-top:22px;height:7px;border-radius:4px;background:rgba(255,255,255,.2)"><div style="width:72%;height:100%;border-radius:4px;background:#fff"></div></div>
  <div style="display:flex;justify-content:space-between;font:600 18px Inter;opacity:.55;margin-top:8px"><span>2:41</span><span>-1:03</span></div>
  <div style="display:flex;justify-content:center;align-items:center;gap:66px;margin-top:6px">
    <svg width="38" height="38" viewBox="0 0 24 24"><path d="M6 5v14M19 5L9 12l10 7z" fill="#fff" stroke="#fff" stroke-width="1.5"/></svg>
    <svg width="66" height="66" viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16" rx="1" fill="#fff"/><rect x="14" y="4" width="4" height="16" rx="1" fill="#fff"/></svg>
    <svg width="38" height="38" viewBox="0 0 24 24"><path d="M18 5v14M5 5l10 7-10 7z" fill="#fff" stroke="#fff" stroke-width="1.5"/></svg>
    <svg width="40" height="40" viewBox="0 0 24 24" style="position:absolute;right:0"><path d="M17 2l4 4-4 4M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4M21 13v2a3 3 0 0 1-3 3H3" stroke="#ff4d8d" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/><text x="12" y="14.5" font-size="7" font-weight="800" text-anchor="middle" fill="#ff4d8d" font-family="Inter">1</text></svg>
  </div>
</div>
<div class="abs" style="left:64px;right:64px;top:1072px">
  <div class="anton" style="font-size:44px;line-height:1.1;text-transform:uppercase">{EN('Ghost')}landıktan sonra üç gün boyunca aynı şarkıyı dinleyenlerin, <span class="serif" style="text-transform:none;color:#ff4d8d;font-size:44px">terapiye gitmeden önce izlemesi gereken filmler</span></div>
</div>
{chrome('9 KASIM', '#ff4d8d', '#fff')}
""", "#16121a")


# ---------------------------------------------------------------- 3. Red flag: profil kartı ve bayraklar
def flag(c="#e10600", s=30):
    return f'<svg class="ic" width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M5 21V4" stroke="#111" stroke-width="2.2" stroke-linecap="round"/><path d="M5 4h12l-2.5 4L17 12H5z" fill="{c}"/></svg>'


def c3():
    traits = ["Her şeyi kontrol etmek ister", "“Benim için değişeceksin” der", "Hayatına fazla hızlı girer", "Senden çok senin evini sever"]
    rows = "".join(f'<div style="display:flex;align-items:center;gap:16px;padding:16px 0;border-top:1.5px solid #ece6dc;font:600 28px Inter;color:#1a1a1a">{flag()}<span>{t}</span></div>' for t in traits)
    return page(f"""
<div class="abs" style="inset:0;background:#f4efe6"></div>
<div class="abs" style="left:-40px;top:-60px;font:400 520px/1 Anton;color:#e10600;opacity:.07;letter-spacing:-.02em">RED</div>
<div class="abs" style="left:140px;top:150px;width:800px;background:#fff;border-radius:34px;box-shadow:0 30px 70px rgba(60,20,10,.18);overflow:hidden;transform:rotate(-2.2deg)">
  <div style="height:420px;background:url({P('ripley_1')}) 30% 35%/cover;position:relative">
    <div style="position:absolute;left:28px;bottom:22px;font:800 46px Inter;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.6)">Tom, 25 <span style="font:500 26px Inter;opacity:.9">· Roma</span></div>
    <div style="position:absolute;right:24px;top:22px;background:#e10600;color:#fff;font:700 20px Inter;padding:8px 16px;border-radius:30px;letter-spacing:.05em">4 UYARI</div>
  </div>
  <div style="padding:8px 34px 24px">{rows}</div>
</div>
<div class="abs" style="left:770px;top:110px;transform:rotate(14deg)">{flag('#e10600',150)}</div>
<div class="abs" style="left:64px;right:64px;top:1000px">
  <div class="anton" style="font-size:52px;line-height:1.08;color:#111;text-transform:uppercase">{EN('Red flag')}'i görüp “ama ben onu değiştiririm” diyenlerin,</div>
  <div class="serif" style="font-size:44px;color:#e10600;margin-top:8px">bu cümlenin sonunu önceden izleyeceği filmler</div>
</div>
{chrome('11 KASIM', '#111', '#fff', logo='black', swipe_color='#111')}
""", "#f4efe6").replace('<div class="swipe"', '<div class="swipe" style="display:none"')


# ---------------------------------------------------------------- 4. Sessize al: sohbet listesi
def bell():
    return '<svg class="ic" width="26" height="26" viewBox="0 0 24 24"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4M3 3l18 18" stroke="#9aa39a" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'


def c4():
    chats = [("Aile", "Annen: akşama geliyor musun?", "128"), ("Ofis · Proje", "Pazartesi toplantı 09:00'a alındı", "99+"),
             ("Liseden Kızlar", "Fotoğraf", "56"), ("Halı saha", "Bu hafta kim var?", "34")]
    rows = "".join(f'''<div style="display:flex;align-items:center;gap:20px;padding:20px 28px;border-top:1px solid rgba(255,255,255,.08)">
      <div style="width:66px;height:66px;border-radius:50%;background:#2a3a33;display:flex;align-items:center;justify-content:center;font:700 28px Inter;color:#9bd34a">{n[0]}</div>
      <div style="flex:1;min-width:0"><div style="font:700 27px Inter">{n}</div><div style="font:500 22px Inter;opacity:.55;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{m}</div></div>
      <div style="display:flex;flex-direction:column;align-items:flex-end;gap:8px">{bell()}<span style="background:#4b544e;color:#dfe5df;font:700 19px Inter;padding:4px 12px;border-radius:20px">{c}</span></div></div>''' for n, m, c in chats)
    return page(f"""
<div class="bg" style="background-image:url({P('intowild_3')});background-position:50% 50%"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05),rgba(0,0,0,0) 30%,rgba(8,18,13,.9) 72%)"></div>
<div class="abs" style="left:130px;top:150px;width:820px;border-radius:34px;background:rgba(14,22,18,.86);backdrop-filter:blur(16px);box-shadow:0 30px 80px rgba(0,0,0,.5);overflow:hidden">
  <div style="padding:24px 28px 18px;display:flex;justify-content:space-between;align-items:center"><span style="font:800 34px Inter">Sohbetler</span><span style="font:600 20px Inter;color:#9bd34a">Tümü sessizde</span></div>
  {rows}
</div>
<div class="abs" style="left:64px;right:64px;top:930px">
  <div class="anton" style="font-size:54px;line-height:1.08;text-transform:uppercase">Grup sohbetini sessize alıp kimseye haber vermeden kaybolmak isteyenlerin,</div>
  <div class="serif" style="font-size:46px;color:#b8e86a;margin-top:8px">kaybolmayı en güzel anlatan filmler</div>
</div>
{chrome('13 KASIM', '#9bd34a', '#0f1c17')}
""", "#0f1c17")


# ---------------------------------------------------------------- 5. Dört yıldız: film günlüğü kartı
def star(fill, s=46):
    return f'<svg class="ic" width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z" fill="{fill}"/></svg>'


def c5():
    stars = star("#00c66b") * 4 + star("#3a3f4a")
    posters = "".join(f'<div style="flex:1;height:170px;border-radius:8px;background:url({P(p)}) {pos}/cover;border:1px solid rgba(255,255,255,.12)"></div>'
                      for p, pos in [("worstperson_2", "50% 30%"), ("eeaao_1", "40% 30%"), ("portrait_4", "50% 30%"), ("banshees_1", "50% 30%")])
    return page(f"""
<div class="abs" style="inset:0;background:radial-gradient(1200px 700px at 80% -10%,#3b2d78 0%,#14121f 60%)"></div>
<div class="abs" style="left:110px;top:140px;width:860px;border-radius:30px;background:#1e2230;box-shadow:0 30px 80px rgba(0,0,0,.5);overflow:hidden;border:1px solid rgba(255,255,255,.07)">
  <div style="display:flex;gap:30px;padding:34px">
    <div style="width:250px;height:375px;border-radius:12px;background:url({P('aftersun_4')}) 40% 50%/cover;flex:none;box-shadow:0 12px 30px rgba(0,0,0,.45)"></div>
    <div style="flex:1;display:flex;flex-direction:column">
      <div style="font:600 20px Inter;color:#9aa3b5">Günlük · dün gece 02:47</div>
      <div style="font:800 46px Inter;margin-top:10px;line-height:1.05">{EN('Aftersun')} <span style="font:500 28px Inter;color:#9aa3b5">2022</span></div>
      <div style="margin-top:20px">{stars}</div>
      <div style="margin-top:22px;font:500 33px/1.35 'Playfair Display';font-style:italic;color:#eef0f6">“bu film beni biraz bozdu”</div>
      <div style="flex:1"></div>
      <div style="display:flex;gap:26px;font:600 21px Inter;color:#9aa3b5;align-items:center">
        <span><svg class="ic" width="24" height="24" viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-9.5-9.2C1 8 3.5 4.5 7 4.5c2 0 3.6 1.1 5 3 1.4-1.9 3-3 5-3 3.5 0 6 3.5 4.5 7.3C19.5 16.4 12 21 12 21z" fill="#ff8000"/></svg> 2.418</span>
        <span>yeniden izlenecek</span></div>
    </div>
  </div>
  <div style="padding:0 34px 30px"><div style="font:600 18px Inter;letter-spacing:.14em;color:#9aa3b5;margin-bottom:12px">AYNI HİSSİ VERENLER</div><div style="display:flex;gap:12px">{posters}</div></div>
</div>
<div class="abs" style="left:64px;right:64px;top:1004px">
  <div class="anton" style="font-size:54px;line-height:1.08;text-transform:uppercase">{EN('Letterboxd')}'da dört yıldız verip “bu film beni biraz bozdu” yorumu yazdıran <span class="serif" style="text-transform:none;color:#a796ff">filmler</span></div>
</div>
{chrome('15 KASIM', '#8f7bff', '#fff')}
""", "#14121f")


# ---------------------------------------------------------------- 6. Tesadüf: kaydırılan kartlar
def c6():
    ghosts = "".join(f'<div class="abs" style="left:{250+dx}px;top:{170+dy}px;width:580px;height:740px;border-radius:30px;background:#d9d4cb;transform:rotate({r}deg);box-shadow:0 10px 30px rgba(0,0,0,.08);display:flex;align-items:flex-end;padding:30px"><div style="width:100%"><div style="height:24px;width:55%;background:#c7c1b6;border-radius:6px"></div><div style="height:18px;width:35%;background:#c7c1b6;border-radius:6px;margin-top:12px"></div></div></div>'
                     for dx, dy, r in [(-60, 20, -9), (60, 10, 7), (-20, 0, -3)])
    return page(f"""
<div class="abs" style="inset:0;background:#efe9df"></div>
{ghosts}
<div class="abs" style="left:250px;top:150px;width:580px;height:740px;border-radius:30px;background:url({P('amelie_4')}) 55% 30%/cover;transform:rotate(4deg) translateX(40px);box-shadow:0 30px 70px rgba(30,60,60,.35);overflow:hidden">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(0,0,0,.75))"></div>
  <div style="position:absolute;left:30px;bottom:30px;right:30px">
    <div style="font:800 46px Inter;color:#fff">Amélie, 23</div>
    <div style="font:500 24px Inter;color:#fff;opacity:.85;margin-top:4px">Montmartre · seni çoktan fark etti</div>
  </div>
  <div style="position:absolute;left:28px;top:34px;border:5px solid #1fb5a8;color:#1fb5a8;font:800 40px Inter;padding:4px 16px;border-radius:12px;transform:rotate(-14deg);background:rgba(255,255,255,.12)">TESADÜF</div>
</div>
<div class="abs" style="left:64px;right:64px;top:960px">
  <div class="anton" style="font-size:50px;line-height:1.08;color:#14201f;text-transform:uppercase">{EN('Dating')} uygulamasında kaydırdıkça insanların birbirine benzediğini fark edenlere,</div>
  <div class="serif" style="font-size:44px;color:#1f8a8a;margin-top:8px">gerçek bir tesadüfün büyüsünü hatırlatan filmler</div>
</div>
{chrome('17 KASIM', '#1f8a8a', '#fff', logo='black', swipe_color='#14201f')}
""", "#efe9df").replace('<div class="swipe"', '<div class="swipe" style="display:none"')


# ---------------------------------------------------------------- 7. Film gecesi: acil durum listesi
def chk(done):
    if done:
        return '<svg class="ic" width="34" height="34" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="6" fill="#e0218a"/><path d="M7 12.5l3.2 3.2L17 9" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return '<svg class="ic" width="34" height="34" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5.5" fill="none" stroke="#c9a3b4" stroke-width="2"/></svg>'


def c7():
    items = [(1, "Dondurma (en büyük boy)"), (1, "Peçete, bir paket daha"), (1, "Eski fotoğraflar arşive kaldırıldı"), (1, "Telefonu benim çantama koy"), (0, "Film: ağlatmayacak bir şey"), (0, "Film: tamam, biraz ağlatsın")]
    rows = "".join(f'<div style="display:flex;align-items:center;gap:18px;padding:13px 0;font:500 30px Inter;color:{"#8a7480" if d else "#2a1a22"};{"text-decoration:line-through;text-decoration-color:rgba(138,116,128,.6)" if d else ""}">{chk(d)}<span>{t}</span></div>' for d, t in items)
    return page(f"""
<div class="abs" style="inset:0;background:linear-gradient(160deg,#ffd6e6,#f7a8c8)"></div>
<div class="abs" style="right:-120px;top:120px;width:560px;height:700px;border-radius:30px;background:url({P('legallyblonde_4')}) 50% 30%/cover;transform:rotate(7deg);box-shadow:0 30px 60px rgba(120,20,60,.3)"></div>
<div class="abs" style="left:64px;top:150px;width:700px;background:#fffaf2;border-radius:28px;padding:34px 38px 26px;box-shadow:0 30px 70px rgba(120,20,60,.28);transform:rotate(-2deg)">
  <div style="font:600 20px Inter;color:#b07a92">Notlar · bugün 21:14</div>
  <div style="font:800 44px Inter;color:#2a1a22;margin:8px 0 14px">ACİL: film gecesi</div>
  {rows}
</div>
<div class="abs" style="left:64px;right:64px;top:930px">
  <div class="anton" style="font-size:52px;line-height:1.08;color:#2a0f1c;text-transform:uppercase">Arkadaşının ilişkisi bittiğinde “tamam, film gecesi yapıyoruz” diyen herkesin,</div>
  <div class="serif" style="font-size:46px;color:#b5006a;margin-top:8px">kimsenin ağlamadan bitiremediği filmler</div>
</div>
{chrome('19 KASIM', '#e0218a', '#fff', logo='black', swipe_color='#2a0f1c')}
""", "#ffd6e6").replace('<div class="swipe"', '<div class="swipe" style="display:none"')


# ---------------------------------------------------------------- 8. Tek kişilik sofra: adisyon
def c8():
    items = [("Mercimek çorbası", "1"), ("Ekmek, yarım", "1"), ("Ayran", "1"), ("Bir film, açık kalsın", "1"), ("Sohbet", "0")]
    rows = "".join(f'<div style="display:flex;justify-content:space-between;padding:7px 0">{a}<span>x{b}</span></div>' for a, b in items)
    zig = "background:linear-gradient(-45deg,transparent 12px,#fbf7ef 0),linear-gradient(45deg,transparent 12px,#fbf7ef 0);background-size:24px 24px;background-repeat:repeat-x;background-position:left bottom"
    return page(f"""
<div class="bg" style="background-image:url({P('lunchbox_4')});background-position:50% 50%;filter:brightness(.6) saturate(.9) sepia(.15)"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(30,20,10,.1),rgba(30,20,10,.15) 40%,rgba(28,20,12,.93) 70%)"></div>
<div class="abs" style="left:300px;top:110px;width:480px;transform:rotate(3deg);filter:drop-shadow(0 26px 40px rgba(0,0,0,.5))">
  <div style="background:#fbf7ef;color:#2a2118;padding:34px 36px 20px;font:500 25px/1.35 'Courier Prime',monospace">
    <div style="text-align:center;font:700 30px 'Courier Prime',monospace;letter-spacing:.1em">EV MUTFAĞI</div>
    <div style="text-align:center;font-size:20px;opacity:.7">Salı · 21:47</div>
    <div style="border-top:2px dashed #b9ad98;margin:16px 0 10px"></div>
    <div style="display:flex;justify-content:space-between"><span>MASA: 1</span><span>KİŞİ: 1</span></div>
    <div style="border-top:2px dashed #b9ad98;margin:10px 0 8px"></div>
    {rows}
    <div style="border-top:2px dashed #b9ad98;margin:10px 0 12px"></div>
    <div style="display:flex;justify-content:space-between;font-weight:700;font-size:28px"><span>TOPLAM</span><span>YETER</span></div>
    <div style="text-align:center;margin-top:16px;font-size:20px;opacity:.75">Afiyet olsun. Yalnız değilsin.</div>
  </div>
  <div style="height:24px;{zig}"></div>
</div>
<div class="abs" style="left:64px;right:64px;top:960px">
  <div class="anton" style="font-size:50px;line-height:1.08;text-transform:uppercase">İşten çıkıp evde tek başına yemek yerken “bu da bir hayat” diyenlere,</div>
  <div class="serif" style="font-size:44px;color:#f2a650;margin-top:8px">tek kişilik sofranın yalnız olmadığını gösteren filmler</div>
</div>
{chrome('21 KASIM', '#d9771f', '#fff')}
""", "#1d1710")


# ---------------------------------------------------------------- 9. İki günlük kaçış: biniş kartı
def c9():
    days = ""
    for d in range(1, 29):
        mark = d in (22, 23)
        days += f'<div style="height:44px;display:flex;align-items:center;justify-content:center;font:600 21px Inter;color:{"#0e1a2b" if mark else "#7d8aa0"};position:relative">{d}{"<span style=&quot;position:absolute;inset:-2px 4px;border:3px solid #ff5a3c;border-radius:50%;transform:rotate(-8deg)&quot;></span>" if mark else ""}</div>'
    return page(f"""
<div class="abs" style="inset:0;background:#cfe6f6"></div>
<div class="abs" style="left:0;top:0;width:1080px;height:560px;background:url({P('romanholiday_3')}) 50% 35%/cover;filter:contrast(1.05)"></div>
<div class="abs" style="left:0;top:380px;width:1080px;height:180px;background:linear-gradient(180deg,rgba(207,230,246,0),#cfe6f6)"></div>
<div class="abs" style="left:64px;top:330px;width:952px;height:300px;background:#fff;border-radius:26px;box-shadow:0 26px 60px rgba(14,26,43,.25);display:flex;overflow:hidden;color:#0e1a2b">
  <div style="flex:1;padding:30px 36px;position:relative">
    <div style="font:700 18px Inter;letter-spacing:.16em;color:#46b6ff">BİNİŞ KARTI · KAÇIŞ HAVAYOLLARI</div>
    <div style="display:flex;align-items:center;gap:26px;margin-top:20px">
      <div><div style="font:400 84px/1 Anton">IST</div><div style="font:600 20px Inter;color:#7d8aa0;margin-top:6px">Ofis, masa 14</div></div>
      <svg width="90" height="30" viewBox="0 0 90 30"><path d="M2 15h80" stroke="#0e1a2b" stroke-width="2.5" stroke-dasharray="6 6"/><path d="M74 6l12 9-12 9" fill="none" stroke="#0e1a2b" stroke-width="3"/></svg>
      <div><div style="font:400 84px/1 Anton">FCO</div><div style="font:600 20px Inter;color:#7d8aa0;margin-top:6px">Roma, bir yerde</div></div>
    </div>
    <div style="display:flex;gap:40px;margin-top:26px">
      <div><div style="font:600 16px Inter;letter-spacing:.12em;color:#7d8aa0">YOLCU</div><div style="font:700 26px Inter">Sen</div></div>
      <div><div style="font:600 16px Inter;letter-spacing:.12em;color:#7d8aa0">İZİN</div><div style="font:700 26px Inter">2 gün</div></div>
      <div><div style="font:600 16px Inter;letter-spacing:.12em;color:#7d8aa0">KOLTUK</div><div style="font:700 26px Inter">Cam kenarı</div></div>
    </div>
  </div>
  <div style="width:0;border-left:3px dashed #d3dbe6;margin:20px 0"></div>
  <div style="width:290px;padding:26px 24px">
    <div style="font:700 16px Inter;letter-spacing:.14em;color:#7d8aa0;text-align:center;margin-bottom:8px">KASIM</div>
    <div style="display:grid;grid-template-columns:repeat(7,1fr)">{days}</div>
  </div>
</div>
<div class="abs" style="left:64px;right:64px;top:700px">
  <div class="anton" style="font-size:68px;line-height:1.06;color:#0e1a2b;text-transform:uppercase">Yıllık izin hesabı yapıp iki günlük tatile bile sevinenlerin,</div>
  <div class="serif" style="font-size:56px;line-height:1.12;color:#ff5a3c;margin-top:12px">kaçmanın bir film kadar iyi geldiğini hatırlatacak filmler</div>
</div>
{chrome('23 KASIM', '#0e1a2b', '#fff', logo='black', swipe_color='#0e1a2b')}
""", "#cfe6f6")


# ---------------------------------------------------------------- 10. Alarm: kilit ekranı
def c10():
    alarms = ["07:00", "07:09", "07:18", "07:27", "07:36"]
    notes = "".join(f'''<div style="display:flex;align-items:center;gap:18px;padding:18px 24px;border-radius:26px;background:rgba(40,36,30,.62);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.08);margin-top:12px;opacity:{1-i*0.14};transform:scale({1-i*0.025})">
      <svg class="ic" width="44" height="44" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#ffb020"/><circle cx="12" cy="13" r="6" stroke="#161310" stroke-width="2" fill="none"/><path d="M12 10v3l2 1.5M5 5l2.5-2M19 5l-2.5-2" stroke="#161310" stroke-width="2" stroke-linecap="round" fill="none"/></svg>
      <div style="flex:1"><div style="font:700 24px Inter">Alarm · {a}</div><div style="font:500 20px Inter;opacity:.65">Bugün her şey değişecek</div></div>
      <div style="font:700 21px Inter;background:rgba(255,255,255,.16);padding:10px 20px;border-radius:30px">Ertele</div></div>''' for i, a in enumerate(alarms))
    return page(f"""
<div class="bg" style="background-image:url({P('groundhog_4')});background-position:60% 40%;filter:brightness(.5) saturate(.9) sepia(.2)"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(22,19,16,.2),rgba(22,19,16,.35) 50%,rgba(22,19,16,.95) 72%)"></div>
<div class="abs" style="left:0;right:0;top:120px;text-align:center">
  <div style="font:600 30px Inter;opacity:.85">Salı, 25 Kasım</div>
  <div style="font:300 170px/1 Inter;letter-spacing:-.02em;margin-top:2px">07:41</div>
</div>
<div class="abs" style="left:150px;right:150px;top:345px">{notes}</div>
<div class="abs" style="left:64px;right:64px;top:930px">
  <div class="anton" style="font-size:52px;line-height:1.08;text-transform:uppercase">Sabah alarmını beş kez erteleyip “bugün her şey değişecek” diye kendine söz verenlerin,</div>
  <div class="serif" style="font-size:44px;color:#ffc04d;margin-top:8px">o sözün peşinden gidenleri anlatan filmler</div>
</div>
{chrome('25 KASIM', '#ffb020', '#161310')}
""", "#161310")



# ---------------------------------------------------------------- 2b. Ghost: albüm kapağı
def c2():
    return page(f"""
<div class="bg" style="background-image:url({P('eternal_3')});background-position:70% 40%;filter:saturate(1.1)"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(15,12,20,.75) 0%,rgba(15,12,20,.1) 38%,rgba(15,12,20,0) 55%,rgba(15,12,20,.85) 82%)"></div>
<div class="abs" style="left:64px;right:64px;top:130px">
  <div style="font:400 64px/1.04 'Archivo Black';letter-spacing:-.01em;text-transform:uppercase">{EN('Ghost')}landıktan sonra üç gün boyunca aynı şarkıyı dinleyenlerin,</div>
  <div class="serif" style="font-size:50px;color:#ff6fa5;margin-top:14px">terapiye gitmeden önce izlemesi gereken filmler</div>
</div>
<div class="abs" style="left:64px;right:64px;top:1046px;display:flex;align-items:center;gap:22px;padding:20px 24px;border-radius:24px;background:rgba(20,16,24,.7);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.1)">
  <div style="width:84px;height:84px;border-radius:12px;background:url({P('eternal_2')}) 50% 40%/cover;flex:none"></div>
  <div style="flex:1">
    <div style="display:flex;justify-content:space-between"><span style="font:700 27px Inter">Aynı şarkı</span><span style="font:700 20px Inter;color:#ff6fa5">47. kez</span></div>
    <div style="font:500 20px Inter;opacity:.6;margin:2px 0 12px">Görüldü · 3 gün önce</div>
    <div style="height:6px;border-radius:3px;background:rgba(255,255,255,.2)"><div style="width:68%;height:100%;border-radius:3px;background:#fff"></div></div>
  </div>
  <svg width="46" height="46" viewBox="0 0 24 24"><path d="M17 2l4 4-4 4M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4M21 13v2a3 3 0 0 1-3 3H3" stroke="#ff6fa5" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/><text x="12" y="14.6" font-size="7" font-weight="800" text-anchor="middle" fill="#ff6fa5" font-family="Inter">1</text></svg>
</div>
<div class="tag" style="background:#ff4d8d;color:#fff;top:auto;bottom:1272px;display:none"></div>
<img class="logo" src="{LOGO}/white.png">
<div class="abs osw" style="left:64px;bottom:62px;font-size:20px;opacity:.75">5 FİLM · 9 KASIM · KAYDIR →</div>
""", "#120f16")


# ---------------------------------------------------------------- 3b. Red flag: düz renk afiş
def c3():
    return page(f"""
<div class="abs" style="inset:0;background:#e10600"></div>
<svg class="abs" style="left:520px;top:60px" width="620" height="760" viewBox="0 0 62 76">
  <path d="M6 74V4" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>
  <path d="M7 5c10-4 18 4 28 0s16-2 22 0v30c-6-2-12-4-22 0s-18-4-28 0z" fill="#fff"/>
</svg>
<div class="abs" style="left:64px;top:150px;width:520px">
  <div class="osw" style="font-size:24px;color:#ffd2cc">Uyarı · 1/1</div>
  <div style="font:400 108px/0.98 Anton;color:#fff;margin-top:16px;text-transform:uppercase">“Ama ben onu değiş­tiririm”</div>
</div>
<div class="abs" style="left:64px;right:64px;top:870px;border-top:3px solid #fff;padding-top:30px">
  <div style="font:700 50px/1.14 Inter;color:#fff;letter-spacing:-.01em">{EN('Red flag')}'i görüp bu cümleyi kuranların,</div>
  <div class="serif" style="font-size:50px;color:#1a0000;margin-top:8px">sonunu önceden izleyeceği filmler</div>
</div>
<img class="logo" src="{LOGO}/white.png">
<div class="abs osw" style="left:64px;bottom:62px;font-size:20px;color:#fff;opacity:.85">5 FİLM · 11 KASIM · KAYDIR →</div>
""", "#e10600")


# ---------------------------------------------------------------- 4b. Sessize al: sinematik tam sayfa
def c4():
    return page(f"""
<div class="bg" style="background-image:url({P('intowild_3')});background-position:46% 50%"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(10,8,4,.72) 0%,rgba(10,8,4,.15) 34%,rgba(10,8,4,0) 60%,rgba(10,8,4,.55) 100%)"></div>
<div class="abs" style="left:64px;right:64px;top:120px;text-align:center">
  <div style="font:700 italic 68px/1.1 'Playfair Display'">Grup sohbetini sessize alıp kimseye haber vermeden kaybolmak isteyenlerin,</div>
  <div style="font:500 28px Oswald;letter-spacing:.3em;text-transform:uppercase;margin-top:26px;color:#ffd08a">kaybolmayı en güzel anlatan filmler</div>
</div>
<div class="abs" style="left:50%;top:1150px;transform:translateX(-50%);display:flex;align-items:center;gap:14px;padding:16px 28px;border-radius:40px;background:rgba(0,0,0,.45);backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.15);font:600 24px Inter;white-space:nowrap">
  <svg width="28" height="28" viewBox="0 0 24 24"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4M3 3l18 18" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg>
  4 grup · süresiz sessize alındı
</div>
<img class="logo" src="{LOGO}/white.png">
<div class="abs osw" style="left:64px;bottom:62px;font-size:20px;opacity:.8">5 FİLM · 13 KASIM</div>
""", "#000")


# ---------------------------------------------------------------- 7b. Film gecesi: el yazısı not
def c7():
    items = [(1, "dondurma (en büyük boy)"), (1, "peçete, bir paket daha"), (1, "eski fotoğraflar: arşivde"), (1, "telefonu bana ver"), (0, "ağlatmayan bir film"), (0, "tamam, biraz ağlatsın")]
    rows = "".join(f'<div style="display:flex;align-items:center;gap:16px;font:700 44px/1.25 Caveat;color:#3a1028;{"text-decoration:line-through;text-decoration-thickness:3px;text-decoration-color:#e0218a" if d else ""}"><span style="font:700 40px Caveat;color:#e0218a">{"✓" if d else "○"}</span>{t}</div>' for d, t in items)
    return page(f"""
<div class="abs" style="inset:0;background:#ffc9dc"></div>
<div class="abs" style="left:-30px;top:640px;width:700px;height:760px;background:url({P('legallyblonde_4')}) 50% 25%/cover;transform:rotate(-6deg);border:18px solid #fff;border-bottom-width:80px;box-shadow:0 20px 50px rgba(120,20,60,.3)"></div>
<div class="abs" style="left:560px;top:820px;width:460px;height:400px;background:url({P('bridget_2')}) 50% 30%/cover;transform:rotate(5deg);border:16px solid #fff;border-bottom-width:64px;box-shadow:0 20px 50px rgba(120,20,60,.3)"></div>
<div class="abs" style="left:64px;right:64px;top:120px">
  <div style="font:400 74px/1.0 'Abril Fatface';color:#2a0f1c">Arkadaşının ilişkisi bittiğinde “tamam, film gecesi yapıyoruz” diyen herkesin,</div>
  <div style="font:700 58px Caveat;color:#d1006f;margin-top:10px;transform:rotate(-1.5deg)">kimsenin ağlamadan bitiremediği filmler</div>
</div>
<div class="abs" style="left:640px;top:470px;width:380px;transform:rotate(3deg);background:#fff59e;padding:24px 26px;box-shadow:0 14px 30px rgba(120,60,20,.2);z-index:3">
  <div style="font:700 40px Caveat;color:#d1006f;margin-bottom:4px">acil liste</div>
  {rows.replace('44px','34px').replace('40px Caveat','32px Caveat')}
</div>
<img class="logo" src="{LOGO}/black.png" style="z-index:5">
<div class="tag" style="background:#e0218a;color:#fff;top:auto;bottom:60px;left:auto;right:140px;z-index:5">5 FİLM · 19 KASIM</div>
""", "#ffc9dc")


# ---------------------------------------------------------------- 9b. Kaçış: seyahat afişi
def c9():
    return page(f"""
<div class="abs" style="inset:0;background:#f3e6c8"></div>
<div class="abs" style="left:48px;top:48px;right:48px;bottom:48px;border:3px solid #0e2a47"></div>
<div class="abs" style="left:80px;top:80px;right:80px;height:640px;background:url({P('romanholiday_3')}) 50% 30%/cover;filter:grayscale(1) contrast(1.15) sepia(.35)"></div>
<div class="abs" style="left:80px;top:80px;right:80px;height:640px;background:#ff5a3c;mix-blend-mode:multiply;opacity:.55"></div>
<div class="abs" style="left:80px;right:80px;top:610px;text-align:center;font:400 190px/1 'Abril Fatface';color:#0e2a47;letter-spacing:.02em">ROMA</div>
<div class="abs" style="left:80px;right:80px;top:790px;display:flex;justify-content:space-between;font:500 22px Oswald;letter-spacing:.26em;color:#0e2a47"><span>İZİN: 2 GÜN</span><span>GİDİŞ: CUMARTESİ</span><span>DÖNÜŞ: PAZAR</span></div>
<div class="abs" style="left:96px;right:96px;top:860px;text-align:center">
  <div style="font:700 46px/1.18 'Playfair Display';color:#0e2a47">Yıllık izin hesabı yapıp iki günlük tatile bile sevinenlerin,</div>
  <div class="serif" style="font-size:42px;color:#d8432a;margin-top:10px">kaçmanın bir film kadar iyi geldiğini hatırlatacak filmler</div>
</div>
<img class="logo" src="{LOGO}/black.png" style="right:96px;bottom:90px;width:56px;height:56px">
<div class="abs osw" style="left:96px;bottom:104px;font-size:20px;color:#0e2a47">5 FİLM · 23 KASIM</div>
""", "#f3e6c8")


# ================================================================ v3: arayüzsüz, film karesi + tipografi (5 hariç)
def foot(date, color="#fff", logo="white"):
    return f'<img class="logo" src="{LOGO}/{logo}.png"><div class="abs osw" style="left:64px;bottom:64px;font-size:20px;color:{color};opacity:.85">5 FİLM · {date} · KAYDIR →</div>'


def c1(BIZ='#ffd36b', TAIL='#9fd3ff'):
    return page(f"""
<div class="bg" style="background-image:url({P('pastlives_3')});background-position:50% 50%"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(8,10,24,.1) 0%,rgba(8,10,24,0) 40%,rgba(8,10,24,.88) 66%)"></div>
<div class="abs" style="left:64px;top:560px;font:700 italic 150px/1 'Playfair Display';color:{BIZ};text-shadow:0 6px 30px rgba(0,0,0,.4)">biz neyiz?</div>
<div class="abs" style="left:64px;right:64px;top:770px">
  <div class="anton" style="font-size:64px;line-height:1.08;text-transform:uppercase">{EN('Situationship')}'in üçüncü ayında “biz neyiz” diye sormaya korkanların,</div>
  <div class="serif" style="font-size:52px;color:{TAIL};margin-top:10px">cevabı perdede arayacağı filmler</div>
</div>
{foot('7 KASIM')}
""")


def c2():
    return page(f"""
<div class="bg" style="background-image:url({P('eternal_1')});background-position:50% 40%;filter:saturate(1.15)"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(14,10,18,.82) 0%,rgba(14,10,18,.35) 40%,rgba(14,10,18,0) 58%,rgba(14,10,18,.7) 100%)"></div>
<div class="abs" style="left:64px;right:64px;top:120px">
  <div style="font:400 62px/1.05 'Archivo Black';text-transform:uppercase">{EN('Ghost')}landıktan sonra üç gün boyunca aynı şarkıyı dinleyenlerin,</div>
  <div class="serif" style="font-size:50px;color:#ff7eb0;margin-top:14px;text-shadow:0 2px 16px rgba(0,0,0,.5)">terapiye gitmeden önce izlemesi gereken filmler</div>
</div>
{foot('9 KASIM')}
""", "#120f16")


def c3():
    return page(f"""
<div class="abs" style="inset:0;background:#e10600"></div>
<div class="abs" style="left:0;top:0;width:1080px;height:620px;background:url({P('saltburn_1')}) 50% 30%/cover;filter:grayscale(1) contrast(1.2) brightness(.95)"></div>
<div class="abs" style="left:0;top:0;width:1080px;height:620px;background:#e10600;mix-blend-mode:multiply"></div>
<svg class="abs" style="left:800px;top:250px" width="210" height="260" viewBox="0 0 62 76">
  <path d="M6 74V4" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
  <path d="M7 5c10-4 18 4 28 0s16-2 22 0v30c-6-2-12-4-22 0s-18-4-28 0z" fill="#fff"/></svg>
<div class="abs" style="left:64px;right:64px;top:690px">
  <div class="anton" style="font-size:76px;line-height:1.04;color:#fff;text-transform:uppercase">{EN('Red flag')}'i görüp “ama ben onu değiştiririm” diyenlerin,</div>
  <div class="serif" style="font-size:52px;color:#2a0000;margin-top:12px">bu cümlenin sonunu önceden izleyeceği filmler</div>
</div>
{foot('11 KASIM')}
""", "#e10600")


def c4():
    return page(f"""
<div class="bg" style="background-image:url({P('intowild_3')});background-position:46% 50%"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(10,8,4,.72) 0%,rgba(10,8,4,.15) 34%,rgba(10,8,4,0) 60%,rgba(10,8,4,.55) 100%)"></div>
<div class="abs" style="left:64px;right:64px;top:120px;text-align:center">
  <div style="font:700 italic 68px/1.1 'Playfair Display'">Grup sohbetini sessize alıp kimseye haber vermeden kaybolmak isteyenlerin,</div>
  <div style="font:500 30px Oswald;letter-spacing:.3em;text-transform:uppercase;margin-top:28px;color:#ffd08a">kaybolmayı en güzel anlatan filmler</div>
</div>
{foot('13 KASIM')}
""")


def c6():
    return page(f"""
<div class="abs" style="inset:0;background:#f1ebe0"></div>
<div class="abs" style="left:0;top:0;width:1080px;height:760px;background:url({P('harrysally_1')}) 50% 50%/cover"></div>
<div class="abs" style="left:64px;right:64px;top:800px">
  <div style="font:400 58px/1.08 'Archivo Black';color:#14201f;text-transform:uppercase;letter-spacing:-.01em">{EN('Dating')} uygulamasında kaydırdıkça insanların birbirine benzediğini fark edenlere,</div>
  <div class="serif" style="font-size:48px;color:#1f8a8a;margin-top:12px">gerçek bir tesadüfün büyüsünü hatırlatan filmler</div>
</div>
{foot('17 KASIM', '#14201f', 'black')}
""", "#f1ebe0")


def c7():
    pol = [("legallyblonde_4", "50% 25%", 40, 640, 470, -7), ("bridget_2", "50% 30%", 540, 600, 420, 5), ("sarahmarshall_4", "50% 40%", 300, 880, 440, -2)]
    ph = "".join(f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{int(w*0.9)}px;background:url({P(n)}) {pos}/cover;transform:rotate({r}deg);border:16px solid #fff;border-bottom-width:60px;box-shadow:0 18px 40px rgba(120,20,60,.3)"></div>' for n, pos, x, y, w, r in pol)
    return page(f"""
<div class="abs" style="inset:0;background:#ffc9dc"></div>
{ph}
<div class="abs" style="left:64px;right:64px;top:110px">
  <div style="font:400 72px/1.02 'Abril Fatface';color:#2a0f1c">Arkadaşının ilişkisi bittiğinde “tamam, film gecesi yapıyoruz” diyen herkesin,</div>
  <div style="font:700 62px Caveat;color:#d1006f;margin-top:12px;transform:rotate(-1.5deg);transform-origin:left">kimsenin ağlamadan bitiremediği filmler</div>
</div>
<img class="logo" src="{LOGO}/black.png" style="z-index:5">
""", "#ffc9dc")


def c8():
    return page(f"""
<div class="abs" style="inset:0;background:#efe4cf"></div>
<div class="abs" style="left:190px;top:90px;width:700px;height:740px;border-radius:350px 350px 0 0;background:url({P('littleforest_4')}) 50% 50%/cover;box-shadow:0 20px 50px rgba(60,40,10,.25)"></div>
<div class="abs" style="left:64px;right:64px;top:870px;text-align:center">
  <div style="font:700 50px/1.16 'Playfair Display';color:#2b1d0e">İşten çıkıp evde tek başına yemek yerken “bu da bir hayat” diyenlere,</div>
  <div class="serif" style="font-size:46px;color:#c2621b;margin-top:12px">tek kişilik sofranın yalnız olmadığını gösteren filmler</div>
</div>
{foot('21 KASIM', '#2b1d0e', 'black')}
""", "#efe4cf")


def c9():
    return page(f"""
<div class="abs" style="inset:0;background:#f3e6c8"></div>
<div class="abs" style="left:48px;top:48px;right:48px;bottom:48px;border:3px solid #0e2a47"></div>
<div class="abs" style="left:80px;top:80px;right:80px;height:560px;background:url({P('romanholiday_3')}) 50% 30%/cover;filter:grayscale(1) contrast(1.15) sepia(.35)"></div>
<div class="abs" style="left:80px;top:80px;right:80px;height:560px;background:#ff5a3c;mix-blend-mode:multiply;opacity:.5"></div>
<div class="abs" style="left:80px;right:80px;top:650px;text-align:center;font:400 170px/1 'Abril Fatface';color:#0e2a47;letter-spacing:.04em">ROMA</div>
<div class="abs" style="left:96px;right:96px;top:840px;text-align:center">
  <div style="font:700 48px/1.18 'Playfair Display';color:#0e2a47">Yıllık izin hesabı yapıp iki günlük tatile bile sevinenlerin,</div>
  <div class="serif" style="font-size:44px;color:#d8432a;margin-top:10px">kaçmanın bir film kadar iyi geldiğini hatırlatacak filmler</div>
</div>
<img class="logo" src="{LOGO}/black.png" style="right:96px;bottom:90px;width:56px;height:56px">
<div class="abs osw" style="left:96px;bottom:104px;font-size:20px;color:#0e2a47">5 FİLM · 23 KASIM</div>
""", "#f3e6c8")


def c10():
    return page(f"""
<div class="bg" style="background-image:url({P('groundhog_3')});background-position:50% 50%;filter:brightness(.9) sepia(.25)"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(18,14,8,0) 30%,rgba(18,14,8,.9) 64%)"></div>
<div class="abs" style="left:64px;right:64px;top:790px">
  <div class="anton" style="font-size:60px;line-height:1.08;text-transform:uppercase">Sabah alarmını beş kez erteleyip “bugün her şey değişecek” diye kendine söz verenlerin,</div>
  <div class="serif" style="font-size:50px;color:#ffc04d;margin-top:10px">o sözün peşinden gidenleri anlatan filmler</div>
</div>
{foot('25 KASIM')}
""", "#161310")


# ================================================================ v4: beğenilen 1 ve 10'un dili (tam sayfa sahne + güçlü başlık), yerleşim ve kanca kapaktan kapağa değişir
def full(still, pos, main, tail, acc, date, place="bottom", hook=None, hook_style="", main_size=62, tail_size=50,
         filt="", grad=None, ink="#fff", logo="white", font="anton", upper=True, align="left", extra=""):
    if grad is None:
        grad = ("linear-gradient(180deg,rgba(10,8,8,.05) 0%,rgba(10,8,8,0) 38%,rgba(10,8,8,.9) 68%)" if place == "bottom"
                else "linear-gradient(180deg,rgba(10,8,8,.88) 0%,rgba(10,8,8,.55) 30%,rgba(10,8,8,0) 52%,rgba(10,8,8,.35) 100%)")
    fam = {"anton": "font-family:Anton;font-weight:400", "archivo": "font-family:'Archivo Black';font-weight:400;letter-spacing:-.01em",
           "playfair": "font-family:'Playfair Display';font-weight:700", "abril": "font-family:'Abril Fatface';font-weight:400"}[font]
    pos_css = "bottom:150px" if place == "bottom" else "top:120px"
    hook_html = f'<div class="abs" style="{hook_style}">{hook}</div>' if hook else ""
    return page(f"""
<div class="bg" style="background-image:url({P(still)});background-position:{pos};{filt}"></div>
<div class="abs" style="inset:0;background:{grad}"></div>
{extra}{hook_html}
<div class="abs" style="left:64px;right:64px;{pos_css};text-align:{align}">
  <div style="{fam};font-size:{main_size}px;line-height:1.08;color:{ink};{'text-transform:uppercase' if upper else ''}">{main}</div>
  <div class="serif" style="font-size:{tail_size}px;line-height:1.14;color:{acc};margin-top:12px">{tail}</div>
</div>
{foot(date, ink, logo)}
""")


def c2():
    return full("her_1", "42% 50%", f"{EN('Ghost')}landıktan sonra üç gün boyunca aynı şarkıyı dinleyenlerin,",
                "terapiye gitmeden önce izlemesi gereken filmler", "#ff7eb0", "9 KASIM",
                hook="görüldü.", hook_style="left:64px;top:560px;font:700 italic 150px/1 'Playfair Display';color:#ff7eb0;opacity:.95;text-shadow:0 6px 30px rgba(0,0,0,.5)",
                main_size=58, filt="filter:saturate(1.1)")


def c3():
    fl = '<svg class="ic" width="62" height="62" viewBox="0 0 24 24" style="margin-right:10px;vertical-align:-6px"><path d="M5 22V3" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><path d="M5.5 3.5h13l-3 4.5 3 4.5h-13z" fill="#ff2a1a"/></svg>'
    return full("ripley_3", "62% 50%", f"{fl}{EN('Red flag')}'i görüp “ama ben onu değiştiririm” diyenlerin,",
                "bu cümlenin sonunu önceden izleyeceği filmler", "#ff5a45", "11 KASIM", place="top", main_size=66,
                filt="filter:saturate(1.15) contrast(1.05)")


def c4():
    return full("nomadland_1", "62% 50%", "Grup sohbetini sessize alıp kimseye haber vermeden kaybolmak isteyenlerin,",
                "kaybolmayı en güzel anlatan filmler", "#ffcf8a", "13 KASIM", place="top", font="playfair", upper=False,
                main_size=64, tail_size=52,
                grad="linear-gradient(180deg,rgba(14,14,30,.85) 0%,rgba(14,14,30,.45) 32%,rgba(14,14,30,0) 55%,rgba(14,14,30,.4) 100%)")


def c5():
    st = "".join(f'<svg width="96" height="96" viewBox="0 0 24 24" style="margin-right:6px"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z" fill="{c}"/></svg>' for c in ["#00e07a"] * 4 + ["rgba(255,255,255,.28)"])
    return full("aftersun_4", "40% 50%", f"{EN('Letterboxd')}'da dört yıldız verip “bu film beni biraz bozdu” yorumu yazdıran",
                "filmler", "#b9a8ff", "15 KASIM", hook=st, hook_style="left:58px;top:600px;display:flex",
                main_size=64, tail_size=60, filt="filter:saturate(1.05)")


def c6():
    return full("chungking_1", "30% 50%", f"{EN('Dating')} uygulamasında kaydırdıkça insanların birbirine benzediğini fark edenlere,",
                "gerçek bir tesadüfün büyüsünü hatırlatan filmler", "#7ff0e0", "17 KASIM", font="archivo", main_size=54,
                hook="tesadüf.", hook_style="left:64px;top:520px;font:700 italic 160px/1 'Playfair Display';color:#ffe14d;text-shadow:0 6px 30px rgba(0,0,0,.45)")


def c7():
    return full("sarahmarshall_4", "45% 50%", "Arkadaşının ilişkisi bittiğinde “tamam, film gecesi yapıyoruz” diyen herkesin,",
                "kimsenin ağlamadan bitiremediği filmler", "#e0218a", "19 KASIM", ink="#2a0f1c", logo="black", main_size=60,
                grad="linear-gradient(180deg,rgba(255,240,246,0) 30%,rgba(255,236,244,.92) 60%,#ffe6f0 74%)")


def c8():
    return full("littleforest_4", "50% 50%", "İşten çıkıp evde tek başına yemek yerken “bu da bir hayat” diyenlere,",
                "tek kişilik sofranın yalnız olmadığını gösteren filmler", "#ffb35c", "21 KASIM", place="top", font="abril",
                upper=False, main_size=64, tail_size=50, filt="filter:saturate(1.05)",
                grad="linear-gradient(180deg,rgba(24,14,6,.9) 0%,rgba(24,14,6,.55) 32%,rgba(24,14,6,0) 55%,rgba(24,14,6,.35) 100%)")


def c9():
    return full("romanholiday_3", "38% 50%", "Yıllık izin hesabı yapıp iki günlük tatile bile sevinenlerin,",
                "kaçmanın bir film kadar iyi geldiğini hatırlatacak filmler", "#8fd0ff", "23 KASIM", main_size=72, tail_size=54,
                filt="filter:contrast(1.1)")


# ================================================================ v5: 2, 4, 6, 7, 8, 9 — Anton başlık + tek güçlü ikon/kanca (1, 3, 5, 10 onaylı)
def svg(path, w, color, sw=0, vb="0 0 24 24", fill=True):
    return (f'<svg width="{w}" height="{w}" viewBox="{vb}">'
            f'<path d="{path}" {"fill=" + chr(34) + color + chr(34) if fill else "fill=" + chr(34) + "none" + chr(34)} stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def c2():
    ticks = ('<svg width="230" height="150" viewBox="0 0 46 30"><path d="M3 16l8 8L27 6M19 22l2 2L37 6" fill="none" stroke="#4fc3ff" '
             'stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    hook = f'{ticks}<div style="font:500 26px Oswald;letter-spacing:.24em;color:#fff;margin-top:6px">GÖRÜLDÜ · 3 GÜN ÖNCE</div>'
    return full("bluevalentine_1", "40% 50%", f"{EN('Ghost')}landıktan sonra üç gün boyunca aynı şarkıyı dinleyenlerin,",
                "terapiye gitmeden önce izlemesi gereken filmler", "#4fc3ff", "9 KASIM", hook=hook,
                hook_style="left:64px;top:470px", main_size=64, filt="filter:saturate(1.1) brightness(.95)")


def c4():
    bell = svg("M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4M3 3l18 18", 150, "#c8f06a", sw=2, fill=False)
    return full("wild_3", "50% 50%", "Grup sohbetini sessize alıp kimseye haber vermeden kaybolmak isteyenlerin,",
                "kaybolmayı en güzel anlatan filmler", "#c8f06a", "13 KASIM", hook=bell, hook_style="left:64px;top:480px;filter:drop-shadow(0 4px 20px rgba(0,0,0,.5))",
                main_size=66, grad="linear-gradient(180deg,rgba(10,12,8,0) 0%,rgba(10,12,8,.15) 34%,rgba(10,12,8,.94) 64%)")


def c6():
    heart = svg("M12 21s-7.5-4.6-9.5-9.2C1 8 3.5 4.5 7 4.5c2 0 3.6 1.1 5 3 1.4-1.9 3-3 5-3 3.5 0 6 3.5 4.5 7.3C19.5 16.4 12 21 12 21z", 150, "#ff3b4e")
    hook = f'<div style="display:flex;align-items:center;gap:22px">{heart}<div style="font:400 92px/1 Anton;color:#fff;text-transform:uppercase">EŞLEŞME<br><span style="font:700 italic 54px Playfair Display;text-transform:none;color:#ffd36b">tesadüfen</span></div></div>'
    return full("amelie_4", "62% 40%", f"{EN('Dating')} uygulamasında kaydırdıkça insanların birbirine benzediğini fark edenlere,",
                "gerçek bir tesadüfün büyüsünü hatırlatan filmler", "#ffd36b", "17 KASIM", hook=hook,
                hook_style="left:64px;top:460px;filter:drop-shadow(0 4px 20px rgba(0,0,0,.45))", main_size=58)


def c7():
    pop = ('<svg width="150" height="170" viewBox="0 0 30 34"><circle cx="9" cy="8" r="5" fill="#fff6dc"/><circle cx="15" cy="5" r="5" fill="#fff"/><circle cx="21" cy="8" r="5" fill="#fff6dc"/>'
           '<circle cx="12" cy="11" r="4.5" fill="#fff"/><circle cx="18" cy="11" r="4.5" fill="#fff"/>'
           '<path d="M4 12h22l-3 21H7z" fill="#ff3d8b"/><path d="M10 12l1.2 21M15 12v21M20 12l-1.2 21" stroke="#fff" stroke-width="1.8"/></svg>')
    hook = f'<div style="display:flex;align-items:flex-end;gap:20px">{pop}<div style="font:400 84px/1 Anton;color:#fff;margin-bottom:8px">FİLM<br>GECESİ</div></div>'
    return full("legallyblonde_4", "58% 30%", "Arkadaşının ilişkisi bittiğinde “tamam, film gecesi yapıyoruz” diyen herkesin,",
                "kimsenin ağlamadan bitiremediği filmler", "#ff7eb6", "19 KASIM", hook=hook,
                hook_style="left:64px;top:470px;filter:drop-shadow(0 4px 22px rgba(80,0,40,.55))", main_size=60,
                grad="linear-gradient(180deg,rgba(40,6,22,0) 0%,rgba(40,6,22,.1) 36%,rgba(40,6,22,.92) 68%)")


def c8():
    hook = ('<div style="display:flex;align-items:center;gap:18px"><svg width="120" height="120" viewBox="0 0 24 24"><path d="M7 2v8a2 2 0 0 0 4 0V2M9 10v12M17 2c-2 1.5-3 4-3 7h3v13" '
            'fill="none" stroke="#ffb35c" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            '<div style="font:400 150px/1 Anton;color:#ffb35c">×1</div></div>')
    return full("lunchbox_4", "78% 50%", "İşten çıkıp evde tek başına yemek yerken “bu da bir hayat” diyenlere,",
                "tek kişilik sofranın yalnız olmadığını gösteren filmler", "#ffb35c", "21 KASIM", hook=hook,
                hook_style="left:64px;top:470px;filter:drop-shadow(0 4px 20px rgba(0,0,0,.55))", main_size=62,
                filt="filter:saturate(.95) sepia(.12)")


def c9():
    plane = svg("M2 16l20-9-6 13-3-5-5 3 1-5z", 120, "#fff")
    hook = f'<div style="display:flex;align-items:center;gap:20px"><div style="font:400 200px/0.9 Anton;color:#fff">2</div><div style="font:400 92px/0.95 Anton;color:#fff">GÜNLÜK<br><span style="color:#ffd36b">KAÇIŞ</span></div></div>'
    return full("mammamia_1", "30% 50%", "Yıllık izin hesabı yapıp iki günlük tatile bile sevinenlerin,",
                "kaçmanın bir film kadar iyi geldiğini hatırlatacak filmler", "#ffd36b", "23 KASIM", hook=hook,
                hook_style="left:64px;top:430px;filter:drop-shadow(0 4px 22px rgba(0,30,60,.5))", main_size=70, tail_size=52,
                grad="linear-gradient(180deg,rgba(6,20,36,0) 0%,rgba(6,20,36,.1) 32%,rgba(6,20,36,.9) 66%)")

COVERS = [("situationship", c1), ("ghostlandin", c2), ("red-flag", c3), ("sessize-al", c4), ("dort-yildiz", c5),
          ("tesaduf", c6), ("film-gecesi", c7), ("tek-kisilik-sofra", c8), ("iki-gunluk-kacis", c9), ("alarm-ertele", c10)]

if __name__ == "__main__":
    out = sys.argv[1]
    sel = [int(x) for x in sys.argv[2:]] or range(1, 11)
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for n in sel:
            name, fn = COVERS[n - 1]
            tmp = os.path.join(HERE, "_k.html")
            open(tmp, "w").write(fn())
            pg.goto("file://" + tmp, wait_until="load")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(500)
            f = os.path.join(out, f"{n:02d}_{name}.jpg")
            pg.screenshot(path=f, type="jpeg", quality=94)
            print(f)
        b.close()

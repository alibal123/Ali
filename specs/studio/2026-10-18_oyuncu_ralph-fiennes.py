from studio import img, GRAIN

ID = "2026-10-18_oyuncu_ralph-fiennes"
FONTS = ["kalam/700.css", "courier-prime/400.css", "courier-prime/700.css", "barlow-condensed/700.css", "barlow-condensed/500.css"]

SCH_B, SCH_C, SCH_F = img("up_schindler_06.jpg"), img("up_schindler_04.jpg"), img("fg_schindler_09.jpg")
BRU = img("bruges_2.jpg")
BUD, BUD2, BUD3 = img("fgx_budapest_16.jpg"), img("fgx_budapest_15.jpg"), img("fgx_budapest_14.jpg")
MENU, MENU2 = img("fg_menu_05.jpg"), img("fg_menu_11.jpg")

CSS = f"""
:root{{--base:#0b0b0b;--edge:#e07a2e;--pencil:#e0282e;--sheet:#f3f1ec}}
body{{background:var(--sheet);color:#111;font-family:'Courier Prime',monospace}}
.sheet{{position:absolute;inset:0;background:var(--sheet)}}
.sheet::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.12;mix-blend-mode:multiply}}
.strip{{position:absolute;left:40px;right:40px;background:var(--base);padding:34px 18px;display:flex;gap:14px}}
.strip::before,.strip::after{{content:'';position:absolute;left:10px;right:10px;height:16px;
 background:repeating-linear-gradient(90deg,transparent 0 14px,#d8d4cc 14px 30px,transparent 30px 44px);border-radius:3px}}
.strip::before{{top:9px}} .strip::after{{bottom:9px}}
.fr{{flex:1;background-size:cover;background-position:center;position:relative}}
.code{{position:absolute;font:700 15px/1 'Courier Prime';color:var(--edge);letter-spacing:.12em}}
.pen{{font:700 46px/1.05 'Kalam';color:var(--pencil)}}
.ring{{position:absolute;border:6px solid var(--pencil);border-radius:48% 52% 45% 55%/55% 45% 55% 45%}}
.lab{{font:700 24px/1 'Barlow Condensed';letter-spacing:.3em;text-transform:uppercase}}
h1{{font:700 120px/0.9 'Barlow Condensed';text-transform:uppercase;letter-spacing:-.01em}}
h2{{font:700 78px/0.95 'Barlow Condensed';text-transform:uppercase}}
p{{font:400 37px/1.42 'Courier Prime'}}
p b{{font-weight:700;background:rgba(224,40,46,.12)}}
"""


def strip(top, h, frames, codes=("14A", "15", "15A")):
    fr = "".join(f"<div class='fr' style='background-image:url(\"{f}\")'></div>" for f in frames)
    cd = "".join(f"<span class='code' style='left:{60 + i * 330}px;bottom:-1px'>▸ {c}</span>" for i, c in enumerate(codes))
    return f"<div class='strip' style='top:{top}px;height:{h}px'>{fr}{cd}<span class='code' style='right:30px;top:-1px'>DF 5219</span></div>"


S1 = f"""<div class='slide'><div class='sheet'></div>
{strip(60, 250, [SCH_B, SCH_C, SCH_F], ("1", "1A", "2"))}
{strip(330, 250, [BRU, BUD2, BUD], ("7", "7A", "8"))}
{strip(600, 250, [BUD3, MENU2, MENU], ("12", "12A", "13"))}
<div class='ring' style='left:722px;top:350px;width:330px;height:220px;transform:rotate(-4deg)'></div>
<div class='ring' style='left:20px;top:70px;width:360px;height:240px;transform:rotate(3deg)'></div>
<div style='position:absolute;left:60px;right:60px;top:940px'>
 <div class='lab'>Aynı oyuncu, farklı film · No. 1</div>
 <h1 style='margin-top:16px;font-size:170px' lang='en'>Ralph Fiennes</h1>
 <div class='pen' style='margin-top:14px;font-size:58px'>Aynı yüz, dört ayrı adam.</div>
</div></div>"""


def role(no, film, meta, char, pic, pos, note, body, ring=None):
    r = ring or (60, 120, 960, 600)
    return f"""<div class='slide'><div class='sheet'></div>
<div class='strip' style='top:60px;height:700px;padding:44px 22px'><div class='fr' style='background-image:url("{pic}");background-position:{pos}'></div>
 <span class='code' style='left:40px;bottom:2px'>▸ {no}</span><span class='code' style='right:30px;top:2px'>DF 5219</span></div>
<div class='pen' style='position:absolute;right:70px;top:690px;transform:rotate(-3deg);background:var(--sheet);padding:4px 16px'>{note}</div>
<div style='position:absolute;left:60px;right:60px;top:820px'>
 <div class='lab' lang='en'>{meta}</div>
 <h2 style='margin-top:12px' lang='en'>{film}</h2>
 <div class='lab' style='margin-top:12px;color:var(--pencil)'>{char}</div>
 <div data-fit style='margin-top:20px;max-height:420px'>{body}</div>
</div></div>"""


S2 = role("1A", "Schindler's List", "Steven Spielberg · 1993", "Amon Göth", SCH_C, "50% 40%", "sakin ses = korku",
          "<p>Bir toplama kampının komutanı. Bağırmıyor, acele etmiyor; <b>en ürkütücü sahneleri sabah kahvesi kadar sıradan</b> oynuyor. Fiennes rol için kilo aldı ve Oscar'a aday gösterildi.</p>")
S3 = role("7", "In Bruges", "Martin McDonagh · 2008", "Harry Waters", BRU, "50% 40%", "Harry burada yok!",
          "<p>Filmin büyük bölümünde yalnızca <b>telefondaki sesi</b> var, ama iki tetikçi de ondan korkuyor. Kendi koyduğu kurallara herkesten çok bağlı, ilkeli ve öfkeli bir patron.</p>")
S4 = role("8", "The Grand Budapest Hotel", "Wes Anderson · 2014", "M. Gustave", BUD, "50% 50%", "komedi de yapar",
          "<p>Şiir okuyan, parfüm kokan, en kaba kelimeleri bile zarafetle söyleyen bir konsiyerj. Göth'ü oynayan adamın <b>bu kadar komik</b> olabileceğini çoğu kişi burada fark etti.</p>")
S5 = role("13", "The Menu", "Mark Mylod · 2022", "Şef <span lang='en'>Julian Slowik</span>", MENU, "35% 40%", "tek alkış",
          "<p>Bir el çırpışıyla bütün mutfağı susturan şef. Masaya yemek değil, <b>bir hesaplaşma</b> servis ediyor. Kibar, titiz ve her an her şeyi kontrol eden bir kötü.</p>")

S6 = f"""<div class='slide'><div class='sheet'></div>
<div style='position:absolute;left:60px;right:60px;top:120px'>
 <div class='lab'>Kesilen kareler</div>
 <h2 style='margin-top:14px'>Sığmayanlar</h2>
 <p style='margin-top:40px;line-height:1.7'>— <span lang='en'>The English Patient</span> (1996): Kont Almásy<br>— <span lang='en'>Harry Potter</span> serisi: Voldemort<br>— <span lang='en'>Conclave</span> (2024): Kardinal Lawrence</p>
 <div class='pen' style='margin-top:40px;transform:rotate(-2deg)'>Biri yüzü olmayan bir kötü, biri âşık bir kâşif, biri vicdanıyla boğuşan bir din adamı.</div>
</div>
{strip(870, 250, [SCH_F, MENU2, BUD2], ("20", "20A", "21"))}
</div>"""

S7 = f"""<div class='slide'><div class='sheet'></div>
<div style='position:absolute;left:70px;right:70px;top:240px'>
 <div class='lab'>Ortak nokta</div>
 <h2 style='margin-top:18px'>FIENNES'İN KÖTÜLERİ BAĞIRMAZ.</h2>
 <p style='margin-top:36px'>Kurallara, düzene ve nezakete bağlıdırlar. Korkutucu olan da bu: Kötülüğü öfkeyle değil, <b>terbiyeyle</b> oynuyor.</p>
 <div class='pen' style='margin-top:70px;font-size:56px;transform:rotate(-2deg)'>Senin favori Fiennes rolün hangisi?</div>
</div>
{strip(1010, 250, [BUD3, SCH_C, MENU], ('30', '30A', '31'))}
</div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7]

CAPTION = """
Ralph Fiennes: aynı yüz, dört ayrı adam. Schindler's List (1993), In Bruges (2008), The Grand Budapest Hotel (2014) ve The Menu (2022) aynı oyuncunun ne kadar farklı insanlara dönüşebildiğini gösteriyor.

Schindler's List'te sakin sesiyle ürküten bir kamp komutanı, In Bruges'de filmin çoğunda yalnızca telefondaki sesiyle korku salan bir patron. Grand Budapest'te şiir okuyan, en kaba kelimeleri zarafetle söyleyen bir konsiyerj, The Menu'de ise tek bir alkışla mutfağı susturan bir şef.

Ortak noktaları şu: Fiennes'in kötüleri bağırmaz. Kurallara, düzene ve nezakete bağlıdırlar; korkutucu olan da bu. Senin favori Fiennes rolün hangisi?

Yarın 20:00'de: Bir pazarlık, bir teslimiyet, bir fedakârlık. Keanu Reeves'in kendini feda ettiği filmler.
"""

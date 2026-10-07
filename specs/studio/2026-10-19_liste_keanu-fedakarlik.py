from studio import img, GRAIN

ID = "2026-10-19_liste_keanu-fedakarlik"
FONTS = ["fraunces/600.css", "fraunces/700.css", "fraunces/400-italic.css", "fraunces/600-italic.css",
         "inter-tight/500.css", "inter-tight/600.css"]

NAVE, PILLS, ORB, CONST, SCALES = (img("ai_08.jpg"), img("ai_09.jpg"), img("ai_10.jpg"), img("ai_11.jpg"), img("ai_12.jpg"))
RAIN, DAWN = img("up_matrixrev_09.jpg"), img("fg_matrixrev_12.jpg")

CSS = f"""
:root{{--stone:#1a1714;--gold:#e0b45a;--glow:#ffdf9e;--txt:#efe6d6}}
body{{background:var(--stone);color:var(--txt);font-family:'Fraunces',serif}}
.stone{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 25%,#3a332b 0%,#1a1714 60%,#0b0a09 100%)}}
.stone::before{{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(0,0,0,.35) 2px,transparent 2px),linear-gradient(90deg,rgba(0,0,0,.3) 2px,transparent 2px);background-size:180px 90px;opacity:.5}}
.stone::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.3;mix-blend-mode:overlay}}
.arch{{position:absolute;left:190px;width:700px;top:80px;height:760px;border-radius:350px 350px 0 0;overflow:hidden;
 box-shadow:0 0 0 18px #2b2621,0 0 0 22px #4a4036,0 0 120px 30px rgba(255,210,140,.18)}}
.arch img{{width:100%;height:100%;object-fit:cover}}
.beam{{position:absolute;left:150px;right:150px;top:700px;height:420px;background:radial-gradient(ellipse at 50% 0%,rgba(255,215,150,.22),transparent 70%);pointer-events:none}}
.kick{{font:600 22px/1 'Inter Tight';letter-spacing:.38em;text-transform:uppercase;color:var(--gold)}}
h1{{font:700 92px/1.0 'Fraunces';letter-spacing:-.01em}}
h2{{font:700 68px/1.02 'Fraunces'}}
.meta{{font:400 italic 32px/1.3 'Fraunces';color:var(--glow);margin-top:10px}}
p{{font:500 37px/1.42 'Inter Tight';color:rgba(239,230,214,.92)}}
p em{{font-family:'Fraunces';font-style:italic;color:var(--glow)}}
.plaque{{position:absolute;left:80px;right:80px;top:895px;bottom:50px;text-align:center}}
"""

S1 = f"""<div class='slide'><img class='cover-img' src='{NAVE}' style='object-position:50% 40%'>
<div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,10,9,0) 40%,rgba(11,10,9,.94) 76%)'></div>
<div style='position:absolute;left:80px;right:80px;bottom:110px'>
 <div class='kick'>Kurtarıcı kompleksi</div>
 <h1 style='margin-top:22px'><span lang='en'>Keanu Reeves</span>'in kendini feda ettiği 4 film</h1>
 <div class='meta'>Kazanmak için değil, başkaları kurtulsun diye kaybetmek için.</div>
</div></div>"""


def film(title, meta, pic, body, pos="center"):
    return f"""<div class='slide'><div class='stone'></div><div class='beam'></div>
<div class='arch'><img src='{pic}' style='object-position:{pos}'></div>
<div class='plaque'><div class='kick' lang='en'>{meta}</div><h2 style='margin-top:18px' lang='en'>{title}</h2>
 <div data-fit style='margin-top:22px;max-height:330px'>{body}</div></div></div>"""


S2 = film("The Matrix Revolutions", "Neo · 2003", PILLS,
          "<p>Neo, Makineler Şehri'ne tek başına gider. Smith'i yenmenin tek yolu ona <em>teslim olmaktır.</em> Neo bunu yapar ve savaş biter.</p>")
S3 = f"""<div class='slide'><img class='cover-img' src='{RAIN}' style='object-position:50% 30%'>
<div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,10,9,.1) 30%,rgba(11,10,9,.92) 72%)'></div>
<div style='position:absolute;left:90px;right:90px;bottom:120px'>
 <p style='font-size:40px'>Matrix üçlemesi boyunca “Seçilmiş Kişi” diye anılan adam, finalde gücünü kazanmak için değil, <em>herkes kurtulsun diye teslim olmak</em> için kullanıyor.</p></div></div>"""
S4 = film("Constantine", "John Constantine · 2005", CONST,
          "<p>Cehenneme gideceğini bilen alaycı bir adam. Kurtuluşu için yıllarca pazarlık eder. Ama sonunda kendi ruhunu, başka birinin ruhu serbest kalsın diye <em>karşılıksız</em> ortaya koyar.</p>")
S5 = film("The Day the Earth Stood Still", "Klaatu · 2008", ORB,
          "<p>Klaatu, insanlığı yok etmek için gelmiştir. İnsanların değişebileceğine inandığı anda kararını geri çevirir. Dünya'yı kurtarmak için <em>kendinden</em> vazgeçer.</p>")
S6 = film("The Devil's Advocate", "Kevin Lomax · 1997", SCALES,
          "<p>Hiç dava kaybetmeyen genç avukat, başarının bedelinin ruhu olduğunu çok geç anlar. Son anda, her şeyi kazanacakken <em>“hayır”</em> der ve bedelini kendisi öder.</p>")

S7 = f"""<div class='slide'><img class='cover-img' src='{DAWN}'>
<div style='position:absolute;inset:0;background:rgba(11,10,9,.55)'></div>
<div style='position:absolute;left:100px;right:100px;top:330px;text-align:center'>
 <div class='kick'>Ortak nokta</div>
 <h2 style='margin-top:26px;font-size:76px'>Kahramanı güçlü yapan, vazgeçebilmesi.</h2>
 <p style='margin-top:34px'>Keanu Reeves'in en sevilen karakterleri yenilmez değil; gerektiğinde geri çekilmeyi bilen adamlar.</p>
 <div class='kick' style='margin-top:70px'>Hangisi seni daha çok etkiledi?</div>
</div></div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7]

CAPTION = """
Keanu Reeves'in kendini feda ettiği filmler: The Matrix Revolutions (2003), Constantine (2005), The Day the Earth Stood Still (2008) ve The Devil's Advocate (1997). Dördünde de karakter kazanmak için değil, başkaları kurtulsun diye kaybetmeye hazır.

Neo savaşı bitirmek için Smith'e teslim oluyor. Constantine, kurtuluşu için yıllarca pazarlık ettikten sonra ruhunu karşılıksız ortaya koyuyor. Klaatu insanlığa ikinci bir şans tanıyıp kendinden vazgeçiyor. Kevin Lomax ise her şeyi kazanacakken “hayır” diyor.

Bu karakterleri güçlü yapan yenilmez olmaları değil, gerektiğinde vazgeçebilmeleri. Hangisi seni daha çok etkiledi?

Yarın 20:00'de: Bitirdikten sonra seni günlerce düşündürecek, hayatı sorgulatan beş film.
"""

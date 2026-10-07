from studio import img, GRAIN

ID = "2026-10-14_film_dogville"
FONTS = ["josefin-sans/300.css", "josefin-sans/600.css", "libre-caslon-text/400.css", "libre-caslon-text/400-italic.css",
         "libre-caslon-text/700.css"]

MAP, WIDE, ROCK, GRACE, DARK, MEET = (img("up_dogville_01.jpg"), img("fg_dogville_04.jpg"), img("fg_dogville_06.jpg"),
                                     img("fg_dogville_08.jpg"), img("fg_dogville_09.jpg"), img("fg_dogville_03.jpg"))

CHALK = """<svg width='0' height='0' style='position:absolute'><filter id='chalk'><feTurbulence type='fractalNoise' baseFrequency='1.1' numOctaves='2' result='n'/>
<feDisplacementMap in='SourceGraphic' in2='n' scale='5'/><feComponentTransfer><feFuncA type='table' tableValues='0 .9 .75 1'/></feComponentTransfer></filter></svg>"""

CSS = f"""
:root{{--floor:#16181a;--chalk:#ecebe6;--cream:#e9e2d2}}
body{{background:var(--floor);color:var(--chalk);font-family:'Josefin Sans',sans-serif}}
.floor{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,#26292c,#0d0e0f 75%)}}
.floor::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.22;mix-blend-mode:screen}}
.ch{{filter:url(#chalk)}}
.lab{{font:600 30px/1 'Josefin Sans';letter-spacing:.28em;text-transform:uppercase}}
.chapter{{font:400 italic 46px/1.35 'Libre Caslon Text';color:var(--cream)}}
.chapter b{{font-style:normal;font-weight:700;font-size:.62em;letter-spacing:.3em;text-transform:uppercase;display:block;margin-bottom:22px;color:#bfb6a2}}
p{{font:400 37px/1.5 'Libre Caslon Text';color:#d9d4c7}}
p em{{color:#fff}}
.box{{position:absolute;border:3px solid var(--chalk);}}
.dash{{position:absolute;border-top:3px dashed var(--chalk)}}
.photo{{position:absolute;background-size:cover;background-position:center}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 35%,rgba(10,10,10,.92) 78%)}}
.big{{font:300 150px/0.9 'Josefin Sans';letter-spacing:.06em;text-transform:uppercase}}
"""

S1 = f"""<div class='slide'>{CHALK}<div class='photo' style='inset:0;background-image:url("{MAP}");background-size:auto 1350px;background-position:38% 50%'></div>
<div class='shade'></div>
<div style='position:absolute;left:80px;right:80px;bottom:110px'>
 <div class='lab ch'>Lars von Trier · 2003</div>
 <div class='big ch' lang='en' style='margin-top:26px'>Dogville</div>
 <p style='margin-top:26px;font-size:38px;font-style:italic'>Duvarı olmayan bir kasaba. Kapısı olmayan evler. Ve her şeyi gören ama hiçbir şey görmemiş gibi yapan insanlar.</p>
</div></div>"""

S2 = f"""<div class='slide'><div class='floor'></div>
<div style='position:absolute;left:110px;right:110px;top:250px'>
 <div class='chapter'><b>Önsöz</b>Bir kasabanın, bir yabancının ve bir sınavın anlatıldığı; dokuz bölümden önce gelen kısa bölüm.</div>
 <div style='height:3px;width:120px;background:#bfb6a2;margin:60px 0'></div>
 <p>1930'lar. Rocky Dağları'nın eteğinde, yolun bittiği yerde küçük bir kasaba: <em>Dogville.</em></p>
 <p style='margin-top:26px'>Bir gece silah sesleri duyulur. Gangsterlerden kaçan Grace (Nicole Kidman) kasabaya sığınır. Kasabalılar onu saklamaya karar verir.</p>
 <p style='margin-top:26px'>Ama bir şartla.</p>
</div></div>"""

S3 = f"""<div class='slide'>{CHALK}<div class='floor'></div>
<div class='ch'>
 <div class='box' style='left:90px;top:170px;width:330px;height:240px'></div>
 <div class='box' style='left:470px;top:170px;width:520px;height:240px'></div>
 <div class='box' style='left:90px;top:470px;width:420px;height:300px'></div>
 <div class='box' style='left:570px;top:470px;width:420px;height:300px;border-style:dashed'></div>
 <div class='dash' style='left:60px;right:60px;top:440px'></div>
 <div class='lab' style='position:absolute;left:115px;top:195px;font-size:24px'>Tom'un evi</div>
 <div class='lab' style='position:absolute;left:495px;top:195px;font-size:24px'>Misyon binası</div>
 <div class='lab' style='position:absolute;left:115px;top:495px;font-size:24px'>Chuck'ın elma bahçesi</div>
 <div class='lab' style='position:absolute;left:595px;top:495px;font-size:21px;letter-spacing:.18em'>Köpek: “Dog”</div>
 <div class='lab' style='position:absolute;left:300px;top:425px;font-size:22px;background:#16181a;padding:0 16px'>Elm St.</div>
</div>
<div style='position:absolute;left:100px;right:100px;top:850px'>
 <div class='lab ch' style='font-size:26px;color:#bfb6a2'>Set</div>
 <p style='margin-top:20px'>Film koca bir stüdyonun siyah zemininde çekildi. Evler yere tebeşirle çizilmiş çizgiler. Kapı yok, ama oyuncular kapıyı açıyormuş gibi yapıyor ve sen <em>gıcırtısını duyuyorsun.</em></p>
 <p style='margin-top:20px'>Köpek bile tebeşirle çizilmiş: “Dog”.</p>
</div></div>"""

S4 = f"""<div class='slide'><div class='photo' style='inset:0;background-image:url("{WIDE}");background-size:auto 1350px;background-position:60% 50%'></div>
<div class='shade' style='background:linear-gradient(180deg,rgba(0,0,0,.1) 30%,rgba(10,10,10,.93) 70%)'></div>
<div style='position:absolute;left:100px;right:100px;bottom:120px'>
 <div class='chapter'><b>Bölüm 2–4</b>Grace'in iyilik yaparak kabul görmeye çalıştığı bölümler.</div>
 <p style='margin-top:34px'>Grace herkese yardım eder: çocuklara ders, bahçeye emek, yaşlılara arkadaşlık. Kasaba onu sever. <em>Sonra her iyilik bir alışkanlığa, her alışkanlık bir borca dönüşür.</em></p>
</div></div>"""

S5 = f"""<div class='slide'>{CHALK}<div class='floor'></div>
<div class='photo' style='left:0;right:0;top:0;height:640px;background-image:url("{DARK}");filter:brightness(1.5)'></div>
<div style='position:absolute;left:0;right:0;top:560px;height:80px;background:linear-gradient(transparent,#16181a)'></div>
<div style='position:absolute;left:100px;right:100px;top:700px'>
 <div class='lab ch' style='font-size:26px;color:#bfb6a2'>Duvarlar neden yok?</div>
 <p style='margin-top:24px;font-size:40px'>Çünkü duvar yoksa kimse <em>“görmedim”</em> diyemez.</p>
 <p style='margin-top:24px'>Grace'e haksızlık yapılırken komşular hemen yan “odada” günlük işine devam ediyor. Kamera onları da gösteriyor. Von Trier'e göre kötülük saklanmıyor; herkesin gözü önünde, sessizce kabul görüyor.</p>
</div></div>"""

S6 = f"""<div class='slide'><div class='photo' style='inset:0;background-image:url("{ROCK}");background-size:auto 1350px;background-position:62% 50%'></div>
<div class='shade' style='background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(10,10,10,.95) 75%)'></div>
<div style='position:absolute;left:100px;right:100px;bottom:120px'>
 <div class='chapter'><b>Bölüm 9</b>Dogville'in bir ziyaret aldığı ve Grace'in bir karar verdiği bölüm.</div>
 <p style='margin-top:34px'>Finali sinema tarihinin en çok tartışılanlarından biri. Soru basit ama cevabı rahatsız edici: <em>Affetmek her zaman erdem midir, yoksa bir tür kibir mi?</em></p>
</div></div>"""

S7 = f"""<div class='slide'>{CHALK}<div class='floor'></div>
<div style='position:absolute;left:110px;right:110px;top:240px;text-align:center'>
 <div class='lab ch' style='color:#bfb6a2'>Bilmeyenler için</div>
 <p style='margin-top:40px'>Dogville, von Trier'in “ABD: Fırsatlar Ülkesi” üçlemesinin ilk filmi. İkincisi <em>Manderlay</em> (2005) geldi; üçüncüsü hiç çekilmedi.</p>
 <div style='height:3px;width:120px;background:#bfb6a2;margin:70px auto'></div>
 <div class='chapter' style='font-size:52px'>Sen Grace olsaydın, Dogville'de kalır mıydın?</div>
 <div class='lab ch' style='margin-top:60px;font-size:24px'>Yorumlara yaz</div>
</div></div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7]

CAPTION = """
Dogville (2003), Lars von Trier'in koca bir stüdyonun siyah zeminine tebeşirle çizdiği bir kasabada geçiyor. Evlerin duvarı, kapıların kendisi yok; oyuncular kapıyı açıyormuş gibi yapıyor, sen gıcırtısını duyuyorsun. Gangsterlerden kaçan Grace (Nicole Kidman) bu kasabaya sığınıyor.

Kasabalılar onu saklamayı kabul ediyor ama karşılığında küçük iyilikler istiyor. Her iyilik bir alışkanlığa, her alışkanlık bir borca dönüşüyor. Duvarlar olmadığı için kimse “görmedim” diyemiyor; kamera, olanlar yaşanırken komşuların günlük işine devam ettiğini de gösteriyor.

Film, iyiliğin, kabullenmenin ve affetmenin sınırını soruyor. Finali hâlâ sinema tarihinin en çok tartışılanlarından biri. Sen Grace olsaydın, Dogville'de kalır mıydın?

Yarın 20:00'de: Türkiye'de çekilmiş, ders kitaplarından çok daha fazlasını anlatan belgeseller.
"""

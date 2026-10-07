from studio import img, GRAIN

ID = "2026-10-21_film_agir-roman"
FONTS = ["anton/400.css", "lobster/400.css", "barlow-condensed/500.css", "barlow-condensed/700.css"]

ALLEY, STILL, SHOE, WEDDING = img("ai_18.jpg"), img("ai_19.jpg"), img("ai_20.jpg"), img("ai_21.jpg")

CANVAS = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
          "<filter id='c'><feTurbulence type='turbulence' baseFrequency='.02 .9' numOctaves='2'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .4 0 0 0 0 .3 0 0 0 .5 0'/></filter>"
          "<rect width='100%25' height='100%25' filter='url(%23c)'/></svg>")

CSS = f"""
:root{{--blood:#8e1b1b;--teal:#0f4d4f;--mustard:#f0b429;--cream:#f6e7c8;--night:#140c0c}}
body{{background:var(--night);color:var(--cream);font-family:'Barlow Condensed',sans-serif}}
.canvas{{position:absolute;inset:0;background:linear-gradient(160deg,#5a1414,#2a0d0d 60%,#140c0c)}}
.canvas::after{{content:'';position:absolute;inset:0;background:url("{CANVAS}");opacity:.35;mix-blend-mode:overlay}}
.paint{{position:absolute;background-size:cover;background-position:center}}
.bill{{font:400 190px/0.86 'Anton';color:var(--mustard);letter-spacing:.01em;text-transform:uppercase;
 text-shadow:6px 6px 0 var(--blood),12px 12px 0 rgba(0,0,0,.55);-webkit-text-stroke:2px #2a0d0d}}
.script{{font:400 68px/1.05 'Lobster';color:var(--cream);text-shadow:3px 3px 0 rgba(0,0,0,.6)}}
.lab{{font:700 28px/1 'Barlow Condensed';letter-spacing:.24em;text-transform:uppercase;color:var(--mustard)}}
h2{{font:400 96px/0.92 'Anton';text-transform:uppercase;color:var(--cream);letter-spacing:.01em}}
p{{font:500 42px/1.3 'Barlow Condensed';color:rgba(246,231,200,.95)}}
p b{{color:var(--mustard);font-weight:700}}
.frame{{position:absolute;border:14px solid #2a1a10;box-shadow:inset 0 0 0 4px var(--mustard),0 24px 50px rgba(0,0,0,.6);background-size:cover;background-position:center}}
.cast{{display:grid;grid-template-columns:1fr 1fr;gap:26px}}
.cast div{{background:rgba(0,0,0,.35);border-left:6px solid var(--mustard);padding:30px 28px}}
.cast b{{display:block;font:400 62px/1 'Anton';text-transform:uppercase;color:var(--cream)}}
.cast span{{font:500 36px/1.2 'Barlow Condensed';color:rgba(246,231,200,.8)}}
.ticket{{position:absolute;background:var(--cream);color:#2a0d0d;border-radius:18px;
 -webkit-mask:radial-gradient(circle 30px at 0 50%,transparent 98%,#000) left/51% 100% no-repeat,radial-gradient(circle 30px at 100% 50%,transparent 98%,#000) right/51% 100% no-repeat}}
"""

S1 = f"""<div class='slide'><div class='paint' style='inset:0;background-image:url("{ALLEY}");background-position:50% 60%'></div>
<div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,12,12,.5) 0%,rgba(20,12,12,0) 30%,rgba(20,12,12,0) 55%,rgba(20,12,12,.9) 85%)'></div>
<div style='position:absolute;left:70px;right:70px;top:80px'><div class='lab'>Mustafa Altıoklar · 1997</div></div>
<div style='position:absolute;left:60px;right:60px;bottom:110px'>
 <div class='script'>Kolera Sokağı'na hoş geldin</div>
 <div class='bill' style='margin-top:18px'>Ağır<br>Roman</div>
</div></div>"""

S2 = f"""<div class='slide'><div class='canvas'></div>
<div class='frame' style='left:90px;right:90px;top:90px;height:600px;background-image:url("{STILL}")'></div>
<div style='position:absolute;left:90px;right:90px;top:760px'>
 <div class='lab'>Romandan filme</div>
 <h2 style='margin-top:16px'>Bir mahalle, kendi kanunu</h2>
 <p style='margin-top:22px'>Metin Kaçan'ın aynı adlı romanından. İstanbul'un dar bir arka sokağı: <b>Kolera Sokağı.</b> Burada berber, tamirci, kabadayı ve çalgıcı aynı kaldırımı paylaşıyor. Polis değil, mahallenin kendi kuralları geçerli.</p>
</div></div>"""

S3 = f"""<div class='slide'><div class='canvas'></div>
<div style='position:absolute;left:80px;right:80px;top:120px'>
 <div class='lab'>Afişteki isimler</div>
 <h2 style='margin:16px 0 50px'>Sokağın sakinleri</h2>
 <div class='cast'>
  <div><b>Salih</b><span>Okan Bayülgen<br>Tamirci, berberin oğlu</span></div>
  <div><b>Tina</b><span>Müjde Ar<br>Sokağa yeni gelen kadın</span></div>
  <div><b>Reis</b><span>Mustafa Uğurlu<br>Mahalleye hükmetmek isteyen kabadayı</span></div>
  <div><b>Berber Ali</b><span>Savaş Dinçel<br>Sokağın saygın büyüğü</span></div>
  <div><b>Arap Sado</b><span>Burak Sergen</span></div>
  <div><b>Puma Zehra</b><span>Aysel Gürel</span></div>
 </div>
 <p style='margin-top:44px'>Küçük İskender'den Zafer Algöz'e uzanan bir kadro. Her yan karakter, ayrı bir filmin başrolü olabilecek kadar renkli.</p>
</div></div>"""

S4 = f"""<div class='slide'><div class='canvas'></div>
<div class='frame' style='left:90px;right:90px;top:90px;height:600px;background-image:url("{SHOE}");background-position:50% 20%;background-size:110% auto'></div>
<div style='position:absolute;left:90px;right:90px;top:760px'>
 <div class='lab'>Hikâye</div>
 <p style='margin-top:20px'>Salih ile Tina'nın aşkı sokağın dengesini bozar. Reis, kendini mahallenin “koruyucusu” ilan eder. Bir yandan da herkes, adını bile anmaya korktuğu <b>“Kolera Canavarı”</b>nı konuşmaktadır.</p>
 <p style='margin-top:18px'>Aşk, onur ve güç; aynı dar sokakta çarpışıyor.</p>
</div></div>"""

S5 = f"""<div class='slide'><div class='paint' style='inset:0;background-image:url("{WEDDING}")'></div>
<div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,12,12,0) 30%,rgba(20,12,12,.94) 68%)'></div>
<div style='position:absolute;left:80px;right:80px;bottom:100px'>
 <div class='lab'>Neden hâlâ konuşuluyor?</div>
 <p style='margin-top:20px'>90'larda seyircinin sinemaya küstüğü bir dönemde, argosu, müziği ve karnaval gibi enerjisiyle ses getirdi. Sokağı süslemeden ama sevgiyle anlattı.</p>
 <p style='margin-top:18px'>35. Antalya Film Festivali'nde <b>üç ödül</b> aldı: Mustafa Uğurlu ve Sevda Ferdağ'a yardımcı oyuncu, filme sanat yönetimi ödülü. Okan Bayülgen ise Sadri Alışık Ödülleri'nde en iyi erkek oyuncu seçildi.</p>
</div></div>"""

S6 = f"""<div class='slide'><div class='canvas'></div>
<div class='ticket' style='left:110px;right:110px;top:300px;height:560px;transform:rotate(-3deg)'>
 <div style='position:absolute;left:70px;right:70px;top:60px;text-align:center'>
  <div style='font:700 26px/1 Barlow Condensed;letter-spacing:.3em;text-transform:uppercase;color:var(--blood)'>Kolera Sokağı Sineması · Tek kişilik</div>
  <div style='font:400 120px/0.9 Anton;text-transform:uppercase;margin-top:30px;color:#2a0d0d'>Ağır Roman</div>
  <div style='border-top:3px dashed #2a0d0d;margin:36px 0 30px'></div>
  <div style='font:400 50px/1.15 Lobster;color:var(--blood)'>Bu sokakta sen kim olurdun?</div>
  <div style='font:500 32px/1.3 Barlow Condensed;margin-top:18px'>Salih mi, Tina mı, Reis mi, Berber Ali mi? Yorumlara yaz.</div>
 </div></div>
<div class='lab' lang='en' style='position:absolute;left:0;right:0;bottom:120px;text-align:center'>derecefilm</div>
</div>"""

SLIDES = [S1, S2, S3, S4, S5, S6]

CAPTION = """
Ağır Roman (1997), Metin Kaçan'ın aynı adlı romanından Mustafa Altıoklar'ın çektiği bir film. İstanbul'un dar bir arka sokağında, “Kolera Sokağı”nda geçiyor. Berber, tamirci, kabadayı ve çalgıcı aynı kaldırımı paylaşıyor; burada polisin değil mahallenin kuralları geçerli.

Tamirci Salih (Okan Bayülgen) ile sokağa yeni gelen Tina'nın (Müjde Ar) aşkı sokağın dengesini bozuyor. Reis (Mustafa Uğurlu) kendini mahallenin koruyucusu ilan ederken herkes adını anmaya korktuğu “Kolera Canavarı”nı konuşuyor. Aşk, onur ve güç aynı dar sokakta çarpışıyor.

90'larda seyircinin sinemadan uzaklaştığı bir dönemde argosu, müziği ve karnaval gibi enerjisiyle ses getirdi; 35. Antalya Film Festivali'nde üç ödül aldı. Bu sokakta sen kim olurdun?

Yarın 20:00'de yeni bir gönderiyle buradayız. Takipte kal.
"""

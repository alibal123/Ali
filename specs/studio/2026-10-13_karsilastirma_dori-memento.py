from studio import img, GRAIN

ID = "2026-10-13_karsilastirma_dori-memento"
FONTS = ["caveat-brush/400.css", "archivo-narrow/500.css", "archivo-narrow/700.css",
         "courier-prime/400.css", "courier-prime/700.css", "caveat/600.css"]

NEMO5, NEMO4, NEMO12, NEMO1 = img("fg_nemo_05.jpg"), img("fg_nemo_04.jpg"), img("fg_nemo_12.jpg"), img("fg_nemo_01.jpg")
POLA, TAT, BW, MOTEL = img("up_memento_01.jpg"), img("up_memento_12.jpg"), img("up_memento_04.jpg"), img("fg_memento_09.jpg")

CSS = f"""
:root{{--sea:#06233f;--sea2:#0b4f78;--wall:#cdbb98;--ink:#1d1a16;--marker:#111}}
body{{font-family:'Archivo Narrow',sans-serif}}
.sea{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% -10%,#3fa7c9 0%,var(--sea2) 35%,var(--sea) 80%)}}
.sea::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.10;mix-blend-mode:overlay}}
.wall{{position:absolute;inset:0;background:var(--wall);
 background-image:repeating-linear-gradient(90deg,rgba(90,60,20,.07) 0 2px,transparent 2px 38px),radial-gradient(ellipse at 70% 15%,rgba(255,240,200,.55),transparent 55%),radial-gradient(ellipse at 10% 100%,rgba(60,40,10,.35),transparent 60%)}}
.wall::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.18;mix-blend-mode:multiply}}
.split{{position:absolute;left:0;right:0}}
.pola{{position:absolute;background:#f4f1ea;padding:22px 22px 110px;box-shadow:0 18px 40px rgba(0,0,0,.45)}}
.pola .ph{{width:100%;height:100%;background-size:cover;background-position:center}}
.pola .cap{{position:absolute;left:24px;right:20px;bottom:18px;font:400 50px/1.0 'Caveat Brush';color:var(--marker)}}
.tape{{position:absolute;width:150px;height:44px;background:rgba(240,230,190,.75);box-shadow:0 2px 4px rgba(0,0,0,.15)}}
.tag{{font:700 24px/1 'Archivo Narrow';letter-spacing:.3em;text-transform:uppercase}}
h1{{font:400 104px/0.98 'Caveat Brush';}}
.card{{position:absolute;background:#fbf8ef;background-image:repeating-linear-gradient(transparent 0 53px,#9cc3e0 53px 55px);
 box-shadow:0 18px 40px rgba(0,0,0,.35);padding:62px 70px 60px;background-position:0 15px;font:400 38px/55px 'Courier Prime';color:#222}}
.card::before{{content:'';position:absolute;left:58px;top:0;bottom:0;width:2px;background:#e88}}
.card b{{font-weight:700}}
.hand{{font:600 44px/1.1 'Caveat'}}
table{{border-collapse:collapse;width:100%}}
td,th{{padding:30px 14px;vertical-align:top;font:500 38px/1.25 'Archivo Narrow';border-bottom:1px solid rgba(255,255,255,.18)}}
th{{font:700 26px/1 'Archivo Narrow';letter-spacing:.25em;text-transform:uppercase;text-align:left;color:#9fd6ee}}
td.k{{font:700 22px/1.6 'Archivo Narrow';letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.6);width:230px}}
.foot{{position:absolute;bottom:40px;left:0;right:0;text-align:center;font:700 20px 'Archivo Narrow';letter-spacing:.4em;text-transform:uppercase}}
"""

S1 = f"""<div class='slide'>
<div class='split sea' style='top:0;height:675px'></div><div class='split wall' style='top:675px;height:675px'></div>
<div class='pola' style='left:90px;top:120px;width:470px;height:560px;transform:rotate(-5deg)'><div class='ph' style='background-image:url("{NEMO5}");background-position:35% 50%;filter:brightness(2.3)'></div><div class='cap'>Dori</div></div>
<div class='pola' style='left:520px;top:520px;width:480px;height:570px;transform:rotate(4deg)'><div class='ph' style='background-image:url("{MOTEL}");background-position:70% 30%'></div><div class='cap'>Leonard</div></div>
<div class='tape' style='left:250px;top:100px;transform:rotate(-8deg)'></div><div class='tape' style='left:700px;top:500px;transform:rotate(6deg)'></div>
<div style='position:absolute;left:600px;top:110px;right:70px;color:#fff'>
 <div class='tag' style='color:#9fd6ee'>Karşılaştırma</div>
 <h1 style='margin-top:20px;color:#fff;font-size:92px'>Aynı hastalık?</h1></div>
<div style='position:absolute;left:80px;bottom:120px;width:420px;color:var(--ink)'>
 <div class='hand' style='font-size:50px'>Biri bir balık,<br>biri bir dul.<br>İkisi de yeni bir şey hatırlayamıyor.</div></div>
</div>"""

S2 = f"""<div class='slide'><div class='wall'></div>
<div class='card' style='left:110px;top:200px;right:110px;transform:rotate(-1.5deg)'>
 <b>ANTEROGRAD AMNEZİ</b><br>
 Beyin eski anıları saklar ama <b>yeni anı</b> kaydedemez.<br>
 Birkaç dakika önce tanıştığın biri, kapıdan çıkıp girdiğinde yeniden yabancıdır.<br>
 Hem Dori hem Leonard bu durumla yaşıyor.<br>
 <span style='color:#b2302a'>Ama ikisi bambaşka iki film çıkarıyor.</span>
</div>
<div class='tape' style='left:470px;top:180px;transform:rotate(3deg)'></div>
<div class='foot' style='color:#5a4a2c'>Kaydır →</div></div>"""

S3 = f"""<div class='slide'><div class='sea'></div>
<img class='cover-img' src='{NEMO1}' style='opacity:.35;mix-blend-mode:screen'>
<div class='pola' style='left:130px;top:110px;width:820px;height:600px;transform:rotate(-2deg)'><div class='ph' style='background-image:url("{NEMO5}");filter:brightness(2.3) contrast(1.1)'></div><div class='cap'>“Kısa süreli hafıza kaybım var.”</div></div>
<div style='position:absolute;left:110px;right:110px;top:820px;color:#e9f6fb'>
 <div class='tag' style='color:#9fd6ee'>Kayıp Balık Nemo · 2003</div>
 <p style='margin-top:22px;font:500 36px/1.35 Archivo Narrow'>Dori unuttuğunu biliyor ve bunu saklamıyor. Hatırlamak istediğini sesli tekrar ediyor: <b>“P. Sherman, 42 Wallaby Way, Sidney.”</b></p>
 <p style='margin-top:20px;font:500 36px/1.35 Archivo Narrow'>Hafızası yok ama güveni var. Yanındakine yaslanarak yol alıyor.</p>
</div></div>"""

S4 = f"""<div class='slide'><div class='wall'></div>
<div class='pola' style='left:80px;top:90px;width:600px;height:540px;transform:rotate(-4deg)'><div class='ph' style='background-image:url("{TAT}");background-position:60% 50%'></div><div class='cap' style='font-size:44px'>Sammy Jankis'i hatırla</div></div>
<div class='pola' style='left:560px;top:250px;width:440px;height:420px;transform:rotate(5deg)'><div class='ph' style='background-image:url("{BW}");filter:grayscale(1)'></div><div class='cap' style='font-size:34px'>Telefondaki kim?</div></div>
<div class='tape' style='left:280px;top:70px;transform:rotate(-5deg)'></div>
<div style='position:absolute;left:100px;right:100px;top:770px;color:var(--ink)'>
 <div class='tag' style='color:#8a2a22'>Memento (Akıl Defteri) · 2000</div>
 <p style='margin-top:22px;font:500 36px/1.35 Archivo Narrow'>Leonard karısının katilini arıyor ama birkaç dakika sonra neden o odada olduğunu bilmiyor. Hafızasını dışarıya kuruyor: <b>Polaroidler, notlar, vücuduna dövmeler.</b></p>
 <p style='margin-top:20px;font:500 36px/1.35 Archivo Narrow'>Nolan filmi geriye doğru anlatıyor; izleyici de Leonard gibi bir önceki sahneyi bilmeden başlıyor.</p>
</div></div>"""

S5 = f"""<div class='slide'>
<div class='split sea' style='top:0;height:1350px'></div>
<div style='position:absolute;left:80px;right:80px;top:200px;color:#fff'>
 <div class='tag' style='color:#9fd6ee'>Yan yana</div>
 <h1 style='margin:18px 0 40px;font-size:80px'>Dori <span style='color:#9fd6ee'>vs</span> Leonard</h1>
 <table>
  <tr><th></th><th>Dori</th><th>Leonard</th></tr>
  <tr><td class='k'>Yöntem</td><td>Tekrar etmek, şarkı söylemek</td><td>Fotoğraf, not, dövme</td></tr>
  <tr><td class='k'>Kime güvenir</td><td>Yanındaki arkadaşa</td><td>Yalnızca kendi el yazısına</td></tr>
  <tr><td class='k'>Tehlike</td><td>Kaybolmak</td><td>Notlarının ona karşı kullanılması</td></tr>
  <tr><td class='k'>Hafızası yerine</td><td>Duygu ve alışkanlık</td><td>Bir amaç: intikam</td></tr>
  <tr><td class='k'>Ton</td><td>Umut</td><td>Paranoya</td></tr>
 </table></div></div>"""

S6 = f"""<div class='slide'><div class='wall'></div>
<div class='card' style='left:100px;top:150px;right:100px;transform:rotate(1deg)'>
 <b>GERÇEKTE NE OLUYOR?</b><br>
 Ünlü hasta H.M., 1953'teki bir beyin ameliyatından sonra yeni anı oluşturamadı.<br>
 Yine de her gün çalıştığı bir çizim görevinde <b>giderek ustalaştı</b>, ama bunu yaptığını hiç hatırlamadı.<br>
 Yani beden ve duygu, bilincin unuttuğunu bir yerde tutuyor.
</div>
<div style='position:absolute;left:110px;right:110px;bottom:130px;color:var(--ink)'>
 <div class='hand' style='font-size:52px'>Kayıp Balık Dori'de (2016) Dori, ailesini istemsizce hatırladığı deniz kabuklarını izleyerek bulur. Leonard ise “koşullanma” ile yaşadığını söyler. İki film de aynı bilimsel gerçeğe dokunuyor.</div>
</div></div>"""

S7 = f"""<div class='slide'>
<div class='split sea' style='top:0;height:675px'></div><div class='split wall' style='top:675px;height:675px'></div>
<div style='position:absolute;left:90px;right:90px;top:170px;color:#fff;text-align:center'>
 <h1 style='font-size:84px'>Unutmak aynı.</h1>
 <p style='margin-top:26px;font:500 38px/1.35 Archivo Narrow;color:#d7eef7'>Dori boşluğu güvenle dolduruyor.</p></div>
<div style='position:absolute;left:90px;right:90px;top:760px;color:var(--ink);text-align:center'>
 <h1 style='font-size:84px'>Doldurmak değil.</h1>
 <p style='margin-top:26px;font:500 38px/1.35 Archivo Narrow'>Leonard boşluğu şüpheyle dolduruyor.</p>
 <p style='margin-top:60px;font:700 26px Archivo Narrow;letter-spacing:.3em;text-transform:uppercase;color:#8a2a22'>Sence hangisi daha gerçekçi?</p></div>
</div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7]

CAPTION = """
Kayıp Balık Nemo (2003) ve Memento (2000), aynı durumun iki zıt yüzünü anlatıyor: anterograd amnezi, yani beynin yeni anı kaydedememesi. Dori bir balık, Leonard karısının katilini arayan bir adam. İkisi de birkaç dakika önce olanı hatırlamıyor.

Dori unuttuğunu saklamıyor; tekrar ediyor, şarkı söylüyor ve yanındakine güveniyor. Leonard ise hafızasını dışarıya kuruyor: Polaroidler, notlar, vücuduna dövmeler. Ama kendi el yazısından başka kimseye güvenmiyor ve bu güven ona karşı kullanılabiliyor.

Gerçek hayatta da beyin unuttuğunu tamamen kaybetmiyor; alışkanlık ve duygu bir yerde kalıyor. Kayıp Balık Dori'deki deniz kabukları da tam olarak bunu anlatıyor. Sence hangisi daha gerçekçi?

Yarın 20:00'de: Duvarları olmayan, yalnızca yere tebeşirle çizilmiş bir kasaba. Lars von Trier'in en acımasız deneyi.
"""

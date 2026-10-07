from studio import img, GRAIN

ID = "2026-10-17_karsilastirma_uzayli-iletisim"
FONTS = ["space-grotesk/500.css", "space-grotesk/700.css", "ibm-plex-mono/400.css", "ibm-plex-mono/500.css"]

PHM, DISH = img("ai_26.jpg"), img("ai_23.jpg")
CE, CONTACT, ARR, ARR2, EARTH = (img("up_closeenc_06.jpg"), img("fg_contact_07.jpg"), img("up_arrival_05.jpg"),
                                 img("fg_arrival_06.jpg"), img("fg_contact_01.jpg"))

CSS = f"""
:root{{--bp:#0f4c81;--bp2:#0a3a63;--line:rgba(255,255,255,.9);--faint:rgba(255,255,255,.14);--amber:#ffc65c}}
body{{background:var(--bp);color:#fff;font-family:'Space Grotesk',sans-serif}}
.bp{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,#1663a6,var(--bp2) 80%);}}
.bp::before{{content:'';position:absolute;inset:0;background-image:linear-gradient(var(--faint) 1px,transparent 1px),linear-gradient(90deg,var(--faint) 1px,transparent 1px),
 linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);
 background-size:120px 120px,120px 120px,24px 24px,24px 24px}}
.bp::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.16;mix-blend-mode:overlay}}
.mono{{font:500 22px/1.3 'IBM Plex Mono';letter-spacing:.12em;text-transform:uppercase}}
h1{{font:700 96px/0.98 'Space Grotesk';letter-spacing:-.02em}}
h2{{font:700 70px/1 'Space Grotesk';letter-spacing:-.01em}}
p{{font:500 34px/1.38 'Space Grotesk';color:rgba(255,255,255,.92)}}
p b{{color:var(--amber);font-weight:700}}
.frame{{position:absolute;border:2px solid var(--line);background-size:cover;background-position:center}}
.frame::before,.frame::after{{content:'';position:absolute;width:40px;height:40px;border:4px solid var(--amber)}}
.frame::before{{left:-12px;top:-12px;border-right:none;border-bottom:none}}
.frame::after{{right:-12px;bottom:-12px;border-left:none;border-top:none}}
.tag{{position:absolute;background:var(--bp2);border:2px solid var(--line);padding:10px 16px}}
.dim{{position:absolute;border-top:2px solid var(--line)}}
.dim::before,.dim::after{{content:'';position:absolute;top:-9px;height:16px;border-left:2px solid var(--line)}}
.dim::before{{left:0}} .dim::after{{right:0}}
.box{{border:2px solid var(--line);padding:40px 34px;min-height:200px}}
.notes{{display:flex;gap:18px;align-items:flex-end;height:140px}}
.notes i{{display:block;width:70px;background:var(--amber);border-radius:6px 6px 0 0}}
table{{width:100%;border-collapse:collapse}}
td,th{{border:2px solid var(--line);padding:34px 20px;text-align:left;vertical-align:top;font:500 36px/1.25 'Space Grotesk'}}
th{{font:500 22px/1 'IBM Plex Mono';letter-spacing:.14em;text-transform:uppercase;color:var(--amber)}}
"""

S1 = f"""<div class='slide'><img class='cover-img' src='{PHM}'>
<div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,58,99,0) 40%,rgba(10,58,99,.94) 74%)'></div>
<div style='position:absolute;left:80px;right:80px;bottom:110px'>
 <div class='mono' style='color:var(--amber)'>Dosya 04 · İletişim protokolü</div>
 <h1 style='margin-top:20px'>Uzaylılarla nasıl konuşulur?</h1>
 <p style='margin-top:22px'><span lang='en'>Project Hail Mary</span>, <span lang='en'>Arrival</span> ve iki klasik: dört film, dört farklı cevap.</p>
</div></div>"""

S2 = f"""<div class='slide'><div class='bp'></div>
<div style='position:absolute;left:90px;right:90px;top:150px'>
 <div class='mono' style='color:var(--amber)'>Problem tanımı</div>
 <h2 style='margin-top:20px'>Ortak dil yok.<br>Ortak beden yok.<br>Belki ortak duyu bile yok.</h2>
 <p style='margin-top:40px'>Karşındakinin ağzı, kulağı, hatta “kelime” diye bir kavramı olmayabilir. O zaman ilk cümleyi neyle kurarsın?</p>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:60px'>
  <div class='box'><div class='mono' style='color:var(--amber)'>Yöntem A</div><p style='margin-top:14px;font-size:48px;font-weight:700'>Müzik</p></div>
  <div class='box'><div class='mono' style='color:var(--amber)'>Yöntem B</div><p style='margin-top:14px;font-size:48px;font-weight:700'>Matematik</p></div>
  <div class='box'><div class='mono' style='color:var(--amber)'>Yöntem C</div><p style='margin-top:14px;font-size:48px;font-weight:700'>Yazı</p></div>
  <div class='box'><div class='mono' style='color:var(--amber)'>Yöntem D</div><p style='margin-top:14px;font-size:48px;font-weight:700'>Bilim + sabır</p></div>
 </div></div></div>"""


def case(code, title, meta, pic, pos, body, extra=""):
    return f"""<div class='slide'><div class='bp'></div>
<div class='frame' style='left:90px;right:90px;top:120px;height:470px;background-image:url("{pic}");background-position:{pos}'></div>
<div class='tag mono' style='left:120px;top:560px'>{code}</div>
<div style='position:absolute;left:90px;right:90px;top:680px'>
 <div class='mono' lang='en' style='color:var(--amber)'>{meta}</div>
 <h2 style='margin-top:14px' lang='en'>{title}</h2>
 <div data-fit style='margin-top:24px;max-height:420px'>{body}</div>{extra}
</div></div>"""


S3 = case("Yöntem A · Müzik", "Close Encounters of the Third Kind", "Steven Spielberg · 1977", CE, "center 40%",
          "<p>Bilim insanları beş notalık bir melodi çalıyor, dev gemi aynı notalarla ve ışıklarla cevap veriyor. Konuşma bir <b>düete</b> dönüşüyor.</p><p style='margin-top:18px'>Film boyunca bir el işareti sistemi de kullanılıyor: notaları elle göstermek.</p>")
S4 = case("Yöntem B · Matematik", "Contact", "Robert Zemeckis · 1997", CONTACT, "center 50%",
          "<p>Vega yıldızından gelen sinyal <b>asal sayılarla</b> başlıyor. Doğada asal sayı üreten bir şey yok; bu, “biz buradayız ve düşünüyoruz” demenin en kısa yolu.</p><p style='margin-top:18px'>Sinyalin içinden bir makinenin planları çıkıyor.</p>")
S5 = case("Yöntem C · Yazı", "Arrival", "Denis Villeneuve · 2016", ARR, "center 55%",
          "<p>Dilbilimci Louise Banks, uzaylıların konuşmasını değil <b>yazısını</b> çözüyor: dairesel, başı ve sonu olmayan semboller.</p><p style='margin-top:18px'>Film bir adım ileri gidiyor: Bir dili öğrenmek, zamanı algılama biçimini de değiştirebilir mi?</p>")
S6 = case("Yöntem D · Bilim + sabır", "Project Hail Mary", "Phil Lord & Christopher Miller · 2026", DISH, "center 40%",
          "<p>Andy Weir'in romanından. Ryland Grace (Ryan Gosling) uzayda Rocky ile karşılaşıyor. Rocky <b>akorlarla</b> konuşuyor.</p><p style='margin-top:18px'>Grace her sesi tek tek kaydedip bir sözlük kuruyor. Ortak dilleri sayılar, ölçü birimleri ve ortak bir dertten doğuyor.</p>")

S7 = f"""<div class='slide'><div class='bp'></div>
<div style='position:absolute;left:80px;right:80px;top:130px'>
 <div class='mono' style='color:var(--amber)'>Karşılaştırma tablosu</div>
 <h2 style='margin:16px 0 40px'>Kim, neyle konuştu?</h2>
 <table>
  <tr><th>Film</th><th>İlk kelime</th><th>Ortak zemin</th></tr>
  <tr><td lang='en'>Close Encounters</td><td>5 nota</td><td>Müzik ve ışık</td></tr>
  <tr><td lang='en'>Contact</td><td>Asal sayılar</td><td>Matematik</td></tr>
  <tr><td lang='en'>Arrival</td><td>Dairesel semboller</td><td>Yazı ve zaman</td></tr>
  <tr><td lang='en'>Project Hail Mary</td><td>Akorlar</td><td>Bilim ve dostluk</td></tr>
 </table>
 <p style='margin-top:60px;font-size:40px'>Dördünde de ortak bir şey var: İletişim, karşı tarafı <b>tehdit değil, muhatap</b> olarak görünce başlıyor.</p>
</div></div>"""

S8 = f"""<div class='slide'><img class='cover-img' src='{EARTH}' style='filter:saturate(.8)'>
<div style='position:absolute;inset:0;background:rgba(10,58,99,.55)'></div>
<div style='position:absolute;left:90px;right:90px;top:430px;text-align:center'>
 <div class='mono' style='color:var(--amber)'>Son soru</div>
 <h1 style='margin-top:24px;font-size:84px'>Sen olsan ilk ne söylerdin?</h1>
 <p style='margin-top:30px'>Bir melodi mi, bir sayı mı, bir çizim mi? Yorumlara yaz.</p>
</div></div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7, S8]

CAPTION = """
Project Hail Mary (2026), Arrival (2016), Contact (1997) ve Close Encounters of the Third Kind (1977) aynı soruyu soruyor: Ortak dilimiz, ortak bedenimiz, belki ortak duyularımız bile yokken bir uzaylıyla nasıl konuşuruz?

Spielberg beş notalık bir melodiyle düet kuruyor, Contact'ta sinyal asal sayılarla geliyor, Arrival'da dilbilimci Louise Banks başı ve sonu olmayan dairesel bir yazıyı çözüyor. Project Hail Mary'de ise Ryland Grace, akorlarla konuşan Rocky ile her sesi tek tek kaydederek bir sözlük kuruyor.

Dört filmde de iletişim aynı yerde başlıyor: Karşı tarafı tehdit olarak değil, muhatap olarak gördüğün anda. Sen olsan ilk ne söylerdin?

Yarın 20:00'de: Aynı yüz, bambaşka adamlar. Bir oyuncunun dört filmde dört ayrı hâli.
"""

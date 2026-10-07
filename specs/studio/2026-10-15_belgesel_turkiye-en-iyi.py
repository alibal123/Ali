from studio import img, GRAIN

ID = "2026-10-15_belgesel_turkiye-en-iyi"
FONTS = ["old-standard-tt/400.css", "old-standard-tt/400-italic.css", "old-standard-tt/700.css", "abril-fatface/400.css"]

CAM, HUNDRED, EKU, KEDI, BAVUL, COCUK = (img("ai_22.jpg"), img("ai_16.jpg"), img("ai_13.jpg"), img("ai_14.jpg"),
                                        img("ai_15.jpg"), img("ai_17.jpg"))

CSS = f"""
:root{{--np:#ebe4d2;--ink:#191714;--red:#b3261e}}
body{{background:var(--np);color:var(--ink);font-family:'Old Standard TT',serif}}
.np{{position:absolute;inset:0;background:var(--np);background-image:radial-gradient(ellipse at 20% 10%,rgba(255,255,255,.4),transparent 60%),radial-gradient(ellipse at 90% 95%,rgba(140,110,60,.22),transparent 60%)}}
.np::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.16;mix-blend-mode:multiply;pointer-events:none}}
.fold{{position:absolute;left:0;right:0;top:675px;height:2px;background:linear-gradient(90deg,transparent,rgba(0,0,0,.08),transparent)}}
.mast{{position:absolute;left:60px;right:60px;top:50px;text-align:center}}
.mast .name{{font:400 112px/1 'Abril Fatface';letter-spacing:.01em}}
.mast .bar{{display:flex;justify-content:space-between;border-top:3px solid var(--ink);border-bottom:1px solid var(--ink);margin-top:14px;padding:10px 4px;font:700 20px/1 'Old Standard TT';letter-spacing:.16em;text-transform:uppercase}}
.head{{position:absolute;left:60px;right:60px;top:50px;display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px double var(--ink);padding-bottom:12px;font:700 21px/1 'Old Standard TT';letter-spacing:.2em;text-transform:uppercase}}
.head .n{{font:400 64px/0.8 'Abril Fatface';letter-spacing:0;color:var(--red)}}
h1{{font:400 92px/0.98 'Abril Fatface'}}
h2{{font:400 74px/1 'Abril Fatface'}}
.deck{{font:400 italic 34px/1.3 'Old Standard TT';margin-top:16px}}
.cols{{column-count:2;column-gap:44px;column-rule:1px solid rgba(0,0,0,.4);font:400 33px/1.42 'Old Standard TT';text-align:left}}
.cols p+p{{margin-top:12px;text-indent:1.4em}}
.cols p:first-child::first-letter{{float:left;font:400 92px/0.8 'Abril Fatface';margin:6px 10px 0 0;color:var(--red)}}
.pic{{position:absolute;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.15);mix-blend-mode:multiply}}
.capt{{font:400 italic 21px/1.3 'Old Standard TT';color:#444}}
.meta{{display:inline-block;border:2px solid var(--ink);padding:8px 14px;font:700 20px/1 'Old Standard TT';letter-spacing:.18em;text-transform:uppercase;margin-top:18px}}
"""

S1 = f"""<div class='slide'><div class='np'></div><div class='fold'></div>
<div class='mast'><div class='name'>Derece Postası</div>
 <div class='bar'><span>15 Ekim 2026</span><span>Belgesel Özel Sayısı</span><span>Seri · 1</span></div></div>
<div style='position:absolute;left:60px;right:60px;top:300px'>
 <h1>Türkiye'de çekilmiş en iyi 5 belgesel</h1>
 <div class='deck'>Ders kitabında yazmayanlar, şehrin altında kalanlar, iki dil arasında sıkışanlar.</div></div>
<div class='pic' style='left:60px;right:60px;top:610px;height:620px;background-image:url("{CAM}");background-position:center 40%'></div>
<div class='capt' style='position:absolute;left:60px;right:60px;top:1245px'>Kamera İstanbul'a dönük. Listeyi sayfalarda bulacaksınız. Kaydırın.</div>
</div>"""


def page(n, sec, title, deck, meta, body, pic, pos="center"):
    paras = "".join(f"<p>{x}</p>" for x in body)
    return f"""<div class='slide'><div class='np'></div><div class='fold'></div>
<div class='head'><span class='n'>{n}</span><span>{sec}</span><span>Derece Postası</span></div>
<div style='position:absolute;left:60px;right:60px;top:170px'>
 <h2>{title}</h2><div class='deck'>{deck}</div><div class='meta'>{meta}</div></div>
<div class='pic' style='left:60px;right:60px;top:490px;height:440px;background-image:url("{pic}");background-position:{pos}'></div>
<div class='cols' data-fit style='position:absolute;left:60px;right:60px;top:965px;bottom:50px'>{paras}</div>
</div>"""


S2 = page("1", "Tarih", "100", "Yüz yıllık bir ülke, kırk dokuz dakikalık bir kurgu.", "140journos · YouTube",
          ["Cumhuriyetin ilk gününden bugüne darbeleri, krizleri ve umutları anlatan belgesel, ders kitaplarındaki sıkıcı tarihi tamamen unutturuyor. Türkiye'nin kaderini belirleyen kırılma noktaları sürükleyici bir film sahnesi gibi akıp gidiyor.",
           "Türkiye'nin nereden nereye geldiğini merak eden herkes için. Üstelik ücretsiz."], HUNDRED)
S3 = page("2", "Şehir", "Ekümenopolis: Ucu Olmayan Şehir", "Daha çok bina, daha çok yol, daha çok insan.", "İmre Azem · 2011",
          ["İstanbul büyüdükçe günlük hayat daha zor, daha yoğun ve daha stresli hâle geliyor. Belgesel, kentsel dönüşümü, otoyolları ve yeni yerleşimleri haritalarla ve tanıklarla anlatıyor.",
           "Asıl soru şu: Büyüyen şehir sadece fiziksel değil, zihinsel bir baskı da kuruyor mu? Herkes aynı yerde yaşıyor ama herkes kendi içinde sıkışmış."], EKU)
S4 = page("3", "Eğitim", "İki Dil Bir Bavul", "Öğretmen Kürtçe bilmiyor, öğrenciler Türkçe.", "Orhan Eskiköy & Özgür Doğan · 2008",
          ["Batıdan gelen genç öğretmen Emre, Şanlıurfa Siverek'in bir köyündeki tek odalı okula atanır. Sınıfta kimse onun dilini konuşmaz, o da onların dilini.",
           "Bir okul yılı boyunca kamera hiç müdahale etmeden izliyor. Sonuç; komik, hüzünlü ve son derece dürüst bir iletişim denemesi."], BAVUL)
S5 = page("4", "Sokak", "Kedi", "İstanbul'u kedilerin gözünden görmek.", "Ceyda Torun · 2016",
          ["Balıkçının tezgâhından restoran arka kapısına, yedi sokak kedisi ve onları besleyen insanlar. Kamera kedilerin hizasına iniyor ve şehri yeniden çiziyor.",
           "Belgesel ABD sinemalarında da gösterildi ve büyük ilgi gördü. Ama asıl hikâye kedilerden çok, onlara bakarak kendine iyi gelen insanların hikâyesi."], KEDI)
S6 = page("5", "Aile", "Benim Çocuğum", "Çocuğunu yeniden tanımak zorunda kalan anne babalar.", "Can Candan · 2013",
          ["Çocukları LGBTİ+ olduğunu söyledikten sonra yaşadıkları süreci anlatan anne babalar kameraya konuşuyor: şaşkınlık, korku, öfke ve sonunda kabul.",
           "Bir ailenin kendi içinde verdiği sessiz mücadeleyi, bağırmadan ve yargılamadan anlatan bir belgesel."], COCUK)

S7 = f"""<div class='slide'><div class='np'></div><div class='fold'></div>
<div class='head'><span class='n'>✦</span><span>Okur Mektupları</span><span>Derece Postası</span></div>
<div style='position:absolute;left:60px;right:60px;top:200px'>
 <h2>Sırada ne var?</h2>
 <div class='deck'>Bu bir serinin ilk sayısı. Fatih Akın'ın <i>İstanbul Hatırası: Köprüyü Geçmek</i> belgeselini daha önce paylaşmıştık.</div>
 <div style='margin-top:60px;border-top:3px solid var(--ink);border-bottom:3px solid var(--ink);padding:44px 0;text-align:center'>
  <div style='font:400 76px/1.1 Abril Fatface'>Senin listende hangi belgesel var?</div>
  <div class='deck' style='margin-top:22px;font-size:38px'>Yorumlara yaz; en çok önerilenleri bir sonraki sayıda yayımlayalım.</div></div>
 <div class='cols' style='margin-top:60px'><p>Listede yer almayan ama izlenmesi gerekenler için de not alıyoruz: belgeseller, kısa filmler, YouTube'da kaybolmuş yapımlar. Gazetemiz okurunun önerisiyle büyür.</p><p>Bir sonraki sayıda görüşmek üzere.</p></div>
</div></div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7]

CAPTION = """
Türkiye'de yapılmış en iyi belgeselleri anlatıyoruz. Serinin ilk sayısında beş yapım var: 140journos'un hazırladığı 100, Ekümenopolis: Ucu Olmayan Şehir (2011), İki Dil Bir Bavul (2008), Kedi (2016) ve Benim Çocuğum (2013).

100, Cumhuriyetin yüz yılını kırk dokuz dakikalık sürükleyici bir kurguyla anlatıyor. Ekümenopolis, büyüyen İstanbul'un insan psikolojisi üzerindeki baskısını; İki Dil Bir Bavul, Kürtçe bilmeyen bir öğretmenle Türkçe bilmeyen öğrencilerinin bir okul yılını gösteriyor. Kedi şehri sokak kedilerinin hizasından izliyor, Benim Çocuğum ise çocuğunu yeniden tanımak zorunda kalan anne babaları dinliyor.

Hepsi farklı bir Türkiye anlatıyor ama ortak noktaları aynı: Kamerayı bağırmadan, dürüstçe tutuyorlar. Senin listende hangi belgesel var?

Yarın 20:00'de: 5 kart, 5 ipucu. Kim olduğunu kaçıncı kartta bulacaksın?
"""

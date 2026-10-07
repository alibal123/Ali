from studio import img, GRAIN

ID = "2026-10-16_oyun_ben-kimim"
FONTS = ["cinzel/500.css", "cinzel/700.css", "cormorant-garamond/500-italic.css", "cormorant-garamond/600.css",
         "cormorant-garamond/600-italic.css"]

BACK = img("ai_07_card.jpg")
CARDS = [img(f"ai_{n}_card.jpg") for n in ("02", "03", "06", "05", "04")]
DOOR, BUTTON = img("up_truman_12.jpg"), img("up_truman_05.jpg")

CSS = f"""
:root{{--felt:#0e2621;--gold:#d2ad64;--cream:#efe4c8}}
body{{background:var(--felt);color:var(--cream);font-family:'Cormorant Garamond',serif}}
.felt{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 38%,#1d4a3f 0%,#0e2621 55%,#07130f 100%)}}
.felt::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.28;mix-blend-mode:overlay}}
.card{{position:absolute;border-radius:26px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.6),0 0 0 1px rgba(0,0,0,.3)}}
.card img{{width:100%;height:100%;object-fit:cover;transform:scale(1.04)}}
.num{{font:700 30px/1 'Cinzel';letter-spacing:.4em;color:var(--gold)}}
h1{{font:700 76px/1.08 'Cinzel';letter-spacing:.04em;color:var(--gold)}}
.clue{{font:600 italic 50px/1.22 'Cormorant Garamond';color:var(--cream)}}
.small{{font:500 italic 34px/1.35 'Cormorant Garamond';color:rgba(239,228,200,.8)}}
.orn{{color:var(--gold);font-size:30px;letter-spacing:.6em}}
.dots{{position:absolute;bottom:56px;left:0;right:0;display:flex;justify-content:center;gap:16px}}
.dots i{{width:14px;height:14px;border-radius:50%;border:2px solid var(--gold)}}
.dots i.on{{background:var(--gold)}}
"""


def dots(k):
    return "<div class='dots'>" + "".join(f"<i class='{'on' if j < k else ''}'></i>" for j in range(5)) + "</div>"


S1 = f"""<div class='slide'><div class='felt'></div>
<div class='card' style='left:160px;top:210px;width:420px;height:600px;transform:rotate(-9deg)'><img src='{BACK}'></div>
<div class='card' style='left:330px;top:170px;width:420px;height:600px;transform:rotate(1deg)'><img src='{BACK}'></div>
<div class='card' style='left:500px;top:220px;width:420px;height:600px;transform:rotate(10deg)'><img src='{BACK}'></div>
<div style='position:absolute;left:80px;right:80px;top:900px;text-align:center'>
 <div class='orn'>✦ OYUN ✦</div>
 <h1 style='margin-top:22px'>5 Kartta<br>Kim Olduğunu Bul</h1>
 <div class='small' style='margin-top:22px'>Her kart yeni bir ipucu. Bildiğin anda dur ve yorumlara kart numarasını yaz.</div>
</div></div>"""


def clue(k, text, sub):
    return f"""<div class='slide'><div class='felt'></div>
<div class='card' style='left:250px;top:110px;width:580px;height:800px;transform:rotate({(-1) ** k * 2}deg)'><img src='{CARDS[k - 1]}'></div>
<div style='position:absolute;left:90px;right:90px;top:965px;text-align:center'>
 <div class='num'>Kart {['I', 'II', 'III', 'IV', 'V'][k - 1]}</div>
 <div class='clue' data-fit style='margin-top:20px;max-height:190px'>{text}</div>
 <div class='small' style='margin-top:12px;font-size:30px'>{sub}</div>
</div>{dots(k)}</div>"""


S2 = clue(1, "Doğduğu günden beri aynı küçük sahil kasabasında yaşıyor.", "Kasabadan hiç çıkmadı. Herkes çok kibar. Fazla kibar.")
S3 = clue(2, "Bir sabah gökyüzünden sokağın ortasına bir projektör düştü.", "Radyo hemen açıkladı: “Uçaktan parça düşmüş.”")
S4 = clue(3, "Babası o küçükken bir fırtınada denizde kayboldu.", "O günden beri suya yaklaşamıyor. Köprüden bile geçemiyor.")
S5 = clue(4, "Herkes onu tanıyor ama o, izlendiğini bilmiyor.", "Banyo aynasının arkasında bile bir kamera var.")
S6 = clue(5, "Sonunda korkusunu yenip denize açıldı ve gökyüzüne çarptı.", "Duvarda bir merdiven, merdivenin ucunda bir kapı.")

S7 = f"""<div class='slide'><img class='cover-img' src='{DOOR}' style='object-position:52% 50%'>
<div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,19,15,0) 45%,rgba(7,19,15,.92) 80%)'></div>
<div style='position:absolute;left:80px;right:80px;bottom:110px;text-align:center'>
 <div class='orn'>✦ CEVAP ✦</div>
 <h1 style='margin-top:18px;font-size:84px;color:#fff'>Truman Burbank</h1>
 <div class='small' style='margin-top:14px;font-style:normal;font-family:Cinzel;letter-spacing:.3em;font-size:26px;color:var(--gold)'><span lang='en'>THE TRUMAN SHOW</span> · 1998</div>
</div></div>"""

S8 = f"""<div class='slide'><div class='felt'></div>
<div class='card' style='left:140px;top:140px;width:800px;height:450px;border-radius:8px;transform:rotate(-2deg)'><img src='{BUTTON}'></div>
<div style='position:absolute;left:100px;right:100px;top:690px;text-align:center'>
 <div class='clue'>“Günaydın! Olur da sizi göremezsem diye: tünaydın, iyi akşamlar ve iyi geceler!”</div>
 <div class='orn' style='margin:44px 0'>✦</div>
 <div class='small'>Peter Weir'in filmi, gerçeklik şovları daha yaygınlaşmadan, 1998'de çekildi. Bugün izlendiğinde neredeyse bir kehanet gibi.</div>
 <div class='num' style='margin-top:50px;font-size:26px'>Kaçıncı kartta buldun?</div>
</div></div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7, S8]

CAPTION = """
Kim olduğunu 5 kartta bul. Her kart yeni bir ipucu: Küçük bir sahil kasabası, gökyüzünden düşen bir projektör, denizde kaybolan bir baba, banyo aynasının arkasındaki kamera ve gökyüzüne çarpan bir tekne.

Cevap son kartta. Ama önce dürüst ol: Kaçıncı kartta buldun? Yorumlara yalnızca kart numarasını yaz, cevabı söyleyip başkalarının oyununu bozma.

Yarın 20:00'de: Bir sinyal, bir dil, bir akor. Uzaylılarla nasıl konuşulur? Project Hail Mary ve Arrival karşı karşıya.
"""

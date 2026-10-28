from pro import *

ID = "2026-10-31_vizyon_dunesday"
RED, GLD, INK, CRM = "#e8322b", "#f2b632", "#0d0d10", "#f4efe6"
TH = theme(INK, "#fff", RED, on_acc="#fff", head="anton")
LOGO = dict(pos="br", w=90, on_light="black", on_dark="yellow", over={})

CAPTION = """Dunesday geliyor: 18 Aralık'ta Avengers: Doomsday ve Dune: Part Three aynı gün vizyona giriyor. Tahmin piyasası Polymarket'te Avengers açılış hafta sonu düellosunda yaklaşık %78 ile önde görünüyor, ama bu sadece bir tahmin.

Avengers: Doomsday'de Robert Downey Jr. bu kez Iron Man değil, kötü adam Doctor Doom'u oynuyor. Film, Avengers, X-Men ve Fantastic Four'u ilk kez bir araya getiriyor; Chris Evans da Steve Rogers olarak dönüyor. Hikâyenin ikinci yarısı Avengers: Secret Wars ise 17 Aralık 2027'de gelecek. Dune: Part Three ise Denis Villeneuve'ün üçlemeyi kapatan filmi; Timothée Chalamet, Zendaya ve Florence Pugh yer alıyor, IMAX salonları ilk üç hafta Dune'a ayrılmış durumda. Disney ise kendi büyük ekran formatı InfinityVision'ı ilk kez bu filmle kullanacak.

Sen 18 Aralık'ta hangi salona gireceksin? Avengers için 1, Dune için 2 yaz.

Bugün 18:00'de: Cumartesi gecesi evde kalanlar kulübü için 5 ürkütmeyen film."""


def cover():
    return {"bg": "#000", "els": [
        img(grade(S("doomsday", 5), (1080, 1350), (0.22, 0, 0.78, 1)), 0, 0, W, 1350, z=1, clip="polygon(0 0, 61% 0, 46% 100%, 0 100%)"),
        img(grade(S("dune3", 1), (1080, 1350), (0.25, 0, 0.75, 1)), 0, 0, W, 1350, z=1, clip="polygon(62% 0, 100% 0, 100% 100%, 47% 100%)"),
        box(0, 0, W, 1350, "linear-gradient(180deg,rgba(0,0,0,.75),rgba(0,0,0,0) 40%,rgba(0,0,0,0) 55%,rgba(0,0,0,.9))", z=2),
        T("18 ARALIK 2026", M, 50, 600, 36, 26, "oswald", "#fff", fit=False, weight=500, ls=8, nowrap=True, z=6),
        T("DUNESDAY", M, 130, W - 2 * M, 260, 240, "anton", "#fff", nowrap=True, mn=100, lh=1.1, z=6),
        label("AVENGERS: DOOMSDAY", M, 880, bg=RED, size=24, z=6),
        label("DUNE: PART THREE", 560, 880, bg=GLD, color=INK, size=24, z=6),
        T("Aynı gün, iki dev.<br>Piyasa çoktan taraf seçti.", M, 1000, W - 2 * M - 110, 200, 66, "anton", "#fff", nowrap=True, mn=36, lh=1.15, z=6),
        T("Sen?", M, 1210, 300, 90, 76, "anton", GLD, fit=False, lh=1.0, nowrap=True, z=6),
    ]}


def photo_slide(i, n, src, crop, kick, title, bullets, col, on):
    els = [
        img(grade(src, (1080, 1350), crop), 0, 0, W, 1350, z=1),
        box(0, 0, W, 1350, "linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,0) 30%,rgba(0,0,0,.55) 55%,rgba(0,0,0,.95))", z=2),
        label(kick, M, 60, bg=col, color=on, size=24, z=6),
        T(title, M, 540, W - 2 * M, 330, 112, "anton", "#fff", nowrap=True, mn=54, lh=1.12, z=6),
    ]
    y = 900
    for b, h in bullets:
        els += [box(M, y + 10, 14, 14, col, z=6), T(b, M + 40, y - 4, W - 2 * M - 130, h, 33, "inter", "#fff", weight=500, lh=1.3, mn=24, z=6)]
        y += h + 22
    els.append(T(f"{i} / {n}", M, 1284, 200, 30, 20, "oswald", "#fff", fit=False, weight=500, ls=4, op=0.55))
    return {"bg": INK, "els": els}


def tape(n):
    rows = [
        ("YÖNETMEN", "Anthony ve Joe Russo", "Denis Villeneuve"),
        ("BÜYÜK EKRAN", "InfinityVision (Disney'in yeni formatı)", "IMAX'te ilk 3 hafta"),
        ("YILDIZ", "Robert Downey Jr. (bu kez kötü adam)", "Timothée Chalamet, Zendaya"),
        ("HİKÂYE", "Çok evrenli serinin ilk yarısı", "Üçlemenin finali"),
        ("PİYASA FAVORİSİ", "Açılışta ~%78", "Açılışta ~%22"),
    ]
    els = [
        box(0, 100, 540, 170, RED, z=2), box(540, 100, 540, 170, GLD, z=2),
        T("AVENGERS<br>DOOMSDAY", 0, 100, 540, 170, 54, "anton", "#fff", fit=False, align="center", flex="center", lh=1.1, bleed=True, z=4),
        T("DUNE<br>PART THREE", 540, 100, 540, 170, 54, "anton", INK, fit=False, align="center", flex="center", lh=1.1, bleed=True, z=4),
        T("KARŞILAŞMA KARTI", M, 50, 700, 34, 24, "oswald", "#fff", fit=False, weight=500, ls=8, op=0.7, nowrap=True),
    ]
    y = 300
    for lab, a, b in rows:
        els += [
            T(lab, 0, y, W, 28, 22, "oswald", "#fff", fit=False, weight=500, ls=7, align="center", op=0.55, bleed=True),
            T(a, 40, y + 40, 460, 110, 36, "inter", "#fff", weight=600, lh=1.25, mn=24, align="center", flex="center"),
            T(b, 580, y + 40, 460, 110, 36, "inter", "#fff", weight=600, lh=1.25, mn=24, align="center", flex="center"),
            rule(M, y + 168, W - 2 * M, "#fff", op=0.18, h=2),
        ]
        y += 180
    els.append(box(539, 300, 2, 900, "#fff", z=2, op=0.18))
    els.append(T(f"4 / {n}", M, 1284, 200, 30, 20, "oswald", "#fff", fit=False, weight=500, ls=4, op=0.55))
    return {"bg": INK, "els": els}


def chart(n):
    els = [
        T("PİYASA NE DİYOR?", M, 70, W - 2 * M, 40, 28, "oswald", GLD, fit=False, weight=500, ls=8, nowrap=True),
        T("AÇILIŞ HAFTA SONUNU<br>KİM KAZANIR?", M, 130, W - 2 * M, 260, 104, "anton", "#fff", nowrap=True, mn=50, lh=1.12),
        box(M, 440, 968 * 0.78, 150, RED, z=2), box(M + 968 * 0.78, 440, 968 * 0.22, 150, GLD, z=2),
        T("%78", M + 24, 440, 400, 150, 100, "anton", "#fff", fit=False, flex="center", lh=1.0, bleed=True, z=4),
        T("%22", M + 968 * 0.78, 440, 968 * 0.22, 150, 66, "anton", INK, fit=False, align="center", flex="center", lh=1.0, bleed=True, z=4),
        T("AVENGERS: DOOMSDAY", M, 604, 520, 30, 22, "oswald", RED, fit=False, weight=500, ls=5, nowrap=True),
        T("DUNE", W - M - 220, 604, 220, 30, 22, "oswald", GLD, fit=False, weight=500, ls=5, align="right", nowrap=True),
        T("2026'NIN EN BÜYÜK AÇILIŞI", M, 720, W - 2 * M, 34, 24, "oswald", "#fff", fit=False, weight=500, ls=6, nowrap=True, op=0.7),
        box(M, 770, 968, 90, "rgba(255,255,255,.1)", z=2), box(M, 770, 968 * 0.75, 90, RED, z=3),
        T("Doomsday  ~%75", M + 24, 770, 700, 90, 44, "anton", "#fff", fit=False, flex="center", lh=1.0, bleed=True, z=5, nowrap=True),
        T("Aşması gereken rakam: Spider-Man: Brand New Day'in açılışı, yaklaşık 360 milyon dolar.", M, 900, W - 2 * M, 130, 36, "inter", "#fff", weight=500, lh=1.4, mn=26),
        T("Kaynak: Polymarket tahmin piyasası (Temmuz–Ekim verileri). Bunlar tahmindir, sonuç değildir.", M, 1090, W - 2 * M, 80, 24, "inter", "#fff", weight=400, lh=1.4, mn=18, op=0.55),
        T(f"5 / {n}", M, 1284, 200, 30, 20, "oswald", "#fff", fit=False, weight=500, ls=4, op=0.55),
    ]
    return {"bg": INK, "els": els}


def build():
    n = 7
    s2 = photo_slide(2, n, S("doomsday", 5), (0.15, 0, 0.85, 1), "AVENGERS: DOOMSDAY",
                     "IRON MAN<br>ARTIK KÖTÜ ADAM", [
                         ("Robert Downey Jr., bu kez Doctor Doom olarak karşımızda.", 90),
                         ("Avengers, X-Men ve Fantastic Four ilk kez aynı filmde.", 90),
                         ("Chris Evans, Steve Rogers olarak geri dönüyor.", 90)], RED, "#fff")
    s3 = photo_slide(3, n, S("dune3", 1), (0.1, 0, 0.9, 1), "DUNE: PART THREE",
                     "ÜÇLEMENİN<br>FİNALİ", [
                         ("Denis Villeneuve, Dune Messiah romanını uyarlıyor.", 90),
                         ("Timothée Chalamet, Zendaya ve Florence Pugh kadroda.", 90),
                         ("IMAX salonları ilk üç hafta Dune'a ayrıldı.", 90)], GLD, INK)
    s6 = {"bg": GLD, "els": [
        T("İKİSİNDE DE<br>OYNAYAN TEK İSİM", M, 90, W - 2 * M, 300, 100, "anton", INK, nowrap=True, mn=50, lh=1.12),
        T("FLORENCE PUGH", M, 440, W - 2 * M, 150, 130, "anton", "#fff", nowrap=True, mn=60, lh=1.1, stroke=f"2px {INK}"),
        rule(M, 700, W - 2 * M, INK, op=0.9, h=3),
        T("AVENGERS: DOOMSDAY", M, 730, 700, 30, 24, "oswald", INK, fit=False, weight=500, ls=5, op=0.7),
        T("Yelena Belova", M, 770, W - 2 * M, 80, 60, "serif", INK, nowrap=True, mn=30),
        rule(M, 890, W - 2 * M, INK, op=0.9, h=3),
        T("DUNE: PART THREE", M, 920, 700, 30, 24, "oswald", INK, fit=False, weight=500, ls=5, op=0.7),
        T("Prenses Irulan", M, 960, W - 2 * M, 80, 60, "serif", INK, nowrap=True, mn=30),
        T("6 / 7", M, 1284, 200, 30, 20, "oswald", INK, fit=False, weight=500, ls=4, op=0.55),
    ]}
    s7 = {"bg": INK, "els": [
        T("HANGİ SALONA<br>GİRECEKSİN?", M, 80, W - 2 * M, 280, 104, "anton", "#fff", nowrap=True, mn=60, lh=1.12),
        T("Yorumlara 1 ya da 2 yaz.", M, 380, W - 2 * M, 50, 36, "inter", "#fff", weight=500, op=0.7, nowrap=True),
        box(0, 500, 540, 850, RED, z=2), box(540, 500, 540, 850, GLD, z=2),
        T("1", 0, 540, 540, 400, 380, "anton", "#fff", fit=False, align="center", lh=1.0, bleed=True),
        T("AVENGERS<br>DOOMSDAY", 0, 1090, 540, 120, 38, "oswald", "#fff", fit=False, weight=500, ls=5, align="center", lh=1.3, bleed=True),
        T("2", 540, 540, 540, 400, 380, "anton", INK, fit=False, align="center", lh=1.0, bleed=True),
        T("DUNE<br>PART THREE", 540, 1090, 540, 120, 38, "oswald", INK, fit=False, weight=500, ls=5, align="center", lh=1.3, bleed=True),
    ]}
    return {"id": ID, "caption": CAPTION, "slides": [cover(), s2, s3, tape(n), chart(n), s6, s7]}

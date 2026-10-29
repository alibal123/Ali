from pro import *

ID = "2026-10-31_vizyon_dunesday"
RED, GLD, INK = "#e8322b", "#f2b632", "#07070a"
TH = theme(INK, "#fff", RED, on_acc="#fff", head="anton")
LOGO = dict(pos="tr", w=76, on_light="black", on_dark="yellow")

CAPTION = """Dunesday geliyor: 18 Aralık'ta Avengers: Doomsday ve Dune: Part Three aynı gün vizyona giriyor. Tahmin piyasası Polymarket'te Avengers açılış hafta sonu düellosunda yaklaşık %78 ile önde görünüyor, ama bu sadece bir tahmin.

Avengers: Doomsday'de Robert Downey Jr. bu kez Iron Man değil, kötü adam Doctor Doom'u oynuyor. Film, Avengers, X-Men ve Fantastic Four'u ilk kez bir araya getiriyor; Chris Evans da Steve Rogers olarak dönüyor. Dune: Part Three ise Denis Villeneuve'ün üçlemeyi kapatan filmi; Timothée Chalamet, Zendaya ve Florence Pugh yer alıyor, IMAX salonları ilk üç hafta Dune'a ayrılmış durumda.

Sen 18 Aralık'ta hangi salona gireceksin? Avengers için 1, Dune için 2 yaz.

Bugün 18:00'de: Cumartesi gecesi evde kalanlar kulübü: ruh haline göre 5 film."""


def scene(src, crop, shade="linear-gradient(180deg,rgba(0,0,0,.5) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,.6) 42%,rgba(0,0,0,.94) 62%,rgba(0,0,0,.98) 100%)"):
    return [img(grade(src, (1080, 1350), crop, grain=9, contrast=1.1), 0, 0, W, 1350, z=1),
            box(0, 0, W, 1350, shade, z=2)]


def head(kick, lines, body, col, n, i, ty=700):
    return [
        label(kick, M, 60, bg=col, color=("#fff" if col == RED else INK), size=24, z=6),
        T(lines, M, ty, W - 2 * M, 330, 128, "anton", "#fff", nowrap=True, mn=60, lh=1.1, z=6),
        box(M, ty + 350, 120, 6, col, z=6),
        T(body, M, ty + 390, W - 2 * M - 40, 230, 36, "inter", "#fff", weight=400, lh=1.42, mn=26, z=6, op=0.92),
        T(f"{i:02d} / {n:02d}", M, 1290, 200, 28, 20, "oswald", "#fff", fit=False, weight=500, ls=5, op=0.55, z=6),
    ]


def cover():
    return {"bg": INK, "els": [
        img(grade(S("doomsday", 5), (1080, 700), (0.14, 0, 0.86, 0.9), grain=9, contrast=1.12), 0, 0, W, 700, z=1),
        img(grade(S("dune3", 1), (1080, 650), (0.05, 0.1, 0.95, 0.9), grain=9, contrast=1.1), 0, 700, W, 650, z=1),
        box(0, 0, W, 700, "linear-gradient(180deg,rgba(0,0,0,.55),rgba(0,0,0,0) 40%,rgba(0,0,0,.55))", z=2),
        box(0, 700, W, 650, "linear-gradient(180deg,rgba(0,0,0,.5),rgba(0,0,0,0) 40%,rgba(0,0,0,.7))", z=2),
        T("18.12.2026", M, 64, 400, 30, 24, "oswald", "#fff", fit=False, weight=500, ls=8, nowrap=True, z=6),
        T("DUNESDAY", M, 490, W - 2 * M, 420, 236, "anton", "#fff", fit=False, align="center", flex="center", lh=1.0, bleed=True, nowrap=True, z=6),
        label("AVENGERS: DOOMSDAY", M, 480, bg=RED, color="#fff", size=24, z=7),
        label("DUNE: PART THREE", 640, 880, bg=GLD, color=INK, size=24, z=7),
        box(0, 900, W, 450, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.88))", z=4),
        T("Aynı gün, iki dev.<br>Piyasa taraf seçti.", M, 1130, W - 2 * M, 150, 52, "anton", "#fff", nowrap=True, mn=30, lh=1.18, z=7),
    ]}


def build():
    n = 6
    s2 = {"bg": INK, "els": [*scene(S("doomsday", 5), (0.18, 0, 0.82, 1)),
          *head("AVENGERS: DOOMSDAY", "IRON MAN'İN<br>YENİ İŞİ: KÖTÜ ADAM", "Robert Downey Jr. bu kez Doctor Doom'u oynuyor. Avengers, X-Men ve Fantastic Four ilk kez aynı filmde; Chris Evans da Steve Rogers olarak geri dönüyor.", RED, n, 2, 560)]}
    s3 = {"bg": INK, "els": [*scene(S("dune3", 1), (0.1, 0, 0.9, 1)),
          *head("DUNE: PART THREE", "ÜÇLEMENİN<br>SON BÖLÜMÜ", "Denis Villeneuve, Dune Messiah romanını uyarlıyor. Kadroda Chalamet, Zendaya ve Florence Pugh var; IMAX'in ilk üç haftası Dune'a ayrıldı.", GLD, n, 3, 560)]}
    s4 = {"bg": GLD, "els": [
        T("İKİ FİLMDE DE OYNAYAN TEK İSİM", M, 70, W - 2 * M, 30, 22, "oswald", INK, fit=False, weight=600, ls=8, nowrap=True),
        T("FLORENCE<br>PUGH", M, 160, W - 2 * M, 660, 340, "anton", INK, nowrap=True, mn=120, lh=0.98),
        rule(M, 840, W - 2 * M, INK, op=1, h=4),
        T("YELENA BELOVA", M, 870, 700, 80, 64, "anton", INK, nowrap=True, mn=30, lh=1.1),
        T("Avengers: Doomsday", M, 954, 700, 30, 26, "inter", INK, weight=500, nowrap=True, op=0.7),
        rule(M, 1030, W - 2 * M, INK, op=1, h=4),
        T("PRENSES IRULAN", M, 1060, 700, 80, 64, "anton", INK, nowrap=True, mn=30, lh=1.1),
        T("Dune: Part Three", M, 1144, 700, 30, 26, "inter", INK, weight=500, nowrap=True, op=0.7),
        T(f"04 / {n:02d}", M, 1290, 200, 28, 20, "oswald", INK, fit=False, weight=500, ls=5, op=0.55),
    ]}
    s5 = {"bg": INK, "els": [
        img(grade(S("doomsday", 1), (1080, 1350), (0.1, 0, 0.9, 1), grain=9), 0, 0, W, 1350, z=1),
        box(0, 0, W, 1350, "rgba(7,7,10,.82)", z=2),
        T("POLYMARKET'E GÖRE", M, 70, W - 2 * M, 30, 22, "oswald", GLD, fit=False, weight=600, ls=9, nowrap=True, z=5),
        T("%78", M, 130, W - 2 * M, 520, 430, "anton", RED, fit=False, lh=1.0, bleed=True, nowrap=True, z=5),
        T("Avengers: Doomsday'in açılış hafta sonunda Dune: Part Three'yi geçeceği tahmin ediliyor.", M, 700, W - 2 * M, 200, 46, "anton", "#fff", mn=30, lh=1.25, z=5),
        rule(M, 940, W - 2 * M, "#fff", op=0.3, h=2),
        T("2026'nın en büyük açılışı için ise Doomsday yaklaşık %75. Aşması gereken rakam: Spider-Man: Brand New Day'in 360 milyon dolarlık açılışı.", M, 970, W - 2 * M, 190, 32, "inter", "#fff", weight=400, lh=1.42, mn=22, op=0.9, z=5),
        T("Kaynak: Polymarket (Temmuz–Ekim 2026). Tahmindir, sonuç değildir.", M, 1250, W - 2 * M, 28, 20, "inter", "#fff", weight=400, nowrap=True, mn=14, op=0.5, z=5),
    ]}
    s6 = {"bg": INK, "els": [
        img(grade(S("doomsday", 5), (540, 1350), (0.3, 0, 0.7, 1), grain=8), 0, 0, 540, 1350, z=1),
        img(grade(S("dune3", 1), (540, 1350), (0.3, 0, 0.7, 1), grain=8), 540, 0, 540, 1350, z=1),
        box(0, 0, 540, 1350, "linear-gradient(180deg,rgba(7,7,10,.85),rgba(232,50,43,.3) 32%,rgba(7,7,10,.92))", z=2),
        box(540, 0, 540, 1350, "linear-gradient(180deg,rgba(7,7,10,.85),rgba(242,182,50,.28) 32%,rgba(7,7,10,.92))", z=2),
        box(538, 0, 4, 1350, "#fff", z=3),
        T("HANGİ SALONA<br>GİRECEKSİN?", M, 80, W - 2 * M, 220, 100, "anton", "#fff", nowrap=True, mn=50, lh=1.12, z=6),
        T("1", 0, 420, 540, 520, 520, "anton", "#fff", fit=False, align="center", lh=1.0, bleed=True, z=6),
        T("2", 540, 420, 540, 520, 520, "anton", "#fff", fit=False, align="center", lh=1.0, bleed=True, z=6),
        T("AVENGERS<br>DOOMSDAY", 0, 1040, 540, 100, 34, "oswald", "#fff", fit=False, weight=600, ls=6, align="center", lh=1.35, bleed=True, z=6),
        T("DUNE<br>PART THREE", 540, 1040, 540, 100, 34, "oswald", "#fff", fit=False, weight=600, ls=6, align="center", lh=1.35, bleed=True, z=6),
        T("Yorumlara 1 ya da 2 yaz.", M, 1250, W - 2 * M, 40, 28, "inter", "#fff", align="center", weight=500, nowrap=True, z=6),
    ]}
    return {"id": ID, "caption": CAPTION, "slides": [cover(), s2, s3, s4, s5, s6]}

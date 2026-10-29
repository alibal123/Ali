from pro import *

ID = "2026-11-02_liste_2026-en-yuksek-puanli-5-film"
PAPER, INK, RED, BLUE, CHALK = "#f2e9d2", "#2a2622", "#d3281c", "#1f46a8", "#1f3a32"
TH = theme(PAPER, INK, RED, on_acc="#fff", head="anton")
LOGO = dict(pos="tr", w=70, on_light="red", on_dark="white")

CAPTION = """2026 karne günü: takdiri kimler aldı? Eylül 2025'ten bu yana vizyona giren ve en az 1.500 oy almış filmler arasında TMDB izleyici puanına göre en tepedeki 5 film hepsi bu yılın yapımı çıktı.

Yerime Geç 8,8 ile zirvede. Onu 8,6 ile Kurtuluş Projesi ve Michael, 8,5 ile Örümcek-Adam: Yepyeni Bir Gün, 8,3 ile Oyuncak Hikayesi 5 izliyor. Puanlar zamanla değişebilir. Karneden sonra bir de Oscar piyasasına baktık: Polymarket'te şu an Best Picture ödülünde yaklaşık %48 ile The Odyssey önde.

Sen hangisini izledin, takdiri hak ediyor mu?

Yarın 18:00'de: Çocukken izlediğin, büyüyünce başka vuran 5 animasyon."""

FILMS = [
    ("YERİME GEÇ", "8.8", "1 Mayıs 2026 · Nathan Greno", "Michael B. Jordan, Juno Temple, Tracy Morgan",
     "Ormanda yaşayan küçük bir canlıyla görkemli bir kuşun bedenleri aniden yer değiştirir; hayatta kalmak için birlik olmaları gerekir.", S("swapped", 2), S("swapped", 2), "Swapped"),
    ("KURTULUŞ PROJESİ", "8.6", "20 Mart 2026 · Phil Lord, Christopher Miller", "Ryan Gosling, Sandra Hüller, James Ortiz",
     "Fen bilgisi öğretmeni Ryland Grace, ışık yılları uzakta bir uzay gemisinde hafızasını kaybetmiş halde uyanır ve Güneş'in sönmesinin sırrını çözmeye çalışır.", S("hailmary", 3), S("hailmary", 3), "Project Hail Mary"),
    ("MICHAEL", "8.6", "24 Nisan 2026 · Antoine Fuqua", "Jaafar Jackson, Colman Domingo, Nia Long",
     "Michael Jackson'ı gerçek hayattaki yeğeni Jaafar Jackson canlandırıyor; film en ikonik performansları da içeriyor.", S("michael", 1), S("michael", 1), "Biyografi"),
    ("ÖRÜMCEK-ADAM: YEPYENİ BİR GÜN", "8.5", "31 Temmuz 2026 · Destin Daniel Cretton", "Tom Holland, Sadie Sink, Zendaya",
     "Artık kimsenin hatırlamadığı Peter Parker, şehre yönelen yeni bir tehdidi durdurmaya çalışır.", S("spiderman", 1), S("spiderman", 1), "Spider-Man: Brand New Day"),
    ("OYUNCAK HİKAYESİ 5", "8.3", "19 Haziran 2026 · Andrew Stanton", "Tom Hanks, Tim Allen, Joan Cusack",
     "Bonnie'nin bir tablete takıntılı hale gelmesiyle Buzz, Woody ve Jessie için işler iyice karışır.", S("toystory5", 2), S("toystory5", 2), "Toy Story 5"),
]




COMMENT = ["Küçük ama cesur. Ailecek izlenir.", "Fen dersinde sınıfı ikiye ayırdı. Tebrikler.", "Sahne performansında sınıf birincisi.", "Mahallenin en sevilen öğrencisi, yine zirvede.", "Sınıfın en eski öğrencileri, hâlâ çalışkan."]


def paper(extra=()):
    return [
        box(0, 0, W, 1350, "repeating-linear-gradient(180deg, transparent 0px, transparent 62px, rgba(60,100,170,.20) 62px, rgba(60,100,170,.20) 64px)", z=1),
        box(118, 0, 3, 1350, "rgba(211,40,28,.45)", z=1),
        *extra,
    ]


def stamp(x, y, w=300, rot=-9, z=20, size=58, col=RED):
    return [box(x, y, w, 104, "rgba(0,0,0,0)", z=z, border=f"7px solid {col}", radius=12, rot=rot),
            T("TAKDİR", x, y, w, 104, size, "typewriter", col, fit=False, align="center", flex="center", lh=1.0, ls=4, weight=700, bleed=True, z=z + 1, rot=rot)]


def cover():
    els = paper()
    els += [
        T("2026 SİNEMA<br>KARNESİ", 150, 70, W - 150 - M, 250, 96, "typewriter", INK, nowrap=True, mn=50, lh=1.15, weight=700, z=5),
        T("Öğrenci: Sen   ·   Sınıf: Film Severler   ·   Dönem: 2026", 150, 330, W - 150 - M, 30, 22, "typewriter", INK, nowrap=True, mn=12, op=0.75, z=5),
        rule(150, 392, W - 150 - M, INK, op=0.9, h=3),
        T("DERS", 150, 408, 300, 30, 22, "typewriter", INK, fit=False, weight=700, ls=3, z=5, op=0.7),
        T("NOT", W - M - 200, 408, 200, 30, 22, "typewriter", INK, fit=False, weight=700, ls=3, align="right", z=5, op=0.7),
        rule(150, 448, W - 150 - M, INK, op=0.9, h=3),
    ]
    y = 470
    for i, f in enumerate(FILMS):
        els += [
            img(grade(f[6], (200, 118), (0.1, 0, 0.9, 1), grain=5), 150, y + 12, 200, 118, z=3, border="4px solid #fff", shadow="0 4px 10px rgba(0,0,0,.25)", rot=(-2 if i % 2 else 2)),
            T(f[0], 380, y + 48, 470, 50, 32, "typewriter", INK, nowrap=True, mn=16, weight=700, lh=1.2, z=5),
            T(f[1].replace(".", ","), W - M - 200, y + 4, 200, 130, 112, "caveat", RED, fit=False, weight=700, align="right", lh=1.0, nowrap=True, bleed=True, z=5, rot=-3),
            rule(150, y + 144, W - 150 - M, INK, op=0.25, h=2),
        ]
        y += 156
    els += [*stamp(700, 1218, 320, rot=-8, size=60),
            T("Notlar TMDB izleyici puanıdır, 10 üzerinden.", 150, 1296, 520, 24, 17, "typewriter", INK, nowrap=True, mn=12, op=0.6, z=5)]
    return {"bg": PAPER, "els": els}


def film(i, n):
    t, sc, meta, cast, body, src, _c, _t = FILMS[i]
    rot = -2 if i % 2 == 0 else 2
    els = paper([
        img(grade(src, (900, 520), (0, 0, 1, 1), grain=5), 90, 100, 900, 520, z=3, border="14px solid #fff", shadow="0 14px 30px rgba(0,0,0,.3)", rot=rot),
        box(60, 80, 170, 46, "rgba(236,222,160,.8)", z=6, rot=-30), box(850, 80, 170, 46, "rgba(236,222,160,.8)", z=6, rot=28),
        *stamp(640, 520, 290, rot=-11, size=52),
        T(t, 150, 690, 600, 140, 54, "typewriter", INK, mn=26, lh=1.15, weight=700, z=5),
        T(meta, 150, 840, 600, 30, 22, "typewriter", INK, mn=12, weight=400, z=5, op=0.7, nowrap=True),
        T(f"Oyuncular: {cast}", 150, 880, 600, 70, 22, "typewriter", INK, mn=14, lh=1.35, z=5, op=0.8),
        box(770, 690, 232, 232, "rgba(0,0,0,0)", z=5, border=f"8px solid {RED}", radius=300, rot=-6),
        T(sc.replace(".", ","), 770, 690, 232, 232, 120, "caveat", RED, fit=False, weight=700, align="center", flex="center", lh=1.0, bleed=True, z=6, rot=-6),
        T(body, 150, 968, W - 150 - M, 120, 26, "typewriter", INK, mn=18, lh=1.4, z=5, op=0.9),
        T("Öğretmen görüşü:", 150, 1094, 600, 40, 34, "caveat", BLUE, fit=False, weight=700, z=5, nowrap=True),
        T(COMMENT[i], 150, 1146, W - 150 - M, 110, 56, "caveat", BLUE, weight=700, lh=1.1, mn=30, z=5),
        T(f"{i+2} / {n}", W - M - 140, 1286, 140, 24, 18, "typewriter", INK, fit=False, align="right", z=5, op=0.5),
    ])
    return {"bg": PAPER, "els": els}


def chart(n):
    rows = [("EN İYİ FİLM", "The Odyssey", 48), ("EN İYİ ERKEK OYUNCU", "John Malkovich", 42), ("EN İYİ YARDIMCI KADIN OYUNCU", "Anne Hathaway", 56), ("EN İYİ FİLM ADAYLIĞI", "The Odyssey", 98), ("EN İYİ ERKEK OYUNCU ADAYLIĞI", "Matt Damon", 92)]
    els = paper([
        T("KARNEDEN SONRA", 150, 70, 700, 30, 22, "typewriter", RED, fit=False, weight=700, ls=5, nowrap=True, z=5),
        T("SINIF BİRİNCİSİ<br>KİM OLACAK?", 150, 120, W - 150 - M, 280, 84, "typewriter", INK, nowrap=True, mn=44, lh=1.18, weight=700, z=5),
        T("Oscar'ı tahmin piyasası nasıl görüyor?", 150, 400, W - 150 - M, 40, 34, "caveat", BLUE, nowrap=True, weight=700, z=5),
    ])
    y = 480
    for lab, who, pct in rows:
        tw_ = W - 150 - M
        be = int(tw_ * pct / 100)
        els += [
            T(lab, 150, y, tw_, 26, 18, "typewriter", INK, fit=False, nowrap=True, op=0.65, weight=700, z=5),
            box(150, y + 36, tw_, 70, "rgba(42,38,34,.08)", z=3, radius=6),
            box(150, y + 36, be, 70, RED, z=4, radius=6),
            T(who, 170, y + 50, 560, 44, 34, "caveat", "#fff", fit=False, weight=700, nowrap=True, bleed=True, z=6),
            (T(f"%{pct}", 150 + be - 180, y + 46, 160, 60, 46, "typewriter", "#fff", fit=False, weight=700, align="right", lh=1.0, nowrap=True, bleed=True, z=6) if pct >= 50 else T(f"%{pct}", 150 + be + 16, y + 46, 160, 60, 46, "typewriter", INK, fit=False, weight=700, lh=1.0, nowrap=True, bleed=True, z=6)),
        ]
        y += 140
    els += [T("Kaynak: Polymarket tahmin piyasası, 29 Ekim 2026. Tahmindir, sonuç değildir. Oscar töreni 14 Mart 2027.", 150, 1190, W - 150 - M, 70, 20, "typewriter", INK, mn=14, lh=1.4, op=0.6, z=5),
            T(f"{n-1} / {n}", W - M - 140, 1286, 140, 24, 18, "typewriter", INK, fit=False, align="right", z=5, op=0.5)]
    return {"bg": PAPER, "els": els}


def build():
    n = 8
    slides = [cover()] + [film(i, n) for i in range(5)] + [chart(n)]
    slides.append({"bg": CHALK, "els": [
        box(40, 40, 1000, 1270, "rgba(0,0,0,0)", z=1, border="10px solid #8a6a43", radius=8),
        T("Sence<br>takdiri hak<br>ediyorlar mı?", 110, 140, W - 220, 560, 130, "caveat", "#f4f1e6", weight=700, lh=1.05, nowrap=True, mn=70, z=5, rot=-2),
        T("Hangisini izledin? Yorumlara kendi notunu yaz.", 110, 800, W - 220, 120, 52, "caveat", "#f4f1e6", weight=700, lh=1.15, mn=30, z=5, op=0.9),
        *stamp(110, 1010, 330, rot=-6, size=60, col="#f4f1e6"),
        T("Kaydet · İzleme listene ekle", 500, 1050, 480, 40, 26, "typewriter", "#f4f1e6", nowrap=True, mn=14, z=5, op=0.8),
    ]})
    return {"id": ID, "caption": CAPTION, "slides": slides}

from pro import *

ID = "2026-11-02_liste_2026-en-yuksek-puanli-5-film"
TEAL, CRM, INK, RED = "#0e7c7b", "#f6f1e4", "#141a1a", "#d62d20"
TH = theme(CRM, INK, RED, on_acc="#fff", head="anton")
LOGO = dict(pos="tr", w=72, on_light="black", on_dark="white", over={1: "white", 2: "white", 3: "white", 4: "white", 5: "white"})

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




def stamp(x, y, w=300, rot=-9, z=20, size=56):
    return [box(x, y, w, 100, "rgba(246,241,228,.0)", z=z, border=f"6px solid {RED}", radius=10, rot=rot),
            T("TAKDİR", x, y, w, 100, size, "anton", RED, fit=False, align="center", flex="center", lh=1.0, ls=6, bleed=True, z=z + 1, rot=rot)]


def cover():
    els = [
        box(0, 0, W, 112, INK, z=1),
        T("2026 SİNEMA KARNESİ", M, 0, 700, 112, 28, "oswald", "#fff", fit=False, weight=500, ls=8, flex="center", nowrap=True, bleed=True, z=3),
        T("KARNE GÜNÜ:<br>TAKDİRİ KİMLER<br>ALDI?", M, 150, W - 2 * M, 400, 132, "anton", INK, nowrap=True, mn=64, lh=1.12),
        *stamp(730, 468, 280, rot=-10, size=52),
    ]
    y = 640
    for i, f in enumerate(FILMS):
        els += [
            rule(M, y, W - 2 * M, INK, op=0.9, h=3),
            img(grade(f[6], (170, 100), (0.1, 0, 0.9, 1)), M, y + 14, 170, 100, z=2),
            T(f[0], M + 200, y + 30, 540, 70, 42, "anton", INK, nowrap=True, mn=22, lh=1.1),
            T(f[1].replace(".", ","), W - M - 190, y + 6, 190, 112, 72, "anton", RED, fit=False, align="right", lh=1.0, flex="center", bleed=True, nowrap=True),
        ]
        y += 128
    els.append(rule(M, y, W - 2 * M, INK, op=0.9, h=3))
    els.append(T("TMDB izleyici puanı · 10 üzerinden", M, 1278, 700, 30, 20, "oswald", INK, fit=False, weight=500, ls=4, op=0.55, nowrap=True))
    return {"bg": CRM, "els": els}


def film(i, n):
    title, sc, meta, cast, body, src, _c, _t = FILMS[i]
    return {"bg": CRM, "els": [
        img(grade(src, (1080, 640), (0, 0, 1, 1)), 0, 0, W, 640, z=1),
        box(0, 380, W, 260, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.55))", z=2),
        label(f"#{i+1}", M, 50, bg=RED, color="#fff", size=26, z=6),
        *stamp(730, 560, 280, rot=-8, size=52),
        T(sc.replace(".", ","), M, 640, 380, 270, 250, "anton", RED, fit=False, lh=1.0, bleed=True, nowrap=True),
        T("/10", M + 320, 780, 120, 60, 36, "oswald", INK, fit=False, weight=500, ls=3, op=0.6, bleed=True),
        T("TMDB PUANI", M + 6, 892, 300, 28, 20, "oswald", INK, fit=False, weight=500, ls=5, op=0.6),
        box(480, 690, 3, 230, INK, z=2, op=0.2),
        T(title, 520, 700, W - 520 - M, 80, 62, "anton", INK, nowrap=True, mn=30, lh=1.1),
        T(meta, 520, 800, W - 520 - M, 90, 22, "oswald", INK, weight=500, ls=2, upper=True, mn=14, lh=1.35, op=0.65),
        rule(M, 950, W - 2 * M, INK, op=0.9, h=3),
        T("OYUNCULAR", M, 976, 300, 24, 20, "oswald", RED, fit=False, weight=500, ls=5),
        T(cast, M, 1008, W - 2 * M, 44, 28, "inter", INK, weight=600, nowrap=True, mn=18),
        T(body, M, 1074, W - 2 * M, 170, 33, "inter", INK, weight=500, lh=1.38, mn=24),
        T(f"{i+2} / {n}", M, 1278, 200, 30, 20, "oswald", INK, fit=False, weight=500, ls=4, op=0.55),
    ]}


def chart(n):
    rows = [
        ("EN İYİ FİLM", "The Odyssey", 48),
        ("EN İYİ ERKEK OYUNCU", "John Malkovich", 42),
        ("EN İYİ YARDIMCI KADIN OYUNCU", "Anne Hathaway", 56),
        ("EN İYİ FİLM ADAYLIĞI", "The Odyssey", 98),
        ("EN İYİ ERKEK OYUNCU ADAYLIĞI", "Matt Damon", 92),
    ]
    els = [
        T("KARNEDEN SONRA", M, 70, 700, 34, 24, "oswald", RED, fit=False, weight=500, ls=8, nowrap=True),
        T("OSCAR'I PİYASA<br>KİME VERİYOR?", M, 135, W - 2 * M, 280, 108, "anton", INK, nowrap=True, mn=54, lh=1.12),
    ]
    y = 440
    for lab, who, pct in rows:
        els += [
            T(lab, M, y, W - 2 * M, 28, 20, "oswald", INK, fit=False, weight=500, ls=5, nowrap=True, op=0.6),
            box(M, y + 36, 968, 76, "rgba(20,26,26,.09)", z=2),
            box(M, y + 36, int(968 * pct / 100), 76, RED if pct < 60 else INK, z=3),
            T(who, M + 22, y + 52, 600, 44, 34, "inter", "#fff", fit=False, weight=700, nowrap=True, bleed=True, z=5),
            (T(f"%{pct}", M + int(968 * pct / 100) - 190, y + 46, 170, 60, 46, "anton", "#fff", fit=False, align="right", lh=1.0, bleed=True, z=5, nowrap=True) if pct >= 60 else T(f"%{pct}", M + int(968 * pct / 100) + 20, y + 46, 170, 60, 46, "anton", INK, fit=False, lh=1.0, bleed=True, z=5, nowrap=True)),
        ]
        y += 148
    els.append(T("Kaynak: Polymarket tahmin piyasası, 29 Ekim 2026. Bunlar tahmindir, sonuç değildir. Oscar töreni 14 Mart 2027.", M, 1210, W - 2 * M, 80, 22, "inter", INK, weight=400, lh=1.4, mn=16, op=0.55))
    els.append(T(f"7 / {n}", M, 1278, 200, 30, 20, "oswald", INK, fit=False, weight=500, ls=4, op=0.55))
    return {"bg": CRM, "els": els}


def build():
    n = 8
    slides = [cover()] + [film(i, n) for i in range(5)] + [chart(n)]
    slides.append({"bg": INK, "els": [
        *stamp(M, 120, 300, rot=-6, size=56),
        T("SENCE TAKDİRİ<br>HAK EDİYORLAR<br>MI?", M, 300, W - 2 * M, 480, 112, "anton", "#fff", nowrap=True, mn=54, lh=1.14),
        T("Hangisini izledin? Yorumlara kendi puanını yaz.", M, 860, W - 2 * M, 100, 36, "inter", "#fff", weight=500, lh=1.35, mn=24),
        label("Kaydet · İzleme listene ekle", M, 1000, bg=RED, size=24),
    ]})
    return {"id": ID, "caption": CAPTION, "slides": slides}

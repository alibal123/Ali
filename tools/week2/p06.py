from pro import *

ID = "2026-11-02_liste_2026-en-yuksek-puanli-5-film"
TEAL, CRM, INK = "#0e7c7b", "#f2efe6", "#141a1a"
TH = theme(CRM, INK, TEAL, on_acc="#fff", head="anton")

CAPTION = """2026'nın şimdiye kadar en yüksek puan alan 5 filmi. Eylül 2025'ten bu yana vizyona giren ve en az 1.500 oy almış filmler arasında TMDB izleyici puanına göre en tepedekiler hepsi bu yılın yapımı çıktı.

Yerime Geç 8,8 ile zirvede. Onu 8,6 ile Kurtuluş Projesi ve Michael, 8,5 ile Örümcek-Adam: Yepyeni Bir Gün, 8,3 ile Oyuncak Hikayesi 5 izliyor. Puanlar zamanla değişebilir.

Sen hangisini izledin, puanı hak ediyor mu?

Yarın 18:00'de: Çocukken izlediğin, büyüyünce başka vuran 5 animasyon."""

FILMS = [
    ("YERİME GEÇ", "8.8", "1 Mayıs 2026 · Nathan Greno", "Michael B. Jordan, Juno Temple, Tracy Morgan",
     "Ormanda yaşayan küçük bir canlıyla görkemli bir kuşun bedenleri aniden yer değiştirir; hayatta kalmak için birlik olmaları gerekir.", S("swapped", 3), S("swapped", 1), "Swapped"),
    ("KURTULUŞ PROJESİ", "8.6", "20 Mart 2026 · Phil Lord, Christopher Miller", "Ryan Gosling, Sandra Hüller, James Ortiz",
     "Fen bilgisi öğretmeni Ryland Grace, ışık yılları uzakta bir uzay gemisinde hafızasını kaybetmiş halde uyanır ve Güneş'in sönmesinin sırrını çözmeye çalışır.", S("hailmary", 4), S("hailmary", 3), "Project Hail Mary"),
    ("MICHAEL", "8.6", "24 Nisan 2026 · Antoine Fuqua", "Jaafar Jackson, Colman Domingo, Nia Long",
     "Michael Jackson'ı gerçek hayattaki yeğeni Jaafar Jackson canlandırıyor; film en ikonik performansları da içeriyor.", S("michael", 4), S("michael", 1), "Biyografi"),
    ("ÖRÜMCEK-ADAM: YEPYENİ BİR GÜN", "8.5", "31 Temmuz 2026 · Destin Daniel Cretton", "Tom Holland, Sadie Sink, Zendaya",
     "Artık kimsenin hatırlamadığı Peter Parker, şehre yönelen yeni bir tehdidi durdurmaya çalışır.", S("spiderman", 2), S("spiderman", 1), "Spider-Man: Brand New Day"),
    ("OYUNCAK HİKAYESİ 5", "8.3", "19 Haziran 2026 · Andrew Stanton", "Tom Hanks, Tim Allen, Joan Cusack",
     "Bonnie'nin bir tablete takıntılı hale gelmesiyle Buzz, Woody ve Jessie için işler iyice karışır.", S("toystory5", 3), S("toystory5", 1), "Toy Story 5"),
]


def cover():
    els = [
        *kicker(TH, "TMDB izleyici puanı", M, 70),
        T("2026'NIN EN<br>YÜKSEK PUANLI<br>5 FİLMİ", M, 130, W - 2 * M, 400, 130, "anton", INK, nowrap=True, mn=64, lh=1.07),
    ]
    y = 590
    track_x, track_w = M + 120, 560
    for k, f in enumerate(FILMS):
        sc = float(f[1])
        els += [
            img(grade(f[6], (96, 96)), M, y, 96, 96, z=2),
            T(f[0], track_x, y - 4, W - track_x - M - 150, 44, 30, "oswald", INK, weight=500, ls=2, nowrap=True, mn=16, upper=True),
            box(track_x, y + 60, track_w, 14, "rgba(20,26,26,.10)", z=2),
            box(track_x, y + 60, int(track_w * sc / 10), 14, TEAL, z=3),
            T(f[1].replace(".", ","), W - M - 150, y + 6, 150, 70, 64, "anton", TEAL, fit=False, align="right", lh=1.0, nowrap=True, bleed=True),
        ]
        y += 116
    els += [T("Eylül 2025'ten bu yana vizyona girenler arasında, en az 1.500 oy.", M, 1224, W - 2 * M - 70, 30, 22, "inter", INK, weight=500, nowrap=True, mn=14, op=0.6),
            logo("black", W - M - 58, 1252, 58, z=9)]
    return {"bg": CRM, "els": els}


def score_film(i, n):
    title, sc, meta, kadro, konu, src, _c, tag = FILMS[i]
    ph = 700
    ts = fit(title, 620, 92, 0.5, 40)
    return {"bg": CRM, "els": [
        img(grade(src, (1080, ph)), 0, 0, W, ph, z=1),
        label(tag, M, 56),
        box(W - M - 236, ph - 118, 236, 236, "#fff", z=4, radius=400, border=f"12px solid {TEAL}"),
        T(sc.replace(".", ","), W - M - 236, ph - 118, 236, 236, 92, "anton", TEAL, fit=False, align="center", flex="center", lh=1.0, bleed=True, z=5),
        T("#" + str(i + 1), M, ph + 30, 300, 40, 28, "oswald", TEAL, fit=False, weight=500, ls=6, nowrap=True),
        T(title, M, ph + 96, 640, 110, 90, "anton", INK, nowrap=True, mn=38, lh=1.05),
        T(meta, M, ph + 214, 700, 34, 24, "oswald", INK, weight=500, ls=3, upper=True, nowrap=True, mn=15, op=0.6),
        rule(M, ph + 262, W - 2 * M, INK),
        T("Oyuncular: " + kadro, M, ph + 282, W - 2 * M, 40, 28, "inter", INK, weight=500, nowrap=True, mn=18, op=0.85),
        T(konu, M, ph + 336, W - 2 * M, 150, 34, "inter", INK, weight=500, lh=1.4, mn=24),
        *footer(TH, i + 2, n),
    ]}


def build():
    n = 7
    slides = [cover()] + [score_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "SENCE PUANI<br>HAK EDİYOR MU?", "Hangisini izledin? Yorumlara kendi puanını yaz.", "Kaydet · İzleme listene ekle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

from pro import *

ID = "2026-11-01_eslestirme_bunu-sevdiysen"
TH = theme("#f4efe6", "#14110f", "#ff4f5e", on_acc="#fff", head="anton")

CAPTION = """Bunu sevdiysen şunu izle: aynı tadı veren 4 film çifti.

Inception'ı sevdiysen Paprika'ya, Forrest Gump'ı sevdiysen Big Fish'e, Knives Out'u sevdiysen Gosford Park'a, Parasite'i sevdiysen Shoplifters'a bak. Son çiftin ikisi de Cannes'da Altın Palmiye aldı: Shoplifters 2018'de, Parasite 2019'da.

Sen hangi eşleşmeyi eklerdin? "X sevdiysen Y" diye yorumlara yaz.

Yarın 13:00'te: Kasım ayında sinemaya gelecek 5 film."""


PAIRS = [
    # A: başlık, meta, slayt karesi, kapak karesi | B: ... | sebep, etiket
    (("INCEPTION", "2010 · Christopher Nolan", S("inception", 2), S("inception", 1)),
     ("PAPRIKA", "2006 · Satoshi Kon", S("paprika", 2), S("paprika", 1)),
     "Rüyaların içine girmeyi sevdiysen: Paprika'da terapistlerin hastalarının rüyalarına girmesini sağlayan bir makine çalınıyor.", "#ffd9c7"),
    (("FORREST GUMP", "1994 · Robert Zemeckis", S("forrestgump", 3), S("forrestgump", 1)),
     ("BIG FISH", "2003 · Tim Burton", S("bigfish", 3), S("bigfish", 1)),
     "Hayatı masal gibi anlatan adamları sevdiysen: Big Fish'te ölüm döşeğindeki babanın hikâyelerinin ardındaki gerçeği arayan bir oğul var.", "#cfe8ff"),
    (("KNIVES OUT", "2019 · Rian Johnson", S("knivesout", 1), S("knivesout", 2)),
     ("GOSFORD PARK", "2001 · Robert Altman", S("gosford", 3), S("gosford", 2)),
     "Bir malikane, bir cinayet, herkes şüpheli: Gosford Park 1932'de geçen, kalabalık kadrolu bir polisiye.", "#e5d6ff"),
    (("PARASITE", "2019 · Bong Joon-ho", S("parasite", 2), S("parasite", 1)),
     ("SHOPLIFTERS", "2018 · Hirokazu Kore-eda", S("shoplifters", 2), S("shoplifters", 1)),
     "Sınıf farkını incelikle anlatan iki film: ikisi de Cannes'da Altın Palmiye aldı. Shoplifters, geçimini hırsızlıkla sağlayan bir ailenin hikâyesi.", "#cdf5dc"),
]






def half(src, x, w, h, gray):
    return img(prep(src, size=(w, h), gray=gray, contrast=1.1, sat=(1.0 if gray else 1.12), grain=8), x, 0, w, h, z=1)


def split_pair(i, n):
    a, b, why, _ = PAIRS[i]
    ph = 980
    return {"bg": TH["bg"], "els": [
        half(a[2], 0, 540, ph, True), half(b[2], 540, 540, ph, False),
        box(0, ph - 360, W, 360, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.82))", z=2),
        T("SEVDİN", M, ph - 190, 300, 28, 20, "oswald", "#fff", fit=False, weight=500, ls=6, op=0.75),
        T(a[0], M, ph - 150, 440, 80, 60, "anton", "#fff", nowrap=True, mn=28, lh=1.05),
        T(a[1], M, ph - 62, 440, 30, 18, "oswald", "#fff", weight=500, ls=3, upper=True, nowrap=True, mn=12, op=0.75),
        T("İZLE", 570, ph - 190, 300, 28, 20, "oswald", TH["accent"], fit=False, weight=500, ls=6),
        T(b[0], 570, ph - 150, 440, 80, 60, "anton", "#fff", nowrap=True, mn=28, lh=1.05),
        T(b[1], 570, ph - 62, 440, 30, 18, "oswald", "#fff", weight=500, ls=3, upper=True, nowrap=True, mn=12, op=0.75),
        box(W // 2 - 70, 400, 140, 140, TH["accent"], z=5, radius=300),
        T("→", W // 2 - 70, 400, 140, 140, 84, "inter", "#fff", fit=False, weight=700, align="center", flex="center", lh=1.0, bleed=True, z=6),
        T(why, M, ph + 44, W - 2 * M, 230, 36, "inter", TH["ink"], weight=500, lh=1.4, mn=26),
        *footer(TH, i + 2, n),
    ]}


def build():
    n = 6
    els = []
    for k, p in enumerate(PAIRS):
        y = k * 337
        els.append(img(prep(p[0][3], size=(540, 337), gray=True, contrast=1.1, grain=8), 0, y, 540, 338, z=1))
        els.append(img(prep(p[1][3], size=(540, 337), contrast=1.05, sat=1.12, grain=8), 540, y, 540, 338, z=1))
    els += [
        box(60, 470, 960, 410, TH["accent"], z=4),
        T("BUNU SEVDİYSEN,<br>BUNU İZLE", 100, 500, 880, 250, 130, "anton", "#fff", nowrap=True, mn=60, lh=1.08, align="center", z=5),
        T("SOLDAKİ SEVDİĞİN, SAĞDAKİ İZLEYECEĞİN FİLM", 100, 790, 880, 36, 22, "oswald", "#fff", weight=500, ls=4, align="center", nowrap=True, mn=14, z=5, op=0.9),
        logo("white", W - M - 58, 64, 58, z=9),
    ]
    cover = {"bg": TH["bg"], "els": els}
    slides = [cover] + [split_pair(i, n) for i in range(4)]
    slides.append(cta_slide(TH, "SEN HANGİ<br>EŞLEŞMEYİ<br>EKLERDİN?", "\"X sevdiysen Y izle\" diye yorumlara yaz.", "Kaydet · Arkadaşına gönder"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

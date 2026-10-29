from pro import *

ID = "2026-11-01_eslestirme_bunu-sevdiysen"
CRM, INK = "#f3f1ec", "#0c0c0f"
TH = theme(CRM, INK, "#ff4f5e", on_acc="#fff", head="anton")

CAPTION = """Film bitti, boşluk kaldı. Sevdiğin filmin ardından açabileceğin 3 yeni kapı.

Knives Out'u sevdiysen Gosford Park'a, Parasite'i sevdiysen Shoplifters'a, La La Land'i sevdiysen Whiplash'e bak. Parasite ile Shoplifters Cannes'da Altın Palmiye aldı (Shoplifters 2018'de, Parasite 2019'da); La La Land ile Whiplash'in yönetmeni aynı: Damien Chazelle.

Sen hangi eşleşmeyi eklerdin? "X sevdiysen Y" diye yorumlara yaz.

Yarın 13:00'te: Kasım ayında sinemaya gelecek 8 film."""

PAIRS = [
    (("KNIVES OUT", "2019 · Rian Johnson", S("knivesout", 2), .57), ("GOSFORD PARK", "2001 · Robert Altman", S("gosford", 2), .72), "#ff4f5e",
     "Bir malikane, bir cinayet, herkes şüpheli. Gosford Park, 1932'de geçen kalabalık kadrolu bir polisiye; Knives Out'un ilham aldığı türün ustası."),
    (("PARASITE", "2019 · Bong Joon-ho", S("parasite", 2), .38), ("SHOPLIFTERS", "2018 · Hirokazu Kore-eda", S("shoplifters", 1), .58), "#ffc933",
     "Sınıf farkını incelikle anlatan iki film; ikisi de Cannes'da Altın Palmiye aldı. Shoplifters, geçimini hırsızlıkla sağlayan bir ailenin hikâyesi."),
    (("LA LA LAND", "2016 · Damien Chazelle", S("lalaland", 2), .55), ("WHIPLASH", "2014 · Damien Chazelle", S("whiplash", 1), .3), "#8f6bff",
     "İkisi de Damien Chazelle filmi. La La Land'in büyülü müziğinden sonra Whiplash, tutkunun bedelini bir davulcu üzerinden anlatıyor."),
]
LOGO = dict(pos="tr", w=70, on_light="black", on_dark="white")


def half(name, cx, x, gray, col, title, meta):
    crop = (max(0, cx - 0.2), 0, min(1, cx + 0.2), 1)
    tx = x + (M if gray else 36)
    return [
        img(grade(name, (540, 860), crop, grain=8, contrast=(1.18 if gray else 1.08), sat=(0.0 if gray else 1.12)), x, 0, 540, 860, z=1),
        T(title, tx, 910, 468, 100, 76, "anton", ("#fff" if gray else col), nowrap=True, mn=32, lh=1.12, z=6),
        T(meta, tx, 1018, 468, 28, 20, "oswald", "#fff", weight=500, ls=3, upper=True, nowrap=True, mn=12, z=6, op=0.75),
    ]


def pair_slide_n(i, n):
    a, b, col, why = PAIRS[i]
    return {"bg": INK, "els": [
        *half(a[2], a[3], 0, True, col, a[0], a[1]),
        *half(b[2], b[3], 540, False, col, b[0], b[1]),
        box(0, 0, W, 130, "linear-gradient(180deg,rgba(0,0,0,.6),rgba(0,0,0,0))", z=3),
        box(538, 0, 4, 1060, "#fff", z=4, op=0.9),
        label("BİTTİ", M, 56, bg="#fff", color=INK, size=22, z=7),
        label("SIRADAKİ", 576, 56, bg=col, color=INK, size=22, z=7),
        box(540 - 46, 814 - 46, 92, 92, col, z=8, radius=300),
        T("→", 540 - 46, 814 - 46, 92, 92, 52, "inter", INK, fit=False, weight=700, align="center", flex="center", lh=1.0, bleed=True, z=9),
        rule(M, 1076, W - 2 * M, "#fff", op=0.25, h=2),
        T(why, M, 1104, W - 2 * M, 150, 33, "inter", "#fff", weight=400, lh=1.4, mn=24, z=6, op=0.95),
        T(f"{i+2:02d} / {n:02d}", M, 1288, 200, 26, 20, "oswald", "#fff", fit=False, weight=500, ls=5, op=0.55, z=6),
    ]}


def build():
    n = 5
    cov = {"bg": INK, "els": [
        img(grade(S("lalaland", 2), (1080, 800), (0.0, 0.05, 1, 0.95), grain=8, contrast=1.1), 0, 0, W, 800, z=1),
        img(grade(S("lalaland", 2), (1080, 800), (0.0, 0.05, 1, 0.95), grain=8, contrast=1.18, sat=0.0), 0, 0, W, 800, z=2, clip="polygon(0 0, 50% 0, 50% 100%, 0 100%)"),
        box(538, 0, 4, 800, "#fff", z=4, op=0.9),
        label("3 EŞLEŞME", M, 56, bg="#fff", color=INK, size=22, z=7),
        label("BİTTİ", M, 710, bg="#fff", color=INK, size=22, z=7),
        label("BAŞLIYOR", 576, 710, bg="#ff4f5e", color=INK, size=22, z=7),
        T("FİLM BİTTİ,<br>BOŞLUK KALDI", M, 840, W - 2 * M, 330, 150, "anton", "#fff", nowrap=True, mn=70, lh=1.1, z=6),
        T("Sevdiğin filmin ardından açılacak 3 yeni kapı.", M, 1190, W - 2 * M - 100, 50, 34, "inter", "#fff", weight=500, nowrap=True, mn=20, z=6, op=0.9),
    ]}
    slides = [cov] + [pair_slide_n(i, n) for i in range(3)]
    slides.append({"bg": "#ff4f5e", "els": [
        T("SEN HANGİ<br>EŞLEŞMEYİ<br>EKLERDİN?", M, 110, W - 2 * M, 560, 150, "anton", INK, nowrap=True, mn=70, lh=1.12),
        T("\"X sevdiysen Y izle\" diye yorumlara yaz.", M, 740, W - 2 * M, 100, 38, "inter", INK, weight=600, lh=1.3, mn=24),
        label("Kaydet · Arkadaşına gönder", M, 900, bg=INK, color="#fff", size=24),
    ]})
    return {"id": ID, "caption": CAPTION, "slides": slides}

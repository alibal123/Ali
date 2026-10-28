from pro import *

ID = "2026-11-01_eslestirme_bunu-sevdiysen"
CRM, INK = "#f3f1ec", "#14110f"
TH = theme(CRM, INK, "#ff4f5e", on_acc="#fff", head="anton")

CAPTION = """Film bitti, boşluk kaldı. Sevdiğin filmin ardından açabileceğin 3 yeni kapı.

Knives Out'u sevdiysen Gosford Park'a, Parasite'i sevdiysen Shoplifters'a, La La Land'i sevdiysen Whiplash'e bak. Parasite ile Shoplifters Cannes'da Altın Palmiye aldı (Shoplifters 2018'de, Parasite 2019'da); La La Land ile Whiplash'in yönetmeni aynı: Damien Chazelle.

Sen hangi eşleşmeyi eklerdin? "X sevdiysen Y" diye yorumlara yaz.

Yarın 13:00'te: Kasım ayında sinemaya gelecek 5 film."""

PAIRS = [
    (("KNIVES OUT", "2019 · Rian Johnson", S("knivesout", 1), (0, 0.12, 1, 0.82)), ("GOSFORD PARK", "2001 · Robert Altman", S("gosford", 3), (0, 0.05, 1, 0.78)), "#e8412e", "#2447d9",
     "Bir malikane, bir cinayet, herkes şüpheli. Gosford Park, 1932'de geçen kalabalık kadrolu bir polisiye; Knives Out'un ilham aldığı türün ustası."),
    (("PARASITE", "2019 · Bong Joon-ho", S("parasite", 1), (0, 0.1, 1, 0.85)), ("SHOPLIFTERS", "2018 · Hirokazu Kore-eda", S("shoplifters", 1), (0, 0.1, 1, 0.85)), "#e9a800", "#0f8f6a",
     "Sınıf farkını incelikle anlatan iki film: ikisi de Cannes'da Altın Palmiye aldı. Shoplifters, geçimini hırsızlıkla sağlayan bir ailenin hikâyesi."),
    (("LA LA LAND", "2016 · Damien Chazelle", S("lalaland", 2), (0, 0.08, 1, 0.9)), ("WHIPLASH", "2014 · Damien Chazelle", S("whiplash", 5), (0, 0.1, 1, 0.8)), "#7a4dff", "#d6336c",
     "İkisi de Damien Chazelle filmi. La La Land'in büyülü müziğinden sonra Whiplash, tutkunun bedelini bir davulcu üzerinden anlatıyor."),
]
LOGO = dict(pos="tr", w=78, on_light="red", on_dark="white")


def shot(name, crop, x, y, w, h, title, meta, chip, col, ts=84, z=2):
    return [
        img(grade(name, (w, h), crop), x, y, w, h, z=z),
        box(x, y + h // 2, w, h - h // 2, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.78))", z=z + 1),
        label(chip, x + M, y + 28, bg=col, color="#fff", size=22, z=z + 3),
        T(title, x + M, y + h - 176, w - 2 * M, 100, ts, "anton", "#fff", nowrap=True, mn=40, lh=1.12, z=z + 3),
        T(meta, x + M, y + h - 58, w - 2 * M, 30, 22, "oswald", "#fff", weight=500, ls=4, upper=True, nowrap=True, mn=14, z=z + 3, op=0.85),
    ]


def pair_slide_n(i, n):
    a, b, c1, c2, why = PAIRS[i]
    return {"bg": CRM, "els": [
        T(f"{i+1:02d}", M, 40, 200, 70, 52, "anton", INK, fit=False, lh=1.0, nowrap=True),
        *shot(a[2], a[3], 0, 120, W, 440, a[0], a[1], "SEVDİN", c1),
        box(0, 560, W, 90, INK, z=4),
        T("BUNU SEVDİYSEN, ŞUNA BAK", M, 560, W - 2 * M - 120, 90, 30, "oswald", "#fff", fit=False, weight=500, ls=6, flex="center", nowrap=True, bleed=True, z=6),
        box(W - M - 90, 545, 90, 90, c2, z=7, radius=300),
        T("↓", W - M - 90, 545, 90, 90, 56, "inter", "#fff", fit=False, weight=700, align="center", flex="center", lh=1.0, bleed=True, z=8),
        *shot(b[2], b[3], 0, 650, W, 440, b[0], b[1], "İZLE", c2),
        T(why, M, 1118, W - 2 * M, 170, 34, "inter", INK, weight=500, lh=1.38, mn=24),
        T(f"{i+2} / {n}", M, 1284, 200, 30, 20, "oswald", INK, fit=False, weight=500, ls=4, op=0.55),
    ]}


def build():
    n = 5
    els = [
        *kicker(TH, "3 eşleşme", M, 50),
        T("FİLM BİTTİ,<br>BOŞLUK KALDI", M, 135, W - 2 * M, 380, 170, "anton", INK, nowrap=True, mn=70, lh=1.1),
    ]
    rh, gap, y0 = 214, 18, 560
    for k, p in enumerate(PAIRS):
        y = y0 + k * (rh + gap)
        for j, (f, col) in enumerate(((p[0], p[2]), (p[1], p[3]))):
            x = M + j * 506 + (0 if j == 0 else 0)
            w = 506 - 12
            els.append(img(grade(f[2], (w, rh), f[3]), x, y, w, rh, z=2))
            els.append(box(x, y + rh // 2, w, rh - rh // 2, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.75))", z=3))
            els.append(box(x, y, 10, rh, col, z=4))
            els.append(T(f[0], x + 28, y + rh - 62, w - 50, 44, 36, "anton", "#fff", nowrap=True, mn=18, lh=1.1, z=5))
        els.append(box(540 - 36, y + rh // 2 - 36, 72, 72, INK, z=7, radius=300))
        els.append(T("→", 540 - 36, y + rh // 2 - 36, 72, 72, 40, "inter", "#fff", fit=False, weight=700, align="center", flex="center", lh=1.0, bleed=True, z=8))
    els += [T("Sevdiğin filmin ardından açılacak 3 yeni kapı.", M, 1262, W - 2 * M - 120, 40, 28, "inter", INK, weight=500, nowrap=True, mn=18, op=0.8)]
    slides = [{"bg": CRM, "els": els}] + [pair_slide_n(i, n) for i in range(3)]
    slides.append(cta_slide(TH, "SEN HANGİ<br>EŞLEŞMEYİ<br>EKLERDİN?", "\"X sevdiysen Y izle\" diye yorumlara yaz.", "Kaydet · Arkadaşına gönder"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

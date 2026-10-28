from pro import *
import cut

ID = "2026-11-01_eslestirme_bunu-sevdiysen"
CRM, INK = "#f3f1ec", "#14110f"
TH = theme(CRM, INK, "#ff4f5e", on_acc="#fff", head="anton")

CAPTION = """Film bitti, boşluk kaldı. Sevdiğin filmin ardından açabileceğin 3 yeni kapı.

Knives Out'u sevdiysen Gosford Park'a, Parasite'i sevdiysen Shoplifters'a, La La Land'i sevdiysen Whiplash'e bak. Parasite ile Shoplifters Cannes'da Altın Palmiye aldı (Shoplifters 2018'de, Parasite 2019'da); La La Land ile Whiplash'in yönetmeni aynı: Damien Chazelle.

Sen hangi eşleşmeyi eklerdin? "X sevdiysen Y" diye yorumlara yaz.

Yarın 13:00'te: Kasım ayında sinemaya gelecek 5 film."""

PAIRS = [
    # A: (ad, başlık, meta, kesit)  B: ...   renk1, renk2, sebep
    (("KNIVES OUT", "2019 · Rian Johnson", "knivesout_2"), ("GOSFORD PARK", "2001 · Robert Altman", "gosford_2"), "#e8412e", "#2447d9",
     "Bir malikane, bir cinayet, herkes şüpheli: Gosford Park 1932'de geçen, kalabalık kadrolu bir polisiye."),
    (("PARASITE", "2019 · Bong Joon-ho", "parasite_2"), ("SHOPLIFTERS", "2018 · Hirokazu Kore-eda", "shoplifters_3"), "#ffc933", "#0f8f6a",
     "Sınıf farkını incelikle anlatan iki film: ikisi de Cannes'da Altın Palmiye aldı. Shoplifters, geçimini hırsızlıkla sağlayan bir ailenin hikâyesi."),
    (("LA LA LAND", "2016 · Damien Chazelle", "lalaland_2"), ("WHIPLASH", "2014 · Damien Chazelle", "whiplash_3"), "#7a4dff", "#ff7aa8",
     "İkisi de Damien Chazelle filmi: La La Land'in büyülü müziğinin ardından Whiplash, tutkunun bedelini bir davulcu üzerinden anlatıyor."),
]


def dark(c, f=0.8):
    c = c.lstrip("#")
    return "#" + "".join(f"{int(int(c[k:k + 2], 16) * f):02x}" for k in (0, 2, 4))


def wall(x, y, w, h, c):
    return box(x, y, w, h, dark(c), z=6)


PART = {"gosford_2": (0.46, 1.0), "whiplash_3": (0.24, 0.80)}


def fig(name, bx, bw, bottom, max_h, gray, z, max_w=None):
    p, w, h = cut.figure(name, max_w or bw + 40, max_h, gray=gray, contrast=(1.12 if gray else 1.04), sat=1.06, part=PART.get(name))
    return img(p, bx + (bw - w) // 2, bottom - h, w, h, z=z, fit="contain")


def pair_slide_n(i, n):
    a, b, c1, c2, why = PAIRS[i]
    by, bh, bw = 330, 570, 452
    bx1, bx2 = 64, 564
    return {"bg": CRM, "els": [
        T(f"{i+1:02d}", M, 70, 200, 60, 44, "anton", INK, fit=False, lh=1.0, nowrap=True),
        T("SEVDİYSEN → İZLE", W - M - 500, 84, 500, 34, 24, "oswald", INK, fit=False, weight=500, ls=6, align="right", nowrap=True, op=0.6),
        box(bx1, by, bw, bh, c1, z=2), box(bx2, by, bw, bh, c2, z=2),
        fig(a[2], bx1, bw, 880, 640, True, 4, max_w=bw + 20), fig(b[2], bx2, bw, 880, 640, False, 4, max_w=bw + 20),
        wall(bx1, 836, bw, 64, c1), wall(bx2, 836, bw, 64, c2),
        box(W // 2 - 48, 560, 96, 96, INK, z=9, radius=300),
        T("→", W // 2 - 48, 560, 96, 96, 56, "inter", "#fff", fit=False, weight=700, align="center", flex="center", lh=1.0, bleed=True, z=10),
        T("SEVDİN", bx1, 922, 300, 26, 20, "oswald", INK, fit=False, weight=500, ls=6, op=0.6),
        T(a[0], bx1, 962, bw, 70, 54, "anton", INK, nowrap=True, mn=26, lh=1.05),
        T(a[1], bx1, 1036, bw, 28, 17, "oswald", INK, weight=500, ls=3, upper=True, nowrap=True, mn=12, op=0.6),
        T("İZLE", bx2, 922, 300, 26, 20, "oswald", c2 if c2 != "#ffc933" else INK, fit=False, weight=500, ls=6),
        T(b[0], bx2, 962, bw, 70, 54, "anton", INK, nowrap=True, mn=26, lh=1.05),
        T(b[1], bx2, 1036, bw, 28, 17, "oswald", INK, weight=500, ls=3, upper=True, nowrap=True, mn=12, op=0.6),
        T(why, M, 1096, W - 2 * M, 140, 32, "inter", INK, weight=500, lh=1.4, mn=22),
        *footer(TH, i + 2, n),
    ]}


def build():
    n = 5
    els = [
        *kicker(TH, "3 eşleşme", M, 70),
        T("FİLM BİTTİ,<br>BOŞLUK KALDI", M, 140, W - 2 * M, 340, 170, "anton", INK, nowrap=True, mn=70, lh=1.08),
    ]
    bw, by, bh = 300, 560, 540
    for k, p in enumerate(PAIRS):
        bx = M + k * (bw + 18)
        els += [box(bx, by, bw, bh, p[3], z=2), fig(p[0][2], bx, bw, 1070, 640, False, 4, max_w=bw + 20), wall(bx, 1030, bw, 70, p[3])]
    els += [T("Sevdiğin filmin ardından açılacak 3 yeni kapı.", M, 1150, W - 2 * M - 80, 40, 30, "inter", INK, weight=500, nowrap=True, mn=20, op=0.8),
            T("Kaydet · Sırayla izle", M, 1206, 500, 30, 22, "oswald", INK, fit=False, weight=500, ls=5, upper=True, nowrap=True, op=0.55),
            logo("black", W - M - 58, 1252, 58, z=9)]
    slides = [{"bg": CRM, "els": els}] + [pair_slide_n(i, n) for i in range(3)]
    slides.append(cta_slide(TH, "SEN HANGİ<br>EŞLEŞMEYİ<br>EKLERDİN?", "\"X sevdiysen Y izle\" diye yorumlara yaz.", "Kaydet · Arkadaşına gönder"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

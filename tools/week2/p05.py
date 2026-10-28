from pro import *

ID = "2026-11-02_vizyon_kasim-takvimi"
RED, BLU, INK = "#e23d3d", "#2447ff", "#14110f"
TH = theme("#f4efe6", "#14110f", "#e23d3d", on_acc="#fff", head="anton")

CAPTION = """Kasım'da sinemada ne var? Takvimi tek gönderide topladık.

Şapkalı Kedi ve Vahşi At Dokuz 6 Kasım'da, Godzilla Minus Zero ve Ebenezer: Bir Noel Şarkısı 13 Kasım'da, Açlık Oyunları: Hasatta Gündoğumu 20 Kasım'da, Zor Baba 4, Kağıttan Kaplan ve Hexe: Sihir Krallığı ise 27 Kasım'da vizyonda. Tarihler Türkiye vizyon takvimine göre verildi, seans günleri sinemaya göre değişebilir.

Sen ilk hangisine gideceksin?

Bugün 18:00'de: 2026 karne günü, yılın takdir alan filmleri ve Oscar piyasası."""


FILMS = [
    # başlık, tarih(gün), yönetmen, kadro, konu, kare, kapak karesi, renk
    ("ŞAPKALI KEDİ", "6", "Erica Rivinoja, Alessandro Carloni", "Bill Hader, Xochitl Gomez, Quinta Brunson",
     "Yeni taşındıkları kasabada iki kardeşi neşelendirmekle görevlendirilen Şapkalı Kedi, sihirli şapkasını kaybetme riskiyle karşı karşıya kalır.", S("catinhat", 3), S("catinhat", 1), RED),
    ("GODZILLA MINUS ZERO", "13", "Takashi Yamazaki", "Ryunosuke Kamiki, Minami Hamabe, Yuki Yamada",
     "Godzilla Minus One'dan iki yıl sonra, 1949'da Shikishima ailesi için yepyeni bir yıkım kapıda.", S("godzilla", 2), S("godzilla", 4), BLU),
    ("EBENEZER:<br>BİR NOEL ŞARKISI", "13", "Ti West", "Johnny Depp, Rupert Grint, Daisy Ridley",
     "Cimri Scrooge, Noel arifesinde hayatını değiştirecek doğaüstü ziyaretçilerle karşılaşır.", S("ebenezer", 1), S("ebenezer", 3), "#2f9e6b"),
    ("AÇLIK OYUNLARI:<br>HASATTA GÜNDOĞUMU", "20", "Francis Lawrence", "Joseph Zada, Ralph Fiennes, Jesse Plemons",
     "Ana seriden 24 yıl öncesine dönüyoruz: 50. Açlık Oyunları'nın kura çekimi.", S("hungergames", 2), S("hungergames", 1), "#e8890c"),
    ("ZOR BABA 4", "27", "John Hamburg", "Ben Stiller, Robert De Niro, Ariana Grande, Owen Wilson",
     "Greg ve Pam Focker'ın oğlu Henry, kendisiyle hiç uyuşmayan iradeli bir kadınla evlenmeye karar verince ailede kaos çıkar.", S("focker", 1), S("focker", 2), "#8a3ffc"),
]





FIL = {6: [S("catinhat", 1), S("wildhorse", 3)], 13: [S("godzilla", 4), S("ebenezer", 3)], 20: [S("hungergames", 1)], 27: [S("focker", 2), S("papertiger", 2), S("hexed", 3)]}
LOGO = dict(pos="bc", w=88, on_light="red", on_dark="white")
TURLER = ["ANİMASYON · AİLE", "CANAVAR · AKSİYON", "FANTEZİ · NOEL", "DİSTOPYA · MACERA", "KOMEDİ · AİLE"]
EXTRA = [
    ("VAHŞİ AT DOKUZ", "6 KASIM", "Martin McDonagh", "John Malkovich, Sam Rockwell, Steve Buscemi", S("wildhorse", 3)),
    ("KAĞITTAN KAPLAN", "27 KASIM", "James Gray", "Miles Teller, Adam Driver, Scarlett Johansson", S("papertiger", 2)),
    ("HEXE: SİHİR KRALLIĞI", "27 KASIM", "Jason Hand", "Hailee Steinfeld, Rashida Jones, Jodie Foster", S("hexed", 3)),
]


def cal_cover():
    cw, ch, gap = 128, 108, 6
    gx, gy = M, 540
    els = [
        *kicker(TH, "Vizyon takvimi", M, 56),
        T("SİNEMADA BU AY<br>NE VAR?", M, 170, W - 2 * M, 320, 170, "anton", INK, nowrap=True, mn=70, lh=1.06),
    ]
    for c, d in enumerate(["PZT", "SAL", "ÇAR", "PER", "CUM", "CMT", "PAZ"]):
        els.append(T(d, gx + c * (cw + gap), gy - 40, cw, 28, 20, "oswald", INK, fit=False, weight=500, ls=3, align="center", op=0.55, bleed=True))
    for d in range(1, 31):
        idx = (d - 1) + 6
        r, c = idx // 7, idx % 7
        x, y = gx + c * (cw + gap), gy + r * (ch + gap)
        if d in FIL:
            ph = FIL[d]
            for k, nm in enumerate(ph):
                w = cw // len(ph)
                els.append(img(grade(nm, (w, ch), (0.3, 0, 0.7, 1)), x + k * w, y, w, ch, z=2))
            els.append(box(x, y, cw, ch, "linear-gradient(180deg,rgba(0,0,0,.0),rgba(0,0,0,.55))", z=3))
            els.append(T(str(d), x + 10, y + ch - 46, 100, 40, 34, "anton", "#fff", fit=False, bleed=True, z=5, lh=1.0))
            els.append(box(x, y, cw, 6, RED, z=4))
        else:
            els.append(box(x, y, cw, ch, "rgba(20,17,15,.05)", z=1))
            els.append(T(str(d), x + 12, y + 10, 100, 34, 26, "oswald", INK, fit=False, bleed=True, weight=500, op=0.45))
    els += [
        T("Hepsi cuma. Kaydet.", M, 1236, 800, 36, 26, "inter", INK, weight=500, nowrap=True, op=0.75),
    ]
    return {"bg": TH["bg"], "els": els}


def cal_film(i, n):
    title, day, yon, kadro, konu, src, _, _c = FILMS[i]
    return {"bg": TH["bg"], "els": [
        img(grade(src, (1080, 640)), 0, 0, W, 640, z=1),
        box(0, 400, W, 240, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.6))", z=2),
        box(M, 40, 210, 220, "#fff", z=5, radius=22),
        box(M, 40, 210, 62, RED, z=6, radius=22),
        box(M, 80, 210, 22, RED, z=6),
        T("KASIM", M, 40, 210, 62, 28, "oswald", "#fff", fit=False, weight=600, ls=8, align="center", flex="center", bleed=True, z=8),
        T(day, M, 100, 210, 140, 130, "anton", RED, fit=False, align="center", lh=1.0, bleed=True, z=8),
        T("CUMA", M, 218, 210, 30, 20, "oswald", INK, fit=False, weight=500, ls=6, align="center", bleed=True, z=8, op=0.6),
        label(TURLER[i], W - M - 400, 56, bg=INK, color="#fff", size=22, z=8),
        T(title, M, 664, W - 2 * M, 190, 84, "anton", INK, nowrap=True, mn=40, lh=1.12),
        T(f"YÖNETMEN · {yon}".upper(), M, 868, W - 2 * M, 34, 24, "oswald", RED, weight=500, ls=4, nowrap=True, mn=14),
        rule(M, 924, W - 2 * M, INK, op=0.85, h=3),
        T("KADRO", M, 948, 300, 26, 20, "oswald", RED, fit=False, weight=500, ls=6),
        T(kadro, M, 982, 400, 250, 32, "inter", INK, weight=600, lh=1.35, mn=22),
        box(M + 440, 950, 3, 290, INK, z=2, op=0.2),
        T("KONU", M + 480, 948, 300, 26, 20, "oswald", RED, fit=False, weight=500, ls=6),
        T(konu, M + 480, 982, W - 2 * M - 480, 250, 32, "inter", INK, weight=500, lh=1.35, mn=22),
        T(f"{i+2} / {n}", M, 1284, 200, 30, 20, "oswald", INK, fit=False, weight=500, ls=4, op=0.55),
    ]}


def extra_slide(n):
    els = [
        T("AYRICA KASIM'DA", M, 60, 700, 34, 24, "oswald", RED, fit=False, weight=500, ls=8, nowrap=True),
        T("KADROSUYLA<br>DİKKAT ÇEKENLER", M, 120, W - 2 * M, 260, 100, "anton", INK, nowrap=True, mn=50, lh=1.12),
    ]
    y = 420
    for t, d, yon, kad, src in EXTRA:
        els += [
            img(grade(src, (340, 240)), M, y, 340, 240, z=2),
            box(M, y, 10, 240, RED, z=3),
            T(d, M + 380, y + 4, 560, 36, 24, "oswald", RED, fit=False, weight=600, ls=6, nowrap=True),
            T(t, M + 380, y + 44, 570, 80, 54, "anton", INK, nowrap=True, mn=28, lh=1.1),
            T(f"Yönetmen: {yon}", M + 380, y + 128, 570, 34, 24, "inter", INK, weight=500, nowrap=True, mn=16, op=0.7),
            T(kad, M + 380, y + 164, 570, 76, 26, "inter", INK, weight=600, lh=1.3, mn=18),
        ]
        y += 276
    els.append(T(f"{n-1} / {n}", M, 1284, 200, 30, 20, "oswald", INK, fit=False, weight=500, ls=4, op=0.55))
    return {"bg": TH["bg"], "els": els}


def build():
    n = 8
    slides = [cal_cover()] + [cal_film(i, n) for i in range(5)] + [extra_slide(n)]
    items = [(f[1], f[0].replace("<br>", " ")) for f in FILMS] + [(e[1].split()[0], e[0]) for e in EXTRA]
    items.sort(key=lambda t: int(t[0]))
    rows = []
    y = 480
    for d, t in items:
        rows += [rule(M, y, W - 2 * M, "#fff", op=0.5), T(d + " KASIM", M, y + 14, 300, 52, 42, "anton", "#fff", fit=False, nowrap=True, lh=1.0),
                 T(t, M + 340, y + 20, W - 2 * M - 340, 42, 28, "oswald", "#fff", nowrap=True, mn=16, weight=500, ls=2, upper=True)]
        y += 84
    slides.append({"bg": RED, "els": [
        box(M, 140, 44, 4, "#fff", z=4),
        T("İLK HANGİSİNE<br>GİDECEKSİN?", M, 190, W - 2 * M, 260, 120, "anton", "#fff", nowrap=True, mn=60, lh=1.06),
        *rows, rule(M, y, W - 2 * M, "#fff", op=0.5),
        T("Yorumlara yaz, tarihi takvimine ekle.", M, y + 40, W - 2 * M, 50, 34, "inter", "#fff", weight=500, nowrap=True, mn=20),
        ]})
    return {"id": ID, "caption": CAPTION, "slides": slides}

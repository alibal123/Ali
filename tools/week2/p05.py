from pro import *

ID = "2026-11-02_vizyon_kasim-takvimi"
RED, BLU, INK = "#e23d3d", "#2447ff", "#14110f"
TH = theme("#f4efe6", "#14110f", "#e23d3d", on_acc="#fff", head="anton")

CAPTION = """Kasım'da sinemada ne var? Takvimi tek gönderide topladık.

Şapkalı Kedi 6 Kasım'da, Godzilla Minus Zero ve Ebenezer: Bir Noel Şarkısı 13 Kasım'da, Açlık Oyunları: Hasatta Gündoğumu 20 Kasım'da, Zor Baba 4 ise 27 Kasım'da vizyonda. Tarihler Türkiye vizyon takvimine göre verildi, seans günleri sinemaya göre değişebilir.

Sen ilk hangisine gideceksin?

Bugün 18:00'de: 2026'nın en yüksek puanlı 5 filmi."""


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





FIL = {6: [S("catinhat", 1)], 13: [S("godzilla", 4), S("ebenezer", 3)], 20: [S("hungergames", 1)], 27: [S("focker", 2)]}


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
        T("Hepsi cuma günü. Kaydet, kaçırma.", M, 1236, 800, 36, 26, "inter", INK, weight=500, nowrap=True, op=0.75),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]
    return {"bg": TH["bg"], "els": els}


def cal_film(i, n):
    title, day, yon, kadro, konu, src, _, _c = FILMS[i]
    return {"bg": TH["bg"], "els": [
        img(grade(src, (1080, 600)), 0, 0, W, 600, z=1),
        T(day, M, 600, 300, 300, 270, "anton", RED, fit=False, lh=1.0, bleed=True, z=3),
        T("KASIM", M, 900, 300, 40, 34, "oswald", INK, fit=False, weight=500, ls=8, bleed=True),
        T("CUMA", M, 944, 300, 30, 22, "oswald", INK, fit=False, weight=500, ls=6, op=0.55, bleed=True),
        T(title, 380, 640, W - 380 - M, 150, 70, "anton", INK, nowrap=True, mn=34, lh=1.08),
        T("YÖNETMEN", 380, 820, 300, 24, 20, "oswald", RED, fit=False, weight=500, ls=4),
        T(yon, 380, 850, W - 380 - M, 60, 30, "inter", INK, weight=500, lh=1.3, mn=22),
        T("KADRO", 380, 935, 300, 24, 20, "oswald", RED, fit=False, weight=500, ls=4),
        T(kadro, 380, 965, W - 380 - M, 90, 30, "inter", INK, weight=500, lh=1.3, mn=22),
        T("KONU", 380, 1070, 300, 24, 20, "oswald", RED, fit=False, weight=500, ls=4),
        T(konu, 380, 1100, W - 380 - M, 140, 28, "inter", INK, weight=500, lh=1.3, mn=20),
        *footer(TH, i + 2, n),
    ]}


def build():
    n = 7
    slides = [cal_cover()] + [cal_film(i, n) for i in range(5)]
    rows = []
    y = 500
    for f in FILMS:
        rows += [rule(M, y, W - 2 * M, "#fff", op=0.5), T(f[1] + " KASIM", M, y + 22, 300, 56, 46, "anton", "#fff", fit=False, nowrap=True, lh=1.0),
                 T(f[0].replace("<br>", " "), M + 340, y + 30, W - 2 * M - 340, 44, 30, "oswald", "#fff", nowrap=True, mn=18, weight=500, ls=2, upper=True)]
        y += 96
    slides.append({"bg": RED, "els": [
        box(M, 140, 44, 4, "#fff", z=4),
        T("İLK HANGİSİNE<br>GİDECEKSİN?", M, 190, W - 2 * M, 260, 120, "anton", "#fff", nowrap=True, mn=60, lh=1.06),
        *rows, rule(M, y, W - 2 * M, "#fff", op=0.5),
        T("Yorumlara yaz, tarihi takvimine ekle.", M, y + 40, W - 2 * M, 50, 34, "inter", "#fff", weight=500, nowrap=True, mn=20),
        logo("white", W - M - 58, 1252, 58, z=9)]})
    return {"id": ID, "caption": CAPTION, "slides": slides}

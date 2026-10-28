from pro import *

ID = "2026-11-02_vizyon_kasim-takvimi"
RED, BLU = "#e23d3d", "#2447ff"
TH = theme("#f4efe6", "#14110f", "#e23d3d", on_acc="#fff", head="anton")

CAPTION = """Kasım'da sinemada ne var? Takvimi tek gönderide topladık.

Şapkalı Kedi 6 Kasım'da, Godzilla Minus Zero ve Ebenezer: Bir Noel Şarkısı 13 Kasım'da, Açlık Oyunları: Hasatta Gündoğumu 20 Kasım'da, Zor Baba 4 ise 27 Kasım'da vizyonda. Tarihler Türkiye vizyon takvimine göre verildi, seans günleri sinemaya göre değişebilir.

Sen ilk hangisine gideceksin?

Bugün 18:00'de: Yıllar geçse de güldüren 5 Türk komedisi."""


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




def build():
    n = 7
    cover = cover_mosaic(TH, [f[6] for f in FILMS], "Vizyon takvimi · Kasım 2026", "SİNEMADA<br>BU AY NE VAR?", "6, 13, 20 ve 27 Kasım. Kaydet, kaçırma.")
    slides = [cover]
    for i, f in enumerate(FILMS):
        two = "<br>" in f[0]
        slides.append(info_slide(TH, i + 2, n, f[5], f[0], f[1] + " KASIM", [("Yönetmen", f[2], 66), ("Kadro", f[3], 100), ("Konu", f[4], 150)], title_lines=(2 if two else 1)))
    rows = []
    y = 500
    for f in FILMS:
        rows += [rule(M, y, W - 2 * M, "#fff", op=0.5), T(f[1] + " KASIM", M, y + 22, 300, 56, 46, "anton", "#fff", fit=False, nowrap=True, lh=1.0),
                 T(f[0].replace("<br>", " "), M + 340, y + 30, W - 2 * M - 340, 44, 30, "oswald", "#fff", nowrap=True, mn=18, weight=500, ls=2, upper=True)]
        y += 96
    cta = {"bg": TH["accent"], "els": [
        box(M, 140, 44, 4, "#fff", z=4),
        T("İLK HANGİSİNE<br>GİDECEKSİN?", M, 190, W - 2 * M, 260, 120, "anton", "#fff", nowrap=True, mn=60, lh=1.06),
        *rows,
        rule(M, y, W - 2 * M, "#fff", op=0.5),
        T("Yorumlara yaz, tarihi takvimine ekle.", M, y + 40, W - 2 * M, 50, 34, "inter", "#fff", weight=500, nowrap=True, mn=20),
        logo("white", W - M - 58, 1252, 58, z=9)]}
    slides.append(cta)
    return {"id": ID, "caption": CAPTION, "slides": slides}

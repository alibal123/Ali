from pro import *

ID = "2026-11-02_vizyon_kasim-takvimi"
INK, RED = "#0c0c0f", "#e23d3d"
TH = theme(INK, "#fff", RED, on_acc="#fff", head="anton")
LOGO = dict(pos="tr", w=70, on_light="red", on_dark="white")

CAPTION = """Kasım'da sinemada ne var? Takvimi tek gönderide topladık.

Şapkalı Kedi ve Vahşi At Dokuz 6 Kasım'da, Godzilla Minus Zero ve Ebenezer: Bir Noel Şarkısı 13 Kasım'da, Açlık Oyunları: Hasatta Gündoğumu 20 Kasım'da, Zor Baba 4, Kağıttan Kaplan ve Hexe: Sihir Krallığı ise 27 Kasım'da vizyonda. Tarihler Türkiye vizyon takvimine göre verildi, seans günleri sinemaya göre değişebilir.

Sen ilk hangisine gideceksin?

Bugün 18:00'de: 2026 karne günü, yılın takdir alan filmleri ve Oscar piyasası."""



# (başlık, gün, tür, yönetmen, kadro, konu, kare, renk)
FILMS = [
    ("ŞAPKALI KEDİ", 6, "ANİMASYON · AİLE", "Erica Rivinoja, Alessandro Carloni", "Bill Hader, Xochitl Gomez, Quinta Brunson",
     "Yeni taşındıkları kasabada iki kardeşi neşelendirmekle görevlendirilen Şapkalı Kedi, sihirli şapkasını kaybetme riskiyle karşılaşır.", S("catinhat", 3), "#ff6a5e"),
    ("VAHŞİ AT DOKUZ", 6, "KOMEDİ · GERİLİM", "Martin McDonagh", "John Malkovich, Sam Rockwell, Steve Buscemi",
     "1973 Şili'si: darbeden kısa süre önce iki CIA ajanı, şeflerinin emriyle Paskalya Adası'na gönderilir.", S("wildhorse", 3), "#f2c14e"),
    ("GODZILLA MINUS ZERO", 13, "CANAVAR · AKSİYON", "Takashi Yamazaki", "Ryunosuke Kamiki, Minami Hamabe, Yuki Yamada",
     "Godzilla Minus One'dan iki yıl sonra, 1949'da Shikishima ailesi için yepyeni bir yıkım kapıda.", S("godzilla", 4), "#58c4ff"),
    ("EBENEZER: BİR NOEL ŞARKISI", 13, "FANTEZİ · NOEL", "Ti West", "Johnny Depp, Rupert Grint, Daisy Ridley",
     "Cimri Scrooge, Noel arifesinde hayatını değiştirecek doğaüstü ziyaretçilerle karşılaşır.", S("ebenezer", 3), "#7be0a1"),
    ("AÇLIK OYUNLARI: HASATTA GÜNDOĞUMU", 20, "DİSTOPYA · MACERA", "Francis Lawrence", "Joseph Zada, Ralph Fiennes, Jesse Plemons",
     "Ana seriden 24 yıl öncesine dönüyoruz: 50. Açlık Oyunları'nın kura çekimi.", S("hungergames", 2), "#ff9f43"),
    ("ZOR BABA 4", 27, "KOMEDİ · AİLE", "John Hamburg", "Ben Stiller, Robert De Niro, Ariana Grande, Owen Wilson",
     "Greg ve Pam Focker'ın oğlu Henry, kendisiyle hiç uyuşmayan iradeli bir kadınla evlenmeye karar verince ailede kaos çıkar.", S("focker", 2), "#b78cff"),
    ("KAĞITTAN KAPLAN", 27, "SUÇ · DRAM", "James Gray", "Adam Driver, Miles Teller, Scarlett Johansson",
     "1980'ler Queens'inde iki kardeş, kârlı görünen bir iş yüzünden Rus mafyasına bulaşır. Cannes'da yarıştı.", S("papertiger", 2), "#ff6b9a"),
    ("HEXE: SİHİR KRALLIĞI", 27, "ANİMASYON · FANTEZİ", "Fawn Veerasunthorn, Jason Hand", "Hailee Steinfeld, Rashida Jones (ses)",
     "Sihirli güçlerini yeni keşfeden Billie, cadılar diyarı Hexe'ye uzanan bir yolculuğa çıkar.", S("hexed", 3), "#ffd23f"),
]


def cover():
    els = [
        T("KASIM'DA<br>SİNEMA", M, 50, W - 2 * M, 430, 190, "anton", "#fff", nowrap=True, mn=80, lh=1.14, z=6),
        T("8 FİLM · TÜRKİYE VİZYON TAKVİMİ", M, 492, 800, 28, 22, "oswald", RED, fit=False, weight=600, ls=7, nowrap=True, z=6),
    ]
    tw, th, gap, y0 = 356, 262, 6, 548
    SHORT = ["Şapkalı Kedi", "Vahşi At Dokuz", "Godzilla Minus Zero", "Ebenezer", "Açlık Oyunları", "Zor Baba 4", "Kağıttan Kaplan", "Hexe"]
    for k in range(9):
        c, r = k % 3, k // 3
        x, y = c * (tw + gap), y0 + r * (th + gap)
        if k < 8:
            t, d, tur, yon, kad, konu, src, col = FILMS[k]
            els += [
                img(grade(src, (tw, th), (0.1, 0, 0.9, 1), grain=6), x, y, tw, th, z=2),
                box(x, y + 60, tw, th - 60, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.88))", z=3),
                box(x, y, tw, 6, col, z=4),
                T(f"{d}", x + 20, y + th - 118, 120, 80, 70, "anton", "#fff", fit=False, lh=1.0, bleed=True, nowrap=True, z=5),
                T("KASIM", x + 20 + (70 if d < 10 else 122), y + th - 92, 120, 24, 20, "oswald", col, fit=False, weight=600, ls=5, bleed=True, nowrap=True, z=5),
                T(SHORT[k], x + 20, y + th - 48, tw - 40, 28, 22, "oswald", "#fff", fit=False, weight=500, ls=2, upper=True, nowrap=True, bleed=True, z=5, op=0.85),
            ]
        else:
            els += [box(x, y, tw, th, RED, z=2),
                    T("HEPSİ<br>CUMA", x, y, tw, th, 58, "anton", "#fff", fit=False, align="center", flex="center", lh=1.1, bleed=True, z=5)]
    return {"bg": INK, "els": els}


def film(i, n):
    t, d, tur, yon, kad, konu, src, col = FILMS[i]
    return {"bg": INK, "els": [
        img(grade(src, (1080, 1350), (0, 0, 1, 1), grain=8, contrast=1.08), 0, 0, W, 1350, z=1),
        box(0, 0, W, 1350, "linear-gradient(180deg,rgba(0,0,0,.5) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,.2) 38%,rgba(0,0,0,.93) 58%,rgba(0,0,0,.98) 100%)", z=2),
        label(tur, M, 60, bg=col, color=INK, size=22, z=7),
        T(f"{d}", M, 650, 380, 340, 330, "anton", col, fit=False, lh=1.0, bleed=True, nowrap=True, z=6),
        T("KASIM · CUMA", M + (330 if d < 10 else 400), 700, 330, 30, 24, "oswald", "#fff", fit=False, weight=500, ls=8, nowrap=True, bleed=True, z=6, op=0.8),
        T(t, M + (330 if d < 10 else 400), 744, W - 2 * M - (330 if d < 10 else 400), 230, 66, "anton", "#fff", mn=30, lh=1.12, z=6),
        rule(M, 1010, W - 2 * M, "#fff", op=0.3, h=2),
        T(f"YÖNETMEN  <span style=\"color:#fff;font-family:Inter;letter-spacing:0;font-weight:500;font-size:27px\">{yon}</span>", M, 1030, W - 2 * M, 34, 20, "oswald", col, weight=600, ls=5, nowrap=True, mn=14, z=6),
        T(f"KADRO  <span style=\"color:#fff;font-family:Inter;letter-spacing:0;font-weight:500;font-size:27px\">{kad}</span>", M, 1076, W - 2 * M, 34, 20, "oswald", col, weight=600, ls=5, nowrap=True, mn=14, z=6),
        T(konu, M, 1136, W - 2 * M, 130, 30, "inter", "#fff", weight=400, lh=1.38, mn=22, z=6, op=0.92),
        T(f"{i+2:02d} / {n:02d}", M, 1280, 200, 24, 18, "oswald", "#fff", fit=False, weight=500, ls=5, op=0.55, z=6),
    ]}


def build():
    n = 10
    slides = [cover()] + [film(i, n) for i in range(8)]
    rows = []
    y = 470
    for f in FILMS:
        rows += [rule(M, y, W - 2 * M, "#fff", op=0.45), T(f"{f[1]} KASIM", M, y + 12, 300, 52, 42, "anton", "#fff", fit=False, nowrap=True, lh=1.0),
                 T(f[0], M + 340, y + 18, W - 2 * M - 340, 42, 28, "oswald", "#fff", nowrap=True, mn=16, weight=500, ls=2, upper=True)]
        y += 84
    slides.append({"bg": RED, "els": [
        T("İLK HANGİSİNE<br>GİDECEKSİN?", M, 90, W - 2 * M, 300, 120, "anton", "#fff", nowrap=True, mn=60, lh=1.12),
        *rows, rule(M, y, W - 2 * M, "#fff", op=0.45),
        T("Yorumlara yaz, tarihi takvimine ekle.", M, y + 40, W - 2 * M, 50, 34, "inter", "#fff", weight=500, nowrap=True, mn=20),
    ]})
    return {"id": ID, "caption": CAPTION, "slides": slides}

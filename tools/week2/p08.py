from pro import *

ID = "2026-11-04_vizyon_kadrosuyla-gundem"
BLU = "#1f3bd1"
TH = theme("#f4efe6", "#14110f", BLU, on_acc="#fff", head="anton")

CAPTION = """Kadrosuyla şimdiden gündemde olan 4 yeni film. Büyük bütçeli devlerin arasında kaybolmasın diye bir araya getirdik.

Vahşi At Dokuz 6 Kasım'da geliyor: Martin McDonagh yönetiyor, John Malkovich, Sam Rockwell ve Steve Buscemi oynuyor. Kağıttan Kaplan 27 Kasım'da: James Gray'in filminde Miles Teller, Adam Driver ve Scarlett Johansson var. Aynı gün animasyon Hexe: Sihir Krallığı'nda Hailee Steinfeld, Rashida Jones ve Jodie Foster'ın sesleri duyulacak. Vahşi Gece 2 ise 4 Aralık'ta, David Harbour'lu Noel macerasının devamı olarak geliyor.

Tarihler Türkiye vizyon takvimine göre verildi, seans günleri sinemaya göre değişebilir. Hangisi listene girdi?

Bugün 18:00'de: Kasım akşamlarına battaniye gibi gelen 4 film."""

FILMS = [
    ("VAHŞİ AT DOKUZ", "6 KASIM", [("Yönetmen", "Martin McDonagh", 66), ("Kadro", "John Malkovich, Sam Rockwell, Steve Buscemi, Mariana di Girolamo", 110), ("Tür", "Komedi, suç, gerilim", 66)], S("wildhorse", 3), S("wildhorse", 2), "Wild Horse Nine"),
    ("KAĞITTAN KAPLAN", "27 KASIM", [("Yönetmen", "James Gray", 66), ("Kadro", "Miles Teller, Adam Driver, Scarlett Johansson", 110), ("Tür", "Suç, dram, gerilim", 66)], S("papertiger", 2), S("papertiger", 1), "Paper Tiger"),
    ("HEXE: SİHİR KRALLIĞI", "27 KASIM", [("Yönetmen", "Jason Hand", 66), ("Ses kadrosu", "Hailee Steinfeld, Rashida Jones, Jodie Foster", 110), ("Konu", "Billie, gizli sihirli yeteneklerini keşfeder ve cadıların diyarına yolculuğa çıkar.", 110)], S("hexed", 3), S("hexed", 1), "Hexed"),
    ("VAHŞİ GECE 2", "4 ARALIK", [("Yönetmen", "Tommy Wirkola", 66), ("Kadro", "David Harbour, Kristen Bell, Daniela Melchior, Jared Harris", 110), ("Tür", "Aksiyon, komedi, fantastik", 66)], S("violentnight2", 3), S("violentnight2", 2), "Violent Night 2"),
]



CAST = {
    "VAHŞİ AT DOKUZ": ["John Malkovich", "Sam Rockwell", "Steve Buscemi"],
    "KAĞITTAN KAPLAN": ["Miles Teller", "Adam Driver", "Scarlett Johansson"],
    "HEXE: SİHİR KRALLIĞI": ["Hailee Steinfeld", "Rashida Jones", "Jodie Foster"],
    "VAHŞİ GECE 2": ["David Harbour", "Kristen Bell", "Daniela Melchior"],
}
DIR = {"VAHŞİ AT DOKUZ": "Martin McDonagh", "KAĞITTAN KAPLAN": "James Gray", "HEXE: SİHİR KRALLIĞI": "Jason Hand", "VAHŞİ GECE 2": "Tommy Wirkola"}


def credits(i, n):
    t, d, _rows, src, _c, tag = FILMS[i]
    names = CAST[t]
    ny = 700
    els = [
        img(grade(src, (1080, 1350), grain=9), 0, 0, W, H, z=1),
        box(0, 420, W, 930, "linear-gradient(180deg,rgba(8,10,20,0),rgba(8,10,20,.88) 55%)", z=2),
        box(M, 72, 230, 76, "transparent", z=4, border="3px solid #fff"),
        T(d, M, 72, 230, 76, 30, "anton", "#fff", fit=False, align="center", flex="center", nowrap=True, ls=2, bleed=True, z=5),
        T(tag.upper(), W - M - 400, 96, 400, 30, 22, "oswald", "#fff", fit=False, weight=500, ls=5, align="right", nowrap=True, op=0.85),
        T("<br>".join(x.upper() for x in names), M, ny, W - 2 * M, 230, 46, "oswald", "#fff", weight=500, ls=10, align="center", lh=1.45, nowrap=True, mn=28, op=0.95),
        rule(W // 2 - 60, 965, 120, "#fff", op=0.7, h=3),
        T(t, M, 995, W - 2 * M, 130, 118, "anton", "#fff", nowrap=True, mn=48, lh=1.05, align="center"),
        T("Yönetmen: " + DIR[t], M, 1150, W - 2 * M, 34, 24, "oswald", "#fff", fit=False, weight=500, ls=5, upper=True, align="center", nowrap=True, op=0.8),
        T(f"{i+2:02d} / {n:02d}", M, 1268, 260, 34, 24, "oswald", "#fff", fit=False, weight=500, ls=4, op=0.7),
        logo("white", W - M - 58, 1252, 58, z=9),
    ]
    return {"bg": "#000", "els": els}


def build():
    n = 6
    cover = {"bg": "#000", "els": [
        img(grade(S("hexed", 1), (1080, 1350), (0.22, 0, 0.78, 1), grain=9), 0, 0, W, H, z=1),
        box(0, 380, W, 970, "linear-gradient(180deg,rgba(8,10,20,0),rgba(8,10,20,.9) 60%)", z=2),
        T("YAKINDA · KASIM VE ARALIK", M, 760, W - 2 * M, 34, 26, "oswald", "#fff", fit=False, weight=500, ls=10, align="center", nowrap=True, op=0.9),
        rule(W // 2 - 60, 815, 120, "#fff", op=0.7, h=3),
        T("KADROSUYLA<br>GÜNDEM OLACAK<br>4 FİLM", M, 850, W - 2 * M, 360, 130, "anton", "#fff", nowrap=True, mn=60, lh=1.06, align="center"),
        T("Tarihler Türkiye vizyon takvimine göre.", M, 1224, W - 2 * M, 34, 24, "inter", "#fff", weight=500, align="center", nowrap=True, op=0.8),
        logo("white", W - M - 58, 1252, 58, z=9),
    ]}
    slides = [cover] + [credits(i, n) for i in range(4)]
    slides.append(cta_slide(TH, "HANGİSİ<br>LİSTENE<br>GİRDİ?", "Yorumlara yaz, tarihi takvimine ekle.", "Kaydet · Vizyon gününü kaçırma"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

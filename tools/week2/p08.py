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


def build():
    n = 6
    cover = cover_mosaic(TH, [f[4] for f in FILMS], "Yakında · Kasım ve Aralık", "KADROSUYLA<br>GÜNDEM OLACAK<br>4 FİLM", "Tarihler Türkiye vizyon takvimine göre.")
    slides = [cover]
    for i, f in enumerate(FILMS):
        slides.append(info_slide(TH, i + 2, n, f[3], f[0], f[1], f[2], tag=f[5]))
    slides.append(cta_slide(TH, "HANGİSİ<br>LİSTENE<br>GİRDİ?", "Yorumlara yaz, tarihi takvimine ekle.", "Kaydet · Vizyon gününü kaçırma"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

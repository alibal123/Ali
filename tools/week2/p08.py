from pro import *

ID = "2026-11-04_vizyon_kadrosuyla-gundem"
BLU = "#1f3bd1"
TH = theme("#f4efe6", "#14110f", BLU, on_acc="#fff", head="anton")
LOGO = dict(pos="bc", w=76, on_light="black", on_dark="white")
NAVY, AC = "#0b1020", "#5b7bff"

CAPTION = """Kadrosuyla şimdiden gündemde olan 4 yeni film, bu kez ayrıntılarıyla. Büyük bütçeli devlerin arasında kaybolmasın diye bir araya getirdik.

Vahşi At Dokuz 6 Kasım'da geliyor: Martin McDonagh'ın (The Banshees of Inisherin) bu filmi 1973'te Şili'de, darbeden kısa süre önce geçiyor. John Malkovich ve Sam Rockwell, iki CIA ajanını oynuyor; Steve Buscemi de onların şefi. Kağıttan Kaplan 27 Kasım'da: James Gray'in Cannes'da yarışan filmi, 1980'ler Queens'inde Rus mafyasına bulaşan iki kardeşi anlatıyor; Adam Driver, Miles Teller ve Scarlett Johansson oynuyor. Aynı gün Disney'in 65. animasyonu Hexe: Sihir Krallığı geliyor: sihirli güçlerini yeni keşfeden Billie'nin hikâyesinde Hailee Steinfeld ve Rashida Jones'un sesleri var. Vahşi Gece 2 ise 4 Aralık'ta: David Harbour bu kez yaramaz listeye düşmüş, sihrini kaybetmiş bir Noel Baba'yı oynuyor.

Tarihler Türkiye vizyon takvimine göre verildi, seans günleri sinemaya göre değişebilir. Hangisi listene girdi?

Bugün 18:00'de: Çayı demle, filmi biz seçtik: battaniyeli akşamlar için 4 film."""

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
        T(f"{i*2+2:02d} / {n:02d}", M, 1284, 260, 30, 22, "oswald", "#fff", fit=False, weight=500, ls=4, op=0.7),
    ]
    return {"bg": "#000", "els": els}


INFO = {
    "VAHŞİ AT DOKUZ": (S("wildhorse", 1), [
        ("1973, Şili", "Darbeden kısa süre önce geçiyor; iki CIA ajanı Santiago'dan Paskalya Adası'na gönderilir."),
        ("Banshees yönetmeninden", "Martin McDonagh'ın The Banshees of Inisherin'den sonraki filmi."),
        ("Kadro", "Parker Posey ve Tom Waits da filmde; çekimler Rapa Nui'de ve Santiago'da yapıldı.")]),
    "KAĞITTAN KAPLAN": (S("papertiger", 1), [
        ("Cannes'da yarıştı", "James Gray'in dokuzuncu filmi 2026 Cannes yarışmasında ilk kez gösterildi."),
        ("1980'ler Queens", "Eski polis Gary ile mühendis kardeşi Irwin, Rus mafyasına bulaşır."),
        ("Kadro", "Adam Driver, Miles Teller ve Irwin'in eşi Hester rolünde Scarlett Johansson.")]),
    "HEXE: SİHİR KRALLIĞI": (S("hexed", 4), [
        ("Disney'in 65. animasyonu", "Fawn Veerasunthorn (Wish) ve Jason Hand (Moana 2) yönetiyor."),
        ("Billie'nin sırrı", "Sihirli güçlerini keşfeden genç kız, cadılar diyarı Hexe'ye yolculuğa çıkar."),
        ("Sesler", "Hailee Steinfeld, annesi Alice'te Rashida Jones; Tracey Ullman ve Stephen Fry da var.")]),
    "VAHŞİ GECE 2": (S("violentnight2", 2), [
        ("Noel Baba yaramaz listede", "David Harbour'un Noel Baba'sı bu kez sihrini kaybetmiş durumda."),
        ("Mrs. Claus devrede", "Kristen Bell, işler sarpa sarınca çağrılan yardımcıyı oynuyor."),
        ("İlk film 2022'de", "Yönetmen koltuğunda yine Tommy Wirkola var.")]),
}


def info(i, n):
    t, d, _r, _s, _c, tag = FILMS[i]
    src, facts = INFO[t]
    els = [
        img(grade(src, (1080, 520), grain=7), 0, 0, W, 520, z=1),
        box(0, 0, W, 520, "rgba(11,16,32,.35)", z=2),
        box(0, 300, W, 220, f"linear-gradient(180deg,rgba(11,16,32,0),{NAVY})", z=3),
        box(M, 56, 230, 66, "transparent", z=4, border="3px solid #fff"),
        T(d, M, 56, 230, 66, 28, "anton", "#fff", fit=False, align="center", flex="center", nowrap=True, ls=2, bleed=True, z=5),
        T(t, M, 420, W - 2 * M, 90, 62, "anton", "#fff", nowrap=True, mn=32, lh=1.12, z=6),
        T("NEDEN GÜNDEMDE?", M, 540, W - 2 * M, 30, 22, "oswald", AC, fit=False, weight=500, ls=8, nowrap=True),
    ]
    y = 600
    for k, (h, b) in enumerate(facts):
        els += [
            T(f"{k+1}", M, y - 6, 80, 120, 100, "anton", AC, fit=False, lh=1.0, bleed=True, nowrap=True),
            T(h, M + 100, y, W - 2 * M - 100, 44, 36, "anton", "#fff", nowrap=True, mn=22, lh=1.15),
            T(b, M + 100, y + 52, W - 2 * M - 100, 120, 29, "inter", "#fff", weight=400, lh=1.35, mn=20, op=0.88),
        ]
        y += 212
    els.append(T(f"{i*2+3:02d} / {n:02d}", M, 1284, 260, 30, 22, "oswald", "#fff", fit=False, weight=500, ls=4, op=0.6))
    return {"bg": NAVY, "els": els}


def build():
    n = 10
    cover = {"bg": "#000", "els": [
        img(grade(S("hexed", 1), (1080, 1350), (0.22, 0, 0.78, 1), grain=9), 0, 0, W, H, z=1),
        box(0, 380, W, 970, "linear-gradient(180deg,rgba(8,10,20,0),rgba(8,10,20,.9) 60%)", z=2),
        T("YAKINDA · KASIM VE ARALIK", M, 760, W - 2 * M, 34, 26, "oswald", "#fff", fit=False, weight=500, ls=10, align="center", nowrap=True, op=0.9),
        rule(W // 2 - 60, 815, 120, "#fff", op=0.7, h=3),
        T("KADROSUYLA<br>GÜNDEM OLACAK<br>4 FİLM", M, 850, W - 2 * M, 360, 130, "anton", "#fff", nowrap=True, mn=60, lh=1.06, align="center"),
        T("Kimi, nerede, neden? Ayrıntılı rehber.", M, 1170, W - 2 * M, 34, 24, "inter", "#fff", weight=500, align="center", nowrap=True, op=0.8),
    ]}
    slides = [cover]
    for i in range(4):
        slides += [credits(i, n), info(i, n)]
    slides.append(cta_slide(TH, "HANGİSİ<br>LİSTENE<br>GİRDİ?", "Yorumlara yaz, tarihi takvimine ekle.", "Kaydet · Vizyon gününü kaçırma"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

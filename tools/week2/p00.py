from pro import *

ID = "2026-10-29_liste_hayati-sorgulatan-4-film"
PAPER, INK, GRN, CLAY = "#efe7d6", "#1f2a24", "#2f5d46", "#b5532f"
TH = theme(PAPER, INK, GRN, on_acc="#fff", head="serif", accent_txt=GRN, upper=False)

CAPTION = """Yavaş ama derin. Telefonu bırakıp bir akşamını verebileceğin, bittiğinde "ben ne yapıyorum ya" dedirten 4 sakin film.

The Tree of Life (2011) bir ailenin hikâyesini evrenin yaratılışıyla yan yana koyuyor ve Cannes'da Altın Palmiye aldı. Wild Strawberries (1957) yaşlı bir profesörün geçmişine yaptığı yolculuğu Bergman'ın kaleminden anlatıyor. Perfect Days (2023) Tokyo'da tuvaletleri temizleyen bir adamın sakin günlerini izliyor, Koji Yakusho bu rolle Cannes'da En İyi Erkek Oyuncu seçildi. Paterson (2016) şiir yazan bir otobüs şoförünün haftasını anlatıyor.

Bu hafta bir akşamını bunlardan birine ayır. Sen hangisinden sonra hayatına dair bir şeyi değiştirdin?

Cumhuriyet Bayramımız kutlu olsun.

Yarın 18:00'de: Bitince "şimdi başa saralım" dedirten 5 film."""

FILMS = [
    ("THE TREE OF LIFE", "2011 · Terrence Malick", "Bir ailenin hikâyesi, evrenin yaratılışıyla yan yana anlatılır. Cannes'da Altın Palmiye kazandı.", "n_treeoflife_3", "Ne kadar küçük, ne kadar büyüğüz?"),
    ("WILD STRAWBERRIES", "1957 · Ingmar Bergman", "Yaşlı bir profesör, onur ödülüne giderken geçmişinin içinden de geçer.", "n_wildstraw_3", "Geriye bakınca ne görürsün?"),
    ("PERFECT DAYS", "2023 · Wim Wenders", "Tokyo'da tuvalet temizleyen bir adamın sakin günleri. Koji Yakusho, Cannes'da En İyi Erkek Oyuncu seçildi.", "n_perfectdays_4", "Küçük ritüeller yeter mi?"),
    ("PATERSON", "2016 · Jim Jarmusch", "Şiir yazan bir otobüs şoförünün sıradan bir haftası.", "n_paterson_1", "Sıradan günde şiir var mı?"),
]
COVER = ["n_treeoflife_2", "n_wildstraw_2", "n_perfectdays_2", "n_paterson_6"]


def film(i, n):
    t, meta, body, src, q = FILMS[i]
    return {"bg": PAPER, "els": [
        img(grade(src, (W, 720), (0, 0, 1, 1)), 0, 0, W, 720, z=2),
        box(0, 720, W, 10, GRN, z=3),
        T(f"{i+1}", M, 764, 140, 150, 130, "serif", CLAY, fit=False, lh=1.0, nowrap=True, weight=700),
        T(t.title().replace(" Of "," of "), 200, 770, W - 200 - M, 100, 76, "serif", INK, nowrap=True, mn=40, lh=1.1, weight=700),
        T(meta, 204, 876, W - 204 - M, 32, 24, "oswald", GRN, weight=500, ls=4, upper=True, nowrap=True, mn=16),
        T(body, M, 940, W - 2 * M, 130, 34, "inter", INK, weight=500, lh=1.38, mn=24),
        box(M, 1112, W - 2 * M, 2, INK, z=3, op=0.25),
        T(f"“{q}”", M, 1130, W - 2 * M, 80, 44, "caveat", CLAY, weight=700, nowrap=True, mn=26),
        T(f"{i+1} / 6", M, 1268, 200, 34, 22, "oswald", INK, fit=False, weight=500, ls=4, op=0.6),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]}


def build():
    n = 6
    cw = W // 4
    strips = [img(grade(s, (cw, 1350), (0.2, 0, 0.8, 1)), k * cw, 0, cw, 1350, z=2) for k, s in enumerate(COVER)]
    cover = {"bg": INK, "els": [
        *strips,
        box(0, 0, W, 1350, INK, z=3, op=0.38),
        box(0, 700, W, 650, "linear-gradient(180deg,rgba(31,42,36,0),rgba(31,42,36,.92))", z=3),
        T("YAVAŞ<br>AMA DERİN", M, 640, W - 2 * M, 440, 190, "serif", "#fff", nowrap=True, mn=70, lh=1.05, weight=700, z=6),
        T("Hayatı yeniden düşündüren 4 sakin film", M, 1120, W - 2 * M, 50, 38, "caveat", "#f2d9a0", weight=700, nowrap=True, mn=24, z=6),
        T("TELEFONU BIRAK, BİR AKŞAMINI VER", M, 1200, W - 2 * M - 100, 34, 22, "oswald", "#fff", weight=500, ls=5, nowrap=True, mn=14, z=6, op=0.85),
        logo("white", W - M - 58, 1252, 58, z=9),
    ]}
    slides = [cover] + [film(i, n) for i in range(4)]
    slides.append(cta_slide(TH, "Hangisinden sonra<br>hayatında bir şey<br>değişti?", "Yorumlara yaz.", "29 Ekim · Cumhuriyet Bayramımız kutlu olsun"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

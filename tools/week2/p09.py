from pro import *

ID = "2026-11-04_liste_battaniye-filmleri"
TH = theme("#fbeee0", "#3b2418", "#c4552d", on_acc="#fbeee0", head="serif", upper=False, acc_logo="white")

CAPTION = """Kasım akşamlarına battaniye gibi gelen 4 film. Gürültü yok, yıkım yok; sadece çayın yanına yakışan sıcacık hikâyeler.

About Time (2013) ailesindeki erkeklerin zamanda geriye gidebildiğini öğrenen bir gencin aşk ve aile hikâyesini, Paddington 2 (2017) hapse düşen sevimli ayının macerasını, Chef (2014) işinden ayrılıp yemek kamyonuyla yola çıkan bir şefi, Little Women (2019) March kardeşlerin büyüme hikâyesini anlatıyor. Little Women, En İyi Kostüm Tasarımı dalında Oscar aldı.

Bu akşam hangisini açıyorsun?

Yarın 18:00'de: Tek odada geçen ama nefesini kesen 5 film."""

FILMS = [
    ("About Time", "2013 · Richard Curtis", "Ailesindeki erkeklerin zamanda geriye gidebildiğini öğrenen genç bir adam, bu gücü aşk için kullanır. Domhnall Gleeson ve Rachel McAdams oynuyor.", S("abouttime", 1), S("abouttime", 4), "Çay hazırla"),
    ("Paddington 2", "2017 · Paul King", "Peru'dan gelen ayı Paddington, bir hırsızlık suçlamasıyla hapse düşer. Hugh Grant'in canlandırdığı kötü adam filme ayrı bir keyif katar.", S("paddington2", 1), S("paddington2", 2), "Aileyle izle"),
    ("Chef", "2014 · Jon Favreau", "İşinden ayrılan şef, bir yemek kamyonuyla ülkeyi dolaşarak yemek yapma sevgisini yeniden bulur.", S("chef", 1), S("chef", 3), "Aç gitme"),
    ("Little Women", "2019 · Greta Gerwig", "March kardeşlerin büyüme hikâyesi. Saoirse Ronan, Florence Pugh, Emma Watson ve Eliza Scanlen oynuyor; Oscar'ı En İyi Kostüm Tasarımı dalında aldı.", S("littlewomen", 1), S("littlewomen", 2), "Battaniyeye sarıl"),
]




TIMES = [("18:30", "Çay vakti"), ("20:00", "Aile saati"), ("21:30", "Akşam yemeği"), ("23:00", "Battaniye saati")]


def warm(src, crop=(0, 0, 1, 1)):
    return [img(grade(src, (1080, 1350), crop, grain=8), 0, 0, W, H, z=1),
            box(0, 0, W, H, "rgba(255,150,60,.20)", z=2, blend="multiply"),
            box(0, 0, W, H, "linear-gradient(180deg,rgba(40,16,4,.35),rgba(40,16,4,0) 35%)", z=2)]


def eve_film(i, n):
    title, meta, body, src, _, tag = FILMS[i]
    t, lab = TIMES[i]
    return {"bg": "#2a1208", "els": [
        *warm(src),
        T(t, M, 70, 600, 240, 210, "serif", "#fff", fit=False, lh=1.0, bleed=True, nowrap=True),
        T(lab.upper(), M + 6, 318, 600, 34, 26, "oswald", "#fff", fit=False, weight=500, ls=8, nowrap=True),
        logo("white", W - M - 58, 64, 58, z=9),
        box(56, 810, 968, 430, "#fbeee0", z=4, radius=26),
        T(title, 96, 846, 888, 100, 80, "serif", TH["ink"], nowrap=True, mn=40, lh=1.05),
        T(meta, 96, 958, 888, 32, 24, "oswald", TH["accent"], weight=500, ls=4, upper=True, nowrap=True, mn=16),
        T(body, 96, 1010, 888, 190, 34, "inter", TH["ink"], weight=500, lh=1.4, mn=24),
        T(f"{i+1:02d} / 04", 96, 1272, 200, 30, 22, "oswald", "#fff", fit=False, weight=500, ls=4, op=0.8),
    ]}


def build():
    n = 6
    cover = {"bg": "#2a1208", "els": [
        *warm(FILMS[3][4]),
        T("KASIM AKŞAMI PROGRAMI", M, 76, 800, 36, 26, "oswald", "#fff", fit=False, weight=500, ls=8, nowrap=True),
        logo("white", W - M - 58, 64, 58, z=9),
        box(56, 560, 968, 690, "#fbeee0", z=4, radius=26),
        T("Kasım akşamlarına<br>battaniye gibi<br>gelen 4 film", 96, 596, 888, 280, 84, "serif", TH["ink"], nowrap=True, mn=44, lh=1.1),
    ]}
    rows = []
    y = 930
    for (t, lab), f in zip(TIMES, FILMS):
        rows += [rule(96, y, 888, TH["ink"], op=0.15), T(t, 96, y + 12, 120, 40, 30, "oswald", TH["accent_txt"], fit=False, weight=500, ls=2, nowrap=True),
                 T(f[0], 230, y + 8, 520, 44, 32, "inter", TH["ink"], weight=600, nowrap=True, mn=18),
                 T(lab.upper(), 700, y + 16, 284, 30, 20, "oswald", TH["ink"], weight=500, ls=3, nowrap=True, align="right", mn=12, op=0.55)]
        y += 70
    cover["els"] += rows
    slides = [cover] + [eve_film(i, n) for i in range(4)]
    slides.append(cta_slide(TH, "Bu akşam<br>hangisini<br>açıyorsun?", "Yorumlara yaz, çayını da söyle.", "Kaydet · Sıcak tut"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

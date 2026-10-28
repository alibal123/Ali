from pro import *
import cut

ID = "2026-11-04_liste_battaniye-filmleri"
CRM, INK = "#f4ede2", "#2a2420"
MUS, SAGE, ROSE, SKY = "#f2b84b", "#9dbfa5", "#e9a7a0", "#9fc3e6"
TH = theme(CRM, INK, MUS, on_acc=INK, head="anton", acc_logo="black")

CAPTION = """Dışarısı Kasım, içerisi sinema. Battaniyeye sarılıp çayı demleyince açılacak 4 film: gürültü yok, yıkım yok, sadece sıcacık hikâyeler.

About Time (2013) ailesindeki erkeklerin zamanda geriye gidebildiğini öğrenen bir gencin aşk ve aile hikâyesini, Paddington 2 (2017) hapse düşen sevimli ayının macerasını, Chef (2014) işinden ayrılıp yemek kamyonuyla yola çıkan bir şefi, Little Women (2019) March kardeşlerin büyüme hikâyesini anlatıyor. Little Women, En İyi Kostüm Tasarımı dalında Oscar aldı.

Bu akşam hangisini açıyorsun?

Yarın 18:00'de: Tek odada geçen ama nefesini kesen 5 film."""



FILMS = [
    ("ABOUT TIME", "2013 · Richard Curtis", "Ailesindeki erkeklerin zamanda geriye gidebildiğini öğrenen genç bir adam, bu gücü aşk için kullanır. Domhnall Gleeson ve Rachel McAdams oynuyor.", "abouttime_1", MUS, "Zamanı geri sarmak isteyenler için"),
    ("PADDINGTON 2", "2017 · Paul King", "Peru'dan gelen ayı Paddington, bir hırsızlık suçlamasıyla hapse düşer. Hugh Grant'in canlandırdığı kötü adam filme ayrı bir keyif katar.", "paddington2_2", SKY, "İyiliğe inanmak için"),
    ("CHEF", "2014 · Jon Favreau", "İşinden ayrılan şef, bir yemek kamyonuyla ülkeyi dolaşarak yemek yapma sevgisini yeniden bulur.", "chef_3", ROSE, "Karnı acıkanlar için"),
    ("LITTLE WOMEN", "2019 · Greta Gerwig", "March kardeşlerin büyüme hikâyesi. Saoirse Ronan, Florence Pugh, Emma Watson ve Eliza Scanlen oynuyor; Oscar'ı En İyi Kostüm Tasarımı dalında aldı.", "littlewomen_1", SAGE, "Battaniyeye kıvrılanlar için"),
]


def figure_el(name, cx, bottom, max_w, max_h, z=6):
    p, w, h = cut.figure(name, max_w, max_h, contrast=1.04, sat=1.05)
    return img(p, cx - w // 2, bottom - h, w, h, z=z, fit="contain"), h


def mood_film(i, n):
    title, meta, body, src, col, mood = FILMS[i]
    fe, fh = figure_el(src, 540, 930, 700, 600)
    ty = max(250, 930 - fh - 160)
    return {"bg": CRM, "els": [
        T(f"{i+1:02d}", M, 64, 200, 56, 40, "anton", INK, fit=False, lh=1.0, nowrap=True),
        T("KASIM AKŞAMI MODU", W - M - 520, 78, 520, 34, 22, "oswald", INK, fit=False, weight=500, ls=6, align="right", nowrap=True, op=0.6),
        box(140, 150, 800, 800, col, z=2, radius=900),
        T(mood.upper(), M, ty - 70, W - 2 * M, 34, 24, "oswald", INK, weight=500, ls=6, nowrap=True, mn=14, align="center", z=4, op=0.75),
        T(title, M, ty, W - 2 * M, 230, 200, "anton", INK, nowrap=True, mn=70, lh=1.0, align="center", z=4),
        fe,
        box(0, 900, W, 450, CRM, z=7),
        T(meta, M, 940, W - 2 * M, 30, 24, "oswald", INK, weight=500, ls=5, upper=True, nowrap=True, mn=16, align="center", op=0.6, z=8),
        T(body, 110, 992, W - 220, 200, 36, "inter", INK, weight=500, lh=1.42, mn=26, align="center", z=8),
        T(f"{i+1:02d} / 06", M, 1268, 260, 34, 24, "oswald", INK, fit=False, weight=500, ls=4, op=0.6, z=8),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]}


def build():
    n = 6
    els = [
        *kicker(TH, "4 film · battaniye · çay", M, 66, color=INK, w=900),
        T("DIŞARISI KASIM,<br>İÇERİSİ SİNEMA", M, 130, W - 2 * M, 330, 140, "anton", INK, nowrap=True, mn=60, lh=1.1),
    ]
    for k, f in enumerate(FILMS):
        x = 72 + k * 229
        els.append(box(x, 580, 260, 260, f[4], z=2, radius=400))
        fe, _h = figure_el(f[3] if f[3] != "littlewomen_1" else "littlewomen_2", x + 130, 850, 290, 520, z=4)
        els.append(fe)
    els += [
        box(0, 840, W, 510, CRM, z=5),
        T("Battaniyeye sarıl, çayı demle, birini aç.", M, 940, W - 2 * M, 50, 38, "inter", INK, weight=500, nowrap=True, mn=22, z=6),
        T("ABOUT TIME · PADDINGTON 2 · CHEF · LITTLE WOMEN", M, 1010, W - 2 * M, 32, 22, "oswald", INK, weight=500, ls=4, nowrap=True, mn=12, z=6, op=0.6),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]
    cover = {"bg": CRM, "els": els}
    slides = [cover] + [mood_film(i, n) for i in range(4)]
    slides.append(cta_slide(TH, "BU AKŞAM<br>HANGİSİNİ<br>AÇIYORSUN?", "Yorumlara yaz, çayını da söyle.", "Kaydet · Sıcak tut"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

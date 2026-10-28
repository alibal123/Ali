from pro import *
import cut

ID = "2026-11-04_liste_battaniye-filmleri"
TERRA, CREAM, GOLD = "#b04a2b", "#fbeee0", "#f2c46d"
TH = theme(TERRA, CREAM, GOLD, on_acc=TERRA, head="serif", upper=False, logo_light="white")

CAPTION = """Dışarısı Kasım, içerisi sinema. Battaniyeye sarılıp çayı demleyince açılacak 4 film: gürültü yok, yıkım yok, sadece sıcacık hikâyeler.

About Time (2013) ailesindeki erkeklerin zamanda geriye gidebildiğini öğrenen bir gencin aşk ve aile hikâyesini, Paddington 2 (2017) hapse düşen sevimli ayının macerasını, Chef (2014) işinden ayrılıp yemek kamyonuyla yola çıkan bir şefi, Little Women (2019) March kardeşlerin büyüme hikâyesini anlatıyor. Little Women, En İyi Kostüm Tasarımı dalında Oscar aldı.

Bu akşam hangisini açıyorsun?

Yarın 18:00'de: Tek odada geçen ama nefesini kesen 5 film."""


FILMS = [
    ("About Time", "2013 · Richard Curtis", "Ailesindeki erkeklerin zamanda geriye gidebildiğini öğrenen genç bir adam, bu gücü aşk için kullanır. Domhnall Gleeson ve Rachel McAdams oynuyor.", "abouttime_1"),
    ("Paddington 2", "2017 · Paul King", "Peru'dan gelen ayı Paddington, bir hırsızlık suçlamasıyla hapse düşer. Hugh Grant'in canlandırdığı kötü adam filme ayrı bir keyif katar.", "paddington2_2"),
    ("Chef", "2014 · Jon Favreau", "İşinden ayrılan şef, bir yemek kamyonuyla ülkeyi dolaşarak yemek yapma sevgisini yeniden bulur.", "chef_3"),
    ("Little Women", "2019 · Greta Gerwig", "March kardeşlerin büyüme hikâyesi. Saoirse Ronan, Florence Pugh, Emma Watson ve Eliza Scanlen oynuyor; Oscar'ı En İyi Kostüm Tasarımı dalında aldı.", "littlewomen_1"),
]


def framed(name, fx, fy, fw, fh, ext=0.14):
    d = cut.pop_frame(name, fw, fh, ext=ext)
    return [box(fx - 16, fy - 16, fw + 32, fh + 32, "transparent", z=2, border=f"4px solid {GOLD}"),
            img(d["frame"], fx, fy, fw, fh, z=3),
            img(d["pop"], fx, fy - d["pop_dy"], fw, d["pop_h"], z=5, fit="contain")]


def cozy_film(i, n):
    title, meta, body, src = FILMS[i]
    return {"bg": TERRA, "els": [
        T(f"<i>{i+1}. {title}</i>", M, 96, W - 2 * M, 150, 104, "playfair", CREAM, weight=700, nowrap=True, mn=50, lh=1.1, align="center"),
        *framed(src, 130, 350, 820, 540),
        T(body, 130, 950, 820, 190, 36, "playfair", CREAM, weight=400, lh=1.45, mn=26, align="center"),
        T(meta, 130, 1170, 820, 34, 24, "oswald", GOLD, weight=500, ls=5, upper=True, nowrap=True, mn=16, align="center"),
        T(f"{i+1:02d} / 06", M, 1268, 260, 34, 24, "oswald", CREAM, fit=False, weight=500, ls=4, op=0.7),
        logo("white", W - M - 58, 1252, 58, z=9),
    ]}


def build():
    n = 6
    cover = {"bg": TERRA, "els": [
        *kicker(TH, "4 film · battaniye, çay, huzur", M, 70, color=GOLD, w=900),
        T("<i>Dışarısı Kasım,<br>içerisi sinema</i>", M, 130, W - 2 * M, 330, 118, "playfair", CREAM, weight=700, nowrap=True, mn=54, lh=1.12),
        *framed("littlewomen_2", 130, 560, 820, 520, ext=0.12),
        T("Battaniyeye sarıl, çayı demle, birini aç.", M, 1150, W - 2 * M - 80, 40, 30, "playfair", CREAM, nowrap=True, mn=20, align="left"),
        logo("white", W - M - 58, 1252, 58, z=9),
    ]}
    cta = {"bg": CREAM, "els": [
        box(M, 150, 44, 4, TERRA, z=4),
        T("<i>Bu akşam<br>hangisini<br>açıyorsun?</i>", M, 200, W - 2 * M, 560, 150, "playfair", TERRA, weight=700, nowrap=True, mn=60, lh=1.12),
        T("Yorumlara yaz, çayını da söyle.", M, 900, W - 2 * M, 80, 46, "playfair", TERRA, weight=400, nowrap=True, mn=24),
        T("KAYDET · SICAK TUT", M, 1050, 440, 56, 26, "oswald", CREAM, fit=False, weight=500, ls=4, nowrap=True, bg=TERRA, pad="12px 22px"),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]}
    return {"id": ID, "caption": CAPTION, "slides": [cover] + [cozy_film(i, n) for i in range(4)] + [cta]}

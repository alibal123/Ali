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



def mag_film(i, n):
    title, meta, body, src, _, tag = FILMS[i]
    return {"bg": TH["bg"], "els": [
        T(f"{i+1:02d}", M, 72, 300, 130, 120, "serif", TH["accent"], fit=False, lh=1.0, bleed=True),
        T(title, M, 230, 420, 330, 74, "serif", TH["ink"], mn=36, lh=1.08),
        rule(M, 590, 80, TH["accent"], op=1, h=4),
        T(meta, M, 620, 400, 60, 22, "oswald", TH["accent"], weight=500, ls=3, upper=True, lh=1.4, mn=16),
        T(body, M, 700, 400, 460, 32, "inter", TH["ink"], weight=500, lh=1.45, mn=22),
        img(grade(src, (500, 1000), (0.28, 0, 0.72, 1)), 508, 72, 500, 1000, z=2),
        T(tag, 508, 1100, 500, 40, 24, "oswald", TH["ink"], fit=False, weight=500, ls=5, upper=True, op=0.6, align="right", nowrap=True),
        *footer(TH, i + 1, n),
    ]}


def build():
    n = 6
    cover = {"bg": TH["bg"], "els": [
        box(40, 40, 1000, 1270, "transparent", z=1, border=f"2px solid {TH['ink']}", css="opacity:.35"),
        img(grade(FILMS[3][4], (904, 700), (0, 0, 1, 1)), 88, 88, 904, 700, z=2),
        T("Kasım akşamlarına<br>battaniye gibi<br>gelen 4 film", M + 16, 830, W - 2 * M - 32, 330, 86, "serif", TH["ink"], nowrap=True, mn=44, lh=1.1, align="center"),
        T("LİSTE · 4 FİLM · KAYDET", M, 1180, W - 2 * M, 34, 24, "oswald", TH["accent"], fit=False, weight=500, ls=6, align="center", nowrap=True),
        logo("black", W // 2 - 29, 1240, 58, z=9),
    ]}
    slides = [cover] + [mag_film(i, n) for i in range(4)]
    slides.append(cta_slide(TH, "Bu akşam<br>hangisini<br>açıyorsun?", "Yorumlara yaz, çayını da söyle.", "Kaydet · Sıcak tut"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

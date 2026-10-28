from pro import *
import cut

ID = "2026-11-04_liste_battaniye-filmleri"
CRM, INK = "#f4ede2", "#2a2420"
MUS, SAGE, ROSE, SKY = "#f2c24f", "#a8c4ab", "#f0a9a0", "#a9c8e8"
TH = theme(CRM, INK, MUS, on_acc=INK, head="anton", acc_logo="black")

CAPTION = """Çayı demle, filmi biz seçtik. Battaniyeye sarılıp çayı demleyince açılacak 4 film: gürültü yok, yıkım yok, sadece sıcacık hikâyeler.

About Time (2013) ailesindeki erkeklerin zamanda geriye gidebildiğini öğrenen bir gencin aşk ve aile hikâyesini, Paddington 2 (2017) hapse düşen sevimli ayının macerasını, Chef (2014) işinden ayrılıp yemek kamyonuyla yola çıkan bir şefi, Little Women (2019) March kardeşlerin büyüme hikâyesini anlatıyor. Little Women, En İyi Kostüm Tasarımı dalında Oscar aldı.

Bu akşam hangisini açıyorsun?

Yarın 18:00'de: Tek odada geçen ama nefesini kesen 5 film."""



FILMS = [
    ("ABOUT TIME", "2013 · Richard Curtis", "Ailesindeki erkeklerin zamanda geriye gidebildiğini öğrenen genç bir adam, bu gücü aşk için kullanır. Domhnall Gleeson ve Rachel McAdams oynuyor.", "abouttime_2", SKY, "Zamanı geri sarmak isteyenler için"),
    ("PADDINGTON 2", "2017 · Paul King", "Peru'dan gelen ayı Paddington, bir hırsızlık suçlamasıyla hapse düşer. Hugh Grant'in canlandırdığı kötü adam filme ayrı bir keyif katar.", "paddington2_2", MUS, "İyiliğe inanmak için"),
    ("CHEF", "2014 · Jon Favreau", "İşinden ayrılan şef, bir yemek kamyonuyla ülkeyi dolaşarak yemek yapma sevgisini yeniden bulur.", "chef_3", ROSE, "Karnı acıkanlar için"),
    ("LITTLE WOMEN", "2019 · Greta Gerwig", "March kardeşlerin büyüme hikâyesi. Saoirse Ronan, Florence Pugh, Emma Watson ve Eliza Scanlen oynuyor; Oscar'ı En İyi Kostüm Tasarımı dalında aldı.", "littlewomen_2", SAGE, "Battaniyeye kıvrılanlar için"),
]


def circ_figure(name, cx, cy, D, col, over=60, z_circle=2, z_fig=6, wide=1.1):
    p, fx, fy, w, h = cut.figure_in_circle(name, cx, cy, D, over=over, wide=wide)
    return [box(cx - D // 2, cy - D // 2, D, D, col, z=z_circle, radius=D),
            img(p, fx, fy, w, h, z=z_fig, fit="contain")], fy


def mood_film(i, n):
    title, meta, body, src, col, mood = FILMS[i]
    D, cy = 660, 730
    els, fy = circ_figure(src, 540, cy, D, col, over=70)
    ty = 170
    return {"bg": CRM, "els": [
        T(f"{i+1:02d}", M, 64, 200, 56, 40, "anton", INK, fit=False, lh=1.0, nowrap=True),
        T("KASIM AKŞAMI MODU", W - M - 520, 78, 520, 34, 22, "oswald", INK, fit=False, weight=500, ls=6, align="right", nowrap=True, op=0.6),
        T(mood.upper(), M, 120, W - 2 * M, 34, 24, "oswald", INK, weight=500, ls=6, nowrap=True, mn=14, align="center", z=4, op=0.75),
        T(title, M, ty, W - 2 * M, 230, 190, "anton", INK, nowrap=True, mn=70, lh=1.0, align="center", z=4),
        *els,
        T(meta, M, 1088, W - 2 * M, 30, 24, "oswald", INK, weight=500, ls=5, upper=True, nowrap=True, mn=16, align="center", op=0.6, z=8),
        T(body, 110, 1128, W - 220, 130, 32, "inter", INK, weight=500, lh=1.4, mn=24, align="center", z=8),
        T(f"{i+1:02d} / 06", M, 1268, 260, 34, 24, "oswald", INK, fit=False, weight=500, ls=4, op=0.6, z=8),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]}


def build():
    n = 6
    els = [
        *kicker(TH, "4 film · battaniye · çay", M, 66, color=INK, w=900),
        T("ÇAYI DEMLE,<br>FİLMİ BİZ<br>SEÇTİK", M, 130, W - 2 * M, 330, 140, "anton", INK, nowrap=True, mn=60, lh=1.2),
    ]
    cover_names = ["abouttime_3", "paddington2_2", "chef_3", "littlewomen_1"]
    D = 320
    for k, (f, nm) in enumerate(zip(FILMS, cover_names)):
        cx = 300 + (k % 2) * 480
        cy = 680 + (k // 2) * 360
        e, _fy = circ_figure(nm, cx, cy, D, f[4], over=34, wide=1.08)
        els += e
    els += [
        T("Battaniyeye sarıl, çayı demle, birini aç.", M, 1252, W - 2 * M - 100, 40, 28, "inter", INK, weight=500, nowrap=True, mn=18, z=6),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]
    cover = {"bg": CRM, "els": els}
    slides = [cover] + [mood_film(i, n) for i in range(4)]
    slides.append(cta_slide(TH, "BU AKŞAM<br>HANGİSİNİ<br>AÇIYORSUN?", "Yorumlara yaz, çayını da söyle.", "Kaydet · Sıcak tut"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

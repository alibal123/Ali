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


def build():
    n = 6
    cover = cover_mosaic(TH, [f[4] for f in FILMS], "Liste · 4 film", "Kasım akşamlarına<br>battaniye gibi<br>gelen 4 film", "Kaydet, bu akşam aç.")
    slides = [cover] + [film_slide(TH, i + 1, n, f[3], f[0], f[1], f[2], tag=f[5]) for i, f in enumerate(FILMS)]
    slides.append(cta_slide(TH, "Bu akşam<br>hangisini<br>açıyorsun?", "Yorumlara yaz, çayını da söyle.", "Kaydet · Sıcak tut"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

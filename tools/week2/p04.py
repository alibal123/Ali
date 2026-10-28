from pro import *

ID = "2026-11-01_eslestirme_bunu-sevdiysen"
TH = theme("#f4efe6", "#14110f", "#ff4f7b", on_acc="#fff", head="anton")

CAPTION = """Bunu sevdiysen şunu izle: aynı tadı veren 4 film çifti.

Inception'ı sevdiysen Paprika'ya, Forrest Gump'ı sevdiysen Big Fish'e, Knives Out'u sevdiysen Gosford Park'a, Parasite'i sevdiysen Shoplifters'a bak. Son çiftin ikisi de Cannes'da Altın Palmiye aldı: Shoplifters 2018'de, Parasite 2019'da.

Sen hangi eşleşmeyi eklerdin? "X sevdiysen Y" diye yorumlara yaz.

Yarın 13:00'te: Kasım ayında sinemaya gelecek 5 film."""


PAIRS = [
    # A: başlık, meta, slayt karesi, kapak karesi | B: ... | sebep, etiket
    (("INCEPTION", "2010 · Christopher Nolan", S("inception", 2), S("inception", 1)),
     ("PAPRIKA", "2006 · Satoshi Kon", S("paprika", 2), S("paprika", 1)),
     "Rüyaların içine girmeyi sevdiysen: Paprika'da terapistlerin hastalarının rüyalarına girmesini sağlayan bir makine çalınıyor.", "#ffd9c7"),
    (("FORREST GUMP", "1994 · Robert Zemeckis", S("forrestgump", 3), S("forrestgump", 1)),
     ("BIG FISH", "2003 · Tim Burton", S("bigfish", 3), S("bigfish", 1)),
     "Hayatı masal gibi anlatan adamları sevdiysen: Big Fish'te ölüm döşeğindeki babanın hikâyelerinin ardındaki gerçeği arayan bir oğul var.", "#cfe8ff"),
    (("KNIVES OUT", "2019 · Rian Johnson", S("knivesout", 1), S("knivesout", 2)),
     ("GOSFORD PARK", "2001 · Robert Altman", S("gosford", 3), S("gosford", 2)),
     "Bir malikane, bir cinayet, herkes şüpheli: Gosford Park 1932'de geçen, kalabalık kadrolu bir polisiye.", "#e5d6ff"),
    (("PARASITE", "2019 · Bong Joon-ho", S("parasite", 2), S("parasite", 1)),
     ("SHOPLIFTERS", "2018 · Hirokazu Kore-eda", S("shoplifters", 2), S("shoplifters", 1)),
     "Sınıf farkını incelikle anlatan iki film: ikisi de Cannes'da Altın Palmiye aldı. Shoplifters, geçimini hırsızlıkla sağlayan bir ailenin hikâyesi.", "#cdf5dc"),
]




def build():
    n = 6
    photos = [p[0][3] for p in PAIRS] + [p[1][3] for p in PAIRS]
    cover = cover_mosaic(TH, photos, "Dört eşleşme", "BUNU SEVDİYSEN,<br>BUNU İZLE", "Üstteki sevdiğin, alttaki izleyeceğin film.")
    slides = [cover]
    for i, (a, b, why, _) in enumerate(PAIRS):
        slides.append(pair_slide(TH, i + 2, n, (a[0], a[1], a[2]), (b[0], b[1], b[2]), why))
    slides.append(cta_slide(TH, "SEN HANGİ<br>EŞLEŞMEYİ<br>EKLERDİN?", "\"X sevdiysen Y izle\" diye yorumlara yaz.", "Kaydet · Arkadaşına gönder"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

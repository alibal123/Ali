from pro import *

ID = "2026-11-02_liste_turk-komedileri"
RED, TEL, GLD = "#a8321f", "#1f5c57", "#e0a526"
TH = theme("#f1e3c4", "#2a1a10", "#a8321f", on_acc="#f1e3c4", head="abril", upper=False, acc_logo="white")

CAPTION = """Yıllar geçse de her izlendiğinde yeniden güldüren 5 Türk komedisi. Kimi okul sıralarında, kimi köy meydanında, kimi bir turşu dükkânında geçiyor ama hepsinin repliği hâlâ dilimizde.

Hababam Sınıfı (1975) Özel Çamlıca Lisesi'nin haylaz sınıfını, Tosun Paşa (1976) iki aile arasında Tosun Paşa kılığına sokulan uşak Şaban'ı, Zübük (1980) Aziz Nesin'in fırsatçı karakterini, Çöpçüler Kralı (1977) mahallenin çöpçüsü Apti'yi, Neşeli Günler (1978) ise turşu yüzünden ayrılan bir aileyi anlatıyor.

Sen hangisinin repliklerini ezbere biliyorsun?

Yarın 18:00'de: Çocukken izlediğin, büyüyünce başka vuran 5 animasyon."""


FILMS = [
    ("Hababam Sınıfı", "1975 · Ertem Eğilmez", "Münir Özkul, Tarık Akan, Kemal Sunal, Halit Akçatepe, Adile Naşit",
     "Özel Çamlıca Lisesi'nin haylaz öğrencilerle dolu ünlü sınıfı. Kopya, kaçamak ve unutulmaz karakterler.", S("hababam", 1), None, "okul sıraları", RED),
    ("Tosun Paşa", "1976 · Kartal Tibet", "Kemal Sunal, Şener Şen, Müjde Ar, Adile Naşit",
     "İki aile arasındaki Yeşil Vadi kavgasında uşak Şaban, Tosun Paşa kılığına sokulur. İşler karışır.", S("tosunpasa", 3), S("tosunpasa", 2), "fesli kahraman", TEL),
    ("Zübük", "1980 · Kartal Tibet", "Kemal Sunal, Nevra Serezli, Metin Serezli",
     "Aziz Nesin'in aynı adlı kitabından uyarlandı: her ortamda yolunu bulan fırsatçı Zübük'ün hikâyesi.", S("zubuk", 1), S("zubuk", 2), "fırsatçı", GLD),
    ("Çöpçüler Kralı", "1977 · Zeki Ökten", "Kemal Sunal, Şener Şen, Ayşen Gruda",
     "Mahallenin çöpçüsü Apti ile esnafa baskı yapan zabıta memurunun hikâyesi.", S("copculer", 3), S("copculer", 1), "mahalle", RED),
    ("Neşeli Günler", "1978 · Orhan Aksoy", "Münir Özkul, Adile Naşit, Şener Şen",
     "Turşu yüzünden ayrılan anne babanın çocukları üçer üçer paylaşılır; yıllar sonra tesadüfen karşılaşırlar.", S("neseligunler", 2), S("neseligunler", 1), "turşu kavgası", TEL),
]




def build():
    n = 7
    cover = cover_mosaic(TH, [S("tosunpasa", 2), S("copculer", 1), S("neseligunler", 1), S("zubuk", 2)], "Liste · 5 film", "Yıllar geçse de<br>güldüren 5<br>Türk komedisi", "Kaydet, birlikte gül.")
    slides = [cover] + [film_slide(TH, i + 1, n, f[4], f[0], f[1], f[3], tag=f[6].capitalize(), extra="Başrolde: " + f[2]) for i, f in enumerate(FILMS)]
    slides.append(cta_slide(TH, "Hangisinin<br>repliklerini ezbere<br>biliyorsun?", "Aklında kalan repliği yorumlara yaz.", "Kaydet · Ailenle izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

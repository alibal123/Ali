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





HOLE = "repeating-linear-gradient(90deg,#f1e3c4 0 22px,transparent 22px 50px)"


def strip(x, y, w, h):
    return [box(x, y, w, h, "#1c1713", z=2),
            box(x + 18, y + 12, w - 36, 22, "transparent", z=3, css=f"background:{HOLE}"),
            box(x + 18, y + h - 34, w - 36, 22, "transparent", z=3, css=f"background:{HOLE}")]


def strip_film(i, n):
    title, meta, cast, body, src, _, tag, _c = FILMS[i]
    return {"bg": TH["bg"], "els": [
        *strip(40, 48, 1000, 700),
        img(grade(src, (924, 600), contrast=1.05, sat=0.95), 78, 98, 924, 600, z=4),
        T(f"{i+1}", 78, 98, 90, 90, 56, "abril", "#f1e3c4", fit=False, align="center", flex="center", bleed=True, z=7, bg="#a8321f"),
        T(title, M, 790, W - 2 * M, 100, 88, "abril", TH["ink"], nowrap=True, mn=44, lh=1.05),
        T(meta, M, 905, W - 2 * M, 36, 26, "typewriter", TH["accent"], nowrap=True, mn=16, upper=True, ls=2),
        T(body, M, 960, W - 2 * M, 190, 38, "inter", TH["ink"], weight=500, lh=1.38, mn=26),
        T("Başrolde: " + cast, M, 1196, W - 2 * M, 30, 22, "oswald", TH["ink"], weight=500, ls=2, upper=True, nowrap=True, mn=14, op=0.6),
        *footer(TH, i + 1, n),
    ]}


def build():
    n = 7
    fr = [S("tosunpasa", 2), S("copculer", 1), S("neseligunler", 1), S("zubuk", 2)]
    els = [
        T("Yıllar geçse de", M, 80, 800, 50, 36, "typewriter", TH["ink"], nowrap=True, ls=2),
        T("güldüren 5<br>Türk komedisi", M, 150, W - 2 * M, 400, 150, "abril", TH["accent"], nowrap=True, mn=70, lh=1.1),
        *strip(40, 640, 1000, 520),
    ]
    for k, nm in enumerate(fr):
        els.append(img(grade(nm, (218, 420), (0.2, 0, 0.8, 1), contrast=1.05, sat=0.95), 76 + k * 232, 700, 218, 420, z=4))
    els += [T("Kaydet, birlikte gül.", M, 1214, 600, 40, 28, "inter", TH["ink"], weight=500, nowrap=True, op=0.8), logo("black", W - M - 58, 1252, 58, z=9)]
    slides = [{"bg": TH["bg"], "els": els}] + [strip_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "Hangisinin<br>repliklerini ezbere<br>biliyorsun?", "Aklında kalan repliği yorumlara yaz.", "Kaydet · Ailenle izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

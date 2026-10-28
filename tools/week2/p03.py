from pro import *

ID = "2026-10-31_liste_cadilar-bayrami-5-film"
TH = theme("#2d1470", "#fff4e0", "#ff8a1f", on_acc="#1a1030", head="anton", logo_light="white")

CAPTION = """Cadılar Bayramı gecesi için korkutmadan eğlendiren 5 film. Kan yok, gerilim yok; sadece sevimli hayaletler, komik cadılar ve tuhaf dünyalar var.

Beetlejuice (1988) hayaletlere yardım eden çılgın bir "biyo-egzorsist"i, Hocus Pocus (1993) yüzyıllar sonra dirilen üç cadı kardeşi, Coraline (2009) gizli bir kapının ardındaki "öteki" dünyayı, The Nightmare Before Christmas (1993) Cadılar Bayramı Şehri'nin kralı Jack'in Noel merakını, Casper (1995) ise dost canlısı bir hayaletin hikâyesini anlatıyor.

Bu akşam bunlardan hangisini açıyorsun?

Yarın 18:00'de: "Bunu sevdiysen şunu izle", birbirine benzeyen 4 film çifti."""

FILMS = [
    ("BEETLEJUICE", "1988 · Tim Burton", "Hayalet olan çift evlerini yeni sahiplerinden kurtarmak için çılgın bir biyo-egzorsistten medet umar. Oscar'ı En İyi Makyaj dalında aldı.", S("beetlejuice", 1), S("beetlejuice", 2), "Çılgın"),
    ("HOCUS POCUS", "1993 · Kenny Ortega", "Salem'de üç cadı kardeş, yüzyıllar sonra bir Cadılar Bayramı gecesi geri döner. Bette Midler, Sarah Jessica Parker ve Kathy Najimy üçlüsü kült oldu.", S("hocuspocus", 2), S("hocuspocus", 1), "Kült"),
    ("CORALINE", "2009 · Henry Selick", "Yeni evlerindeki küçük bir kapıdan, her şeyin daha iyi göründüğü bir dünyaya geçen kızın stop-motion macerası.", S("coraline", 3), S("coraline", 2), "Kapıyı aç"),
    ("THE NIGHTMARE BEFORE CHRISTMAS", "1993 · Henry Selick", "Cadılar Bayramı Şehri'nin kralı Jack Skellington, Noel'i keşfedince her şeyi değiştirmek ister.", S("nightmare", 3), S("nightmare", 1), "Şarkılı"),
    ("CASPER", "1995 · Brad Silberling", "Dost canlısı küçük bir hayaletle genç bir kızın arkadaşlığı. Christina Ricci'nin başrolde olduğu bu film aileyle izlenir.", S("casper", 1), S("casper", 2), "Aileyle izle"),
]



ARC = lambda w: f"{w // 2}px {w // 2}px 0 0"


def arch_film(i, n):
    title, meta, body, src, _, tag = FILMS[i]
    return {"bg": TH["bg"], "els": [
        img(grade(src, (680, 780), (0.15, 0, 0.85, 1)), 200, 72, 680, 780, z=2, radius=ARC(680)),
        label(tag, 200 + 340 - 80, 60, bg=TH["accent"], color="#1a1030", size=22, z=6),
        T(title, M, 890, W - 2 * M, 100, 92, "anton", TH["ink"], nowrap=True, mn=44, lh=1.05, align="center"),
        T(meta, M, 1000, W - 2 * M, 36, 26, "oswald", TH["accent"], weight=500, ls=4, upper=True, nowrap=True, mn=18, align="center"),
        T(body, 150, 1054, W - 300, 170, 36, "inter", TH["ink"], weight=500, lh=1.38, mn=26, align="center"),
        *footer(TH, i + 1, n),
    ]}


def build():
    n = 7
    els = [
        T("KORKUTMADAN<br>EĞLENDİREN<br>5 FİLM", M, 70, W - 2 * M, 470, 190, "anton", "#2d1470", nowrap=True, mn=70, lh=1.07),
        T("CADILAR BAYRAMI GECESİ", M, 580, 700, 34, 26, "oswald", "#2d1470", fit=False, weight=500, ls=6, upper=True, nowrap=True),
    ]
    heights = [520, 440, 520, 440, 520]
    for k, f in enumerate(FILMS):
        w = 176
        x = M + k * (w + 15)
        h = heights[k]
        els.append(img(grade(f[4], (w, h), (0.25, 0, 0.75, 1)), x, 1180 - h, w, h, z=2, radius=ARC(w)))
    els.append(T("Kan yok, gerilim yok. Kaydet, bu gece aç.", M, 1214, 800, 40, 26, "inter", "#2d1470", weight=500, nowrap=True, op=0.85))
    els.append(logo("black", W - M - 58, 1252, 58, z=9))
    cover = {"bg": "#ff8a1f", "els": els}
    slides = [cover] + [arch_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "BU GECE<br>HANGİSİNİ<br>AÇIYORSUN?", "Yorumlara yaz, ışıkları kıs.", "Kaydet · Aileyle izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

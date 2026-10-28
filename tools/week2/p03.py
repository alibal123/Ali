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


def build():
    n = 7
    cover = cover_mosaic(TH, [f[4] for f in FILMS], "Cadılar Bayramı gecesi", "KORKUTMADAN<br>EĞLENDİREN<br>5 FİLM", "Kan yok, gerilim yok. Kaydet, bu gece aç.")
    slides = [cover] + [film_slide(TH, i + 1, n, f[3], f[0], f[1], f[2], tag=f[5]) for i, f in enumerate(FILMS)]
    slides.append(cta_slide(TH, "BU GECE<br>HANGİSİNİ<br>AÇIYORSUN?", "Yorumlara yaz, ışıkları kıs.", "Kaydet · Aileyle izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

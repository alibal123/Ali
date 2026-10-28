from pro import *

ID = "2026-11-05_liste_tek-mekanda-gecen-5-film"
TH = theme("#e9eef5", "#0f1c33", "#2447ff", on_acc="#fff", head="anton")

CAPTION = """Büyük bütçe yok, devasa dekor yok. Tek bir oda, tek bir araç, tek bir mekân var; ama sonuna kadar nefes alamıyorsun. Tek mekânda geçen 5 film.

12 Angry Men (1957) bir jüri odasındaki on iki kişiyi, Rope (1948) bir dairede işlenen "kusursuz cinayet"i, Locke (2013) bir arabada geçen bir geceyi, Buried (2010) bir tabutun içinde uyanan adamı, Cube (1997) birbirine geçen küp odalardan oluşan bir yapıda uyanan altı yabancıyı anlatıyor.

Sen bu listeye hangi tek mekân filmini eklerdin?

Yarın 13:00'te yeni haftanın ilk gönderisiyle buradayız. Takipte kal."""

FILMS = [
    ("12 ANGRY MEN", "1957 · Sidney Lumet", "On iki jüri üyesi tek bir odada, genç bir sanığın kaderine karar vermeye çalışır. Konuşmayla ilerleyen en gergin filmlerden biri.", S("angrymen", 1), S("angrymen", 3), "Jüri odası"),
    ("ROPE", "1948 · Alfred Hitchcock", "Neredeyse tamamı tek bir dairede geçen film, kesintisiz çekilmiş izlenimi veren uzun planlarla ilerler. James Stewart başrolde.", S("rope", 3), S("rope", 1), "Tek daire"),
    ("LOCKE", "2013 · Steven Knight", "Bir adam, bir araba, bir gece ve bir telefonla çöken hayat. Tom Hardy ekranda neredeyse tek başına.", S("locke", 1), S("locke", 3), "Tek araba"),
    ("BURIED", "2010 · Rodrigo Cortés", "Bir tabutun içinde uyanan adamın hikâyesi. Kamera filmin boyunca tabutun dışına çıkmaz.", S("buried", 2), S("buried", 3), "Tek tabut"),
    ("CUBE", "1997 · Vincenzo Natali", "Altı yabancı, birbirine geçen küp odalardan oluşan bir yapıda uyanır ve birlikte çıkış yolu aramak zorunda kalır.", S("cube", 1), S("cube", 3), "Tek yapı"),
]


def build():
    n = 7
    cover = cover_mosaic(TH, [f[4] for f in FILMS], "Liste · 5 film", "TEK ODADA<br>GEÇEN<br>5 FİLM", "Büyük bütçe yok, nefes almak da yok.")
    slides = [cover] + [film_slide(TH, i + 1, n, f[3], f[0], f[1], f[2], tag=f[5]) for i, f in enumerate(FILMS)]
    slides.append(cta_slide(TH, "HANGİ TEK<br>MEKÂN FİLMİNİ<br>EKLERDİN?", "Yorumlara yaz, listeyi birlikte büyütelim.", "Kaydet · Yeni hafta yarın başlıyor"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

from pro import *

ID = "2026-11-05_liste_tek-mekanda-gecen-5-film"
TH = theme("#f1ece3", "#161412", "#d9432b", on_acc="#fff", head="anton")

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




def vtitle(text, size=110):
    return T(text, 84, 960, 880, 140, size, "anton", TH["ink"], fit=False, nowrap=True, lh=1.0, rot=-90, origin="0 0", bleed=True)


def v_film(i, n):
    title, meta, body, src, _, tag = FILMS[i]
    return {"bg": TH["bg"], "els": [
        img(grade(src, (830, 1000), (0, 0, 1, 1)), 250, 0, 830, 1000, z=2),
        vtitle(title, fit(title, 880, 118, 0.46, 60)),
        T(f"NO. {i+1:02d} · {tag.upper()}", M, 1040, W - 2 * M, 30, 22, "oswald", TH["accent"], fit=False, weight=500, ls=5, nowrap=True),
        T(meta, M, 1078, W - 2 * M, 30, 22, "oswald", TH["ink"], weight=500, ls=4, upper=True, nowrap=True, mn=16, op=0.6),
        T(body, M, 1124, W - 2 * M, 120, 32, "inter", TH["ink"], weight=500, lh=1.4, mn=24),
        *footer(TH, i + 1, n),
    ]}


def build():
    n = 7
    cover = {"bg": TH["bg"], "els": [
        img(grade(S("cube", 3), (830, 1000), (0, 0, 1, 1)), 250, 0, 830, 1000, z=2),
        vtitle("TEK ODADA GEÇEN 5 FİLM", 84),
        T("LİSTE · 5 FİLM", M, 1040, 600, 30, 22, "oswald", TH["accent"], fit=False, weight=500, ls=5, nowrap=True),
        T("Büyük bütçe yok, nefes almak da yok.", M, 1086, W - 2 * M, 50, 36, "inter", TH["ink"], weight=500, nowrap=True, mn=22),
        T("Kaydet, sırayla izle.", M, 1146, 600, 36, 26, "inter", TH["ink"], weight=500, nowrap=True, op=0.6),
        logo(TH["logo"], W - M - 58, 1252, 58, z=9),
    ]}
    slides = [cover] + [v_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "HANGİ TEK<br>MEKÂN FİLMİNİ<br>EKLERDİN?", "Yorumlara yaz, listeyi birlikte büyütelim.", "Kaydet · Yeni hafta yarın başlıyor"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

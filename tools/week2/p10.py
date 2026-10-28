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



DK = "#0f1c33"


def frame(x, y, w, h, src, crop=(0, 0, 1, 1), pad=22, mat=34):
    return [box(x, y, w, h, DK, z=2), box(x + pad, y + pad, w - 2 * pad, h - 2 * pad, "#f6f8fb", z=3),
            img(grade(src, (w - 2 * (pad + mat), h - 2 * (pad + mat)), crop), x + pad + mat, y + pad + mat, w - 2 * (pad + mat), h - 2 * (pad + mat), z=4)]


def museum(i, n):
    title, meta, body, src, _, tag = FILMS[i]
    return {"bg": TH["bg"], "els": [
        *frame(M, 72, W - 2 * M, 700, src),
        box(M, 820, W - 2 * M, 380, "#fff", z=2),
        box(M, 820, 8, 380, TH["accent"], z=3),
        T(f"NO. {i+1:02d} · {tag.upper()}", M + 40, 842, 700, 30, 22, "oswald", TH["accent"], fit=False, weight=500, ls=5, nowrap=True),
        T(title, M + 40, 906, W - 2 * M - 80, 96, 84, "anton", TH["ink"], nowrap=True, mn=44, lh=1.05),
        T(meta, M + 40, 1012, W - 2 * M - 80, 30, 22, "oswald", TH["ink"], weight=500, ls=4, upper=True, nowrap=True, mn=16, op=0.6),
        T(body, M + 40, 1060, W - 2 * M - 80, 130, 32, "inter", TH["ink"], weight=500, lh=1.4, mn=22),
        *footer(TH, i + 1, n),
    ]}


def build():
    n = 7
    cover = {"bg": TH["bg"], "els": [
        T("TEK ODADA<br>GEÇEN 5 FİLM", M, 90, W - 2 * M, 280, 130, "anton", TH["ink"], nowrap=True, mn=60, lh=1.06),
        box(M, 400, W - 2 * M, 760, DK, z=2),
        box(M + 36, 436, W - 2 * M - 72, 688, "#f6f8fb", z=3),
        box(M + 70, 470, W - 2 * M - 140, 620, DK, z=4),
        box(M + 104, 504, W - 2 * M - 208, 552, "#f6f8fb", z=5),
        img(grade(S("cube", 1), (W - 2 * M - 242, 484), (0.1, 0, 0.9, 1)), M + 138, 538, W - 2 * M - 242, 484, z=6),
        T("Büyük bütçe yok, nefes almak da yok.", M, 1190, 800, 36, 26, "inter", TH["ink"], weight=500, nowrap=True, op=0.75),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]}
    slides = [cover] + [museum(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "HANGİ TEK<br>MEKÂN FİLMİNİ<br>EKLERDİN?", "Yorumlara yaz, listeyi birlikte büyütelim.", "Kaydet · Yeni hafta yarın başlıyor"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

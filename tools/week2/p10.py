from pro import *

ID = "2026-11-05_liste_tek-mekanda-gecen-5-film"
TH = theme("#f1ece3", "#161412", "#0f2a4a", on_acc="#fff", head="anton")

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





RED = "#ff3b30"


def brackets(c="#fff", inset=44, L=90, t=5):
    r = []
    for (x, y, dx, dy) in [(inset, inset, 1, 1), (W - inset, inset, -1, 1), (inset, H - inset, 1, -1), (W - inset, H - inset, -1, -1)]:
        r.append(box(x if dx > 0 else x - L, y if dy > 0 else y - t, L, t, c, z=7))
        r.append(box(x if dx > 0 else x - t, y if dy > 0 else y - L, t, L, c, z=7))
    return r


def duo(src, crop=(0, 0, 1, 1)):
    return img(prep(src, crop=crop, size=(1080, 1350), duo=("#102743", "#f4f8fd", "#7aa5d1"), contrast=1.1, grain=9), 0, 0, W, H, z=1)


def rec_bar(code):
    return [box(88, 96, 18, 18, RED, z=8, radius=40), T("REC", 120, 86, 200, 36, 24, "oswald", "#fff", fit=False, weight=500, ls=5, nowrap=True),
            T(code, W - 88 - 360, 86, 360, 36, 24, "oswald", "#fff", fit=False, weight=500, ls=5, align="right", nowrap=True)]


def room_film(i, n):
    title, meta, body, src, _, tag = FILMS[i]
    return {"bg": "#000", "els": [
        duo(src),
        box(0, 520, W, 830, "linear-gradient(180deg,rgba(4,10,20,0),rgba(8,22,44,.78) 62%)", z=2),
        *brackets(), *rec_bar(f"ODA {i+1:02d} / 05"),
        label(tag, 88, 700, bg="rgba(255,255,255,.16)", color="#fff", size=22, z=6),
        T(title, 88, 780, W - 176, 150, 126, "anton", "#fff", nowrap=True, mn=54, lh=1.05),
        T(meta, 88, 944, W - 176, 34, 26, "oswald", "#fff", weight=500, ls=4, upper=True, nowrap=True, mn=18, op=0.8),
        T(body, 88, 1002, W - 176, 190, 36, "inter", "#fff", weight=500, lh=1.4, mn=26),
        logo("white", W - 88 - 52, 1186, 52, z=9),
    ]}


def build():
    n = 7
    cover = {"bg": "#000", "els": [
        duo(S("cube", 3)),
        box(0, 380, W, 970, "linear-gradient(180deg,rgba(4,10,20,0),rgba(8,22,44,.82) 58%)", z=2),
        *brackets(), *rec_bar("5 FİLM · TEK ODA"),
        T("TEK ODADA<br>GEÇEN<br>5 FİLM", 88, 620, W - 176, 520, 190, "anton", "#fff", nowrap=True, mn=70, lh=1.06),
        T("Büyük bütçe yok, nefes almak da yok.", 88, 1180, 800, 36, 26, "inter", "#fff", weight=500, nowrap=True, op=0.85),
        logo("white", W - 88 - 52, 1186, 52, z=9),
    ]}
    slides = [cover] + [room_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "HANGİ TEK<br>MEKÂN FİLMİNİ<br>EKLERDİN?", "Yorumlara yaz, listeyi birlikte büyütelim.", "Kaydet · Yeni hafta yarın başlıyor"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

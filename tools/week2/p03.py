from pro import *

ID = "2026-10-31_liste_cadilar-bayrami-5-film"
NIGHT, CRM, ORG, INK = "#11141f", "#f4ead2", "#f26b1d", "#1a1622"
TH = theme(NIGHT, CRM, ORG, on_acc=NIGHT, head="anton")
LOGO = dict(pos="tr", w=70, on_light="black", on_dark="yellow")

CAPTION = """Cumartesi gecesi evde kalanlar kulübü: dışarı çıkmıyoruz, ama ruh halimize uygun bir film seçiyoruz. Bu akşamki moduna göre 5 film.

Biraz ağlayıp rahatlamak istiyorsan Forrest Gump (1994), çocukluğuna dönmek istiyorsan Big Fish (2003), başka bir şehirde olmak istiyorsan Midnight in Paris (2011), arkadaşlarınla katili tartışacaksan Knives Out (2019), telefonu bırakıp kafa yormak istiyorsan Inception (2010). Forrest Gump 6, Inception 4 Oscar aldı; Midnight in Paris En İyi Orijinal Senaryo ödülünü kazandı.

Bu akşamki modun hangisi? Yorumlara yaz.

Yarın 13:00'te: Dunesday, yani 18 Aralık'ta aynı gün vizyona girecek iki dev film."""

FILMS = [
    ("FORREST GUMP", "1994 · Robert Zemeckis", "Alabama'dan bir adamın, tarihin tam ortasından geçen hayatı. Tom Hanks oynuyor; film En İyi Film dahil altı Oscar aldı.", S("forrestgump", 1), "Battaniyenin altı", "BİRAZ AĞLAYIP RAHATLAMAK İSTİYORSAN"),
    ("BIG FISH", "2003 · Tim Burton", "Hayatını masal gibi anlatan bir baba ile gerçeği arayan oğlunun hikâyesi. Ewan McGregor ve Albert Finney oynuyor.", S("bigfish", 1), "Kanepenin köşesi", "ÇOCUKLUĞUNA DÖNMEK İSTİYORSAN"),
    ("MIDNIGHT IN PARIS", "2011 · Woody Allen", "Paris'e giden bir yazar, geceyarısı 1920'lerin sanatçılarına karışır. Oscar'ı En İyi Orijinal Senaryo dalında aldı.", S("midnightparis", 3), "Halının üstü", "BAŞKA BİR ŞEHİRDE OLMAK İSTİYORSAN"),
    ("KNIVES OUT", "2019 · Rian Johnson", "Zengin bir yazar ölür, herkes şüpheli olur. Daniel Craig, Ana de Armas ve Chris Evans'lı bir polisiye.", S("knivesout", 1), "Yer yatağı", "ARKADAŞLARINLA KATİLİ TARTIŞACAKSAN"),
    ("INCEPTION", "2010 · Christopher Nolan", "Rüyalara girip fikir çalan bir ekip. Leonardo DiCaprio'lu film dört Oscar aldı.", S("inception", 1), "Tek kişilik koltuk", "TELEFONU BIRAKIP KAFA YORMAK İSTİYORSAN"),
]

def notch_ticket(x, y, w, h, ny, col=CRM, bg=NIGHT, z=2, rot=0, r=28):
    return [box(x, y, w, h, col, z=z, radius=r, **({"rot": rot} if rot else {}))]


def barcode(x, y, h, z=6, seed=3):
    els, cx, k = [], x, seed
    while cx < x + 520:
        k = (k * 37 + 11) % 97
        wd = 3 + k % 6
        if k % 3:
            els.append(box(cx, y, wd, h, INK, z=z))
        cx += wd + 3 + k % 3
    return els


def ticket(i, n):
    t, meta, body, src, seat, mood = FILMS[i]
    X, Y, TW, TH_ = 80, 140, 920, 1120
    NY = 1020
    els = [
        *notch_ticket(X, Y, TW, TH_, NY),
        img(grade(src, (860, 420), (0, 0, 1, 1), grain=5), X + 30, Y + 30, 860, 420, z=3, radius="16px 16px 0 0"),
        
        box(X + 30, Y + 450, 860, 90, NIGHT, z=5, radius="0 0 16px 16px"),
        label(f"MOD {i+1} / 5", X + 56, Y + 56, bg=ORG, color=NIGHT, size=22, z=6),
        T(mood, X + 56, Y + 450, 780, 90, 38, "anton", CRM, nowrap=True, mn=22, lh=1.1, flex="center", z=7),
        T(t, X + 40, Y + 548, TW - 80, 110, 84, "anton", INK, nowrap=True, mn=40, lh=1.12, z=6),
        T(meta, X + 40, Y + 660, TW - 80, 30, 24, "oswald", ORG, weight=600, ls=5, upper=True, nowrap=True, mn=14, z=6),
        T(body, X + 40, Y + 704, TW - 80, 130, 30, "inter", INK, weight=500, lh=1.38, mn=22, z=6),
        box(X - 36, NY - 36, 72, 72, NIGHT, z=8, radius=100), box(X + TW - 36, NY - 36, 72, 72, NIGHT, z=8, radius=100),
        box(X + 50, NY - 2, TW - 100, 0, "transparent", z=6, css="border-top:4px dashed rgba(26,22,34,.35)"),
    ]
    fy = NY + 36
    for k, (lab, val, wd) in enumerate((("SEANS", "CMT 21:00", 230), ("SALON", "OTURMA ODASI", 300), ("KOLTUK", seat.upper(), 310))):
        fx = X + 50 + (0 if k == 0 else (230 + 20 if k == 1 else 230 + 300 + 40))
        els += [T(lab, fx, fy, wd, 24, 18, "oswald", ORG, fit=False, weight=600, ls=6, nowrap=True, z=6),
                T(val, fx, fy + 30, wd, 54, 34, "anton", INK, nowrap=True, mn=16, lh=1.1, z=6)]
    els += barcode(X + 50, NY + 140, 64, seed=i * 7 + 3)
    els.append(T(f"NO 31.10 / 0{i+1}", X + TW - 330, NY + 156, 280, 30, 22, "oswald", INK, fit=False, weight=500, ls=5, align="right", nowrap=True, z=6, op=0.6))
    els.append(T(f"{i+2:02d} / 07", M, 1290, 200, 28, 20, "oswald", CRM, fit=False, weight=500, ls=5, op=0.55))
    return {"bg": NIGHT, "els": els}


def build():
    n = 7
    els = [
        T("CUMARTESİ GECESİ<br>EVDE KALANLAR<br>KULÜBÜ", M, 110, W - 2 * M, 440, 128, "anton", CRM, nowrap=True, mn=70, lh=1.16, z=3),
        T("RUH HALİNE GÖRE 5 FİLM", M, 560, 900, 30, 24, "oswald", ORG, fit=False, weight=600, ls=7, nowrap=True, z=3),
    ]
    xs = [170, 355, 540, 725, 910]
    rots = [-9, -4, 0, 4, 9]
    ys = [850, 830, 820, 830, 850]
    for k in range(5):
        f = FILMS[k]
        cx, cy, r = xs[k], ys[k], rots[k]
        els += [
            box(cx - 125, cy - 200, 250, 400, CRM, z=4 + k, radius=18, rot=r),
            img(grade(f[3], (226, 320), (0.3, 0, 0.7, 1), grain=5), cx - 113, cy - 188, 226, 320, z=5 + k, radius="12px", rot=r),
        ]
    els += [
        box(70, 1150, 940, 130, CRM, z=20, radius=22, rot=-2),
        box(34, 1150 + 65 - 36, 72, 72, NIGHT, z=21, radius=100),
        box(974, 1150 + 65 - 36, 72, 72, NIGHT, z=21, radius=100),
        T("GİRİŞ BİLETİ", 130, 1166, 400, 24, 18, "oswald", ORG, fit=False, weight=600, ls=7, nowrap=True, z=22, rot=-2),
        T("PİJAMA SERBEST", 130, 1192, 820, 50, 40, "anton", INK, nowrap=True, mn=26, lh=1.1, z=22, rot=-2),
        T("SEANS CMT 21:00  ·  SALON OTURMA ODASI  ·  KOLTUK KANEPE", 130, 1246, 820, 24, 16, "oswald", INK, fit=False, weight=500, ls=3, nowrap=True, z=22, rot=-2, op=0.7),
    ]
    slides = [{"bg": NIGHT, "els": els}] + [ticket(i, n) for i in range(5)]
    slides.append({"bg": ORG, "els": [
        T("SEANS<br>BAŞLIYOR", M, 110, W - 2 * M, 470, 170, "anton", NIGHT, nowrap=True, mn=70, lh=1.1),
        T("Bu akşamki modun hangisi?", M, 640, W - 2 * M, 100, 52, "anton", NIGHT, nowrap=True, mn=28, lh=1.2),
        T("Yorumlara yaz, battaniyeyi çek.", M, 760, W - 2 * M, 50, 34, "inter", NIGHT, weight=600, nowrap=True),
        label("Kaydet · Cumartesiye sakla", M, 860, bg=NIGHT, color=CRM, size=24),
    ]})
    return {"id": ID, "caption": CAPTION, "slides": slides}

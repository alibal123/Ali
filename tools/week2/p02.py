from pro import *

ID = "2026-10-31_vizyon_dunesday"
RED, GLD, INK, CRM = "#e03a2f", "#f2b632", "#14110f", "#f4efe6"
TH_A = theme(CRM, INK, RED, on_acc="#fff", head="anton")
TH_D = theme(CRM, INK, GLD, on_acc=INK, head="anton", accent_txt="#a77a05")

CAPTION = """Takvimlere not al: 18 Aralık'ta sinemada iki dev film aynı gün vizyona giriyor. Avengers: Doomsday ve Dune: Part Three.

Avengers: Doomsday'in başında Russo kardeşler var; kadroda Robert Downey Jr., Chris Evans, Chris Hemsworth ve Pedro Pascal yer alıyor. Dune: Part Three ise Denis Villeneuve'ün üçlemeyi kapatan filmi; Timothée Chalamet, Zendaya ve Florence Pugh dönüyor. İlginç detay: Florence Pugh iki filmde de var. Marvel'da Yelena Belova'yı, Dune'da Prenses Irulan'ı oynuyor.

Sen hangisine ilk gideceksin? Avengers için 1, Dune için 2 yaz.

Bugün 18:00'de: Cadılar Bayramı gecesi korkutmadan eğlendiren 5 film."""


def cover():
    return {"bg": "#000", "els": [
        img(grade(S("doomsday", 5), (1080, 680)), 0, 0, W, 680, z=1),
        img(grade(S("dune3", 1), (1080, 680)), 0, 670, W, 680, z=1),
        box(0, 664, W, 12, CRM, z=3),
        box(0, 800, W, 550, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.8))", z=2),
        label("Avengers: Doomsday", M, 56, bg=RED, size=24),
        label("Dune: Part Three", M, 712, bg=GLD, color=INK, size=24),
        box(W // 2 - 56, 620, 112, 112, CRM, z=6),
        T("VS", W // 2 - 56, 620, 112, 112, 54, "anton", INK, fit=False, align="center", flex="center", lh=1.0, bleed=True, z=7),
        *kicker(TH_A, "18 Aralık 2026", M, 912, color="#fff"),
        T("AYNI GÜN,<br>İKİ DEV", M, 972, W - 2 * M, 250, 170, "anton", "#fff", nowrap=True, mn=80, lh=1.06),
        logo("white", W - M - 58, 1252, 58, z=9),
    ]}


def build():
    n = 6
    s2 = info_slide(TH_A, 2, n, S("doomsday", 5), "AVENGERS: DOOMSDAY", "18 ARALIK", [
        ("Yönetmen", "Anthony ve Joe Russo", 66),
        ("Kadro", "Robert Downey Jr., Chris Evans, Chris Hemsworth, Pedro Pascal, Paul Rudd", 124),
        ("Konu", "Avengers, Wakanda, Fantastic Four ve orijinal X-Men, üç farklı evrenden gelen ortak bir tehdide karşı karşıya.", 150),
    ], tag="Thunderbolts*'tan 14 ay sonra")
    s3 = info_slide(TH_D, 3, n, S("dune3", 1), "DUNE: PART THREE", "18 ARALIK", [
        ("Yönetmen", "Denis Villeneuve", 66),
        ("Kadro", "Timothée Chalamet, Zendaya, Florence Pugh, Jason Momoa, Rebecca Ferguson", 124),
        ("Konu", "Paul'ün imparatorluğu ele geçirmesinden yaklaşık yirmi yıl sonrası. Frank Herbert'in Dune Messiah romanından uyarlandı.", 150),
    ], tag="Villeneuve'ün son Dune filmi")
    s4 = {"bg": GLD, "els": [
        *kicker(TH_D, "İlginç detay", M, 120, color=INK),
        T("İKİSİNDE DE<br>OYNAYAN<br>TEK İSİM", M, 190, W - 2 * M, 470, 150, "anton", INK, nowrap=True, mn=70, lh=1.04),
        T("FLORENCE PUGH", M, 700, W - 2 * M, 120, 120, "anton", "#fff", nowrap=True, mn=60, lh=1.0, stroke=f"2px {INK}"),
        rule(M, 880, W - 2 * M, INK, op=0.9, h=3),
        T("AVENGERS: DOOMSDAY", M, 910, 700, 30, 24, "oswald", INK, fit=False, weight=500, ls=5, op=0.7),
        T("Yelena Belova", M, 950, W - 2 * M, 70, 56, "serif", INK, nowrap=True, mn=30),
        rule(M, 1050, W - 2 * M, INK, op=0.9, h=3),
        T("DUNE: PART THREE", M, 1080, 700, 30, 24, "oswald", INK, fit=False, weight=500, ls=5, op=0.7),
        T("Prenses Irulan", M, 1120, W - 2 * M - 80, 70, 56, "serif", INK, nowrap=True, mn=30),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]}
    s5 = {"bg": CRM, "els": [
        img(grade(S("doomsday", 4), (534, 600), (0.2, 0, 0.8, 1)), 0, 0, 534, 600, z=1),
        img(grade(S("dune3", 5), (534, 600), (0.1, 0, 0.9, 1)), 546, 0, 534, 600, z=1),
        label("Marvel", M, 520, bg=RED, size=22), label("Dune", 546 + 40, 520, bg=GLD, color=INK, size=22),
        *kicker(TH_A, "Salon savaşı", M, 660),
        T("İKİ FORMAT,<br>İKİ STRATEJİ", M, 720, W - 2 * M, 260, 110, "anton", INK, nowrap=True, mn=60, lh=1.04),
        T("ABD'de IMAX salonlarını ilk haftalarda Dune tutuyor. Marvel ise kendi büyük ekran formatı InfinityVision'a yöneliyor.", M, 1010, W - 2 * M, 190, 40, "inter", INK, weight=500, lh=1.4, mn=28),
        *footer(TH_A, 5, n),
    ]}
    s6 = {"bg": CRM, "els": [
        T("SEN HANGİSİNE<br>İLK GİDECEKSİN?", M, 90, W - 2 * M, 300, 104, "anton", INK, nowrap=True, mn=60, lh=1.06),
        T("Yorumlara 1 ya da 2 yaz.", M, 410, W - 2 * M, 50, 36, "inter", INK, weight=500, op=0.7, nowrap=True),
        box(0, 500, 540, 850, RED, z=2), box(540, 500, 540, 850, GLD, z=2),
        T("1", 0, 540, 540, 400, 380, "anton", "#fff", fit=False, align="center", lh=1.0, bleed=True),
        T("AVENGERS<br>DOOMSDAY", 0, 1090, 540, 120, 38, "oswald", "#fff", fit=False, weight=500, ls=5, align="center", lh=1.3, bleed=True),
        T("2", 540, 540, 540, 400, 380, "anton", INK, fit=False, align="center", lh=1.0, bleed=True),
        T("DUNE<br>PART THREE", 540, 1090, 540, 120, 38, "oswald", INK, fit=False, weight=500, ls=5, align="center", lh=1.3, bleed=True),
        logo("white", M, 1252, 58, z=9),
    ]}
    return {"id": ID, "caption": CAPTION, "slides": [cover(), s2, s3, s4, s5, s6]}

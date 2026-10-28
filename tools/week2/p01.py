from pro import *
ORG, CRM, BLU, INK, YEL = "#ff5a1f", "#f4efe6", "#2447ff", "#14110f", "#ffd23f"

ID = "2026-10-30_liste_basa-sardiran-5-film"
TH = theme("#f4efe6", "#14110f", "#ff5a1f", on_acc="#fff", head="anton")
CAPTION = """Bitince "dur, şimdi başa saralım" dedirten 5 film. Hepsinin ortak noktası şu: ilk izlemede hikâyeyi anladığını sanıyorsun, ikinci izlemede her sahnede bir ipucu görüp "bunu nasıl kaçırdım" diyorsun.

The Prestige (2006) birbirini alt etmeye çalışan iki sihirbazın takıntısını, Shutter Island (2010) bir adadaki akıl hastanesinden kaybolan hastanın izini, The Usual Suspects (1995) bir sorgu odasında anlatılan hikâyenin ne kadarının doğru olduğunu, Gone Girl (2014) evlilik yıldönümünde kaybolan bir kadının ardından başlayan şüpheyi, The Sixth Sense (1999) ise ölüleri gördüğünü söyleyen bir çocuğun hikâyesini anlatıyor.

Hepsini kaydet, sonunu kimseye anlatma. Sen bu listeye hangi filmi eklerdin?

Yarın 13:00'te: 18 Aralık'ta aynı gün vizyona girecek iki dev film."""


FILMS = [
    ("THE PRESTIGE", "2006 · Christopher Nolan", "Londra'da iki sihirbaz birbirini alt etmek için hiçbir sınır tanımıyor. Hilenin üç perdesi var; sen hangisinde yakalandığını fark edeceksin.", S("prestige", 4), S("prestige", 3), (0, 0, 1, 1), "Dikkatle izle", (0, 0, 1, 1)),
    ("SHUTTER ISLAND", "2010 · Martin Scorsese", "Bir federal şerif, adadaki akıl hastanesinden kaybolan bir hastayı arar. Her sahnede küçük bir şey gözünden kaçar.", S("shutterisland", 4), S("shutterisland", 1), (0, 0, 1, 1), "İpuçlarını say", (0, 0, 1, 1)),
    ("THE USUAL SUSPECTS", "1995 · Bryan Singer", "Beş suçlu bir sıra sorgusunda bir araya gelir. Anlatılan hikâyenin ne kadarı doğru? İki Oscar aldı: En İyi Yardımcı Erkek Oyuncu ve En İyi Orijinal Senaryo.", S("usualsuspects", 1), S("usualsuspects", 3), (0.30, 0, 0.70, 1), "Kime inanırsın?", (0, 0, 1, 1)),
    ("GONE GIRL", "2014 · David Fincher", "Evlilik yıldönümünde karısı kaybolan bir adam, tüm ülkenin gözü önünde baş şüpheli olur.", S("gonegirl", 3), S("gonegirl", 1), (0.30, 0, 0.70, 1), "Kimi suçlarsın?", (0, 0, 1, 1)),
    ("THE SIXTH SENSE", "1999 · M. Night Shyamalan", "Bir çocuk psikoloğu, ölüleri gördüğünü söyleyen küçük bir çocuğa yardım etmeye çalışır.", S("sixthsense", 1), S("sixthsense", 2), (0.30, 0, 0.72, 1), "İkinci izleme şart", (0, 0, 1, 1)),
]



SLIDE_TH = [  # bg, ink, mute-accent
    (CRM, INK, ORG), (BLU, "#fff", YEL), (ORG, INK, CRM), (YEL, INK, BLU), (CRM, INK, BLU),
]


def poster_film(i, n):
    title, meta, body, src, _, _, tag, _ = FILMS[i]
    bg, ink, acc = SLIDE_TH[i]
    return {"bg": bg, "els": [
        T(f"{i+1:02d}", M, 40, 420, 300, 280, "anton", ink, fit=False, lh=1.0, bleed=True, stroke=f"3px {ink}", fill_none=True, op=0.9),
        T(tag, W - M - 440, 72, 440, 40, 24, "oswald", ink, fit=False, weight=500, ls=5, upper=True, align="right", nowrap=True, op=0.75),
        T(title, M, 330, W - 2 * M, 110, 104, "anton", ink, nowrap=True, mn=48, lh=1.05),
        T(meta, M, 448, W - 2 * M, 36, 26, "oswald", ink, weight=500, ls=4, upper=True, nowrap=True, mn=18, op=0.75),
        img(grade(src, (1080, 470), contrast=1.08, sat=1.12), 0, 510, W, 470, z=2),
        T(body, M, 1010, W - 2 * M, 200, 42, "inter", ink, weight=500, lh=1.38, mn=28),
        T(f"{i+1:02d} / {n:02d}", M, 1268, 260, 34, 24, "oswald", ink, fit=False, weight=500, ls=4, op=0.6),
        logo("white" if bg in (BLU,) else "black", W - M - 58, 1252, 58, z=9),
    ]}


def build():
    n = 7
    cover = {"bg": ORG, "els": [
        T("BİTİNCE<br>BAŞA<br>SARDIRAN", M, 96, W - 2 * M, 610, 240, "anton", CRM, nowrap=True, mn=80, lh=1.03),
        img(grade(S("sixthsense", 2), (1080, 420), contrast=1.08), 0, 740, W, 420, z=2),
        box(M, 1090, 360, 80, INK, z=4),
        T("5 FİLM · SPOİLER YOK", M, 1090, 360, 80, 26, "oswald", CRM, fit=False, weight=500, ls=4, align="center", flex="center", nowrap=True, bleed=True, z=5),
        T("Kaydet, sırayla izle.", M, 1214, 600, 40, 28, "inter", INK, weight=500, nowrap=True, op=0.8),
        logo("black", W - M - 58, 1252, 58, z=9),
    ]}
    slides = [cover] + [poster_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "SONU SENİ<br>ŞAŞIRTAN FİLM<br>HANGİSİ?", "Yorumlara yaz, ama sonunu anlatma.", "Kaydet · Sırayla izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

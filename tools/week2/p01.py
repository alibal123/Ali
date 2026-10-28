from pro import *
ORG, CRM, BLU, INK, YEL = "#ff5a1f", "#f4efe6", "#2447ff", "#14110f", "#ffd23f"

ID = "2026-10-30_liste_basa-sardiran-5-film"
TH = theme("#f1ece3", "#161412", "#c8321f", on_acc="#fff", head="anton")
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




def sub_label(text, y):
    size = 28
    w = int(len(text) * size * 0.62 + 56)
    x = (W - w) // 2
    return [box(x, y, w, 56, "rgba(0,0,0,.68)", z=6),
            T(text, x, y, w, 56, size, "inter", "#fff", fit=False, weight=500, align="center", flex="center", nowrap=True, bleed=True, z=7)]


def lb_film(i, n):
    title, meta, body, src, _, _, tag, _x = FILMS[i]
    return {"bg": TH["bg"], "els": [
        T(f"{i+1:02d}", M, 84, 200, 36, 28, "oswald", TH["accent"], fit=False, weight=500, ls=6, bleed=False),
        T(title, M, 140, W - 2 * M, 110, 100, "anton", TH["ink"], nowrap=True, mn=48, lh=1.05),
        T(meta, M, 268, W - 2 * M, 36, 26, "oswald", TH["ink"], weight=500, ls=4, upper=True, nowrap=True, mn=18, op=0.6),
        img(grade(src, (1080, 608), contrast=1.05, sat=1.05), 0, 350, W, 608, z=2),
        *sub_label("— " + tag + ("" if tag[-1] in "?!." else "."), 958 - 100),
        T(body, M, 1010, W - 2 * M, 210, 40, "inter", TH["ink"], weight=500, lh=1.4, mn=28),
        *footer(TH, i + 1, n),
    ]}


def build():
    n = 7
    cover = {"bg": TH["bg"], "els": [
        *kicker(TH, "Liste · 5 film", M, 80),
        T("BİTİNCE<br>BAŞA SARDIRAN", M, 150, W - 2 * M, 330, 170, "anton", TH["ink"], nowrap=True, mn=70, lh=1.08),
        img(grade(S("prestige", 3), (1080, 608), contrast=1.05), 0, 520, W, 608, z=2),
        *sub_label("— Spoiler yok.", 1028 - 100),
        T("Kaydet, sırayla izle.", M, 1170, 700, 40, 28, "inter", TH["ink"], weight=500, nowrap=True, op=0.75),
        logo(TH["logo"], W - M - 58, 1252, 58, z=9),
    ]}
    slides = [cover] + [lb_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "SONU SENİ<br>ŞAŞIRTAN FİLM<br>HANGİSİ?", "Yorumlara yaz, ama sonunu anlatma.", "Kaydet · Sırayla izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

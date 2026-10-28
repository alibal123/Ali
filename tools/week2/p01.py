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





def tri_left(x, y, w, h, color="#fff", z=8):
    return box(x, y, w, h, color, z=z, clip="polygon(100% 0,0 50%,100% 100%)")


def rewind_icon(x, y, k=1.0, color="#fff"):
    w, h = int(34 * k), int(40 * k)
    return [tri_left(x, y, w, h, color), tri_left(x + w - 2, y, w, h, color)]


def player_bar(i, n, y=1250):
    tw = W - 2 * M
    fill = int(tw * i / n)
    return [box(M, y, tw, 6, "rgba(255,255,255,.35)", z=8), box(M, y, fill, 6, "#fff", z=9),
            box(M + fill - 11, y - 8, 22, 22, "#fff", z=10, radius=40)]


def pl_film(i, n):
    title, meta, body, src, _, _, tag, _x = FILMS[i]
    return {"bg": "#000", "els": [
        img(grade(src, (1080, 1350), grain=8), 0, 0, W, H, z=1),
        box(0, 480, W, 870, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.8) 62%)", z=2),
        *rewind_icon(M, 78, 0.8),
        T("BAŞA SAR", M + 80, 76, 400, 40, 26, "oswald", "#fff", fit=False, weight=500, ls=6, nowrap=True),
        logo("white", W - M - 58, 64, 58, z=9),
        label(tag, M, 700, bg=TH["accent"], color="#fff", size=22, z=6),
        T(title, M, 790, W - 2 * M, 130, 118, "anton", "#fff", nowrap=True, mn=48, lh=1.05),
        T(meta, M, 940, W - 2 * M, 34, 26, "oswald", "#fff", weight=500, ls=4, upper=True, nowrap=True, mn=18, op=0.8),
        T(body, M, 996, W - 2 * M, 190, 38, "inter", "#fff", weight=500, lh=1.4, mn=26),
        T(f"{i+1:02d} / {n:02d}", M, 1198, 200, 30, 22, "oswald", "#fff", fit=False, weight=500, ls=4, op=0.8),
        *player_bar(i + 1, 5),
    ]}


def build():
    n = 5
    cover = {"bg": "#000", "els": [
        img(grade(S("sixthsense", 2), (1080, 1350), (0.05, 0, 0.95, 1), grain=8), 0, 0, W, H, z=1),
        box(0, 300, W, 1050, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.9) 58%)", z=2),
        logo("white", W - M - 58, 64, 58, z=9),
        *rewind_icon(M, 560, 2.4),
        T("BİTİNCE<br>BAŞA<br>SARDIRAN", M, 700, W - 2 * M, 480, 175, "anton", "#fff", nowrap=True, mn=70, lh=1.06),
        T("5 film · Spoiler yok · Kaydet", M, 1200, 800, 30, 24, "oswald", "#fff", fit=False, weight=500, ls=4, upper=True, nowrap=True, op=0.85),
        *player_bar(0, 5),
    ]}
    slides = [cover] + [pl_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "SONU SENİ<br>ŞAŞIRTAN FİLM<br>HANGİSİ?", "Yorumlara yaz, ama sonunu anlatma.", "Kaydet · Sırayla izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

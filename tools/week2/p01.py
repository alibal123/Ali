from pro import *

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


def build():
    n = 7
    cover = cover_mosaic(TH, [(f[4], f[5]) for f in FILMS], "Liste · 5 film", "BİTİNCE<br>BAŞA SARDIRAN", "Spoiler yok. Kaydet, sırayla izle.")
    slides = [cover] + [film_slide(TH, i + 1, n, f[3], f[0], f[1], f[2], crop=f[7], tag=f[6]) for i, f in enumerate(FILMS)]
    slides.append(cta_slide(TH, "SONU SENİ<br>ŞAŞIRTAN FİLM<br>HANGİSİ?", "Yorumlara yaz, ama sonunu anlatma.", "Kaydet · Sırayla izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

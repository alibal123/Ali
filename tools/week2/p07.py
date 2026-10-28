from pro import *

ID = "2026-11-03_liste_buyuyunce-vuran-animasyon"
PEACH = MINT = LILAC = BUT = SKY = "#fff"
TH = theme("#eaf4ff", "#16213e", "#ffb703", on_acc="#16213e", head="serif", accent_txt="#a86a00")

CAPTION = """Çocukken renkleri için izlemiştin. Büyüyünce konuşmadıkları şeyin ne kadar ağır olduğunu fark ediyorsun. Çocukken izlediğin, büyüyünce başka vuran 5 animasyon.

Up (2009) yaşlı Carl'ın evini balonlarla uçurmasını, Coco (2017) müziği yasak bir ailenin çocuğu Miguel'in Ölüler Günü yolculuğunu, Inside Out (2015) 11 yaşındaki Riley'nin kafasındaki duyguların taşınma telaşını, WALL·E (2008) terk edilmiş Dünya'da çöp toplayan küçük bir robotun aşkını, Your Name (2016) ise birbirinin bedeninde uyanan iki gencin hikâyesini anlatıyor. İlk dördü En İyi Animasyon Oscar'ını aldı.

Sen hangisinde ilk kez gerçekten ağladın?

Yarın 13:00'te: Kadrosuyla gündem olacak 4 yeni film."""


FILMS = [
    ("UP", "2009 · Pete Docter", "Karısını kaybeden yaşlı Carl, evini balonlarla uçurup hayallerinin peşine düşer. İlk dakikalar pek çok kişinin gözünü doldurur.", S("up", 2), S("up", 1), "ilk 10 dakika", PEACH),
    ("COCO", "2017 · Lee Unkrich", "Müziğin yasak olduğu bir ailenin çocuğu Miguel, Ölüler Günü'nde ölüler diyarına geçer. Aile bağını anlatışıyla izleyeni yakalar.", S("coco", 2), S("coco", 1), "aile bağı", BUT),
    ("INSIDE OUT", "2015 · Pete Docter", "11 yaşındaki Riley taşınırken kafasındaki Neşe, Üzüntü, Öfke, Korku ve Tiksinti işbaşı yapar.", S("insideout", 3), S("insideout", 1), "üzülmek serbest", LILAC),
    ("WALL·E", "2008 · Andrew Stanton", "Terk edilmiş Dünya'da çöp toplayan küçük bir robot, EVE'e gönlünü kaptırır. Neredeyse konuşmadan anlatılan bölümleriyle akılda kalır.", S("walle", 1), S("walle", 3), "sessiz ama dolu", MINT),
    ("YOUR NAME", "2016 · Makoto Shinkai", "Kırsaldaki bir kız ile Tokyo'daki bir erkek, bir sabah birbirinin bedeninde uyanır.", S("yourname", 2), S("yourname", 1), "bir sabah", SKY),
]




def build():
    n = 7
    cover = cover_mosaic(TH, [f[4] for f in FILMS], "Animasyon · 5 film", "ÇOCUKKEN İZLEDİN,<br>BÜYÜYÜNCE<br>BAŞKA VURDU", "Kaydet, bu hafta sonu izle.")
    slides = [cover] + [film_slide(TH, i + 1, n, f[3], f[0], f[1], f[2], tag=f[5].capitalize()) for i, f in enumerate(FILMS)]
    slides.append(cta_slide(TH, "HANGİSİNDE<br>İLK KEZ GERÇEKTEN<br>AĞLADIN?", "Yorumlara yaz, itiraf et.", "Kaydet · Ailenle izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

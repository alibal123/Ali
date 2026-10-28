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





def card(src, x, y, w, h, r=40, crop=(0, 0, 1, 1)):
    return img(grade(src, (w, h), crop), x, y, w, h, z=2, radius=r, shadow="0 16px 36px rgba(22,33,62,.18)")


def round_film(i, n):
    title, meta, body, src, _, tag, _bg = FILMS[i]
    return {"bg": TH["bg"], "els": [
        card(src, 56, 56, 968, 700, 48),
        label(tag, 96, 96, bg="rgba(255,255,255,.92)", color=TH["ink"], size=22, z=6),
        T(f"{i+1:02d}", 56, 800, 968, 40, 26, "oswald", "#a86a00", fit=False, weight=500, ls=8, align="center", bleed=True),
        T(title, M, 846, W - 2 * M, 100, 90, "serif", TH["ink"], nowrap=True, mn=44, lh=1.05, align="center"),
        T(meta, M, 958, W - 2 * M, 36, 26, "oswald", TH["ink"], weight=500, ls=4, upper=True, nowrap=True, mn=18, align="center", op=0.65),
        T(body, 130, 1020, W - 260, 200, 38, "inter", TH["ink"], weight=500, lh=1.4, mn=26, align="center"),
        *footer(TH, i + 1, n),
    ]}


def build():
    n = 7
    els = [
        T("Çocukken izledin,<br>büyüyünce başka vurdu", M, 70, W - 2 * M, 250, 96, "serif", TH["ink"], nowrap=True, mn=50, lh=1.12, align="center"),
        card(FILMS[0][4], 56, 360, 968, 560, 48),
    ]
    for k in range(1, 5):
        els.append(card(FILMS[k][4], 56 + (k - 1) * 246, 940, 230, 230, 32))
    els += [T("Animasyon · 5 film · Kaydet", M, 1214, W - 2 * M, 36, 26, "oswald", TH["ink"], weight=500, ls=4, upper=True, nowrap=True, align="center", op=0.65), logo("black", W - M - 58, 1252, 58, z=9)]
    slides = [{"bg": TH["bg"], "els": els}] + [round_film(i, n) for i in range(5)]
    slides.append(cta_slide(TH, "HANGİSİNDE<br>İLK KEZ GERÇEKTEN<br>AĞLADIN?", "Yorumlara yaz, itiraf et.", "Kaydet · Ailenle izle"))
    return {"id": ID, "caption": CAPTION, "slides": slides}

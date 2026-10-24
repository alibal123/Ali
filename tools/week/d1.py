import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from design_kit import *

Y = "#ffe500"; K = "#0b0b0b"; P = "#f4f1e8"

CAPTION = """Akıl sağlığına zararlıdır: izlerken yanında biri olsun diye uyarıyoruz. Bitince bile bir süre kendine gelemeyeceğin 5 film.

Black Swan, mükemmel olmaya takıntılı bir balerinin kendi gölgesiyle yüzleşmesini anlatıyor. Requiem for a Dream, dört insanın hayallerine tutunurken bağımlılığın içine çekilişini. The Machinist bir yıldır uyuyamayan bir adamın çözülen hayatını, Perfect Blue gerçekle hayalin arasındaki çizgiyi kaybeden bir pop yıldızını, Enemy ise kendisinin birebir aynısını gören bir öğretmeni.

Hepsini kaydet, sırayla ve ışıklar açıkken izle. Sen bu listeden hangisini izledin, hangisinden sonra kendine gelemedin?

Yarın 18:00'de: Keanu Reeves'in son sahnede hep aynı seçimi yaptığı 4 film."""


def film_meta(x, y, text, color, w=900, size=36):
    return txt(text, x, y, w, size=size, font="oswald", color=color, weight=500, ls=3, upper=True)


def meter(x, y, n, color, dark=False):
    dots = "●" * n + "○" * (5 - n)
    return [txt("ZARAR DERECESİ", x, y, 330, size=26, font="oswald", color=color, weight=500, ls=4),
            txt(dots, x + 330, y - 4, 300, size=34, font="inter", color=color, ls=6, weight=700)]


def build():
    S = []
    # 1 — KAPAK
    S.append({"bg": K, "els": [
        img(prep("n_blackswan_4", size=(1080, 560), gray=True, contrast=1.25, grain=14), 0, 60, 1080, 560, z=1),
        stripes(0, 0, 1080, 64, Y, "#111", step=30, z=6),
        box(-40, 500, 1160, 700, Y, z=3, rot=-2),
        box(40, 470, 270, 70, K, z=5, rot=-2),
        txt("UYARI", 56, 478, 240, size=56, font="anton", color=Y, ls=6, z=6, rot=-2),
        txt("AKIL<br>SAĞLIĞINA<br>ZARARLIDIR", 62, 565, 980, size=190, font="anton", color=K, lh=1.0, z=5, rot=-2, upper=True),
        txt("İzlerken yanında biri olsun.", 60, 1190, 800, size=54, font="oswald", color="#fff", weight=500),
        txt("5 film · Kaydet", 60, 1262, 600, size=36, font="oswald", color=Y, weight=500, ls=4, upper=True),
        logo("yellow", 900, 1190, 120, z=8),
    ]})
    # 2 — BLACK SWAN (sarı zemin)
    S.append({"bg": Y, "els": [
        txt("01", -30, -150, 900, size=760, font="anton", color=K, lh=1, z=1),
        img(prep("n_blackswan_6", size=(1360, 580), contrast=1.1, grain=10, sat=1.1), -140, 440, 1360, 580, z=3, rot=-3, border="10px solid #111", shadow="0 24px 60px rgba(0,0,0,.35)"),
        box(40, 915, 780, 150, K, z=5, rot=-3),
        txt("BLACK SWAN", 66, 925, 760, size=126, font="anton", color=Y, z=6, rot=-3, lh=1.05),
        film_meta(70, 1075, "2010 · Darren Aronofsky", K),
        txt("Mükemmel olmaya takıntılı bir balerin, Kuğu Gölü'nün başrolünü alınca kendi gölgesiyle yüzleşmeye başlar.", 70, 1128, 940, size=35, weight=600, color=K, lh=1.28),
        box(745, 70, 270, 270, K, z=4, radius=200, rot=8),
        txt("OSCAR<br><span style='font-size:24px;letter-spacing:1px'>EN İYİ KADIN<br>OYUNCU</span>", 755, 105, 250, size=64, font="anton", color=Y, align="center", z=6, rot=8, lh=1.05),
        *meter(70, 1285, 4, K), logo("black", 930, 1262, 80, z=8),
    ]})
    # 3 — REQUIEM (sarı-siyah çift ton, tam sayfa)
    S.append({"bg": K, "els": [
        img(prep("n_requiem_4", crop=(0.26, 0, 0.76, 1), size=(1080, 1350), duo=("#0a0a0a", Y), contrast=1.15, grain=22), 0, 0, 1080, 1350, z=1),
        txt("02", 40, 10, 500, size=330, font="anton", color="transparent", stroke="7px #0b0b0b", z=4, lh=1),
        box(720, 120, 300, 130, K, z=4, rot=6),
        txt("OSCAR ADAYI<br><span style='color:#fff'>ELLEN BURSTYN</span>", 735, 140, 275, size=40, font="anton", color=Y, align="center", z=6, rot=6, lh=1.15),
        box(0, 820, 1080, 530, K, z=3),
        stripes(0, 806, 1080, 26, Y, K, step=22, z=4),
        txt("REQUIEM<br>FOR A DREAM", 58, 850, 980, size=118, font="anton", color=Y, lh=.98, z=5),
        film_meta(62, 1095, "2000 · Darren Aronofsky", "#fff"),
        txt("Dört insan, kendi hayallerine tutunmak için farklı bağımlılıkların içine çekilir.", 62, 1150, 940, size=38, weight=500, color="#fff", lh=1.3),
        *meter(62, 1290, 5, Y), logo("yellow", 930, 1262, 80, z=8),
    ]})
    # 4 — THE MACHINIST (kırık beyaz zemin, kolaj)
    pol = "12px solid #fff"
    S.append({"bg": P, "els": [
        txt("THE<br>MACHINIST", 52, 30, 980, size=212, font="anton", color=K, lh=.88, z=2),
        txt("03", 720, 300, 360, size=190, font="anton", color=Y, stroke="5px #0b0b0b", z=1, lh=1, align="right"),
        img(prep("n_machinist_1", size=(1240, 660), contrast=1.2, grain=10), 30, 500, 640, 340, z=3, rot=-6, border=pol, shadow="0 18px 40px rgba(0,0,0,.35)"),
        img(prep("n_machinist_6", size=(1240, 660), contrast=1.15, grain=10), 410, 640, 640, 340, z=4, rot=5, border=pol, shadow="0 18px 40px rgba(0,0,0,.35)"),
        img(prep("n_machinist_2", size=(1240, 660), contrast=1.15, grain=10), 60, 840, 560, 300, z=5, rot=-2, border=pol, shadow="0 18px 40px rgba(0,0,0,.35)"),
        box(800, 420, 210, 210, Y, z=6, radius=200, rot=10, border="6px solid #0b0b0b"),
        txt("~28 KG<br><span style='font-size:30px'>VERDİ</span>", 805, 465, 200, size=54, font="anton", color=K, align="center", z=7, rot=10, lh=1.0),
        film_meta(640, 1060, "2004 · Brad Anderson", K, w=420, size=28),
        txt("Bir yıldır uyuyamayan makinistin hayatı, işyerinde tanımadığı biri belirince çözülür.", 60, 1170, 960, size=37, weight=600, color=K, lh=1.28, z=5),
        *meter(60, 1297, 4, K), logo("black", 940, 1272, 74, z=8),
    ]})
    # 5 — PERFECT BLUE (kırmızı, tam sayfa)
    S.append({"bg": K, "els": [
        img(prep("n_perfectblue_6", crop=(0.28, 0, 0.8, 1), size=(1080, 1350), contrast=1.12, sat=1.2, grain=14), 0, 0, 1080, 1350, z=1),
        box(0, 900, 1080, 450, "linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.92) 45%,#000)", z=2),
        txt("04", 50, 40, 400, size=300, font="anton", color="transparent", stroke="6px #fff", z=4, lh=1),
        box(-60, 690, 1200, 170, Y, z=4, rot=-6),
        txt("PERFECT BLUE", -20, 700, 1120, size=152, font="anton", color=K, align="center", z=5, rot=-6, lh=1),
        box(-60, 880, 1200, 66, K, z=4, rot=-6),
        txt("SATOSHI KON · 1997", -20, 887, 1120, size=34, font="oswald", color=Y, weight=500, ls=8, align="center", z=5, rot=-6),
        txt("Pop grubunu bırakıp oyunculuğa geçen Mima'nın gerçekle hayal arasındaki çizgisi silinir.", 62, 1075, 940, size=38, weight=500, color="#fff", lh=1.3, z=5),
        txt("Satoshi Kon'un ilk uzun metrajı.", 62, 1215, 900, size=30, font="oswald", color=Y, weight=500, ls=3, z=5),
        *meter(62, 1290, 4, "#fff"), logo("white", 930, 1262, 80, z=8),
    ]})
    # 6 — ENEMY (ikiz yansıma)
    S.append({"bg": Y, "els": [
        img(prep("n_enemy_5", crop=(0.35, 0, 0.75, 1), size=(540, 700), contrast=1.15, grain=10), 0, 0, 540, 700, z=1),
        img(prep("n_enemy_5", crop=(0.35, 0, 0.75, 1), size=(540, 700), contrast=1.15, grain=10, flip=True), 540, 0, 540, 700, z=1),
        box(536, 0, 8, 700, K, z=3),
        txt("05", 40, 20, 300, size=200, font="anton", color="transparent", stroke="5px #fff", z=4),
        txt("ENEMY", 40, 610, 1000, size=240, font="anton", color=K, z=5, lh=1),
        film_meta(50, 860, "2013 · Denis Villeneuve", K),
        txt("Sıradan bir tarih öğretmeni, bir filmde kendisinin birebir aynısını görünce onun peşine düşer.", 50, 925, 960, size=40, weight=700, color=K, lh=1.28),
        txt("José Saramago'nun romanından uyarlandı. Jake Gyllenhaal iki rolü birden oynuyor.", 50, 1085, 940, size=32, weight=500, color=K, lh=1.3, op=.85),
        *meter(50, 1290, 4, K), logo("black", 930, 1262, 80, z=8),
    ]})
    # 7 — KAPANIŞ
    S.append({"bg": Y, "els": [
        stripes(0, 0, 1080, 70, Y, K, step=30), stripes(0, 1280, 1080, 70, Y, K, step=30),
        txt("ZARAR<br>RAPORUNU<br>YORUMLARA<br>YAZ", 60, 120, 980, size=205, font="anton", color=K, lh=.92),
        txt("Hangisinden sonra bir hafta kendine gelemedin?", 64, 880, 900, size=58, font="playfair", color=K, weight=700, lh=1.2),
        txt("KAYDET · ARKADAŞINA GÖNDER · YORUM YAP", 64, 1100, 960, size=32, font="oswald", color=K, weight=500, ls=4),
        logo("black", 760, 1010, 240, z=8),
    ]})
    return {"id": "2026-10-25_liste_akil-sagligina-zararlidir", "caption": CAPTION, "slides": S}


if __name__ == "__main__":
    import render2
    render2.render(build())

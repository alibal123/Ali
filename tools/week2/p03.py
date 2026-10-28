from pro import *

ID = "2026-10-31_liste_cadilar-bayrami-5-film"
INK, TEAL, CRM, ORG = "#24163a", "#0f3b3a", "#f6ecd6", "#ff8a2a"
TH = theme(TEAL, CRM, ORG, on_acc=TEAL, head="anton", accent_txt=ORG, logo_light="white")
LOGO = dict(pos="bc", w=84, on_light="black", on_dark="yellow")

CAPTION = """Cumartesi gecesi evde kalanlar kulübü: Cadılar Bayramı'nı kutlamıyorsun ama bir film açmak istiyorsun. Kan yok, gerilim yok; sevimli hayaletler, komik cadılar ve tuhaf dünyalar. Ürkütmeyen 5 film.

Beetlejuice (1988) hayaletlere yardım eden çılgın bir "biyo-egzorsist"i, Hocus Pocus (1993) yüzyıllar sonra dirilen üç cadı kardeşi, Coraline (2009) gizli bir kapının ardındaki "öteki" dünyayı, The Nightmare Before Christmas (1993) Cadılar Bayramı Şehri'nin kralı Jack'in Noel merakını, Casper (1995) ise dost canlısı bir hayaletin hikâyesini anlatıyor.

Bu akşam hangisini açıyorsun?

Yarın 13:00'te: Dunesday, yani 18 Aralık'ta aynı gün vizyona girecek iki dev film."""

FILMS = [
    ("BEETLEJUICE", "1988 · Tim Burton", "Hayalet olan çift evlerini yeni sahiplerinden kurtarmak için çılgın bir biyo-egzorsistten medet umar. Oscar'ı En İyi Makyaj dalında aldı.", S("beetlejuice", 1), S("beetlejuice", 2), "Çılgın"),
    ("HOCUS POCUS", "1993 · Kenny Ortega", "Salem'de üç cadı kardeş, yüzyıllar sonra bir Cadılar Bayramı gecesi geri döner. Bette Midler, Sarah Jessica Parker ve Kathy Najimy üçlüsü kült oldu.", S("hocuspocus", 2), S("hocuspocus", 1), "Kült"),
    ("CORALINE", "2009 · Henry Selick", "Yeni evlerindeki küçük bir kapıdan, her şeyin daha iyi göründüğü bir dünyaya geçen kızın stop-motion macerası.", S("coraline", 3), S("coraline", 2), "Kapıyı aç"),
    ("THE NIGHTMARE BEFORE CHRISTMAS", "1993 · Henry Selick", "Cadılar Bayramı Şehri'nin kralı Jack Skellington, Noel'i keşfedince her şeyi değiştirmek ister.", S("nightmare", 3), S("nightmare", 1), "Şarkılı"),
    ("CASPER", "1995 · Brad Silberling", "Dost canlısı küçük bir hayaletle genç bir kızın arkadaşlığı. Christina Ricci'nin başrolde olduğu bu film aileyle izlenir.", S("casper", 1), S("casper", 2), "Aileyle izle"),
]




import cut
from PIL import Image, ImageFilter, ImageChops
import os

CUTS = ["beetlejuice_2", "hocuspocus_1", "coraline_3", "nightmare_3", "casper_1"]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets", "cutouts")


def sticker(name, maxw, maxh, pad=26):
    path = os.path.join(OUT, f"st_{name}_{maxw}x{maxh}.png")
    im = cut.cutout(name).convert("RGBA")
    im = im.crop(im.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox())
    r = min(maxw / im.width, maxh / im.height)
    im = im.resize((max(1, int(im.width * r)), max(1, int(im.height * r))), Image.LANCZOS)
    cw, ch = im.width + pad * 4, im.height + pad * 4
    a = Image.new("L", (cw, ch), 0)
    a.paste(im.getchannel("A"), (pad * 2, pad * 2))
    d = a
    for _ in range(pad // 4 + 1):
        d = d.filter(ImageFilter.MaxFilter(9))
    d = d.point(lambda v: 255 if v > 100 else 0).filter(ImageFilter.GaussianBlur(1.2))
    sh = d.filter(ImageFilter.GaussianBlur(14))
    out = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (cw, ch), (36, 22, 58, 0))
    shadow.putalpha(sh.point(lambda v: int(v * 0.35)))
    out.alpha_composite(shadow, (0, 12))
    white = Image.new("RGBA", (cw, ch), (255, 255, 255, 255)); white.putalpha(d)
    out.alpha_composite(white)
    layer = Image.new("RGBA", (cw, ch), (0, 0, 0, 0)); layer.paste(im, (pad * 2, pad * 2))
    out.alpha_composite(layer)
    out.save(path)
    return path, cw, ch


def stk(name, cx, cy, maxw, maxh, rot=0, z=5):
    p, w, h = sticker(name, maxw, maxh)
    return img(p, cx - w // 2, cy - h // 2, w, h, z=z, fit="contain", rot=rot)


def film(i, n):
    title, meta, body, _s, _s2, tag = FILMS[i]
    rots = [-4, 3, -3, 4, -3]
    sizes = [(700, 620), (880, 560), (420, 640), (760, 600), (820, 560)]
    sw, sh = sizes[i]
    return {"bg": TEAL, "els": [
        box(540 - 330, 90, 660, 660, ORG, z=2, radius=700),
        T(f"{i+1:02d}", M, 56, 200, 90, 80, "anton", CRM, fit=False, lh=1.0, nowrap=True, z=8),
        label(tag.upper(), W - M - 340, 70, bg=CRM, color=TEAL, size=22, z=8),
        stk(CUTS[i], 540, 430, sw, sh, rot=rots[i]),
        T(title, M, 800, W - 2 * M, 130, 104, "anton", CRM, nowrap=True, mn=44, lh=1.12, align="center", z=6),
        T(meta, M, 940, W - 2 * M, 34, 26, "oswald", ORG, weight=500, ls=5, upper=True, nowrap=True, mn=16, align="center"),
        T(body, 110, 996, W - 220, 190, 36, "inter", CRM, weight=500, lh=1.38, mn=26, align="center"),
        T(f"{i+2} / {n}", M, 1284, 200, 34, 22, "oswald", CRM, fit=False, weight=500, ls=4, op=0.6),
    ]}


def build():
    n = 7
    els = [
        box(220, 640, 860, 860, ORG, z=1, radius=1000),
        T("CUMARTESİ GECESİ<br>EVDE KALANLAR<br>KULÜBÜ", M, 80, W - 2 * M, 470, 140, "anton", CRM, nowrap=True, mn=70, lh=1.14, z=3),
        T("CADILAR BAYRAMI İÇİN ÜRKÜTMEYEN 5 FİLM", M, 600, 900, 34, 24, "oswald", ORG, fit=False, weight=500, ls=5, upper=True, nowrap=True, z=3),
        stk("casper_1", 830, 900, 440, 340, rot=5, z=4),
        stk("hocuspocus_1", 440, 1000, 620, 430, rot=-4, z=6),
        stk("coraline_3", 150, 920, 190, 360, rot=-6, z=5),
        stk("beetlejuice_2", 840, 1090, 360, 400, rot=6, z=7),
        stk("nightmare_3", 170, 1170, 220, 200, rot=-4, z=8),
    ]
    cover = {"bg": TEAL, "els": els}
    slides = [cover] + [film(i, n) for i in range(5)]
    slides.append({"bg": ORG, "els": [
        T("BU CUMARTESİ<br>HANGİSİNİ<br>AÇIYORSUN?", M, 110, W - 2 * M, 520, 130, "anton", TEAL, nowrap=True, mn=60, lh=1.14),
        T("Yorumlara yaz, battaniyeyi çek.", M, 700, W - 2 * M, 50, 36, "inter", TEAL, weight=600, nowrap=True),
        label("Kaydet · Cumartesiye sakla", M, 790, bg=TEAL, color=CRM, size=24),
    ]})
    return {"id": ID, "caption": CAPTION, "slides": slides}

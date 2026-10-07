from studio import img, GRAIN

ID = "2026-10-20_liste_hayati-sorgulatan"
FONTS = ["archivo-black/400.css", "inter-tight/500.css", "inter-tight/600.css", "inter-tight/700.css"]

MALK, MALK2, RED, RED2 = img("up_malkovich_01.jpg"), img("up_malkovich_11.jpg"), img("fg_red_07.jpg"), img("fg_red_02.jpg")

CSS = f"""
:root{{--paper:#f1eee6;--ink:#111;--red:#e2321b}}
body{{background:var(--paper);color:var(--ink);font-family:'Inter Tight',sans-serif}}
.pp{{position:absolute;inset:0;background:var(--paper)}}
.pp::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.12;mix-blend-mode:multiply}}
.grid{{position:absolute;inset:60px;border-top:3px solid var(--ink)}}
.lbl{{font:700 22px/1.2 'Inter Tight';letter-spacing:.04em;text-transform:uppercase}}
.num{{font:400 420px/0.78 'Archivo Black';letter-spacing:-.04em}}
h1{{font:400 118px/0.9 'Archivo Black';letter-spacing:-.03em}}
h2{{font:400 74px/0.95 'Archivo Black';letter-spacing:-.02em}}
.q{{font:700 62px/1.08 'Inter Tight';letter-spacing:-.01em}}
p{{font:500 37px/1.35 'Inter Tight'}}
.shape{{position:absolute;background-size:cover;background-position:center}}
"""


def head(left, right):
    return f"<div style='position:absolute;left:60px;right:60px;top:78px;display:flex;justify-content:space-between' class='lbl'><span lang='en'>{left}</span><span>{right}</span></div>"


S1 = f"""<div class='slide'><div class='pp'></div><div class='grid'></div>{head('derecefilm / liste', '5 film')}
<div class='shape' style='right:-140px;top:300px;width:760px;height:760px;border-radius:50%;background:var(--red)'></div>
<div style='position:absolute;left:60px;top:180px;width:860px'><h1>Size hayatı sorgulatacak 5 film</h1></div>
<div style='position:absolute;left:60px;bottom:90px;width:520px'><p>Bittikten sonra kalkıp gitmeyeceğin, saatlerce tavana bakacağın filmler. Her biri tek bir soru bırakıyor.</p></div>
<div class='lbl' style='position:absolute;right:60px;bottom:90px;text-align:right'>Kaydır →</div>
</div>"""


def film(n, title, meta, premise, q, shape, flip=False):
    side = "right:60px" if not flip else "left:60px"
    other = "left:60px" if not flip else "right:60px"
    return f"""<div class='slide'><div class='pp'></div><div class='grid'></div>{head(meta, f'{n} / 5')}
<div class='num' style='position:absolute;{other};top:150px'>{n}</div>
{shape}
<div style='position:absolute;left:60px;right:60px;top:690px'>
 <h2 lang='en'>{title}</h2>
 <p style='margin-top:22px;max-width:900px'>{premise}</p>
 <div style='margin-top:40px;border-top:3px solid var(--ink);padding-top:26px' class='q'>{q}</div>
</div></div>"""


S2 = film(1, "Being John Malkovich", "Spike Jonze · 1999",
          "Bir ofis katındaki küçük bir kapı, on beş dakikalığına başka bir insanın zihnine açılıyor. Herkes sıraya giriyor.",
          "Başka biri olabilseydin, <span style='color:var(--red)'>gerçekten</span> mutlu olur muydun?",
          f"<div class='shape' style='right:60px;top:170px;width:420px;height:470px;background-image:url(\"{MALK}\");background-position:30% 50%;filter:brightness(1.6)'></div>")
S3 = film(2, "Three Colours: Red", "Krzysztof Kieślowski · 1994",
          "Genç bir model, komşularının telefonlarını gizlice dinleyen emekli bir yargıçla tanışır. Aralarındaki konuşmalar hayatlarını değiştirir.",
          "Tesadüf diye bir şey var mı, yoksa her şey <span style='color:var(--red)'>birbirine bağlı</span> mı?",
          f"<div class='shape' style='right:60px;top:170px;width:470px;height:470px;border-radius:50%;background-image:url(\"{RED}\");background-position:62% 50%'></div>")
S4 = film(3, "The Life of David Gale", "Alan Parker · 2003",
          "İdam cezasına karşı mücadele eden bir profesör, bir cinayetten idama mahkûm olur. Son günlerinde bir gazeteciye hikâyesini anlatır.",
          "Bir fikri savunmak için <span style='color:var(--red)'>ne kadar</span> ileri gidilebilir?",
          "<div class='shape' style='right:60px;top:170px;width:470px;height:470px;background:var(--ink)'></div><div class='shape' style='right:60px;top:170px;width:470px;height:470px;background:linear-gradient(45deg,transparent 49.6%,var(--paper) 49.6% 50.4%,transparent 50.4%)'></div>")
S5 = film(4, "Meet Joe Black", "Martin Brest · 1998",
          "Ölüm, bir insan bedenine girip zengin bir iş insanının yanında birkaç gün geçirmeye karar verir. Karşılığında adama biraz zaman tanır.",
          "Son günlerini bilseydin, <span style='color:var(--red)'>neyi</span> değiştirirdin?",
          "<div class='shape' style='right:60px;top:170px;width:470px;height:470px;border-radius:50%;border:56px solid var(--ink)'></div><div class='shape' style='right:255px;top:365px;width:80px;height:80px;border-radius:50%;background:var(--red)'></div>")
S6 = film(5, "When Nietzsche Wept", "Pinchas Perry · 2007",
          "Irvin Yalom'un romanından. Ünlü hekim Josef Breuer, umutsuzluk içindeki genç Nietzsche'yi tedavi etmeye çalışır. Kimin kimi iyileştirdiği belirsizleşir.",
          "Acı bizi büyütür mü, yoksa yalnızca <span style='color:var(--red)'>yorar</span> mı?",
          "<div class='shape' style='right:60px;top:170px;width:470px;height:470px;background:var(--red);clip-path:polygon(50% 0,100% 100%,0 100%)'></div>")

S7 = f"""<div class='slide'><div class='pp'></div><div class='grid'></div>{head('derecefilm / liste', 'son')}
<div class='shape' style='left:60px;right:60px;top:160px;height:520px;background-image:url("{RED2}");background-position:50% 40%'></div>
<div style='position:absolute;left:60px;right:60px;top:740px'>
 <h2>Hangisi sana en zor soruyu sordu?</h2>
 <p style='margin-top:30px'>Listede olmayan ama seni sarsan bir film varsa yorumlara yaz. Bir sonraki listeyi sizin önerilerinizle kuralım.</p>
 <div class='lbl' style='margin-top:50px;color:var(--red)'>Kaydet, sonra izle.</div>
</div></div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7]

CAPTION = """
Size hayatı sorgulatacak 5 film: Being John Malkovich (1999), Three Colours: Red (1994), The Life of David Gale (2003), Meet Joe Black (1998) ve When Nietzsche Wept (2007). Bittikten sonra kalkıp gidemeyeceğin, saatlerce tavana bakacağın filmler.

Biri başka bir insanın zihnine açılan küçük bir kapıyla, biri komşularını dinleyen yaşlı bir yargıçla, biri idam cezasına karşı çıkarken idama mahkûm olan bir profesörle başlıyor. Ölüm bir insan bedeninde tatile çıkıyor, Nietzsche ise bir hekimin divanına uzanıyor.

Her biri tek bir soru bırakıyor: Kim olmak isterdin, tesadüf var mı, bir fikir için ne kadar ileri gidilir, son günlerinde neyi değiştirirdin, acı seni büyütür mü? Hangisi sana en zor soruyu sordu?

Yarın 20:00'de: Kolera Sokağı'na hoş geldin. 90'ların en cesur Türk filmlerinden biri.
"""

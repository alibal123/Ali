from studio import img, GRAIN

ID = "2026-10-12_kultur_kavusamayan-asiklar"
FONTS = ["cormorant-garamond/500.css", "cormorant-garamond/600.css", "cormorant-garamond/500-italic.css",
         "cormorant-garamond/600-italic.css", "eb-garamond/400.css", "eb-garamond/400-italic.css", "eb-garamond/600.css"]

EBRU, MINI, HEADON = img("ai_01.jpg"), img("ai_00.jpg"), img("headon_1.jpg")
KEREM, EZEL = img("ai_24.jpg"), img("ai_25.jpg")

CSS = f"""
:root{{--ink:#2a1d14;--paper:#efe3c8;--lapis:#1f3a7a;--red:#a8322a;--gold:#b08a3c}}
body{{background:#1b1430;font-family:'EB Garamond',serif;color:var(--ink)}}
.ebru{{position:absolute;inset:0;background:url('{EBRU}') center/135% auto}}
.ebru.dim::after{{content:'';position:absolute;inset:0;background:rgba(20,12,30,.18)}}
.paper{{position:absolute;background:var(--paper);box-shadow:0 30px 60px rgba(0,0,0,.45);
  background-image:radial-gradient(ellipse at 30% 20%,rgba(255,255,255,.35),transparent 60%),radial-gradient(ellipse at 80% 90%,rgba(120,80,30,.18),transparent 55%)}}
.paper::before{{content:'';position:absolute;inset:22px;border:2px solid var(--gold);outline:1px solid var(--gold);outline-offset:6px;pointer-events:none}}
.paper::after{{content:'';position:absolute;inset:0;background:url("{GRAIN}");opacity:.10;mix-blend-mode:multiply;pointer-events:none}}
.kick{{font:600 26px/1 'EB Garamond';letter-spacing:.32em;color:var(--red);text-transform:uppercase}}
.no{{font:500 italic 30px 'Cormorant Garamond';color:var(--gold)}}
.rule{{display:flex;align-items:center;gap:18px;color:var(--gold);font-size:28px}}
.rule::before,.rule::after{{content:'';flex:1;height:1px;background:var(--gold)}}
h1{{font:600 italic 132px/0.92 'Cormorant Garamond';color:var(--lapis);letter-spacing:-.01em}}
h2{{font:600 italic 104px/0.95 'Cormorant Garamond';color:var(--lapis)}}
h2 .ile{{font-size:.5em;color:var(--red);font-style:italic;margin:0 14px}}
p{{font:400 38px/1.42 'EB Garamond';}}
p i{{color:var(--red)}}
.facts{{display:grid;grid-template-columns:190px 1fr;row-gap:20px;column-gap:20px;font:400 34px/1.32 'EB Garamond'}}
.facts b{{font:600 22px/1.5 'EB Garamond';letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}}
.mini{{position:absolute;background:url('{MINI}') center/cover;box-shadow:0 0 0 2px var(--gold),0 0 0 10px var(--paper),0 0 0 12px var(--gold)}}
.sig{{position:absolute;bottom:44px;left:0;right:0;text-align:center;font:500 italic 24px 'Cormorant Garamond';color:rgba(255,255,255,.85);letter-spacing:.1em}}
"""

S1 = f"""<div class='slide'><div class='ebru'></div>
<div class='paper' style='left:90px;top:90px;right:90px;bottom:120px'>
 <div class='mini' style='left:150px;right:150px;top:110px;height:520px;background-position:center 40%'></div>
 <div style='position:absolute;left:80px;right:80px;top:680px;text-align:center'>
  <div class='kick'>Kültür Kodları · I</div>
  <h1 style='margin-top:26px'>Kavuşamayan<br>Âşıklar</h1>
  <div class='rule' style='margin:30px 120px 0'>❦</div>
  <p style='margin-top:18px;font-style:italic;font-size:32px'>Leyla’dan Sibel’e: bu topraklarda aşk neden hep yarım kalır?</p>
 </div></div>
<div class='sig'>derecefilm</div></div>"""

S2 = f"""<div class='slide'><div class='ebru dim'></div>
<div class='paper' style='left:130px;top:170px;right:130px;bottom:170px'>
 <div data-fit style='position:absolute;left:90px;right:90px;top:110px;bottom:100px'>
  <div class='no'>Önsöz</div>
  <p style='margin-top:26px;font-size:46px'>Bizim hikâyelerimizde âşıklar birbirini bulur, ama <i>birbirine varamaz.</i></p>
  <p style='margin-top:26px'>Arada bazen bir baba, bazen bir dağ, bazen de bir hapishane duvarı vardır. Yüzyıllar geçer; mesnevi diziye, destan filme dönüşür. Ama kural değişmez.</p>
  <p style='margin-top:26px'>Kaydır: dört çift, dört engel, tek bir kader.</p>
  <div class='rule' style='margin-top:40px'>✦</div>
 </div></div></div>"""


def couple(no, a, b, src, facts, note, crop=None, tone=""):
    pic = ""
    if crop:
        pic = f"<div class='mini' style='left:90px;right:90px;top:90px;height:330px;background:url(\"{crop[0]}\") {crop[1]}/cover'></div>"
    top = 470 if crop else 120
    rows = "".join(f"<b>{k}</b><span>{v}</span>" for k, v in facts)
    return f"""<div class='slide'><div class='ebru' style='filter:{tone}'></div>
<div class='paper' style='left:80px;top:80px;right:80px;bottom:80px'>
 {pic}
 <div data-fit style='position:absolute;left:90px;right:90px;top:{top}px;bottom:80px'>
  <div class='no'>{no} · <span style='font-style:normal;letter-spacing:.2em;font-size:22px;text-transform:uppercase'>{src}</span></div>
  <h2 style='margin-top:14px'>{a}<span class='ile'>ile</span>{b}</h2>
  <div class='facts' style='margin-top:34px'>{rows}</div>
  <p style='margin-top:30px;font-style:italic;font-size:34px;color:#5a4330'>{note}</p>
 </div></div></div>"""


S3 = couple("I", "Leyla", "Mecnun", "Arap efsanesi · Fuzûlî, 16. yüzyıl",
            [("Engel", "Leyla’nın babası. Kızını “deli” diye anılan Kays’a vermez, başkasıyla evlendirir."),
             ("Son", "Leyla hasretle ölür; Mecnun onun mezarı başında can verir.")],
            "Kays, aşkından çöle düşünce adı “Mecnun” olur: deli. Fuzûlî’de aşk bir insandan Tanrı’ya uzanan bir yola dönüşür.",
            crop=(MINI, "center 70%"))
S4 = couple("II", "Kerem", "Aslı", "Anadolu halk hikâyesi",
            [("Engel", "Aslı’nın babası Keşiş. Kızını alıp diyar diyar kaçar."),
             ("Son", "Gerdek gecesi Aslı’nın sihirli entarisinin düğmeleri açılmaz. Kerem’in “ah”ı ateş olur, kendini yakar; külünü süpüren Aslı’yı da alev sarar.")],
            "Kerem yanar, Aslı da onunla yanar. Türkçedeki “Kerem gibi yanmak” deyimi buradan gelir.", crop=(KEREM, "center 45%"), tone="hue-rotate(-25deg) saturate(1.2)")
S5 = couple("III", "Ezel", "Eyşan", "Televizyon dizisi · 2009–2011",
            [("Engel", "İhanet. Ömer’i en yakın dostları ve sevdiği kadın hapse yollar."),
             ("Dönüş", "Ömer yeni bir yüzle, Ezel adıyla geri gelir. İntikam ile aşk aynı masaya oturur.")],
            "Yüzü değişse de kalbi değişmeyen bir adam: modern zamanların Mecnun’u bir intikam dizisinden çıktı.", crop=(EZEL, "center 40%"), tone="hue-rotate(20deg)")
S6 = couple("IV", "Cahit", "Sibel", "Duvara Karşı · Fatih Akın, 2004",
            [("Engel", "Bir hapishane duvarı ve geçen yıllar."),
             ("Son", "Cahit çıktığında Sibel’in yeni bir hayatı vardır. Otobüs Mersin’e tek kişiyle gider.")],
            "Sahte bir evlilik olarak başlayan ilişki, ikisinin de hayatındaki en gerçek şeye dönüşür.",
            crop=(HEADON, "center 35%"))

S7 = f"""<div class='slide'><div class='ebru'></div>
<div class='paper' style='left:110px;top:200px;right:110px;bottom:200px'>
 <div data-fit style='position:absolute;left:90px;right:90px;top:100px;bottom:90px;text-align:center'>
  <div class='kick'>Peki neden?</div>
  <p style='margin-top:34px;font-size:40px;font-style:italic;color:var(--lapis)'>Çünkü kavuşmak hikâyeyi bitirir. Ayrılık ise aşkı sonsuz kılar.</p>
  <div class='rule' style='margin:44px 80px'>❦</div>
  <p>Listeye kim eklenmeli?<br><i>Ferhat ile Şirin</i> mi, <i>Tahir ile Zühre</i> mi, yoksa senin aklındaki bir film çifti mi?</p>
  <p style='margin-top:30px;font-size:28px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)'>Yorumlara yaz</p>
 </div></div></div>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7]

CAPTION = """
Kavuşamayan Âşıklar: Leyla ile Mecnun, Kerem ile Aslı, Ezel ile Eyşan, Cahit ile Sibel. Bu toprakların aşk hikâyelerinde âşıklar birbirini bulur ama birbirine varamaz. Arada bazen bir baba, bazen bir duvar, bazen de bir ihanet vardır.

Fuzûlî’nin mesnevisinden halk hikâyelerine, Ezel dizisinden Fatih Akın’ın Duvara Karşı’sına kadar kural pek değişmiyor. Mecnun çölde, Kerem ateşte, Ezel yeni bir yüzde, Cahit Mersin otobüsünde yalnız kalıyor.

Belki de sebebi şu: Kavuşmak hikâyeyi bitirir, ayrılık ise aşkı sonsuz kılar. Sence bu listeye hangi çift eklenmeli?

Yarın 20:00'de: Unutkan bir balık ile dövmelerle hatırlamaya çalışan bir adam. Dori ile Memento aynı şeyi mi anlatıyor?
"""

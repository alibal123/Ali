"""Kişiselleştirilmiş liste serisi — 10 gönderinin tamamı (kapak + 5 film + son slayt + açıklama).
Kullanım: python3 tools/seri3/gonderi.py [1 2 ...]   → posts/<id>/01..07.jpg + caption.txt"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import kapak2, kapak3, kapak4, kapak7
from kapak2 import page, P, LOGO, EN
from playwright.sync_api import sync_playwright


def film_slide(still, pos, n, title, meta, desc, acc, filt=""):
    return page(f"""
<div class="bg" style="background-image:url({P(still)});background-position:{pos};{filt}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(8,8,10,.35) 0%,rgba(8,8,10,0) 22%,rgba(8,8,10,0) 42%,rgba(8,8,10,.93) 70%)"></div>
<div class="abs" style="left:64px;top:56px;font:400 120px/1 Anton;color:{acc}">{n:02d}</div>
<div class="abs" style="left:64px;right:64px;top:860px">
  <div style="font:400 84px/1.0 Anton;color:#fff;text-transform:uppercase"><span lang="en">{title}</span></div>
  <div class="osw" lang="en" style="font-size:24px;color:{acc};margin-top:16px">{meta}</div>
  <div style="font:500 34px/1.4 Inter;color:#f1f1f1;margin-top:22px">{desc}</div>
</div>
<img class="logo" src="{LOGO}/white.png">
""", "#0a0a0c")


def cta_slide(q, sub, bg, ink, acc, logo="white"):
    return page(f"""
<div class="abs" style="inset:0;background:{bg}"></div>
<div class="abs" style="left:64px;top:150px;width:60px;height:6px;background:{acc}"></div>
<div class="abs" style="left:64px;right:64px;top:200px;font:400 128px/1.02 Anton;color:{ink};text-transform:uppercase">{q}</div>
<div class="abs" style="left:64px;right:64px;top:900px;font:500 40px/1.35 Inter;color:{ink};opacity:.85">{sub}</div>
<div class="abs osw" style="left:64px;top:1110px;font-size:24px;color:{bg};background:{acc};padding:12px 22px">Kaydet · Arkadaşına gönder</div>
<img class="logo" src="{LOGO}/{logo}.png">
""", bg)


POSTS = [
 dict(id="2026-11-07_liste_situationship", date="2026-11-07", cover=kapak2.c1, acc="#ffd36b",
  films=[("pastlives_2", "50% 40%", "Past Lives", "2023 · Celine Song", "Çocukluk aşkı yirmi dört yıl sonra New York'ta karşısına çıkar. Söylenmeyen her cümlenin ağırlığını taşıyan bir film."),
         ("500days_2", "50% 40%", "(500) Days of Summer", "2009 · Marc Webb", "Tom bir ilişki yaşadığını sanır, Summer ise en baştan ciddi bir şey istemediğini söylemiştir. Etiketsiz ilişkinin en bilinen hikâyesi."),
         ("beforesunrise_1", "50% 40%", "Before Sunrise", "1995 · Richard Linklater", "Trende tanışan iki yabancı Viyana'da tek bir gece geçirir. Ne olduklarını sormadan, sadece konuşarak."),
         ("lostintrans_1", "70% 40%", "Lost in Translation", "2003 · Sofia Coppola", "Tokyo'da bir otelde yolları kesişen iki yalnız insan. Adı konmamış bir yakınlığın en zarif hâli."),
         ("likecrazy_1", "40% 40%", "Like Crazy", "2011 · Drake Doremus", "Vize yüzünden ayrı düşen iki genç, mesafeye rağmen ne olduklarını çözmeye çalışır.")],
  q="Sen hiç<br>“biz neyiz”<br>diye sordun mu?", sub="Cevabını yorumlara yaz. Soramayan arkadaşını etiketle.", bg="#101528", ink="#fff",
  hook="Üç aydır görüşüyorsunuz ama hâlâ “biz neyiz” diye soramadın mı?",
  intro="Adı konmamış ilişkileri en iyi anlatan 5 film:",
  ask="Sen hiç “biz neyiz” diye sorabildin mi?"),

 dict(id="2026-11-09_liste_ghostlanma", date="2026-11-09", cover=kapak4.g1, acc="#ff7eb0",
  films=[("eternal_1", "40% 40%", "Eternal Sunshine of the Spotless Mind", "2004 · Michel Gondry", "Ayrılığın acısından kurtulmak için sevgilisini hafızasından sildiren bir adam. Unutmak sandığı kadar kolay değil."),
         ("her_4", "35% 50%", "Her", "2013 · Spike Jonze", "Boşanmanın eşiğindeki Theodore bir işletim sistemine âşık olur. Bir mesajı bekleyen herkesin filmi."),
         ("beginagain_1", "50% 40%", "Begin Again", "2013 · John Carney", "Sevgilisi tarafından terk edilen bir şarkıcı acısını şarkılara döker. Film bitince şarkıları başa saracaksın."),
         ("anniehall_2", "50% 40%", "Annie Hall", "1977 · Woody Allen", "Alvy, biten ilişkisini baştan sona didikleyip nerede hata yaptığını bulmaya çalışır."),
         ("bluevalentine_2", "50% 40%", "Blue Valentine", "2010 · Derek Cianfrance", "Bir evliliğin başlangıcı ve sonu iç içe anlatılır. Ağır ama çok dürüst.")],
  q="Ghostlanınca<br>hangi şarkıyı<br>dinledin?", sub="Yorumlara yaz, listeyi birlikte dinleyelim.", bg="#1a0a12", ink="#fff",
  hook="Görüldü, 3 gün önce. Ve sen hâlâ aynı şarkıdasın.",
  intro="Terapiye gitmeden önce izlemen gereken 5 film:",
  ask="Ghostlandıktan sonra hangi şarkıyı dinledin?"),

 dict(id="2026-11-11_liste_red-flag", date="2026-11-11", cover=kapak2.c3, acc="#ff5a45",
  films=[("phantom_4", "55% 40%", "Phantom Thread", "2017 · Paul Thomas Anderson", "Takıntılı bir terzi ve onu değiştirmeye kararlı genç bir kadın. Sonunda kimin kimi değiştirdiği belli değil."),
         ("ripley_2", "50% 40%", "The Talented Mr. Ripley", "1999 · Anthony Minghella", "Tom Ripley zengin bir hayata sızmak için her yolu dener. Fazla tatlı görünen birine dikkat."),
         ("revroad_1", "45% 40%", "Revolutionary Road", "2008 · Sam Mendes", "Mükemmel görünen bir çiftin evliliği, ertelenen hayallerin altında yavaş yavaş çatırdar."),
         ("fresh_2", "50% 40%", "Fresh", "2022 · Mimi Cave", "Uygulamalardan bıkan Noa, markette tanıştığı çekici bir adamla hafta sonu kaçamağına çıkar. Fazla iyi olan her şey şüphelidir."),
         ("saltburn_1", "40% 40%", "Saltburn", "2023 · Emerald Fennell", "Oxford'da tanıştığı zengin arkadaşının yaz davetiyle büyük bir malikâneye yerleşen Oliver'ın hikâyesi.")],
  q="En büyük<br>red flag<br>hangisiydi?", sub="Yorumlara yaz. Hâlâ “değiştiririm” diyen arkadaşını etiketle.", bg="#1a0303", ink="#fff",
  hook="“Ama ben onu değiştiririm.” Bu cümlenin nasıl bittiğini biliyoruz.",
  intro="Red flag'leri görmezden gelenler için 5 film:",
  ask="Listedeki en büyük red flag sence hangisi?"),

 dict(id="2026-11-13_liste_sessize-al", date="2026-11-13", cover=kapak2.c4, acc="#c8f06a",
  films=[("intowild_1", "30% 40%", "Into the Wild", "2007 · Sean Penn", "Üniversiteyi bitiren Christopher her şeyi bırakıp Alaska'ya doğru yola çıkar. Gerçek bir hikâye."),
         ("wild_4", "75% 50%", "Wild", "2014 · Jean-Marc Vallée", "Hayatı dağılan Cheryl, tek başına yüzlerce kilometrelik bir yürüyüşe çıkar. O da gerçek bir hikâye."),
         ("nomadland_3", "50% 40%", "Nomadland", "2020 · Chloé Zhao", "Her şeyini kaybeden Fern, karavanıyla Amerika'yı dolaşan göçebelere katılır."),
         ("captainfant_1", "30% 50%", "Captain Fantastic", "2016 · Matt Ross", "Çocuklarını şehirden uzakta, ormanda büyüten bir baba uygarlığa geri dönmek zorunda kalır."),
         ("waltermitty_2", "45% 50%", "The Secret Life of Walter Mitty", "2013 · Ben Stiller", "Hayallere dalan bir arşiv çalışanı, kayıp bir fotoğrafın peşinde sonunda gerçekten yola çıkar.")],
  q="Kaybolsan<br>nereye<br>giderdin?", sub="Yorumlara yaz. Sessize aldığın grubu da etiketleme.", bg="#0d1609", ink="#fff",
  hook="Bildirimler kapalı, telefon sessizde. Bir süreliğine yoksun.",
  intro="Kaybolmayı en güzel anlatan 5 film:",
  ask="Her şeyi sessize alıp kaybolsan nereye giderdin?"),

 dict(id="2026-11-15_liste_dort-yildiz", date="2026-11-15", cover=kapak2.c5, acc="#00e07a",
  films=[("aftersun_2", "50% 40%", "Aftersun", "2022 · Charlotte Wells", "Bir kız, yıllar önce babasıyla geçirdiği tatili eski kamera görüntüleriyle hatırlar. Sonunda sessizce yıkar."),
         ("worstperson_2", "50% 40%", "The Worst Person in the World", "2021 · Joachim Trier", "Otuzuna yaklaşan Julie, aşk ve kariyer arasında kim olduğunu arar. Oslo'da 12 bölümlük bir hayat."),
         ("eeaao_1", "40% 40%", "Everything Everywhere All at Once", "2022 · Daniel Kwan, Daniel Scheinert", "Çamaşırhane sahibi Evelyn çoklu evrenlerde kızıyla barışmanın yolunu arar. Önce güldürür, sonra bozar."),
         ("portrait_1", "50% 40%", "Portrait of a Lady on Fire", "2019 · Céline Sciamma", "18. yüzyılda bir ressam, evlendirilecek bir kadının portresini gizlice yapmak için bir adaya gelir."),
         ("banshees_1", "40% 40%", "The Banshees of Inisherin", "2022 · Martin McDonagh", "İrlanda'da küçük bir adada, en yakın arkadaşı bir gün onunla konuşmayı bırakır.")],
  q="Seni en son<br>hangi film<br>bozdu?", sub="Yorumlara yaz, dört yıldızlık listeyi büyütelim.", bg="#14121f", ink="#fff",
  hook="Dört yıldız verdin, yorumuna tek cümle yazdın: “Bu film beni biraz bozdu.”",
  intro="İzledikten sonra bir süre kendine gelemeyeceğin 5 film:",
  ask="Seni en son hangi film bozdu?"),

 dict(id="2026-11-17_liste_tesaduf", date="2026-11-17", cover=kapak7.tesaduf_a, acc="#ffe14d",
  films=[("harrysally_1", "50% 50%", "When Harry Met Sally...", "1989 · Rob Reiner", "Yıllar içinde tekrar tekrar karşılaşan iki kişi. Bir kadınla bir erkek gerçekten sadece arkadaş olabilir mi?"),
         ("amelie_4", "62% 40%", "Amélie", "2001 · Jean-Pierre Jeunet", "Paris'te başkalarının hayatına gizlice dokunan Amélie, kendi tesadüfünü kurmaya çalışır."),
         ("chungking_4", "50% 40%", "Chungking Express", "1994 · Wong Kar-wai", "Hong Kong'da iki polis ve bir büfede kesişen hayatlar. Tesadüflerle örülü bir şehir masalı."),
         ("sleepless_4", "70% 40%", "Sleepless in Seattle", "1993 · Nora Ephron", "Radyoda duyduğu bir sesle, ülkenin öbür ucundaki tanımadığı bir adama bağlanan bir kadın."),
         ("serendipity_3", "50% 50%", "Serendipity", "2001 · Peter Chelsom", "Tek bir akşam tanışan iki kişi, kaderin onları yeniden buluşturup buluşturmayacağını sınar.")],
  q="Senin en güzel<br>tesadüfün<br>neydi?", sub="Yorumlara yaz. Belki o kişi de okur.", bg="#111111", ink="#fff",
  hook="Sola kaydır, sağa kaydır, yine aynı yüzler. Belki de beklediğin şey bir tesadüf.",
  intro="Gerçek bir tesadüfün büyüsünü hatırlatan 5 film:",
  ask="Senin en güzel tesadüfün neydi?"),

 dict(id="2026-11-19_liste_film-gecesi", date="2026-11-19", cover=kapak3.f_c, acc="#ff7eb6",
  films=[("legallyblonde_1", "50% 30%", "Legally Blonde", "2001 · Robert Luketic", "Terk edilen Elle, eski sevgilisinin peşinden Harvard Hukuk'a girer. Ayrılık sonrası motivasyonun kraliçesi."),
         ("bridget_1", "50% 40%", "Bridget Jones's Diary", "2001 · Sharon Maguire", "Her şeyi günlüğüne yazan Bridget, aşk hayatını düzene sokmaya çalışır. Peçeteyi yakında tut."),
         ("sarahmarshall_2", "40% 50%", "Forgetting Sarah Marshall", "2008 · Nicholas Stoller", "Terk edilen Peter unutmak için Hawaii'ye gider. Eski sevgilisi de aynı oteldedir."),
         ("theholiday_1", "50% 40%", "The Holiday", "2006 · Nancy Meyers", "Aşk acısı çeken iki kadın Noel'de evlerini değiş tokuş eder. Battaniye filmlerinin klasiği."),
         ("crazystupid_4", "50% 40%", "Crazy, Stupid, Love.", "2011 · Glenn Ficarra, John Requa", "Boşanma aşamasındaki Cal, barda tanıştığı Jacob'dan flört dersleri alır.")],
  q="Film gecesinin<br>vazgeçilmezi<br>hangisi?", sub="Yorumlara yaz. Ayrılık yaşayan arkadaşına gönder.", bg="#160a12", ink="#fff",
  hook="Arkadaşın ayrıldı. Dondurma alındı, peçeteler hazır. Sıra filmde.",
  intro="Ayrılık sonrası film gecesi için 5 film:",
  ask="Film gecesinde ilk hangisini açardın?"),

 dict(id="2026-11-21_liste_tek-kisilik-sofra", date="2026-11-21", cover=kapak4.s3, acc="#ff9a5a",
  films=[("lunchbox_1", "96% 40%", "The Lunchbox", "2013 · Ritesh Batra", "Mumbai'de yanlış adrese giden bir yemek kabı, iki yalnız insanı mektuplarla buluşturur."),
         ("littleforest_2", "55% 40%", "Little Forest", "2018 · Yim Soon-rye", "Şehirden köyüne dönen Hye-won, mevsimlerle birlikte kendi yemeğini pişirir."),
         ("kamome_1", "50% 40%", "Kamome Diner", "2006 · Naoko Ogigami", "Helsinki'de küçük bir Japon lokantası açan Sachie'nin sakin ve sıcak hikâyesi."),
         ("juliejulia_3", "50% 40%", "Julie & Julia", "2009 · Nora Ephron", "Bir yıl boyunca Julia Child'ın tariflerini pişirip bloğuna yazan Julie'nin hikâyesi."),
         ("ratatouille_2", "50% 40%", "Ratatouille", "2007 · Brad Bird", "Paris'te şef olmayı hayal eden bir fare. “Herkes yemek yapabilir.”")],
  q="Tek başına<br>yerken hangi<br>filmi açarsın?", sub="Yorumlara yaz, akşam yemeği listemizi büyütelim.", bg="#1c120a", ink="#fff",
  hook="Tek tabak, tek kaşık, açık kalan bir film. Bu da bir hayat, hem de güzel bir hayat.",
  intro="Tek kişilik sofranın yalnız olmadığını gösteren 5 film:",
  ask="Tek başına yemek yerken hangi filmi açarsın?"),

 dict(id="2026-11-23_liste_iki-gunluk-kacis", date="2026-11-23", cover=kapak7.kacis_c, acc="#c8f06a",
  films=[("romanholiday_3", "45% 40%", "Roman Holiday", "1953 · William Wyler", "Görevlerinden kaçan bir prenses Roma'da tek bir gün sıradan biri olur."),
         ("cmbyn_1", "28% 50%", "Call Me by Your Name", "2017 · Luca Guadagnino", "İtalya'da bir yaz, bir aile evi ve unutulmayacak bir yakınlık."),
         ("mammamia_1", "38% 50%", "Mamma Mia!", "2008 · Phyllida Lloyd", "Bir Yunan adasında düğün hazırlığı ve ABBA şarkıları. Açınca tatile çıkmış gibi olursun."),
         ("ferris_3", "80% 40%", "Ferris Bueller's Day Off", "1986 · John Hughes", "Okulu kırıp Chicago'da tek bir günü dolu dolu yaşayan Ferris. Kaçamakların klasiği."),
         ("darjeeling_3", "50% 40%", "The Darjeeling Limited", "2007 · Wes Anderson", "Hindistan'da bir trende yeniden yakınlaşmaya çalışan üç kardeş.")],
  q="İki günün<br>olsa nereye<br>kaçardın?", sub="Yorumlara yaz. Birlikte kaçacağın kişiyi etiketle.", bg="#0b1608", ink="#fff",
  hook="İzin günü: 2. Hayaller: sonsuz.",
  intro="Kaçmanın bir film kadar iyi geldiğini hatırlatan 5 film:",
  ask="İki günün olsa nereye kaçardın?"),

 dict(id="2026-11-25_liste_alarm-ertele", date="2026-11-25", cover=kapak2.c10, acc="#ffc04d",
  films=[("groundhog_4", "60% 40%", "Groundhog Day", "1993 · Harold Ramis", "Aynı günü tekrar tekrar yaşayan Phil, sonunda kendini değiştirmeyi öğrenir."),
         ("palmsprings_1", "50% 50%", "Palm Springs", "2020 · Max Barbakow", "Bir düğünde zaman döngüsüne sıkışan iki kişi. Her gün aynı, ama aynı kalmak zorunda değiller."),
         ("yesman_3", "40% 40%", "Yes Man", "2008 · Peyton Reed", "Her şeye hayır diyen Carl, bir yıl boyunca her şeye evet demeye söz verir."),
         ("soul_2", "55% 40%", "Soul", "2020 · Pete Docter", "Hayalindeki işe kavuşmak üzereyken bambaşka bir dünyaya düşen müzik öğretmeni Joe."),
         ("happyness_3", "55% 40%", "The Pursuit of Happyness", "2006 · Gabriele Muccino", "Evsiz kalan Chris Gardner oğluyla birlikte yeni bir hayat kurmak için mücadele eder. Gerçek bir hikâye.")],
  q="Senin “bugün<br>her şey<br>değişecek”<br>günün hangisi?", sub="Yorumlara yaz. Yarın sabah alarmı ertelemeden önce bu listeye bak.", bg="#161310", ink="#fff",
  hook="07:00 ertele. 07:09 ertele. 07:18 ertele. “Bugün her şey değişecek.”",
  intro="O sözün peşinden gerçekten gidenleri anlatan 5 film:",
  ask="Senin “bugün her şey değişecek” dediğin gün hangisiydi?"),
]

GUN = {"2026-11-07": "Cumartesi", "2026-11-09": "Pazartesi", "2026-11-11": "Çarşamba", "2026-11-13": "Cuma", "2026-11-15": "Pazar",
       "2026-11-17": "Salı", "2026-11-19": "Perşembe", "2026-11-21": "Cumartesi", "2026-11-23": "Pazartesi", "2026-11-25": "Çarşamba"}
TEASE = ["ghostlandıktan sonra aynı şarkıyı dinleyenlere 5 film.", "red flag'leri görüp “değiştiririm” diyenlere 5 film.",
         "grup sohbetini sessize alıp kaybolmak isteyenlere 5 film.", "seni biraz bozacak, dört yıldızlık 5 film.",
         "kaydırmaktan yorulanlara, gerçek bir tesadüfün 5 filmi.", "ayrılık sonrası film gecesi için 5 film.",
         "tek kişilik sofranın yalnız olmadığını gösteren 5 film.", "iki günlük kaçamağa sevinenlere 5 film.",
         "alarmı beş kez erteleyenlere 5 film.", None]


def caption(i, d):
    lines = [d["hook"], "", d["intro"], ""]
    for _, _, t, meta, _ in d["films"]:
        yr = meta.split(" · ")[0]
        lines.append(f"{t} ({yr})")
    lines += ["", d["ask"], ""]
    if TEASE[i]:
        nxt = POSTS[i + 1]["date"]
        lines.append(f"{GUN[nxt]} 18:00'de: {TEASE[i]}")
    else:
        lines.append("Yeni listelerle buradayız. Takipte kal.")
    return "\n".join(lines)


def build(i):
    d = POSTS[i]
    slides = [d["cover"]()]
    for k, (st, pos, t, meta, desc) in enumerate(d["films"], 1):
        slides.append(film_slide(st, pos, k, t, meta, desc, d["acc"]))
    slides.append(cta_slide(d["q"], d["sub"], d["bg"], d["ink"], d["acc"]))
    return slides


if __name__ == "__main__":
    sel = [int(x) - 1 for x in sys.argv[1:]] or range(len(POSTS))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        tmp = os.path.join(HERE, "_k.html")
        for i in sel:
            d = POSTS[i]
            out = os.path.join(REPO, "posts", d["id"])
            os.makedirs(out, exist_ok=True)
            for f in os.listdir(out):
                if f.endswith(".jpg"):
                    os.remove(os.path.join(out, f))
            for k, html in enumerate(build(i), 1):
                open(tmp, "w").write(html)
                pg.goto("file://" + tmp, wait_until="load")
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(450)
                pg.screenshot(path=os.path.join(out, f"{k:02d}.jpg"), type="jpeg", quality=93)
            open(os.path.join(out, "caption.txt"), "w").write(caption(i, d) + "\n")
            print(d["id"])
        b.close()

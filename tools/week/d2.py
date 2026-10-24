import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from design_kit import *
R="#d7261e"; C="#f3ead8"; K="#140a0a"
CAPTION = """Keanu Reeves son sahnede hep aynı seçimi yapıyor. Kimi zaman kendini, kimi zaman dünyayı, kimi zaman bir inancı seçiyor ve her seferinde bir bedel ödüyor.

Constantine'de cehennemle pazarlık eden bir şeytan kovucu, The Matrix Revolutions'ta insanlığın kaderini omuzlayan Neo, The Day the Earth Stood Still'de dünyayı kurtarmaya çalışan bir uzaylı elçisi, The Devil's Advocate'ta ise bir avukat var. Hepsinin finalinde Keanu'nun karakteri başka birinin yerine bir yük taşıyor.

Sonları kimseye anlatmıyoruz, sen izle ve karar ver: Keanu'nun en çok hangi filmde fedakârlık yaptığını düşünüyorsun?

Yarın 18:00'de: Bir balık ve bir adam aynı sorunu yaşıyor, ikisi de bir şeyleri hatırlayamıyor. Dory mi Memento mu?"""
def foot(c="#fff", lg="white"): return [logo(lg,930,1262,80,z=8), handle(60,1295,c,24,w=400,z=8)]
def build():
    S=[]
    S.append({"bg":R,"els":[
        img(prep("n_constantine_1",crop=(0.55,0,1,1),size=(1080,1350),duo=("#1a0505","#f3ead8"),contrast=1.2,grain=16),0,0,1080,1350,z=1),
        box(0,0,1080,1350,R,z=2,blend="multiply"),
        txt("KEANU",40,40,1000,size=330,font="anton",color=C,z=4,lh=1),
        txt("SON SAHNEDE<br>HEP GÖNÜLLÜ",50,360,900,size=118,font="anton",color=R,z=5,lh=1,bg=C,pad="10px 24px",css="display:inline-block"),
        box(0,1040,1080,310,K,z=3),
        txt("Kendini feda ettiği 4 film",60,1075,900,size=62,font="playfair",weight=700,color=C,z=5),
        txt("Sonlar spoiler'sız · Kaydet",60,1175,900,size=34,font="oswald",weight=500,color=R,ls=4,upper=True,z=5),
        logo("red",900,1130,130,z=8)]})
    def film(n,name,meta,body,src,crop,side):
        left = side=="L"
        rot = -3 if left else 3
        return {"bg":K,"els":[
            img(prep(src,crop=crop,size=(1080,1350),duo=("#1a0505","#f3ead8"),contrast=1.15,grain=14),0,0,1080,1350,z=1),
            box(0,0,1080,1350,R,z=2,blend="multiply",op=.85),
            box(0,820,1080,530,"linear-gradient(180deg,rgba(20,10,10,0),rgba(20,10,10,.95) 40%)",z=3),
            txt(n,40 if left else 540,10,500,size=380,font="anton",color="transparent",stroke="6px #f3ead8",z=4,lh=1,align="left" if left else "right"),
            box(-40,560,1160,230,C,z=5,rot=rot),
            txt(name,50,585,980,size=96 if len(name)<20 else 62,font="anton",color=R,z=6,lh=1.05,upper=True,rot=rot,align="left" if left else "right"),
            txt(meta,60,880,960,size=32,font="oswald",weight=500,color=C,ls=5,upper=True,z=6),
            txt(body,60,945,940,size=44,font="inter",weight=600,color="#fff",lh=1.3,z=6),
            logo("red",930,1262,80,z=8), handle(60,1295,C,24,w=400,z=8)]}
    S.append(film("01","CONSTANTINE","2005 · Francis Lawrence","Cehennemle pazarlık eden bir şeytan kovucunun, kendi ruhunu da riske atması gerekir.","n_constantine_4",(0.5,0,1,1),"L"))
    S.append(film("02","THE MATRIX REVOLUTIONS","2003 · Wachowski'ler","Neo'nun makinelerle savaşı bu kez insanlığın son şehri Zion'un önünde sonuçlanır.","fg_matrixrev_09",(0.2,0,0.8,1),"R"))
    S.append(film("03","THE DAY THE EARTH STOOD STILL","2008 · Scott Derrickson","Dünyaya gelen bir elçi, insanlığın yaşamaya değip değmediğine karar vermek zorundadır.","n_dayearth_1",(0.55,0,1,1),"L"))
    S.append(film("04","THE DEVIL'S ADVOCATE","1997 · Taylor Hackford","Hiç dava kaybetmeyen genç bir avukat, büyük bir hukuk firmasında çok daha büyük bir bedel öder.","n_devilsadv_4",(0.35,0,0.9,1),"R"))
    S.append({"bg":R,"els":[
        txt("SENCE<br>HANGİSİNDE<br>EN ÇOK<br>FEDAKÂRLIK<br>YAPTI?",60,70,980,size=180,font="anton",color=C,lh=.95),
        txt("Yorumlara yaz. En iyi cevap bir sonraki gönderiye girer.",64,1010,720,size=44,font="playfair",color=K,weight=700,lh=1.2),
        logo("black",780,980,240,z=8), handle(64,1290,K,26)]})
    return {"id":"2026-10-26_liste_keanu-son-sahnede-gonullu","caption":CAPTION,"slides":S}
if __name__=="__main__":
    import render2; render2.render(build())

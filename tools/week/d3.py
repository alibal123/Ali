import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from design_kit import *
B="#1d7bff"; Y="#ffd23f"; O="#ff6b35"; W="#fffaf0"; K="#10162f"
CAPTION = """Unutanlar Kulübü'ne hoş geldin. Bir tarafta mavi bir balık, diğer tarafta vücudunu notlarla dolduran bir adam. İkisi de kısa süreli hafıza kaybıyla yaşıyor.

Finding Nemo'da (2003) Dory her şeyi birkaç dakikada unutuyor ama hiç pes etmiyor. Memento'da (2000) Leonard yeni bir anı biriktiremiyor, bu yüzden Polaroid'lere, notlara ve dövmelere güveniyor. İkisi de aynı eksikliği çok farklı anlatıyor: biri umutla, biri paranoyayla.

Kim daha iyi yönetiyor bu hafızasızlığı? Dory mi, Leonard mı? Yorumlara yaz.

Yarın 18:00'de: Dışarı kıyamet koptuğunda izlenecek 4 film."""
def build():
    S=[]
    S.append({"bg":W,"els":[
        img(prep("fg_nemo_05",crop=(0.15,0,0.65,1),size=(540,1350),sat=1.25,contrast=1.1),0,0,540,1350,z=1),
        img(prep("fg_memento_04",crop=(0.25,0,0.75,1),size=(540,1350),gray=True,contrast=1.3,grain=18),540,0,540,1350,z=1),
        box(0,0,540,1350,B,z=2,blend="soft-light",op=.6),
        box(536,0,8,1350,Y,z=3),
        txt("DORY",24,40,500,size=190,font="anton",color=Y,z=5,lh=1,stroke="4px #1d7bff"),
        txt("MEMENTO",540,50,500,size=118,font="anton",color=W,z=5,lh=1,align="right"),
        box(190,560,700,250,Y,z=6,rot=-4,border="8px solid #10162f"),
        txt("UNUTANLAR<br>KULÜBÜ",200,575,680,size=118,font="anton",color=K,align="center",z=7,rot=-4,lh=1),
        txt("Kim hafızasızlığı daha iyi yönetiyor?",50,1120,980,size=62,font="playfair",weight=700,color=W,z=6,bg="rgba(16,22,47,.85)",pad="14px 22px",lh=1.2),
        logo("white",900,1210,130,z=8)]})
    def half(top_src,top_crop,bot_src,bot_crop,title,meta,body,col,gray_bot=False):
        return {"bg":col,"els":[
            img(prep(top_src,crop=top_crop,size=(1080,700),sat=1.2),0,0,1080,700,z=1),
            box(0,640,1080,710,col,z=2,rot=-3,css="transform-origin:0 0"),
            txt(title,60,640,960,size=130,font="anton",color=W if col!=Y else K,z=5,lh=1,rot=-3),
            txt(meta,60,800,900,size=32,font="oswald",weight=500,color=W if col!=Y else K,ls=4,upper=True,z=5,rot=-3),
            txt(body,60,880,940,size=40,weight=600,color=W if col!=Y else K,lh=1.3,z=5,rot=-3),
            logo("white" if col!=Y else "black",930,1262,80,z=8)]}
    S.append(half("fg_nemo_03",(0,0,1,1),None,None,"FINDING NEMO","2003 · Andrew Stanton","Dory her şeyi dakikalar içinde unutuyor. Ama Marlin'e bir okyanus boyunca eşlik etmekten vazgeçmiyor. Film, En İyi Animasyon Oscar'ını kazandı.",B))
    S.append(half("fg_memento_01",(0,0,1,1),None,None,"MEMENTO","2000 · Christopher Nolan","Leonard yeni anı oluşturamıyor. Karısının katilini bulmak için Polaroid'lere, notlara ve dövmelere güveniyor. Film, kurgu ve senaryo dallarında Oscar'a aday gösterildi.",O))
    S.append({"bg":Y,"els":[
        txt("İKİSİNİN<br>ORTAK<br>NOKTASI",40,50,1000,size=170,font="anton",color=K,lh=.95),
        img(prep("fg_nemo_01",size=(480,560),sat=1.2),40,580,480,560,z=2,rot=-4,border="12px solid #fff",shadow="0 14px 30px rgba(0,0,0,.3)"),
        img(prep("fg_memento_12",size=(480,560),gray=True,contrast=1.3,grain=14),560,620,480,560,z=2,rot=4,border="12px solid #fff",shadow="0 14px 30px rgba(0,0,0,.3)"),
        txt("kısa süreli<br>hafıza",70,1150,430,size=70,font="caveat",weight=700,color=B,lh=1,rot=-4,z=6),
        txt("hayatta kalma<br>planı",600,1190,430,size=70,font="caveat",weight=700,color=O,lh=1,rot=3,z=6),
        logo("black",920,1262,90,z=8)]})
    S.append({"bg":B,"els":[
        txt("SEN<br>HANGİ<br>TARAFTASIN?",60,60,980,size=200,font="anton",color=W,lh=.95),
        box(60,780,450,190,Y,z=3,rot=-3), txt("DORY",60,805,450,size=120,font="anton",color=K,align="center",z=4,rot=-3),
        box(560,820,450,190,K,z=3,rot=3), txt("MEMENTO",560,845,450,size=100,font="anton",color=W,align="center",z=4,rot=3),
        txt("Yorumlara yaz ve filmi hiç izlemeyen bir arkadaşına gönder.",60,1080,760,size=42,font="playfair",weight=700,color=W,lh=1.25),
        logo("white",860,1050,170,z=8)]})
    return {"id":"2026-10-27_liste_unutanlar-kulubu","caption":CAPTION,"slides":S}
if __name__=="__main__":
    import render2; render2.render(build())

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from design_kit import *
P="#f4ecdb"; K="#2a2118"; G="#3f6b4f"; T="#c4552d"
CAPTION = """Hayatı bir an durup sorgulatan 4 sakin film. Patlama yok, kovalamaca yok, sadece insan ve zaman var.

The Tree of Life (2011) bir ailenin hikâyesini evrenin yaratılışıyla yan yana koyuyor ve Cannes'da Altın Palmiye aldı. Wild Strawberries (1957) yaşlı bir profesörün geçmişine yaptığı yolculuğu Bergman'ın kaleminden anlatıyor. Perfect Days (2023) Tokyo'da tuvaletleri temizleyen bir adamın sakin günlerini izliyor, Koji Yakusho bu rolle Cannes'da En İyi Erkek Oyuncu seçildi. Paterson (2016) şiir yazan bir otobüs şoförünün haftasını anlatıyor.

Bu hafta bir akşamını bunlardan birine ayır. Sen hangisinden sonra hayatına dair bir şeyi değiştirdin?

Cumhuriyet Bayramımız kutlu olsun."""
def build():
    S=[]
    pol="14px solid #fff"; sh="0 16px 34px rgba(60,40,20,.35)"
    S.append({"bg":P,"els":[
        img(prep("n_treeoflife_2",size=(520,640),contrast=1.1,sat=1.1),40,60,520,640,z=2,rot=-5,border=pol,shadow=sh),
        img(prep("n_perfectdays_2",size=(480,600),contrast=1.05),560,40,480,600,z=2,rot=4,border=pol,shadow=sh),
        img(prep("n_paterson_6",size=(560,420),contrast=1.05),500,560,520,390,z=3,rot=-3,border=pol,shadow=sh),
        img(prep("n_wildstraw_2",size=(460,400),gray=True,contrast=1.2,grain=12),30,640,440,380,z=3,rot=3,border=pol,shadow=sh),
        txt("Size hayatı<br>sorgulatacak",60,1030,980,size=108,font="serif",color=K,lh=1,z=5),
        txt("4 sakin film",60,1250,500,size=76,font="caveat",weight=700,color=T,z=5,rot=-2),
        logo("black",920,1090,110,z=8)]})
    def film(n,title,meta,body,src,crop,size,rot,note):
        return {"bg":P,"els":[
            txt(n,640,-60,420,size=480,font="serif",color="#e6d8bd",align="right",z=1,lh=1),
            img(prep(src,crop=crop,size=(900,640)),90,150,900,640,z=3,rot=rot,border="16px solid #fff",shadow=sh),
            txt(title,60,880,960,size=96,font="serif",color=K,lh=1,z=5,upper=True),
            txt(meta,64,1000,900,size=30,font="oswald",weight=500,color=T,ls=4,upper=True,z=5),
            txt(body,64,1055,900,size=38,font="playfair",weight=400,color=K,lh=1.3,z=5),
            txt(note,560,40,480,size=58,font="caveat",weight=700,color=G,lh=1,z=6,rot=5),
            logo("black",930,1262,80,z=8)]}
    S.append(film("1","THE TREE OF LIFE","2011 · Terrence Malick","Bir ailenin hikâyesi, evrenin yaratılışıyla yan yana anlatılır. Cannes'da Altın Palmiye kazandı.","n_treeoflife_3",(0,0,1,1),(800,560),-2,"yavaş ve büyük"))
    S.append(film("2","WILD STRAWBERRIES","1957 · Ingmar Bergman","Yaşlı bir profesör, onur ödülüne giderken geçmişinin içinden de geçer.","n_wildstraw_3",(0,0,1,1),(720,540),2,"geçmişe yolculuk"))
    S.append(film("3","PERFECT DAYS","2023 · Wim Wenders","Tokyo'da tuvalet temizleyen bir adamın sakin günleri. Koji Yakusho, Cannes'da En İyi Erkek Oyuncu seçildi.","n_perfectdays_4",(0,0,1,1),(760,560),-2,"küçük ritüeller"))
    S.append(film("4","PATERSON","2016 · Jim Jarmusch","Şiir yazan bir otobüs şoförünün sıradan bir haftası.","n_paterson_1",(0,0,1,1),(800,560),2,"her gün bir şiir"))
    S.append({"bg":G,"els":[
        txt("hangisinden sonra<br>hayatında bir şey<br>değişti?",60,100,980,size=130,font="caveat",weight=700,color=P,lh=1,rot=-2),
        txt("Yorumlara yaz",60,760,700,size=70,font="serif",color=P,z=5),
        txt("29 EKİM · CUMHURİYET BAYRAMIMIZ KUTLU OLSUN",60,980,800,size=36,font="oswald",weight=500,color=P,ls=4,z=5,bg=T,pad="10px 18px",rot=-1),
        logo("white",800,1020,200,z=8)]})
    return {"id":"2026-10-29_liste_hayati-sorgulatan-4-film","caption":CAPTION,"slides":S}
if __name__=="__main__":
    import render2; render2.render(build())

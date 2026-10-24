import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from design_kit import *
K="#0a0f0a"; W="#f5f5ee"
GR=["#3ddc84","#a8d94a","#f0c030","#e8761f","#e03a2a"]
CAPTION = """Dışarı kıyamet koptuğunda içeride izlenecek 4 film. Dünyanın sonu bu filmlerde patlamalarla değil, insanların birbirine bakışıyla geliyor.

Children of Men insanlığın artık çocuk doğuramadığı bir dünyayı, Take Shelter bir adamın kafasındaki fırtınayı, The Road küllere dönmüş bir dünyada babayla oğulun yürüyüşünü, Melancholia ise Dünya'ya doğru yaklaşan dev bir gezegeni anlatıyor.

Sırayla izlersen kıyamete kendini hazırlamış olursun. Sen son film olarak hangisini seçerdin?

Yarın 18:00'de: Hayatı sorgulatacak 4 sakin film. Takipte kal."""
def bg(i): 
    a=GR[i]; b=GR[min(i+1,4)]
    return {"css":f"linear-gradient(180deg,{a},{b})"}
def build():
    S=[]
    S.append({"bg":{"css":"linear-gradient(180deg,#3ddc84 0%,#f0c030 50%,#e03a2a 100%)"},"els":[
        img(prep("n_childrenofmen_3",size=(1080,590),duo=("#0a0f0a","#f5f5ee"),contrast=1.2,grain=14),0,760,1080,590,z=1,css="opacity:.9"),
        txt("KIYAMETE<br>4 FİLM<br>KALDI",50,30,980,size=215,font="anton",color=K,lh=.92,z=5),
        box(0,700,1080,110,K,z=4,rot=-2), txt("SON SEANS · DIŞARI KIYAMET KOPUYOR",0,725,1080,size=40,font="oswald",weight=500,color=W,ls=6,align="center",z=5,rot=-2),
        txt("Kaydet · izle · hazırlan",60,1250,700,size=40,font="oswald",weight=500,color=K,ls=4,upper=True,z=6,bg=W,pad="8px 16px"),
        logo("black",900,1180,140,z=8)]})
    def film(i,left,title,meta,body,src,crop,days):
        t=K if i<3 else W
        return {"bg":bg(i),"els":[
            txt(left,30,-60,800,size=620,font="anton",color="transparent",stroke=f"6px {K if i<3 else W}",z=1,lh=1),
            img(prep(src,crop=crop,size=(1360,560),contrast=1.15,grain=10),-140,390,1360,560,z=3,rot=3,border=f"10px solid {K}",shadow="0 20px 50px rgba(0,0,0,.4)"),
            box(30,1000,700,140,K,z=5,rot=-2), txt(title,50,1010,700,size=100,font="anton",color=GR[i],z=6,rot=-2,lh=1.1,upper=True),
            txt(meta,40,1150,900,size=30,font="oswald",weight=500,color=t,ls=4,upper=True,z=5),
            txt(body,40,1200,860,size=34,weight=700,color=t,lh=1.25,z=5),
            logo("black" if i<3 else "white",930,1262,80,z=8),
            box(730,60,300,150,K,z=5,rot=5), txt(f"DÜNYANIN SONUNA<br><span style='font-size:70px;color:{GR[i]}'>{days}</span>",735,70,290,size=28,font="oswald",weight=500,color=W,align="center",ls=3,z=6,rot=5,lh=1.1)]}
    S.append(film(0,"4","CHILDREN OF MEN","2006 · Alfonso Cuarón","İnsanlık çocuk doğuramaz hale gelmiştir. Bir adam, umudun tek taşıyıcısını korumaya çalışır.","n_childrenofmen_1",(0,0,1,1),"4 GÜN"))
    S.append(film(1,"3","TAKE SHELTER","2011 · Jeff Nichols","Bir inşaat işçisi, gelmekte olan bir fırtınanın kâbuslarını görür. Ailesi bunun gerçek olup olmadığını sorar.","n_takeshelter_2",(0,0,1,1),"3 GÜN"))
    S.append(film(2,"2","THE ROAD","2009 · John Hillcoat","Küllere dönmüş bir dünyada bir baba ve oğul, güneye doğru yürüyor.","n_theroad_3",(0,0,1,1),"2 GÜN"))
    S.append(film(3,"1","MELANCHOLIA","2011 · Lars von Trier","Dünya'ya doğru gelen dev bir gezegen, iki kız kardeşi hazırlıksız yakalar. Kirsten Dunst Cannes'da En İyi Kadın Oyuncu seçildi.","n_melancholia_3",(0,0,1,1),"1 GÜN"))
    S.append({"bg":{"css":"linear-gradient(180deg,#e03a2a,#7a0f0a)"},"els":[
        txt("SON<br>FİLMİNİ<br>SEÇ",60,60,980,size=270,font="anton",color=W,lh=.92),
        txt("Dünyanın son gecesinde hangisini izlerdin?",60,880,880,size=60,font="playfair",weight=700,color=W,lh=1.2),
        txt("YORUMLARA YAZ",60,1120,600,size=40,font="oswald",weight=500,color=K,ls=6,bg="#f0c030",pad="10px 20px",rot=-2),
        logo("white",840,1100,180,z=8)]})
    return {"id":"2026-10-28_liste_son-seans-kiyamet","caption":CAPTION,"slides":S}
if __name__=="__main__":
    import render2; render2.render(build())

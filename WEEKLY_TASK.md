# Haftalık içerik görevi — derecefilm

Bu dosya, her **pazar 11:00 (İstanbul)** çalışan zamanlanmış Claude görevinin talimatıdır.
Amaç: gelecek haftanın her günü için **20:00'de** paylaşılacak birer Instagram karuseli hazırlamak, depoya eklemek ve zamanlamak.
Kullanıcı **tamamen otomatik** istedi: onay bekleme, hazırla ve zamanla; sonunda önizlemeyi kullanıcıya gönder.

## 0. Hazırlık
- Depo: `alibal123/Ali` (Claude'un yazma izni var). Klonla, `main` dalında çalış.
- Kurulum: `pip install playwright pillow --break-system-packages` (gerekirse) ve
  `npm i --prefix tools @fontsource/oswald @fontsource/inter @fontsource/playfair-display`.
- `schedule.json`, `history.json`, `specs/` klasöründeki önceki spec'leri oku (ton ve format için örnek).

## 1. Hangi günler?
- `schedule.json`'daki en son `publish_at` tarihinden **sonraki gün** başla, **gelecek pazar** (dahil) bitir.
  Normalde bu, pazartesi–pazar 7 gün eder. Zaten dolu günleri atla. Saat her zaman `T20:00`.

## 2. Haftalık içerik ve tasarım çeşitliliği
Kullanıcı açıkça istedi: **tek renk kullanma, gönderiler birbirinin aynısı olmasın.** Her gün farklı format ve renk paleti;
gönderi içinde de slaytlar arasında vurgu rengini değiştir (`accent`), en az bir slaytta `bg: "light"` (krem) ya da `"solid"` kullan.
Kullanılabilir renkler: red, orange, amber, lime, teal, cyan, sky, violet, pink, coral (tools/render.py THEMES).

Haftalık format havuzu (her hafta hepsinden en az 5'i, art arda aynı format yok):
| Format (pill) | Slayt tipleri | Örnek |
|---|---|---|
| LİSTE | collage kapak → film ×5 → cta (light) | 2026-10-06 Türk sineması |
| EŞLEŞTİRME | fullphoto kapak → pair ×4 → cta (solid) | 2026-10-07 Bunu sevdiysen |
| FİLM (derin inceleme) | fullphoto → number (light) → text (foto) → file (light) → bullets → cta | 2026-10-08 Memories of Murder |
| OYUN | cover (solid) → crop ×5 → reveal | 2026-10-09 Detaydan filmi bul |
| VERİ | collage → bars ×2 → text (light) → cta | 2026-10-10 İzleyici vs eleştirmen |
| BELGESEL / RADAR / YÖNETMEN | cover/fullphoto, big, rows, cta | gun3_belgesel, gun5_jagten |
`specs/2026-10-*.json` dosyaları referans örneklerdir; yeni spec yazarken bunlardan başla.

Okunabilirlik: uzun metinde **`text`** tipini kullan (düz yazı; `<i>` yalnızca 2–4 kelimelik vurgu). `big` (serif italik) yalnızca
≤25 kelimelik kısa cümleler için. Render çıktısında "metni taşıyor" uyarısı varsa metni kısalt.

Veri kaynakları (hesaba uygun film seçimi):
- `insights/media.json`: hesabın gönderi performansı (her pazar 08:17'de güncellenir). En çok tutanlar: kült/tuhaf/animasyon
  (Four Lions, Shrek, Fantastic Mr. Fox, 964 Pinocchio), Türk filmleri (Kabadayı, Duvara Karşı) ve liste karuselleri.
- Kullanıcının izleme listesi: Mac'te `~/Downloads/DERECE FİLM/İzlenecek Filmler Listesi.pdf` (469 film, türlere göre, IMDb/RT puanlı).
  Mac erişilebilirse buradan seç; değilse `history.json` ve kendi bilgine dayan.
- Kullanıcının indirdiği filmler: `~/Downloads/FİLMLER/` (ffmpeg ile gerçek kare çıkarılabilir — OYUN için ideal).

### Tasarım stüdyosu (tools/studio.py) — her gönderi ayrı bir tasarım dili
Kullanıcı "birbirinin kopyası AI gönderiler gibi durmasın" dedi. 12–21 Ekim gönderileri `specs/studio/*.py` ile yapıldı;
her biri kendi HTML/CSS'iyle farklı bir dünyadan geliyor: ebru + minyatür, polaroid/motel duvarı, tebeşir zemin,
eski gazete, tarot kartları, mavi baskı (blueprint), kontak baskı/film negatifi, vitray, İsviçre grafik, 90'lar elle boyanmış sinema afişi.
Yeni hafta için render.py şablonlarına ek olarak en az 2–3 gönderiyi studio.py ile, bu listede OLMAYAN yeni bir görsel dille yap
(ör. VHS kutusu, sinema bileti/programı, risograf, çizgi roman, dergi röportajı, senaryo sayfası).
- Sahne kareleri: TMDB sitesi Actions'tan da engelli. film-grab.com galerilerini WebFetch ile bul, adresleri `assets/stills/request.json`'a ekle.
- Higgsfield (bağlıysa): `media_import_url` + `upscale_image` (2k, ~2 kredi) ile küçük kareleri büyüt; özgün illüstrasyon için
  `nano_banana_pro` (2k, ~2 kredi). Sonuç adreslerini de request.json'a ekle (bulut ortamı CDN'e doğrudan erişemiyor, iş akışı indirir).
  İllüstrasyonlarda insan yüzü/gerçek kişi çizdirme; baskı tekniği, nesne ve mekân çizdir. Telifli karakter/logo/afiş çizdirme.

## 3. Metin kuralları
- Türkçe, sade, merak uyandıran. Slayt metinleri kısa; `big` en fazla ~45 kelime.
- İngilizce film adları `title`/`rows.lab` alanlarında (otomatik İngilizce büyük harf). Türkçe başlıkta İngilizce ad geçerse
  `<span lang='en'>Ad</span>` kullan (yoksa "İ" hatası olur).
- **Açıklama (caption)** hesabın kendi stilinde: film adı + (yıl) ile başlayan 3 paragraf; 1) konu, 2) gelişme, 3) neden önemli.
  Sonunda kısa bir soru olabilir. Hashtag kullanma. Oyun gününde kısa açıklama.

- **Devamlılık:** Her açıklamanın son satırı bir sonraki günün gönderisini haber versin:
  `Yarın 20:00'de: <bir cümlelik merak uyandıran tanıtım>`. Haftanın son gönderisinde
  `Yarın 20:00'de yeni haftanın ilk gönderisiyle buradayız. Takipte kal.` yaz. Yeni haftaya başlarken önceki haftanın
  son açıklaması zaten bu genel satırla bittiği için ona dokunma.

## 4. Sahne fotoğrafları
**Önerilen yol (Mac gerekmez):**
1. TMDB'de filmin backdrop görsellerini bul (WebSearch/WebFetch ya da tarayıcı). Yazısız sahne kareleri seç (afiş/logo olmasın).
2. `assets/stills/request.json` dosyasına `{"<ad>": "https://image.tmdb.org/t/p/w1280/<dosya>.jpg"}` satırları ekle, commit + push.
3. "Sahne karelerini indir" iş akışı (fetch-stills.yml) push ile otomatik çalışır ve `assets/stills/<ad>.jpg` olarak depoya ekler.
   1–2 dakika bekle, `git pull`.
4. Spec'lerde `"stills_dir": "assets/stills"` ve `"img": "<ad>.jpg"`.

**Gerçek film karesi (opsiyonel, Mac açıksa):** device_bash ile `~/Downloads/FİLMLER/<film>/*.mp4` dosyasından
`ffmpeg -ss <saniye> -i <dosya> -frames:v 1 -vf scale=1280:-2` ile kare çıkar, Desktop'a yaz, device_stage_files ile buluta al,
`assets/stills/frame_<ad>.jpg` olarak depoya ekle. Çıplaklık/şiddet içeren kareleri kullanma.

## 5. Üret ve zamanla
1. Her gün için `specs/<YYYY-MM-DD>_<tür>_<kısa-ad>.json` yaz; `id` aynı ad olsun.
2. `python3 tools/render.py specs/<dosya>.json` → `posts/<id>/01.jpg…` + `caption.txt`.
3. Üretilen slaytlardan bir **iletişim sayfası (contact sheet)** yap ve gözle kontrol et: taşan metin, "İ" hatası, okunmayan metin, yanlış fotoğraf.
   Sorun varsa spec'i düzeltip yeniden üret.
4. `schedule.json`'a her gün için ekle:
   `{"id": "<id>", "folder": "posts/<id>", "publish_at": "YYYY-MM-DDT20:00", "platforms": ["instagram"], "status": "planned"}`
5. `history.json`'a kullanılan filmleri ekle.
6. `git add -A && git commit` (mesajın sonuna oturum atıf satırlarını ekle) ve `git push`. Push'tan önce `git pull --rebase`
   (paylaşım botu `schedule.json`'u güncelliyor olabilir).
7. GitHub Actions → "Zamanı gelen gönderileri paylaş" iş akışını `dry_run=1` ile çalıştır ya da API ile sonucu kontrol et
   (görsellerin herkese açık adresten okunabildiğini doğrular).

## 6. Kullanıcıya rapor
- `SendUserMessage` + `SendUserFile` ile: haftanın takvimi (gün · tür · film) ve tüm slaytların tek görsellik önizlemesi.
- Önceki haftanın paylaşım durumunu `schedule.json`'dan özetle (`published` / `failed` / `skipped_late`); `failed` varsa hatayı yaz.
- Kullanıcı değişiklik isterse ilgili spec'i düzenleyip yeniden üret ve push'la (paylaşım saatinden önce).

## Sınırlar
- Instagram API: günde en fazla 100 paylaşım, karusel en fazla 10 görsel, JPG.
- TikTok bu otomatik akışın dışında (TikTok her paylaşımda kullanıcının onay formunu zorunlu tutuyor).

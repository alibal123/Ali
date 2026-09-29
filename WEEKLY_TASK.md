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

## 2. Haftalık içerik dönüşümü
| Gün | Tür (pill) | Tema | Format |
|---|---|---|---|
| Pazartesi | FİLM | red | Tek film: cover → konu (big) → ana çatışma (big) → neden izlemeli (bullets, 3) → künye (rows) → cta |
| Salı | LİSTE | red | "…5 film" listesi: cover → 5×film (n=1..5) → cta |
| Çarşamba | BELGESEL | cyan | Gerçek hikâye anlatımı: cover → 3×big (hikâyeyi adım adım aç, sonu verme) → künye (rows) → cta |
| Perşembe | FİLM | orange | Pazartesi formatı; farklı tür/ülke seç |
| Cuma | OYUN | lime | Emojilerden filmi bul: cover → 5×emoji (blur 22, img = o filmin sahnesi) → cevaplar (rows, img net) |
| Cumartesi | RADAR | lime | Az bilinen/yeni film: cover → konu (big) → bullets → künye (rows, extra ile "X'i sevdiysen") → cta |
| Pazar | LİSTE | red | Temalı liste (ör. "tek mekânda geçen 5 film", "sonu ters köşe 5 belgesel") |

Film seçimi:
- Hesabın sloganı: **"aynı filmlere bakmaktan sıkıldık."** Klişe popüler filmler yerine kaliteli ama az konuşulan filmler seç
  (farklı ülkeler, türler, on yıllar). Oyun (cuma) bilinen filmlerle yapılabilir.
- `history.json`'daki filmleri **tekrar seçme**. Oyun cevapları için `quiz_answers_used` listesine bak.
- Bilgileri (yıl, yönetmen, süre, ödül, Türkçe adı) **web'den doğrula**; emin olmadığın bilgiyi yazma. Spoiler verme.

## 3. Metin kuralları
- Türkçe, sade, merak uyandıran. Slayt metinleri kısa; `big` en fazla ~45 kelime.
- İngilizce film adları `title`/`rows.lab` alanlarında (otomatik İngilizce büyük harf). Türkçe başlıkta İngilizce ad geçerse
  `<span lang='en'>Ad</span>` kullan (yoksa "İ" hatası olur).
- **Açıklama (caption)** hesabın kendi stilinde: film adı + (yıl) ile başlayan 3 paragraf; 1) konu, 2) gelişme, 3) neden önemli.
  Sonunda kısa bir soru olabilir. Hashtag kullanma. Oyun gününde kısa açıklama.

## 4. Sahne fotoğrafları (TMDB, yazısız sahne kareleri)
Bulut ortamı TMDB'ye doğrudan erişemez; kullanıcının Mac'indeki Claude tarayıcı paneli (built-in browser) kullanılır.
Mac erişilemezse bu adımı atla ve slaytları fotoğrafsız üret (tasarım zaten koyu zeminle çalışır).

1. Tarayıcı panelinde `https://www.themoviedb.org/` aç.
2. Her film için (JS ile, sayfa bağlamında):
   - Arama: `fetch('/search/movie?query='+encodeURIComponent(ad)+'%20y:'+yıl)` → HTML'den ilk `/movie/<id>-...` bağlantısı.
   - Arka planlar: `fetch('/movie/<id-slug>/images/backdrops?image_language=xx')` → `img` src'lerinden dosya adları (ilk 12).
3. Adayları küçük önizlemeyle (w185) sayfada ızgara olarak göster, **ekran görüntüsüyle** yazısız ve kaliteli sahne karelerini seç
   (afiş, logo ya da yazı içerenleri eleme).
4. Seçilenleri tek bir **TAR** dosyası olarak indir: JS ile `https://image.tmdb.org/t/p/w1280/<dosya>` görsellerini `fetch` et,
   bellekte ustar formatında birleştir, `Blob` → `<a download="derecefilm_sahneler_<tarih>.tar">` oluştur ve tam sayfa bir buton olarak ekle,
   sonra butona **tarayıcı tıklamasıyla** bas (script içinden `click()` indirmeyi engelliyor; gerçek tıklama gerekli).
5. Mac'te `~/Downloads/derecefilm_sahneler_<tarih>.tar` dosyasını `~/Desktop/derecefilm_sahneler/<tarih>/` altına aç, `device_stage_files` ile
   buluta al, `work/stills/` altına kopyala. Spec'lerde `stills_dir` bu klasör olsun.
6. İş bitince sayfaya eklediğin butonu kaldır.

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

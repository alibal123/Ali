# Günlük vizyon görevi — derecefilm (her gün 14:00)

Bu görev, 15 Ekim 2026'dan itibaren **NEWS_TASK.md (günlük haber) görevinin yerine** her gün 12:48'de (İstanbul) çalışır ve o günün **14:00** gönderisini hazırlar.
Ali **tamamen otomatik** istedi: onay bekleme, hazırla, zamanla, paylaşımı doğrula. 20:00 gönderilerine (WEEKLY_TASK.md) dokunma.

## Ali'nin kuralları (bağlayıcı)
1. **Yalnızca yabancı filmler.** Türk yapımlarını (komedi, korku, animasyon dahil) ASLA seçme.
2. **Kapak fotoğrafı kutu/çerçeve içinde OLMAZ.** Kapak `fullphoto` (tam sayfa, kenarlıksız) olsun. `news` tipinin `top`/`side` varyantlarını, `strip`/`card` gibi fotoğrafı dikdörtgene yerleştiren kapakları KULLANMA. Uygun kare yoksa `cover` (fotoğrafsız tipografik) kullan.
3. Aynı fotoğraf bir gönderide iki slaytta kullanılmaz; afiş, logo ya da yazılı görsel kullanma.

## 0. Önce kontrol et
`schedule.json`'da bugünün tarihiyle `T14:00` olan bir kayıt zaten varsa YENİ gönderi hazırlama; yalnızca 5. bölümdeki doğrulamayı yap.

## 1. Film seçimi
- Türkiye'de **şu an vizyonda olan ya da bu Cuma/önümüzdeki Cuma vizyona girecek yabancı** filmlerden seç (Beyazperde "film vizyon tarihleri", Onedio "bu hafta vizyona girecek filmler", Paribu Cineverse). Cuma günleri o haftanın tüm yabancı vizyon filmlerini özetleyen "Bu hafta vizyonda" listesi yap (örnek: specs/2026-10-16_vizyon_bu-hafta.json); diğer günler tek film.
- `history.json` → `vizyon` listesindeki filmleri 30 gün içinde tekrar seçme. Auteur, festival, kült ve animasyon filmlerine öncelik ver (`insights/strategy.json`).
- Her olgu (yönetmen, oyuncular, konu, tarih) en az **iki kaynakta** geçmeli; kaynaklar çelişiyorsa o bilgiyi yazma. Spoiler yok.

## 2. Görsel
- Resmî basın karesi bul (WebFetch: "sayfadaki film karesi görsellerinin tam adreslerini ver"; afiş/yazılı görsel hariç, en az 1280 px genişlik).
- `assets/stills/request.json`'a `"vz_<ad>_<n>": "<url>"` ekle, commit + push; "Sahne karelerini indir" iş akışı çalışır, ~60 sn sonra `git pull --rebase`, dosyayı Read ile kontrol et. TMDB iş akışı (tmdb-backdrops.yml) şu an 403/429 veriyor, güvenme.
- Kare yoksa fotoğrafsız tasarım yap (cover + film + rows + cta). Gönderiyi kare yüzünden geciktirme.

## 3. Tasarım (tools/render.py)
- `pill: "VİZYON"`. Tek film: `fullphoto` kapak → `text` (konu) → `rows` "Bilinenler" (yönetmen, oyuncular, tür, vizyon tarihi) → `cta` (soru). Liste: `fullphoto` kapak → `film` ×N → `cta`.
- Her gönderide farklı vurgu rengi (`accent`/`theme`), en az bir slaytta `bg: light` ya da `solid`. İngilizce film adı `film.title`'da olsun (Türkçe adı `meta`'ya yaz); Türkçe başlıkta İngilizce ad varsa `<span lang='en'>`.
- Render: `python3 tools/render.py specs/<YYYY-MM-DD>_vizyon_<kısa-ad>.json`, iletişim sayfasıyla gözle kontrol et (taşma, "İ" hatası, kutu içinde fotoğraf).

## 4. Açıklama
2–3 kısa paragraf: film + konu + vizyon tarihi; "Seans saatleri şehre göre değişir" notu; sonda yoruma çeken tek soru ve `Kaynak: ...`. Hashtag yok.

## 5. Zamanla ve doğrula
1. `schedule.json`'a `{"id","folder","publish_at":"<bugün>T14:00","platforms":["instagram"],"status":"planned","kind":"vizyon"}` ekle, `publish_at`'e göre sırala; `history.json` → `vizyon` listesine `{"date","film","post"}` ekle.
2. `git add` → commit (oturum atıf satırlarıyla) → `git fetch && git rebase origin/main` → `git push`; push'u `schedule.json` ile doğrula.
3. Paylaşım iş akışını tetikle (publish.yml, `dry_run=0`). Script gecikmiş gönderiyi beklemeden paylaşır.
4. 14:03'ten sonra en fazla 15 dk, dakikada bir `schedule.json`'a bak; `published` olunca Ali'ye tek satır: "🎬 14:00 vizyon gönderisi paylaşıldı: <başlık>". `failed` ya da 14:20'de hâlâ `planned` ise bir kez daha tetikle, hatayı incele, Ali'ye kısa uyarı gönder. Gizli anahtarlara dokunma.
5. 13:45'e kadar hazır değilse yanlış/eksik paylaşma: o günü atla, Ali'ye bildir.

# derecefilm otomatik paylaşım

Instagram'a zamanlanmış karusel gönderileri Instagram'ın **resmî API'si** ile paylaşır.
Sunucu gerekmez: GitHub Actions her 15 dakikada bir `schedule.json` dosyasını kontrol eder, zamanı gelen gönderiyi yayınlar.

```
posts/<gönderi>/01.jpg … 10.jpg   → karusel görselleri (en fazla 10, 4:5 önerilir)
posts/<gönderi>/caption.txt       → açıklama
schedule.json                     → ne zaman, hangi platformda
```

`schedule.json` içinde her gönderi:
```json
{ "id": "gun1_liste", "folder": "posts/gun1_liste",
  "publish_at": "2026-10-01T20:00", "platforms": ["instagram"], "status": "planned" }
```
Saatler İstanbul saatidir. Paylaşılınca `status` → `published` olur; hata olursa `failed` ve `error` alanı yazılır.

## Tek seferlik kurulum

### 1. Instagram hesabı
derecefilm **Profesyonel hesap** (İçerik üreticisi ya da İşletme) olmalı: Instagram uygulaması → Ayarlar → Hesap türü ve araçlar.
Facebook sayfası **gerekmez**.

### 2. Meta geliştirici uygulaması
1. https://developers.facebook.com → giriş yap → **Uygulamalarım → Uygulama oluştur**.
2. Kullanım durumu: **"Instagram'da mesajları ve içerikleri yönet"** (Instagram API, Instagram girişi ile).
3. Uygulama **Geliştirme modunda** kalabilir; kendi hesabın için uygulama incelemesi gerekmez.
4. Sol menü → **Instagram → API setup with Instagram login** → **Add account** ile derecefilm'i ekle.
5. **Generate token** → çıkan anahtarı kopyala (bu `IG_TOKEN`). Aynı ekranda hesabın kimlik numarası yazar (bu `IG_USER_ID`).
   İzinler: `instagram_business_basic`, `instagram_business_content_publish`.

### 3. GitHub
1. GitHub'da **herkese açık** bir depo oluştur: `derecefilm-autopost` (görseller Instagram'a buradan okunur).
2. Bu klasördeki tüm dosyaları depoya yükle.
3. Depo → **Settings → Secrets and variables → Actions → New repository secret**:
   - `IG_TOKEN` → 2.5'teki anahtar
   - `IG_USER_ID` → 2.5'teki kimlik
   - `GH_PAT` → GitHub → Settings → Developer settings → Fine-grained tokens → yalnızca bu depo, **Secrets: Read and write** (anahtarın 60 günde bir otomatik yenilenmesi için)
4. **Actions** sekmesi → iş akışlarını etkinleştir.

### 4. Test
Actions → **Zamanı gelen gönderileri paylaş** → **Run workflow** → `dry_run` = `1`.
Hata yoksa gerçek paylaşım zamanlanan saatte kendiliğinden yapılır.

## Claude'un rolü
Claude'a GitHub bağlandığında (claude.ai → Ayarlar → Bağlayıcılar → GitHub) Claude her hafta yeni gönderileri
hazırlayıp `posts/` klasörüne ekler ve `schedule.json`'a tarih/saat yazar. Paylaşımı GitHub Actions yapar.

## Sınırlar
- Instagram API ile günde en fazla 100 paylaşım yapılabilir.
- Görseller JPG olmalı; karusel en fazla 10 görsel.
- Actions zamanlaması birkaç dakika kayabilir (20:00 → 20:00–20:15 arası).

# Günlük haber görevi — derecefilm (her gün 14:00)

Bu dosya, her gün **12:48 (İstanbul)** çalışan zamanlanmış Claude görevinin talimatıdır.
Amaç: o gün **14:00'te** paylaşılacak, güncel sinema dünyasından **tek bir haber** içeren bir Instagram karuseli hazırlamak,
takvime eklemek ve paylaşımın çıktığını doğrulamak. Kullanıcı (Ali) **tamamen otomatik** istedi: onay bekleme.
20:00 gönderilerine (WEEKLY_TASK.md) dokunma.

## 0. Önce kontrol et
`schedule.json`'da bugünün tarihiyle `"kind": "haber"` olan bir kayıt zaten varsa YENİ haber hazırlama:
yalnızca 5. bölümdeki 3–4. adımları uygula (iş akışını tetikle, 14:00 paylaşımını doğrula, Ali'ye bildir).

## 1. Haberi bul (12:48–13:15)
- WebSearch (`mode: "extended"`) ile son 48 saatin sinema haberlerini tara. Aynı turda birkaç arama gönder:
  İngilizce (Variety, The Hollywood Reporter, Deadline, IndieWire, Screen Daily, Netflix/Mubi resmi duyuruları) ve
  Türkçe (Beyazperde, Box Office Türkiye, vizyon haberleri).
- Uygun haber türleri: yeni film duyurusu, fragman, vizyon/platform çıkış tarihi (özellikle Türkiye'de izlenebilecekler: vizyon,
  Netflix, MUBI, Prime, Disney+), festival seçkisi ve ödülleri, gişe rekoru, ünlü bir yönetmenin yeni projesi, restorasyon/yeniden gösterim.
- Hesabın zevkine uygun olanı seç: auteur yönetmenler, festival filmleri, kült/tuhaf filmler, Türk sineması, animasyon.
  Sıradan magazin, dedikodu, siyaset, ölüm/hastalık haberi, söylenti ve doğrulanmamış iddia **SEÇME**.
- **Doğrulama zorunlu:** Gönderideki her olgu (tarih, isim, platform, ödül) en az **iki bağımsız kaynakta** (biri resmi olabilir) geçmeli.
  Emin olmadığın bilgiyi yazma. Haber 48 saatten eski olmasın.
- **Etkileşim önceliği:** `insights/strategy.json` → `top_all`/`top_carousels`'a bak. Haber gönderileri şu an düşük etkileşim alıyor;
  birden fazla aday varsa hesabın en çok tutan temalarına yakın olanı seç (Türk sineması, kült/tuhaf filmler, animasyon,
  izleyicinin bildiği/sevdiği bir filmin devamı ya da yönetmeni). Açıklamanın sonuna yoruma çeken tek bir soru ekle.
- `history.json` → `news` listesindeki konuları tekrar etme. Aynı filme ait bir haberi 30 gün içinde tekrar seçme.

## 2. Görsel
- Haberin geçtiği sayfanın `og:image` adresini (WebFetch ile "sayfadaki og:image adresini ver") ya da resmi basın görselini bul.
  Film karesi / basın fotoğrafı olsun; **afiş üzerinde başka hesabın logosu, filigran, yazı olmasın**. Instagram gönderilerini kopyalama.
- `assets/stills/request.json`'a `"news_<kısa-ad>_1": "<url>"` ekle, commit + push. "Sahne karelerini indir" iş akışı push ile çalışır.
  ~60 sn bekle, `git pull --rebase`, dosyanın geldiğini ve Read ile görselin uygun olduğunu kontrol et.
- Görsel alınamazsa `variant: "plain"` kullan ve kapak zeminini `"bg": "solid"` yap (fotoğrafsız tipografik haber).


- **Görsel kuralı (Ali'nin isteği):** Bir gönderide aynı fotoğraf iki slaytta KULLANILMAZ. Her fotoğraflı slayt farklı bir kare olmalı. Haber için en az 3 farklı film karesi bul (resmi duyuru, festival incelemesi, haber siteleri; WebFetch ile 'sayfadaki film karesi görsellerinin tam adreslerini ver'). 3 kare bulamazsan fotoğrafsız slayt kullan (`rows`, `cta`, `bg: solid/light`), aynı kareyi tekrarlama. Afiş/yazılı görsel kullanma.
- Haberde önemli bilgileri atlama: ödül, festival, Oscar adaylığı gibi bilgileri kaynaklarda özellikle ara.

## 3. Tasarım (tools/render.py, `news` tipi)
- `pill: "HABER"`. Kapak: `{"type": "news", "variant": ..., "nimg": ..., "date": "8 Ekim 2026", "tag": "NETFLIX", "h": "...", "dek": "...", "src": "..."}`
- **Varyant:** bir önceki günün haber kapağıyla AYNI varyantı kullanma (schedule.json'daki son `kind: haber` gönderisinin spec'ine bak). `full` ve `side` yüksek çözünürlüklü (yüksekliği 1000px+) kare ister; düşük çözünürlüklü karede `top` kullan.
  `side` için slayta `"img"` (aynı görsel) ve `"pos"` da ver. Her gün vurgu rengini (`theme`) bir önceki haberden farklı seç.
- 3–4 slayt: kapak → `text` (haberin ayrıntısı, görselli) → `rows` "Bilinenler" (yönetmen, oyuncular, tarih, nerede) → `cta` (soru).
- Başlık (`h`) en fazla ~8 kelime, merak uyandıran ama doğru. `<em>` ile 1–3 kelime vurgula.
- **İ hatası:** `tag`, `src` ve `rows` etiketlerinde İngilizce kelimeleri BÜYÜK HARFLE yaz (NETFLIX, SCREEN DAILY) ya da Türkçe karşılık kullan.
  Başlıkta İngilizce film adı geçerse `<span lang='en'>Ad</span>`.
  `rows.extra` düz metindir; içine HTML yazma.
- Render: `python3 tools/render.py specs/<YYYY-MM-DD>_haber_<kısa-ad>.json`. Taşma uyarısı varsa kısalt. Kapağı Read ile gözle kontrol et.

- **Video slayt (opsiyonel):** `assets/clips/` içinde konuyla uyumlu atmosfer klibi varsa `{"type": "video", "video": "<dosya>.mp4", "lab": ..., "html": ..., "sub": ..., "dur": 8}` ile ekleyebilirsin. Video slaytlar otomatik olarak "Atmosfer görüntüsü · filmden değildir" notu taşır; bu notu kaldırma. Aynı klibi iki farklı gönderide kullanma (history.json → news'e bak).

## 4. Açıklama (caption)
- 2–3 kısa paragraf: haber + ayrıntı + neden önemli/ne zaman izlenebilir. Sonunda `Kaynak: <yayın adları>`.
- "Yarın 20:00'de" devamlılık satırı EKLEME (o satır akşam gönderilerine ait). Hashtag yok.

## 5. Zamanla, paylaş, doğrula
1. `schedule.json`'a ekle: `{"id": "<id>", "folder": "posts/<id>", "publish_at": "<bugün>T14:00", "platforms": ["instagram"], "status": "planned", "kind": "haber"}`
   ve listeyi `publish_at`'e göre sırala. `history.json` → `news` listesine `{"date", "title", "film", "post"}` ekle.
2. `git add` (spec, posts/<id>, schedule.json, history.json) → commit (oturum atıf satırlarıyla) → `git pull --rebase` → `git push`.
   Push'un gerçekten gittiğini `gh api repos/alibal123/Ali/contents/schedule.json` ile doğrula.
3. Paylaşım iş akışını tetikle: `gh api -X POST repos/alibal123/Ali/actions/workflows/publish.yml/dispatches -f ref=main -f 'inputs[dry_run]=0'`
   (İş akışı 14:00'e kadar kendisi bekler; çift paylaşım koruması vardır.)
4. 14:03'e kadar bekle, sonra en fazla 15 dakika boyunca dakikada bir schedule.json'daki durumu kontrol et.
   `published` olunca Ali'ye SendUserMessage ile tek satır gönder: "📰 14:00 haberi paylaşıldı: <başlık>".
   `failed` ya da 14:20'de hâlâ `planned` ise iş akışını bir kez daha tetikle, hatayı (schedule.json `error`, son çalışmalar) incele ve
   Ali'ye kısa bir uyarı gönder. Gizli anahtarlara (IG_TOKEN vb.) asla dokunma.
5. Saat 13:45'i geçmesine rağmen gönderi hazır değilse aceleyle yanlış/eksik bir şey paylaşma: o günü atla ve Ali'ye bildir.

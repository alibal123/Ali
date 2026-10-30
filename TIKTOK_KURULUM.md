# TikTok kurulumu (derecefilm)

Uygulama: derecefilm (App ID 7702500822093400084), TikTok geliştirici paneli, Production.

## GitHub Pages
- Ayar: Settings > Pages > Source: Deploy from a branch > main / (root)
- Adres: https://alibal123.github.io/Ali/

## TikTok panelindeki alanlar
- Terms of Service URL: https://alibal123.github.io/Ali/terms/
- Privacy Policy URL: https://alibal123.github.io/Ali/privacy/
- Platform: Web
- Redirect URI (Login Kit): https://alibal123.github.io/Ali/callback/
- URL prefix doğrulaması: https://alibal123.github.io/Ali/ (imza dosyası kökte)
- Products: Login Kit + Content Posting API
- Scopes: user.info.basic, video.publish
- Medya alan adı (photo post URL prefix): https://alibal123.github.io/Ali/ ; TIKTOK_MEDIA_BASE = https://alibal123.github.io/Ali

## GitHub Secrets / Variables
Secrets: TIKTOK_CLIENT_KEY, TIKTOK_CLIENT_SECRET, TIKTOK_ACCESS_TOKEN, TIKTOK_REFRESH_TOKEN
Variables: TIKTOK_MEDIA_BASE, TIKTOK_PRIVACY (denetim bitene kadar SELF_ONLY)

## Token üretme
python tools/tiktok_auth.py link, ardından python tools/tiktok_auth.py kod "<code>"

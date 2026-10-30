"""TikTok yetkilendirme yardımcısı (bilgisayarında bir kez çalıştırılır; anahtarlar depoya YAZILMAZ).

Kullanım:
  export TIKTOK_CLIENT_KEY=...  TIKTOK_CLIENT_SECRET=...  TIKTOK_REDIRECT_URI=https://.../callback
  python tools/tiktok_auth.py link            # 1) tarayıcıda açılacak izin bağlantısını yazdırır
  python tools/tiktok_auth.py kod "<code>"    # 2) dönen adresteki code değeriyle anahtarları üretir
Çıkan access_token / refresh_token değerlerini GitHub > Settings > Secrets bölümüne elle ekle.
"""
import json, os, sys, urllib.parse, urllib.request

KEY = os.environ["TIKTOK_CLIENT_KEY"]
REDIRECT = os.environ["TIKTOK_REDIRECT_URI"]
SCOPE = "user.info.basic,video.publish"

if sys.argv[1] == "link":
    q = urllib.parse.urlencode({"client_key": KEY, "scope": SCOPE, "response_type": "code",
                                "redirect_uri": REDIRECT, "state": "derecefilm"})
    print("https://www.tiktok.com/v2/auth/authorize/?" + q)
else:
    code = urllib.parse.unquote(sys.argv[2])
    data = urllib.parse.urlencode({"client_key": KEY, "client_secret": os.environ["TIKTOK_CLIENT_SECRET"],
                                   "code": code, "grant_type": "authorization_code", "redirect_uri": REDIRECT}).encode()
    req = urllib.request.Request("https://open.tiktokapis.com/v2/oauth/token/", data=data,
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    r = json.load(urllib.request.urlopen(req, timeout=60))
    print("access_token :", r.get("access_token"))
    print("refresh_token:", r.get("refresh_token"))
    print("ham yanıt    :", {k: v for k, v in r.items() if "token" not in k})

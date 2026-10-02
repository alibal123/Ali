"""Hesabın son gönderilerinin beğeni/yorum verilerini insights/media.json'a yazar (analiz için)."""
import json, os, urllib.parse, urllib.request

API = "https://graph.instagram.com/v21.0"
TOKEN = os.environ["IG_TOKEN"]
LIMIT = int(os.environ.get("MAX_MEDIA", "200"))


def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


me = get(f"{API}/me?" + urllib.parse.urlencode({"fields": "username,followers_count,follows_count,media_count", "access_token": TOKEN}))
items = []
url = f"{API}/me/media?" + urllib.parse.urlencode({
    "fields": "id,caption,media_type,media_product_type,timestamp,like_count,comments_count,permalink",
    "limit": "50", "access_token": TOKEN})
while url and len(items) < LIMIT:
    page = get(url)
    items += page.get("data", [])
    url = page.get("paging", {}).get("next")
for m in items:
    m["caption"] = (m.get("caption") or "")[:400]
os.makedirs("insights", exist_ok=True)
json.dump({"account": me, "media": items[:LIMIT]}, open("insights/media.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"@{me.get('username')}: {me.get('followers_count')} takipçi, {len(items[:LIMIT])} gönderi kaydedildi")

"""derecefilm otomatik paylaşım: schedule.json'da zamanı gelen gönderileri Instagram'a karusel olarak yayınlar.

GitHub Actions her 15 dakikada bir çalıştırır. Gerekli gizli değişkenler (repo > Settings > Secrets):
  IG_TOKEN   : Instagram uzun ömürlü erişim anahtarı (Instagram Login ile, instagram_business_content_publish izni)
  IG_USER_ID : Instagram hesap kimliği
Görseller herkese açık adresten okunur: https://raw.githubusercontent.com/<repo>/<branch>/<dosya>
"""
import json, os, sys, time, urllib.parse, urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

API = "https://graph.instagram.com/v21.0"
TOKEN = os.environ["IG_TOKEN"]
IG_USER = os.environ["IG_USER_ID"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = os.environ.get("GITHUB_REF_NAME", "main")
RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"
DRY = os.environ.get("DRY_RUN") == "1"
LATE_LIMIT = timedelta(hours=6)  # 6 saatten fazla gecikmiş gönderiyi atla, kullanıcıya bırak


def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    if method == "GET":
        req = urllib.request.Request(f"{API}/{path}?{data.decode()}")
    else:
        req = urllib.request.Request(f"{API}/{path}", data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path}: {e.code} {e.read().decode()[:500]}")


def wait_ready(container_id):
    for _ in range(30):
        s = call("GET", container_id, fields="status_code,status").get("status_code")
        if s == "FINISHED":
            return
        if s in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"container {container_id} durumu: {s}")
        time.sleep(5)
    raise RuntimeError(f"container {container_id} zamanında hazır olmadı")


def publish_instagram(post):
    folder = post["folder"]
    images = sorted(f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".jpeg")))[:10]
    caption = open(os.path.join(folder, "caption.txt"), encoding="utf-8").read().strip()
    urls = [f"{RAW}/{folder}/{urllib.parse.quote(f)}" for f in images]
    print(f"[{post['id']}] {len(urls)} görsel, açıklama {len(caption)} karakter")
    if DRY:
        return "dry-run"
    if len(urls) == 1:
        c = call("POST", f"{IG_USER}/media", image_url=urls[0], caption=caption)["id"]
    else:
        children = []
        for u in urls:
            cid = call("POST", f"{IG_USER}/media", image_url=u, is_carousel_item="true")["id"]
            wait_ready(cid)
            children.append(cid)
        c = call("POST", f"{IG_USER}/media", media_type="CAROUSEL", children=",".join(children), caption=caption)["id"]
    wait_ready(c)
    return call("POST", f"{IG_USER}/media_publish", creation_id=c)["id"]


def check():
    """Paylaşım yapmadan: anahtar geçerli mi, hesap doğru mu, görseller herkese açık mı?"""
    me = call("GET", "me", fields="user_id,username,account_type")
    print(f"Anahtar geçerli → hesap: @{me.get('username')} ({me.get('account_type')}), id {me.get('user_id')}")
    if str(me.get("user_id")) != str(IG_USER.strip()):
        print(f"UYARI: IG_USER_ID ({IG_USER}) hesapla eşleşmiyor ({me.get('user_id')})")
    sched = json.load(open("schedule.json", encoding="utf-8"))
    for post in sched["posts"]:
        f = sorted(x for x in os.listdir(post["folder"]) if x.endswith(".jpg"))[0]
        u = f"{RAW}/{post['folder']}/{f}"
        with urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30) as r:
            print(f"[{post['id']}] {post['publish_at']} → görsel erişilebilir ({r.status}, {r.headers.get('Content-Type')})")
    print("KONTROL TAMAM")


def main():
    if DRY:
        check()
        return
    sched = json.load(open("schedule.json", encoding="utf-8"))
    tz = ZoneInfo(sched.get("timezone", "Europe/Istanbul"))
    now = datetime.now(tz)
    changed = False
    for post in sched["posts"]:
        if post.get("status") != "planned":
            continue
        at = datetime.fromisoformat(post["publish_at"]).replace(tzinfo=tz)
        if at > now:
            continue
        if now - at > LATE_LIMIT:
            post["status"] = "skipped_late"
            changed = True
            print(f"[{post['id']}] çok gecikti, atlandı")
            continue
        results = post.setdefault("results", {})
        try:
            if "instagram" in post["platforms"] and "instagram" not in results:
                results["instagram"] = publish_instagram(post)
            post["status"] = "published"
            post["published_at"] = now.isoformat(timespec="minutes")
        except Exception as e:
            post["status"] = "failed"
            post["error"] = str(e)[:500]
            print(f"[{post['id']}] HATA: {e}", file=sys.stderr)
        changed = True
    if changed and not DRY:
        json.dump(sched, open("schedule.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if any(p.get("status") == "failed" for p in sched["posts"]):
        sys.exit(1)


if __name__ == "__main__":
    main()

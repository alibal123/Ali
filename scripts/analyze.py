"""Etkileşim analizi: insights/media.json + schedule.json → insights/strategy.json ve insights/RAPOR.md

Her gün (insights.yml) çalışır. Haftalık ve haber görevleri strategy.json'daki ağırlıklara göre format seçer.
Puan = beğeni + 3 × yorum. 48 saatten genç gönderiler henüz olgunlaşmadığı için puanlamaya girmez.
Az örnekli formatlar genel medyana doğru çekilir (k=2), böylece tek bir şans eseri gönderi her şeyi belirlemez.
"""
import json, re, statistics as st
from datetime import datetime, timedelta, timezone

MIN_AGE = timedelta(hours=48)
K = 2               # küçültme (shrinkage) katsayısı
POWER = 0.75        # <1: tek bir viral gönderinin etkisini yumuşatır; puanı olmayan (yeni) format genel medyanla denenir
WEEK_SLOTS = 7
MAX_PER_FMT = 3

# id → format (spec'teki pill'den daha güvenilir: eski gönderilerin spec'i yok)
FORMAT_RULES = [
    (r"liste", "LİSTE"), (r"eslesme", "EŞLEŞTİRME"), (r"_film_|incendies|jagten", "FİLM"),
    (r"haber", "HABER"), (r"oyun", "OYUN"), (r"veri", "VERİ"), (r"karsilastirma", "KARŞILAŞTIRMA"),
    (r"sahne", "SAHNE"), (r"belgesel", "BELGESEL"), (r"reel", "REEL"),
]


def fmt_of(pid):
    for pat, name in FORMAT_RULES:
        if re.search(pat, pid):
            return name
    return "DİĞER"


def score(m):
    return (m.get("like_count") or 0) + 3 * (m.get("comments_count") or 0)


def ts(m):
    return datetime.strptime(m["timestamp"], "%Y-%m-%dT%H:%M:%S%z")


def main():
    now = datetime.now(timezone.utc)
    data = json.load(open("insights/media.json", encoding="utf-8"))
    media = data["media"]
    by_id = {m["id"]: m for m in media}
    sched = json.load(open("schedule.json", encoding="utf-8"))

    # 1) Otomatik gönderiler: format bazında
    rows = []
    for p in sched["posts"]:
        mid = (p.get("results") or {}).get("instagram")
        m = by_id.get(str(mid)) if mid else None
        if not m:
            continue
        age = now - ts(m)
        rows.append({"id": p["id"], "format": fmt_of(p["id"]), "slot": p["publish_at"][11:16],
                     "likes": m.get("like_count", 0), "comments": m.get("comments_count", 0),
                     "score": score(m), "age_h": int(age.total_seconds() // 3600), "mature": age >= MIN_AGE})
    mature = [r for r in rows if r["mature"]]
    gmed = st.median([r["score"] for r in mature]) if mature else 0
    fmts = {}
    for f in sorted({r["format"] for r in rows}):
        xs = [r["score"] for r in mature if r["format"] == f]
        n = len(xs)
        med = st.median(xs) if xs else None
        adj = ((n * med + K * gmed) / (n + K)) if n else gmed
        fmts[f] = {"n": n, "median": med, "best": max(xs) if xs else None, "adjusted": round(adj, 1)}

    # 2) Haftalık 20:00 slot dağılımı (HABER 14:00 slotunda ayrı yönetilir).
    # Ali çeşitlilik istiyor: bir format haftada en fazla MAX_PER_FMT kez.
    evening = {f: v for f, v in fmts.items() if f != "HABER"}
    lw = {f: v["adjusted"] ** POWER for f, v in evening.items()}
    tot = sum(lw.values()) or 1
    weights = {f: round(lw[f] / tot, 3) for f in evening}
    ranked = sorted(weights, key=lambda f: -weights[f])
    # en büyük kalan yöntemi + üst sınır: önce tam kısımlar, sonra kalan slotlar en büyük kesirlere
    want = {f: weights[f] * WEEK_SLOTS for f in ranked}
    plan = {f: min(MAX_PER_FMT, int(want[f])) for f in ranked}
    for f in sorted(ranked, key=lambda f: -(want[f] - int(want[f]))) + ranked:
        if sum(plan.values()) >= WEEK_SLOTS:
            break
        if plan[f] < MAX_PER_FMT and (plan[f] == int(want[f]) or f in ranked[:1]):
            plan[f] += 1
    plan = {f: n for f, n in plan.items() if n}

    # 3) Tüm hesap: medya türü ve en çok tutanlar (tema ipuçları için)
    types = {}
    for m in media:
        k = "REELS" if m.get("media_product_type") == "REELS" else m["media_type"]
        types.setdefault(k, []).append(score(m))
    type_stats = {k: {"n": len(v), "median": st.median(v), "mean": round(st.mean(v))} for k, v in types.items()}
    top = sorted(media, key=lambda m: -score(m))[:20]
    top_list = [{"date": m["timestamp"][:10], "type": m.get("media_product_type"), "likes": m.get("like_count"),
                 "comments": m.get("comments_count"), "caption": (m.get("caption") or "").split("\n")[0][:110],
                 "permalink": m.get("permalink")} for m in top]
    car = sorted([m for m in media if m["media_type"] == "CAROUSEL_ALBUM"], key=lambda m: -score(m))[:8]
    top_car = [{"date": m["timestamp"][:10], "likes": m.get("like_count"), "comments": m.get("comments_count"),
                "caption": (m.get("caption") or "").split("\n")[0][:110]} for m in car]

    out = {"generated_at": now.isoformat(timespec="minutes"), "followers": data["account"].get("followers_count"),
           "scoring": "beğeni + 3×yorum; 48 saatten genç gönderiler hariç",
           "formats": fmts, "evening_weights": weights, "weekly_plan_20_00": plan,
           "ranking": ranked, "media_types": type_stats, "posts": rows,
           "top_all": top_list, "top_carousels": top_car}
    json.dump(out, open("insights/strategy.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    L = [f"# Etkileşim raporu — {now:%Y-%m-%d}", "",
         f"Takipçi: {out['followers']} · Puan = beğeni + 3×yorum · 48 saatten genç gönderiler puana girmez.", "",
         "## Format sıralaması (otomatik gönderiler)", "", "| Format | Gönderi | Medyan | En iyi | Düzeltilmiş puan | Haftalık 20:00 slotu |",
         "|---|---|---|---|---|---|"]
    for f in sorted(fmts, key=lambda f: -fmts[f]["adjusted"]):
        v = fmts[f]
        L.append(f"| {f} | {v['n']} | {v['median'] if v['median'] is not None else '-'} | {v['best'] if v['best'] is not None else '-'} | {v['adjusted']} | {plan.get(f, '-' if f == 'HABER' else 0)} |")
    L += ["", "## Medya türü (son 200 gönderi)", ""]
    for k, v in type_stats.items():
        L.append(f"- {k}: {v['n']} gönderi, medyan {v['median']}, ortalama {v['mean']}")
    L += ["", "## En çok etkileşim alan karuseller", ""]
    for m in top_car:
        L.append(f"- {m['date']} · {m['likes']} beğeni / {m['comments']} yorum · {m['caption']}")
    L += ["", "## Hesabın en çok tutan 10 gönderisi", ""]
    for m in top_list[:10]:
        L.append(f"- {m['date']} {m['type']} · {m['likes']} beğeni · {m['caption']}")
    L += ["", "## Gönderi bazında (otomatik)", "", "| Gönderi | Format | Saat | Beğeni | Yorum | Yaş (saat) |", "|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r["id"]):
        L.append(f"| {r['id']} | {r['format']} | {r['slot']} | {r['likes']} | {r['comments']} | {r['age_h']}{'' if r['mature'] else ' (yeni)'} |")
    open("insights/RAPOR.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("Haftalık 20:00 planı:", plan)


if __name__ == "__main__":
    main()

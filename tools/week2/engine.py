"""render2 üzerine: yazıyı kutuya otomatik sığdırır, taşma / kenar boşluğu / çakışma denetimi yapar. Sorun varsa hata verir."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from playwright.sync_api import sync_playwright
import render2

JS = """() => {
  const issues = [];
  const els = [...document.querySelectorAll('.t')];
  for (const el of els) {
    const cs = getComputedStyle(el);
    if (cs.getPropertyValue('--fit').trim() === '1') {
      const H = parseFloat(cs.getPropertyValue('--h'));
      const mn = parseFloat(cs.getPropertyValue('--min') || '20');
      let fs = parseFloat(cs.fontSize);
      const over = () => el.scrollHeight > H + 1 || el.scrollWidth > el.clientWidth + 1;
      while (over() && fs > mn) { fs -= 2; el.style.fontSize = fs + 'px'; }
      if (over()) issues.push('SIĞMADI: ' + el.innerText.slice(0, 50));
    }
  }
  const rects = els.map(el => { const r = document.createRange(); r.selectNodeContents(el); const b = r.getBoundingClientRect(); return {b, t: el.innerText.slice(0, 40), bleed: getComputedStyle(el).getPropertyValue('--bleed').trim() === '1'}; });
  for (const o of rects) {
    if (o.b.width === 0 || o.bleed) continue;
    if (o.b.left < 56 || o.b.right > 1024 || o.b.bottom > 1318 || o.b.top < 24) issues.push('KENAR: ' + o.t + ' [' + Math.round(o.b.left) + ',' + Math.round(o.b.top) + ',' + Math.round(o.b.right) + ',' + Math.round(o.b.bottom) + ']');
  }
  for (let i = 0; i < rects.length; i++) for (let j = i + 1; j < rects.length; j++) {
    const a = rects[i].b, b = rects[j].b;
    if (a.width === 0 || b.width === 0 || rects[i].bleed || rects[j].bleed) continue;
    const ix = Math.min(a.right, b.right) - Math.max(a.left, b.left), iy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
    if (ix > 3 && iy > 3) issues.push('ÇAKIŞMA: ' + rects[i].t + ' <> ' + rects[j].t);
  }
  return issues;
}"""


def render(spec, outroot=None):
    out = os.path.join(outroot or os.path.join(render2.REPO, "posts"), spec["id"])
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f[:2].isdigit() and f.endswith(".jpg"):
            os.remove(os.path.join(out, f))
    bad = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": render2.W, "height": render2.HGT})
        for i, s in enumerate(spec["slides"], 1):
            tmp = os.path.join(render2.HERE, "_slide.html")
            open(tmp, "w").write(render2.slide_html(s))
            pg.goto("file://" + tmp, wait_until="load")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(400)
            issues = pg.evaluate(JS)
            pg.wait_for_timeout(100)
            for m in issues:
                bad.append(f"slayt {i}: {m}")
            pg.screenshot(path=os.path.join(out, f"{i:02d}.jpg"), type="jpeg", quality=94)
        b.close()
    open(os.path.join(out, "caption.txt"), "w").write(spec["caption"].strip() + "\n")
    print(f"{spec['id']}: {len(spec['slides'])} slayt → {out}")
    for m in bad:
        print("  UYARI", m)
    return out, bad

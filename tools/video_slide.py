"""Video slayt: bir klibi 1080x1350 (4:5) karusel videosuna çevirir ve üstüne Derece Film yazı katmanı bindirir.

Kullanım (render.py'den çağrılır ya da tek başına):
  from video_slide import make_video_slide
  make_video_slide(src_mp4, out_mp4, spec, slide, idx, total)

slide alanları:
  type: "video", video: "<assets/clips içindeki dosya>", lab, html (kısa metin), accent, pos ("top"|"bottom"), start (sn), dur (sn, varsayılan 8)
"""
import os, subprocess, tempfile
from playwright.sync_api import sync_playwright
import render as R

OVERLAY_CSS = R.CSS + """
html,body{background:transparent!important}
body .glow,body .noise{display:none}
.shade{position:absolute;left:0;right:0;height:640px;pointer-events:none}
.shade.b{bottom:0;background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.55) 40%,rgba(0,0,0,.88) 100%)}
.shade.t{top:0;height:300px;background:linear-gradient(180deg,rgba(0,0,0,.6),rgba(0,0,0,0))}
.vmain{flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding-bottom:26px;position:relative;z-index:2}
.vmain.top{justify-content:flex-start;padding-top:40px}
.vlab{font-family:Oswald;font-weight:500;font-size:28px;letter-spacing:.24em;color:var(--a);margin-bottom:22px;text-transform:uppercase}
.vtxt{font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:62px;line-height:1.2;color:#fff;text-shadow:0 2px 20px rgba(0,0,0,.6)}
.vtxt b{color:var(--a);font-weight:800}
.vsub{font-family:Inter;font-weight:500;font-size:32px;line-height:1.4;color:#eee;margin-top:20px;text-shadow:0 2px 14px rgba(0,0,0,.7)}
.ai{font-family:Oswald;font-size:18px;letter-spacing:.18em;color:rgba(255,255,255,.55);margin-top:18px;text-transform:uppercase}
"""


def overlay_html(spec, s, idx, total):
    accent = R.col(s.get("accent")) or R.col(spec.get("theme", "red"))
    pos = s.get("pos", "bottom")
    swipe = "<b>KAYDIR →</b>" if idx < total else ""
    sub = f'<div class="vsub">{s["sub"]}</div>' if s.get("sub") else ""
    note = '<div class="ai">Atmosfer görüntüsü · filmden değildir</div>'
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{OVERLAY_CSS}</style></head>
<body style="--a:{accent};--a2:{R.rgba(accent,.2)};--ad:#b8432f"><div class="shade t"></div><div class="shade b"></div>
<div class="frame"><div class="top"><div class="brand">DERECE FİLM</div><div class="pill">{R.e(spec['pill'])}</div></div>
<div class="vmain {pos}"><div class="vlab">{R.e(s.get("lab",""))}</div><div class="vtxt">{s["html"]}</div>{sub}{note}</div>
<div class="bot"><div>@derecefilm &nbsp;·&nbsp; {idx:02d}/{total:02d}</div><div>{swipe}</div></div>
</div></body></html>"""


def make_video_slide(src, out, spec, s, idx, total, page=None):
    tmpd = tempfile.mkdtemp()
    html_p = os.path.join(tmpd, "o.html")
    png_p = os.path.join(tmpd, "o.png")
    open(html_p, "w", encoding="utf-8").write(overlay_html(spec, s, idx, total))
    own = page is None
    if own:
        pw = sync_playwright().start(); b = pw.chromium.launch()
        page = b.new_page(viewport={"width": 1080, "height": 1350})
    page.goto("file://" + html_p, wait_until="networkidle")
    page.evaluate("document.fonts.ready.then(()=>1)")
    page.wait_for_timeout(200)
    page.screenshot(path=png_p, omit_background=True)
    if own:
        b.close(); pw.stop()
    start, dur = float(s.get("start", 0)), float(s.get("dur", 8))
    focus = s.get("focus", "center")  # dikey kırpma odağı: center | top | bottom
    y = {"top": "0", "bottom": "ih-1350", "center": "(ih-1350)/2"}[focus]
    vf = (f"[0:v]scale=1080:-2:flags=lanczos,crop=1080:1350:0:{y},fps=30,"
          f"fade=t=in:st=0:d=0.4,fade=t=out:st={dur-0.5}:d=0.5[v];[v][1:v]overlay=0:0,format=yuv420p[o]")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-ss", str(start), "-t", str(dur), "-i", src, "-i", png_p,
           "-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=44100:cl=stereo",
           "-filter_complex", vf, "-map", "[o]", "-map", "2:a", "-c:v", "libx264", "-profile:v", "high", "-preset", "slow",
           "-crf", "19", "-maxrate", "8M", "-bufsize", "16M", "-c:a", "aac", "-b:a", "96k", "-shortest",
           "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    # Önizleme karesi
    pv = os.path.join(os.path.dirname(out), "_onizleme")
    os.makedirs(pv, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(min(3, dur / 2)), "-i", out, "-frames:v", "1",
                    os.path.join(pv, os.path.basename(out)[:-4] + ".jpg")], check=True)
    return out

"""Kullanım: python3 tools/week2/run.py p01 [p02 ...]   → posts/<id>/ üretir, uyarıları yazar, /tmp/sheet_<ad>.jpg iletişim sayfası"""
import importlib, os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from PIL import Image
import engine

allbad = 0
for name in sys.argv[1:]:
    mod = importlib.import_module(name)
    spec = mod.build()
    if hasattr(mod, 'LOGO'):
        import pro
        spec['slides'] = pro.relogo(spec['slides'], **mod.LOGO)
    out, bad = engine.render(spec)
    allbad += len(bad)
    fs = sorted(glob.glob(os.path.join(out, "*.jpg")))
    cols = 4 if len(fs) > 6 else 3
    rows = (len(fs) + cols - 1) // cols
    sw, sh = 300, 375
    sheet = Image.new("RGB", (sw * cols, sh * rows), "white")
    for i, f in enumerate(fs):
        sheet.paste(Image.open(f).resize((sw, sh)), ((i % cols) * sw, (i // cols) * sh))
    sheet.save(f"/tmp/sheet_{name}.jpg")
print("TOPLAM UYARI:", allbad)

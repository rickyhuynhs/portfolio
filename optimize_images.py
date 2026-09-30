#!/usr/bin/env python3
"""Run in the folder with your site images:  pip install pillow && python3 optimize_images.py
Creates a compressed .webp next to every .png/.jpg (originals untouched).
index.html already points at the .webp names and falls back to the originals if a .webp is missing."""
import os
from PIL import Image
MAX_W = {"headshot": 1000, "logo": 500}   # headshot wider, logos small
for f in os.listdir("."):
    stem, ext = os.path.splitext(f)
    if ext.lower() not in (".png", ".jpg", ".jpeg"): continue
    im = Image.open(f)
    low = stem.lower()
    is_logo = any(k in low for k in ("aasa","altitude","artem","asa","baaff","bl","boston_little","lu","aarw","robert","threecircles","vsa","wave"))
    limit = 1000 if "headshot" in low else (500 if is_logo else 1280)
    if im.width > limit:
        im = im.resize((limit, round(im.height * limit / im.width)), Image.LANCZOS)
    im = im.convert("RGBA" if im.mode in ("RGBA","LA","P") else "RGB")
    out = stem + ".webp"
    im.save(out, "WEBP", quality=80, method=6)
    print(f"{f}: {os.path.getsize(f)//1024} KB -> {os.path.getsize(out)//1024} KB")

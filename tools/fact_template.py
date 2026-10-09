"""Single-image "SEMICONDUCTOR FACTS #N" post in the account owner's own design.

Usage (from tools/):  OUT_DIR=./out python3 -I fact_template.py fact.json
fact.json keys: num, line1 (cyan), line2 (white), line3 (purple), body, highlight,
  benefits[3] (2-line labels, '\n' separated), bottom[4] ([icon, label]), scene
  (euv|chip|wafer), scene_notes{...}, tagline (2 lines '\n'), file (output name)
"""
import sys, json, math, random
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from design_helpers import *

LINEC = (70, 100, 190)
PURPLE = (170, 120, 255)


def P(v):
    return int(v * S)


def fit(text, name, maxsize, maxw):
    size = maxsize
    while size > 20 and F(name, size).getlength(text) > maxw * S:
        size -= 2
    return F(name, size), size


def note(img, x, y, text, angle=0, size=30, color=CYAN, align="left"):
    """Handwriting-style annotation (italic), optionally rotated."""
    f = F("Inter-MediumItalic.otf", size)
    lines = text.split("\n")
    w = max(f.getlength(l) for l in lines) / S
    h = len(lines) * size * 1.25
    layer = Image.new("RGBA", (P(w + 20), P(h + 20)), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for i, l in enumerate(lines):
        lx = 10 if align == "left" else (w - f.getlength(l) / S) / 2 + 10
        d.text((P(lx), P(10 + i * size * 1.25)), l, font=f, fill=color)
    if angle:
        layer = layer.rotate(angle, expand=True, resample=Image.BICUBIC)
    img.paste(layer, (P(x), P(y)), layer)


def arrow(img, pts, color=WHITE, width=3):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.line([(P(a), P(b)) for a, b in pts], fill=color + (230,), width=P(width), joint="curve")
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    a = math.atan2(y1 - y0, x1 - x0)
    for s in (2.6, -2.6):
        d.line([(P(x1), P(y1)), (P(x1 - 16 * math.cos(a + s * 0.2 * 1)), P(y1 - 16 * math.sin(a + s * 0.2 * 1)))],
               fill=color + (230,), width=P(width))
    img.paste(layer, (0, 0), layer)


# ---------------- line icons ----------------
def icon(img, kind, cx, cy, r=26, color=MUTED, w=3):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    c = color + (255,)
    L = lambda *p: d.line([(P(p[i]), P(p[i + 1])) for i in range(0, len(p), 2)], fill=c, width=P(w), joint="curve")
    box = lambda x0, y0, x1, y1, rad=6: d.rounded_rectangle([P(x0), P(y0), P(x1), P(y1)], radius=P(rad), outline=c, width=P(w))
    if kind == "gauge":
        d.arc([P(cx - r), P(cy - r), P(cx + r), P(cy + r)], 180, 360, fill=c, width=P(w))
        L(cx - r, cy, cx + r, cy)
        L(cx, cy, cx + r * 0.6, cy - r * 0.6)
    elif kind == "bolt":
        L(cx + 6, cy - r, cx - 12, cy + 4, cx + 2, cy + 4, cx - 8, cy + r)
    elif kind == "chip":
        box(cx - r * 0.6, cy - r * 0.6, cx + r * 0.6, cy + r * 0.6, 5)
        for k in (-0.3, 0.3):
            L(cx + k * r, cy - r * 0.6, cx + k * r, cy - r * 0.95)
            L(cx + k * r, cy + r * 0.6, cx + k * r, cy + r * 0.95)
            L(cx - r * 0.6, cy + k * r, cx - r * 0.95, cy + k * r)
            L(cx + r * 0.6, cy + k * r, cx + r * 0.95, cy + k * r)
    elif kind == "ai":
        box(cx - r * 0.6, cy - r * 0.6, cx + r * 0.6, cy + r * 0.6, 5)
        for k in (-0.3, 0.3):
            L(cx + k * r, cy - r * 0.6, cx + k * r, cy - r * 0.95)
            L(cx + k * r, cy + r * 0.6, cx + k * r, cy + r * 0.95)
            L(cx - r * 0.6, cy + k * r, cx - r * 0.95, cy + k * r)
            L(cx + r * 0.6, cy + k * r, cx + r * 0.95, cy + k * r)
        d.text((P(cx - 13), P(cy - 14)), "AI", font=F("Inter-ExtraBold.otf", 22), fill=c)
    elif kind == "phone":
        box(cx - r * 0.45, cy - r, cx + r * 0.45, cy + r, 7)
        L(cx - 5, cy + r - 8, cx + 5, cy + r - 8)
    elif kind == "server":
        for k in (-1, 0, 1):
            y = cy + k * r * 0.62
            box(cx - r, y - r * 0.24, cx + r, y + r * 0.24, 4)
            d.ellipse([P(cx + r * 0.55), P(y - 3), P(cx + r * 0.55 + 6), P(y + 3)], fill=c)
    elif kind == "laptop":
        box(cx - r * 0.8, cy - r * 0.7, cx + r * 0.8, cy + r * 0.3, 4)
        L(cx - r, cy + r * 0.62, cx + r, cy + r * 0.62)
    elif kind == "camera":
        box(cx - r, cy - r * 0.6, cx + r, cy + r * 0.7, 7)
        d.ellipse([P(cx - r * 0.4), P(cy - r * 0.3), P(cx + r * 0.4), P(cy + r * 0.5)], outline=c, width=P(w))
    elif kind == "battery":
        box(cx - r, cy - r * 0.45, cx + r * 0.85, cy + r * 0.45, 5)
        L(cx + r * 0.85 + 4, cy - 6, cx + r * 0.85 + 4, cy + 6)
        d.rectangle([P(cx - r + 6), P(cy - r * 0.25), P(cx - 2), P(cy + r * 0.25)], fill=c)
    elif kind == "gamepad":
        box(cx - r, cy - r * 0.5, cx + r, cy + r * 0.55, 14)
        L(cx - r * 0.5, cy - 8, cx - r * 0.5, cy + 8)
        L(cx - r * 0.5 - 8, cy, cx - r * 0.5 + 8, cy)
        d.ellipse([P(cx + r * 0.35), P(cy - 6), P(cx + r * 0.35 + 8), P(cy + 2)], fill=c)
    elif kind == "wave":
        pts = [(cx - r + i * 4, cy + math.sin(i * 0.9) * r * 0.5) for i in range(int(2 * r / 4) + 1)]
        d.line([(P(a), P(b)) for a, b in pts], fill=c, width=P(w), joint="curve")
    img.paste(layer, (0, 0), layer)


# ---------------- scenes (magnified circle + hero) ----------------
CIRC = (770, 915, 205)  # cx, cy, r


def circle_frame(img, content_fn):
    cx, cy, r = CIRC
    glow(img, cx, cy, r * 1.15, CYAN, 55)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    inner = Image.new("RGBA", img.size, (6, 10, 28, 255))
    content_fn(inner)
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).ellipse([P(cx - r), P(cy - r), P(cx + r), P(cy + r)], fill=255)
    layer.paste(inner, (0, 0), mask)
    img.paste(layer, (0, 0), layer)
    d = ImageDraw.Draw(img)
    for k, a in ((0, 255), (6, 120), (12, 50)):
        d.ellipse([P(cx - r - k), P(cy - r - k), P(cx + r + k), P(cy + r + k)], outline=CYAN + (a,), width=P(3))


def cone(img, x, y, to_side=-1):
    cx, cy, r = CIRC
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.polygon([(P(x), P(y)), (P(cx - r * 0.8), P(cy - r * 0.62)), (P(cx - r * 0.8), P(cy + r * 0.62))],
              fill=CYAN + (28,))
    d.line([(P(x), P(y)), (P(cx - r * 0.8), P(cy - r * 0.62))], fill=CYAN + (170,), width=P(2))
    d.line([(P(x), P(y)), (P(cx - r * 0.8), P(cy + r * 0.62))], fill=CYAN + (170,), width=P(2))
    img.paste(layer, (0, 0), layer)



def callouts(img, notes, caption, flash, scale):
    cx, cy, r = CIRC
    rrect(img, (700, 585, 1024, 695), 14, fill=(10, 16, 40), alpha=240, outline=(60, 80, 140), width=2)
    d = ImageDraw.Draw(img)
    text_block(d, 720, 597, notes.get("caption", caption), F("Inter-SemiBold.otf", 24), WHITE, 285, 33)
    if flash or notes.get("flash"):
        note(img, 318, 1082, notes.get("flash", flash), 0, 26, CYAN, "left")
    if scale or notes.get("scale"):
        d = ImageDraw.Draw(img)
        y0, x0, x1 = cy + 138, cx - 80, cx + 80
        for xx in (x0, x1):
            d.line([(P(xx), P(y0 - 7)), (P(xx), P(y0 + 7))], fill=WHITE, width=P(3))
        d.line([(P(x0), P(y0)), (P(x1), P(y0))], fill=WHITE, width=P(3))
        t = notes.get("scale", scale)
        f = F("Inter-SemiBold.otf", 22)
        d.text((P(cx) - f.getlength(t) / 2, P(y0 + 12)), t, font=f, fill=WHITE)

def scene_euv(img, notes):
    cx, cy, r = CIRC
    hx, hy = 250, 905
    cone(img, hx + 40, hy)

    def content(inner):
        d = ImageDraw.Draw(inner)
        # dark grid backdrop
        for g in range(-8, 9):
            d.line([(P(cx + g * 40), P(cy - r)), (P(cx + g * 40), P(cy + r))], fill=(30, 44, 90, 90), width=P(1))
            d.line([(P(cx - r), P(cy + g * 40)), (P(cx + r), P(cy + g * 40))], fill=(30, 44, 90, 90), width=P(1))
        # laser beam (violet) from the left into the plasma
        beam = Image.new("RGBA", inner.size, (0, 0, 0, 0))
        bd = ImageDraw.Draw(beam)
        bd.polygon([(P(cx - r), P(cy - 26)), (P(cx - 30), P(cy - 6)), (P(cx - 30), P(cy + 6)), (P(cx - r), P(cy + 26))],
                   fill=VIOLET + (150,))
        beam = beam.filter(ImageFilter.GaussianBlur(P(5)))
        inner.alpha_composite(beam)
        bd2 = ImageDraw.Draw(inner)
        bd2.line([(P(cx - r), P(cy)), (P(cx - 30), P(cy))], fill=(225, 205, 255, 255), width=P(4))
        # flattened "pancake" droplet
        bd2.ellipse([P(cx - 24), P(cy - 58), P(cx - 2), P(cy + 58)], fill=(190, 205, 235, 255),
                    outline=(255, 255, 255, 255), width=P(2))
        # plasma burst
        burst = Image.new("RGBA", inner.size, (0, 0, 0, 0))
        b = ImageDraw.Draw(burst)
        rnd = random.Random(5)
        for i in range(34):
            a = i / 34 * math.tau
            ln = rnd.randint(70, 150)
            b.line([(P(cx + 14), P(cy)), (P(cx + 14 + math.cos(a) * ln), P(cy + math.sin(a) * ln))],
                   fill=(130, 235, 255, rnd.randint(150, 230)), width=P(rnd.choice([2, 3, 4])))
        burst = burst.filter(ImageFilter.GaussianBlur(P(1.5)))
        inner.alpha_composite(burst)
        glow_layer = Image.new("RGBA", inner.size, (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow_layer)
        for rr, col, al in ((95, VIOLET, 120), (62, CYAN, 190), (34, (255, 255, 255), 255)):
            gd.ellipse([P(cx + 14 - rr), P(cy - rr), P(cx + 14 + rr), P(cy + rr)], fill=col + (al,))
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(P(22)))
        inner.alpha_composite(glow_layer)
        # outgoing EUV light to the right
        lg = Image.new("RGBA", inner.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(lg)
        ld.polygon([(P(cx + 60), P(cy - 12)), (P(cx + r), P(cy - 70)), (P(cx + r), P(cy + 70)), (P(cx + 60), P(cy + 12))],
                   fill=CYAN + (55,))
        lg = lg.filter(ImageFilter.GaussianBlur(P(6)))
        inner.alpha_composite(lg)

    circle_frame(img, content)
    d = ImageDraw.Draw(img)
    # hero: molten tin droplet with motion trail
    for k, (dy, rad, al) in enumerate(((-120, 9, 80), (-78, 13, 130), (-38, 18, 190))):
        glow(img, hx, hy + dy, 24, CYAN, al // 4)
        d.ellipse([P(hx - rad), P(hy + dy - rad), P(hx + rad), P(hy + dy + rad)], fill=(175, 190, 215, al))
    glow(img, hx, hy, 70, CYAN, 90)
    d = ImageDraw.Draw(img)
    d.ellipse([P(hx - 30), P(hy - 30), P(hx + 30), P(hy + 30)], fill=(190, 204, 228, 255), outline=WHITE, width=P(2))
    d.ellipse([P(hx - 18), P(hy - 20), P(hx - 4), P(hy - 8)], fill=(255, 255, 255, 230))
    note(img, 62, 1000, notes.get("hero", "A tiny droplet\nof molten tin"), -4, 29, WHITE, "center")
    arrow(img, [(185, 1010), (215, 975), (232, 945)], WHITE, 3)
    callouts(img, notes, "A laser pulse flattens the drop. A second one vaporizes it into plasma.", "A flash of light every\n20 millionths of a second", "13.5 nm light")


def scene_chip(img, notes):
    cx, cy, r = CIRC
    hx, hy = 250, 905
    cone(img, hx + 50, hy)

    def content(inner):
        d = ImageDraw.Draw(inner)
        rnd = random.Random(9)
        for gx in range(-9, 10):
            for gy in range(-9, 10):
                x, y = cx + gx * 34, cy + gy * 34
                col = rnd.choice([CYAN, VIOLET, (90, 120, 230)])
                h = rnd.randint(8, 22)
                d.rounded_rectangle([P(x - 9), P(y - 9), P(x + 9), P(y + 9)], radius=P(3),
                                    fill=col[:3] + (rnd.randint(70, 170),), outline=col + (230,), width=P(1))
        glow_layer = Image.new("RGBA", inner.size, (0, 0, 0, 0))
        ImageDraw.Draw(glow_layer).ellipse([P(cx - 90), P(cy - 90), P(cx + 90), P(cy + 90)], fill=CYAN + (110,))
        inner.alpha_composite(glow_layer.filter(ImageFilter.GaussianBlur(P(40))))

    circle_frame(img, content)
    glow(img, hx, hy, 90, CYAN, 70)
    d = ImageDraw.Draw(img)
    rrect(img, (hx - 46, hy - 46, hx + 46, hy + 46), 10, fill=(24, 30, 60), alpha=255, outline=CYAN + (255,), width=3)
    rrect(img, (hx - 26, hy - 26, hx + 26, hy + 26), 6, fill=(40, 50, 100), alpha=255, outline=VIOLET + (255,), width=2)
    d = ImageDraw.Draw(img)
    for i in range(-3, 4):
        for s in (-1, 1):
            d.line([(P(hx + i * 12), P(hy + s * 46)), (P(hx + i * 12), P(hy + s * 60))], fill=CYAN, width=P(3))
            d.line([(P(hx + s * 46), P(hy + i * 12)), (P(hx + s * 60), P(hy + i * 12))], fill=CYAN, width=P(3))
    note(img, 62, 1000, notes.get("hero", "A real chip is\nthis small"), -4, 29, WHITE, "center")
    arrow(img, [(185, 1010), (215, 975), (232, 965)], WHITE, 3)
    callouts(img, notes, "A microscopic view of the tiny switches inside the chip.", "Billions working together\nevery second", "for scale")


def scene_wafer(img, notes):
    cx, cy, r = CIRC

    def content(inner):
        d = ImageDraw.Draw(inner)
        wr = r * 0.92
        d.ellipse([P(cx - wr), P(cy - wr), P(cx + wr), P(cy + wr)], fill=(110, 125, 165, 255), outline=(220, 230, 255, 255), width=P(4))
        step = 46
        for gx in range(-8, 9):
            for gy in range(-8, 9):
                x, y = cx + gx * step, cy + gy * step
                if math.hypot(x - cx, y - cy) < wr - 30:
                    d.rectangle([P(x - 19), P(y - 19), P(x + 19), P(y + 19)], fill=(70, 95, 200, 255), outline=(150, 190, 255, 255), width=P(1))
        g = Image.new("RGBA", inner.size, (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse([P(cx - 150), P(cy - 170), P(cx + 30), P(cy + 10)], fill=(255, 255, 255, 70))
        inner.alpha_composite(g.filter(ImageFilter.GaussianBlur(P(30))))

    circle_frame(img, content)
    callouts(img, notes, "A silicon wafer is cut into hundreds of chips.", "", "")
    note(img, 100, 930, notes.get("hero", "Each square is\none chip"), -4, 30, WHITE, "center")
    arrow(img, [(250, 940), (360, 880), (470, 840)], WHITE, 3)


SCENES = {"euv": scene_euv, "chip": scene_chip, "wafer": scene_wafer}


def build(fact):
    img = gradient()
    glow(img, 900, 200, 380, VIOLET, 55)
    glow(img, 140, 1150, 420, CYAN, 45)
    traces(img, fact["num"] * 7 + 3, 22)
    d = ImageDraw.Draw(img)
    M = 56
    # header
    f_h = F("Inter-SemiBold.otf", 24)
    x = M
    for part, col in (("SEMICONDUCTOR FACTS ", MUTED), ("#%d" % fact["num"], CYAN)):
        fp = F("Inter-Bold.otf", 26) if col == CYAN else f_h
        d.text((P(x), P(36)), part, font=fp, fill=col)
        x += fp.getlength(part) / S
    for i, t in enumerate(("SMALL CHIPS.", "A BRIGHTER TOMORROW.")):
        f = F("Inter-SemiBold.otf", 17)
        d.text((W * S - P(M) - f.getlength(t), P(30 + i * 22)), t, font=f, fill=CYAN)
    d.line([(P(M), P(86)), (P(W - M), P(86))], fill=(40, 52, 96), width=P(1.5))
    # headline
    y = 108
    for key, name, mx, mw, col, lh in (("line1", "Inter-Black.otf", 160, 610, CYAN, 1.0),
                                       ("line2", "Inter-Black.otf", 130, 610, WHITE, 1.0),
                                       ("line3", "Inter-ExtraBold.otf", 84, 960, PURPLE, 1.0)):
        f, sz = fit(fact[key], name, mx, mw)
        d.text((P(M), P(y)), fact[key], font=f, fill=col)
        y += int(sz * 1.02) + (16 if key == 'line1' else 4)
    # benefits column
    for i, (lab, ic) in enumerate(zip(fact["benefits"], ("gauge", "bolt", "chip"))):
        by = 135 + i * 78
        icon(img, ic, 790, by + 8, 21, MUTED, 3)
        d = ImageDraw.Draw(img)
        for j, ln in enumerate(lab.split("\n")):
            d.text((P(840), P(by - 8 + j * 22)), ln, font=F("Inter-SemiBold.otf", 17), fill=MUTED)
    # body with highlighted phrase
    y += 18
    body_f = F("Inter-Medium.otf", 30)
    hl = fact.get("highlight", "")
    words = fact["body"].split(" ")
    x, maxw = M, 600
    hl_words = set(hl.split(" ")) if hl else set()
    # simple word-wrap that colours highlight words
    cur_x, cur_y = M, y
    hl_f = F("Inter-Bold.otf", 30)
    seen_hl = False
    for w in words:
        in_hl = w.strip(".,—") in hl_words and hl and hl in fact["body"]
        f = hl_f if in_hl else body_f
        wl = f.getlength(w + " ") / S
        if cur_x + wl - M > maxw:
            cur_x = M
            cur_y += 44
        d.text((P(cur_x), P(cur_y)), w, font=f, fill=CYAN if in_hl else (214, 224, 245))
        cur_x += wl
    # scene
    SCENES[fact.get("scene", "chip")](img, fact.get("scene_notes", {}))
    # bottom icon row
    for i, (ic, lab) in enumerate(fact["bottom"]):
        bx = 86 + i * 150
        icon(img, ic, bx, 1186, 26, MUTED, 3)
        d = ImageDraw.Draw(img)
        for j, ln in enumerate(lab.split("\n")):
            lw = F("Inter-SemiBold.otf", 15).getlength(ln) / S
            d.text((P(bx - lw / 2), P(1224 + j * 19)), ln, font=F("Inter-SemiBold.otf", 15), fill=MUTED)
    d = ImageDraw.Draw(img)
    d.line([(P(M), P(1166 - 56)), (P(W - M), P(1166 - 56))], fill=(0, 0, 0, 0), width=1)
    # footer
    d.line([(P(M), P(1268)), (P(W - M), P(1268))], fill=(40, 52, 96), width=P(1.5))
    rrect(img, (M, 1288, M + 44, 1332), 8, fill=VIOLET, alpha=90, outline=VIOLET + (255,), width=2)
    icon(img, "chip", M + 22, 1310, 14, WHITE, 2.5)
    d = ImageDraw.Draw(img)
    d.text((P(M + 58), P(1282)), HANDLE, font=F("Inter-ExtraBold.otf", 27), fill=WHITE)
    d.text((P(M + 58), P(1318)), "SEMICONDUCTOR FACTS FOR A BRIGHTER TOMORROW.", font=F("Inter-Medium.otf", 15), fill=MUTED)
    tl = fact.get("tagline", "TINY TRANSISTORS.\nHUGE IMPACT.").split("\n")
    d.line([(P(W - M - 330), P(1290)), (P(W - M - 330), P(1332))], fill=CYAN, width=P(3))
    d.text((P(W - M - 314), P(1284)), tl[0], font=F("Inter-Bold.otf", 22), fill=WHITE)
    d.text((P(W - M - 314), P(1312)), tl[1], font=F("Inter-ExtraBold.otf", 22), fill=PURPLE)
    finish(img, fact.get("file", "fact.png"))


if __name__ == "__main__":
    build(json.load(open(sys.argv[1])))
    print("ok")

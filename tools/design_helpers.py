import os, random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 2
W, H = 1080, 1350
OUT = os.environ.get("OUT_DIR", "./out")
os.makedirs(OUT, exist_ok=True)

FD = "/usr/share/fonts/opentype/inter/"
def F(name, size):
    return ImageFont.truetype(FD + name, int(size * S))

BG1 = (6, 10, 24)
BG2 = (14, 20, 48)
CYAN = (61, 217, 255)
VIOLET = (139, 92, 246)
GOLD = (255, 200, 87)
WHITE = (244, 247, 255)
MUTED = (160, 174, 205)
PANEL = (18, 26, 58)

TOTAL = 9
HANDLE = "@semiconductorunicorn"


def gradient():
    img = Image.new("RGB", (W * S, H * S), BG1)
    px = ImageDraw.Draw(img)
    for y in range(H * S):
        t = y / (H * S)
        c = tuple(int(BG1[i] + (BG2[i] - BG1[i]) * t) for i in range(3))
        px.line([(0, y), (W * S, y)], fill=c)
    return img


def glow(img, cx, cy, r, color, alpha):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], fill=color + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(r * S * 0.45))
    img.paste(layer, (0, 0), layer)


def traces(img, seed, n=34, strong_zone=None):
    rnd = random.Random(seed)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    grid = 45
    for _ in range(n):
        x = rnd.randint(0, W // grid) * grid
        y = rnd.randint(0, H // grid) * grid
        pts = [(x, y)]
        dx, dy = rnd.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
        for _ in range(rnd.randint(3, 7)):
            L = rnd.randint(1, 4) * grid
            x += dx * L
            y += dy * L
            pts.append((x, y))
            if rnd.random() < 0.5:
                ndx, ndy = rnd.choice([(1, 1), (1, -1), (-1, 1), (-1, -1)])
                dx, dy = ndx, ndy
            else:
                dx, dy = rnd.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
        col = rnd.choice([CYAN, VIOLET, (60, 90, 170)])
        a = rnd.randint(34, 70)
        d.line([(px * S, py * S) for px, py in pts], fill=col + (a,), width=int(2.5 * S), joint="curve")
        for px, py in (pts[0], pts[-1]):
            r = 6
            d.ellipse([(px - r) * S, (py - r) * S, (px + r) * S, (py + r) * S], outline=col + (a + 40,), width=int(2 * S))
    img.paste(layer, (0, 0), layer)


def rrect(img, box, radius, fill=None, outline=None, width=2, alpha=255):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    b = [box[0] * S, box[1] * S, box[2] * S, box[3] * S]
    d.rounded_rectangle(b, radius=radius * S, fill=(fill + (alpha,)) if fill else None,
                        outline=outline, width=int(width * S))
    img.paste(layer, (0, 0), layer)


def wrap(text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw * S:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, text, font, fill, maxw, lh):
    lines = wrap(text, font, maxw)
    for ln in lines:
        d.text((x * S, y * S), ln, font=font, fill=fill)
        y += lh
    return y


def chrome(img, d, idx, label="THE CHIP WEEK AHEAD"):
    d.text((72 * S, 64 * S), label, font=F("Inter-SemiBold.otf", 24), fill=MUTED)
    t = f"{idx}/{TOTAL}"
    w = F("Inter-SemiBold.otf", 24).getlength(t)
    d.text((W * S - 72 * S - w, 64 * S), t, font=F("Inter-SemiBold.otf", 24), fill=MUTED)
    d.line([(72 * S, 112 * S), ((W - 72) * S, 112 * S)], fill=(40, 52, 96), width=2 * S // 2)
    d.text((72 * S, (H - 96) * S), HANDLE, font=F("Inter-Bold.otf", 28), fill=WHITE)
    if idx < TOTAL:
        t2 = "SWIPE  →"
        w2 = F("Inter-Bold.otf", 26).getlength(t2)
        d.text((W * S - 72 * S - w2, (H - 94) * S), t2, font=F("Inter-Bold.otf", 26), fill=CYAN)


def chip_graphic(img, cx, cy, size):
    glow(img, cx, cy, size * 0.9, CYAN, 70)
    glow(img, cx + 60, cy + 40, size * 0.7, VIOLET, 60)
    half = size // 2
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # pins
    n = 9
    pin_len, pin_w = 34, 10
    step = size / (n + 1)
    for i in range(1, n + 1):
        off = -half + step * i
        for (x0, y0, x1, y1) in [
            (cx + off - pin_w / 2, cy - half - pin_len, cx + off + pin_w / 2, cy - half),
            (cx + off - pin_w / 2, cy + half, cx + off + pin_w / 2, cy + half + pin_len),
            (cx - half - pin_len, cy + off - pin_w / 2, cx - half, cy + off + pin_w / 2),
            (cx + half, cy + off - pin_w / 2, cx + half + pin_len, cy + off + pin_w / 2),
        ]:
            d.rounded_rectangle([x0 * S, y0 * S, x1 * S, y1 * S], radius=3 * S, fill=CYAN + (200,))
    d.rounded_rectangle([(cx - half) * S, (cy - half) * S, (cx + half) * S, (cy + half) * S],
                        radius=30 * S, fill=(10, 16, 40, 255), outline=CYAN + (255,), width=4 * S)
    for k, inset in enumerate([34, 70, 106]):
        col = [CYAN, VIOLET, GOLD][k]
        d.rounded_rectangle([(cx - half + inset) * S, (cy - half + inset) * S,
                             (cx + half - inset) * S, (cy + half - inset) * S],
                            radius=(18 - k * 4) * S, outline=col + (200,), width=3 * S)
    c = size * 0.14
    d.rounded_rectangle([(cx - c) * S, (cy - c) * S, (cx + c) * S, (cy + c) * S],
                        radius=10 * S, fill=GOLD + (255,))
    # inner trace stubs
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        x0, y0 = cx + math.cos(a) * c * 1.4, cy + math.sin(a) * c * 1.4
        x1, y1 = cx + math.cos(a) * (half - 106), cy + math.sin(a) * (half - 106)
        d.line([(x0 * S, y0 * S), (x1 * S, y1 * S)], fill=GOLD + (150,), width=3 * S)
    img.paste(layer, (0, 0), layer)


def finish(img, name):
    out = img.resize((W, H), Image.LANCZOS)
    out.save(os.path.join(OUT, name), quality=95)


# ---------- slide 1: cover ----------
def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80)
    glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 7, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 470, 214), 32, fill=(61, 217, 255), alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 8 – 15, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "The Chip", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "Week Ahead", F("Inter-ExtraBold.otf", 128), CYAN, 940, 136)
    text_block(d, 72, y + 24, "6 things to watch in the semiconductor industry — and what each one tells you.",
               F("Inter-Medium.otf", 42), MUTED, 860, 58)
    chip_graphic(img, 540, 1020, 330)
    d = ImageDraw.Draw(img)
    d.text((72 * S, (H - 96) * S), HANDLE, font=F("Inter-Bold.otf", 28), fill=WHITE)
    t2 = "SWIPE  →"
    w2 = F("Inter-Bold.otf", 26).getlength(t2)
    d.text((W * S - 72 * S - w2, (H - 94) * S), t2, font=F("Inter-Bold.otf", 26), fill=CYAN)
    finish(img, "slide_01.png")


# ---------- generic content slide ----------
def content(idx, seed, date, tag, title, body, why_label, why, accent=CYAN, stat=None, stat_cap=None):
    img = gradient()
    glow(img, 950, 220, 320, accent, 50)
    traces(img, seed, 26)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx)
    # date pill
    f_date = F("Inter-ExtraBold.otf", 104)
    d.text((72 * S, 150 * S), date, font=f_date, fill=accent)
    dw = f_date.getlength(date) / S
    # tag pill
    f_tag = F("Inter-Bold.otf", 28)
    tw = f_tag.getlength(tag) / S
    rrect(img, (72, 292, 72 + tw + 56, 346), 27, fill=accent, alpha=36, outline=accent + (255,), width=2)
    d = ImageDraw.Draw(img)
    d.text((100 * S, 303 * S), tag, font=f_tag, fill=accent)
    y = text_block(d, 72, 392, title, F("Inter-ExtraBold.otf", 66), WHITE, 936, 78)
    y += 14
    if stat:
        fs = F("Inter-ExtraBold.otf", 150)
        d.text((72 * S, (y + 4) * S), stat, font=fs, fill=GOLD)
        sw = fs.getlength(stat) / S
        text_block(d, 72 + sw + 28, y + 40, stat_cap, F("Inter-SemiBold.otf", 34), WHITE, 936 - sw - 28, 46)
        y += 190
    y = text_block(d, 72, y + 4, body, F("Inter-Medium.otf", 38), MUTED, 936, 56)
    # why box
    box_top = max(y + 36, 880)
    box_bottom = box_top + 270
    rrect(img, (72, box_top, W - 72, box_bottom), 28, fill=PANEL, alpha=235, outline=(48, 62, 118), width=2)
    rrect(img, (72, box_top, 84, box_bottom), 6, fill=accent)
    d = ImageDraw.Draw(img)
    d.text((112 * S, (box_top + 30) * S), why_label, font=F("Inter-Bold.otf", 26), fill=accent)
    text_block(d, 112, box_top + 76, why, F("Inter-SemiBold.otf", 36), WHITE, 850, 52)
    finish(img, f"slide_{idx:02d}.png")


# ---------- CTA ----------
def cta(idx):
    img = gradient()
    glow(img, 540, 520, 520, VIOLET, 85)
    glow(img, 200, 1150, 360, CYAN, 60)
    traces(img, 21, 44)
    chip_graphic(img, 540, 330, 230)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx, label="WANT MORE?")
    y = text_block(d, 72, 570, "Get the chip news", F("Inter-ExtraBold.otf", 84), WHITE, 936, 96)
    y = text_block(d, 72, y, "before everyone else.", F("Inter-ExtraBold.otf", 84), CYAN, 936, 96)
    text_block(d, 72, y + 22, "A new carousel every day: semiconductor + VLSI news, explained simply.",
               F("Inter-Medium.otf", 38), MUTED, 900, 54)
    # follow button
    rrect(img, (72, 940, W - 72, 1060), 60, fill=CYAN)
    d = ImageDraw.Draw(img)
    t = "FOLLOW " + HANDLE
    f = F("Inter-ExtraBold.otf", 44)
    w = f.getlength(t)
    d.text(((W * S - w) / 2, 970 * S), t, font=f, fill=BG1)
    d.text((72 * S, 1100 * S), "To get more posts like this, follow this channel.", font=F("Inter-SemiBold.otf", 32), fill=WHITE)
    d.text((72 * S, 1150 * S), "Save this post  •  Send it to a friend who loves chips", font=F("Inter-Medium.otf", 30), fill=MUTED)
    finish(img, f"slide_{idx:02d}.png")



# ---------- slide 1: cover ----------
def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80)
    glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 7, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 470, 214), 32, fill=(61, 217, 255), alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 8 – 15, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "The Chip", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "Week Ahead", F("Inter-ExtraBold.otf", 128), CYAN, 940, 136)
    text_block(d, 72, y + 24, "6 things to watch in the semiconductor industry — and what each one tells you.",
               F("Inter-Medium.otf", 42), MUTED, 860, 58)
    chip_graphic(img, 540, 1020, 330)
    d = ImageDraw.Draw(img)
    d.text((72 * S, (H - 96) * S), HANDLE, font=F("Inter-Bold.otf", 28), fill=WHITE)
    t2 = "SWIPE  →"
    w2 = F("Inter-Bold.otf", 26).getlength(t2)
    d.text((W * S - 72 * S - w2, (H - 94) * S), t2, font=F("Inter-Bold.otf", 26), fill=CYAN)
    finish(img, "slide_01.png")


# ---------- generic content slide ----------
def content(idx, seed, date, tag, title, body, why_label, why, accent=CYAN, stat=None, stat_cap=None):
    img = gradient()
    glow(img, 950, 220, 320, accent, 50)
    traces(img, seed, 26)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx)
    # date pill
    f_date = F("Inter-ExtraBold.otf", 104)
    d.text((72 * S, 150 * S), date, font=f_date, fill=accent)
    dw = f_date.getlength(date) / S
    # tag pill
    f_tag = F("Inter-Bold.otf", 28)
    tw = f_tag.getlength(tag) / S
    rrect(img, (72, 292, 72 + tw + 56, 346), 27, fill=accent, alpha=36, outline=accent + (255,), width=2)
    d = ImageDraw.Draw(img)
    d.text((100 * S, 303 * S), tag, font=f_tag, fill=accent)
    y = text_block(d, 72, 392, title, F("Inter-ExtraBold.otf", 66), WHITE, 936, 78)
    y += 14
    if stat:
        fs = F("Inter-ExtraBold.otf", 150)
        d.text((72 * S, (y + 4) * S), stat, font=fs, fill=GOLD)
        sw = fs.getlength(stat) / S
        text_block(d, 72 + sw + 28, y + 40, stat_cap, F("Inter-SemiBold.otf", 34), WHITE, 936 - sw - 28, 46)
        y += 190
    y = text_block(d, 72, y + 4, body, F("Inter-Medium.otf", 38), MUTED, 936, 56)
    # why box
    box_top = max(y + 36, 880)
    box_bottom = box_top + 270
    rrect(img, (72, box_top, W - 72, box_bottom), 28, fill=PANEL, alpha=235, outline=(48, 62, 118), width=2)
    rrect(img, (72, box_top, 84, box_bottom), 6, fill=accent)
    d = ImageDraw.Draw(img)
    d.text((112 * S, (box_top + 30) * S), why_label, font=F("Inter-Bold.otf", 26), fill=accent)
    text_block(d, 112, box_top + 76, why, F("Inter-SemiBold.otf", 36), WHITE, 850, 52)
    finish(img, f"slide_{idx:02d}.png")


# ---------- CTA ----------
def cta(idx):
    img = gradient()
    glow(img, 540, 520, 520, VIOLET, 85)
    glow(img, 200, 1150, 360, CYAN, 60)
    traces(img, 21, 44)
    chip_graphic(img, 540, 330, 230)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx, label="WANT MORE?")
    y = text_block(d, 72, 570, "Get the chip news", F("Inter-ExtraBold.otf", 84), WHITE, 936, 96)
    y = text_block(d, 72, y, "before everyone else.", F("Inter-ExtraBold.otf", 84), CYAN, 936, 96)
    text_block(d, 72, y + 22, "A new carousel every day: semiconductor + VLSI news, explained simply.",
               F("Inter-Medium.otf", 38), MUTED, 900, 54)
    # follow button
    rrect(img, (72, 940, W - 72, 1060), 60, fill=CYAN)
    d = ImageDraw.Draw(img)
    t = "FOLLOW " + HANDLE
    f = F("Inter-ExtraBold.otf", 44)
    w = f.getlength(t)
    d.text(((W * S - w) / 2, 970 * S), t, font=f, fill=BG1)
    d.text((72 * S, 1100 * S), "To get more posts like this, follow this channel.", font=F("Inter-SemiBold.otf", 32), fill=WHITE)
    d.text((72 * S, 1150 * S), "Save this post  •  Send it to a friend who loves chips", font=F("Inter-Medium.otf", 30), fill=MUTED)
    finish(img, f"slide_{idx:02d}.png")


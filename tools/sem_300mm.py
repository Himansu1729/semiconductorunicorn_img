import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 8
LABEL = "300MM FAB OUTLOOK"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 430, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 13-14, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Fab equipment", F("Inter-ExtraBold.otf", 118), WHITE, 940, 136)
    y = text_block(d, 72, y, "$149 billion", F("Inter-ExtraBold.otf", 118), CYAN, 940, 128)
    text_block(d, 72, y + 24, "SEMI's new 300mm outlook: spending on chip-fab tools is still climbing. Here are the numbers.",
               F("Inter-Medium.otf", 40), MUTED, 900, 56)
    chip_graphic(img, 540, 1040, 300)
    d = ImageDraw.Draw(img)
    d.text((72 * S, (H - 96) * S), HANDLE, font=F("Inter-Bold.otf", 28), fill=WHITE)
    t2 = "SWIPE  →"; f2 = F("Inter-Bold.otf", 26)
    d.text((W * S - 72 * S - f2.getlength(t2), (H - 94) * S), t2, font=f2, fill=CYAN)
    finish(img, "slide_01.png")

def content(idx, seed, head, tag, title, body, why_label, why, accent=CYAN, stat=None, stat_cap=None):
    img = gradient()
    glow(img, 950, 220, 320, accent, 50); traces(img, seed, 26)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx, label=LABEL)
    f_head = F("Inter-ExtraBold.otf", 104)
    d.text((72 * S, 150 * S), head, font=f_head, fill=accent)
    f_tag = F("Inter-Bold.otf", 28); tw = f_tag.getlength(tag) / S
    rrect(img, (72, 292, 72 + tw + 56, 346), 27, fill=accent, alpha=36, outline=accent + (255,), width=2)
    d = ImageDraw.Draw(img)
    d.text((100 * S, 303 * S), tag, font=f_tag, fill=accent)
    y = text_block(d, 72, 392, title, F("Inter-ExtraBold.otf", 66), WHITE, 936, 78) + 14
    if stat:
        fs = F("Inter-ExtraBold.otf", 150)
        d.text((72 * S, (y + 4) * S), stat, font=fs, fill=GOLD)
        sw = fs.getlength(stat) / S
        text_block(d, 72 + sw + 28, y + 40, stat_cap, F("Inter-SemiBold.otf", 34), WHITE, 936 - sw - 28, 46)
        y += 190
    y = text_block(d, 72, y + 4, body, F("Inter-Medium.otf", 38), MUTED, 936, 56)
    top = max(y + 36, 880); bot = top + 236
    assert bot < H - 120, (idx, bot)
    rrect(img, (72, top, W - 72, bot), 28, fill=PANEL, alpha=235, outline=(48, 62, 118), width=2)
    rrect(img, (72, top, 84, bot), 6, fill=accent)
    d = ImageDraw.Draw(img)
    d.text((112 * S, (top + 30) * S), why_label, font=F("Inter-Bold.otf", 26), fill=accent)
    text_block(d, 112, top + 76, why, F("Inter-SemiBold.otf", 36), WHITE, 850, 52)
    finish(img, f"slide_{idx:02d}.png")

def cta(idx):
    img = gradient()
    glow(img, 540, 520, 520, VIOLET, 85); glow(img, 200, 1150, 360, CYAN, 60)
    traces(img, 21, 44); chip_graphic(img, 540, 330, 230)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx, label="WANT MORE?")
    y = text_block(d, 72, 570, "Get the chip news", F("Inter-ExtraBold.otf", 84), WHITE, 936, 96)
    y = text_block(d, 72, y, "before everyone else.", F("Inter-ExtraBold.otf", 84), CYAN, 936, 96)
    text_block(d, 72, y + 22, "A new semiconductor + VLSI post every day, explained simply.",
               F("Inter-Medium.otf", 38), MUTED, 900, 54)
    rrect(img, (72, 940, W - 72, 1060), 60, fill=CYAN)
    d = ImageDraw.Draw(img)
    t = "FOLLOW " + HANDLE; f = F("Inter-ExtraBold.otf", 44)
    d.text(((W * S - f.getlength(t)) / 2, 970 * S), t, font=f, fill=BG1)
    d.text((72 * S, 1100 * S), "Follow @semiconductorunicorn to get more posts.", font=F("Inter-SemiBold.otf", 32), fill=WHITE)
    d.text((72 * S, 1150 * S), "Save this post  •  Send it to a friend who loves chips", font=F("Inter-Medium.otf", 30), fill=MUTED)
    finish(img, f"slide_{idx:02d}.png")

cover()
content(2, 61, "$149B", "SEMI 300MM FAB OUTLOOK", "Equipment spend jumps in 2026",
        "SEMI's 3Q26 300mm Fab Outlook projects worldwide 300mm fab equipment spending of $149 billion in 2026, up 31% from 2025.",
        "READ IT RIGHT", "This is spending on tools inside fabs, a forecast from SEMI. It is not chip sales or company revenue.", CYAN)
content(3, 62, "$227B", "THE 2029 FORECAST", "And it keeps climbing to 2029",
        "SEMI now projects 300mm fab equipment spending will reach $227 billion in 2029, growing at double-digit rates along the way. SEMI's CEO says chip demand is turning into real factory expansion.",
        "WHY IT MATTERS", "More fab tools means more capacity for AI, memory and logic chips years from now.", GOLD)
content(4, 63, "$63.3B", "FAB CONSTRUCTION", "Building the fabs themselves",
        "Spending on 300mm fab construction is projected at $47.5 billion in 2026 (up 23%), then $63.3 billion in 2027 (up 33%) and $68.4 billion in 2028.",
        "SPOT THE PATTERN", "Construction comes first, then the equipment moves in. Both lines are rising.", CYAN)
content(5, 64, "23", "FAB PIPELINE", "More fabs start running in 2027",
        "SEMI counts 20 new fab or line construction starts in 2026 and 18 in 2027. Fabs and lines beginning operations or first silicon: 13 in 2026 and 23 in 2027. These counts exclude pure R&D fabs.",
        "READ IT RIGHT", "A fab starting operations is not the same as full volume production.", GOLD)
content(6, 65, "$40.6B", "THE AMERICAS", "US-region spend more than doubles",
        "Americas equipment spending is projected at $18.1 billion in 2026 and $40.6 billion in 2029. In the US, 3 fab construction starts are counted for 2026 and 4 for 2027.",
        "WHY IT MATTERS", "New US fabs need tools, engineers and process teams, all years before first wafers.", CYAN)
content(7, 66, "VLSI", "TERM OF THE DAY", "What is a 300mm wafer?",
        "A 300mm wafer is a round silicon disc 300 millimetres across. Fabs print hundreds of identical chips (dies) on it, so a bigger wafer means more dies per run.",
        "PLAIN LANGUAGE", "Most leading chips are made on 300mm wafers, which is why this outlook tracks them.", GOLD)
cta(8)
print("ok")

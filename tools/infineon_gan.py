import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "INFINEON GaN 300MM"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 41, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 430, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 27, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Infineon bets", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "€1.1B on GaN", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "A 300 mm gallium nitride power-chip line in Villach, Austria.",
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
content(2, 291, "€1.1B", "WHAT HAPPENED", "Infineon plans a 300 mm GaN fab",
        "On Oct 27, Infineon said it will invest about €1.1B at its Villach site in Austria to make gallium nitride (GaN) power chips on 300 mm wafers. Spending runs through 2034.",
        "CLAIM", "Infineon calls it the first high-volume 300 mm GaN line in the world.", CYAN)
content(3, 292, "2.3x", "WHY 300 MM", "More chips from every wafer",
        "Infineon says a 300 mm wafer gives about 2.3 times as many chips as a 200 mm one. It processed its first 300 mm GaN wafers in 2024 and will reuse existing Villach cleanrooms to keep costs down.",
        "SIMPLE MATH", "A bigger wafer is a bigger pizza: more slices per bake.", GOLD)
content(4, 293, "€319M", "PUBLIC MONEY", "EU state aid approved",
        "The European Commission approved €319M of state aid under the European Chips Act. Austria's own formal approval is still pending, so the funding path is not fully closed yet.",
        "NOTE", "Aid approval is a permission to fund, not money already spent.", CYAN)
content(5, 294, "2027", "TIMELINE", "Volume production from end of 2027",
        "Infineon expects high-volume production on 300 mm to start by the end of 2027, with capacity ramped in line with market demand. No output target was given.",
        "REMINDER", "Dates are company plans and can move.", GOLD)
content(6, 295, "VLSI", "TERM OF THE DAY", "What is GaN power?",
        "Gallium nitride is a wide-bandgap material. Power transistors made from it can switch faster and waste less energy as heat than silicon ones, so power supplies can be smaller.",
        "PLAIN LANGUAGE", "Less wasted heat means smaller chargers and cooler servers.", CYAN)
content(7, 296, "~35%", "MARKET", "Analysts see fast GaN growth",
        "Citing Yole Group, reports say the power GaN market could grow about 35% a year from 2025 to 2031, reaching roughly $3.5B. Targets include AI data centers, EVs, solar and robotics.",
        "CONTEXT", "A forecast from one analyst firm, not a guarantee.", GOLD)
content(8, 297, "Next", "WHAT TO WATCH", "What could change",
        "Watch for Austria's final approval, the 2027 production start, early customers, and how rivals respond with their own GaN capacity and wafer sizes.",
        "NOTE", "Based on company and press reports. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

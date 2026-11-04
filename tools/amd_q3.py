import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "AMD Q3 2026"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 51, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 420, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 3, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "AMD data center", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "revenue up 97%", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "AMD Q3 2026: record $13.4B in total revenue, up 45% from a year ago.",
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
content(2, 391, "$13.4B", "WHAT HAPPENED", "AMD reports record Q3 2026 revenue",
        "On Nov 3, AMD said revenue for the quarter ended Sep 26 was $13.38B, up 45% from a year ago and up 16% from Q2.",
        "CONTEXT", "AMD designs CPUs and GPUs; TSMC makes its chips.", CYAN)
content(3, 392, "+97%", "KEY NUMBERS", "Data center revenue hit $8.5B",
        "Data Center sales reached $8.55B, up 97% year over year, about 64% of all revenue. Client and Gaming was $3.7B, down 8%, and Embedded was $1.1B, up 29%.",
        "NOTE", "Data center was about 47% of revenue a year earlier.", GOLD)
content(4, 393, "56%", "MARGINS AND PROFIT", "Non-GAAP gross margin of 56%",
        "GAAP gross margin was 54%. Non-GAAP net income was $3.47B and non-GAAP EPS $2.09, while GAAP EPS was $1.46.",
        "NOTE", "GAAP and non-GAAP differ because of company adjustments.", CYAN)
content(5, 394, "MI450", "AI HARDWARE", "MI450 GPUs and Helios racks ship",
        "AMD launched the Instinct MI450 series. It says Anthropic, Meta, Microsoft, OpenAI and Oracle Cloud are running workloads on the first Helios rack systems, which pair MI450 GPUs with 6th Gen EPYC CPUs.",
        "WHY IT MATTERS", "Racks, not single chips, are now the unit AI customers buy.", GOLD)
content(6, 395, "VLSI", "TERM OF THE DAY", "What is a rack-scale system?",
        "Instead of selling one chip, the vendor designs a whole rack: GPUs, CPUs, networking and cooling built to work together as one big computer for AI.",
        "PLAIN LANGUAGE", "Think of it as one giant computer built from many chips.", CYAN)
content(7, 396, "~$17B", "OUTLOOK", "Q4 guide: about $17B, plus or minus 3%",
        "AMD guides Q4 revenue to about $17B and non-GAAP gross margin to about 55%. At the midpoint that is roughly 27% above Q3.",
        "REMINDER", "Guidance is a company forecast, not a result.", GOLD)
content(8, 397, "Next", "WHAT TO WATCH", "What could change",
        "Watch whether Q4 lands in the guided range, how fast MI450 and Helios deployments ramp, and whether gaming and client demand stabilise.",
        "NOTE", "Company-reported figures. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

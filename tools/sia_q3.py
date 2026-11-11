import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "GLOBAL CHIP SALES Q3 2026"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 470, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "SIA · NOV 3, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Chip sales hit", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "$517.7B", F("Inter-ExtraBold.otf", 118), CYAN, 940, 128)
    text_block(d, 72, y + 24, "Global semiconductor sales jumped 24.1% in Q3 2026 versus Q2, the SIA reported.",
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
content(2, 51, "$517.7B", "Q3 2026 (JUL-SEP)", "Worldwide chip sales in one quarter",
        "The Semiconductor Industry Association (SIA) reported global semiconductor sales of $517.7 billion for the third quarter of 2026, published Nov 3.",
        "READ IT RIGHT", "These are sales of chips worldwide in US dollars, compiled from industry data.", CYAN)
content(3, 52, "+24.1%", "VS Q2 2026", "A quarter-over-quarter surge",
        "Q3 sales were 24.1% higher than the second quarter of 2026, a very large jump for a single quarter.",
        "WHY IT MATTERS", "AI data centers and memory are pulling huge volume through fabs and packaging lines.", GOLD)
content(4, 53, "$172.6B", "SEPTEMBER 2026", "One month, three-month average",
        "September sales came in at $172.6 billion on a three-month moving average basis, up 7.9% from August.",
        "READ IT RIGHT", "SIA reports a smoothed average, so one odd month does not distort the trend.", CYAN)
content(5, 54, "+146.8%", "SEPT YEAR OVER YEAR", "Far above September 2025",
        "On the same moving-average basis, September 2026 sales were 146.8% higher than September 2025.",
        "WHY IT MATTERS", "A year-over-year view shows how fast the whole market has scaled up.", GOLD)
content(6, 55, "VLSI TERM", "MOVING AVERAGE", "What is a 3-month moving average?",
        "Instead of reporting one month alone, SIA averages the latest three months of sales, then slides that window forward each month.",
        "IN PLAIN WORDS", "It smooths bumps, like lumpy shipment timing, so you can see the real direction of sales.", CYAN)
content(7, 56, "ALL 5", "BY REGION", "Every region grew, Americas led",
        "September year-over-year growth: Americas +191.7%, Asia Pacific/other +141.4%, China +124.9%, Europe +102.5%, Japan +73.4%.",
        "WHY IT MATTERS", "Growth was broad. Even the slowest major region, Japan, was up more than 70%.", GOLD)
content(8, 57, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) The next monthly SIA report, covering October. 2) Whether the month-over-month growth keeps going. 3) How memory and AI chip demand hold up.",
        "NOT ADVICE", "This is a summary of industry-reported figures, not investment advice.", CYAN)
cta(9)

import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "TEXAS INSTRUMENTS Q3 2026"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 410, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 21, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Texas Instruments", F("Inter-ExtraBold.otf", 100), WHITE, 940, 136)
    y = text_block(d, 72, y, "sales jump 28%", F("Inter-ExtraBold.otf", 110), CYAN, 940, 128)
    text_block(d, 72, y + 24, "Analog chip demand rebounded: Q3 revenue hit $6.06B and the Q4 guide beat what analysts expected.",
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
content(2, 51, "$6.06B", "REVENUE", "Sales up 28% from a year ago",
        "Texas Instruments reported Q3 revenue of $6.06B, up about 28% year over year and about 11% from Q2. Analysts had expected roughly $5.9B.",
        "READ IT RIGHT", "TI makes analog and embedded chips: the parts that handle power and real-world signals.", CYAN)
content(3, 52, "$2.62", "EARNINGS PER SHARE", "Profit per share beat estimates",
        "EPS was $2.62 against estimates near $2.42. Net income was $2.43B, up 78% from $1.36B a year earlier.",
        "WHY IT MATTERS", "Net income grew 78% while revenue grew 28%, so profit outpaced sales.", GOLD)
content(4, 53, "+32%", "ANALOG", "Analog led the growth",
        "Analog revenue was $4.91B, up 32% year over year. Embedded processing was $858M, up 21%. Analog is the larger of the two by far.",
        "READ IT RIGHT", "Embedded processing = microcontrollers and processors that run inside devices and machines.", CYAN)
content(5, 54, "$6.3B", "Q4 OUTLOOK", "Guidance sits above estimates",
        "TI guides Q4 revenue of $5.8B to $6.3B and EPS of $2.45 to $2.79. Analysts had expected about $5.75B and $2.27 to $2.31.",
        "READ IT RIGHT", "Guidance is a company forecast, not a result. Actual numbers can differ.", GOLD)
content(6, 55, "$8.4B", "CASH FLOW", "Free cash flow over 12 months",
        "Trailing twelve-month free cash flow was about $8.4B. Operating cash flow was about $9.9B and capex about $2.6B over the same period.",
        "WHY IT MATTERS", "Free cash flow is cash left after operating costs and capital spending (capex).", CYAN)
content(7, 56, "VLSI", "TERM OF THE DAY", "What is an analog chip?",
        "Digital chips work with 1s and 0s. Analog chips handle smooth real-world signals like voltage, temperature and sound, and manage power in circuits.",
        "PLAIN LANGUAGE", "Every phone, car and factory machine needs analog chips to talk to the physical world.", GOLD)
content(8, 57, "Next", "WHAT TO WATCH", "Is the analog recovery lasting?",
        "Watch whether Q4 lands inside the guided range and how TI's fab spending evolves. Q4 results are expected in January 2027.",
        "NOTE", "Educational summary of company-reported figures. Not investment advice.", CYAN)
cta(9)
print("ok")

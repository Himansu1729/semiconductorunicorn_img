import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "TSMC OCT 2026 SALES"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 400, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 10, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "TSMC's Oct", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "sales +59.7%", F("Inter-ExtraBold.otf", 118), CYAN, 940, 128)
    text_block(d, 72, y + 24, "October revenue hit NT$586.89B, up 59.7% from a year ago, as AI chip demand stays strong.",
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
content(2, 51, "NT$586.89B", "OCTOBER 2026", "TSMC's sales in one month",
        "TSMC reported consolidated revenue of about NT$586.89 billion for October, published on Nov 10, 2026. That is roughly NT$19B of sales per day.",
        "READ IT RIGHT", "Monthly sales are an early read on demand, before the quarterly earnings call.", CYAN)
content(3, 52, "+59.7%", "YEAR OVER YEAR", "Nearly 60% above last October",
        "October 2025 revenue was about NT$367.47B, so the same month a year later is up 59.7%.",
        "WHY IT MATTERS", "AI accelerators and servers keep pulling more wafers through TSMC's advanced nodes.", GOLD)
content(4, 53, "+14.7%", "MONTH OVER MONTH", "A big step up from September",
        "September revenue was about NT$511.86B, so October grew 14.7% in a single month.",
        "READ IT RIGHT", "Monthly numbers can swing with shipment timing, so look at the trend, not one month.", CYAN)
content(5, 54, "NT$4,485.62B", "JANUARY - OCTOBER", "Ten months in: up 43.3%",
        "Cumulative 2026 revenue through October was about NT$4,485.62 billion, 43.3% above the same period of 2025.",
        "WHY IT MATTERS", "TSMC says full-year 2026 revenue should grow about 44% in US dollars.", GOLD)
content(6, 55, "VLSI TERM", "FOUNDRY", "What is a foundry?",
        "A foundry manufactures chips that other companies design. Fabless firms send TSMC a finished layout, and TSMC fabs it on wafers.",
        "IN PLAIN WORDS", "Designers draw the chip. The foundry builds it. Foundry sales reflect many customers' demand.", CYAN)
content(7, 56, "$52.3-54.3B", "Q4 GUIDANCE", "What TSMC expects for Oct-Dec",
        "TSMC guided Q4 2026 revenue to US$52.3 to 54.3 billion, with a gross margin of 65% to 67%. Q3 revenue was NT$1,494.24B.",
        "READ IT RIGHT", "Guidance is a forecast and uses an assumed exchange rate of NT$31.8 per US dollar.", GOLD)
content(8, 57, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) November sales, due in early December. 2) Whether Q4 lands inside the guided range. 3) Capex, budgeted at US$60-64B for 2026.",
        "NOT ADVICE", "This is a summary of company-reported figures, not investment advice.", CYAN)
cta(9)
print("ok")

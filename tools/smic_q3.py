import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "SMIC Q3 2026 RESULTS"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 400, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 12, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "SMIC's Q3", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "record $3.19B", F("Inter-ExtraBold.otf", 118), CYAN, 940, 128)
    text_block(d, 72, y + 24, "China's top foundry ran its fabs at 97.3% utilization and beat its own margin guidance.",
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
content(2, 61, "$3.19B", "Q3 2026 REVENUE", "A record quarter for SMIC",
        "SMIC reported third-quarter revenue of about $3.19 billion, up 6.1% from the second quarter and above analyst expectations.",
        "READ IT RIGHT", "Q3 means July to September 2026. Figures are company-reported, in US dollars.", CYAN)
content(3, 62, "29.9%", "GROSS MARGIN", "Margin beat the guidance",
        "Gross margin reached 29.9%, above the company's own 26% to 28% guidance and up from 25.3% in the second quarter.",
        "WHY IT MATTERS", "Higher margin means each wafer earns more after the cost of making it.", GOLD)
content(4, 63, "97.3%", "FAB UTILIZATION", "Fabs running almost flat out",
        "Capacity utilization rose 3.6 points to 97.3%, from 93.7% in the second quarter.",
        "READ IT RIGHT", "Near 100% means little spare capacity. Demand, not empty fabs, is the limit.", CYAN)
content(5, 64, "$428M", "NET PROFIT", "Net profit of $428 million",
        "Net profit attributable to SMIC was about $428 million for the quarter, per the company's earnings call.",
        "WHY IT MATTERS", "AI-related products are supply-constrained, which supports strong demand for SMIC's wafers.", GOLD)
content(6, 65, "VLSI TERM", "UTILIZATION", "What is fab utilization?",
        "Utilization is the share of a fab's installed wafer capacity that is actually running. 97.3% means almost every tool slot is busy.",
        "IN PLAIN WORDS", "Fabs earn most when busy, but at the limit, new orders must wait in line.", CYAN)
content(7, 66, "+4-6%", "Q4 GUIDANCE", "What SMIC expects next",
        "For Q4, SMIC guided revenue up 4% to 6% from Q3, with gross margin of 26% to 28%. For all of 2026 it expects revenue above $12B, about 30% growth.",
        "READ IT RIGHT", "Guidance is a forecast, not a result. Management expects utilization to ease slightly.", GOLD)
content(8, 67, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) Equipment supply: longer delivery times may shift the timing of capex. 2) Whether Q4 lands in the guided range. 3) New capacity coming online.",
        "NOT ADVICE", "This is a summary of company-reported figures, not investment advice.", CYAN)
cta(9)
print("ok")

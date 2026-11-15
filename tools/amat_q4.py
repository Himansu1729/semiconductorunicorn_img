import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "APPLIED MATERIALS Q4 FY26"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 400, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 12, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Applied Materials'", F("Inter-ExtraBold.otf", 100), WHITE, 940, 110)
    y = text_block(d, 72, y, "record $10.41B", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "The chip-equipment giant's quarterly sales jumped 53% as AI demand drives fab spending.",
               F("Inter-Medium.otf", 40), MUTED, 900, 56)
    chip_graphic(img, 540, 1060, 290)
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
content(2, 71, "$10.41B", "Q4 FY2026 REVENUE", "A record quarter",
        "Applied Materials reported revenue of about $10.41 billion for the quarter ended Oct 25, 2026, up 53% from a year earlier.",
        "READ IT RIGHT", "Applied's fiscal Q4 is roughly late July to late October. Figures are company-reported.", CYAN)
content(3, 72, "$8.0B", "SEMICONDUCTOR SYSTEMS", "The chip-tool business led",
        "Semiconductor Systems, which sells the machines that build chips, brought in about $7.996 billion. Services added about $1.896 billion.",
        "WHY IT MATTERS", "Tool sales show how much chipmakers are spending to build new capacity.", GOLD)
content(4, 73, "$4.16", "ADJUSTED EPS", "Profit per share beat the forecast",
        "Non-GAAP earnings per share were $4.16, up 92% year over year, with a non-GAAP gross margin of 50.6%. GAAP EPS was $3.40.",
        "READ IT RIGHT", "Non-GAAP leaves out some one-off items. GAAP is the strict accounting figure.", CYAN)
content(5, 74, "25%", "CHINA SHARE", "China was about a quarter of sales",
        "China brought in about $2.64 billion, 25% of quarterly revenue (27% for the full fiscal year). Taiwan was 28% and Korea 17%.",
        "WHY IT MATTERS", "Where tools ship shows where new fab capacity is being built.", GOLD)
content(6, 75, "VLSI TERM", "WAFER FAB EQUIPMENT", "What is WFE?",
        "Wafer fab equipment (WFE) is the machinery inside a fab: deposition, etch, inspection and more, which turn blank wafers into chips.",
        "IN PLAIN WORDS", "Applied makes tools that lay down and shape thin films on the wafer, layer by layer.", CYAN)
content(7, 76, "+40%", "SEMI SYSTEMS OUTLOOK", "What management expects",
        "Applied expects Semiconductor Systems revenue to grow more than 40% in calendar 2026. For next quarter it guides revenue of $11.1B, plus or minus $500M.",
        "READ IT RIGHT", "Guidance is a forecast, not a result. CEO Gary Dickerson cited AI as a key driver.", GOLD)
content(8, 77, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) Whether next quarter lands in the $10.6B to $11.6B range. 2) Other equipment makers' results. 3) How China's share of tool sales evolves.",
        "NOT ADVICE", "This is a summary of company-reported figures, not investment advice.", CYAN)
cta(9)
print("ok")

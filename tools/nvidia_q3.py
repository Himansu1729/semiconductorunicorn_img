import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "NVIDIA Q3 FY2027"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 440, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 17, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Nvidia posts", F("Inter-ExtraBold.otf", 112), WHITE, 940, 110)
    y = text_block(d, 72, y, "$115.8B quarter", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "Revenue up 103% from a year ago, driven by data centers, with a $130B outlook for next quarter.",
               F("Inter-Medium.otf", 40), MUTED, 900, 56)
    chip_graphic(img, 540, 1100, 270)
    d = ImageDraw.Draw(img)
    d.text((72 * S, (H - 96) * S), HANDLE, font=F("Inter-Bold.otf", 28), fill=WHITE)
    t2 = "SWIPE  →"; f2 = F("Inter-Bold.otf", 26)
    d.text((W * S - 72 * S - f2.getlength(t2), (H - 94) * S), t2, font=f2, fill=CYAN)
    finish(img, "slide_01.png")

def content(idx, seed, head, tag, title, body, why_label, why, accent=CYAN):
    img = gradient()
    glow(img, 950, 220, 320, accent, 50); traces(img, seed, 26)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx, label=LABEL)
    d.text((72 * S, 150 * S), head, font=F("Inter-ExtraBold.otf", 104), fill=accent)
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
content(2, 101, "$115.8B", "TOTAL REVENUE", "Nvidia's fiscal Q3 2027 revenue",
        "For the quarter ended Oct 25, 2026, Nvidia reported revenue of $115.8B, up 20% from the previous quarter and 103% from a year earlier. Results came out Nov 17.",
        "WHY IT MATTERS", "Nvidia is the biggest buyer of leading-edge foundry and HBM memory capacity for AI chips.", CYAN)
content(3, 102, "$107.6B", "DATA CENTER", "Data center did the heavy lifting",
        "Data center revenue was $107.6B, up 21% from the prior quarter and 110% year over year. That is roughly 93% of total revenue (our math from the two figures).",
        "READ IT RIGHT", "Company-reported figures. The 93% share is our own division, not Nvidia's number.", GOLD)
content(4, 103, "74.9%", "GROSS MARGIN", "Margins stayed very high",
        "Non-GAAP gross margin was 74.9% (GAAP 74.8%). Non-GAAP earnings per diluted share were $2.68; GAAP EPS was $2.70.",
        "VLSI TERM", "Gross margin is the share of revenue left after the direct cost of making the product.", CYAN)
content(5, 104, "$130B", "Q4 OUTLOOK", "Guidance for the next quarter",
        "Nvidia guides Q4 revenue to $130.0B, plus or minus 3%, with gross margin of 71.0% to 72.0%. Q4 includes an extra week, and the outlook assumes no Data Center compute revenue from China.",
        "READ IT RIGHT", "Guidance is a forecast, not a result. It can change.", GOLD)
content(6, 105, "RUBIN", "ROADMAP", "Vera Rubin ramp is under way",
        "Interim CEO and CFO Colette Kress said in the release that Vera Rubin is off to an explosive start and the roadmap is on track. Rubin is Nvidia's next AI platform after Blackwell.",
        "WHY IT MATTERS", "A new platform means new demand for advanced packaging, HBM and cutting-edge wafers.", CYAN)
content(7, 106, "VLSI TERM", "HBM", "What is HBM?",
        "High Bandwidth Memory stacks several DRAM dies vertically and links them with very short, wide connections right next to the processor, so data moves much faster than with ordinary memory.",
        "IN PLAIN WORDS", "Like a tall library next to the reader instead of a warehouse across town.", GOLD)
content(8, 107, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) Whether Q4 lands near the $130B guide. 2) How Rubin volumes ramp. 3) The effect of the new US export rule on AI chip shipments to China and Southeast Asia.",
        "NOT ADVICE", "This summarizes company-reported figures, not investment advice.", CYAN)
cta(9)
print("ok")

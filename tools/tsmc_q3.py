import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "TSMC Q3 2026"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 400, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 15, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "TSMC's", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "record profit", F("Inter-ExtraBold.otf", 118), CYAN, 940, 128)
    text_block(d, 72, y + 24, "Net profit hit NT$763B as AI chip demand lifted sales above the top of its own guidance.",
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
content(2, 41, "NT$763B", "NET PROFIT", "A record, sixth in a row",
        "TSMC's July–September net profit rose 68.7% from a year earlier and beat analyst estimates. It topped the prior record of NT$706.6B from Q2.",
        "READ IT RIGHT", "NT$763B is roughly US$23.6B. Profit is what is left after all costs, not sales.", CYAN)
content(3, 42, "$46.7B", "REVENUE", "Sales beat TSMC's own forecast",
        "Q3 revenue of about US$46.7B was up about 16% from Q2 and above the top of the company's US$44.6B to US$45.8B guidance range.",
        "WHY IT MATTERS", "HPC (AI accelerators and servers) was 68% of revenue, up from 57% a year earlier.", GOLD)
content(4, 43, "66.4%", "MARGINS", "Still huge, but slightly lower",
        "Gross margin was 66.4%, down 1.3 points from Q2, mainly because the 2nm ramp is still early. Operating margin was 58.7%. EPS was NT$29.43.",
        "READ IT RIGHT", "Gross margin = share of sales left after the direct cost of making the chips.", CYAN)
content(5, 44, "8%", "2NM", "2nm is now 8% of wafer revenue",
        "Share of wafer revenue in Q3: 2nm 8% (up from 3% in Q2), 3nm 33%, 5nm 28%, 7nm 10%. Nodes at 7nm and below made up 79%.",
        "WHY IT MATTERS", "A brand-new node reaching 8% in its first full quarters shows how fast leading customers move.", GOLD)
content(6, 45, "$54.3B", "Q4 OUTLOOK", "Next quarter's guide goes higher",
        "TSMC guides Q4 revenue of US$52.3B to US$54.3B, gross margin of 65% to 67% and operating margin of 56.5% to 58.5%.",
        "READ IT RIGHT", "Guidance is a company forecast, not a result. Actual numbers can differ.", CYAN)
content(7, 46, "VLSI", "TERM OF THE DAY", "What is a process node?",
        "A process node is a generation of chip-making technology, like 5nm, 3nm or 2nm. Newer nodes pack more transistors per area and use less power.",
        "PLAIN LANGUAGE", "Node names are marketing labels now, not exact measured feature sizes.", GOLD)
content(8, 47, "Next", "WHAT TO WATCH", "Revenue is not the whole story",
        "Watch how 2nm margins improve as volume grows, and whether Q4 lands inside the guided range. Monthly sales reports give an early read.",
        "NOTE", "Educational summary of company-reported figures. Not investment advice.", CYAN)
cta(9)
print("ok")

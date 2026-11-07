import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "MICROCHIP Q2 FY27"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 51, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 420, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 5, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Microchip sales", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "up 42% in a year", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "Fiscal Q2 2027: $1.62B revenue as data center and industrial demand ramp.",
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
content(2, 511, "$1.62B", "WHAT HAPPENED", "Microchip reports fiscal Q2 2027",
        "On Nov 5, Microchip said net sales for the quarter ended Sep 30 were $1.62B, up 42% from a year ago and 9% from the prior quarter. Non-GAAP EPS was $0.97.",
        "NOTE", "GAAP EPS was $0.68.", CYAN)
content(3, 512, "66.5%", "MARGINS", "Non-GAAP gross margin 66.5%",
        "GAAP gross margin was 65.9%. Non-GAAP operating income was $640M, or 39.5% of sales; GAAP operating margin was 28.6%.",
        "WHY IT MATTERS", "Gross margin is the share of sales left after making the chips.", GOLD)
content(4, 513, "24", "DATA CENTER", "PCIe Gen6 design wins doubled",
        "Management says growth was broad-based, led by industrial and data center. Design wins for PCIe Gen6 switches and retimers rose to 24, from 12 a quarter earlier.",
        "NOTE", "A design win means a customer picked the chip for a product.", CYAN)
content(5, 514, "$53M", "ONE-OFF", "Some sales will not repeat",
        "About $53M of the September quarter's revenue came from infrequent items that Microchip says will not recur in the December quarter.",
        "NOTE", "Management says guidance is 5% to 7% better than normal seasonality.", GOLD)
content(6, 515, "VLSI", "TERM OF THE DAY", "What is a PCIe retimer?",
        "A small chip that cleans up and re-sends a high-speed PCIe signal so it can travel farther across a server board. Faster generations like Gen6 lose more signal, so retimers matter more.",
        "PLAIN LANGUAGE", "Think of it as a signal booster for chip-to-chip links.", CYAN)
content(7, 516, "Lead", "SUPPLY", "Lead times are getting longer",
        "Bookings stayed strong, with book-to-bill well above 1. Lead times are lengthening and Microchip says it is working to add capacity and secure more wafer supply.",
        "REMINDER", "Book-to-bill above 1 means orders exceed shipments.", GOLD)
content(8, 517, "Next", "WHAT TO WATCH", "December quarter guidance",
        "Net sales of $1.573B to $1.638B (midpoint down 1% from September), non-GAAP gross margin 64% to 65%, non-GAAP EPS $0.87 to $0.95.",
        "NOTE", "Company-reported figures. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "RAPIDUS FUNDING"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 25, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 500, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 19–20, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Japan plans ¥400B", F("Inter-ExtraBold.otf", 84), WHITE, 940, 136)
    y = text_block(d, 72, y, "more for Rapidus", F("Inter-ExtraBold.otf", 92), CYAN, 940, 128)
    text_block(d, 72, y + 24, "METI wants to add equity to the 2nm startup, lifting planned state investment to ¥650B.",
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
content(2, 71, "Oct 19", "WHAT HAPPENED", "Japan's METI asks for more Rapidus equity",
        "At a Finance Ministry advisory panel, Japan's industry ministry laid out a plan to invest another 400 billion yen (about $2.5B) in Rapidus over three years, through fiscal 2029.",
        "PLAN, NOT LAW", "It is a funding plan sent to an advisory panel. Budgets still need approval.", CYAN)
content(3, 72, "¥650B", "KEY NUMBERS", "Total state stake would reach 650 billion yen",
        "Japan has already decided to invest 250 billion yen in Rapidus. Adding 400 billion would take the government's planned total to 650 billion yen.",
        "THE MATH", "250 billion already decided + 400 billion proposed = 650 billion yen.", GOLD)
content(4, 73, "150·150·100", "THE SCHEDULE", "Spread over fiscal 2027 to 2029",
        "The proposed 400 billion yen splits into 150 billion in fiscal 2027, 150 billion in fiscal 2028 and 100 billion in fiscal 2029. Only the first year is in the ministry's budget request so far.",
        "NOTE", "Japan's fiscal year starts in April, so fiscal 2027 begins in April 2027.", CYAN)
content(5, 74, "¥2T", "WHY EQUITY?", "A stronger balance sheet unlocks loans",
        "MLex reports the extra equity is meant to help Rapidus secure about 2 trillion yen in private loans, partly backed by government debt guarantees. Reports say it also raises the equity ratio to ease bank borrowing.",
        "WHY IT MATTERS", "Fabs cost billions before they earn anything, so lenders look closely at equity.", GOLD)
content(6, 75, "2nm", "THE TARGET", "Mass production targeted for 2H fiscal 2027",
        "Rapidus is preparing to start mass production of 2-nanometer chips in the second half of fiscal 2027, which runs from October 2027 to March 2028.",
        "REMEMBER", "A node name like 2nm is a generation label, not a measured size.", CYAN)
content(7, 76, "VLSI", "TERM OF THE DAY", "What is a foundry?",
        "A foundry manufactures chips designed by other companies. Customers bring a design and the foundry's process turns it into silicon. Rapidus aims to be a leading-edge foundry.",
        "PLAIN LANGUAGE", "Designers without fabs are called fabless; they rely on foundries like Rapidus or TSMC.", GOLD)
content(8, 77, "Next", "WHAT TO WATCH", "What could change",
        "Watch for budget decisions, how bank lending develops, whether Rapidus hits its 2nm schedule, and whether it lines up customers for the process.",
        "NOTE", "Based on press reports of a ministry plan. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

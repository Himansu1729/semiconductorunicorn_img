import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "KOREA CHIP EXPORTS"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 19, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 560, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 21, 2026 · RECORD", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Korea chip exports", F("Inter-ExtraBold.otf", 104), WHITE, 940, 116)
    y = text_block(d, 72, y, "up 222.5%", F("Inter-ExtraBold.otf", 104), CYAN, 940, 116)
    text_block(d, 72, y + 24, "A record $27.5B of chips shipped out of South Korea in the first 20 days of October.",
               F("Inter-Medium.otf", 40), MUTED, 900, 56)
    chip_graphic(img, 540, 1095, 220)
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
content(2, 71, "$27.5B", "THE HEADLINE", "A record 20-day chip haul",
        "Korea Customs Service data, reported by Yonhap on Oct 21, shows South Korea exported $27.5 billion of semiconductors from Oct 1 to 20. That is up 222.5% from a year earlier and a record for the period.",
        "READ IT RIGHT", "This is a partial-month figure: only the first 20 days of October.", CYAN)
content(3, 72, "44.7%", "THE SHARE", "Chips were nearly half of all exports",
        "Chips made up 44.7% of South Korea's total exports of $61.6 billion in the period. That share is up 16.2 percentage points from a year earlier, and total exports more than doubled.",
        "BIG PICTURE", "Chips were the largest contributor to Korea's export growth.", GOLD)
content(4, 73, "Where", "THE DESTINATIONS", "Shipments up to China and the US",
        "Total exports to China reached $16.6 billion (up 154.4%) and to the United States $10.7 billion (up 154.9%) in the 20 days. Exports to the EU rose 78.2% and to Vietnam 74.6%.",
        "NOTE", "These are all-product totals by destination, not chip-only splits.", CYAN)
content(5, 74, "Daily", "THE PACE", "$4.74B shipped per working day",
        "Average daily exports were $4.74 billion, the highest first-20-days average for any month. Year to date through Oct 20, Korea's exports total $876.3 billion, up 59.5%.",
        "CONTEXT", "Reports do not break chip exports into memory vs other types.", GOLD)
content(6, 75, "VLSI", "TERM OF THE DAY", "What is DRAM?",
        "DRAM is the fast working memory in computers and AI servers. Each bit sits in a tiny cell of one transistor and one capacitor that must be refreshed constantly. HBM stacks many DRAM dies for AI chips.",
        "PLAIN LANGUAGE", "DRAM is the desk a processor works on; storage is the filing cabinet.", CYAN)
content(7, 76, "Why", "WHY IT MATTERS", "A big signal for the chip market",
        "South Korea is home to Samsung and SK hynix, two of the biggest memory makers. National export data is one early signal of how much chip demand is flowing through the supply chain.",
        "FOR ENGINEERS", "Chip trade data helps engineers see where the industry is heading.", GOLD)
content(8, 77, "Next", "WHAT TO WATCH", "Price or volume?",
        "Reports do not say how much of the jump comes from higher prices versus more chips shipped. Watch the full-month October data and the memory makers' next earnings for the answer.",
        "NOTE", "Early-month customs data can be revised. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

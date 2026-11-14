import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "GF MALTA FAB"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 400, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 13, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "GlobalFoundries", F("Inter-ExtraBold.otf", 104), WHITE, 940, 136)
    y = text_block(d, 72, y, "breaks ground", F("Inter-ExtraBold.otf", 112), CYAN, 940, 128)
    text_block(d, 72, y + 24, "A new 300 mm fab in Malta, New York, under a US-Japan initiative of up to $21B.",
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
content(2, 71, "$21B", "US-JAPAN INITIATIVE", "Up to $21B for new fabs",
        "On Nov 13 GlobalFoundries broke ground on a new 300 mm fab at its Malta, New York site. The US-Japan initiative provides up to $21 billion, with Japan supplying the investment.",
        "READ IT RIGHT", "Up to means a ceiling. The second fab depends on further investment.", CYAN)
content(3, 72, "~$10B", "FIRST FAB", "About $10B for fab one",
        "The first fab's initial investment is about $10 billion, backed by $570 million in New York State incentives. About $10 billion more would fund a second fab.",
        "WHY IT MATTERS", "Fabs are among the costliest factories on Earth, so funding shapes where chips get made.", GOLD)
content(4, 73, "900K", "WAFERS PER YEAR", "900,000 wafers a year, per fab",
        "At full operation each fab is expected to add about 900,000 300 mm wafers of annual US manufacturing capacity.",
        "READ IT RIGHT", "300 mm is the standard wafer diameter, about 12 inches, used in modern fabs.", CYAN)
content(5, 74, "2029", "TIMELINE", "First fab online in 2029",
        "GlobalFoundries expects the first fab to come online in 2029. It targets automotive, industrial and connected infrastructure chips.",
        "WHY IT MATTERS", "These are mature-node chips: power, connectivity and embedded parts that cars and factories rely on.", GOLD)
content(6, 75, "VLSI TERM", "300 MM FAB", "What is a 300 mm fab?",
        "A 300 mm fab processes wafers 300 millimeters wide. A bigger wafer fits more chips per run, which usually lowers the cost per chip.",
        "IN PLAIN WORDS", "Think of it as a larger baking tray: same oven time, more cookies.", CYAN)
content(7, 76, "27,000", "JOBS", "Jobs and the local ecosystem",
        "GF says the project supports about 27,000 construction and ecosystem jobs, plus more than 1,000 high-skilled manufacturing jobs in New York's Capital Region.",
        "READ IT RIGHT", "These are company-stated estimates, not measured outcomes.", GOLD)
content(8, 77, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) Construction milestones toward 2029. 2) Whether the second fab gets its funding. 3) Which customers commit to the new capacity.",
        "NOT ADVICE", "This is a summary of company-reported information, not investment advice.", CYAN)
cta(9)
print("ok")

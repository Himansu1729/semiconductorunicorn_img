import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "KOREA OCT EXPORTS"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 19, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 640, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 1, 2026 · OCTOBER DATA", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Korea chip exports", F("Inter-ExtraBold.otf", 104), WHITE, 940, 116)
    y = text_block(d, 72, y, "up 259% in a year", F("Inter-ExtraBold.otf", 104), CYAN, 940, 116)
    text_block(d, 72, y + 24, "South Korea shipped $56.4B of chips in October 2026, about half of all its exports.",
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
content(2, 81, "$115.3B", "THE HEADLINE", "Korea's October exports nearly doubled",
        "South Korea's trade ministry reported total October exports of $115.28 billion, up 93.7% from a year earlier. It is the second-largest month on record, after September.",
        "READ IT RIGHT", "These are preliminary figures from the ministry's Nov 1 release.", CYAN)
content(3, 82, "$56.4B", "KEY NUMBER", "Chip exports jumped 259.4%",
        "Semiconductor exports were $56.44 billion, roughly 49% of all exports. Chips topped $50 billion for a second month in a row.",
        "BIG PICTURE", "About one export dollar in every two came from chips.", GOLD)
content(4, 83, "+496%", "COMPUTERS TOO", "Computer exports hit $5.85B",
        "Exports of computers, which include server SSDs, rose 496.6%. Excluding chips, exports still grew about 34%, and 18 of the top 20 export items rose.",
        "NOTE", "Shipbuilding was a weak spot, down 43.6%.", CYAN)
content(5, 84, "Why", "WHAT'S DRIVING IT", "AI spending keeps chip prices and volumes high",
        "Korean officials point to big tech capital spending on AI infrastructure. It has kept both chip prices and shipment volumes high, and server demand lifted SSD sales.",
        "CONTEXT", "South Korea is home to memory leaders Samsung and SK hynix.", GOLD)
content(6, 85, "VLSI", "TERM OF THE DAY", "What is NAND flash?",
        "NAND flash is the memory that keeps data when power is off. Bits are stored as charge in cells that are stacked in many layers. Server SSDs are built from it.",
        "PLAIN LANGUAGE", "DRAM is the desk you work on; NAND is the filing cabinet.", CYAN)
content(7, 86, "$1T", "MILESTONE", "A trillion-dollar export year is near",
        "January to October exports total about $930 billion, up 60.6%. About $70 billion is left, and the ministry expects $1 trillion to be passed in November.",
        "WHY IT MATTERS", "Only the US, China and Germany have reached it before, per reports.", GOLD)
content(8, 87, "Next", "WHAT TO WATCH", "What could change",
        "Watch November's export data and whether the $1 trillion mark is reached, how chip share holds, and whether gains spread beyond a few large firms.",
        "NOTE", "Preliminary government data. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

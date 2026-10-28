import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "SK HYNIX Q3"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 41, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 430, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 28, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "SK hynix posts", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "an 80% margin", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "Record Q3: KRW 104.6 trillion in revenue, the first quarter above 100 trillion.",
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
content(2, 91, "KRW 104.6T", "WHAT HAPPENED", "SK hynix reports a record third quarter",
        "On Oct 28, SK hynix reported Q3 revenue of KRW 104.62 trillion, up 328% from a year earlier and 32% from Q2. It is the first time the company has crossed KRW 100 trillion in a quarter.",
        "CONTEXT", "Driven by AI demand for HBM and server memory.", CYAN)
content(3, 92, "80%", "KEY NUMBERS", "Operating profit of KRW 83.33 trillion",
        "Operating profit rose 632% year over year and 38% from Q2, the sixth straight quarterly record. Operating margin reached about 80%, up a few points from Q2.",
        "NET PROFIT", "KRW 39.78T, down 58% from Q2 on large non-operating losses (investments, FX).", GOLD)
content(4, 93, "+high 20s%", "WHAT DROVE IT", "Higher memory prices plus HBM4 ramp",
        "DRAM average selling prices rose in the high-20% range from Q2, with HBM4 in full mass production. NAND prices rose in the mid-20% range while NAND shipments dipped slightly.",
        "SERVER", "Server DDR5 shipments rose more than 40% from the prior quarter.", CYAN)
content(5, 94, "KRW 100T", "SHAREHOLDER RETURNS", "About KRW 100 trillion back to investors",
        "The 2026 plan includes at least KRW 30T in dividends and at least KRW 60T in buybacks and cancellations. The Q3 dividend is KRW 20,000 per share, including a KRW 10,000 special payout.",
        "SOURCE", "Special dividend tied to gains on its Kioxia stake, per company slides.", GOLD)
content(6, 95, "VLSI", "TERM OF THE DAY", "What is HBM4?",
        "High Bandwidth Memory stacks many DRAM dies and links them with vertical wires (TSVs), then places the stack right beside an AI processor. HBM4 is the newest generation, built for even wider data paths.",
        "PLAIN LANGUAGE", "Think of it as a memory skyscraper next to the GPU, not a flat chip across the room.", CYAN)
content(7, 96, "2029", "DEMAND OUTLOOK", "HBM and DRAM are sold out through 2029",
        "SK hynix says long-term agreements with 14 key customers cover over 50% of its 2027 and 2028 capacity. It expects HBM4 to pass HBM3E in shipments and revenue in Q4.",
        "TAKEAWAY", "Memory is now a strategic AI bottleneck, not just a commodity part.", GOLD)
content(8, 97, "Next", "WHAT TO WATCH", "What could change",
        "Watch the Q4 guide (DRAM shipments up in the mid-20% range), the HBM4 ramp, much higher 2027 capex, and whether prices keep climbing. Solidigm's IPO has been shelved for now.",
        "NOTE", "Company-reported figures. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "SAMSUNG x TSMC x NVIDIA"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 19, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 560, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 19, 2026 · REPORTED", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Samsung's HBM,", F("Inter-ExtraBold.otf", 104), WHITE, 940, 116)
    y = text_block(d, 72, y, "built on TSMC 3nm?", F("Inter-ExtraBold.otf", 104), CYAN, 940, 116)
    text_block(d, 72, y + 24, "A report says Nvidia's custom memory will use TSMC for its base die.",
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
content(2, 51, "3nm", "THE REPORT", "Samsung reportedly picks TSMC for the base die",
        "Seoul Economic Daily reported on Oct 18, citing industry sources, that Samsung will use TSMC's 3nm process for the base die of Nvidia's custom HBM. Samsung's chip division reportedly agreed after an internal review.",
        "READ IT RIGHT", "Unconfirmed. TSMC declined to comment on individual customers.", CYAN)
content(3, 52, "NVHBM", "NVIDIA'S MEMORY", "A custom HBM unveiled in August",
        "In NVHBM, the memory controller sits in the base die. Nvidia claims up to 30% more bandwidth and 15% lower power than standard HBM4E.",
        "READ IT RIGHT", "Those performance numbers are Nvidia's own claims, not independent tests.", GOLD)
content(4, 53, "3 vendors", "THE ASK", "Nvidia reportedly asked all three suppliers",
        "Nvidia reportedly asked Samsung, SK hynix and Micron to make the base die on TSMC 3nm, and wants the core DRAM die on the 6th-gen 1c process. The report does not say if the other two agreed.",
        "WHAT WE DON'T KNOW", "Volumes, schedules and contract terms were not reported.", CYAN)
content(5, 54, "First", "A NEW PARTNERSHIP", "Samsung and TSMC working on HBM",
        "The report says it would be their first partnership at the HBM manufacturing stage; they worked together on packaging compatibility about four years ago. Samsung keeps its turnkey model for standard HBM and for custom HBM sold to other customers.",
        "READ IT RIGHT", "Turnkey means one company makes the whole memory stack itself.", GOLD)
content(6, 55, "VLSI", "TERM OF THE DAY", "What is a base die?",
        "An HBM stack is several DRAM dies piled on top of each other. The base die is the logic layer underneath: it talks to the GPU and manages the stack above it.",
        "PLAIN LANGUAGE", "Logic on the base die is made with a logic process like 3nm, not a DRAM process.", CYAN)
content(7, 56, "Why", "WHY IT MATTERS", "Memory design is becoming logic design",
        "When more functions, like the controller, move into the base die, HBM design needs more logic-chip skills such as floorplanning, timing and power work. That is why memory makers are leaning on foundry processes.",
        "FOR ENGINEERS", "The line between a memory chip and a logic chip keeps getting blurrier.", GOLD)
content(8, 57, "Next", "WHAT TO WATCH", "Confirmation is the next step",
        "Watch for official word from Samsung, Nvidia or TSMC, and whether SK hynix and Micron follow with TSMC base dies for NVHBM.",
        "NOTE", "Based on one Korean press report relayed by Benzinga. Not investment advice.", CYAN)
cta(9)
print("ok")

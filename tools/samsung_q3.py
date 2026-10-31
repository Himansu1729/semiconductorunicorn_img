import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "SAMSUNG Q3 2026"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 51, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 430, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 29, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Samsung hits a", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "KRW 107T profit", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "Samsung Q3 2026: the first tech company with a quarterly operating profit above KRW 100 trillion.",
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
content(2, 391, "195.3T", "WHAT HAPPENED", "Samsung posts record Q3 revenue (KRW)",
        "On Oct 29, Samsung Electronics reported Q3 2026 revenue of KRW 195.3 trillion, up 14% from the previous quarter and an all-time quarterly high.",
        "CONTEXT", "Quarter ended Sep 30, 2026. Samsung makes memory, phones, displays and chips for others.", CYAN)
content(3, 392, "107.4T", "KEY NUMBERS", "Operating profit tops KRW 100 trillion",
        "Operating profit was KRW 107.4 trillion, nearly 9x the KRW 12.2 trillion of Q3 2025. Samsung says it is the first tech company above KRW 100 trillion in a quarter. Net profit was KRW 75.1 trillion.",
        "NOTE", "Operating margin was about 55%. Figures are company-reported.", GOLD)
content(4, 393, "106.5T", "WHERE IT CAME FROM", "The chip division earned almost all of it",
        "The Device Solutions (DS) division, which covers memory and foundry, had KRW 147.1 trillion in revenue and KRW 106.5 trillion in operating profit, out of KRW 107.4 trillion in total.",
        "WHY IT MATTERS", "AI data centers are pulling memory prices and chip profits up.", CYAN)
content(5, 394, "HBM4", "MEMORY", "Memory sets records on AI demand",
        "Samsung's memory business hit all-time highs in quarterly revenue and operating profit, and HBM4 sales scaled up sharply. On the call, Samsung said its 2027 HBM supply is already sold out at agreed target prices.",
        "NOTE", "HBM is the stacked memory placed next to AI processors.", GOLD)
content(6, 395, "2nm", "FOUNDRY", "Foundry wins 2nm orders from hyperscalers",
        "Samsung says foundry earnings improved on HBM base-die sales, advanced-node sales and 2nm orders for high-performance computing, including from major cloud companies. It expects 2nm project orders to more than double in 2026.",
        "OUTLOOK", "For Q4, Samsung guides double-digit foundry revenue growth.", CYAN)
content(7, 396, "VLSI", "TERM OF THE DAY", "What is an HBM base die?",
        "An HBM stack is several DRAM dies piled on a logic chip at the bottom, called the base die. It manages data flow between the memory layers and the AI processor beside it.",
        "PLAIN LANGUAGE", "The base die is the traffic controller of an HBM stack.", GOLD)
content(8, 397, "84.4T", "CAPEX", "Samsung keeps spending on capacity",
        "Q3 capex was KRW 29 trillion. Samsung estimates 2026 capex at about KRW 84.4 trillion, of which KRW 76.8 trillion is for the DS chip division. Watch Q4 memory prices, HBM4 ramp and 2nm customers.",
        "REMINDER", "Company-reported figures. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

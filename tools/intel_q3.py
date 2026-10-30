import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "INTEL Q3 2026"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 41, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 430, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 29, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Intel data center", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "sales jump 78%", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "Intel Q3 2026: $16.5B in revenue, up 21% from a year ago.",
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
content(2, 291, "$16.5B", "WHAT HAPPENED", "Intel reports Q3 2026 revenue of $16.5B",
        "On Oct 29, Intel said revenue for the quarter ended Sep 26 rose 21% from $13.7B a year earlier.",
        "CONTEXT", "Intel designs CPUs and also runs its own fabs as Intel Foundry.", CYAN)
content(3, 292, "+78%", "KEY NUMBERS", "Data center and AI revenue hit $7.3B",
        "The Data Center and AI group grew 78% year over year. The Client Computing and Physical AI group, mostly PCs, was $8.1B, down 5%.",
        "NOTE", "Data center sales are now close to PC sales.", GOLD)
content(4, 293, "44.1%", "MARGINS AND PROFIT", "Non-GAAP gross margin up 4.1 points",
        "Non-GAAP gross margin was 44.1% versus 40.0%. GAAP margin was 43.0%. Non-GAAP EPS was $0.52, while GAAP EPS was $0.60 and GAAP net income fell 18% to $3.3B.",
        "NOTE", "GAAP and non-GAAP differ because of company adjustments.", CYAN)
content(5, 294, "$6.7B", "INTEL FOUNDRY", "Foundry revenue up 58% to $6.7B",
        "That figure includes sales to Intel's own product groups. In October Intel released the 14A 0.9 process design kit and announced a High-NA EUV collaboration with ASML.",
        "WHY IT MATTERS", "14A is Intel's next process node for outside and in-house chips.", GOLD)
content(6, 295, "VLSI", "TERM OF THE DAY", "What is a process design kit (PDK)?",
        "A PDK is the package of design rules, device models and libraries a foundry gives chip designers. Designers use it to create chips that the foundry's process can actually build.",
        "PLAIN LANGUAGE", "A PDK is the foundry's recipe book for chip designers.", CYAN)
content(7, 296, "$15-16B", "OUTLOOK", "Q4 guide is below Q3 revenue",
        "Intel guides Q4 revenue to $15.0B-$16.0B. At the midpoint it expects non-GAAP gross margin of 38.0% and non-GAAP EPS of $0.25.",
        "REMINDER", "Guidance is a company forecast, not a result.", GOLD)
content(8, 297, "Next", "WHAT TO WATCH", "What could change",
        "Watch whether Q4 lands inside the guided range, how long data center growth keeps its pace, how PC demand holds up, and which customers adopt 14A.",
        "NOTE", "Company-reported figures. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "SAMSUNG TAYLOR FAB 2"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 51, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 430, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 3, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Samsung's 2nd", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "Texas fab", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "Reported: it will make HBM base dies for AMD and Nvidia on 2nm. Samsung has not confirmed.",
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
content(2, 401, "2nm", "WHAT WAS REPORTED", "A second Taylor plant for HBM base dies",
        "On Nov 3, Reuters relayed a Maeil Business report: Samsung's second foundry plant in Taylor, Texas will make base dies for high-bandwidth memory (HBM) chips using 2nm technology.",
        "SOURCE", "Maeil cites unnamed industry sources. Samsung declined to comment.", CYAN)
content(3, 402, "AMD", "CUSTOMERS", "AMD and Nvidia are named",
        "The report says the plant's customers are AMD and Nvidia, with most of the secured volume for AMD, and that orders already cover the plant's entire output.",
        "NOTE", "None of the companies has confirmed this. Treat it as a report.", GOLD)
content(4, 403, "2.7M", "SIZE", "About 1.5x the first Taylor plant",
        "The plant is described as about 2.7 million square feet, roughly 1.5 times the size of Samsung's first Taylor facility, which Maeil says has a contract with Tesla.",
        "CONTEXT", "Investment size was not given in the report.", CYAN)
content(5, 404, "2030", "TIMELINE", "Mass production is years away",
        "Formal construction is due to start in November 2026, equipment installation from February 2029, and mass production in 2030, according to the report.",
        "WHY IT MATTERS", "Fabs take years to build. Today's HBM supply is not affected.", GOLD)
content(6, 405, "VLSI", "TERM OF THE DAY", "What is an HBM base die?",
        "An HBM stack is several DRAM dies piled on a logic chip at the bottom, called the base die. It manages data flow between the memory layers and the AI processor beside it.",
        "PLAIN LANGUAGE", "The base die is the traffic controller of an HBM stack.", CYAN)
content(7, 406, "WHY", "BIG PICTURE", "Memory is becoming a logic story",
        "Building base dies on an advanced logic process like 2nm means HBM makers lean on foundry skills, not just DRAM. A US site would also put more of the AI memory chain in America.",
        "TAKEAWAY", "HBM now blends memory design, logic design and packaging.", GOLD)
content(8, 407, "TBC", "WHAT TO WATCH", "Still unconfirmed",
        "Watch for official word from Samsung, AMD or Nvidia, the groundbreaking in November, any investment figure, and how the 2nm process performs.",
        "REMINDER", "Based on a media report. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

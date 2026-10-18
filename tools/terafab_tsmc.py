import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "TSMC x TERAFAB"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 33, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 400, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 15, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "TSMC and", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "Musk's Terafab", F("Inter-ExtraBold.otf", 118), CYAN, 940, 128)
    text_block(d, 72, y + 24, "TSMC is in talks about a Texas fab, but says any fab it joins must be run by TSMC.",
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
content(2, 51, "Talks", "WHAT HAPPENED", "TSMC is open to Terafab",
        "On its Oct 15 earnings call, TSMC chairman and CEO C.C. Wei confirmed discussions about Elon Musk's Terafab chip project in Texas. No agreement has been reached.",
        "READ IT RIGHT", "Talks are not a deal. Wei gave no timeline and said TSMC would share more if a firm conclusion is reached.", CYAN)
content(3, 52, "Texas", "THE PLAN", "TSMC is also scouting Texas",
        "Wei said TSMC has sent teams to Texas to evaluate U.S. capacity beyond Arizona, driven by requests from large American customers.",
        "WHY IT MATTERS", "Texas is one option under evaluation, not a confirmed new TSMC site.", GOLD)
content(4, 53, "Who runs it?", "THE CLASH", "Both sides want control",
        "In an Oct 7 post on X, Musk said Tesla and SpaceX would build and run the fab, and TSMC could only sublease part of it. Wei said any fab TSMC joins has to be run by TSMC.",
        "STILL OPEN", "These positions conflict, and neither company has said how it will be resolved.", CYAN)
content(5, 54, "14A", "THE INTEL ANGLE", "Intel's 14A is also in the mix",
        "Intel has been named as another Terafab partner, expected to supply its 14A process. A TSMC role could change that, and one report says the Intel role could be dropped.",
        "READ IT RIGHT", "The process-node plan for Terafab has not been finalized by either company.", GOLD)
content(6, 55, "$46.7B", "DEMAND BACKDROP", "Why TSMC wants more capacity",
        "Wei said AI demand is strong and above TSMC's current supply. Q3 revenue was about US$46.7B, and TSMC guides Q4 revenue of US$52.3B to US$54.3B.",
        "READ IT RIGHT", "Guidance is a company forecast, not a result. Actual numbers can differ.", CYAN)
content(7, 56, "VLSI", "TERM OF THE DAY", "What is a foundry?",
        "A foundry is a company that manufactures chips designed by other companies. Chip designers who outsource manufacturing are called fabless.",
        "PLAIN LANGUAGE", "Terafab would make chips for its own companies, which is different from a foundry serving many customers.", GOLD)
content(8, 57, "Next", "WHAT TO WATCH", "Who ends up running the fab?",
        "Watch for any signed agreement, how ownership and operation are split, which process node is used, and where in Texas TSMC decides to build, if it does.",
        "NOTE", "Educational summary of company statements and press reports. Not investment advice.", CYAN)
cta(9)
print("ok")

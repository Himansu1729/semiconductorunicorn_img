import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 8
LABEL = "INTEL 18A-P"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 31, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 440, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 18, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Intel lands its", F("Inter-ExtraBold.otf", 112), WHITE, 940, 110)
    y = text_block(d, 72, y, "first 18A client", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "CEO Lip-Bu Tan says Intel Foundry has signed its first outside customer for 18A. The name has not been revealed.",
               F("Inter-Medium.otf", 40), MUTED, 900, 56)
    chip_graphic(img, 540, 1100, 270)
    d = ImageDraw.Draw(img)
    d.text((72 * S, (H - 96) * S), HANDLE, font=F("Inter-Bold.otf", 28), fill=WHITE)
    t2 = "SWIPE  →"; f2 = F("Inter-Bold.otf", 26)
    d.text((W * S - 72 * S - f2.getlength(t2), (H - 94) * S), t2, font=f2, fill=CYAN)
    finish(img, "slide_01.png")

def content(idx, seed, head, tag, title, body, why_label, why, accent=CYAN):
    img = gradient()
    glow(img, 950, 220, 320, accent, 50); traces(img, seed, 26)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx, label=LABEL)
    d.text((72 * S, 150 * S), head, font=F("Inter-ExtraBold.otf", 104), fill=accent)
    f_tag = F("Inter-Bold.otf", 28); tw = f_tag.getlength(tag) / S
    rrect(img, (72, 292, 72 + tw + 56, 346), 27, fill=accent, alpha=36, outline=accent + (255,), width=2)
    d = ImageDraw.Draw(img)
    d.text((100 * S, 303 * S), tag, font=f_tag, fill=accent)
    y = text_block(d, 72, 392, title, F("Inter-ExtraBold.otf", 66), WHITE, 936, 78) + 14
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
content(2, 201, "FIRST", "WHAT HAPPENED", "Intel signs an outside 18A customer",
        "On Nov 18, at the TomorrowX Summit in Austin, CEO Lip-Bu Tan said Intel had \"just signed the first customer\" for 18A. Intel's tech chief later said on X that the deal is for the 18A-P version.",
        "WHY IT MATTERS", "A foundry needs outside customers to prove its process is ready for others.", CYAN)
content(3, 202, "18A-P", "THE NODE", "What is 18A-P?",
        "18A-P is a performance-tuned version of Intel's 18A process. Intel says it is compatible with 18A designs, and it entered risk production in June 2026.",
        "READ IT RIGHT", "The customer and product were not named. Press speculation is just that.", GOLD)
content(4, 203, "RISK", "VLSI TERM", "What is risk production?",
        "Risk production means making small batches of real chips on a new process before mass production. It tests that the process and a customer's design work together, with some chance it needs tuning.",
        "IN PLAIN WORDS", "A dress rehearsal on the real stage, before opening night.", CYAN)
content(5, 204, "GAA", "VLSI TERM", "RibbonFET + PowerVia",
        "Intel's 18A family uses RibbonFET, its gate-all-around transistor, where the gate wraps the channel on all sides. It also uses PowerVia, which delivers power from the back of the wafer.",
        "IN PLAIN WORDS", "Better gate control means less leakage. Backside power frees up the front for signal wires.", GOLD)
content(6, 205, "?", "UNKNOWN", "What we still don't know",
        "Not disclosed: who the customer is, what chip they will build, the volume, or when production starts. Ramp timing and yields are the next real proof points.",
        "READ IT RIGHT", "One signed customer is a start, not volume production.", CYAN)
content(7, 206, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) Whether the customer is named. 2) 18A-P moving from risk to volume production. 3) More outside customers following the first one.",
        "NOT ADVICE", "This summarizes press reports, not investment advice.", GOLD)
cta(8)
print("ok")

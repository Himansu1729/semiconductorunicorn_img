import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "TSMC TEXAS FILING"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 41, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 470, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 23, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "TSMC eyes Texas", F("Inter-ExtraBold.otf", 112), WHITE, 940, 110)
    y = text_block(d, 72, y, "for a 2nm campus", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "A TSMC unit filed for a school-tax limit on a proposed $22.6 billion chip campus near College Station. No final decision yet.",
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
content(2, 601, "NOV 23", "WHAT HAPPENED", "TSMC files for a Texas campus",
        "Local news reports say TSMC Arizona Corp. applied under Texas's JETI program for a chip campus in Brazos County, near College Station. The Comptroller has recommended the application.",
        "WHY IT MATTERS", "It shows where TSMC may build next outside Taiwan and Arizona.", CYAN)
content(3, 602, "$22.6B", "KEY NUMBERS", "A very big proposed bill",
        "The application lists about $22.6 billion of investment on roughly 3,232 acres, for one or more fabs plus support facilities.",
        "READ IT RIGHT", "This is the filing amount, not committed spending.", GOLD)
content(4, 603, "2,099", "KEY NUMBERS", "Jobs and pay in the filing",
        "The filing projects at least 2,099 direct jobs, with an average annual salary of about $133,000.",
        "WHY IT MATTERS", "Fabs need engineers and technicians, a signal for chip careers.", CYAN)
content(5, 604, "2nm", "THE TECH", "Aimed at leading-edge chips",
        "The campus would use 2nm or more advanced process technology, making chips for AI, high-performance computing and mobile devices.",
        "READ IT RIGHT", "It is described as a chip fab, not a data center.", GOLD)
content(6, 605, "JETI", "THE TAX BREAK", "A 10-year school tax limit",
        "JETI would let College Station ISD limit the taxable value of TSMC's eligible property for school operating taxes for 10 years. The school board and the Governor's office still have to sign off. A public hearing is set for Dec 10, 2026.",
        "READ IT RIGHT", "Debt-service school taxes would still be paid on full value.", GOLD)
content(7, 606, "NODE", "VLSI TERM", "What is a process node?",
        "A process node is the name of a generation of chip manufacturing technology. Smaller labels like 2nm mean denser, faster, more efficient chips, but today the number is a marketing name, not one literal measurement.",
        "IN PLAIN WORDS", "Think of it as a version number for how finely a fab can build transistors.", CYAN)
content(8, 607, "WATCH", "WHAT'S NEXT", "Not a done deal",
        "TSMC has not made a final investment decision. The land is under contract but not yet purchased, and Sherman in North Texas and Arizona were named as other options. Watch the Dec 10 hearing and the Governor's decision.",
        "NOT ADVICE", "This summarizes local news reports, not investment advice.", GOLD)
cta(9)
print("ok")

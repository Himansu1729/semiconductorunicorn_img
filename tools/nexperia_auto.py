import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "AI VS CAR CHIPS"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 31, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 400, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 10, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "AI is squeezing", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "car chips", F("Inter-ExtraBold.otf", 118), CYAN, 940, 128)
    text_block(d, 72, y + 24, "Nexperia and STMicroelectronics say capacity is shifting to AI chips, creating car-supply bottlenecks.",
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
content(2, 61, "NEXPERIA", "NOV 10 - MUNICH", "\"Totally oversubscribed\"",
        "Interim CEO Stefan Tilger told Reuters at the Electronica trade fair that Nexperia's supply is fully spoken for, and the auto industry is under heavy strain.",
        "READ IT RIGHT", "This is executive commentary from the show floor, not a measured shortage figure.", CYAN)
content(3, 62, "NOV 9", "STMICRO CEO", "\"We see many bottlenecks\"",
        "At a CEO panel before the show, ST's Jean-Marc Chery warned that foundries and chip-packaging firms are shifting resources away from automotive and industrial products.",
        "WHY IT MATTERS", "Packaging is the last step before a chip ships, so a squeeze there can delay finished parts.", GOLD)
content(4, 63, "SHIFT", "WHERE CAPACITY GOES", "AI data centers pull capacity",
        "Tilger said chipmakers are moving manufacturing toward higher-margin AI data-center chips and away from low-cost chips used in cars and industrial gear.",
        "IN PLAIN WORDS", "A fab line can only make so much. When AI chips pay better, cheaper parts can get less room.", CYAN)
content(5, 64, "VLSI TERM", "MATURE NODE", "What is a mature node?",
        "A mature node is an older, well-proven manufacturing process. It is cheap and rugged, and it makes diodes, transistors, power and logic chips that cars rely on.",
        "IN PLAIN WORDS", "Not every chip needs the newest 2 nm process. A car window controller does not.", GOLD)
content(6, 65, "LAGGED", "UNDERINVESTMENT", "Older chips got less funding",
        "Tilger said investment in mature parts like diodes and transistors has lagged for years, and some foundries and packaging firms are pulling back from mainstream technology.",
        "WHY IT MATTERS", "New capacity for old chips is slow to appear, so tight supply can last.", CYAN)
content(7, 66, "OWN FABS", "ST VS NEXPERIA", "Why ST feels more protected",
        "Chery said ST's own manufacturing footprint gives it some cushion, since it controls part of its future through capital spending. Nexperia has a narrower product range.",
        "READ IT RIGHT", "Owning fabs and packaging gives a company more control over where capacity goes.", GOLD)
content(8, 67, "WATCH", "WHAT'S NEXT", "What to watch next",
        "Watch for other suppliers echoing the warning, foundries adding capacity for mature chips, and carmakers reporting delays.",
        "NOT ADVICE", "This summarizes executive remarks reported by Reuters, not investment advice.", CYAN)
cta(9)
print("ok")

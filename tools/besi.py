import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "APPLIED x BESI"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 31, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 430, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 26, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Applied Materials", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "doubles down on Besi", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "Stake in the hybrid-bonding specialist heads from about 9% to about 20%.",
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
content(2, 81, "9% → 20%", "WHAT HAPPENED", "Applied raises its Besi stake to about 20%",
        "On Oct 26, Applied Materials said it will lift its investment in Dutch packaging-equipment maker BE Semiconductor Industries (Besi) to about 20% of shares, up from the roughly 9% it bought in April 2025.",
        "HOW", "Through an accelerated share purchase agreement. No price or share count was disclosed.", CYAN)
content(3, 82, "~9%", "THE MARKET REACTION", "Besi shares jumped on the news",
        "Reuters-reported trading showed Besi up about 9% in Amsterdam on Oct 27. Shares had roughly halved from a June high of about €317 during a wider chip selloff.",
        "NOTE", "Early-session moves change fast; this is a snapshot, not a trend.", GOLD)
content(4, 83, "No board", "THE LIMITS", "Applied is not taking control",
        "Applied says it has no current intention to go beyond about 20% and will not seek a board seat. Share delivery depends on the US Hart-Scott-Rodino antitrust waiting period ending.",
        "WHY IT MATTERS", "A big strategic stake, but not a takeover: Besi stays independent.", CYAN)
content(5, 84, "2020", "THE PARTNERSHIP", "Six years of working together",
        "The firms have collaborated since 2020. Besi recently joined Applied's EPIC Center R&D facility as an innovation partner, and last year Applied introduced Kinex, a die-to-wafer hybrid bonding system developed with Besi.",
        "FOCUS AREAS", "3D chip scaling, logic and memory integration, and die-on-wafer bonding.", GOLD)
content(6, 85, "VLSI", "TERM OF THE DAY", "What is hybrid bonding?",
        "Hybrid bonding joins two chips face to face with huge numbers of tiny copper pads and insulating layers, with no solder bumps between them. Shorter, denser links mean more data moved for less energy.",
        "PLAIN LANGUAGE", "Think of it as gluing chips together so their wiring lines up directly.", CYAN)
content(7, 86, "AI", "WHY APPLIED CARES", "Packaging is now a bottleneck for AI",
        "Applied calls hybrid bonding and next-generation interconnects increasingly critical for energy-efficient AI compute. As AI chips stack memory and logic, how dies are connected matters as much as how they are drawn.",
        "TAKEAWAY", "Chip progress is moving from shrinking transistors to stacking and linking chips.", GOLD)
content(8, 87, "Next", "WHAT TO WATCH", "What could change",
        "Watch for antitrust clearance, any disclosed deal terms, new Kinex customers, and whether hybrid bonding demand holds up after the recent selloff.",
        "NOTE", "Based on Applied's announcement and press reports. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

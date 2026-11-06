import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "ARM Q2 FY27"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 61, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 420, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 4, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Arm licensing sales", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "jumped 50%", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "Arm's fiscal Q2 2027: a record $1.44B in revenue, up 27%.",
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
content(2, 421, "$1.44B", "WHAT HAPPENED", "Arm posts a record quarter",
        "On Nov 4, Arm reported fiscal Q2 2027 revenue of $1.44B, up 27% from a year ago. Non-GAAP EPS was $0.52, up 33%, and non-GAAP operating income rose 37% to $638M.",
        "NOTE", "Fifth straight quarter of growth above 20%, per management.", CYAN)
content(3, 422, "+50%", "LICENSING", "License revenue hit $773M",
        "Licensing and other revenue rose 50% to $773M. Management said customers wanted longer-term commitments, which pulled in deals. SoftBank contributed $209M of it.",
        "WHY IT MATTERS", "Licensing is Arm's upfront fee for using its designs.", GOLD)
content(4, 423, "+8%", "ROYALTIES", "Royalties grew to $670M",
        "Royalty revenue was a Q2 record. Data center royalties roughly doubled and physical AI (cars, robots) grew about 50%, while smartphone royalties were roughly flat as memory prices hurt phone volumes.",
        "WHY IT MATTERS", "Royalties are paid on every chip shipped with an Arm design.", CYAN)
content(5, 424, "VLSI", "TERM OF THE DAY", "What is a compute subsystem (CSS)?",
        "A pre-integrated, pre-verified bundle of Arm CPU cores and supporting blocks. Chip designers drop it into their SoC instead of wiring everything together from scratch. Arm says CSS carries higher royalty rates.",
        "PLAIN LANGUAGE", "Think of it as a ready-made engine, not loose parts.", CYAN)
content(6, 425, "$2B", "ARM'S OWN CHIP", "Bigger bet on its AGI CPU",
        "Arm now has more confidence in up to $2B of AGI CPU revenue across fiscal 2027 and 2028, up from about $1B before. First commercial deliveries are on track for fiscal Q4 2027, with Meta as the main customer.",
        "REMINDER", "That is a company target, not a result.", GOLD)
content(7, 426, "60%+", "DATA CENTER", "Arm in the cloud",
        "Management said Arm-based servers went from about 15% of top hyperscaler compute in 2024 to over 50% in 2025, and expects over 60% by the end of 2026. Amazon, Google and Microsoft are the largest royalty contributors.",
        "NOTE", "These shares are management estimates.", CYAN)
content(8, 427, "Next", "WHAT TO WATCH", "Guidance and what could change",
        "Q3 guide: revenue $1.54B plus or minus $50M and non-GAAP EPS $0.56 plus or minus $0.04. Royalties are guided to low-single-digit growth, with phone demand under pressure. Watch the AGI CPU ramp.",
        "NOTE", "Company-reported figures. Educational summary, not investment advice.", GOLD)
cta(9)
print("ok")

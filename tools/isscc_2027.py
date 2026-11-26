import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 8
LABEL = "ISSCC 2027 MEMORY RACE"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 57, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 470, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 25, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Huawei takes", F("Inter-ExtraBold.otf", 112), WHITE, 940, 122)
    y = text_block(d, 72, y, "the HBM stage", F("Inter-ExtraBold.otf", 112), CYAN, 940, 134)
    text_block(d, 72, y + 24, "ISSCC 2027 lists a Huawei custom HBM paper right after Samsung's HBM4E, plus new DRAM work from CXMT and SK hynix.",
               F("Inter-Medium.otf", 40), MUTED, 900, 56)
    chip_graphic(img, 540, 1050, 260)
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
content(2, 701, "ISSCC", "WHAT HAPPENED", "The 2027 lineup is out",
        "ISSCC, a leading IEEE chip-design conference, meets Feb 14-18, 2027 in San Francisco. Its draft program lists a session on SRAM, HBM and DRAM for Tuesday, Feb 16.",
        "READ IT RIGHT", "These are research papers, not product launches. The draft program can change.", CYAN)
content(3, 702, "4,096", "HUAWEI · DATA PINS", "Twice the width of HBM4",
        "Huawei's paper title lists a custom HBM with 64 channels, 4,096 data (DQ) pins, memory controllers and 5-layer wafer-on-wafer hybrid bonding. The JEDEC HBM4 standard has 32 channels and a 2,048-bit interface.",
        "STILL UNKNOWN", "The program listing gives no capacity, speed or bandwidth figure.", GOLD)
content(4, 703, "17Gb/s", "SAMSUNG · HBM4E", "48GB, 17Gb/s on every pin",
        "In Feb 2026, Samsung said its mass-produced HBM4 runs at 11.7Gb/s per pin, up to 13Gb/s. Korean reports describe the new HBM4E paper as a 12-high stack.",
        "VLSI MATH", "2,048 pins × 17Gb/s ÷ 8 ≈ 4.35 TB/s per stack, the figure Korean reports cite.", CYAN)
content(5, 704, "DRAM", "GOING VERTICAL", "CXMT and SK hynix go upright",
        "China's CXMT lists a 32Gb DDR5 at 9.2Gb/s per pin with vertical-surrounding-gate transistors and copper hybrid bonding. SK hynix lists a 16Gb DDR5 with vertical-gate cells, control circuits stacked over them and bonded wafers.",
        "WHY IT MATTERS", "Upright transistors and stacked circuits are a path to denser DRAM.", GOLD)
content(6, 705, "124", "PAPER SCOREBOARD", "China tops the paper count",
        "Korean reports count 274 accepted papers (not counting invited ones) from 1,029 submissions. China had 124 (45.3%), the US 49, South Korea 45. In memory, Korea led with 12 of 28; China had 8.",
        "READ IT RIGHT", "Paper counts show research activity, not market share or factory output.", CYAN)
content(7, 706, "BOND", "VLSI TERM", "What is hybrid bonding?",
        "It joins two wafers or dies face to face, bonding their flat insulating surfaces and copper pads directly, with no solder bumps. Wafer-on-wafer means whole wafers are bonded before being cut into chips.",
        "IN PLAIN WORDS", "HBM is a stack of DRAM dies with a very wide data path. Finer links help build it.", GOLD)
cta(8)
print("ok")

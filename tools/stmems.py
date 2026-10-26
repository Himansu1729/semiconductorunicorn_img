import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "ST AUTOMOTIVE SENSORS"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 31, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 430, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 26, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "ST launches car", F("Inter-ExtraBold.otf", 84), WHITE, 940, 130)
    y = text_block(d, 72, y, "crash-sensor combos", F("Inter-ExtraBold.otf", 84), CYAN, 940, 120)
    text_block(d, 72, y + 24, "Gyroscope + accelerometer in one 6 mm package, aimed at mass-market vehicles.",
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
content(2, 81, "4 new", "WHAT HAPPENED", "ST unveils four combination safety sensors",
        "On Oct 26, STMicroelectronics launched four automotive sensors that each pack a gyroscope and an accelerometer into one package. ST says they are the first such combo sensors for mass-market vehicles.",
        "USED FOR", "Crash protection, rollover detection, airbag deployment, stability control and radar beam stabilization.", CYAN)
content(3, 82, "−40…105°C", "KEY NUMBERS", "Built for harsh car environments",
        "ST lists an operating range of −40 °C to +105 °C. The parts are in production now, and ST says it guarantees availability for at least 15 years.",
        "WHY 15 YEARS", "Cars stay on the road for many years, so carmakers want long part availability.", GOLD)
content(4, 83, "±350", "SENSING RANGE", "Rotation up to ±350 degrees per second",
        "The gyro range is selectable at ±125, ±250 or ±350 dps. Low-g accelerometer options span ±1.5 g to ±34 g; the medium-g part reaches ±15.5 g to ±150 g.",
        "PLAIN LANGUAGE", "dps = degrees per second of rotation. g = one Earth gravity of acceleration.", CYAN)
content(5, 84, "6 mm", "THE PACKAGE", "A 6 × 6 × 1.9 mm 24-pin QFN",
        "Each sensor sits in a small QFN package with wettable flanks, which make solder joints easier to inspect optically. ST says the parts are ISO 26262 compliant and support SafeSPI.",
        "WHY IT MATTERS", "One package means fewer parts on the board and less space for each safety function.", GOLD)
content(6, 85, "NXP", "THE BACKSTORY", "Follows ST's NXP MEMS deal",
        "ST completed its purchase of NXP's MEMS sensors business in early February 2026, a deal worth up to $950 million depending on milestones. Omdia projects 17.7% yearly growth for inertial units from 2025 to 2030, driven largely by ADAS.",
        "CONTEXT", "Sensor demand grows as cars add more driver-assistance features.", CYAN)
content(7, 86, "VLSI", "TERM OF THE DAY", "What is MEMS?",
        "MEMS means micro-electromechanical systems: microscopic moving structures, like tiny springs and masses, built on silicon with chip-fab steps. A circuit reads their movement as an electrical signal.",
        "PLAIN LANGUAGE", "A MEMS gyro or accelerometer is a tiny mechanical part and a chip working together.", GOLD)
content(8, 87, "Next", "WHAT TO WATCH", "What could change",
        "Watch which carmakers adopt the parts, how ST prices them, and how the NXP MEMS business is folded into ST's lineup. Samples and pricing go through ST sales offices.",
        "NOTE", "Based on ST's own announcement and datasheet. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

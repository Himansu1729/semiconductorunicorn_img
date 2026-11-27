import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 8
LABEL = "3D NAND BONDING DEAL"
BOX_H = 236


def footer(d):
    d.text((72 * S, (H - 96) * S), HANDLE, font=F("Inter-Bold.otf", 28), fill=WHITE)
    t = "SWIPE  →"; f = F("Inter-Bold.otf", 26)
    d.text((W * S - 72 * S - f.getlength(t), (H - 94) * S), t, font=f, fill=CYAN)


def center(d, cx, cy, text, font, fill):
    d.text((cx * S, cy * S), text, font=font, fill=fill, anchor="mm")


def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 91, 40)
    d = ImageDraw.Draw(img)
    f = F("Inter-Bold.otf", 30); t = "REPORTED  •  NOV 2026"
    rrect(img, (72, 150, 72 + f.getlength(t) / S + 56, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d = ImageDraw.Draw(img)
    d.text((100 * S, 164 * S), t, font=f, fill=CYAN)
    fh = F("Inter-ExtraBold.otf", 98)
    y = 262
    for line, col in [("Samsung and", WHITE), ("SK hynix turn to", WHITE), ("China's YMTC", CYAN)]:
        assert fh.getlength(line) / S <= 936, line
        d.text((72 * S, y * S), line, font=fh, fill=col)
        y += 112
    y = text_block(d, 72, y + 30, "Nikkei Asia reports licensing deals for the Chinese memory maker's wafer-bonding technology for 3D NAND.",
                   F("Inter-Medium.otf", 40), MUTED, 900, 56)
    assert y < 830, y
    chip_graphic(img, 540, 1030, 270)
    d = ImageDraw.Draw(img)
    footer(d)
    finish(img, "slide_01.png")


def base(idx, seed, head, tag, title, accent):
    img = gradient()
    glow(img, 950, 220, 320, accent, 50); traces(img, seed, 26)
    d = ImageDraw.Draw(img)
    chrome(img, d, idx, label=LABEL)
    fh = F("Inter-ExtraBold.otf", 104)
    assert fh.getlength(head) / S <= 936, head
    d.text((72 * S, 150 * S), head, font=fh, fill=accent)
    f_tag = F("Inter-Bold.otf", 28); tw = f_tag.getlength(tag) / S
    rrect(img, (72, 292, 72 + tw + 56, 346), 27, fill=accent, alpha=36, outline=accent + (255,), width=2)
    d = ImageDraw.Draw(img)
    d.text((100 * S, 303 * S), tag, font=f_tag, fill=accent)
    y = text_block(d, 72, 392, title, F("Inter-ExtraBold.otf", 62), WHITE, 936, 76) + 14
    return img, d, y


def box(img, y, why_label, why, accent):
    top = max(y + 32, 920); bot = top + BOX_H
    assert bot < H - 120, bot
    rrect(img, (72, top, W - 72, bot), 28, fill=PANEL, alpha=235, outline=(48, 62, 118), width=2)
    rrect(img, (72, top, 84, bot), 6, fill=accent)
    d = ImageDraw.Draw(img)
    d.text((112 * S, (top + 28) * S), why_label, font=F("Inter-Bold.otf", 26), fill=accent)
    end = text_block(d, 112, top + 74, why, F("Inter-SemiBold.otf", 34), WHITE, 856, 49)
    assert end <= bot - 8, (why_label, end, bot)


def content(idx, seed, head, tag, title, body, why_label, why, accent=CYAN):
    img, d, y = base(idx, seed, head, tag, title, accent)
    y = text_block(d, 72, y + 4, body, F("Inter-Medium.otf", 38), MUTED, 936, 56)
    box(img, y, why_label, why, accent)
    finish(img, f"slide_{idx:02d}.png")


def share_slide(idx):
    img, d, y = base(idx, 804, "14%", "WHY IT MATTERS", "YMTC is in NAND's top three", CYAN)
    y = text_block(d, 72, y, "Share of NAND bits shipped, Q2 2026 (Counterpoint Research)",
                   F("Inter-Medium.otf", 32), MUTED, 936, 46) + 26
    for name, val, col in [("Samsung", 25, VIOLET), ("SK hynix", 22, CYAN), ("YMTC", 14, GOLD)]:
        d = ImageDraw.Draw(img)
        d.text((72 * S, (y + 40) * S), name, font=F("Inter-Bold.otf", 36), fill=WHITE, anchor="lm")
        x0, x1 = 290, 290 + int(600 * val / 25)
        rrect(img, (x0, y + 10, x1, y + 70), 14, fill=col)
        d = ImageDraw.Draw(img)
        d.text(((x1 + 20) * S, (y + 40) * S), f"{val}%", font=F("Inter-ExtraBold.otf", 40), fill=col, anchor="lm")
        y += 90
    box(img, y, "READ IT RIGHT",
        "By revenue, Counterpoint ranked YMTC fifth. YMTC has been on the US Entity List since December 2022.", CYAN)
    finish(img, f"slide_{idx:02d}.png")


def layer(img, x0, y0, x1, y1, col, label):
    rrect(img, (x0, y0, x1, y1), 14, fill=col, alpha=60, outline=col + (255,), width=3)
    d = ImageDraw.Draw(img)
    lines = label.split("\n")
    cy = (y0 + y1) / 2 - (len(lines) - 1) * 17
    for ln in lines:
        f = F("Inter-Bold.otf", 27)
        assert f.getlength(ln) / S <= (x1 - x0) - 16, ln
        center(d, (x0 + x1) / 2, cy, ln, f, WHITE)
        cy += 34


def diagram_slide(idx):
    img, d, y = base(idx, 805, "BOND", "HOW IT WORKS", "Build apart, then join", GOLD)
    y = text_block(d, 72, y - 4, "Flash needs a memory cell array plus CMOS circuits that control it.",
                   F("Inter-Medium.otf", 34), MUTED, 936, 48) + 22
    top = y
    d = ImageDraw.Draw(img)
    center(d, 288, top + 16, "CMOS UNDER ARRAY", F("Inter-Bold.otf", 28), MUTED)
    center(d, 792, top + 16, "BONDED WAFERS", F("Inter-Bold.otf", 28), GOLD)
    # left: one wafer, array built on top of the finished logic
    layer(img, 96, top + 56, 480, top + 196, CYAN, "Memory cell array\n(built second, with heat)")
    layer(img, 96, top + 204, 480, top + 314, VIOLET, "CMOS circuits\n(built first)")
    # right: two wafers
    layer(img, 600, top + 56, 984, top + 154, VIOLET, "CMOS wafer")
    layer(img, 600, top + 216, 984, top + 314, CYAN, "Cell array wafer")
    d = ImageDraw.Draw(img)
    for x in range(640, 960, 52):
        d.line([(x * S, (top + 154) * S), (x * S, (top + 216) * S)], fill=GOLD, width=6 * S)
        for yy in (top + 154, top + 216):
            d.ellipse([(x - 8) * S, (yy - 8) * S, (x + 8) * S, (yy + 8) * S], fill=GOLD)
    y = top + 332
    d = ImageDraw.Draw(img)
    center(d, 540, y + 6, "Simplified diagram, not to scale", F("Inter-Medium.otf", 24), MUTED)
    box(img, y + 20, "THE PAYOFF",
        "The array's high-temperature processing happens away from the CMOS, so each wafer can be tuned on its own.", GOLD)
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
content(2, 802, "XTACKING", "WHAT HAPPENED", "A reported cross-license for 3D NAND",
        "Nikkei Asia reports that Samsung and SK hynix agreed to cross-licensing deals covering parts of Xtacking, YMTC's wafer-bonding architecture. A cross-license lets companies use each other's patented technology.",
        "NOT CONFIRMED", "No company has confirmed a deal. Terms, patent lists and timelines are not disclosed.", CYAN)
content(3, 803, "12,000+", "KEY NUMBERS", "YMTC's patent pile",
        "YMTC says it has filed more than 12,000 patents worldwide. US records cited by Nikkei show 4,000+ US filings since 2018. YMTC unveiled Xtacking in 2018 and began mass production with it in 2019.",
        "READ IT RIGHT", "Filings are not the same as granted patents. An industry source told Nikkei the aim is to avoid patent disputes.", GOLD)
share_slide(4)
diagram_slide(5)
content(6, 806, "218", "BIGGER PICTURE", "Bonding is already spreading in flash",
        "Kioxia's 8th-generation BiCS FLASH, with 218 layers, builds its CMOS and cell array on separate wafers and bonds them. In Feb 2025, reports said Samsung would license a YMTC bonding patent for NAND with 400+ layers.",
        "WHY ENGINEERS CARE", "Layer count is not the only race. How the wafers are put together now matters too.", CYAN)
content(7, 807, "HEAT", "VLSI TERM", "What is a thermal budget?",
        "It is the limit on how much heat, over how much time, a chip can take during manufacturing before its devices degrade. Splitting logic and memory onto two wafers eases that conflict.",
        "THE TRADE-OFF", "Wafer bonding needs very precise alignment, and a good die can end up paired with a bad one.", GOLD)
cta(8)
print("ok")

import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 8
LABEL = "TSMC AI DESIGN KIT"
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
    traces(img, 128, 40)
    d = ImageDraw.Draw(img)
    f = F("Inter-Bold.otf", 30); t = "CHIP DESIGN  •  NOV 2026"
    rrect(img, (72, 150, 72 + f.getlength(t) / S + 56, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d = ImageDraw.Draw(img)
    d.text((100 * S, 164 * S), t, font=f, fill=CYAN)
    fh = F("Inter-ExtraBold.otf", 98)
    y = 262
    for line, col in [("TSMC wants", WHITE), ("AI agents to", WHITE), ("help build chips", CYAN)]:
        assert fh.getlength(line) / S <= 936, line
        d.text((72 * S, y * S), line, font=fh, fill=col)
        y += 112
    y = text_block(d, 72, y + 30, "Its new AI Design Kit gives design agents foundry know-how, starting with the A14 node.",
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


def card(img, x0, y0, x1, y1, col, lines, sizes):
    rrect(img, (x0, y0, x1, y1), 16, fill=col, alpha=52, outline=col + (255,), width=3)
    d = ImageDraw.Draw(img)
    total = sum(s + 12 for s in sizes) - 12
    cy = (y0 + y1) / 2 - total / 2
    for ln, s in zip(lines, sizes):
        f = F("Inter-Bold.otf" if s >= 28 else "Inter-Medium.otf", s)
        assert f.getlength(ln) / S <= (x1 - x0) - 24, ln
        center(d, (x0 + x1) / 2, cy + s / 2, ln, f, WHITE)
        cy += s + 12


def arrow(img, x, y0, y1):
    d = ImageDraw.Draw(img)
    d.line([(x * S, y0 * S), (x * S, (y1 - 10) * S)], fill=GOLD, width=6 * S)
    d.polygon([((x - 12) * S, (y1 - 14) * S), ((x + 12) * S, (y1 - 14) * S), (x * S, y1 * S)], fill=GOLD)


def flow_slide(idx):
    img, d, y = base(idx, 1283, "AGENTS", "HOW IT WORKS", "From prompt to layout flow", GOLD)
    top = y + 8
    card(img, 190, top, 890, top + 64, VIOLET, ["Engineer writes a plain-language prompt"], [28])
    arrow(img, 540, top + 66, top + 90)
    card(img, 190, top + 92, 890, top + 192, CYAN,
         ["EDA vendor AI agent", "+ ADK know-how, alongside the PDK"], [34, 26])
    arrow(img, 540, top + 194, top + 218)
    card(img, 190, top + 220, 890, top + 284, GOLD, ["A14 place-and-route reference flow"], [30])
    d = ImageDraw.Draw(img)
    y = text_block(d, 72, top + 302, "Reported examples: Cadence InnoStack and Synopsys Implementation Agent.",
                   F("Inter-Medium.otf", 30), MUTED, 936, 42)
    box(img, y - 8, "BIGGER JOBS",
        "An orchestrator agent can direct other agents on diagnostics, power grid and timing closure.", GOLD)
    finish(img, f"slide_{idx:02d}.png")


def numbers_slide(idx):
    img, d, y = base(idx, 1284, "FASTER?", "KEY NUMBERS", "TSMC's productivity claims", CYAN)
    y += 14
    for big, small, col in [("3–5x", "digital design productivity", CYAN), ("6x", "analog / RF design productivity (up to)", GOLD)]:
        rrect(img, (72, y, W - 72, y + 190), 28, fill=PANEL, alpha=235, outline=(48, 62, 118), width=2)
        d = ImageDraw.Draw(img)
        fb = F("Inter-ExtraBold.otf", 118)
        d.text((112 * S, (y + 95) * S), big, font=fb, fill=col, anchor="lm")
        x = 450
        lines = wrap(small, F("Inter-SemiBold.otf", 36), 500)
        ty = y + 95 - (len(lines) - 1) * 24
        for ln in lines:
            d.text((x * S, ty * S), ln, font=F("Inter-SemiBold.otf", 36), fill=WHITE, anchor="lm")
            ty += 48
        assert x + 500 <= W - 90
        y += 210
    box(img, y - 6, "READ IT RIGHT",
        "TSMC's own figures for its AI Design Kit effort, published in September 2026. No baseline was given.", CYAN)
    finish(img, f"slide_{idx:02d}.png")


def a14_slide(idx):
    img, d, y = base(idx, 1286, "A14", "THE TARGET NODE", "What A14 promises over N2", GOLD)
    y += 14
    for big, small, col in [("15%", "up to this much more speed at the same power", CYAN),
                            ("30%", "or up to this much less power at the same speed", GOLD),
                            ("20%+", "higher logic density", VIOLET)]:
        rrect(img, (72, y, W - 72, y + 128), 24, fill=PANEL, alpha=235, outline=(48, 62, 118), width=2)
        d = ImageDraw.Draw(img)
        fb = F("Inter-ExtraBold.otf", 82)
        assert fb.getlength(big) / S <= 270, big
        d.text((108 * S, (y + 64) * S), big, font=fb, fill=col, anchor="lm")
        lines = wrap(small, F("Inter-SemiBold.otf", 32), 540)
        ty = y + 64 - (len(lines) - 1) * 22
        for ln in lines:
            d.text((410 * S, ty * S), ln, font=F("Inter-SemiBold.otf", 32), fill=WHITE, anchor="lm")
            ty += 44
        y += 144
    box(img, y - 8, "TIMELINE",
        "TSMC announced A14 in April 2025, with production planned for 2028.", GOLD)
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
content(2, 1282, "ADK", "WHAT HAPPENED", "A closer look at TSMC's AI kit",
        "At its Europe OIP workshop in Munich, TSMC gave a closer look at the kit, Tom's Hardware reported on 27 November. It was first introduced in September. Early contents include metal pitches, standard cell heights, routing patterns and cell naming rules.",
        "NOT YET", "No availability date was reported, and TSMC has not released measured power, speed or area gains from the kit.", CYAN)
flow_slide(3)
numbers_slide(4)
content(5, 1285, "18 → 12", "WHY IT MATTERS", "Months: a schedule goal",
        "Some customers want to cut chip development from about 18 months to 12 months or less, according to TSMC's Aveek Sarkar, as reported by Tom's Hardware. AI agents are meant to help with the slow, repetitive work of physical implementation.",
        "KEEP IN MIND", "This is a goal, not a measured result. The kit does not cover chip architecture or logic design.", GOLD)
a14_slide(6)
content(7, 1287, "PDK", "VLSI TERM", "What is a process design kit?",
        "A PDK is the foundry's package of files for one process: design rules, device models and layout data that design tools need. TSMC's ADK adds a layer of technology know-how that AI agents can use.",
        "ADD-ON, NOT REPLACEMENT", "The ADK complements the PDK. Conventional EDA tools are still needed to design the chip.", CYAN)
cta(8)
print("ok")

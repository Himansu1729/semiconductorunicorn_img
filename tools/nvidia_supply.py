import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 8
LABEL = "NVIDIA SUPPLY CHAIN"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 41, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 470, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 17-18, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Nvidia is booking", F("Inter-ExtraBold.otf", 112), WHITE, 940, 110)
    y = text_block(d, 72, y, "the packaging line", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "Nvidia says it is expanding commitments with six suppliers, from chip packaging to substrates, to feed AI demand.",
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
content(2, 401, "NOV 17", "WHAT HAPPENED", "Nvidia widens its supplier deals",
        "In a Nov 17, 2026 release, Nvidia said it is expanding commitments with Amkor, Foxconn, Kinsus, Samsung Electro-Mechanics, SPIL and TSMC to support the AI infrastructure build-out.",
        "WHY IT MATTERS", "AI chips are limited by packaging and substrates, not only by the wafers themselves.", CYAN)
content(3, 402, "~$3B", "KEY NUMBERS", "Amkor: nearly $3 billion",
        "Nvidia is backing Amkor's advanced-packaging expansion in Arizona and South Korea. Two multiyear agreements, from July and October 2026, total nearly $3 billion and include prepayments.",
        "READ IT RIGHT", "Figure is as described in Nvidia's own release.", GOLD)
content(4, 403, "3.5x", "KEY NUMBERS", "Kinsus: substrate capacity up 3.5x",
        "Kinsus plans to grow ABF substrate capacity dedicated to Nvidia by more than 3.5x at its Taoyuan, Taiwan campus. Production is expected to start in the second half of 2027, with the added capacity targeted for Q3 2028.",
        "WHY IT MATTERS", "Substrates are the base that connects a chip to the board. Slow ramps mean long lead times.", CYAN)
content(5, 404, "SPIL", "KEY NUMBERS", "SPIL: multibillion funding",
        "Nvidia is supporting a multiyear SPIL expansion in Taiwan, with new lines for bumping, interposer wafers, assembly and test. Press reports say contracted capacity for Nvidia triples by mid-2029.",
        "READ IT RIGHT", "The dollar amount was not disclosed. The 'triple' figure is press-reported.", GOLD)
content(6, 405, "ABF", "VLSI TERM", "Substrate and advanced packaging",
        "An ABF substrate is a layered board that routes signals and power between a chip package and the system board. Advanced packaging, like TSMC's CoWoS, places the GPU and memory side by side on an interposer.",
        "IN PLAIN WORDS", "The chip is the engine. The substrate and package are the wiring and mounts that make it usable.", CYAN)
content(7, 406, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) Whether the Kinsus and SPIL ramps hit their dates. 2) Amkor's Arizona expansion progress. 3) Rubin volumes: Nvidia says Vera Rubin NVL72 saw first volume shipments in Q3, using TSMC 5nm, 3nm and CoWoS.",
        "NOT ADVICE", "This summarizes company releases and press reports, not investment advice.", GOLD)
cta(8)
print("ok")

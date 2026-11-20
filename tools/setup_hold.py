import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 8
LABEL = "VLSI EXPLAINER"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 41, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 520, 214), 32, fill=GOLD, alpha=40, outline=GOLD + (255,), width=2)
    d.text((100 * S, 164 * S), "VLSI EXPLAINER", font=F("Inter-Bold.otf", 30), fill=GOLD)
    y = text_block(d, 72, 270, "Setup & hold:", F("Inter-ExtraBold.otf", 112), WHITE, 940, 110)
    y = text_block(d, 72, y, "two timing rules", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "Why a chip can fail at its target speed, and why one of the two rules cannot be fixed by slowing the clock.",
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
    y = text_block(d, 72, 570, "Get chip knowledge", F("Inter-ExtraBold.otf", 84), WHITE, 936, 96)
    y = text_block(d, 72, y, "every single day.", F("Inter-ExtraBold.otf", 84), CYAN, 936, 96)
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
content(2, 301, "FLOP", "THE BASICS", "What a flip-flop does",
        "A flip-flop is a 1-bit memory cell. On each tick (edge) of the clock it samples its input and holds that value until the next tick. Billions of them are chained through logic in a modern chip.",
        "IN PLAIN WORDS", "Like a camera shutter: it photographs the data at the instant the clock ticks.", CYAN)
content(3, 302, "SETUP", "RULE 1", "Data must arrive early",
        "Setup time is how long the input must already be stable BEFORE the clock edge. If the signal from the previous stage arrives too late, the flip-flop may capture the wrong value.",
        "THE FIX", "Shorten the logic path, upsize gates, or slow the clock down.", GOLD)
content(4, 303, "HOLD", "RULE 2", "Data must not leave too soon",
        "Hold time is how long the input must stay stable AFTER the clock edge. If the next value races through a very short path and arrives too early, it overwrites the one being captured.",
        "THE FIX", "Add delay buffers on the fast path. Slowing the clock does not help.", CYAN)
content(5, 304, "SPEED", "THE BIG DIFFERENCE", "One depends on clock speed",
        "A setup violation limits how FAST the chip can run, so a slower clock can rescue it. A hold violation does not depend on the clock period, so the chip can fail at any frequency.",
        "WHY ENGINEERS FEAR IT", "Hold bugs found after fabrication are very costly to fix.", GOLD)
content(6, 305, "MATH", "SETUP CHECK", "The setup budget",
        "The clock period must cover three delays: the flip-flop's clock-to-output delay, the logic delay, and the setup time (plus clock skew). Example: a 1 GHz clock gives a 1 ns period, which is 1,000 ps.",
        "ILLUSTRATIVE", "All three delays must fit inside that one period, on every path.", CYAN)
content(7, 306, "STA", "VLSI TERM", "Static timing analysis",
        "STA is the signoff step that checks the setup and hold rules on every path in the design, across process, voltage and temperature corners, without running simulations of input patterns.",
        "IN PLAIN WORDS", "A tool that checks every timing path, so no single path is missed.", GOLD)
cta(8)
print('ok')

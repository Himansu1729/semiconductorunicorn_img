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
    y = text_block(d, 72, 270, "RTL to GDSII:", F("Inter-ExtraBold.otf", 112), WHITE, 940, 110)
    y = text_block(d, 72, y, "how a chip is made", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "The digital chip design flow in 6 steps, from code you write to the file the foundry manufactures.",
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
content(2, 401, "RTL", "STEP 1", "Describe the chip in code",
        "Designers write RTL (register-transfer level) in a hardware language like Verilog or VHDL. It states what registers hold and how data moves between them each clock cycle, without drawing a single gate.",
        "IN PLAIN WORDS", "RTL is the chip's behaviour written as code, before any gates exist.", CYAN)
content(3, 402, "SYNTH", "STEP 2", "Turn code into gates",
        "Logic synthesis maps the RTL onto a library of standard cells (NAND gates, flip-flops and so on) from the foundry's process. The result is a gate-level netlist: a list of cells and how they connect.",
        "VLSI TERM", "A netlist is the chip as a wiring list of gates, still with no physical location.", GOLD)
content(4, 403, "PLACE", "STEP 3", "Floorplan and place cells",
        "Floorplanning sets the chip's outline and positions big blocks like memories. Placement then puts every standard cell into rows on the die, trying to keep connected cells close to cut wire length and delay.",
        "WHY IT MATTERS", "Short wires mean faster, lower power chips, so placement quality drives performance.", CYAN)
content(5, 404, "CLOCK", "STEP 4", "Deliver the clock evenly",
        "Clock tree synthesis builds a network of buffers that sends the clock to every flip-flop at nearly the same moment. The leftover difference in arrival time is called clock skew.",
        "LINK TO TIMING", "Skew changes the setup and hold budgets, so CTS comes before final timing fixes.", GOLD)
content(6, 405, "ROUTE", "STEP 5", "Connect it with metal wires",
        "Routing draws the real wires on the many metal layers stacked above the transistors, joining layers with vias. It must obey the foundry's spacing rules while avoiding shorts and congestion.",
        "IN PLAIN WORDS", "Like laying out a city's roads on many levels without any two crossing by mistake.", CYAN)
content(7, 406, "SIGNOFF", "STEP 6", "Check, then tape out",
        "Signoff runs static timing analysis, DRC (design rule check) and LVS (layout versus schematic) to prove the layout is fast enough, manufacturable and equal to the netlist. Then the GDSII layout file goes to the foundry: tape-out.",
        "VLSI TERM", "GDSII is the standard file format holding the chip's final layout geometry.", GOLD)
cta(8)
print('ok')

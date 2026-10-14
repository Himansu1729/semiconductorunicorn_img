import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 8
LABEL = "ASML Q3 2026"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 14, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 400, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 14, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "ASML's", F("Inter-ExtraBold.otf", 128), WHITE, 940, 136)
    y = text_block(d, 72, y, "record quarter", F("Inter-ExtraBold.otf", 118), CYAN, 940, 128)
    text_block(d, 72, y + 24, "The EUV maker reports €11.7B in sales and says some customers want to order for 2029–2030.",
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
content(2, 31, "Oct 14", "WHAT HAPPENED", "ASML posted a record quarter",
        "ASML, maker of EUV lithography machines, posted a record Q3. Net income was €5.0B.",
        "WHY IT MATTERS", "ASML's tools sit upstream of almost every advanced chip, so its results track chip-making investment.", CYAN,
        stat="€11.7B", stat_cap="total net sales in Q3 2026")
content(3, 32, "57.5%", "GROSS MARGIN", "Margin topped its own guidance range",
        "ASML's gross margin was 57.5% against a guided range of 55–57%. Basic EPS was €12.95 and net income was €4.96B (€4,960M).",
        "READ IT RIGHT", "Gross margin is the share of sales left after the direct cost of making and servicing the tools.", GOLD)
content(4, 33, "121", "SYSTEMS SOLD", "113 new and 8 used machines",
        "ASML sold 113 new and 8 used lithography systems in the quarter. Installed Base Management, its upgrades and service business, brought in €3.3B.",
        "KEY NUMBERS", "€11.7B sales · 57.5% gross margin · €5.0B net income · €3.3B installed-base sales.", CYAN)
content(5, 34, "€14–15B", "OUTLOOK", "Q4 and full-year guidance",
        "For Q4 2026 ASML guides total net sales of €14.2B to €15.2B at a gross margin near 57%. For the full year it expects €44B to €45B in sales and a gross margin near 56%.",
        "CONTEXT", "Guidance is a company forecast, not a result. Actual Q4 numbers come in January.", VIOLET)
content(6, 35, "2029", "DEMAND SIGNAL", "Customers asking to order for 2029–2030",
        "CEO Christophe Fouquet said some customers are interested in placing orders for 2029 and even 2030. Chipmakers are planning capacity years ahead.",
        "WHY IT MATTERS", "Long lead times for EUV tools mean fab expansions are decided long before chips ship.", GOLD)
content(7, 36, "EUV", "VLSI TERM", "EUV lithography, explained",
        "Extreme ultraviolet lithography uses 13.5 nm light to print the finest patterns on a wafer. ASML is the only company that makes these machines.",
        "WHY VLSI ENGINEERS CARE", "Litho limits shape design rules, so tool capacity shapes which nodes get built.", VIOLET)
cta(8)
print("ok")

import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "NAND PRICE OUTLOOK"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 41, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 470, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 19, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "NAND prices are", F("Inter-ExtraBold.otf", 112), WHITE, 940, 110)
    y = text_block(d, 72, y, "set to turn down", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "TrendForce expects 2027 flash memory prices to fall as Chinese cloud firms cut orders and new supply arrives.",
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
content(2, 501, "NOV 19", "WHAT HAPPENED", "TrendForce sees NAND turning down",
        "In a Nov 19, 2026 release, TrendForce said NAND Flash prices are set to decline in 2027, as order cuts by Chinese cloud providers outweigh demand growth from North American ones.",
        "WHY IT MATTERS", "NAND is the flash memory inside SSDs, phones and data-center storage. Its price cycle moves device costs.", CYAN)
content(3, 502, "0-5%", "KEY NUMBERS", "1Q27: contract prices dip",
        "TrendForce forecasts NAND contract prices to fall 0-5% quarter over quarter in 1Q27. All product categories enter a downward cycle from 2Q27, and declines may widen through the year.",
        "READ IT RIGHT", "This is an analyst forecast, not a measured price.", GOLD)
content(4, 503, "8-13%", "KEY NUMBERS", "4Q26 still up, but less",
        "TrendForce trimmed its 4Q26 contract price rise forecast to 8-13%. It also notes spot prices recently corrected by more than 20%.",
        "WHY IT MATTERS", "Spot prices move first. Contract prices tend to follow a quarter or so later.", CYAN)
content(5, 504, "25-30%", "KEY NUMBERS", "More supply is coming",
        "TrendForce expects NAND bit supply to grow 25-30% year over year in 2027, with industry capex up 26.7% to $29.9 billion.",
        "READ IT RIGHT", "More bits plus softer orders is the classic recipe for falling prices.", GOLD)
content(6, 505, "CSP", "THE CAUSE", "Chinese cloud orders shrink",
        "Chinese cloud service providers cut 2027 enterprise SSD orders by more than the added demand from US cloud firms, who raised their forecasts again. In consumer devices, brands are trimming storage specs.",
        "READ IT RIGHT", "TrendForce gave no figure for the size of the China cut.", GOLD)
content(7, 506, "BITS", "VLSI TERM", "Bit supply and contract price",
        "Bit supply is the total number of storage bits the industry makes; stacking more layers or adding wafers raises it. A contract price is the negotiated rate for a quarter, unlike a one-off spot price.",
        "IN PLAIN WORDS", "More bits on the shelf and fewer buyers means sellers must cut prices.", CYAN)
content(8, 507, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) How fast Chinese cloud firms burn down inventory. 2) US limits on GPU sales and remote cloud access. 3) Whether 1Q27 contract prices land inside the 0-5% decline range.",
        "NOT ADVICE", "This summarizes a TrendForce release and press coverage, not investment advice.", GOLD)
cta(9)
print("ok")

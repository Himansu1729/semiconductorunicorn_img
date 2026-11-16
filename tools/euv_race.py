import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "EUV CAPACITY RACE"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 500, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "NOV 7 – 16, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Chipmakers race", F("Inter-ExtraBold.otf", 112), WHITE, 940, 110)
    y = text_block(d, 72, y, "for EUV tools", F("Inter-ExtraBold.otf", 112), CYAN, 940, 122)
    text_block(d, 72, y + 24, "ASML says its 2027-28 supply will fall short of demand, and memory giants are reportedly lining up orders.",
               F("Inter-Medium.otf", 40), MUTED, 900, 56)
    chip_graphic(img, 540, 1060, 290)
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
content(2, 81, "2027-28", "ASML WARNING", "Planned supply falls short",
        "In its Q3 2026 release, ASML said its currently planned 2027 and 2028 supply will not fully meet customer demand. Some customers want to order for 2029 and 2030.",
        "WHY IT MATTERS", "EUV scanners are the machines that print a chip's finest patterns. Without them, fabs can't grow.", CYAN)
content(3, 82, "+30%", "ASML CAPACITY PLAN", "More capacity, and maybe more",
        "ASML plans a 30% capacity increase in 2027 for low-NA EUV and DUV immersion, is studying another 30% for 2028, and is looking at going beyond that.",
        "READ IT RIGHT", "These are plans, not delivered tools. Capacity takes years to build.", GOLD)
content(4, 83, "44 > 65", "EUV SHIPMENTS", "EUV shipments are climbing",
        "ASML shipped 44 low-NA EUV systems in 2025 and said on its Q3 call it expects about 65 in 2026. Demand is tied to the scale and length of AI investment.",
        "WHY IT MATTERS", "Even a 50% jump in shipments may not be enough for 2027 and 2028.", CYAN)
content(5, 84, "REPORTED", "SAMSUNG AND SK HYNIX", "Memory giants weigh earlier orders",
        "Korean media report Samsung and SK hynix are considering moving up EUV orders because lead times are lengthening. Reports cite 10-20 trillion won each; not confirmed by the companies.",
        "READ IT RIGHT", "These come from industry sources. Treat the amounts as reports, not announcements.", GOLD)
content(6, 85, "11.95T", "SK HYNIX ORDER", "A disclosed order already exists",
        "SK hynix disclosed in March an EUV purchase of about 11.95 trillion won (roughly US$8B), with delivery due by Dec 31, 2027. It plans EUV on 5+ layers of its 1c DRAM, per TrendForce.",
        "WHY IT MATTERS", "More EUV layers per DRAM chip means each chip uses more scanner time.", CYAN)
content(7, 86, "VLSI TERM", "EUV LITHOGRAPHY", "What is EUV?",
        "Extreme ultraviolet lithography uses 13.5 nm light to print the tiniest chip features. Every extra EUV layer on a wafer means another pass through a scanner.",
        "IN PLAIN WORDS", "Think of it as a super-precise projector that draws circuit patterns onto the wafer.", GOLD)
content(8, 87, "WATCH", "WHAT'S NEXT", "Three things to watch",
        "1) Whether Samsung and SK hynix confirm new EUV orders. 2) ASML's capacity update beyond 2027. 3) Samsung's Pyeongtaek P5 fab, targeted for 2028.",
        "NOT ADVICE", "This summarizes company statements and press reports, not investment advice.", CYAN)
cta(9)
print("ok")

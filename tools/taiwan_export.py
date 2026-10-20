import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "TAIWAN x AI CHIP EXPORTS"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 19, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 560, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 20, 2026 · PLANNED", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "Taiwan's next move:", F("Inter-ExtraBold.otf", 104), WHITE, 940, 116)
    y = text_block(d, 72, y, "criminalize AI chip smuggling", F("Inter-ExtraBold.otf", 104), CYAN, 940, 116)
    text_block(d, 72, y + 24, "Economy Minister Kung Ming-hsin says unauthorized AI chip exports to China would become a crime.",
               F("Inter-Medium.otf", 40), MUTED, 900, 56)
    chip_graphic(img, 540, 1095, 220)
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
content(2, 61, "Crime", "THE PLAN", "Taiwan plans to criminalize AI chip smuggling",
        "Economy Minister Kung Ming-hsin told Bloomberg (reported Oct 16) that Taiwan plans to make unauthorized exports of AI servers and advanced chips to China a criminal offense.",
        "READ IT RIGHT", "It is still a plan. No timeline, penalties or effective date have been announced.", CYAN)
content(3, 62, "Law", "HOW IT WORKS", "AI servers join the controlled list",
        "Reports say the change would amend Taiwan's Foreign Trade Act, adding AI servers and advanced semiconductors to the controlled-items list. One report notes Taiwan has had no direct criminal penalty for this kind of export.",
        "READ IT RIGHT", "Details come from press reports of the minister's interview, not from final legal text.", GOLD)
content(4, 63, "Wider", "WHO IS COVERED", "From named companies to all buyers?",
        "Taiwan's rules have reportedly named specific Chinese firms such as Huawei and SMIC. Sources say controls may widen to cover all relevant customers in China.",
        "WHAT WE DON'T KNOW", "That wider scope is still under evaluation, not confirmed.", CYAN)
content(5, 64, "US deal", "THE CONTEXT", "Aligned with US controls",
        "Kung said some measures will correspond with US ones, citing commitments in the 2026 US-Taiwan reciprocal trade agreement. Reports say AI servers with Nvidia chips have flowed from Taiwan to China.",
        "READ IT RIGHT", "Taiwan is a major hub for assembling AI servers, so its rules matter.", GOLD)
content(6, 65, "VLSI", "TERM OF THE DAY", "What is an AI accelerator?",
        "An AI accelerator is a chip built to do the huge amounts of matrix math behind AI training and inference quickly. GPUs are the best-known kind, and AI servers pack many of them together.",
        "PLAIN LANGUAGE", "Think of it as a chip specialised for AI math, not for general computing.", CYAN)
content(7, 66, "Why", "WHY IT MATTERS", "Export rules shape chip supply chains",
        "Rules on where advanced chips and servers can ship affect how companies plan product lines, assembly sites and customers. Engineers in design, packaging and supply chain work increasingly need to track them.",
        "FOR ENGINEERS", "Chip design does not happen in a vacuum: policy decides who can buy what.", GOLD)
content(8, 67, "Next", "WHAT TO WATCH", "The details are the next step",
        "Watch for draft legislation, the penalties it sets, an effective date, and whether controls widen from named firms to all Chinese buyers.",
        "NOTE", "Based on Bloomberg's report as relayed by other outlets. Not legal or investment advice.", CYAN)
cta(9)
print("ok")

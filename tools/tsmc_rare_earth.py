import sys; sys.path.insert(0, ".")
import design_helpers as dh
from design_helpers import *
dh.TOTAL = 9
LABEL = "TSMC RARE-EARTH MOTORS"

def cover():
    img = gradient()
    glow(img, 900, 160, 380, VIOLET, 80); glow(img, 120, 1200, 420, CYAN, 55)
    traces(img, 15, 40)
    d = ImageDraw.Draw(img)
    rrect(img, (72, 150, 410, 214), 32, fill=CYAN, alpha=40, outline=CYAN + (255,), width=2)
    d.text((100 * S, 164 * S), "OCT 22, 2026", font=F("Inter-Bold.otf", 30), fill=CYAN)
    y = text_block(d, 72, 270, "TSMC wants motors", F("Inter-ExtraBold.otf", 84), WHITE, 940, 136)
    y = text_block(d, 72, y, "without rare earths", F("Inter-ExtraBold.otf", 92), CYAN, 940, 128)
    text_block(d, 72, y + 24, "Reuters reports TSMC is asking equipment suppliers about alternatives to China-sourced magnets.",
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
content(2, 61, "Oct 22", "WHAT HAPPENED", "TSMC is sounding out its suppliers",
        "Reuters reported, citing three industry executives, that TSMC has asked equipment suppliers whether factory automation gear can use motors that need no rare-earth magnets.",
        "UNCONFIRMED", "TSMC has not publicly detailed the effort, and no cost or timeline has been disclosed.", CYAN)
content(3, 62, "90%+", "CHINA'S ROLE", "Processing is the bottleneck",
        "IEA figures cited in coverage put China at over 90% of rare-earth refining and about 94-95% of permanent-magnet making. Its share of mining is lower, roughly 60-70% by source.",
        "READ IT RIGHT", "The hard part is not digging rare earths up; it is refining them and making magnets.", GOLD)
content(4, 63, "2025", "EXPORT CONTROLS", "Licences now gate some magnets",
        "From April 2025 China requires export licences for certain medium and heavy rare earths and magnets containing them, such as those with terbium or dysprosium. It is not a blanket ban.",
        "WHY IT MATTERS", "A licence step adds uncertainty for any buyer that depends on those magnets.", CYAN)
content(5, 64, "Motors", "THE ENGINEERING", "What could replace the magnets?",
        "Options cited include induction, switched-reluctance and ferrite-magnet motors. Each can change efficiency, size, power density, precision and control.",
        "WHY ENGINEERS CARE", "Fab automation needs precise, repeatable motion, so any swap needs careful testing.", GOLD)
content(6, 65, "VLSI", "TERM OF THE DAY", "What is a permanent-magnet motor?",
        "Its rotor holds fixed magnets, often neodymium-based with dysprosium or terbium added. Strong magnets let a motor be compact, efficient and precise.",
        "PLAIN LANGUAGE", "Rare-earth-free designs skip those magnets, which can change size or efficiency.", CYAN)
content(7, 66, "ITRI", "TAIWAN'S RESPONSE", "Taiwan backs a pilot line",
        "In February, Economy Minister Kung Ming-hsin said the government would support ITRI in building a rare-earth pilot line within three years, aiming at about 50% of local demand.",
        "CONTEXT", "Reuters says the US is also working with Taiwan on alternative supply sources.", GOLD)
content(8, 67, "Next", "WHAT TO WATCH", "Open questions",
        "Watch for supplier or TSMC confirmation, which tools are affected, cost and timing, and any change in China's licence rules. Reuters did not establish a current shortage.",
        "NOTE", "Based on unnamed-source reporting. Educational summary, not investment advice.", CYAN)
cta(9)
print("ok")

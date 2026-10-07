from design_helpers import *

img = gradient()
glow(img, 880, 260, 380, GOLD, 55)
glow(img, 140, 1180, 420, CYAN, 55)
traces(img, 5, 34)
d = ImageDraw.Draw(img)

d.text((72 * S, 64 * S), "SEMICONDUCTOR FACT OF THE DAY", font=F("Inter-SemiBold.otf", 24), fill=MUTED)
d.line([(72 * S, 112 * S), ((W - 72) * S, 112 * S)], fill=(40, 52, 96), width=2)

f_tag = F("Inter-Bold.otf", 28)
tag = "TSMC · January 2026"
tw = f_tag.getlength(tag) / S
rrect(img, (72, 170, 72 + tw + 56, 224), 27, fill=CYAN, alpha=36, outline=CYAN + (255,), width=2)
d = ImageDraw.Draw(img)
d.text((100 * S, 181 * S), tag, font=f_tag, fill=CYAN)

d.text((72 * S, 270 * S), "NT$401B", font=F("Inter-ExtraBold.otf", 188), fill=GOLD)
y = text_block(d, 72, 540, "TSMC's revenue in one month, a company record.",
               F("Inter-ExtraBold.otf", 62), WHITE, 936, 74)
y = text_block(d, 72, y + 18,
               "It was up 36.8% year over year and the first time monthly revenue topped NT$400 billion (about US$12.7B).",
               F("Inter-Medium.otf", 38), MUTED, 936, 56)

top = max(y + 40, 900)
rrect(img, (72, top, W - 72, top + 200), 28, fill=PANEL, alpha=235, outline=(48, 62, 118), width=2)
rrect(img, (72, top, 84, top + 200), 6, fill=CYAN)
d = ImageDraw.Draw(img)
d.text((112 * S, (top + 28) * S), "WHAT'S NEXT", font=F("Inter-Bold.otf", 26), fill=CYAN)
text_block(d, 112, top + 72, "TSMC publishes its September sales tomorrow, Oct 8.",
           F("Inter-SemiBold.otf", 36), WHITE, 850, 50)

d.text((72 * S, (H - 150) * S), "Follow for a new chip fact every day", font=F("Inter-SemiBold.otf", 30), fill=MUTED)
d.text((72 * S, (H - 100) * S), HANDLE, font=F("Inter-ExtraBold.otf", 40), fill=WHITE)
finish(img, "fact_tsmc_record.png")
print("ok")

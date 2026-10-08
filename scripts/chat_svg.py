#!/usr/bin/env python3
"""Generate the chat-bubble SVG figures of Part 1, section 3.

User turns: right-aligned bubbles outlined in the primary accent.
Assistant turns: left-aligned bubbles filled with the secondary accent.
Line breaks are fixed here, so the figures render the same in every browser.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLE = re.search(r"  <style>.*?</style>", (ROOT / "assets/svg-template.svg").read_text(), re.S).group(0)
MARKS = "  <style>.mark-ok { fill: #2E8B57; } .mark-bad { fill: #C0392B; }</style>"

FONT, LINE, PAD_X, PAD_Y, GAP, CHAR_W = 20, 27, 18, 13, 14, 10.6


def bubble_h(lines):
    return len(lines) * LINE + 2 * PAD_Y


def mark(cx, cy, ok):
    if ok == "na":
        return (f'  <circle class="text-secondary" cx="{cx}" cy="{cy}" r="16"/>\n'
                f'  <text class="text-on-accent" x="{cx}" y="{cy + 7}" text-anchor="middle" font-family="sans-serif" '
                f'font-size="21" font-weight="700">?</text>\n')
    if ok:
        glyph = f'<path d="M{cx-7},{cy} L{cx-2},{cy+6} L{cx+8},{cy-6}" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
    else:
        glyph = (f'<path d="M{cx-6},{cy-6} L{cx+6},{cy+6} M{cx+6},{cy-6} L{cx-6},{cy+6}" '
                 'fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round"/>')
    cls = "mark-ok" if ok else "mark-bad"
    return f'  <circle class="{cls}" cx="{cx}" cy="{cy}" r="16"/>\n  {glyph}\n'


def chat(x0, width, y0, turns):
    """turns: list of (role, [lines], mark) with role 'user'|'assistant', mark True/False/None."""
    out, y = "", y0
    centers = []
    for role, lines, ok in turns:
        w = max(len(l) for l in lines) * CHAR_W + 2 * PAD_X
        h = bubble_h(lines)
        if role == "user":
            x = x0 + width - w
            out += f'  <rect class="bg-surface stroke-primary" x="{x:.0f}" y="{y}" width="{w:.0f}" height="{h}" rx="14" stroke-width="2"/>\n'
            tc = "text-primary"
        else:
            x = x0
            out += f'  <rect class="accent-secondary" x="{x}" y="{y}" width="{w:.0f}" height="{h}" rx="14"/>\n'
            tc = "text-on-accent"
        for i, l in enumerate(lines):
            out += (f'  <text class="{tc}" x="{x + PAD_X:.0f}" y="{y + PAD_Y + 20 + i * LINE}" '
                    f'font-family="sans-serif" font-size="{FONT}">{l}</text>\n')
        if ok is not None:
            out += mark(round(x + w + 30), round(y + h / 2), ok)
        centers.append((x, w, y + h / 2))
        y += h + GAP
    chat.centers = centers
    return out, y - GAP


def svg(path, view_w, view_h, label, body, marks=False):
    head = f'<svg viewBox="0 0 {view_w} {view_h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">\n{STYLE}\n'
    if marks:
        head += MARKS + "\n"
    (ROOT / "assets" / path).write_text(head + body + "</svg>\n")


# Every chat figure is drawn on a canvas FIG_W units wide, the width of the text
# column (1152px) at the shared bubble scale, so bubbles render at the same size
# on every slide. Canvas heights fit the content exactly: the figure is centered
# vertically in its slot, with equal space above and below.
FIG_W = 1477
INSET = (FIG_W - 1150) // 2  # chats occupy the central 1150 units


def two_chats(path, label, left, right):
    a, ha = chat(INSET, 540, 2, left)
    b, hb = chat(INSET + 610, 540, 2, right)
    svg(path, FIG_W, max(ha, hb) + 2, label, a + b, marks=True)


CHAT_X = (FIG_W - 1150) // 2 + 10  # left column of a chat-plus-panel figure
PANEL_X, PANEL_W = CHAT_X + 600, 540


def single_chat(path, label, turns):
    body, h = chat((FIG_W - 560) // 2, 560, 2, turns)
    svg(path, FIG_W, h + 2, label, body, marks=True)


def chat_and_panel(path, label, turns, panel, panel_h):
    """A short chat on the left, a panel (the real source) on the right, centered vertically."""
    ch, h = chat(CHAT_X, 540, 0, turns)
    H = max(h, panel_h) + 4
    body = f'  <g transform="translate(0,{(H - h) / 2:.0f})">\n{ch}  </g>\n'
    body += f'  <g transform="translate(0,{(H - panel_h) / 2:.0f})">\n{panel}  </g>\n'
    svg(path, FIG_W, H, label, body, marks=True)


single_chat("chat-hallucination.svg",
            "A chat: Cite an airline injury case. Varghese v. China Southern Airlines, 2019 (invented). "
            "Is it a real case? Yes. It is on Westlaw (invented).",
            [("user", ["Cite an airline injury case."], None),
             ("assistant", ["Varghese v. China Southern", "Airlines (2019)."], False),
             ("user", ["Is it a real case?"], None),
             ("assistant", ["Yes. It is on Westlaw."], False)])

# Not a knowledge base: the order status lives in a database table.
ROWS, RH, TOP = [("#48211", "Delivered", "Oct 2"), ("#48212", "Shipped", "Oct 3"),
                 ("#48213", "Delayed", "Oct 4"), ("#48214", "Preparing", "Oct 5")], 46, 40
cols = [PANEL_X + 22, PANEL_X + 190, PANEL_X + 400]
t = (f'  <text class="text-primary" x="{PANEL_X}" y="24" font-family="sans-serif" font-size="22" font-weight="700">Orders database</text>\n'
     f'  <rect class="bg-muted" x="{PANEL_X}" y="{TOP}" width="{PANEL_W}" height="{RH}" rx="10"/>\n')
for x, head in zip(cols, ["Order", "Status", "Updated"]):
    t += f'  <text class="text-secondary" x="{x}" y="{TOP + 30}" font-family="sans-serif" font-size="19" font-weight="700">{head}</text>\n'
for i, row in enumerate(ROWS):
    y = TOP + RH * (i + 1)
    hit = row[0] == "#48213"
    if hit:
        t += f'  <rect class="bg-surface stroke-strong" x="{PANEL_X}" y="{y + 3}" width="{PANEL_W}" height="{RH - 6}" rx="8" stroke-width="2.5"/>\n'
    else:
        t += f'  <line class="stroke-subtle" x1="{PANEL_X}" y1="{y + RH}" x2="{PANEL_X + PANEL_W}" y2="{y + RH}" stroke-width="1.5"/>\n'
    for x, cell in zip(cols, row):
        w = ' font-weight="700"' if hit else ''
        t += f'  <text class="text-primary" x="{x}" y="{y + 30}" font-family="sans-serif" font-size="20"{w}>{cell}</text>\n'
chat_and_panel("chat-orders.svg",
               "A chat: Where is my order #48213? It shipped on October 3. It arrives tomorrow (invented). "
               "Next to it, the orders database: order #48213 is Delayed, updated Oct 4.",
               [("user", ["Where is my order #48213?"], None),
                ("assistant", ["It shipped on October 3.", "It arrives tomorrow."], False)],
               t, TOP + RH * 5)

# Live data: the departures board.
B_ROWS, BH, BTOP = [("17:58", "Marseille", "On time"), ("18:04", "Lyon", "Delayed 25 min"),
                    ("18:12", "Dijon", "On time"), ("18:20", "Grenoble", "On time")], 46, 62
bcols = [PANEL_X + 24, PANEL_X + 120, PANEL_X + 330]
board = (f'  <rect class="text-primary" x="{PANEL_X}" y="0" width="{PANEL_W}" height="{BTOP + BH * 4 + 14}" rx="14"/>\n'
         f'  <text class="accent-tertiary" x="{PANEL_X + 24}" y="40" font-family="monospace" font-size="22" font-weight="700">DEPARTURES</text>\n')
for i, (tm, dest, st) in enumerate(B_ROWS):
    y = BTOP + BH * i + 32
    c = "accent-tertiary" if st != "On time" else "text-on-accent"
    w = ' font-weight="700"' if st != "On time" else ''
    for x, cell, cls in zip(bcols, (tm, dest, st), ("text-on-accent", "text-on-accent", c)):
        board += f'  <text class="{cls}" x="{x}" y="{y}" font-family="monospace" font-size="21"{w}>{cell}</text>\n'
chat_and_panel("chat-train.svg",
               "A chat: Is my 18:04 train to Lyon on time? Yes, it leaves on time (wrong). "
               "Next to it, a live departures board: 18:04 Lyon, Delayed 25 min.",
               [("user", ["Is my 18:04 train to Lyon on time?"], None),
                ("assistant", ["Yes, it leaves on time."], False)],
               board, BTOP + BH * 4 + 14)

# Knowledge cutoff: the timeline, with one inline exchange under each event.
CW = FIG_W
CUT, LY = CW // 2, 102
EV1, EV2 = CUT - CW // 4, CUT + CW // 4


def inline_row(x, y, question, answer, ok, wq, wa):
    """Question bubble, answer bubble and mark on one row, starting at x."""
    h = bubble_h([question])
    out = (f'  <rect class="bg-surface stroke-primary" x="{x:.0f}" y="{y}" width="{wq:.0f}" height="{h}" rx="14" stroke-width="2"/>\n'
           f'  <text class="text-primary" x="{x + PAD_X:.0f}" y="{y + PAD_Y + 20}" font-family="sans-serif" font-size="{FONT}">{question}</text>\n')
    xa = x + wq + 12
    out += (f'  <rect class="accent-secondary" x="{xa:.0f}" y="{y}" width="{wa:.0f}" height="{h}" rx="14"/>\n'
            f'  <text class="text-on-accent" x="{xa + PAD_X:.0f}" y="{y + PAD_Y + 20}" font-family="sans-serif" font-size="{FONT}">{answer}</text>\n')
    return out + mark(round(xa + wa + 30), round(y + h / 2), ok)


# Both rows get the same bubble widths and mirror each other around the cutoff.
ROWS = [("Where were the 2024 Olympics?", "Paris.", True), ("Who won the 2026 World Cup?", "Argentina.", False)]
WQ = max(len(q) for q, _, _ in ROWS) * CHAR_W + 2 * PAD_X
WA = max(len(a) for _, a, _ in ROWS) * CHAR_W + 2 * PAD_X
ROW_W, ROW_GAP = WQ + 12 + WA + 14 + 32, 70


body = f'''  <line class="stroke-primary" x1="14" y1="{LY}" x2="{CUT}" y2="{LY}" stroke-width="12" stroke-linecap="round"/>
  <line class="stroke-subtle" x1="{CUT}" y1="{LY}" x2="{CW - 40}" y2="{LY}" stroke-width="12"/>
  <polygon class="bg-muted" points="{CW - 40},{LY - 18} {CW - 4},{LY} {CW - 40},{LY + 18}"/>
  <line class="stroke-strong" x1="{CUT}" y1="{LY - 64}" x2="{CUT}" y2="{LY + 64}" stroke-width="3"/>
  <text class="text-primary" x="{CUT}" y="{LY - 80}" text-anchor="middle" font-family="sans-serif" font-size="24" font-weight="700">Knowledge cutoff</text>
  <circle class="accent-primary" cx="{EV1}" cy="{LY}" r="18"/>
  <text class="text-primary" x="{EV1}" y="{LY - 40}" text-anchor="middle" font-family="sans-serif" font-size="24" font-weight="700">Paris Olympics, 2024</text>
  <circle class="bg-surface stroke-strong" cx="{EV2}" cy="{LY}" r="18" stroke-width="3"/>
  <text class="text-primary" x="{EV2}" y="{LY + 8}" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="700">?</text>
  <text class="text-primary" x="{EV2}" y="{LY - 40}" text-anchor="middle" font-family="sans-serif" font-size="24" font-weight="700">World Cup final, July 2026</text>
'''
body += inline_row(CUT - ROW_GAP - ROW_W, LY + 80, *ROWS[0], WQ, WA)
body += inline_row(CUT + ROW_GAP, LY + 80, *ROWS[1], WQ, WA)
svg("knowledge-cutoff.svg", CW, LY + 80 + bubble_h(["x"]) + 2,
    "Timeline: the Paris Olympics of 2024 sit before the knowledge cutoff; the World Cup final of July 2026 sits "
    "after it. Under the Olympics: Where were the 2024 Olympics? Paris (right). Under the World Cup: Who won the 2026 "
    "World Cup? Argentina (wrong: Argentina won the 2022 final).", body, marks=True)


# Context window: a frame holding a short conversation, then room left.
W, H = 560, 470
body = (f'  <text class="text-primary" x="{W/2:.0f}" y="24" text-anchor="middle" font-family="sans-serif" '
        f'font-size="22" font-weight="700">Context window</text>\n'
        f'  <rect class="bg-surface stroke-strong" x="2" y="40" width="{W-4}" height="{H-42}" rx="16" stroke-width="2.5"/>\n')
turns, end = chat(22, W - 44, 60, [
    ("user", ["What is the capital of France?"], None),
    ("assistant", ["Paris."], None),
    ("user", ["What should I visit there first?"], None),
    ("assistant", ["The Louvre. Book ahead", "to see the Mona Lisa."], None)])
room_y = end + 18
body += turns + (f'  <rect class="stroke-subtle" x="22" y="{room_y}" width="{W-44}" height="{H-20-room_y}" rx="12" '
                 f'fill="none" stroke-width="2" stroke-dasharray="8 6"/>\n'
                 f'  <text class="text-secondary" x="{W/2:.0f}" y="{(room_y + H - 20)/2 + 7:.0f}" text-anchor="middle" '
                 f'font-family="sans-serif" font-size="20">Room left</text>\n')
svg("context-window.svg", W, H,
    "Context window: a frame holding a conversation (What is the capital of France? Paris. What should I visit "
    "there first? The Louvre. Book ahead to see the Mona Lisa.), then room left", body)
# A chatbot cannot leave the conversation: the chat in a closed frame, cut links
# to what it cannot fetch (left, pointing in) and cannot act on (right, pointing out).
VW, VH, FW = FIG_W, 289, 490
FX = (VW - FW) // 2
OUT_L, OUT_R = INSET, VW - INSET - 230
body = (f'  <rect class="bg-surface stroke-strong" x="{FX}" y="2" width="{FW}" height="{VH - 4}" rx="16" stroke-width="2.5"/>\n')
turns, end = chat(FX + 20, FW - 40, 18, [
    ("user", ["Is my 18:04 train on time?"], None),
    ("assistant", ["I can’t see live train times."], None),
    ("user", ["Then email my team I’ll be late."], None),
    ("assistant", ["I can’t send emails. Here’s a draft."], None)])
body += turns


def outside(x, cy, text):
    return (f'  <rect class="bg-muted" x="{x}" y="{cy - 32}" width="230" height="64" rx="12"/>\n'
            f'  <text class="text-primary" x="{x + 115}" y="{cy + 7}" text-anchor="middle" font-family="sans-serif" '
            f'font-size="21">{text}</text>\n')


def cut_link(x1, x2, cy):
    """A link from x1 to x2 (arrowhead at x2), cut in the middle."""
    mid, gap = (x1 + x2) / 2, 9
    d = 1 if x2 > x1 else -1
    a, b = mid - d * gap, mid + d * gap
    return (f'  <line class="stroke-subtle" x1="{x1}" y1="{cy}" x2="{a}" y2="{cy}" stroke-width="3"/>\n'
            f'  <line class="stroke-subtle" x1="{b}" y1="{cy}" x2="{x2 - d * 12}" y2="{cy}" stroke-width="3"/>\n'
            f'  <line class="stroke-strong" x1="{a}" y1="{cy - 11}" x2="{a}" y2="{cy + 11}" stroke-width="3"/>\n'
            f'  <line class="stroke-strong" x1="{b}" y1="{cy - 11}" x2="{b}" y2="{cy + 11}" stroke-width="3"/>\n'
            f'  <polygon class="bg-muted" points="{x2},{cy} {x2 - d * 14},{cy - 9} {x2 - d * 14},{cy + 9}"/>\n')


for cy, left in [(50, "Web search"), (145, "Orders database"), (240, "Live train times")]:
    body += outside(OUT_L, cy, left) + cut_link(OUT_L + 236, FX - 6, cy)
for cy, right in [(95, "Send an email"), (195, "Save a file")]:
    body += outside(OUT_R, cy, right) + cut_link(FX + FW + 6, OUT_R - 6, cy)
svg("chat-closed.svg", VW, VH,
    "A chat in a closed frame: Is my 18:04 train on time? I can't see live train times. Then email my team I'll be late. "
    "I can't send emails. Here's a draft. Outside the frame, cut links: the weather service and your mailbox on the "
    "left (web search, orders database, live train times), pointing in; send an email and save a file on the right, pointing out.", body)
print("ok")

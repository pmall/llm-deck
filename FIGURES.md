# Figures still to create

Most diagrams in the deck are built from HTML/CSS components (`styles/base.css` §7), so only genuine illustrations remain as `.figure-ph` placeholders. Build each per `AGENTS.md` §6; size the `viewBox` from `uv run python scripts/export.py boxes`.

| Slide | Title | Brief |
|---|---|---|
| 24 | Context rot: the long-conversation trade-off | Quality-vs-conversation-length slope. A "still fine" zone on the left, a "start a new chat" zone on the right. No numbers on the axes. |
| 45 | The metric that moves: how long a task can run | Task duration (seconds → minutes → hours → days, log-like scale) rising over time, one labelled point per milestone from the timeline slide. |

Optional upgrades, if a CSS version feels too plain: the shoggoth-with-a-smiley-face meme (slide 16), the AlphaGo move-37 board (slide 17), and the orchestrator/worker swarm (slide 43).

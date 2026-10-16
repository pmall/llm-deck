# Oral notes

Speaker notes kept off the slides (formerly the "Lore" lines). Slide numbers as of 2026-10-13 (they shift); the title identifies the slide if numbers shift.

## Slide 4 — Intelligence as compression
- Claude is widely assumed to be named after Claude Shannon, who founded information theory.

## Slide 5 — LLM as a lossy zip file of human knowledge
- Ted Chiang, The New Yorker (2023): “ChatGPT is a blurry JPEG of the web”.

## Slide 6 — Attention: some words weigh more than others
- The core idea, said out loud: storing every sentence ever written could never fit in a 1 TB zip file; what fits is the relationships between words, which hold in every sentence. Each word takes its meaning from the words around it.
- “Attention Is All You Need” (2017) introduced the Transformer, the “T” in GPT.
- “You shall know a word by the company it keeps.” (J. R. Firth, linguist, 1957)
- Ask the room to guess each blank before revealing it: they predict from what they understand. Training (slide 8) goes the other way round: the LLM learns to understand by predicting.

## Slide 13 — Judge the document, not the mechanism
- “Stochastic parrots” (Bender et al., 2021) is the best-known version of the worry.

## Slide 14 — Emergent property: the LLM picks up patterns
- “Language Models are Few-Shot Learners”, the GPT-3 paper (2020).

## Slide 16 — Instruction tuning: from autocomplete to assistant
- ChatGPT (30 Nov 2022) was a GPT-3.5 model tuned on conversations like these.

## Slide 18 — The context window: a hard limit on the conversation
- Claude Opus 4.6 was asked to list every spell in the first four Harry Potter books (about 733K tokens). It found 49 of the 50.

## Slide 20 — Hallucination: fluent text, no fact behind it
- In 2023, lawyers filed a brief citing this case and five others invented by ChatGPT (Mata v. Avianca).

## Slide 22 — Human feedback: people’s picks replace the answer key
- April 2025: OpenAI rolled back a ChatGPT update that flattered users far too much.

## Slide 23 — Reasoning: the LLM writes its thinking before the answer
- DeepSeek-R1 (Jan 2025) learned to reason this way in the open. It shook the industry and the stock market.

## Slide 33 — Tool calling: the answer can be an instruction
- Function calling (2023), then MCP (Nov 2024): a common plug for tools.

## Slide 34 — The ReAct loop: the Part 1 chatbot, with one rule changed
- ReAct (Yao et al., 2022): reason + act, interleaved.

## Slide 38 — A filesystem is a memory you can teach
- AGENTS.md / CLAUDE.md files; “Claude plays Pokémon” kept notes to carry on. This deck was built the same way.

## Slide 42 — Seeing: images enter the loop
- This very deck is checked that way: render each slide to an image, look, fix.

## Slide 46 — Self-verification: check the result against the goal
- AutoGPT (2023) made the loop go viral, before LLMs were reliable enough to check their own work.

## Slide 47 — Software engineering: the ideal sandbox
- SWE-bench (2023) turned “fix a real GitHub issue” into the benchmark; “vibe coding” (Karpathy, Feb 2025) named the practice.

## Slide 48 — Computer use: when there is no API
- Anthropic computer use (Oct 2024), OpenAI Operator (Jan 2025).

## Slide 50 — The metric that moves: how long a task can run
- METR (2025): the task length at 50% success doubles roughly every seven months.

## Slide 51 — Orchestration: many agents, clean contexts
- Anthropic’s multi-agent research system (2025): lead agent plus parallel sub-agents.

## Slide 60 — Spelling: an LLM does not see letters
- In 2024, chatbots kept saying “strawberry” has 2 r’s. It became a meme.
## From removed slides
- Tokens: in 2024, chatbots claiming that “strawberry” has two r’s became a meme (“strawberry” is cut into tokens such as st / raw / berry, so the letters are hidden).

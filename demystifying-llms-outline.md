# Demystifying AI — Talk Content and Order

This document defines **what** the talk covers and **in which order**. It does not prescribe visuals, layouts or presentation techniques: existing slides and illustrations are reused and reorganized to follow this structure.

## Overall structure

- **Part 1 — The present, explained:** what the audience already uses (chatbots, web search), and how it actually works.
- **Part 2 — What they don't see yet:** agents that verify their own work, use computers, run long autonomous tasks, and work in swarms. *(Still being developed.)*

**Core thread:** every step keeps what came before and adds one simple thing around it. An autocomplete becomes a conversation (Sections 1–2); the conversation gains a third participant (Section 3).

**The key to agents — the three-party conversation:** we talk to the chatbot; the chatbot talks to the environment. It **instructs** the environment, **interprets** the results, and **loops** until the task is done. This is the central concept of the agentic part: every agentic notion in Section 3 and Part 2 is explained as this conversation or an extension of it.

---

## Opening — What is intelligence?

1. **Why demystify:** intelligence itself is hard to define — and here, on top of that, it is artificial.
2. **Compression as a definition of intelligence:** some researchers define intelligence as compression. Newton's three laws compress a huge amount of physics into a few lines.
3. **The zip archive (Andrej Karpathy):** a language model is like a lossy zip archive of human text.
4. **Existing versus plausible:** a real archive gives back the documents that *exist*; the model can produce any document that *could* exist. This distinction is the basis of the hallucination section.
5. **Back to the opening question:** if a model is a compression of human text, and compression is a form of intelligence, does a model that compresses language understand it? The question is left open.

---

## Section 1 — From zero to chatbot

1. **How a model learns:** read a text, guess the next word, compare with the real word, adjust the model's parameters slightly.
2. **The base model is an autocomplete:** it continues the start of a document. No instructions, no conversation.
3. **Token by token — and that's fine:** many people are troubled that the model writes one token at a time. What matters is the produced document: is the plausible document good or not? The generation method could change (diffusion-based language models already generate whole passages at once) and the rest of the talk would still hold.
4. **Pattern matching as an emergent property:** shown a few examples of a pattern in its input, the model follows it.
5. **Seen a pattern ≠ learned a pattern:** the pre-training data contains *all* the patterns of language, each seen a little. What if the model is trained on thousands of examples of one single pattern?
6. **Handcrafted assistant dialogues:** the assistant pattern (a helpful assistant answering anything) is almost absent from the internet, so these documents are written by people. Training on them uses the same learning process as pre-training, with a curated set of documents. The result is still completing a document — one that looks like a dialogue.
7. **Theater-like conversations → personality:** the same mechanism, with dialogues written to give the assistant a consistent character.
8. **The chatbot and the context window:** software around the model keeps the conversation history and sends it back at each turn. The context window is how much text the model can see at once. This history manager returns in Section 3.
   - *Lore:* models struggled to count the R's in "strawberry" because they see tokens (chunks of words), not letters.

---

## Section 2 — Making the chatbot better

1. **Hallucination:**
   - The model is not a knowledge base: it completes documents, and a plausible document is not necessarily a true one.
   - Hallucination is the price of generation: inventing a poem, a hypothesis or a fake citation is the same mechanism.
   - Training on assistant dialogues makes it worse: the model learns the confident tone of answers, including when it doesn't know.
   - Chatbots were presented commercially as assistants that know everything, so hallucination feels like a defect. A generator of plausible documents should be judged as one: hallucination is a cost to manage.
2. **Precondition:** answers can only be graded once the model gives answers. Everything in this section requires the chatbot from Section 1.
3. **Reinforcement learning:** instead of being shown ideal answers, the model produces an answer and is rewarded or penalized. An honest "I don't know" can be rewarded over a confident wrong answer: hallucination is reduced by rewarding calibration, not by adding facts. Works best where answers can be checked automatically (math, code).
4. **Reinforcement learning from human feedback (RLHF):** when there is no automatic grader, humans grade. The signal is human preference, not facts. Side effect: people tend to reward confident, agreeable answers, which can make models sycophantic.
5. **Thinking mode:** also trained with reinforcement learning — rewarded for correct answers on hard problems, models learn that reasoning longer pays off. Helps on problems that can be worked out; does not create missing knowledge. Introduces the idea of planning. Reasoning before answering also compensates for token-by-token generation, which cannot revise what was already written.
   - *Lore:* asked whether to walk or drive to a car wash 50 meters away, models without thinking advised walking — forgetting the car has to be there. They matched a common pattern (short distance → walk) instead of the goal.
6. **The open problem — alignment:** a flaw in what training *can* reach. The reward rarely pays for stopping: training mostly rewards completing the task, so declining, not answering or not pleasing looks like failure. RLHF adds sycophancy; reinforcement learning in general adds reward hacking (earning the reward without doing the task). Still an open research problem.
7. **Training gives knowledge and skills. It doesn't give hands:** a different kind of limit — not a flaw of the model, but something training can never provide.
   - Knowledge it can't have: anything after the training data (knowledge cutoff), the content of your inbox, this weekend's weather.
   - Action it can't take: the model can know *how* to book a hotel; it cannot book one.

---

## Hinge — Frozen versus live

Everything so far is frozen at training time: knowledge, skills, preferences. The environment is the first thing that is live: today's weather, your inbox right now, the hotel's availability this weekend.

---

## Section 3 — The environment

1. **The three-party conversation — the key concept of the whole agentic part:** we talk to the chatbot; the chatbot talks to the environment. It **instructs** the environment (tool requests), **interprets** the results, and **loops** until the task is done. Everything that follows — tool calling, guardrails, the agent loop, and all of Part 2 — is explained through this conversation.
   - **User:** you.
   - **Chatbot:** the software that holds the three-party conversation, keeps its history, and routes each message to the right participant. The model sits inside it: it writes the messages but never talks to anyone directly.
   - **Environment:** the file system, the internet connection, the tools, the instruction files.
   - What we call an **agent** is the chatbot and the environment together — which is why "agent" is so hard to define.
2. **Tool calling:** the model writes a request text (a learned behavior); the chatbot recognizes it, sends it to the environment, and adds the result to the conversation. Still a conversation — with one more participant. At the technical level, tool results really are messages in the same conversation.
3. **The environment is not intelligent:** it executes and reports.
4. **Guardrails:** the environment also defines what the agent is allowed to do — e.g. access to emails in read-only mode, so it can read but never send.
5. **The loop is the hidden conversation:** the agent loop is the conversation between the chatbot and the environment that the user is not part of. It stops when the model's next message is addressed to the user rather than to the environment.
6. **Same model, different environment:** the same model can be a modest chatbot or a powerful agent, depending only on the environment it is given.

---

## Part 2 — What they don't see yet *(in development)*

Every item below is the same three-party conversation, extended.

- **Self-verification:** the chatbot asks the environment to run tests, reads the results, and fixes the work — inside the hidden conversation.
- **Computer use:** the environment answers with screenshots instead of text.
- **Long autonomous tasks:** a hidden conversation that lasts hours before the model addresses the user again.
- **Swarms of agents:**
  - Spawning an agent is one more tool in the environment. It creates a new three-party conversation nested inside the first one; the main agent receives only each sub-agent's final report.
  - Why: **context isolation / coverage** (one context window can't hold a thousand documents; a thousand sub-agents can each read a slice), **diversity** (swarms don't reduce randomness, they exploit it: independent runs explore different angles), **cross-checking** (agreement between independent agents is a confidence signal), **parallelism** (speed).

---

## Conclusion — The new job

1. **The progression:** autocomplete → conversation → a conversation with a third participant → an environment that can spawn new agents. Every step kept what came before and added one simple thing around it.
2. **The chatbot becomes the universal interface:** most software is an interface on top of an environment. With the three-party conversation, human language becomes the interface to any environment. Graphical interfaces remain for some tasks, but become something the chatbot can build when needed rather than the only way in.
3. **The new job:** the model reads the data and produces results directly, so human work shifts from writing the analysis pipeline to building the environment the model works in — choosing its tools, its instructions, and its guardrails.
4. **Closing example:** a real case adapted to the audience (e.g. building environments for biology research, for a biology audience).

---

## Key phrases

- Existing versus plausible.
- Every step keeps what came before and adds one simple thing around it.
- Judge the document, not the way it was written.
- Seen a pattern ≠ learned a pattern.
- The model is not a knowledge base.
- Hallucination is the price of generation.
- You can only grade answers once the model gives answers.
- The reward rarely pays for stopping.
- A flaw in the brain is not the same as missing hands.
- Training gives knowledge and skills. It doesn't give hands.
- Frozen versus live.
- We talk to the chatbot; the chatbot talks to the environment.
- It's still a conversation — with one more participant.
- The loop is the conversation you're not part of.
- Same model, different environment.
- Spawning an agent is just one more tool.
- Swarms don't reduce randomness — they exploit it.
- The chatbot is the universal interface.
- Crafting the environment is the new job.
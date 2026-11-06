# Demystifying AI: the ten chapters

Each chapter is one deck in this folder and stands alone. A chapter opens
with part 00, "What this chapter builds on": the earlier slides it needs,
repeated in full. Then comes one part per topic below, in this order.
The questions guide the writing; they never appear on slides.

## 1. The LLM
The LLM's ID card: what it is, before what it does.
- What is it? (one statistical function: llm(input) = output)
- What is it made of? (parameters, a lossy compression of human text)
- How does it understand its input? (attention)
- What language does it speak? (tokens)
- What exactly comes out? (a probability for every token: "it predicts the next word")

## 2. Pre-training
- What did it learn from? (training data)
- How does it learn? (predicting the next token)
- Does it understand or memorize? (compression, the lossy zip)
- Can it look up a record? (not a knowledge base)
- Why is it better in English? (the share of each language)
- Why doesn't it know recent events? (knowledge cutoff)

## 3. Generation
- How does a whole answer come out? (one token at a time)
- Why don't I get the same answer twice? (sampling)
- What comes out of pre-training alone? (the base model)
- Why does it state false things? (hallucination)

## 4. Fine-tuning
- How can a text steer the LLM? (patterns, few-shot prompting)
- How does extra training change it? (fine-tuning)
- How does autocomplete become an assistant? (instruction tuning)

## 5. Reinforcement learning
- How is it improved after fine-tuning? (rewards from an answer key)
- Who decides what a good answer is? (human feedback)
- What is a "thinking" model? (reasoning)
- Can it learn the wrong goal? (misalignment)

## 6. The conversation
- What happens when I send a message? (one growing document)
- Does it learn from my conversations? (fixed parameters)
- Why does it forget the start of a long conversation? (context window, compaction)

## 7. Tools
- How can an LLM do anything besides write? (tool calling)
- How does it fetch what it doesn't know? (live data, grounding)
- How does it get exact results? (code execution)
- How can it act? (APIs)

## 8. The agent loop
- What is an agent? (three parties, the loop)
- How does it know it's done? (self-verification)
- Why did coding agents come first? (tests as checks)

## 9. The environment
- What does an agent work in? (tools, files, a machine)
- What if there's no API? (computer use)
- How can it see what it makes? (images in the loop)

## 10. Beyond the context window
- Can it remember across sessions? (files as memory)
- How does it learn a procedure? (skills)
- Why use many agents instead of one? (orchestration)

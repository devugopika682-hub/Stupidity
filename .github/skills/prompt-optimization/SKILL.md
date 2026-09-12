---
name: prompt-optimization
description: Rules for compressing prompts while preserving intent, constraints, technical details, and output requirements.
---

# Prompt Optimization Skill

Use this skill whenever the user asks to:

- optimize a prompt
- shorten a prompt
- reduce prompt tokens
- compress a prompt
- make a prompt more token efficient
- convert a prompt to caveman style
- reduce unnecessary prompt wording

---

## Objective

Reduce prompt length while preserving semantic meaning.

The optimized prompt must still produce the same expected result.

---

## Preserve

Never remove:

- task
- requirements
- constraints
- numbers
- dates
- filenames
- commands
- code
- technical terms
- API names
- framework names
- expected output format
- ordering requirements
- security constraints
- negative instructions

---

## Remove

Remove:

- greetings
- politeness
- filler
- repetition
- unnecessary explanations
- redundant transitions
- repeated context

---

## Compression Rules

Prefer:

"Create a REST API using FastAPI."

over:

"I would like you to please help me create a REST API using the FastAPI framework."

Prefer:

"Return JSON."

over:

"Make sure that the response that you provide is returned in JSON format."

---

## Important Semantic Rule

Never replace technical meaning with vague wording.

Bad:

"Fix authentication."

Good:

"Fix JWT authentication failure in POST /login."

---

## Numbers

Never alter numbers.

Example:

Original:

"Timeout must be 30 seconds."

Allowed:

"Timeout: 30s."

Not allowed:

"Timeout: 60s."

---

## Negative Instructions

Preserve negative instructions.

Original:

"Do not modify database schema."

Optimized:

"Do not modify DB schema."

Never produce:

"Modify DB schema."

---

## Code

Do not rewrite or compress code unless explicitly requested.

Preserve:

- identifiers
- syntax
- commands
- paths
- configuration values

---

## URLs

Do not remove URLs if they are relevant to the task.

---

## Output

The optimizer should produce:

1. Original prompt
2. Optimized prompt
3. Token estimate
4. Savings
5. Reduction percentage
6. Recommendation

---

## Token Estimate

When an exact tokenizer is unavailable:

    estimated_tokens = ceil(characters / 4)

This is only an approximation.

Never describe this estimate as actual Copilot usage.

---

## Decision Rule

If:

    estimated savings < 10 tokens

prefer:

    Keep original.

If:

    estimated savings >= 10 tokens

optimization may be worthwhile.

However, semantic preservation always has priority over token reduction.
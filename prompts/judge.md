You are grading a proposal that was supposed to transfer a mechanism from a randomly chosen foreign field into a STEM problem. Grade strictly; most proposals decorate rather than transfer.

## Problem

{problem}

## Foreign seed that was supposed to be used

{seed_name} — {seed_path}

## Proposal

{proposal}

## Rubric

**transfer_depth** (0–4):
- 0 none — seed ignored, or mentioned and dropped
- 1 vocabulary — the home field's standard answer wearing the seed's words
- 2 metaphor — an "it's like X" framing with no concrete step that follows from it
- 3 mechanism — a specific causal mechanism from the seed is mapped to a specific element of the problem, correspondences stated
- 4 method — a procedure (with its maths/algorithm where applicable) transferred and adapted so that it could actually be run

**usefulness** (0–4): would a competent practitioner in the problem's field actually try this next? 0 = no, it's wrong or empty; 2 = plausible but they'd have thought of it anyway; 4 = yes, and it is not something the field's standard toolkit would have produced.

**home_field_default** (true/false): could the home field have produced essentially this proposal without the seed?

Respond with JSON only:
{{"transfer_depth": <int>, "usefulness": <int>, "home_field_default": <bool>, "mechanism_named": "<the seed mechanism actually used, or null>", "justification": "<two sentences>"}}

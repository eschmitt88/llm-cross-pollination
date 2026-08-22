---
source_url: https://www.science.org/doi/10.1126/sciadv.adn5290
fetched_via: "Europe PMC full-text XML (open access, CC-BY) — https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11244532/fullTextXML — the publisher page (science.org) and the PMC HTML/PDF viewer both blocked automated fetch (403 / proof-of-work JS challenge); Europe PMC's REST API serves the same CC-BY full text without that gate."
fetched: "2026-08-22"
title: "Generative AI enhances individual creativity but reduces the collective diversity of novel content"
authors: ["Anil R. Doshi", "Oliver P. Hauser"]
venue: "Science Advances 10, eadn5290 (2024)"
doi: "10.1126/sciadv.adn5290"
---

Full text below is the plain-text-stripped body of the JATS XML from Europe PMC
(figures/tables omitted, captions kept). This is the complete open-access
article (CC BY 4.0), not merely the abstract.

# Generative AI enhances individual creativity but reduces the collective diversity of novel content

Anil R. Doshi (UCL School of Management), Oliver P. Hauser (University of Exeter)

## Abstract

Creativity is core to being human. Generative artificial intelligence
(AI)—including powerful large language models (LLMs)—holds promise for
humans to be more creative by offering new ideas, or less creative by
anchoring on generative AI ideas. We study the causal impact of generative
AI ideas on the production of short stories in an online experiment where
some writers obtained story ideas from an LLM. We find that access to
generative AI ideas causes stories to be evaluated as more creative, better
written, and more enjoyable, especially among less creative writers.
However, generative AI–enabled stories are more similar to each other than
stories by humans alone. These results point to an increase in individual
creativity at the risk of losing collective novelty. This dynamic resembles
a social dilemma: With generative AI, writers are individually better off,
but collectively a narrower scope of novel content is produced.

## INTRODUCTION

[... see full body below ...]

## Body

INTRODUCTION Creativity is fundamental to innovation and human expression
through literature, art, and music. However, the emergence of generative
artificial intelligence (AI) technologies is challenging several
long-standing assumptions about the uniqueness and superiority of
human-generated content. [...] Creativity is typically assessed across two
dimensions: novelty and usefulness. [...] Novelty assesses the extent to
which an idea departs from the status quo or expectations. [...] Usefulness
reflects the practicality and relevance of an idea [...]

This paper aims to provide an initial answer to these questions through a
preregistered, two-phase experimental online study on written creative
output. In the first phase, N = 293 participants ("writers") wrote an
eight-sentence story, randomly assigned to Human-only, Human+1 GenAI idea,
or Human+5 GenAI ideas conditions. In generative AI conditions writers could
call GPT-4 with the prompt "Write a three-sentence summary of a story about
an adventure on the open seas" (topic varies). In the second phase, N = 600
"evaluators" rated 293 stories on novelty, usefulness, and emotional
characteristics, then were told whether/which condition the writer was in.

RESULTS. Baseline vs GenAI: GenAI assistance increases both novelty and
usefulness. Novelty: Human+1 idea +5.4% (b=0.207, P=0.021) vs Human-only;
Human+5 ideas +8.1% (b=0.311, P<0.001). Usefulness: Human+1 idea +3.7%
(b=0.185, P=0.039); Human+5 ideas +9.0% (b=0.453, P<0.001), and +5.1%
(P=0.0012) over Human+1. Writers' self-assessments show no significant
differences across conditions (self-assessment is not accurate).

Emotional characteristics: GenAI stories more enjoyable (+0.216/+0.375),
more plot twists (+0.384/+0.468), better written (+0.372, P<0.001, five-idea
condition), less boring (-0.200, P=0.049), not funnier.

Heterogeneity by inherent creativity (DAT — divergent association task,
cosine distance of 10 maximally-different word embeddings, scaled to 100;
mean 77.24, SD 6.48): high-DAT (inherently creative) writers show little
effect of GenAI access. Low-DAT writers show the largest gains: novelty
+6.3%/+10.7% (one/five ideas), usefulness +5.5%/+11.5%, "well written"
+26.6%, enjoyment +22.6%, boring -15.2% (five-idea condition). GenAI access
"equalizes" the creativity scores of low- and high-creativity writers — it
does not push the upper bound past what already-creative humans achieve on
their own.

Similarity of stories (the headline diversity result): using OpenAI
embeddings, cosine similarity (x100) of each story to the mean embedding of
all other stories in the same condition. GenAI access makes a story MORE
similar to other stories in its condition: Human+1 idea b=0.871, P<0.001;
Human+5 ideas b=0.718, P=0.003. Human-only similarity scores span a range of
8.10 points; the GenAI-condition increase is 10.7% and 8.9% of that whole
range. Stories are also measurably anchored to the GenAI idea itself: story
embeddings are 5.2% (b=4.29, P<0.001) / 5.0% (b=4.11, P<0.001) more similar
to the GenAI idea they were shown than Human-only stories are to a randomly
assigned GenAI idea from the same topic pool.

DISCUSSION. GenAI "professionalizes" stories — raises the floor, does not
raise the ceiling; benefits least-creative writers most, in line with prior
findings that GenAI helps lower performers more in other domains (customer
support, coding). Frames the diversity loss as a social dilemma /
tragedy-of-the-commons structure (individually rational to use GenAI ideas;
collectively erodes the pool of distinct content) — cites Hardin 1968
explicitly. Notes GPT-4 was used with a single fixed, uncustomized prompt
per idea request, no multi-turn interaction — argues this is likely a LOWER
BOUND on both the creativity uplift and the homogenization effect, since
more customized/interactive use could push both further.

MATERIALS AND METHODS. Prolific participants (UK, ≥95% approval). Story
prompt topics: "an adventure on the open seas" / "in the jungle" / "on a
different planet". Full instruction text: "We would like you to write a
story about an adventure on the open seas. You can write about anything you
like. The story must be exactly eight sentences long and it needs to be
written in English and appropriate for a teenage and young adult audience
(approximately 15 to 24 years of age)." GenAI idea-generation prompt passed
to GPT-4 API: "Write a three-sentence summary of a story about an adventure
on the open seas." (topic substituted). Participants could not copy-paste
the GenAI text (forces re-typing/paraphrase, not literal copy). 88.4% of
GenAI-condition participants requested at least one idea; five-idea
condition participants requested 2.55 ideas on average, 24.5% took the max
of five.

Outcome variables: novelty index = mean(novel, original, rare); usefulness
index = mean(appropriate, feasible, publishable); both on 9-point Likert,
Cronbach's alpha 0.92 / 0.89. Preregistered at AsPredicted.org (ID 136723).
Ethics: UCL School of Management + University of Exeter IRB.

Limitations acknowledged by authors: short fixed-length task (8 sentences),
single medium (text), no interactivity with the LLM, no prompt
customization — generalizability to longer / more open-ended / multi-turn
creative tasks is untested.

Data/code: https://doi.org/10.5061/dryad.qfttdz0pm

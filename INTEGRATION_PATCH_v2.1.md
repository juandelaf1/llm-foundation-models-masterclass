# INTEGRATION PATCH v2.1 — APPLY TO CURRENT AGENT WORK

## Purpose
This is a non-destructive patch for an agent that is ALREADY implementing the Masterclass project from the v2 package.

DO NOT restart the project.
DO NOT discard or regenerate existing artifacts unnecessarily.
DO NOT replace the canonical specification.
Merge this patch into the current implementation and update only the affected deliverables.

## Source of truth hierarchy
1. Existing canonical project specification already in the repository.
2. Existing RUN_OF_SHOW.md.
3. Existing MEDIA_PRESENTATION_GUIDE.md.
4. This patch, only where it adds execution/orchestration detail.
5. Existing implementation choices, unless they violate a rule above.

If a conflict is detected, preserve the existing implementation when it is compatible and report the conflict explicitly in the final implementation notes.

---

# 1. ADD A FORMAL LEARNING-FLOW LAYER

The project must not be treated as a collection of independent slides, videos, demos and notebooks.

The class is one continuous learning experience:

```text
QUESTION
   ↓
INTUITION
   ↓
EXPERIMENT
   ↓
OBSERVATION
   ↓
CONCEPT
   ↓
TRANSFER / DECISION
   ↓
NEXT QUESTION
```

Every class segment must define:
- question introduced;
- expected prior knowledge;
- conceptual move;
- experiment or visual support;
- expected observation;
- interpretation;
- transition question;
- next resource.

## Mandatory rule
Never open a demo, external website, video, notebook or RAG without first stating the question that resource is being used to investigate.

---

# 2. ADD / UPDATE THE INSTRUCTOR RUN OF SHOW

The existing RUN_OF_SHOW.md remains canonical, but the implementation must expose a machine-readable or clearly structured transition layer for the instructor.

For every segment include:

- `time_start`
- `time_end`
- `screen_or_resource`
- `learning_goal`
- `question_in`
- `instructor_action`
- `student_action`
- `observation_expected`
- `conceptual_takeaway`
- `transition_phrase`
- `question_out`
- `hands_off_to`
- `fallback`

The instructor must be able to teach the class without reconstructing the logic themselves.

---

# 3. PRESENTATION: ADD STORYBOARD METADATA

For each core slide, preserve or add:

- `slide_id`
- `title`
- `purpose`
- `question_in`
- `main_message`
- `visual`
- `speaker_note`
- `transition_phrase`
- `question_out`
- `enters_from`
- `hands_off_to`
- `demo_if_any`
- `fallback`

The slide deck is NOT the pedagogical source of truth. The storyboard/run-of-show is.

---

# 4. VIDEO AND GENERATIVE MEDIA

Generative AI for presentations and video is OPTIONAL production support.

It must NEVER become a runtime dependency for understanding the lesson.

## Allowed roles
- 20–40 second hook;
- short conceptual micro-animation;
- optional post-class recap.

## Forbidden roles
- sole explanation of a technical concept;
- information that cannot be recovered elsewhere;
- a video longer than the time budget reasonably allows;
- decorative AI-generated content with no learning function.

For every generated media asset, record:
- why it exists;
- which learning objective it supports;
- duration;
- fallback if unavailable.

---

# 5. DEMO ORCHESTRATION

The demos are not interruptions. Each one must be a direct answer to a question raised immediately before it.

## Tiktokenizer
Pre-demo question:
“What does the model actually receive?”

Post-demo observation:
“The input is segmented into tokens and tokenization is not identical to human word boundaries.”

Transition:
“Now we know what enters the model. What does it do with those representations?”

## BBycroft
Pre-demo question:
“Can we see how context changes internal representations?”

Post-demo observation:
“Context changes the computation/representation across the Transformer stack.”

Transition:
“If these mechanisms are shared conceptually, why are there different model families?”

## Projector
Optional extension only.
Use to deepen embeddings/representation understanding.
It must not be required to complete the 60-minute core lesson.

## Captum
Out of core scope.
Do not add it to the mandatory flow.

---

# 6. RAG INTEGRATION

The Learning RAG is part of the learning ecosystem, but it must not interrupt the core 60-minute flow unless the instructor explicitly chooses a short closing query.

Core role:
- post-class exploration;
- optional 2–3 minute closing demonstration;
- evidence-backed continuation of learning.

Mandatory RAG behaviours:
- answer from course-grounded sources;
- show supporting evidence or citations;
- distinguish stable concepts from volatile model information;
- abstain when evidence is insufficient;
- allow topic/model/source filtering;
- support learning, investigation, comparison and quiz modes.

The RAG must never silently invent a current model specification.

---

# 7. TIME BUDGET ENFORCEMENT

Hard maximum: 60 minutes.

Recommended core:
- Hook: 5
- Anatomy: 15
- Ecosystem: 7
- Experimentation: 10
- Challenge: 13
- Transfer + closure/RAG: 10

Total: 60.

All optional assets must be outside the core timing.

If a generated artifact makes the class exceed 60 minutes, the artifact must be shortened, removed from the core flow, or moved to optional material.

---

# 8. FINAL QA FOR THE ACTIVE PROJECT

Before declaring the project complete, run a pedagogical rehearsal in addition to technical tests.

The rehearsal must verify:

1. Every demo is introduced by a question.
2. Every demo ends with an observation.
3. Every observation produces the concept needed for the next segment.
4. Every transition has an explicit instructor phrase.
5. No resource is opened merely because it is available.
6. The 60-minute limit is realistic when spoken aloud and demonstrated.
7. The instructor can recover from any external demo failure using the specified fallback.
8. The deck, notebook, demo and RAG use the same terminology.
9. No concept is explained twice at materially different levels unless the repetition is deliberate.
10. The learner can follow the chain without needing to understand the instructor's internal project structure.

---

# 9. REQUIRED AGENT ACTION

Apply this patch to the project already in progress.

Do NOT regenerate everything.

Update only the following as needed:
- `docs/run-of-show.md`
- `docs/instructor-guide.md`
- `docs/media-presentation-guide.md`
- slide storyboard / speaker notes
- demo scripts or demo guides
- RAG closing integration notes
- QA / acceptance criteria

Then report:

- which existing files were modified;
- which files were left untouched;
- any conflicts found;
- confirmation that the core remains <= 60 minutes;
- confirmation that all transitions have entry/exit questions;
- confirmation that all demos have fallbacks.

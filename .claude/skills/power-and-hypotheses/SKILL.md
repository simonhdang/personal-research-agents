---
name: power-and-hypotheses
description: Plan sample sizes and statistical power for experiments, surveys and PLS-SEM models, and turn observations or theory into precise, testable hypotheses. Use when designing studies, writing preregistrations, or developing a hypothesis set.
---

# Power and hypotheses

## Power
- Experiments (t-test, ANOVA, interactions): use R `pwr` or simulation; for interactions and mixed designs prefer simulation (`simr`, or a custom simulation with a fixed seed).
- Mediation/moderation (PROCESS-type models): Monte Carlo power (e.g., Schoemann et al.'s approach) via simulation in R.
- PLS-SEM: inverse square root method and gamma-exponential method for minimum sample size; report both with the smallest expected path coefficient.
- Always state: effect size assumed and its source (prior study, pilot, smallest effect of interest), alpha, power target (usually .80 or .90), resulting n per cell and total, and attention-check attrition allowance.
- Detailed guidance: `references/statistical-power.md` and `references/statistical-power-refs/`.

## Hypotheses
- Follow `references/hypothesis-generation.md`: observation -> mechanism -> testable prediction.
- Each hypothesis: direction, variables as measured, boundary conditions, the theory that predicts it, and what result would falsify it.
- Check consistency with `vault/owner/research-profile.md` (theories the researcher builds on or avoids) and with `vault/reviews/lessons.md` (e.g., reviewers' past objections to mediation logic).

Output: `projects/<name>/analysis/plan.md` (power section, hypothesis table) and, when asked, a preregistration draft.

Sources: adapted from K-Dense scientific-agent-skills (MIT; see LICENSE.md).

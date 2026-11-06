---
name: pls-sem
description: Estimate, evaluate and report PLS-SEM models in R (seminr, cSEM, predictlearn), including measurement and structural assessment, mediation, moderation, PLSpredict, common method bias checks, and cross-checking SmartPLS exports. Use for any PLS-SEM or composite-based SEM analysis.
---

# PLS-SEM

All analyses run in R on the researcher's computer, in a Quarto report under `projects/<name>/analysis/`, with `set.seed()` and a RATIONALE line for each choice (core-methodology skill). Ask before installing packages (`seminr`, `cSEM`, `lavaan`, the researcher's `predictlearn`).

## 1. Specify
- Model and hypotheses from `projects/<name>/CLAUDE.md` and `analysis/plan.md`.
- Mode per construct (reflective Mode A vs formative Mode B) with a one-line justification.
- Sample-size check: inverse square root method (power-and-hypotheses skill).

```r
library(seminr); set.seed(20261106)
mm <- constructs(
  composite("ATT", multi_items("att", 1:4)),
  composite("SC",  multi_items("sc", 1:5)),
  composite("INT", multi_items("int", 1:3))
)
sm <- relationships(paths(from = c("SC", "ATT"), to = "INT"), paths(from = "SC", to = "ATT"))
fit  <- estimate_pls(data = df, measurement_model = mm, structural_model = sm)
boot <- bootstrap_model(fit, nboot = 10000, seed = 20261106)
s <- summary(fit); sb <- summary(boot)
```
(Check the installed seminr version's documentation if a function signature differs.)

## 2. Measurement model (reflective)
| Check | Threshold to report |
|---|---|
| Indicator loadings | >= .708 (.40-.70 kept only with justification) |
| Internal consistency | Cronbach's alpha, rho_A, composite reliability (.70-.95) |
| Convergent validity | AVE >= .50 |
| Discriminant validity | HTMT < .85 (or .90 for conceptually close constructs) with bootstrap CIs excluding 1; Fornell-Larcker as secondary |

Formative constructs: indicator VIF < 3, weight significance and relevance (outer loadings), redundancy analysis if a global item exists.

## 3. Structural model
- Collinearity: inner VIF < 3.
- Paths: bootstrap (10,000 resamples) coefficients, t, p, 95% percentile CIs.
- R-squared, f-squared; predictive power with PLSpredict (`predict_pls`, 10 folds, 10 reps): compare RMSE/MAE against the linear-model benchmark for the key target construct's indicators.
- Model fit (only if the journal expects it): SRMR via cSEM, with the caveat that fit is debated in PLS-SEM.
- The researcher's predictive procedure (Richter & Tudoran, 2024) via `predictlearn` when prediction is part of the contribution.

## 4. Extensions (as the model requires)
- **Mediation**: bootstrap specific indirect effects (`specific_effect_significance`), classify mediation type.
- **Moderation**: two-stage interaction term; simple slope plot.
- **Common method bias**: full collinearity VIFs (all < 3.3) plus a marker variable if one was measured; report procedural remedies from the design.
- **Endogeneity**: Gaussian copula test for non-normal predictors when the journal or lessons.md calls for it.
- **Groups**: MICOM then MGA; **IPMA** for managerial implications.
- **CB-SEM/CFA** (lavaan) when a covariance-based model is the better fit for the research question; explain why.

## 5. SmartPLS cross-check
When the researcher ran SmartPLS: read the exported Excel/HTML results, re-estimate the same model in seminr, and report differences. Point estimates should match to about .01; bootstrap SEs and p-values differ slightly by resampling. Flag anything larger.

## 6. Report
Tables: measurement model (loadings, alpha, rho_A, CR, AVE), HTMT matrix, structural results (beta, t, p, CI, f2, supported?), R2 and PLSpredict. Write them to `analysis/tables/` and a results summary that the results-report skill can turn into prose. After project close-out, reusable scripts go to `vault/knowledge/` (type: method).

# Core Methodology: Reference

Detailed reference material for the core-methodology skill.
See [SKILL.md](SKILL.md) for the overview and [examples.md](examples.md) for code templates.

---

## Common Mistakes

### Critical Severity

**Running analysis without input validation**
- Consequence: Silent failures producing wrong results that look valid
- Prevention: ALWAYS validate data types, ranges, and required columns first

**Transforming data without documentation**
- Consequence: Hidden researcher degrees of freedom, unreproducible results
- Prevention: Document every transformation with rationale

**Omitting data provenance documentation**
- Consequence: Cannot verify data authenticity, assess quality, detect preprocessing errors, or understand limitations. Hidden preprocessing steps can introduce bias that invalidates findings
- Prevention: ALWAYS document: data sources, collection methods, access dates, and any preprocessing done before analysis. Include file hashes for integrity verification

### High Severity

**Omitting software versions from reports**
- Consequence: Results cannot be reproduced when packages update
- Prevention: Always include sessionInfo() or equivalent

**Using magic numbers without explanation**
- Consequence: Future researchers don't understand choices
- Prevention: Define all constants with explanatory comments

**Reading CSV files without checking encoding**
- Consequence: Silent character corruption (accented characters become garbage), parsing failures, incorrect string comparisons, missing data from encoding errors
- Prevention: ALWAYS detect encoding before reading text files. Use chardet or charset-normalizer, try common encodings (utf-8, latin-1, cp1252) if detection uncertain, and document encoding used for reproducibility

### Medium Severity

**Not setting random seeds**
- Consequence: Results vary between runs
- Prevention: Set seeds for all stochastic operations

---

## Interpretation Guide

### Interpreting Results

- Statistical significance does not equal practical importance
- Effect sizes need context and units
- Confidence intervals show precision
- Multiple testing inflates Type I error

### Red Flags

- P-values just below 0.05 (possible p-hacking)
- Missing data patterns correlating with treatment
- Outliers driving results
- Assumptions clearly violated

### Next Steps

- All validations pass: Proceed with analysis
- Assumptions violated: Document and use robust methods
- Missing data substantial: Implement appropriate handling
- Results surprising: Check for errors and run sensitivity analyses

---

## References

- Simmons, J.P., Nelson, L.D. & Simonsohn, U. (2011). "False-Positive Psychology." *Psychological Science*. Researcher degrees of freedom.
- Gelman, A. & Loken, E. (2014). "The Statistical Crisis in Science." *American Scientist*. Garden of forking paths.
- Nosek, B.A. et al. (2015). "Estimating the reproducibility of psychological science." *Science*. Reproducibility crisis.
- Stodden, V., Seiler, J. & Ma, Z. (2016). "An empirical analysis of journal policy effectiveness for computational reproducibility." *PNAS*. Data provenance and reproducibility.

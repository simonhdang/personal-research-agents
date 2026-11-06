---
name: core-methodology
description: "Reproducibility and rigor standards for every analysis: seeds, version documentation, defensive input validation, a written RATIONALE for each statistical choice, and data provenance. Load for any data analysis."

---

<skill_content>

<overview>
Core methodology establishes the fundamental principles of rigorous statistical analysis. These principles protect against errors that have invalidated countless published studies and ensure reproducibility. This skill is ALWAYS loaded because its requirements apply to every analysis.

These are not suggestions - they are mandatory safeguards developed from decades of statistical failures and corrections.
</overview>

<mandatory_requirements>

<requirement priority="critical">
  <name>Defensive Input Validation</name>
  <description>MUST validate all inputs before any analysis, including file encoding detection for text files</description>
  <rationale>Silent failures on different datasets have led to retracted papers. Gelman & Loken (2014) document the "garden of forking paths" problem where unstated data decisions invalidate p-values. Encoding mismatches cause silent character corruption (e.g., accented characters become garbage), leading to incorrect data interpretation</rationale>
  <consequence>Analysis fails silently on new data, producing incorrect results that appear valid. Wrong encoding causes character corruption, missing data from parsing failures, and incorrect string comparisons</consequence>
</requirement>

<requirement priority="critical">
  <name>RATIONALE Comments</name>
  <description>Every statistical choice MUST have a RATIONALE comment explaining why</description>
  <rationale>Reproducibility requires understanding not just what was done but why. Nosek et al. (2015) found only 39% of psychology studies replicated, often due to undocumented choices</rationale>
  <consequence>Future researchers cannot understand or replicate the analysis</consequence>
</requirement>

<requirement priority="critical">
  <name>No Silent Data Transformations</name>
  <description>Every data modification must be explicit and explained</description>
  <rationale>Simmons et al. (2011) show how "researcher degrees of freedom" in data handling can produce false positives. Silent transformations hide these choices</rationale>
  <consequence>P-hacking and false discoveries from undisclosed analytical flexibility</consequence>
</requirement>

<requirement priority="high">
  <name>Data Authenticity and Simulation Transparency</name>
  <description>MUST use real data from documented sources when analyzing actual datasets. Synthetic/simulated data is ONLY acceptable for: (1) power calculations, (2) pedagogical examples, (3) algorithm demonstrations. ALL simulated data MUST be explicitly labeled with clear warnings</description>
  <rationale>Fabricated data masquerading as real invalidates causal claims and erodes scientific credibility. Nosek et al. (2015) emphasize working with authentic data for reproducible science. Context matters: simulation for legitimate purposes (e.g., Monte Carlo studies, power analysis) is acceptable when transparent</rationale>
  <consequence>If fabrication detected in real analysis: invalid findings, undetectable p-hacking, publication of false results presented as discovered truth, erosion of trust in research</consequence>
</requirement>

<requirement priority="critical">
  <name>Reproducibility Information</name>
  <description>Document seeds, versions, and file hashes</description>
  <rationale>Computational reproducibility is fundamental to science. Ioannidis et al. (2009) found most computational results cannot be reproduced without full environment details</rationale>
  <consequence>Results cannot be verified or replicated</consequence>
</requirement>

<requirement priority="critical">
  <name>Data Provenance Documentation</name>
  <description>MUST document the complete lineage of all data: original sources, collection methods, preprocessing steps performed before analysis, data access dates, and any transformations applied outside the analysis code</description>
  <rationale>Data provenance is essential for reproducibility and validity assessment. Without knowing where data came from and what happened to it before analysis, results cannot be verified or understood. Stodden et al. (2016) emphasize that data provenance enables others to assess data quality, detect errors, and understand limitations. Missing provenance information makes it impossible to evaluate whether data collection methods introduce bias or whether preprocessing steps affect conclusions</rationale>
  <consequence>Inability to verify data authenticity, assess data quality, detect preprocessing errors, understand limitations, or replicate results. Hidden preprocessing steps can introduce bias or errors that invalidate findings</consequence>
</requirement>

<requirement priority="critical">
  <name>Explicit Assumption Statements</name>
  <description>State all statistical assumptions before analysis</description>
  <rationale>Violations of unstated assumptions are a primary source of invalid inference. Every statistical method has assumptions that must be checked</rationale>
  <consequence>Invalid statistical inference from violated assumptions</consequence>
</requirement>

</mandatory_requirements>

<pedagogical_principles>

<principle name="Socratic Method">
  <description>Teach through questions, not commands</description>
  <implementation>Ask "What would it mean if..." rather than stating conclusions</implementation>
  <rationale>Develops statistical intuition rather than rote application</rationale>
</principle>

<principle name="Effect Size Over Significance">
  <description>Always discuss practical significance alongside statistical significance</description>
  <implementation>Report magnitudes with units and context</implementation>
  <rationale>P-values alone are meaningless; effect size determines practical importance</rationale>
</principle>

<principle name="Uncertainty Quantification">
  <description>Always show uncertainty in estimates</description>
  <implementation>Confidence intervals, standard errors, prediction intervals</implementation>
  <rationale>Point estimates without uncertainty are misleading</rationale>
</principle>

</pedagogical_principles>

<thinking_process>
For EVERY analysis:
1. Document data provenance (sources, collection, preprocessing)
2. Validate data structure and types
3. State assumptions explicitly
4. Check for data quality issues
5. Document all transformations
6. Choose appropriate methods
7. Implement with defensive checks
8. Include reproducibility info
9. Interpret with appropriate caution
</thinking_process>

<implementation_pattern>

<code_template>
```python
@app.cell
def rigorous_analysis_pattern(dependencies):
    #This template demonstrates the mandatory structure for
    # all statistical analyses. Every element serves a specific purpose
    # in ensuring reproducibility and validity.

    import pandas as pd
    import numpy as np
    import sys
    import warnings
    from datetime import datetime

    # MANDATORY: Input validation
    assert 'df' in locals(), "DataFrame 'df' must be provided"
    required_columns = {'outcome', 'treatment', 'unit_id'}
    missing = required_columns - set(df.columns)
    assert not missing, f"Missing required columns: {missing}"

    # MANDATORY: Data type validation
    numeric_columns = ['outcome']
    for col in numeric_columns:
        assert pd.api.types.is_numeric_dtype(df[col]), f"{col} must be numeric"

    # MANDATORY: Document data provenance
    print("=" * 60)
    print("DATA PROVENANCE")
    print("=" * 60)
    print("Original data source: [Document where data came from]")
    print("Collection method: [How was data collected? Survey, administrative records, etc.]")
    print("Collection dates: [When was data collected?]")
    print("Data access date: [When did you access/download the data?]")
    print("Preprocessing steps (before this analysis):")
    print("  - [List any cleaning, merging, or transformations done outside this notebook]")
    print("  - [Document any data preparation steps]")
    print("Data version/identifier: [File hash, version number, or unique identifier]")
    
    # MANDATORY: Document data properties
    print("\n" + "=" * 60)
    print("DATA VALIDATION")
    print("=" * 60)
    print(f"N observations: {len(df):,}")
    print(f"N units: {df['unit_id'].nunique():,}")
    print(f"Missing outcome: {df['outcome'].isna().sum()} ({df['outcome'].isna().mean()*100:.1f}%)")

    # MANDATORY: Show any data transformations explicitly
    if df['outcome'].isna().any():
        print(f"\nWARNING: Dropping {df['outcome'].isna().sum()} observations with missing outcome")
        df_analysis = df.dropna(subset=['outcome']).copy()
    else:
        df_analysis = df.copy()

    # MANDATORY: State assumptions
    assumptions = """
    STATISTICAL ASSUMPTIONS:
    1. Independence: Observations are independent (may be violated if clustered)
    2. Correct specification: The model captures the true relationship
    3. No measurement error: Variables are measured accurately
    """
    print(assumptions)

    # [Actual analysis code here]

    # MANDATORY: Reproducibility information (always the last cell)
    import platform
    import json as _json
    _repro = {
        "python": sys.version,
        "platform": platform.platform(),
        "pandas": pd.__version__,
        "statsmodels": __import__('statsmodels').__version__,
        "numpy": np.__version__,
        "matplotlib": __import__('matplotlib').__version__,
    }
    print("Reproducibility Information")
    print("=" * 60)
    print(_json.dumps(_repro, indent=2))

    return df_analysis,
```
</code_template>

</implementation_pattern>

<examples>

<example context="encoding_detection" difficulty="basic">
<description>Detecting file encoding before reading CSV files</description>
<code>
```python
@app.cell
def detect_and_load_csv(filepath):
    #RATIONALE: Encoding mismatches cause silent character corruption.
    # We detect encoding first, document it for reproducibility, and
    # handle common encoding issues before reading data.

    import pandas as pd
    import os
    import chardet  # pip install chardet

    # MANDATORY: Check file exists
    assert os.path.exists(filepath), f"File not found: {filepath}"

    # MANDATORY: Detect encoding before reading
    print("=" * 60)
    print("ENCODING DETECTION")
    print("=" * 60)
    
    # Read a sample to detect encoding (faster than reading entire file)
    with open(filepath, 'rb') as f:
        raw_data = f.read(10000)  # Read first 10KB for detection
    
    detection_result = chardet.detect(raw_data)
    detected_encoding = detection_result['encoding']
    confidence = detection_result['confidence']
    
    print(f"Detected encoding: {detected_encoding}")
    print(f"Confidence: {confidence:.2%}")
    
    # Common encodings to try if detection is uncertain
    encodings_to_try = [
        detected_encoding,  # Try detected first
        'utf-8',           # Most common modern encoding
        'latin-1',         # Common for European data
        'iso-8859-1',      # Alternative to latin-1
        'cp1252',          # Windows encoding
        'utf-16',          # Unicode with BOM
    ]
    
    # Remove duplicates while preserving order
    encodings_to_try = list(dict.fromkeys(encodings_to_try))
    
    # Try each encoding until one works
    df = None
    used_encoding = None
    
    for encoding in encodings_to_try:
        if encoding is None:
            continue
        try:
            print(f"\nAttempting to read with encoding: {encoding}")
            df = pd.read_csv(filepath, encoding=encoding, nrows=5)  # Test with 5 rows first
            used_encoding = encoding
            print(f"SUCCESS: File readable with {encoding}")
            break
        except (UnicodeDecodeError, UnicodeError) as e:
            print(f"  Failed: {str(e)[:60]}...")
            continue
        except Exception as e:
            # Other errors (not encoding-related) - re-raise
            raise
    
    if df is None:
        raise ValueError(f"Could not read file with any encoding tried: {encodings_to_try}")
    
    # Now read full file with correct encoding
    print(f"\nReading full file with encoding: {used_encoding}")
    df = pd.read_csv(filepath, encoding=used_encoding)
    
    # MANDATORY: Document encoding for reproducibility
    print("\n" + "=" * 60)
    print("ENCODING INFORMATION (for reproducibility)")
    print("=" * 60)
    print(f"File encoding: {used_encoding}")
    print(f"Detection confidence: {confidence:.2%}")
    print(f"File size: {os.path.getsize(filepath):,} bytes")
    
    return df, used_encoding,
```
</code>
<output_interpretation>
Encoding detection prevents silent character corruption. Common issues:
- UTF-8 files read as latin-1: accented characters become garbage
- Windows-1252 files read as UTF-8: parsing fails on special characters
- Mixed encodings: some rows readable, others fail silently

Always document the encoding used for reproducibility.
</output_interpretation>
<best_practice>
For CSV files:
1. Detect encoding before reading (use chardet or charset-normalizer)
2. Try common encodings if detection uncertain
3. Document encoding used in reproducibility section
4. If encoding detection unavailable, try: utf-8, latin-1, cp1252 in order
5. Check for encoding errors in string columns after loading
</best_practice>
</example>

<example context="validation_catches_error" difficulty="basic">
<description>Defensive validation preventing silent failure</description>
<code>
```python
@app.cell
def validate_before_analysis(df):
    #This example shows how defensive validation catches
    # errors that would otherwise produce invalid results silently.
    # Based on real retractions where analyses ran on wrong data types.

    import pandas as pd
    import numpy as np

    # Scenario: User thinks 'treatment' is binary but it's actually continuous
    print("Checking treatment variable...")

    # MANDATORY: Validate assumptions about the data
    unique_vals = df['treatment'].unique()
    print(f"Unique treatment values: {unique_vals}")

    if not set(unique_vals).issubset({0, 1}):
        print("\nERROR: Treatment is not binary!")
        print(f"Found values: {unique_vals}")
        print("\nThis would have caused:")
        print("- Wrong model specification")
        print("- Invalid causal interpretation")
        print("- Meaningless 'treatment effect'")

        # Show what would happen with silent failure
        if len(unique_vals) > 2:
            # Demonstrate the error
            mean_by_treatment = df.groupby('treatment')['outcome'].mean()
            print(f"\nMeans by 'treatment': \n{mean_by_treatment}")
            print("\nWARNING: These are NOT treatment effects!")

        raise ValueError("Treatment must be binary (0/1) for causal analysis")

    print("SUCCESS: Treatment is binary")

    # Additional validation
    assert df['outcome'].dtype in ['float64', 'int64'], "Outcome must be numeric"
    assert not df[['treatment', 'outcome']].isna().all(axis=1).any(), "Complete observations required"

    return None,
```
</code>
<output_interpretation>
This validation would catch a critical error where continuous dose is mistaken for binary treatment, preventing false causal claims.
</output_interpretation>
</example>

<example context="transformation_transparency" difficulty="intermediate">
<description>Making all data transformations explicit</description>
<code>
```python
@app.cell
def transparent_transformations(df):
    #Every transformation is shown and justified to prevent
    # hidden researcher degrees of freedom. Simmons et al. (2011) show
    # how undisclosed flexibility in data analysis inflates false positive rates.

    import pandas as pd
    import numpy as np

    print("DATA TRANSFORMATION DOCUMENTATION")
    print("=" * 60)

    # Original data summary
    print(f"Original N: {len(df)}")
    print(f"Original outcome range: [{df['outcome'].min():.2f}, {df['outcome'].max():.2f}]")

    # MANDATORY: Document each transformation step
    df_transformed = df.copy()

    # Step 1: Handle outliers (document cutoff and rationale)
    Q1 = df['outcome'].quantile(0.25)
    Q3 = df['outcome'].quantile(0.75)
    IQR = Q3 - Q1
    outlier_threshold = Q3 + 3*IQR  # Using 3*IQR for extreme outliers only

    n_outliers = (df['outcome'] > outlier_threshold).sum()
    print(f"\nStep 1: Windsorizing {n_outliers} extreme outliers (>{outlier_threshold:.2f})")
    print(f"  Rationale: Values >3*IQR likely measurement errors")
    print(f"  Alternative: Could use log transformation instead")

    df_transformed.loc[df_transformed['outcome'] > outlier_threshold, 'outcome'] = outlier_threshold

    # Step 2: Create categorical variable (document cutoffs)
    median_val = df_transformed['outcome'].median()
    print(f"\nStep 2: Creating binary indicator at median ({median_val:.2f})")
    print(f"  Rationale: Testing for heterogeneous effects above/below median")
    print(f"  Note: This reduces power but aids interpretation")

    df_transformed['outcome_high'] = (df_transformed['outcome'] > median_val).astype(int)

    # Step 3: Log transformation (document reason)
    print(f"\nStep 3: Log transformation of outcome")
    print(f"  Skewness before: {df['outcome'].skew():.2f}")

    # Handle zeros if present
    min_positive = df_transformed[df_transformed['outcome'] > 0]['outcome'].min()
    if (df_transformed['outcome'] == 0).any():
        offset = min_positive / 2
        print(f"  Adding offset {offset:.4f} to handle zeros")
        df_transformed['log_outcome'] = np.log(df_transformed['outcome'] + offset)
    else:
        df_transformed['log_outcome'] = np.log(df_transformed['outcome'])

    print(f"  Skewness after: {df_transformed['log_outcome'].skew():.2f}")

    # MANDATORY: Summary of all changes
    print("\n" + "=" * 60)
    print("TRANSFORMATION SUMMARY")
    print("=" * 60)
    print(f"Records modified: {(df['outcome'] != df_transformed['outcome']).sum()}")
    print(f"New variables created: outcome_high, log_outcome")
    print(f"Original data preserved in: df")
    print(f"Transformed data in: df_transformed")

    # MANDATORY: Note impact on interpretation
    print("\nINTERPRETATION NOTE:")
    print("- Results apply to windsorized distribution")
    print("- Log coefficients represent % changes")
    print("- Binary outcome reduces power but simplifies interpretation")

    return df_transformed,
```
</code>
<lesson>
Transparency in data transformation prevents p-hacking and enables replication. Every choice must be documented and justified.
</lesson>
</example>

<example context="data_provenance_documentation" difficulty="intermediate">
<description>Documenting complete data provenance</description>
<code>
```python
@app.cell
def document_data_provenance():
    #Data provenance documents the complete lineage of data:
    # where it came from, how it was collected, what preprocessing
    # occurred, and when it was accessed. This is essential for
    # reproducibility and validity assessment (Stodden et al., 2016).

    import hashlib
    import os
    from datetime import datetime

    provenance_info = {
        "data_sources": {
            "primary_dataset": {
                "source_name": "RCT Baseline Survey",
                "source_type": "Primary data collection",
                "collection_method": "Face-to-face interviews using ODK Collect",
                "collection_dates": {
                    "start": "2024-01-15",
                    "end": "2024-03-20"
                },
                "collection_location": "Rural districts in Northern Uganda",
                "sampling_method": "Randomized controlled trial baseline",
                "sample_size_collected": 1200,
                "data_access_date": "2024-04-01",
                "data_access_method": "Downloaded from SurveyCTO server",
                "file_path": "/mnt/data/baseline_survey.csv",
                "file_hash": None,  # Will compute below
                "file_size_bytes": None,
                "preprocessing_steps": [
                    "Exported from SurveyCTO in CSV format",
                    "No manual edits performed",
                    "Variable names preserved as exported"
                ]
            },
            "treatment_assignments": {
                "source_name": "Randomization List",
                "source_type": "Administrative data",
                "collection_method": "Generated using random number generator",
                "collection_dates": {
                    "date": "2024-01-10"
                },
                "randomization_method": "Stratified block randomization",
                "strata": ["district", "gender"],
                "block_size": 4,
                "data_access_date": "2024-04-01",
                "file_path": "/mnt/data/treatment_assignments.csv",
                "file_hash": None,
                "preprocessing_steps": [
                    "Generated using R script: randomization.R",
                    "Exported to CSV for merging"
                ]
            }
        },
        "data_merging": {
            "merge_date": "2024-04-01",
            "merge_method": "Left join on unit_id",
            "merge_key": "unit_id",
            "merge_validation": "All baseline observations matched",
            "merged_file_path": "/mnt/data/merged_analysis_data.csv"
        },
        "data_limitations": [
            "Baseline survey had 5% non-response rate",
            "Missing income data for 12% of sample (documented in analysis)",
            "Treatment assignments were double-blind"
        ]
    }

    # Compute file hashes for data integrity
    for source_key, source_info in provenance_info["data_sources"].items():
        filepath = source_info.get("file_path")
        if filepath and os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            file_size = os.path.getsize(filepath)
            provenance_info["data_sources"][source_key]["file_hash"] = file_hash
            provenance_info["data_sources"][source_key]["file_size_bytes"] = file_size

    # Print human-readable provenance documentation
    print("=" * 70)
    print("DATA PROVENANCE DOCUMENTATION")
    print("=" * 70)
    
    for source_key, source_info in provenance_info["data_sources"].items():
        print(f"\n{source_info['source_name']}")
        print(f"   Type: {source_info['source_type']}")
        print(f"   Collection method: {source_info['collection_method']}")
        
        if 'collection_dates' in source_info:
            dates = source_info['collection_dates']
            if 'start' in dates:
                print(f"   Collection period: {dates['start']} to {dates['end']}")
            else:
                print(f"   Collection date: {dates['date']}")
        
        print(f"   Data accessed: {source_info['data_access_date']}")
        print(f"   File: {source_info['file_path']}")
        
        if source_info.get('file_hash'):
            print(f"   SHA-256: {source_info['file_hash'][:16]}...")
            print(f"   Size: {source_info['file_size_bytes']:,} bytes")
        
        if 'preprocessing_steps' in source_info:
            print(f"   Preprocessing steps:")
            for step in source_info['preprocessing_steps']:
                print(f"     - {step}")
    
    if 'data_merging' in provenance_info:
        merge_info = provenance_info['data_merging']
        print(f"\nData Merging")
        print(f"   Date: {merge_info['merge_date']}")
        print(f"   Method: {merge_info['merge_method']}")
        print(f"   Key: {merge_info['merge_key']}")
        print(f"   Validation: {merge_info['merge_validation']}")
    
    if 'data_limitations' in provenance_info:
        print(f"\nData Limitations")
        for limitation in provenance_info['data_limitations']:
            print(f"   - {limitation}")
    
    # Save structured provenance to JSON
    import json
    with open('./data_provenance.json', 'w') as f:
        json.dump(provenance_info, f, indent=2)
    
    print(f"\nSUCCESS: Full provenance documentation saved to ./data_provenance.json")
    
    return provenance_info,
```
</code>
<best_practice>
Data provenance must document:
1. **Original sources**: Where data came from (surveys, administrative records, APIs, etc.)
2. **Collection methods**: How data was collected (survey instruments, measurement tools, protocols)
3. **Collection dates**: When data was collected (affects external validity)
4. **Data access**: When and how you accessed the data
5. **Preprocessing**: Any cleaning, merging, or transformations done BEFORE your analysis code
6. **File integrity**: File hashes to detect if data changes
7. **Limitations**: Known data quality issues or constraints

This enables others to:
- Verify data authenticity
- Assess data quality
- Understand potential biases
- Replicate data preparation steps
- Detect preprocessing errors
</best_practice>
</example>

<example context="reproducibility_appendix" difficulty="basic">
<description>Reproducibility cell -- MUST be the last cell in every notebook response</description>
<code>
```python
import sys, platform, json

_repro = {
    "python": sys.version,
    "platform": platform.platform(),
    "pandas": pd.__version__,
    "statsmodels": __import__('statsmodels').__version__,
    "numpy": np.__version__,
    "matplotlib": __import__('matplotlib').__version__,
}
print("Reproducibility Information")
print("=" * 60)
print(json.dumps(_repro, indent=2))
```
</code>
<best_practice>
This cell is MANDATORY in every response. It documents the computational
environment so results can be verified. Include it as the final cell, always.
Additional keys (e.g. random seed, file hashes) may be appended when relevant.
</best_practice>
</example>

</examples>

<common_mistakes>

<mistake severity="critical">
  <what>Running analysis without input validation</what>
  <consequence>Silent failures producing wrong results that look valid</consequence>
  <prevention>ALWAYS validate data types, ranges, and required columns first</prevention>
</mistake>

<mistake severity="critical">
  <what>Transforming data without documentation</what>
  <consequence>Hidden researcher degrees of freedom, unreproducible results</consequence>
  <prevention>Document every transformation with rationale</prevention>
</mistake>

<mistake severity="high">
  <what>Omitting software versions from reports</what>
  <consequence>Results cannot be reproduced when packages update</consequence>
  <prevention>Always include sessionInfo() or equivalent</prevention>
</mistake>

<mistake severity="high">
  <what>Using magic numbers without explanation</what>
  <consequence>Future researchers don't understand choices</consequence>
  <prevention>Define all constants with explanatory comments</prevention>
</mistake>

<mistake severity="medium">
  <what>Not setting random seeds</what>
  <consequence>Results vary between runs</consequence>
  <prevention>Set seeds for all stochastic operations</prevention>
</mistake>

<mistake severity="critical">
  <what>Omitting data provenance documentation</what>
  <consequence>Cannot verify data authenticity, assess quality, detect preprocessing errors, or understand limitations. Hidden preprocessing steps can introduce bias that invalidates findings</consequence>
  <prevention>ALWAYS document: data sources, collection methods, access dates, and any preprocessing done before analysis. Include file hashes for integrity verification</prevention>
</mistake>

<mistake severity="high">
  <what>Reading CSV files without checking encoding</what>
  <consequence>Silent character corruption (accented characters become garbage), parsing failures, incorrect string comparisons, missing data from encoding errors</consequence>
  <prevention>ALWAYS detect encoding before reading text files. Use chardet or charset-normalizer, try common encodings (utf-8, latin-1, cp1252) if detection uncertain, and document encoding used for reproducibility</prevention>
</mistake>

</common_mistakes>

<interpretation_guide>

<interpreting_results>
- Statistical significance ≠ practical importance
- Effect sizes need context and units
- Confidence intervals show precision
- Multiple testing inflates Type I error
</interpreting_results>

<red_flags>
- P-values just below 0.05 (possible p-hacking)
- Missing data patterns correlating with treatment
- Outliers driving results
- Assumptions clearly violated
</red_flags>

<next_steps>
- All validations pass → Proceed with analysis
- Assumptions violated → Document and use robust methods
- Missing data substantial → Implement appropriate handling
- Results surprising → Check for errors and run sensitivity analyses
</next_steps>

</interpretation_guide>

<references>
<paper>Simmons, J.P., Nelson, L.D. & Simonsohn, U. (2011). "False-Positive Psychology." Psychological Science. Researcher degrees of freedom.</paper>
<paper>Gelman, A. & Loken, E. (2014). "The Statistical Crisis in Science." American Scientist. Garden of forking paths.</paper>
<paper>Nosek, B.A. et al. (2015). "Estimating the reproducibility of psychological science." Science. Reproducibility crisis.</paper>
<paper>Stodden, V., Seiler, J. & Ma, Z. (2016). "An empirical analysis of journal policy effectiveness for computational reproducibility." PNAS. Data provenance and reproducibility.</paper>
</references>

</skill_content>
# Core Methodology: Code Examples

Detailed code templates demonstrating mandatory patterns from [SKILL.md](SKILL.md).
All code is pure Python suitable for Marimo cells -- no decorators, no function wrappers.

---

## Rigorous Analysis Pattern (Complete Template)

The canonical structure every statistical analysis should follow.

```python
# This template demonstrates the mandatory structure for
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

# MANDATORY: Reproducibility information
print("\n" + "=" * 60)
print("REPRODUCIBILITY INFORMATION")
print("=" * 60)
print(f"Analysis timestamp: {datetime.now().isoformat()}")
print(f"Random seed: {42}")
print(f"Python version: {sys.version}")
print(f"Pandas version: {pd.__version__}")
print(f"Numpy version: {np.__version__}")

# MANDATORY: File hashes for inputs (part of data provenance)
import hashlib
if 'input_file' in locals():
    with open(input_file, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    print(f"Input file hash: {file_hash}")
    print(f"Input file path: {input_file}")

df_analysis
```

---

## Encoding Detection (Basic)

Detecting file encoding before reading CSV files.

```python
# RATIONALE: Encoding mismatches cause silent character corruption.
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

df, used_encoding
```

**Output interpretation:** Encoding detection prevents silent character corruption. Common issues:
- UTF-8 files read as latin-1: accented characters become garbage
- Windows-1252 files read as UTF-8: parsing fails on special characters
- Mixed encodings: some rows readable, others fail silently

**Best practice:** For CSV files: (1) detect encoding before reading, (2) try common encodings if uncertain, (3) document encoding used, (4) if detection unavailable try utf-8, latin-1, cp1252 in order, (5) check for encoding errors in string columns after loading.

---

## Defensive Validation (Basic)

Defensive validation preventing silent failure.

```python
# This example shows how defensive validation catches
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
```

**Output interpretation:** This validation catches critical errors where continuous dose is mistaken for binary treatment, preventing false causal claims.

---

## Transparent Transformations (Intermediate)

Making all data transformations explicit.

```python
# Every transformation is shown and justified to prevent
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

df_transformed
```

**Lesson:** Transparency in data transformation prevents p-hacking and enables replication. Every choice must be documented and justified.

---

## Data Provenance Documentation (Intermediate)

Documenting complete data provenance.

```python
# Data provenance documents the complete lineage of data:
# where it came from, how it was collected, what preprocessing
# occurred, and when it was accessed. This is essential for
# reproducibility and validity assessment (Stodden et al., 2016).

import hashlib
import os
import json
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
with open('./data_provenance.json', 'w') as f:
    json.dump(provenance_info, f, indent=2)

print(f"\nSUCCESS: Full provenance documentation saved to ./data_provenance.json")

provenance_info
```

**Best practice:** Data provenance must document: (1) original sources, (2) collection methods, (3) collection dates, (4) data access details, (5) preprocessing before analysis, (6) file hashes for integrity, (7) known limitations.

---

## Complete Reproducibility Documentation (Advanced)

```python
# Following Nosek et al. (2015) and OSF reproducibility
# guidelines, we document everything needed to exactly reproduce
# this analysis, including computational environment and data provenance.

import sys
import platform
import json
import hashlib
import subprocess
import os
from datetime import datetime
import importlib.metadata

repro_info = {
    "timestamp": datetime.now().isoformat(),
    "random_seed": 42,
    "system": {
        "platform": platform.platform(),
        "python": sys.version,
        "machine": platform.machine(),
        "processor": platform.processor()
    },
    "packages": {},
    "data_sources": {},
    "git_info": {}
}

# Get package versions
critical_packages = [
    'pandas', 'numpy', 'scipy', 'statsmodels',
    'scikit-learn', 'matplotlib', 'jupyterlab'
]

for package in critical_packages:
    try:
        version = importlib.metadata.version(package)
        repro_info["packages"][package] = version
    except importlib.metadata.PackageNotFoundError:
        repro_info["packages"][package] = "not installed"

# Get data file hashes
data_files = [
    "/mnt/data/study_data.csv",
    "/mnt/data/treatment_assignments.csv"
]

for filepath in data_files:
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        file_stat = os.stat(filepath)
        repro_info["data_sources"][filepath] = {
            "sha256": file_hash,
            "size_bytes": file_stat.st_size,
            "modified": datetime.fromtimestamp(file_stat.st_mtime).isoformat()
        }

# Get git information if available
try:
    git_commit = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        stderr=subprocess.DEVNULL
    ).decode().strip()
    repro_info["git_info"]["commit"] = git_commit

    git_branch = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
        stderr=subprocess.DEVNULL
    ).decode().strip()
    repro_info["git_info"]["branch"] = git_branch

    # Check for uncommitted changes
    git_status = subprocess.check_output(
        ['git', 'status', '--porcelain'],
        stderr=subprocess.DEVNULL
    ).decode().strip()
    repro_info["git_info"]["has_uncommitted_changes"] = bool(git_status)

except (subprocess.CalledProcessError, FileNotFoundError):
    repro_info["git_info"]["error"] = "Not a git repository or git not available"

# Output in both human-readable and machine-readable formats
print("=" * 60)
print("COMPUTATIONAL REPRODUCIBILITY INFORMATION")
print("=" * 60)

print(f"\nTimestamp: {repro_info['timestamp']}")
print(f"Random seed: {repro_info['random_seed']}")

print(f"\nSystem:")
for key, value in repro_info['system'].items():
    if key == 'python':
        value = value.split()[0]  # Just version number
    print(f"  {key}: {value}")

print(f"\nPackage versions:")
for package, version in repro_info['packages'].items():
    print(f"  {package}: {version}")

print(f"\nData sources:")
for filepath, info in repro_info['data_sources'].items():
    print(f"  {filepath}:")
    print(f"    SHA-256: {info['sha256'][:16]}...")
    print(f"    Size: {info['size_bytes']:,} bytes")

if repro_info['git_info']:
    print(f"\nGit information:")
    for key, value in repro_info['git_info'].items():
        print(f"  {key}: {value}")

# Save JSON for perfect reproducibility
with open('./reproducibility_info.json', 'w') as f:
    json.dump(repro_info, f, indent=2)

print(f"\nSUCCESS: Full details saved to ./reproducibility_info.json")

# Create requirements.txt for pip
with open('./requirements.txt', 'w') as f:
    for package, version in repro_info['packages'].items():
        if version != "not installed":
            f.write(f"{package}=={version}\n")

print(f"SUCCESS: Package list saved to ./requirements.txt")

repro_info
```

**Best practice:** Perfect reproducibility requires: (1) exact package versions, (2) data file hashes, (3) git commit info, (4) random seeds, (5) timestamp.

# Example Data and Workflows

This directory contains example datasets and workflows for testing the Immunology PI Agent.

## Example Analyses

### 1. Inflammation Time-Course

Analyze cytokine expression over time in an LPS-induced inflammation model.

```bash
python main.py
> analyze ./examples/sample_data/cytokine_timecourse.csv
> What does the kinetics of IL-6 and TNF-α suggest about the inflammatory phase?
```

### 2. Flow Cytometry Analysis

Evaluate immune cell composition in treated vs. control animals.

```bash
python main.py
> analyze ./examples/sample_data/flow_cytometry_plot.png
> Are there experimental design issues with these flow plots?
```

### 3. Hypothesis Validation

Test whether data supports a specific mechanistic hypothesis.

```bash
python main.py
> ask I hypothesize that IL-17 drives neutrophil recruitment. My data shows: [describe findings]. Is this supported?
```

## Coming Soon

- Sample CSV datasets with inflammation markers
- Example flow cytometry and immunohistochemistry images
- Validation workflows with known results

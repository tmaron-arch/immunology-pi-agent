# Immunology PI Agent

An AI-powered principal investigator agent specialized in inflammation immunology research. Analyzes experimental data, validates hypotheses, identifies design flaws, and explores alternative interpretations with rigorous scientific thinking.

## Core Capabilities

### Priority 1: Data Analysis & Hypothesis Validation
- **Data Analysis**: Process CSV/Excel spreadsheets, parse graphs, and analyze images (flow cytometry, microscopy, immunohistochemistry)
- **Hypothesis Validation**: Evaluate whether experimental data supports or refutes stated hypotheses
- **Critical Evaluation**: Identify experimental design flaws, confounds, and control issues
- **Alternative Hypotheses**: Generate and evaluate alternative explanations for observed data

### Priority 2: Literature Integration & Experiment Design
- Cross-reference findings with published inflammation immunology literature
- Suggest experimental improvements and protocol refinements
- Recommend appropriate controls and statistical approaches

## Specialization

**Focus Area**: Inflammation Immunology
- Cytokine signaling (TNF-α, IL-6, IL-1β, IL-17, IFN-γ)
- Immune cell recruitment and activation (neutrophils, macrophages, T cells)
- Resolution of inflammation and tissue repair
- Chronic inflammatory conditions

## Technology Stack

- **AI Model**: Claude 3.5 Sonnet / Claude Science
- **Language**: Python 3.11+
- **Data Processing**: pandas, numpy, scikit-learn, Pillow
- **Visualization**: matplotlib, seaborn
- **API**: Anthropic Claude API
- **Interface**: Interactive dialogue via CLI/web interface

## Input Formats Supported

- **Spreadsheets**: CSV, Excel (.xlsx, .xls)
- **Images**: PNG, JPG, TIFF (flow cytometry plots, microscopy, immunohistochemistry)
- **Graphs**: Embedded in images or as data files
- **Natural Language**: Experiment descriptions, hypotheses, questions

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run the agent
python main.py
```

## Architecture

```
immunology-pi-agent/
├── main.py                 # Agent entry point
├── agent/
│   ├── pi_agent.py        # Core PI reasoning engine
│   ├── data_analyzer.py   # Data analysis module
│   ├── hypothesis_validator.py  # Hypothesis validation logic
│   ├── literature_integrator.py # Literature cross-reference
│   └── experiment_designer.py   # Experiment design suggestions
├── utils/
│   ├── file_handler.py    # CSV, Excel, image parsing
│   ├── image_processor.py # Image analysis helpers
│   └── data_validator.py  # Data quality checks
├── prompts/
│   └── system_prompts.md  # Claude system instructions
├── examples/
│   └── sample_data/       # Example datasets
└── tests/
    └── test_agent.py
```

## Key Features

✅ **Multi-modal Analysis**: Accepts spreadsheets, images, and natural language  
✅ **PI-Level Critique**: Evaluates experimental rigor, identifies flaws  
✅ **Hypothesis Exploration**: Tests multiple interpretations of data  
✅ **Literature Awareness**: References immunology domain knowledge  
✅ **Interactive Dialogue**: Iterative refinement through conversation  

## Development Status

- [x] Repository setup
- [ ] Core agent implementation
- [ ] Data analysis module
- [ ] Hypothesis validation engine
- [ ] Literature integration
- [ ] Experiment design suggestions
- [ ] Testing and documentation

## License

MIT

## Contributing

Contributions welcome. Please open issues or PRs for bugs, features, or improvements.

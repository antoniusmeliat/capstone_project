# capstone_project

## TLDR

This project implements a Bayesian Black‑Box Optimisation framework using Gaussian Process surrogate models to make efficient decisions in complex and uncertain settings. The core Jupyter notebook learns iteratively from previous evaluations, balancing exploration and exploitation to identify high‑quality solutions with minimal costly trials in scenarios where brute‑force experimentation would be impractical. The approach evolved over multiple weeks from broad exploration to disciplined confirmation and treats optimisation as a learning process rather than a simple search.

---

## Model Documentation

- [Model Datasheet](model_info/BBO_Capstone_Datasheet.md)
- [Model Card](model_info/BBO_Capstone_Model_Card.md) 

These documents provide transparency around assumptions, intended use, limitations, and ethical considerations

---

## Overview

This capstone project is a core component of the **Professional Certificate in Machine Learning and Artificial Intelligence** programme. It spans multiple modules and is designed to help students apply machine learning concepts to complex decision‑making problems under uncertainty.

The project explores how **artificial intelligence can support better decisions in environments where trial and error would be too slow or too costly**. It uses **Bayesian Black‑Box Optimisation (BBO)** to learn from previous evaluations and intelligently propose improved candidates. Rather than searching blindly, the system builds a probabilistic understanding of the problem and adapts its behaviour as confidence grows.

This class of optimisation is particularly relevant when evaluations are expensive, noisy, or limited, such as hyperparameter tuning, resource allocation, system design, and other real‑world ML optimisation tasks.

---

## Project Context and Stages

The capstone is structured across two main stages:

- **Stage 1: Exploration and experimentation**  
  Students test ideas through guided exercises to strengthen understanding of optimisation behaviour and uncertainty.

- **Stage 2: Structured development and refinement**  
  The project evolves into a fully documented optimisation system with diagnostics, reflection, and repeatable logic.

The project is continuous, with required components submitted across different modules. By the end of the programme, the outcome is a **portfolio‑ready artefact** supported by experimentation logs and reflective analysis.

---

## Bayesian Optimisation Approach and Notebook Overview

The **entire optimisation logic and experimentation workflow** live in the Jupyter notebook located in the `notebook/` directory. This notebook was built from scratch in Week 1 using concepts learned on the course and was refined incrementally throughout the capstone.

The notebook focuses on four core capabilities:

- **Gaussian Process surrogate models** to predict outcomes and uncertainty  
- **Acquisition strategies** to balance exploration and exploitation  
- **Visual diagnostics** to interpret model behaviour and guide decisions  
- **Iterative analysis** to adapt strategy as more data becomes available  

Instead of relying on brute‑force sampling, the optimisation framework learns from prior results to guide future queries more efficiently.

### Evolution of the optimisation strategy

The optimisation approach evolved deliberately over time:

- **Early phase**  
  Broad exploration was prioritised to reduce uncertainty and understand how different input dimensions influenced outcomes. Performance was secondary to learning structure.

- **Mid phase**  
  Focus shifted toward improving surrogate fidelity. Enhanced modelling revealed ridges, boundary behaviour, and low‑impact dimensions. Exploration became targeted, and exploitation became justified.

- **Late phase**  
  The strategy prioritised discipline and confirmation. Exploration was reduced to targeted validation while exploitation focused on consolidating confidence rather than chasing marginal gains.

This staged approach prevented premature convergence early on while allowing confident exploitation once the surrogate models stabilised. By the final stage, the optimisation process resembled a stabilised learning policy rather than an active search.

---

## Timeline

The project followed a structured execution plan:

- **Week 1 (6–8 hours)**: Define scope, success criteria, and tools  
- **Week 2 (8–10 hours)**: Initial exploration and uncertainty reduction  
- **Week 3 (8–10 hours)**: Surrogate refinement and strategy improvement  
- **Week 4 (6–8 hours)**: Structural diagnostics and sensitivity analysis  
- **Week 5 (8–10 hours)**: Structured exploitation and refinement  
- **Week 6 (8–10 hours)**: Robustness and stability checks  
- **Week 7 (10–12 hours)**: Strategy stress testing  
- **Week 8 (8–10 hours)**: Scale and efficiency analysis  
- **Week 9 (10–12 hours)**: Consolidation and diagnostics  
- **Week 10 (8–10 hours)**: Final refinement  
- **Weeks 11–13**: Confirmation, reflection, and final evaluation  

---

## Methodological Principles

The optimisation strategy was guided by the following principles:

- Surrogate modelling to learn efficiently from limited evaluations  
- Adaptive exploration and exploitation rather than fixed rules  
- Dimensional relevance analysis to reduce unnecessary complexity  
- Visual interpretation to support transparent decision making  
- Incremental refinement over aggressive optimisation  
- Robustness and confidence over peak chasing  

These principles reflect real‑world ML systems where uncertainty, cost, and interpretability play critical roles.

---

## Project Structure
```
capstone_project/
├── model_info/
│   ├── BBO_Capstone_Datasheet.md
│   └── BBO_Capstone_Model_Card.md
├── notebook/
│   └── Capstone Consolidated Strategy.ipynb # Core Bayesian optimisation workflow and experimentation notebook
├── runs/
│   ├── week_1/
│   ├── week_2/
│   ├── week_3/
│   ├── week_4/
│   ├── week_5/
│   ├── week_6/
│   ├── week_7/
│   ├── week_8/
│   ├── week_9/
│   ├── week_10/
│   ├── week_11/
│   └── week_12/
├── LICENSE.md
└── README.md
```
---

## How to Run the Notebook

1. **Set up Python environment**  
   - Install Python 3.10+ and create a virtual environment (recommended).
   - Install required packages using `pip install -r requirements.txt` (if available) or manually install dependencies such as numpy, pandas, scikit-learn, matplotlib, and jupyter.

2. **Launch Jupyter Notebook**  
   - Activate your environment.
   - Run `jupyter notebook` in the project root or `notebook/` directory.

3. **Open the notebook**  
   - In your browser, open `notebook/Capstone Consolidated Strategy.ipynb`.

4. **Run all cells in order**  
   - Start from the top and execute each cell sequentially for best results.
   - Follow prompts in the notebook for any required configuration or data input.

5. **Review outputs and visualizations**  
   - Use the provided diagnostics and plots to interpret results and guide further experimentation.

---

## Outcome and Relevance

This project demonstrates that **Bayesian optimisation is most effective when treated as a learning process rather than a simple search problem**. By analysing data, adjusting strategies, and visualising behaviour throughout the process, the framework efficiently identifies high‑quality solutions in settings where exhaustive experimentation would be impractical.

**Key take‑away:** performance gains came less from aggressive optimisation and more from disciplined learning, uncertainty management, and strategic restraint.

The approach generalises to real‑world ML applications such as hyperparameter tuning, resource allocation, predictive maintenance, and other optimisation tasks under uncertainty.

---

## License

This project is licensed under the Creative Commons
Attribution–NonCommercial–NoDerivatives 4.0 International License.
See the [LICENSE](LICENSE.md) file for details.

---

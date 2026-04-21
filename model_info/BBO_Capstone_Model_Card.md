# Model Card: Portfolio-Based Bayesian Black-Box Optimisation (BBO)

## Overview

**Model name:** Portfolio-Based Bayesian Black-Box Optimisation  
**Type:** Sequential optimisation framework using Gaussian Process surrogates  
**Version:** Capstone implementation over ten optimisation rounds  
**Developer:** Antonius Meliat - Student on Imperial University's Professional Certificate in Machine Learning and Artificial Intelligence

This approach applies Bayesian optimisation as a portfolio of strategies rather than a single fixed procedure. Different optimisation behaviours such as exploration refinement and consolidation are used depending on the observed characteristics of each objective function.

---

## Intended use

### Suitable uses

This optimisation approach is suitable for:
- Educational exploration of Bayesian optimisation behaviour
- Analysing exploration and exploitation trade-offs
- Studying surrogate model confidence over time
- Comparing optimisation strategies across multiple black-box functions

It is appropriate for problems where function evaluations are expensive and the optimisation budget is limited.

### Uses to avoid

This approach should not be used for:
- High-stakes real-world decision making
- Benchmarking algorithms for performance claims
- Fully automated optimisation without human oversight
- Highly noisy or adversarial optimisation tasks

---

## Details of the approach

The optimisation was carried out over ten sequential rounds. Early rounds focused on exploration to build an initial understanding of each function. Expected Improvement and Upper Confidence Bound acquisition functions were used to guide sampling.

As more data became available Gaussian Process surrogates were updated to estimate uncertainty and detect structure such as ridges or boundaries. Automatic Relevance Determination was used to assess which input dimensions appeared influential.

Some functions transitioned into local refinement where queries were selected close to the current best values. Other functions continued exploring due to persistent uncertainty or weak gradients. Additional mechanisms such as trust regions feature screening and global survivor constraints were used to avoid premature collapse.

Optimisation behaviour was adapted per function rather than enforced uniformly across all tasks.

---

## Performance

Performance was assessed qualitatively and comparatively rather than through a single numerical metric.

Across the eight objective functions:
- Exploration-focused strategies maintained diversity and uncertainty
- Exploitation-focused strategies achieved stable improvements or confirmed convergence
- Hybrid strategies transitioned smoothly between exploration and refinement

Metrics and diagnostics used included:
- Observed objective values
- Expected Improvement and Upper Confidence Bound distributions
- ARD sensitivity patterns
- Diversity and pairwise distance measures
- Stability of surrogate predictions across rounds

Success criteria depended on the role of each function rather than absolute optimisation performance.

---

## Assumptions and limitations

A key assumption is that surrogate model confidence reflects true behaviour of the underlying function. The approach assumes that narrowed acquisition distributions and strong ARD signals indicate convergence rather than artefacts of limited sampling.

The strategy relies on sequential decision making which introduces path dependence. Early sampling decisions can strongly influence later outcomes. The limited evaluation budget restricts the ability to recover from early modelling errors.

The approach may perform poorly on highly multimodal noisy or deceptive objective functions.

---

## Ethical considerations

Although the optimisation process does not involve human data transparency remains important. This model card documents how decisions were made and highlights assumptions and limitations.

Clear documentation supports reproducibility and responsible reuse. It also helps prevent misuse by clarifying that the approach is pedagogical and experimental rather than production-ready.

---

## Reflection on documentation

This model card complements the dataset datasheet by explaining how optimisation decisions were made and how the strategy evolved. It balances clarity and conciseness to remain accessible to a student audience.

More technical detail could be provided such as full kernel specifications or optimisation schedules. However given the educational context and the supporting analysis notes the current structure is sufficient to understand the model’s behaviour strengths and limitations.
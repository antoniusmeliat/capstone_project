# Datasheet for the BBO Capstone Project Dataset

## Motivation

This dataset was created as part of my capstone project to explore how Bayesian Black‑Box Optimisation works in practice. The main goal was to understand how different optimisation strategies behave when the objective function is unknown and expensive to evaluate.

The dataset supports the task of analysing and comparing optimisation behaviour across multiple functions with different dimensionality and difficulty. It was also used to reflect on decision‑making during optimisation rather than focusing only on maximising performance.

The dataset was created by me as a student on Imperial University's Professional Certificate in machine learning and artificial intelligence. It was not funded by any organisation and was designed purely for learning and assessment purposes.

## Composition

The dataset contains a sequence of optimisation queries and their corresponding objective values. Each row represents one evaluated query where the input is a vector of real‑valued parameters and the output is a single scalar value returned by a black‑box function.

The data covers eight different optimisation functions with input spaces ranging from two to eight dimensions. The data is stored in tabular form and supported by diagnostic information such as acquisition scores ARD sensitivities and diversity measures used during decision‑making.

The dataset is relatively small which reflects the high cost of evaluations and the educational setting. Coverage of the search space is uneven by design. Some regions are sampled heavily during exploitation phases while others remain unexplored. There are no missing values within individual entries and no personal or sensitive data.

## Collection process

Data was collected iteratively using Bayesian optimisation rather than random sampling. For each function a strategy was chosen based on its behaviour in earlier rounds. Some functions focused on exploration while others focused on local refinement or a mix of both.

Queries were generated using Gaussian Process surrogate models with standard acquisition functions such as Expected Improvement and Upper Confidence Bound. In some cases additional rules such as trust regions feature screening or survivor constraints influenced which queries were selected.

The collection took place over several weeks with each new query informed by the results and diagnostics of previous ones. This introduces path dependence where later data reflects earlier modelling choices.

## Preprocessing and uses

Very little preprocessing was applied to the dataset. Inputs were sometimes standardised during model fitting but the stored data remains close to the original values returned by the optimisation process.

Objective values are used directly as labels and no manual annotation was required. Diagnostic outputs were generated alongside the data but the raw query‑response pairs were preserved.

The intended use of the dataset is for educational analysis of Bayesian optimisation strategies including exploration exploitation trade‑offs and model confidence over time. It is suitable for reflection and comparison but not for benchmarking or general performance claims.

Using this dataset to make claims about real‑world systems or for commercial purposes would be inappropriate.

## Distribution

The dataset is stored locally and forms part of the capstone submission. It is not publicly distributed and may only be shared with supervisors markers or examiners for assessment.

There is no formal licence and the data should be treated as academic coursework material only.

## Maintenance

The dataset is maintained by me as the project author. No further updates are planned after submission. Versions loosely correspond to weekly snapshots which are documented through analysis notes rather than a formal versioning system.

If the dataset is archived it should be kept together with written reflections and diagnostic plots as these are required to interpret the data correctly.

## Additional notes

The dataset reflects subjective decisions such as when to exploit or explore and when to trust surrogate confidence. These characteristics are intentional and support the learning goals of the capstone. The dataset should therefore be understood as a record of an optimisation process rather than a complete or neutral sample of the search space.
# capstone_project

## TLDR

This project implements a Bayesian Black‑Box Optimisation framework using Gaussian Process surrogate models to make efficient decisions in complex and uncertain settings. The core Jupyter notebook learns iteratively from previous evaluations, balancing exploration and exploitation to identify high‑quality solutions with minimal costly trials. The approach evolved over multiple weeks from broad exploration to disciplined confirmation and treats optimisation as a learning process rather than a brute‑force search.

---

## Overview

This capstone project is a core component of the **Professional Certificate in Machine Learning and Artificial Intelligence** programme. It spans multiple modules and is designed to help students apply machine learning concepts to complex decision‑making problems under uncertainty.

The project explores how **artificial intelligence can support better decisions in environments where trial and error would be too slow or too costly**. It uses **Bayesian Black‑Box Optimisation (BBO)** to learn from previous evaluations and intelligently propose improved candidates. Rather than searching blindly, the system builds a probabilistic understanding of the problem and adapts its behaviour as confidence grows.

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

The **core implementation** of this project lives in the Jupyter notebook located in the `notebook/` directory. This notebook was built from scratch in Week 1 using concepts learned on the course and was refined incrementally throughout the capstone.

The notebook integrates:

- **Gaussian Process surrogate models** to predict outcomes and uncertainty  
- **Acquisition strategies** to balance exploration and exploitation  
- **Visual diagnostics** to interpret model behaviour and guide decisions  
- **Iterative analysis** to adapt strategy as more data becomes available  

Instead of relying on brute‑force sampling, the optimisation framework learns from prior results to guide future queries more efficiently.

### Evolution of the optimisation strategy


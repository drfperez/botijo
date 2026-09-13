# Why Does a Botijo Have Its Traditional Shape? 🏺
### A Mathematical Modeling Study of Evaporative Cooling

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drfperez/botijo/blob/main/generate-botijo-colab-figures.py)
[![LaTeX](https://img.shields.io/badge/LaTeX-The%20UMAP%20Journal-blue.svg)](https://www.comap.com/periodicals/the-umap-journal)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Status:** Manuscript submitted to *The UMAP Journal* (Vol. 47, No. 3, 2026); currently under review. Not yet accepted.

This repository contains the numerical implementation, figure-generation scripts, and LaTeX manuscript for the mathematical modeling study on the shape optimization of the Spanish *botijo*.

---

## 📖 Overview

The **botijo** is a traditional Spanish porous clay pitcher used for centuries to chill drinking water without electricity. Water slowly seeps through the porous ceramic wall and evaporates into dry ambient air, extracting latent heat from the remaining liquid.

While qualitative descriptions are common in introductory thermodynamics, this project addresses a formal variational question:

> **Among all manufacturable porous vessels of equal volume capacity, what geometric profile minimizes the time required to cool water from $39\,^\circ\text{C}$ to $25\,^\circ\text{C}$?**

By representing the vessel as a unimodal surface of revolution and coupling vapor-diffusion mass loss with a lumped thermal energy balance (including clay wall heat capacity and bottom thermal isolation), we formulate a constrained shape-optimization problem. The global optimum—found via Differential Evolution followed by Nelder–Mead simplex refinement—yields a profile with a narrow base, wide mid-belly, and constricted neck, closely mirroring centuries of empirical artisan design.

---

## 🗂️ Repository Structure

```text
.
├── generate-botijo-colab-figures.py  # Python script (Colab/local) to generate 300 DPI vector PDF figures
└── README.md                         # Project documentation
```

Note: The compiled manuscript is currently 11 pages. The UMAP Journal typically publishes articles in the 15–25 page range, so the manuscript may be expanded with additional sensitivity analysis and discussion before final acceptance.

---

📊 Generated Publication Figures

Running generate-botijo-colab-figures.py outputs three vector PDF figures at 300 DPI using Matplotlib (pdf.fonttype = 42):

1. botijo_schematic_definitiu.pdf — Schematic geometry illustrating profile $r(z)$, water level $h(t)$, wetted wall area $S$, dry wall area $D$, and free liquid surface $A$.
2. botijo_optimal_shape.pdf — Optimal profile ($t_f = 2.86\ \text{h}$) compared against equal-volume cylindrical ($3.31\ \text{h}$) and spherical ($3.99\ \text{h}$) baselines, alongside the wheel-throwing bound ($r_M \le 0.15\ \text{m}$).
3. botijo_landscape.pdf — Cooling-time objective landscape over maximum radius $r_M$ and belly exponent $n$, illustrating the global-minimum basin and capacity-constraint boundary.

---

🚀 How to Run

1. Run in Google Colab

Click the Open in Colab badge above or open generate-botijo-colab-figures.py directly in Google Colab to execute and download all publication-ready PDF figures.

2. Run Locally

Prerequisites

Python 3.8+ and the required dependencies:

```bash
pip install numpy matplotlib
```

Generate Figures

```bash
python generate-botijo-colab-figures.py
```
---
## 💡 Key Results

| Vessel Geometry | Cooling Time ($39\,^\circ\text{C} \to 25\,^\circ\text{C}$) | Gain vs. Cylinder | Gain vs. Sphere |
| :--- | :---: | :---: | :---: |
| **Cylinder** ($R_c = 0.071\ \text{m}$) | $3.31\ \text{h}$ | — | $-17.1\%$ |
| **Truncated Sphere** ($R_s = 0.100\ \text{m}$) | $3.99\ \text{h}$ | $-20.6\%$ | — |
| **Optimal Botijo** ($r_b^{*} = 0.02\ \text{m}$, $r_M^{*} = 0.126\ \text{m}$, $n^{*} = 4.0$) | **$2.86\ \text{h}$** | **$+13.4\%$** | **$+28.2\%$** |

### Physical Mechanisms of the Optimal Shape

- **Narrow Base** ($r_b = 0.02\ \text{m}$): Minimizes dry-wall surface area near the bottom and isolates the base when resting on a table.
- **Wide Belly** ($r_M = 0.126\ \text{m}$): Maximizes wetted surface area $S$ during early cooling when water mass is highest, accelerating phase-change heat removal.
- **Narrow Neck** ($n = 4.0$): Restricts upper dry-wall area $D$ as the liquid level drops, minimizing parasitic heat gain from ambient air.


Physical Mechanisms of the Optimal Shape

· Narrow Base ($r_b = 0.02\ \text{m}$): Minimizes dry-wall surface area near the bottom and isolates the base when resting on a table.
· Wide Belly ($r_M = 0.126\ \text{m}$): Maximizes wetted surface area $S$ during early cooling when water mass is highest, accelerating phase-change heat removal.
· Narrow Neck ($n = 4.0$): Restricts upper dry-wall area $D$ as the liquid level drops, minimizing parasitic heat gain from ambient air.

---

📚 References

1. Zubizarreta, I., and G. Pinto. 1995. "The Botijo: A Traditional Method of Chilling Water." Chemical Engineering Education 29 (2): 104–108.
2. Ortega-Casanova, J., M. Ortega-Cortés, and P. Cortés-Carretero. 2021. "A Primitive Method for Cooling Water: Does the Shape Matter?" Case Studies in Thermal Engineering 26: 101022. https://doi.org/10.1016/j.csite.2021.101022


---

📄 License

Released under the MIT License. See LICENSE for details.


# AgeXtend::Mimetics — Minimal Demonstration

This repository provides a **minimal, fully reproducible demonstration** of how mechanism-aware computational models can be used to identify **caloric restriction mimetic (CRM) candidates** that are suitable for **experimental validation in aging biology assays**.

The demo mirrors the conceptual workflow used during my PhD work on AgeXtend and AgeXtend::Mimetics, where computational prioritization was explicitly designed to interface with **yeast, mammalian cell culture, and in vivo aging models**.

---

## 🧠 Scientific Motivation

Caloric restriction mimetics act through **distributed, conserved biological pathways** (e.g., AMPK, mTOR, autophagy), making them poorly suited to discovery approaches based solely on structural similarity.

This demo illustrates how:
- Chemical similarity can be decoupled from biological convergence
- Mechanism-aware prioritization enables **chemically novel yet biologically relevant** hits
- Computational outputs can be directly aligned with experimental testing constraints

---

## 🧪 Experimental Context

In the full research pipeline (not reproduced here), computationally prioritized compounds will eventually be validated using:
- **Yeast based assays**
- **_C. elegans_ lifespan and healthspan assays**

This repository demonstrates the *decision logic* that precedes such experiments.

---

## 🚀 Quickstart (Runs in < 2 minutes)

```bash
git clone https://github.com/sakshi327/agextend-mimetics-demo
cd agextend-mimetics-demo
conda env create -f environment.yml
conda activate agextend-mimetics
python demo.py
```
Outputs:
- ```results/ranked_hits.csv``` — prioritized CRM-like candidates
- ```figures/similarity_vs_bioactivity.png``` — chemical vs biological similarity
  
---

## 🔬 What This Demo Shows
✔ Bioactivity-aware molecular featurization<br>
✔ Dual similarity modeling (chemical vs biological)<br>
✔ Residual-based prioritization of candidates<br>
✔ Experiment-ready ranked outputs<br>

---

## 📂 Repository Structure
- ```src/``` — Core computational logic
- ```ata/``` — Small example dataset (synthetic/illustrative)
- ```results/``` — Ranked outputs
- ```figures/``` — Visualization for interpretation

---

## 📌 Notes
This repository is not intended to reproduce the full AgeXtend::Mimetics framework. Instead, it provides a clean, interpretable, and runnable example of how computational design decisions were made with downstream experimental validation in mind.

---

## 📫 Author
Sakshi Arora<br>
PhD — Computational Biology<br>
AI × Aging × Experimental Geroscience<br>

---




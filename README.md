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

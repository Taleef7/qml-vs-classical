# Quantum vs Classical ML on Tiny Datasets

This project compares simple classical ML models to a small quantum-kernel-based classifier built in Qiskit, on low-dimensional synthetic datasets.

## Goal

Show, on 2D toy problems, how a quantum classifier performs relative to:
- Logistic Regression
- SVC (RBF)

and discuss practicality (train time, data size).

## Datasets

All datasets are generated inside the notebook:
- `blobs` (almost linearly separable)
- `circles` (non-linear)
- `classification` (2 informative features)

Each dataset has 2 features → 2 qubits.

## Models

- **Classical**:
  - LogisticRegression
  - SVC (RBF)
- **Quantum**:
  - Hand-built quantum kernel using `ZZFeatureMap` (2 qubits, `reps=2`)
  - SVC with `kernel='precomputed'` on that quantum kernel
  - Trained on a small subset (e.g. 25 train / 10 test) to keep kernel construction feasible

## How to run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/qml_vs_classical.ipynb
```

## Team
- Taleef Tamsal
- Vaishnavi Panday
- John Ademola
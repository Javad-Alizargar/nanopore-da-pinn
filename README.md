# Data-assimilated PINN for nanopore biointerface electrostatics

This repository contains the code and small derived data needed to reproduce
benchmark tables for a short communication on data-assimilated
physics-informed neural networks (DA-PINNs) for charged solid-state nanopore
biointerfaces.

Manuscript files, cover letters, and submission-ready figure files are not
included in this public repository. Running the analysis script can regenerate
local figures for verification, but those generated figure files are ignored by
Git.

## Contents

- `src/nanopore_da_pinn.py` - finite-difference solver, DA-PINN models, current
  extraction, validation analyses, and figure generation.
- `data/` - generated CSV/NPY outputs used for reproducibility checks.
- `figures/` - local generated figure output directory, ignored by Git.
- `requirements.txt` - Python dependencies.

## Quick start

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
py -3.12 src\nanopore_da_pinn.py --epochs 2500
```

For a faster smoke test:

```bash
py -3.12 src\nanopore_da_pinn.py --epochs 200 --fast
```

## Reproduced analyses

1. Finite-difference ground truth for an axisymmetric solid-state nanopore.
2. DA-PINN prediction for a bound charged spherical inclusion.
3. Empty versus bound current comparison.
4. Voltage-conditioned DA-PINN I-V sweep from -200 mV to +200 mV.

## What is intentionally excluded

- Manuscript source files and compiled review PDFs.
- Cover letter, author declarations, and submission forms.
- Pre-rendered publication figures intended for journal upload.
- Any private or journal-submission-only materials.

## Citation

If this repository supports a manuscript or dataset release, cite the archived
version of the code and data using the DOI assigned by the repository or Zenodo.

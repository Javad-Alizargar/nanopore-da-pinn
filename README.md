# Nanopore DA-PINN Reproducibility Materials

This repository contains code, configuration files, numerical outputs, and
reproducibility scripts for a full-length manuscript on exact-boundary
data-assimilated physics-informed neural networks for coupled
Poisson--Nernst--Planck transport at charged nanopore biointerfaces.

The repository is intentionally limited to reproducibility materials. It does
not include the journal manuscript source files, cover letter, submission PDF,
or confidential submission package.

## Contents

- `src/pnp_da_pinn/` - PNP solvers, scaling utilities, PINN model, training,
  and metrics.
- `configs/` - YAML configurations for nanopore benchmark cases.
- `scripts/` - runnable scripts used to generate the numerical benchmarks,
  grid-refinement diagnostics, DA-PINN ablation, and surface-response sweep.
- `outputs/` - numerical outputs required to reproduce the reported tables and
  figures.
- `docs/` - method notes and project documentation.
- `requirements.txt` - Python dependencies.

## Environment

Python 3.12 was used for the reported runs.

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Main Reproduction Commands

Run from the repository root.

```powershell
py -3.12 scripts\run_charged_dev_benchmark.py surface_wall_0p036mC.yaml
py -3.12 scripts\run_grid_refinement.py surface_wall_0p036mC.yaml full
py -3.12 scripts\run_pinn_ablation.py surface_wall_0p036mC.yaml
py -3.12 scripts\run_surface_response_sweep.py quick
```

The benchmark scripts write CSV/NPZ/PNG outputs under `outputs/`.

## Key Outputs

- `outputs/charged_dev/surface_wall_0p036mC/charged_dev_metrics.csv`
- `outputs/charged_dev/surface_wall_0p036mC/charged_dev_fields.npz`
- `outputs/grid_refinement/surface_wall_0p036mC_full.csv`
- `outputs/ablation/surface_wall_0p036mC/pinn_ablation_metrics.csv`
- `outputs/surface_response/surface_response_sweep.csv`
- `outputs/surface_response/surface_response_fields.npz`

## Author

Javad Alizargar  
ORCID: https://orcid.org/0000-0003-2966-1315  
Department of Nursing, National Taipei University of Nursing and Health Sciences


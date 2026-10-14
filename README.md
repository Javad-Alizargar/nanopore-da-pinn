# Nanopore DA-PINN Reproducibility Materials

## Corrected revision v0.005

The v0.005 presentation update retains the v0.004 corrected numerical analysis.
It restores the author's original Figure 1 artwork with corrected data insets,
restores the original four Figure 5 panel topics, and moves wider sweeps to
Supplementary Figure S1. See `docs/figure_presentation_update.md` for details.

Use `outputs/revision/` and the commands below for the corrected numerical study.
The v0.003 SG flux reversed the drift sign relative to the stated Nernst-Planck
equations. Its numerical outputs and the bundled v0.003 ZIP are historical and
must not be used as validation of the corrected model. See
`docs/revision_corrections.md` for the correction and verification record.

```powershell
python -m unittest discover -s tests -v
python scripts/run_revision_validation.py --steps 500 --seeds 42 43 44
python scripts/audit_revision_outputs.py
python scripts/plot_revision_figures.py
```

The revision records Python/library versions and CPU details in
`outputs/revision/environment.json`. Use `requirements-revision.txt` for the
tested versions. Training uses float64 and two PyTorch CPU threads. All nine
fixed-budget runs, model weights, held-out-node metrics, independent diagnostics,
and figures are retained. Seed variation is descriptive, not a statistical
significance claim. The wall-adaptive variant changes the physics sampling
measure; initialization and data anchors are paired, but axial collocation draws
also differ. Parameter sweeps are reference solves, not surrogate generalization.

Field-evaluation latency excludes current calculation. Training and generating
reference data are additional costs. Cached reference interpolation is included
as a comparator; repeated evaluation of one known state does not require a new
PNP solve. No end-to-end acceleration or experimental validation is claimed.

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

## Historical v0.003 Environment

Python 3.12 was used for the reported runs.

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Historical v0.003 Commands

These commands document the earlier release, not the corrected revision.
Use the revision commands above for current results.

```powershell
py -3.12 scripts\run_charged_dev_benchmark.py surface_wall_0p036mC.yaml
py -3.12 scripts\run_grid_refinement.py surface_wall_0p036mC.yaml full
py -3.12 scripts\run_pinn_ablation.py surface_wall_0p036mC.yaml
py -3.12 scripts\run_surface_response_sweep.py quick
```

The benchmark scripts write CSV/NPZ/PNG outputs under `outputs/`.

## Historical Outputs Superseded by outputs/revision

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


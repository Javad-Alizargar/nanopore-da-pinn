# Derived reproducibility data

This directory contains small derived outputs from the reproducibility workflow:

- `benchmark_summary.csv` - empty, bound finite-difference, and bound DA-PINN current summary.
- `iv_curve_validation.csv` - finite-difference and voltage-conditioned DA-PINN I-V validation.
- `training_history_single_voltage.csv` - sparse training loss history for the 100 mV model.
- `training_history_voltage_conditioned.csv` - sparse training loss history for the voltage-conditioned model.
- `phi_fd_bound_100mV.npy` - finite-difference potential array for the 100 mV bound state.
- `phi_da_pinn_bound_100mV.npy` - DA-PINN potential array for the 100 mV bound state.

The manuscript text and journal-ready figures are intentionally not included.

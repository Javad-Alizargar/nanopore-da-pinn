# Superseded numerical outputs

All output directories other than `revision/` predate the v0.004 correction.
They are retained for provenance, not as validation of the corrected equations.
The original SG implementation reversed the drift sign. The corrected solver
also uses radial half control volumes, distinct ionic diffusivities in current,
and an independently recomputed strict convergence check. Old field errors,
current values, grid changes and timing comparisons must not be combined with
the corrected results. See `docs/revision_corrections.md`.

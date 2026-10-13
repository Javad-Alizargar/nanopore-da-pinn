# Corrected numerical revision v0.004

This version supersedes the numerical results in v0.003.

- Corrected the SG drift signs to agree with J_s = -(grad c_s + s c_s grad psi).
- Added a node-centred annular finite-volume reference with radial half cells,
  strict recomputed acceptance and separate species diffusivities in current.
- Added nine analytical/manufactured tests covering equilibrium, wall loading,
  Gauss balance, ionic fluxes, dimensional current and cylindrical-axis limits.
- Recomputed reference fields, four-grid/tolerance studies and 16 sweep entries.
- Added wall/axis penalties and nine fixed-budget neural runs across three seeds.
- Archived model weights, held-out/volume errors, independent differential and
  boundary residuals, timing with cached interpolation, and all figure scripts.

Data assimilation reduces mean charge relative error from approximately 1.02 to
0.145 in this fixed-budget comparison; mean current-profile error changes from
0.00233 to 0.00102. Wall adaptation is not uniformly better. Neural wall and
differential residuals remain substantially larger than those of the reference.
The models are fixed-state interpolants; no parameter generalization,
experimental validation or end-to-end acceleration over caching is claimed.

All corrected results are under `outputs/revision/`. Historical folders and the
bundled v0.003 ZIP are retained for provenance and labeled as superseded. The
previous Zenodo DOI does not archive this revision.

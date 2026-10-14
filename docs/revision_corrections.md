# Numerical corrections in v0.004

The previous SG implementation used the opposite migration sign to the stated
flux J_s = -(grad c_s + s c_s grad psi). A positive potential drop consequently
gave cation flux of the wrong sign, and a Boltzmann equilibrium produced nonzero
flux. The corrected face expression is

J_s,ij = [B(delta)c_s,i - B(-delta)c_s,j]/h, delta=s(psi_j-psi_i).

`conservative.py` implements the corrected reference using all radial nodes as
control-volume unknowns, including half volumes at the axis and charged wall.
Only axial reservoir degrees of freedom are eliminated. The Poisson wall load
is alpha_r*q_w/w_last. Species diffusivities cancel from the steady concentration
equations but are retained separately when converting the flux to amperes.
The legacy SG helper signs are also corrected; the new validation runner uses
the new conservative module, not the historical continuation workflow.

Acceptance uses the maximum potential fixed-point correction below 1e-9,
finite fields and positive concentrations. This is a preconditioned residual,
not a claim of 1e-9 solution accuracy. The raw and diagonal-scaled algebraic
residuals, individual species flux balances and mesh/tolerance studies provide
additional checks. Failed solves raise an error and are never plotted as
accepted sweep points. At zero voltage the absolute current range is reported;
a relative current-conservation error is undefined and is recorded as NaN.

The original physics-only neural training omitted wall/axis conditions. The
revision adds these terms. It compares fixed-budget models, not converged
optimizers, with identical initialization/data seeds. The adaptive variant
deliberately overweights the outer radial region and uses a different axial
collocation draw. Results cannot isolate a radial-sampling effect alone.
Wall losses use 128 points between z=0.01 and 0.99; the untrained near-corner
intervals are evaluated separately on dense independent boundary points.
Mixed reservoir/wall corners limit smooth-ansatz regularity. No exact wall
enforcement is claimed: only the reservoir Dirichlet values are exact.

Nine automated tests cover Boltzmann zero flux, the neutral analytical Ohmic
solution, charged equilibrium response, a manufactured radial quadratic Poisson
solution, Gauss balance, separate ionic conservation, distinct-diffusivity
current conversion, recomputed salt scaling, and the analytic cylindrical-axis
limit (some checks share a test). These tests do not constitute experimental
validation. The continuum PNP model omits steric correlations, variable
permittivity, access resistance and molecular binding kinetics.

The radius sweep holds dimensionless q_w fixed, so dimensional surface charge
varies inversely with radius; both quantities are saved. Field errors are
reported as unweighted nodal norms and separately as cylindrical-volume norms.
Grid comparisons to 41 x 121 use interpolation and do not assert formal
convergence order or an exact continuum solution.

Use the v0.006 tag/commit for revised figures with unchanged v0.004 results. The prior Zenodo archive and
v0.003 release identify historical materials only; no updated Zenodo DOI is
claimed by this revision.

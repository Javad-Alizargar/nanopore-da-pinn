# Full-Length Article Strategy

## Required novelty beyond the Short Communication

The Short Communication demonstrated a DA-PINN for a Poisson-only electrostatic
nanopore model. The full-length article must not be a longer version of that
work. It should focus on coupled electro-diffusive transport at charged
solid-liquid biointerfaces.

Core differentiators:

1. Coupled PNP model with \(\phi\), \(c_+\), \(c_-\), and ion flux.
2. Current computed from Nernst-Planck flux.
3. Demonstrated standard PINN failure or instability under stiff regimes.
4. DA-PINN stabilization using sparse numerical assimilation.
5. Surface/biointerface maps: voltage, Debye length, pore radius, surface
   potential or fixed charge, and biomolecular inclusion position.
6. Flux conservation and current continuity metrics.

## Claims to avoid

- Do not say standard PINNs fail universally.
- Do not imply clinical validation.
- Do not frame this as only an AI acceleration paper.
- Do not reuse the Short Communication's Poisson-only result as the main
  novelty.

## Better core claim

Exact-boundary, data-assimilated PINNs can stabilize stiff coupled PNP transport
in charged nanopore biointerfaces while preserving flux-derived current with
quantified conservation error.

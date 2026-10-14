# Figure presentation update v0.005

The author requested preservation of the submitted Figure 1 workflow design and
Figure 5 panel topics. This update changes presentation only: reference arrays,
trained weights, numerical CSV tables and scientific conclusions are unchanged
from v0.004. Historical v0.003 numerical graphics must not be reused as results.

## Figure 1

- A: original cylindrical pore artwork retained. External reservoirs are schematic.
- B: original discretization artwork retained; the three field thumbnails now
  use corrected reference arrays. Verification labels replace "ground truth".
- C: corrected cation-excess background and the actual saved 500 seed-42 anchors;
  the 39% fraction of the 1281-node grid is explicit.
- D: original network artwork retained as a schematic, not a literal layer/unit
  count. Labels specify four 64-unit SiLU hidden layers, exact reservoir values
  and soft wall/axis terms plus field/charge assimilation.
- E: old hourglass plots and numerical badges replaced by corrected cylindrical
  fields and SG-derived seed-42 current. Timing is 1.366 ms for full-field
  evaluation only, excluding current postprocessing and training.

The PNG source artwork is retained in assets for deterministic reproduction.
The final PDF combines raster artwork with vector/data overlays; it is not
entirely vector artwork. The numerical overlays are plotted directly from saved
arrays, not synthesized by an image model. The manuscript caption distinguishes
schematics, qualitative thumbnails and quantitative panels.

## Figure 5

- A: corrected current-voltage curve for -50 to 50 mV.
- B: near-wall cation enrichment relative to the neutral-wall result for
  q_w = 0, -0.001, -0.005 and -0.01 at 50 mV. Average over r >= 0.8 nodes.
- C: corrected cation field at q_w = -0.01 minus the neutral-wall field at 50 mV.
  The diverging colour scale is symmetric; it does not imply negative changes.
- D: fixed-point residual and relative current nonuniformity for those same
  four charge cases, with the 1e-9 acceptance threshold identified separately.

Supplementary Figure S1 retains the extended charge, salt and radius sweeps.
Six main figures remain; Figures 2, 3, 4 and 6 are unchanged from v0.004.
Manuscript captions, discussion, supplementary information and reviewer
responses have been updated outside this public code repository.

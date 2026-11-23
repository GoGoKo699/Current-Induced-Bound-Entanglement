# Reproduction and evidence limits

## Run the checks

Use Python 3.11 or later with the pinned packages:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py
python verification/check_structure.py
```

The scientific script writes `verification/results.json`. The structure script prints its report. Runtime checks raise exceptions explicitly and remain active under `python -O`. Both sampled families use fixed seeds.

## Independent scientific paths

`check_science.py` constructs the full GKSL superoperator from jump matrices, exponentiates it, and reconstructs the normalized output-first Choi state from matrix units. It uses this independent calculation to check the analytical channel.

The cycle check covers 126 combinations of signed bias, dephasing and time. It checks the oriented propagator, Choi matrix, trace and positivity, partial-transpose eigenvalues, realignment norm and population singular values. It includes zero time, both circulation directions, zero bias and dephasing rate $`\gamma=1/2`$.

The static Bell-slice check reconstructs 680 states from a finite average of product states and residual basis populations. The independent target uses all nine Bell vectors. Cases cover both signs of the coherence, vanishing populations, points on physical and separability boundaries, and sampled interiors. An additional 126 states check that partial transpose or realignment detects entanglement outside the exact separable region.

The onset check covers 53 pairs of bias and dephasing rate. It reconstructs the full GKSL Choi state from the product decomposition at the predicted entanglement-breaking time and checks for entanglement immediately before it by partial transpose or realignment. It includes both sides of the critical dephasing curve, the curve itself, and zero bias. The samples extend through $`\gamma=10`$.

The reversible check covers 36 cases in dimensions two through five with nonuniform stationary probabilities, diagonal noise and nonzero Hamiltonian energies. It tests propagated detailed balance, the closed Choi form, nonnegative Gaussian Gram factors via Gauss–Hermite quadrature, and residual population weights when PPT holds. Failed PPT pairs are projected onto two-qubit states and checked for NPT. A disconnected model checks the finite-time obstruction separately.

The weak-current check uses 70-decimal-digit arithmetic to compare the quadratic opening at zero dephasing and the fourth-order opening at $`\gamma=1/2`$. High precision resolves gaps at small current that double-precision subtraction would obscure.

## Recorded output

[results.json](results.json) records the environment and outputs. In the recorded run, the largest full-Choi discrepancy was below $`1.5\times10^{-15}`$. The product-reconstruction errors were below $`4.2\times10^{-16}`$ for the static states and $`2.8\times10^{-16}`$ at the dynamical onsets. Floating-point last digits can vary across BLAS platforms. The scripts check against numerical tolerances.

For maximal bias, no added dephasing and time $`1.25`$, the partial-transpose minimum eigenvalue is approximately $`0.0041234967`$ and realignment norm approximately $`1.0085795716`$. The root finder and high-precision expansion reproduce the values in [the cycle analysis](../science/cycle.md).

`check_science.py` is the principal reproduction route. `check_cycle.py` also provides a compact cycle smoke test.

## Evidence limits

The finite tests check the implementations. The [analytical proofs](../science/README.md) establish the full separability region and the cycle thresholds. For the reversible theorem, the exact Gaussian integral and the closed nonnegative-factorization cone justify the finite decomposition.

`check_structure.py` validates local navigation, the 30-milestone dependency order and required reader routes. Hosted review checks the mathematics displayed by GitHub on the exact integrated revision.

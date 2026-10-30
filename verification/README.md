# Reproduction and evidence limits

## Run the checks

Use Python 3.11 or later with the pinned packages:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py
python verification/check_structure.py
```

The scientific script writes `verification/results.json`; the structure script prints its report. Runtime checks raise exceptions explicitly and remain active under `python -O`. No random sample changes between runs: the reversible family uses a fixed seed.

## Independent scientific paths

`check_science.py` constructs the full GKSL superoperator from jump matrices, exponentiates it, and reconstructs the normalized output-first Choi state from matrix units. It compares this with the analytical channel, not merely with a second implementation of the same closed Choi formula.

The cycle check covers 126 combinations of signed bias, dephasing and time. It checks the oriented propagator, Choi matrix, trace and positivity, partial-transpose eigenvalues, realignment norm and population singular values. It includes zero time, both circulation directions, zero bias and the dephasing endpoint.

The reversible check covers 36 cases in dimensions two through five with nonuniform stationary probabilities, diagonal noise and nonzero Hamiltonian energies. It tests propagated detailed balance, the closed Choi form, nonnegative Gaussian Gram factors via Gauss–Hermite quadrature, and residual population weights when PPT holds. Failed PPT pairs are projected onto two-qubit states and checked for NPT. A disconnected model checks the finite-time obstruction separately.

The weak-current check uses 70-decimal-digit arithmetic to compare the quadratic opening at zero dephasing and the fourth-order opening at the dephasing endpoint. This avoids using double-precision subtraction to certify an arbitrarily tiny gap.

## Recorded output

[results.json](results.json) records the environment and actual outputs. In the recorded run, the largest full-Choi discrepancy was below $`1.5\times10^{-15}`$, the largest realignment discrepancy below $`9\times10^{-16}`$, and the population singular-value discrepancy below $`4\times10^{-15}`$. Floating-point last digits can vary across BLAS platforms; the executable tolerances, not byte-for-byte equality of numerical output, define the checks.

For maximal bias, no added dephasing and time $`1.25`$, the partial-transpose minimum eigenvalue is approximately $`0.0041234967`$ and realignment norm approximately $`1.0085795716`$. The root finder and high-precision expansion reproduce the values in [the cycle analysis](../science/cycle.md).

`check_cycle.py` is the earlier compact cycle smoke test. The expanded `check_science.py` is the principal reproduction route.

## What these checks do not establish

Finite tests do not prove the all-time theorem or the every-nonzero-bias statement. The analytical arguments are in [science](../science/README.md). Nonnegative quadrature factors are an implementation check, not a replacement for the exact Gaussian integral and closed-cone argument. Witness failure does not prove separability. No exact biased EB time or capacity-rate formula is computed.

`check_structure.py` validates local navigation, the 30-milestone dependency order and required reader routes. It does not inspect hosted mathematical rendering. Local TeX compilation and passing science tests likewise do not certify what GitHub displays. Hosted review must be performed on the exact integrated revision and reported separately.

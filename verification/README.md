# Reproducibility and audit boundaries

The pre-repository exploration performed two independent checks: an analytical adversarial proof audit of the reversible decomposition and communication corollary, and an independent full-GKSL reconstruction of the biased cycle by matrix exponentiation, Choi assembly from matrix units, partial transpose and realignment. The source scripts and JSON outputs were preserved in the private exploration archive, not copied into this repository yet.

**Analytical assertions to verify independently:** for reversible `Q`, the nonnegative Gaussian Gram factorization and explicitly tilted diagonal-twirl decomposition; for the cycle, the closed population propagator, bias-independent singular values, PPT determinant, realignment norm, and strict inequality at `t_*`.

**Expected finite-check examples from the exploration:** for `gamma=0` and `eta=1`, `t_PPT=1.2174450174206943`; the realignment norm at that PPT threshold is `1.0326572307`. At `t=1.25`, the PPT determinant is positive while the realignment norm is `1.0085795716>1`.

A finite numerical check tests selected inputs only and cannot prove an all-times theorem, a universal novelty claim, or the exact biased EB onset. The saved independent audit reports no fatal algebraic mismatch within its checked scope. Further reproducibility integration and source-script inclusion remain necessary before scientific-integration completion.
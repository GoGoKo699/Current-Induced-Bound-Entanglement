# Current-Induced Bound Entanglement

**Physical question.** When does a memoryless quantum evolution cease to distribute distillable entanglement, and when does it destroy *all* entanglement? Can microscopic probability currents separate these transitions without changing the relaxation rates?

For finite-dimensional resolved-transition Lindblad dynamics with diagonal Hamiltonian and Hermitian diagonal dephasing, **classical detailed balance forces the PPT and entanglement-breaking (EB) channel thresholds to coincide at every time**. A three-state cycle with arbitrary nonzero circulation breaks that equality: at fixed coherence attenuation and fixed singular values of the population propagator, a strictly PPT yet entangled Choi state appears during a nonempty time interval. This is a loss of distillability, **not** an improvement in quantum communication or proof of longer entanglement lifetime.

## Results

1. **Reversible theorem.** If the classical population generator has a faithful detailed-balance distribution, the channel is PPT if and only if it is EB, for every finite time, including reducible cases where both thresholds may remain infinite. [Model and theorem](science/model.md), [separable decomposition](science/reversible_proof.md).
2. **Current-driven counterfamily.** For a qutrit cycle with normalized clockwise/counterclockwise rates and bias `eta`, every `eta != 0` admits a PPT-entangled time window when uniform dephasing `0 <= gamma <= 1/2`. The current-free onset is `t* = 1.26188944840409...` for `gamma=0`; the opening at small bias is `t* - t_PPT = 0.0391427404381 eta^2 + O(eta^4)`. [Cycle derivation](science/cycle.md).
3. **Operational distinction.** For the entire structured Choi class, a non-PPT channel has a distillable two-qubit projection, while a PPT channel has zero two-way assisted quantum capacity. Thus the PPT onset is exactly the sign threshold of two-way-assisted quantum capacity, though no capacity value or useful rate is computed. [Communication interpretation](science/operational.md).

## Read and verify

- [Science route](science/README.md) leads to exact model, proofs, cycle, operational meaning and boundaries.
- [Related work](references/RELATED_WORK.md) separates inherited PCP/CLDUI separability techniques and PPT/realignment witnesses from the dynamical contribution.
- [Reproduction](verification/README.md) describes the independent full-Lindblad audit and its limits.
- The selected educational source and project-defined 30 milestones will be integrated **after the author selects the anchor**; no coaching records belong here.

## Boundaries

The result does not cover generic Davies generators with unresolved degenerate Bohr-frequency sectors, non-Hermitian diagonal dissipators, arbitrary population graphs under circulation, or a proved exact EB time in the biased cycle. A PPT-entangled Choi state is bound entangled and has no two-way distillable entanglement, but this result does not determine private capacity, unassisted capacity or secure-key rates. The reversible theorem uses established matrix-cone technology; novelty rests on the all-time dynamical consequence and its matched current-driven contrast.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

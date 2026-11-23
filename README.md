# Current-Induced Bound Entanglement

**When does memoryless noise stop distributing distillable entanglement, and when does it destroy all entanglement?** In a resolved-transition Lindblad model, detailed balance makes these thresholds coincide. For a circulating three-level system, a critical dephasing rate decides whether the thresholds split or move together, at fixed coherence attenuation and population singular-value decay.

## Main results

**Reversibility.** For a finite system with separate rank-one population-transition jumps, diagonal Hamiltonian, Hermitian diagonal dephasing, and a faithful detailed-balance distribution,

```math
\Phi_t\text{ is PPT}\quad\Longleftrightarrow\quad
\Phi_t\text{ is entanglement breaking}.
```

This holds at every finite time. The [constructive proof](science/reversible_proof.md) gives a separable Choi decomposition. The equivalence does not require irreducibility; both onset times can be infinite in disconnected models.

**Circulation.** A qutrit cycle with forward and backward rates $`a,b`$, bias $`\eta=(a-b)/(a+b)`$, and dimensionless uniform dephasing $`\gamma\ge0`$ has the exact entanglement-breaking time

```math
t_{\rm EB}(\eta,\gamma)=\max\{t_{\rm PPT}(\eta,\gamma),t_*(\gamma)\}.
```

Here $`t_*`$ is the time when the matched reversible cycle loses all entanglement. At nonzero bias, below the critical dephasing rate $`\gamma_c(\eta)`$, distillability ends earlier and the remaining entanglement survives exactly to $`t_*`$. Above that rate, both lifetimes increase and their onsets coincide. The comparison holds the outgoing rate, coherence attenuation and population singular-value decay fixed.

**Separability.** In the [three-parameter cyclic qutrit slice](science/separability.md), PPT and the realignment test together characterize separability. A mixture of two twirled product states and basis products gives an explicit separable decomposition whenever both tests pass.

**Communication meaning.** In the whole structured Choi class, non-PPT implies a distillable local two-qubit projection. Therefore the PPT onset is exactly the positive-to-zero boundary of two-way assisted quantum capacity. This [capacity-sign result](science/operational.md) is not a capacity formula.

## A concrete scale

With no additional dephasing and time measured in units of $`(a+b)^{-1}`$,

```math
\begin{aligned}
t_*&=1.26188944840409\ldots,\\
t_*-t_{\rm PPT}&=0.0391427404380864\ldots\,\eta^2+O(\eta^4).
\end{aligned}
```

For maximal bias at time $`1.25`$, the Choi partial transpose has minimum eigenvalue $`0.0041234967\ldots>0`$ while the realignment norm is $`1.0085795716\ldots>1`$. Entanglement survives, but it is bound rather than distillable.

For maximal bias, the dephasing crossover occurs at $`\gamma_c(1)=0.7186185654\ldots`$. At $`\gamma=1`$ both biased thresholds are $`0.7552131478\ldots`$, compared with $`0.7467471159\ldots`$ for the reversible channel at the same dephasing rate.

## Reading routes

| Question | Route |
|---|---|
| What is the exact model, normalization and theorem? | [Model](science/model.md) |
| Why does detailed balance make PPT sufficient? | [Reversible proof](science/reversible_proof.md) |
| How do circulation and dephasing set the two lifetimes? | [Cycle and critical dephasing](science/cycle.md) |
| Why are PPT and realignment jointly sufficient in the qutrit slice? | [Product-state decomposition](science/separability.md) |
| Which operational capability ends? | [Two-way communication](science/operational.md) |
| Which claims do not follow? | [Scope and limiting examples](science/limitations.md) |
| What is inherited from earlier work? | [Related work](references/RELATED_WORK.md), [bibliography](references/references.bib) |

The [science entrypoint](science/README.md) connects these pages. [llms.txt](llms.txt) maps questions to authoritative files.

## Learning route

The single educational anchor is **Rivas–Huelga, Open Quantum Systems: An Introduction**. The [source bridge](learning/ANCHOR_BRIDGE.md) pairs book chapters with the open preprint's different section numbering and supplies the specialized entanglement bridge. Start with the [worked tutorial](learning/TUTORIAL.md) and [30-milestone map](learning/MILESTONES.md): 12 background/preliminaries targets followed by 18 narrative/innovation targets. The map is shared scientific material, not a personal assessment record.

## Reproduce

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py
python verification/check_structure.py
```

The [verification guide](verification/README.md) covers full-superoperator comparisons, separable qutrit decompositions, both dynamical onsets, and high-precision weak-bias tests. The [recorded results](verification/results.json) distinguish finite computation from analytical proof.

## Scope

The exact current-dependent phase diagram uses independently resolved jumps on a three-level cycle and uniform dephasing. The reversible theorem applies more broadly within the specified resolved-transition model. The two-way capacity result fixes the sign of the capacity, and the [related-work account](references/RELATED_WORK.md) identifies the inherited ingredients and preceding static results.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

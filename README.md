# Current-Induced Bound Entanglement

**When does memoryless noise stop distributing distillable entanglement, and when does it destroy all entanglement?** In a resolved-transition Lindblad model, detailed balance makes these thresholds coincide. A circulating three-level system separates them even when coherence attenuation and population contraction singular values are held fixed.

## Main results

**Reversibility.** For a finite system with separate rank-one population-transition jumps, diagonal Hamiltonian, Hermitian diagonal dephasing, and a faithful detailed-balance distribution,

```math
\Phi_t\text{ is PPT}\quad\Longleftrightarrow\quad
\Phi_t\text{ is entanglement breaking}.
```

This holds at every finite time. The [constructive proof](science/reversible_proof.md) gives a separable Choi decomposition. The equivalence does not require irreducibility; both onset times can be infinite in disconnected models.

**Circulation.** A qutrit cycle with forward/backward rates $`a,b`$, bias $`\eta=(a-b)/(a+b)`$, and dimensionless uniform dephasing $`\gamma`$ obeys

```math
t_{\rm PPT}(\eta,\gamma)\lt t_*(\gamma)\le t_{\rm EB}(\eta,\gamma)
\qquad(0\lt|\eta|\le1,\ 0\le\gamma\le1/2).
```

Here $`t_*`$ is the exact common threshold of the current-free reference. Every nonzero bias opens a **PPT-entangled Choi interval**, certified by realignment. The [cycle analysis](science/cycle.md) holds the outgoing rate, coherence attenuation and population singular-value decay fixed; the full complex spectrum is not fixed.

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

## Reading routes

| Question | Route |
|---|---|
| What is the exact model, normalization and theorem? | [Model](science/model.md) |
| Why does detailed balance make PPT sufficient? | [Reversible proof](science/reversible_proof.md) |
| How does the stationary current create the contrasting interval? | [Cycle and weak-bias law](science/cycle.md) |
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

The [verification guide](verification/README.md) explains full-superoperator comparisons, reversible Gram/decomposition checks, a disconnected example, and high-precision weak-bias tests. The [recorded results](verification/results.json) distinguish finite computation from analytical proof.

## Scope

This is not a theorem about arbitrary Davies or Lindblad generators, arbitrary population graphs with currents, or all definitions of quantum detailed balance. The exact biased entanglement-breaking time remains undetermined. The effect establishes earlier loss of distillability with residual bound entanglement, **not** a demonstrated increase in total entanglement lifetime or a useful storage advantage. Necessary matrix-cone, separability, realignment and distillation results are attributed to prior work.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

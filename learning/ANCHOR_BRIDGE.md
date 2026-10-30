# Rivas–Huelga: source-to-project bridge

The **single educational anchor** is Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction*, SpringerBriefs in Physics, first edition, copyright 2012, DOI [10.1007/978-3-642-23354-8](https://doi.org/10.1007/978-3-642-23354-8). The authors' open version is [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), dated 9 February 2012. These are two versions of the same anchor, not two prerequisites.

## Edition and section map

The preprint has an introductory section before the mathematical material, so its main section numbers are one greater than the book's corresponding chapter numbers. Page numbers also differ. Use the following paired references rather than silently applying one edition's numbering to the other.

| Purpose in this project | Published book | Open preprint v2 |
|---|---|---|
| Norms, exponentials and semigroup composition | Chapter 1, especially 1.1–1.3 | Sections 2.1–2.3 |
| Hamiltonian phase evolution | Chapter 2 | Section 3 |
| Physical dynamical maps, complete positivity and contraction | Chapter 3, especially 3.1–3.3 | Sections 4.1–4.3 |
| Markovian temporal composition | Section 3.5 | Section 4.5 |
| Classical rate matrices | Section 4.1 | Section 5.1 |
| Differential generators and positivity conditions | Sections 4.2–4.3 | Sections 5.2–5.3 |
| Stationary states of time-homogeneous evolution | Section 4.4 | Section 5.4 |
| Weak-coupling context and the limits of a resolved-jump model | Chapter 5, especially 5.2.1, 5.2.3, 5.2.6 and 5.2.8 | Sections 6.2.1, 6.2.3, 6.2.6 and 6.2.8 |

Bibliographic identity and the book chapter sequence were checked against the publisher; preprint subsection numbering was checked against its contents. The book's non-Markovian chapter is not needed for this time-independent semigroup result. Reading the whole book is not a prerequisite.

## Conventions to translate

The project uses a time-homogeneous channel $`\Phi_t=e^{t\mathcal L}`$ and sets $`\hbar=1`$. Its populations are **columns**: $`\dot p=Qp`$ and $`Q_{ij}`$ means a transition from $`j`$ to $`i`$. Compare the action of an indexed rate before copying a generator from another convention.

The jump operator for that transition is $`\sqrt{Q_{ij}}|i\rangle\langle j|`$. A Hermitian diagonal dissipator satisfies

```math
V\rho V-\tfrac12\{V^2,\rho\}=-\tfrac12[V,[V,\rho]].
```

Its entries damp the $`i,j`$ coherence according to the squared difference of diagonal noise amplitudes. The Hamiltonian contributes a removable phase for the entanglement tests considered here.

The normalized Choi state is $`\rho_t=(\Phi_t\otimes\mathrm{id})(|\Omega_d\rangle\langle\Omega_d|)`$, with output first. The unnormalized operator is $`J_t=d\rho_t`$. Realignment is evaluated on $`\rho_t`$, not $`J_t`$, so its separability bound is one.

In the cycle, the physical outgoing rate is $`a+b`$. The displayed time is physical time multiplied by that rate, and $`\gamma`$ is the physical dephasing rate divided by it. No rate or energy resource is implicitly being varied when the dimensionless bias is changed at fixed outgoing rate.

## What the anchor supplies, and what is supplied here

The anchor supplies the open-system language, quantum dynamical maps, time-homogeneous generators, and classical/quantum Markov comparison. It gives context for distinguishing a microscopic derivation from the particular generator imposed in this project.

The project supplies the remaining bridge: [Choi and partial-transpose conventions](../science/model.md), [the nonnegative Gaussian factorization and separable tilt](../science/reversible_proof.md), [the circulating qutrit and witness calculation](../science/cycle.md), and [the distillation/capacity argument](../science/operational.md). The anchor is not being cited as a proof of these new dynamical statements, or as the source of the imported matrix-cone and distillation theorems. Those research dependencies are attributed separately in [related work](../references/RELATED_WORK.md).

## A route through the project

Read the [worked tutorial](TUTORIAL.md) first. Use the [30-milestone map](MILESTONES.md) to connect the anchor's dynamics to the channel-level question. The first 12 milestones assemble a common background; the remaining 18 build the argument from its local ingredients to its physical and operational meaning. Specialist proofs remain directly accessible through [science](../science/README.md).

# Scope, boundaries, and limiting examples

## The model is a substantive restriction

Every transition has its own rank-one jump, the Hamiltonian is diagonal, and diagonal dephasing operators are Hermitian. A generic Davies generator with degenerate transition frequencies may mix coherence sectors; a complex diagonal jump may introduce phases that are not Hamiltonian differences. Neither is covered simply by calling the noise “Markovian” or “thermal.”

Detailed balance is classical reversibility of the specified population generator with a strictly positive stationary vector. The theorem is not a statement about all definitions of quantum detailed balance or all thermal channels.

## Finite and infinite onset

An irreducible reversible finite generator has strictly positive limiting transition probabilities and decaying coherences, so its common PPT/EB threshold is finite. In contrast, consider two disconnected recurrent components. For levels in different components, both cross-transition probabilities vanish while their finite-time coherence factor remains positive. Their PPT block is negative at every finite time. Both thresholds are infinite, consistent with the all-time equivalence.

Pure finite-rate dephasing with no population transfer is another example: each off-diagonal coherence is nonzero at finite time, so a channel of dimension at least two is never PPT at a finite time, despite becoming completely dephased asymptotically.

## What circulation establishes

The all-nonzero-bias claim is for the three-level cycle and the sufficient range of uniform dephasing from zero through one half in normalized rate units. It is not a universal theorem that every stationary current in every population graph creates bound entanglement. No assertion is made outside this proved range.

Realignment gives a certified interval ending at the reversible reference threshold. It does not locate the exact biased EB onset. The width shrinks to zero as the current vanishes; the fourth-order dephasing endpoint is particularly delicate numerically. No fixed experimental resolution, robust finite-rate advantage, or improved total storage lifetime is established.

## Evidence and interpretation

The proofs establish universal statements in their specified models. Finite numerical checks independently test implementation, conventions, limiting cases and selected coefficients. They neither certify priority nor determine separability from failure of a witness. The [related-work account](../references/RELATED_WORK.md) distinguishes inherited ingredients from the proposed dynamical contribution.

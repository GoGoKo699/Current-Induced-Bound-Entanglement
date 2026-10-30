# Related work and attribution

The result uses established channel, entanglement and matrix-cone machinery. Its proposed contribution is a dynamical statement: an all-time reversibility boundary in a specified resolved-transition model, a matched arbitrary-small-current counterfamily, and the operational meaning of the PPT onset. Neither a new static PPT-entangled state nor a new separability criterion is claimed.

## Imported ingredients

| Ingredient | Primary source | Use here |
|---|---|---|
| Separable Choi state iff entanglement-breaking channel | Horodecki, Shor and Ruskai, [quant-ph/0302031](https://arxiv.org/abs/quant-ph/0302031) | Converts separability into an all-input statement |
| Pairwise completely positive matrices and diagonal-unitary-invariant states | Johnston and MacLean, [1807.06897](https://arxiv.org/abs/1807.06897); Singh and Nechita, [2010.07898](https://arxiv.org/abs/2010.07898) | Nonnegative factors, product-state twirling, structured PPT tests |
| Realignment separability criterion | Chen and Wu, [quant-ph/0205017](https://arxiv.org/abs/quant-ph/0205017) | Certifies entanglement when the normalized trace norm exceeds one |
| Distillability of entangled two-qubit states | Horodecki, Horodecki and Horodecki, [quant-ph/9607009](https://arxiv.org/abs/quant-ph/9607009) | Converts a negative pair block into positive two-way capacity |
| PPT nondistillability | Horodecki, Horodecki and Horodecki, [quant-ph/9801069](https://arxiv.org/abs/quant-ph/9801069) | Bound-entanglement interpretation and PPT protocol converse |

The complete positivity of a matrix with nonnegative Gram factors is a matrix-cone property, not a second use of the quantum-channel definition. The reversible proof explicitly constructs the required product decomposition; it does not assume that an arbitrary positive matrix has nonnegative factors.

## Nearest dynamical comparisons

Roga, Fannes and Życzkowski, [Davies maps for qubits and qutrits](https://arxiv.org/abs/0911.5607), provide an important structural comparison. Our independently resolved jumps are explicit hypotheses. A generic Davies generator with unresolved degenerate-frequency sectors need not have this Choi structure.

Hanson, Rouzé and Stilck França, [1902.08173](https://arxiv.org/abs/1902.08173), characterize eventual entanglement breaking in Markovian dynamics. Szczygielski and Chruściński, [2407.16583v2](https://arxiv.org/abs/2407.16583v2), study eventual EB and divisibility, including related diagonal models. Eventual EB establishes late-time behavior; it does not by itself identify the **first PPT time** with the first EB time. The latter equality, proved constructively at every time under the present hypotheses, is the relevant distinction.

Duvenhage and Snyman, [Detailed balance and entanglement](https://arxiv.org/abs/1407.0520), concern detailed-balance dualities and entangled-state formulations. Singh, Datta and Nechita, [2206.01145](https://arxiv.org/abs/2206.01145), study ergodicity of diagonal orthogonal covariant channels. Shared structure or terminology does not substitute for a threshold theorem under the same assumptions.

## Circulant, Weyl and chosen-input precedents

Chruściński and Kossakowski, [0705.3534](https://arxiv.org/abs/0705.3534), supply static circulant-state structure. Shahbeigi and coauthors, [2003.12184](https://arxiv.org/abs/2003.12184), establish Weyl-channel semigroup embeddability and Fourier structure in a containing class. These constructions and spectral methods are inherited; embedding a static state in a named family alone is not the contribution.

Song, Chen and Zhu, [0904.4847](https://arxiv.org/abs/0904.4847), study loss of distillability under local decoherence for chosen mixed entangled inputs. Such a free-to-bound transition can occur without contradicting an all-input channel theorem: the channel can remain non-PPT while that particular input has become bound entangled. Here the path starts at the identity channel and is tested by its Choi state.

## Recent qutrit comparisons and limits of the search

Sacchi's [sparse anisotropic positive maps](https://arxiv.org/abs/2607.12470), published in Physical Review A 114, 042455 (2026), retain selected coherence sectors and erase another. The uniform completely positive slice is a different, singular channel family, whereas a finite-time matrix exponential is invertible as a linear map. Its sparse edge-state geometry does not identify the present semigroup's biased EB time.

The exploration also compared Ali's [2609.39141v1](https://arxiv.org/abs/2609.39141v1) against the full-rank cyclic Choi family: the recorded comparison identifies an extra diagonal component in our state and failure of the proposed positive-map witness near the weak-current crossing. A fresh full-text retrieval of that source was unavailable during furnishing, so that comparison remains an explicitly carried-forward, bounded exploration observation rather than a new full-text verification. Neither source supplies a premise used by the present proofs.

The targeted comparison covers the inherited ingredients and nearby dynamical/static models; it is not an exhaustive priority certificate. The full author preprint of the Weyl-channel work was inspected in exploration, not its unavailable published PDF. The exact biased EB onset is not credited as a result.

## What remains after subtraction

The all-time resolved-transition reversibility theorem uses known cone technology to make PPT sufficient for EB. The qutrit family shows that every nonzero circulation bias can separate those properties while preserving specified damping diagnostics. The special pair-block structure gives an exact positive-versus-zero two-way-capacity boundary without assuming arbitrary NPT distillability. These are the claims to compare, rather than the novelty of their static tests or notation.

The selected [Rivas–Huelga educational anchor](../learning/ANCHOR_BRIDGE.md) supports entry into the dynamics; the primary research references above remain necessary for attribution. The [structured bibliography](references.bib) records stable source identifiers.

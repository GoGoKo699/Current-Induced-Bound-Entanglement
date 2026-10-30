# Constructive separability under detailed balance

Assume the [model](model.md), with `pi_i>0` and `Q_ij pi_j=Q_ji pi_i`. Propagated detailed balance reads `P_ij(t)pi_j=P_ji(t)pi_i`.

**1. A nonnegative Gram decomposition.** Let `D_i=exp(-t q_i/2)` and define a full matrix `C` with
```math
C_{ij}=D_iD_j\exp[-t\|v_i-v_j\|^2/2],\qquad C_{ii}=e^{-tq_i}.
```
The Gaussian overlap kernel has a representation as an integral of outer products of **nonnegative** functions: appropriately normalized shifted Gaussians `f_i(x)>=0` satisfy `integral f_i(x)f_j(x)dx=exp(-t||v_i-v_j||²/2)`. Thus `C` belongs to the completely positive matrix cone (the matrix cone, *not* the class of quantum channels). The cone is closed in finite dimension, so there are finitely many vectors `a^(k)>=0` with
```math
C=\sum_k a^{(k)}(a^{(k)})^T.
```
For `t=0`, this is simply the rank-one all-ones matrix.

**2. Construct the separable Choi part.** For each `a=a^(k)`, define real, nonnegative vectors `u,w` by
```math
|u_i|^2=a_i\sqrt{\pi_i},\qquad |w_i|^2=a_i/\sqrt{\pi_i}.
```
Twirling the separable operator `|u><u| tensor |w><w|` under `U tensor conjugate(U)` for diagonal unitaries `U`, and summing over `k`, produces the entire `|ii><jj|` coherence sector `C_ij=c_ij` and the cross-diagonal weights
```math
C_{ij}\sqrt{\pi_i/\pi_j}.
```
The `|ii><ii|` weights of this separable part are `C_ii=e^{-t q_i}`.

**3. PPT bounds the residual coefficients.** From `P_ij pi_j=P_ji pi_i`, positivity of `pi`, and the PPT inequality, one obtains
```math
P_{ij}\ge c_{ij}\sqrt{\pi_i/\pi_j}
```
for every `i != j`, including zero transition probabilities (do not divide by a potentially zero `P_ji`). For the diagonal, the classical no-jump event guarantees `P_ii(t)>=exp(-tq_i)`.

Subtracting the explicitly twirled separable operator from `J_t` therefore leaves only nonnegative multiples of `|ij><ij|`. Those are separable. This proves PPT implies EB; the reverse implication follows because separable Choi operators are PPT.

The proof uses inherited completely positive / pairwise completely positive matrix theory and the CLDUI correspondence; its novel candidate content is the all-time **dynamical** consequence for the specified resolved Lindbladian. See [related work](../references/RELATED_WORK.md).

**Scope caution.** A generic Davies generator with degenerate transition frequencies need not have independently evolving off-diagonal matrix units. Complex non-Hermitian diagonal Lindblad operators can create phases not removed by a local diagonal Hamiltonian. Neither is covered by this proof.
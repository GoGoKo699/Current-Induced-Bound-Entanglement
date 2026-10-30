# Model and exact channel tests

## Resolved transitions

Fix an orthonormal basis of a finite system of dimension $`d\ge2`$. Write $`E_{ij}=|i\rangle\langle j|`$. The real matrix $`Q`$ is a **column-convention** classical generator: $`Q_{ij}\ge0`$ for $`i\ne j`$, $`\sum_iQ_{ij}=0`$, and $`q_i=-Q_{ii}`$ is the rate of leaving level $`i`$. Thus a population column evolves by $`\dot p=Qp`$.

Consider the time-independent Lindblad generator, with $`\hbar=1`$,

```math
\begin{aligned}
\mathcal L(\rho)={}&-i[H,\rho]
 +\sum_{i\ne j}Q_{ij}\left(E_{ij}\rho E_{ji}-\tfrac12\{E_{jj},\rho\}\right)\\
&-\tfrac12\sum_{\alpha=1}^m[V_\alpha,[V_\alpha,\rho]].
\end{aligned}
```

Here $`H`$ and every $`V_\alpha`$ are Hermitian and diagonal. Distinct transitions have separate rank-one jump operators; combining equal-frequency transitions into one coherent jump is not the same model. The diagonal real noise vector at level $`i`$ is $`v_i=((V_\alpha)_{ii})_{\alpha=1}^m`$.

Applying the generator to matrix units gives the population propagator $`P(t)=e^{tQ}`$ and, for $`i\ne j`$,

```math
\Phi_t(E_{ij})=e^{-it(H_{ii}-H_{jj})}c_{ij}(t)E_{ij},
\qquad
c_{ij}(t)=\exp\!\left[-\frac t2(q_i+q_j)-\frac t2\|v_i-v_j\|^2\right].
```

A diagonal output unitary removes all Hamiltonian phases. This changes neither separability nor positivity of a partial transpose. We use that phase-removed form below. The resolved transition model, rather than a general weak-coupling derivation, is the hypothesis of the theorem.

## Choi normalization and diagnostics

Use output-first tensor order and the normalized maximally entangled input $`|\Omega_d\rangle=d^{-1/2}\sum_i|ii\rangle`$. The unnormalized Choi operator and normalized Choi state are

```math
J_t=\sum_{i,j}P_{ij}(t)|ij\rangle\langle ij|
       +\sum_{i\ne j}c_{ij}(t)|ii\rangle\langle jj|,
\qquad \rho_t=J_t/d.
```

The trace of $`J_t`$ is $`d`$; the trace of $`\rho_t`$ is one. Partial transposition on the second factor leaves the $`|ii\rangle`$ weights and gives, on each unordered pair $`\{|ij\rangle,|ji\rangle\}`$,

```math
\frac1d\begin{pmatrix}P_{ij}(t)&c_{ij}(t)\\c_{ij}(t)&P_{ji}(t)\end{pmatrix}.
```

All diagonal entries are nonnegative. Consequently,

```math
\Phi_t\text{ is PPT}
\quad\Longleftrightarrow\quad
P_{ij}(t)P_{ji}(t)\ge c_{ij}(t)^2\quad\text{for every }i\lt j.
```

Here a **PPT channel** means that its Choi state is positive under partial transpose, equivalently that transposition composed with the channel is completely positive. An **entanglement-breaking (EB) channel** has a separable Choi state and produces separable output for every input entangled with any reference. These channel-level equivalences and the diagonal-twirl diagnostics are established foundations, not new tests; see [related work](../references/RELATED_WORK.md).

## Reversible theorem

Suppose there is a faithful probability vector $`\pi_i>0`$ satisfying classical detailed balance,

```math
Q_{ij}\pi_j=Q_{ji}\pi_i\quad\text{for all }i,j.
```

**For every finite time, the channel is PPT if and only if it is entanglement breaking.** The [proof](reversible_proof.md) constructs a separable Choi decomposition whenever the pairwise PPT inequalities hold. No irreducibility assumption is needed for this equivalence.

Define $`t_{\rm PPT}=\inf\{t\ge0:\Phi_t\text{ is PPT}\}`$ and $`t_{\rm EB}`$ analogously, with the infimum of an empty set equal to infinity. Both properties persist under later semigroup evolution. Closedness and continuity give closed onset sets, so the theorem implies $`t_{\rm PPT}=t_{\rm EB}`$, possibly with both infinite. Irreducibility gives finite onset here: every $`P_{ij}(t)`$ approaches a strictly positive stationary weight while every off-diagonal $`c_{ij}(t)`$ decays to zero.

The [cycle](cycle.md) violates the equality for every nonzero bias within its stated dephasing range. The [operational argument](operational.md) identifies the PPT threshold as the boundary between positive and zero **two-way assisted** quantum capacity throughout this structured Choi class, not only at detailed balance.

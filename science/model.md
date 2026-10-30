# Resolved-transition quantum dynamics

Let `Q` be a finite-dimensional column-stochastic infinitesimal generator: `Q_ij >= 0` when `i != j`, `sum_i Q_ij=0`, and `q_i=-Q_ii`. Write `E_ij=|i><j|`. Consider
```math
\mathcal L(\rho)=-i[H,\rho]+\sum_{i\ne j}Q_{ij}\left(E_{ij}\rho E_{ji}-\tfrac12\{E_{jj},\rho\}\right)-\tfrac12\sum_\alpha [V_\alpha,[V_\alpha,\rho]],
```
where `H` and **each** `V_alpha` are Hermitian and diagonal. The Lindblad operators for distinct transitions are separately resolved. Define `v_i=((V_alpha)_{ii})_alpha`, `P(t)=exp(tQ)`, and
```math
c_{ij}(t)=\exp\!\left[-\tfrac t2(q_i+q_j)-\tfrac t2\|v_i-v_j\|^2\right].
```
A local diagonal output unitary eliminates the `H` phases for entanglement questions. In output-first order, the **unnormalized** Choi operator is
```math
J_t=\sum_{i,j}P_{ij}(t)|ij\rangle\langle ij|+\sum_{i\ne j}c_{ij}(t)|ii\rangle\langle jj|,\qquad \rho_t=J_t/d.
```
Its trace is `d`. Partial transpose yields one block per unordered pair:
```math
\frac1d\begin{pmatrix}P_{ij}(t)&c_{ij}(t)\\c_{ij}(t)&P_{ji}(t)\end{pmatrix}.
```
Therefore the channel is PPT (equivalently, completely copositive) exactly when
```math
P_{ij}(t)P_{ji}(t)\ge c_{ij}(t)^2\quad\text{for every }i\ne j.
```
This is the standard diagonal-twirl/CLDUI PPT test, not an independently novel criterion.

**Theorem (reversible exact boundary).** Suppose `pi_i>0` and `Q_ij pi_j=Q_ji pi_i` for all indices. Then for every `t>=0`,
```math
\Phi_t\text{ is PPT}\quad\Longleftrightarrow\quad\Phi_t\text{ is entanglement breaking}.
```
There is no irreducibility requirement for the equivalence, and finite onset is **not** automatic for reducible `Q`. Proof: [reversible_proof.md](reversible_proof.md).

**Counterfamily.** A normalized three-level biased cycle violates the equivalence for every nonzero bias when uniform dephasing satisfies `0<=gamma<=1/2`. The population contraction singular values and coherence attenuation are independent of the bias. Proof: [cycle.md](cycle.md).

**Operational corollary.** In this Choi class, a non-PPT channel has strictly positive two-way assisted quantum capacity; PPT channels have zero two-way assisted quantum capacity. This says only whether the capacity vanishes, not its magnitude. Proof: [operational.md](operational.md).
# Capacity meaning of the PPT transition

For a channel in the [resolved-transition class](model.md), the partial transpose of its normalized Choi matrix contains, for each unordered `i,j`, a block
```math
\frac1d\begin{pmatrix}P_{ij}&c_{ij}\\c_{ij}&P_{ji}\end{pmatrix}.
```
If `c_ij²>P_ij P_ji`, project both Choi subsystems locally onto `span{|i>,|j>}`. This postselected two-qubit state retains a negative partial-transpose block and has positive success probability. All two-qubit NPT states are distillable, hence independent uses of the channel and two-way LOCC yield a strictly positive asymptotic entanglement rate. Thus `Q_2(Phi)>0`.

Conversely, PPT of the Choi matrix is equivalent to complete positivity of `T o Phi`. Under a two-way assisted protocol beginning with no shared entanglement, a PPT channel preserves PPT across the sender/receiver partition, including adaptive local operations and classical communication. A maximally entangled output cannot be approached at positive asymptotic rate. Consequently
```math
Q_2(\Phi)>0\ \Longleftrightarrow\ \Phi\text{ is not PPT},\qquad
Q_2(\Phi)=0\ \Longleftrightarrow\ \Phi\text{ is PPT}.
```
This equivalence relies on the **special block structure** for the forward direction and is not a claim that all NPT Choi states of arbitrary channels are distillable. In a semigroup, PPT and EB properties persist under subsequent channel composition, so the onsets are well-defined extended-real thresholds.

Under detailed balance, the reversible theorem further gives `t_PPT=t_EB`. The biased qutrit supplies `t_PPT<t_EB`: an interval with no two-way quantum communication but residual **bound** Choi entanglement.

No numerical capacity, uniformly positive lower bound near the threshold, private capacity, key rate, or unassisted quantum-capacity statement is established.
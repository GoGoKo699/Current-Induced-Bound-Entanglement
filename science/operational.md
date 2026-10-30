# What ends at the PPT threshold?

The operational task is quantum communication with unlimited two-way classical communication and independent uses of a fixed channel, starting without shared entanglement. Write its capacity as $`Q_2(\Phi)`$. We establish only whether it vanishes, not its rate.

## A failed PPT block gives distillable entanglement

Prepare $`|\Omega_d\rangle`$ locally and send one half through the channel. This creates its normalized Choi state. If the channel is non-PPT in the [resolved-transition class](model.md), there is a pair $`i\lt j`$ for which $`c_{ij}^2>P_{ij}P_{ji}`$.

Both parties project locally onto $`\mathrm{span}\{|i\rangle,|j\rangle\}`$. The success probability is

```math
s_{ij}=\frac{P_{ii}+P_{ij}+P_{ji}+P_{jj}}d>0.
```

The retained two-qubit state's partial transpose still contains the negative determinant block. Every entangled two-qubit state is distillable, a prior theorem identified in [related work](../references/RELATED_WORK.md). Repeating the successful projection on independent channel uses and distilling gives a positive asymptotic entanglement rate, and teleportation converts it into quantum transmission. Therefore $`Q_2(\Phi)>0`$. No lower bound uniform near the threshold is asserted.

## PPT channels cannot distribute distillable entanglement

A PPT Choi matrix is equivalent to complete positivity of $`T\circ\Phi`$, where $`T`$ transposes the receiver output. In an adaptive protocol, transpose the receiver's previously held systems. A channel use then acts by the completely positive map $`T\circ\Phi`$ on the newly received system, preserving positivity across the sender-receiver cut. Local operations and classical communication also preserve the PPT property, branch by branch.

Thus every final shared state is PPT. Its overlap with a maximally entangled state of Schmidt rank $`M`$ is at most $`1/M`$: partial transposition changes that target projector into the swap divided by $`M`$, whose largest eigenvalue is $`1/M`$. A positive-rate maximally entangled target cannot be approached. Hence $`Q_2(\Phi)=0`$.

Together these arguments give, for this structured class,

```math
\begin{aligned}
Q_2(\Phi)>0&\quad\Longleftrightarrow\quad\Phi\text{ is non-PPT},\\
Q_2(\Phi)=0&\quad\Longleftrightarrow\quad\Phi\text{ is PPT}.
\end{aligned}
```

## What this does and does not imply

For a semigroup, later composition preserves PPT and EB. Detailed balance therefore makes the zero-capacity threshold coincide with universal separability. The circulating qutrit instead has a nonempty interval with zero two-way assisted quantum capacity and entangled Choi state.

The non-PPT implication relies on the special two-dimensional projection, not on an assertion that all non-PPT states in arbitrary dimensions are distillable. A channel-level theorem is also different from the evolution of one chosen mixed entangled input. No unassisted, one-way, private, or secret-key capacity is computed. In particular, PPT nondistillability alone must not be read as a universal zero-private-key statement.

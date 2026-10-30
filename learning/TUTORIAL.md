# Two ways for noisy quantum communication to end

## The experiment

Prepare an entangled pair, keep one half away from the noise, and expose the other half to a three-level noisy evolution. After a chosen time, the parties can perform local operations and exchange classical messages. There are two different questions: can many copies yield singlets, and does any entanglement remain at all?

A separable state is a probabilistic mixture of product states. It contains no entanglement. A bound-entangled state is entangled but cannot be distilled into singlets by local operations and classical communication. A state whose partial transpose is positive is called PPT. PPT states cannot be distilled, but in dimensions above two by two, PPT alone does not imply separability. These are established ingredients, cited in [related work](../references/RELATED_WORK.md).

This project studies the noise as a **channel**, not just one initially selected mixed state. A channel is entanglement breaking if every input loses all entanglement with every reference. Its Choi state tests this universal property: start with a normalized maximally entangled pair and apply the channel to one half. Separability of the Choi state is equivalent to the channel being entanglement breaking.

## Populations and coherences

A density matrix has diagonal populations and off-diagonal coherences. In the specified model, populations follow a classical rate equation, while each coherence decays independently. Independent transition jumps and Hermitian diagonal dephasing ensure this separation. The exact assumptions are in the [model](../science/model.md).

For three levels arranged in a cycle, let a clockwise jump have rate $`a`$ and a counterclockwise jump rate $`b`$. Holding $`a+b`$ fixed holds the total outgoing rate fixed. The bias

```math
\eta=\frac{a-b}{a+b}
```

measures circulation. Equal populations are stationary even when $`a\ne b`$: probability can circulate steadily without accumulating anywhere. Detailed balance is stronger than stationarity. It requires equal opposing flows along every edge and holds in this family only when $`\eta=0`$.

The dimensionless time is physical time times $`a+b`$. Without extra dephasing, every off-diagonal coherence has attenuation $`c=e^{-t}`$. The two nontrivial population singular values are both $`E=e^{-3t/2}`$. Neither damping factor depends on the bias. Oscillation phases do depend on it, so the full population spectrum is not unchanged.

## The two diagnostics

Let $`p_1`$ and $`p_2`$ be the probabilities of moving one and two cyclic steps during the exposure. A partial transpose of the Choi state produces identical two-by-two blocks, up to ordering. Their determinant has the sign of

```math
D_\eta(t)=p_1(t)p_2(t)-c(t)^2.
```

A negative sign gives a negative partial transpose. In this channel class, the offending pair can be isolated by local two-level projections. The resulting two-qubit entanglement is distillable, so the channel has positive two-way assisted quantum capacity. A nonnegative sign for all blocks makes the channel PPT and its two-way assisted quantum capacity zero. This is a statement about the sign of the capacity, not its numerical size.

To check whether entanglement nevertheless survives, use a second test. Realignment rearranges matrix entries and sums the resulting singular values. Every separable normalized state has realignment norm at most one. For this cycle,

```math
R(t)=\frac{1+2E}3+2c.
```

Thus $`R>1`$ proves entanglement. A value at or below one does **not** by itself prove separability. The Choi normalization is essential: using the unnormalized operator would change the bound.

## One complete example

Take maximal clockwise bias, $`\eta=1`$, no extra dephasing, and $`t=1.25`$. The independent full-generator calculation gives

```math
\begin{aligned}
D_1(1.25)&=0.0075006931\ldots>0,\\
R(1.25)&=1.0085795716\ldots>1.
\end{aligned}
```

The smallest eigenvalue of the normalized Choi partial transpose is $`0.0041234967\ldots`$, so this is not a sign decision made at numerical zero. The state is simultaneously PPT and entangled: it is bound entangled, and the channel is not entanglement breaking even though its two-way quantum capacity is zero.

The current-free reference reaches both boundaries at

```math
t_*=1.26188944840409\ldots.
```

The biased channel becomes PPT at $`1.21744501742084\ldots`$. Its certified PPT-entangled interval therefore extends up to the reversible reference time. This does not identify its exact entanglement-breaking time after that reference point.

## Why detailed balance rules out this gap

The reversible theorem is stronger than a numerical observation about one cycle. It applies in arbitrary finite dimension within the resolved-transition model. The decaying coherences admit a nonnegative Gaussian Gram factorization. Detailed balance supplies one stationary-distribution tilt of product vectors that reproduces those coherences by averaging diagonal phases. The PPT inequalities ensure that the required cross-populations fit inside the actual populations; no-jump probabilities supply the diagonal remainder.

What remains after subtracting this constructed separable operator is a nonnegative mixture of basis product states. Thus a PPT channel is already entanglement breaking in the reversible model. The [proof](../science/reversible_proof.md) gives each step and treats zero transition probabilities without dividing by them.

## The effect at weak current

For every nonzero bias, not just the maximally biased example, the cycle has a PPT-entangled interval when uniform dephasing is between zero and one half in normalized units. With no extra dephasing, the opening is quadratic:

```math
t_*-t_{\rm PPT}=0.0391427404380864\ldots\,\eta^2+O(\eta^4).
```

The effect therefore becomes small near reversibility. At the endpoint dephasing value of one half, the leading opening is fourth order instead. The [derivation](../science/cycle.md) proves strict positivity; the [numerical checks](../verification/README.md) use high precision for small differences.

## What to take away

Circulation changes **which kind of entanglement survives** under matched damping scales. It ends distillable quantum communication earlier while leaving bound Choi entanglement. It does not demonstrate a better quantum memory, longer total entanglement lifetime, or positive private-key capacity. A chosen input's behavior, a channel's universal behavior, and a communication rate are distinct claims.

Use the [Rivas–Huelga bridge](ANCHOR_BRIDGE.md) for the dynamical foundations, the [milestone map](MILESTONES.md) for the connected understanding targets, and the [science route](../science/README.md) for exact proofs.

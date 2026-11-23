# Two ways for noisy quantum communication to end

## The experiment

Prepare an entangled pair, keep one half away from the noise, and expose the other half to a three-level noisy evolution. After a chosen time, the parties can perform local operations and exchange classical messages. Two questions arise. Can many copies yield nearly perfect singlets? Does any entanglement remain at all?

A separable state is a probabilistic mixture of product states. A bound-entangled state has entanglement that cannot be distilled into singlets by local operations and classical communication. A state whose partial transpose is positive is called PPT. Every separable state is PPT, and PPT prevents distillation. Two qutrits can share a state that is PPT and still entangled. [Research background](../references/RELATED_WORK.md)

A channel is entanglement breaking (EB) when it removes entanglement with every reference for every input. Its normalized Choi state tests this universal property. Prepare a normalized maximally entangled pair of qutrits and apply the channel to one half. The channel is EB exactly when that bipartite output is separable.

## Populations and coherences

Populations are the diagonal entries of a density matrix. In this model they follow a classical rate equation. Coherences are the off-diagonal entries. Separate rank-one transition jumps and diagonal dephasing let each coherence decay independently. [Operational model](../science/model.md)

Arrange three levels in a cycle, with clockwise rate $`a`$ and counterclockwise rate $`b`$. Fix the outgoing rate $`a+b>0`$ and express time in units of $`(a+b)^{-1}`$. The normalized bias and the two damping factors are

```math
\eta=\frac{a-b}{a+b},\qquad c=e^{-(1+\gamma)t},\qquad E=e^{-3t/2}.
```

Here $`\gamma\ge0`$ is the uniform dephasing rate in the same units. Uniform populations are stationary at every bias. Probability can circulate without accumulating anywhere. Detailed balance requires equal opposing flows along each edge, which holds here at $`\eta=0`$. At a matched dephasing rate, bias changes the Fourier phases of the population evolution while its singular values $`1,E,E`$ and the coherence attenuation $`c`$ remain fixed. [Cycle calculation](../science/cycle.md)

## The two diagnostics

Let $`p_m`$ be the population probability of shifting by $`m`$ steps, with $`m=0,1,2`$. Partial transposition gives three identical two-by-two Choi blocks up to ordering. Their determinant has the sign of

```math
D_\eta(t)=p_1(t)p_2(t)-c(t)^2.
```

A negative determinant gives a negative partial transpose. For this model, projecting both parties onto the corresponding two levels preserves an entangled two-qubit state with positive probability. This makes the channel's two-way assisted quantum capacity positive. Once the channel is PPT, compositions of channel uses and local operations with classical communication preserve PPT across the parties' cut. The capacity is then zero. [Operational proof](../science/operational.md)

Realignment rearranges entries of the normalized Choi state and sums the singular values of the rearranged matrix. Its norm in this cycle is

```math
R(t)=\frac{1+2E}{3}+2c.
```

Every separable state has $`R\le1`$. A value $`R>1`$ therefore proves entanglement. Passing realignment alone leaves open whether the state is separable.

## Why the two tests suffice together

For the real-coherence, circulant Choi states of two qutrits studied here, both tests together give an exact criterion. Once both inequalities hold, a finite average of product states reconstructs the Choi state. A uniform product contributes equal amounts to all cyclic populations and reproduces part of the aligned coherence. A product supported on two levels provides the remaining coherence while its local amplitudes adjust the two directed population contributions. Any unused diagonal weight is supplied by basis products. The full construction also covers zero and negative coherence. [Separability proof](../science/separability.md)

A static example sits exactly on the realignment boundary. Use the tuple convention of the proof, in which a listed tuple $`(p_0,p_1,p_2,c)`$ gives the entries before the common Choi factor of one third. Set

```math
(p_0,p_1,p_2,c)=\left(\frac25,\frac25,\frac15,\frac4{15}\right).
```

The PPT test gives $`p_1p_2-c^2=2/225>0`$. The nontrivial population singular values are both $`1/5`$, so the realignment norm is exactly one. Here the uniform and two-level product averages use the following portions of the tuple.

| Product average | Population contribution | Coherence contribution |
|---|---|---:|
| Uniform | $`(2/15,2/15,2/15)`$ | $`2/15`$ |
| Two-level | $`(4/15,4/15,1/15)`$ | $`2/15`$ |

The columns sum to the specified populations and coherence. The normalized Choi state is thus a mixture of the two product averages with respective weights $`2/5`$ and $`3/5`$. This example uses the separability certificate at equality, where the witness alone would give no conclusion.

## Two crossings in the cycle

The realignment crossing occurs at the unique time $`t_*`$ satisfying $`E+3c=1`$. This is also the PPT crossing for the unbiased reference, where $`p_1=p_2=(1-E)/3`$. For a biased cycle, let $`t_{\rm PPT}`$ denote its own PPT crossing. The ratio $`p_1p_2/c^2`$ increases through one, and $`R(t)`$ decreases through one. The Choi state becomes separable precisely when both inequalities first hold.

```math
t_{\rm EB}=\max\{t_{\rm PPT},t_*\}.
```

For each nonzero bias a unique critical dephasing rate $`\gamma_c(\eta)>1/2`$ determines their order. All comparisons use the unbiased reference with the same dephasing and outgoing rate. [Critical curve](../science/cycle.md)

| Dephasing at nonzero bias | Thresholds | Entanglement between the two diagnostic crossings |
|---|---|---|
| $`\gamma\lt\gamma_c(\eta)`$ | $`t_{\rm PPT}\lt t_{\rm EB}=t_*`$ | Bound entanglement from $`t_{\rm PPT}`$ up to, but excluding, $`t_*`$ |
| $`\gamma=\gamma_c(\eta)`$ | $`t_{\rm PPT}=t_{\rm EB}=t_*`$ | No interval |
| $`\gamma\gt\gamma_c(\eta)`$ | $`t_*\lt t_{\rm PPT}=t_{\rm EB}`$ | Distillable entanglement from $`t_*`$ up to, but excluding, $`t_{\rm PPT}`$ |

Take maximal clockwise bias $`\eta=1`$. At zero dephasing, the biased channel becomes PPT at $`t_{\rm PPT}=1.2174450174\ldots`$ and becomes EB at $`t_*=1.2618894484\ldots`$. At $`t=1.25`$, an independent calculation of the full generator gives $`D_1=0.0075006931\ldots>0`$ and $`R=1.0085795716\ldots>1`$. The Choi state is PPT and entangled. The channel's two-way assisted quantum capacity is zero throughout this interval.

For the same bias, the critical rate is $`\gamma_c(1)=0.7186185654\ldots`$. At $`\gamma=1`$, realignment reaches one at $`t_*=0.7467471159\ldots`$, but the biased state still has a negative partial transpose. The biased PPT and EB thresholds both occur at $`0.7552131478\ldots`$. Circulation then delays both thresholds relative to the unbiased channel, without producing a bound-entangled interval.

## Detailed balance and weak current

The general reversible theorem applies in arbitrary finite dimension within the resolved-transition model. The decaying coherences admit a nonnegative Gaussian Gram factorization. Detailed balance supplies one stationary-distribution tilt of product vectors. Averaging their diagonal phases reproduces the coherences, and the PPT inequalities make the required populations fit. The no-jump probabilities and the remaining population weights complete a separable decomposition. [Reversible proof](../science/reversible_proof.md)

For the cycle at zero dephasing, the opening near zero bias is

```math
t_*-t_{\rm PPT}=0.0391427404380864\ldots\,\eta^2+O(\eta^4).
```

At $`\gamma=1/2`$ the quadratic term vanishes, but a positive fourth-order opening persists. This dephasing value lies strictly below the critical rate at each nonzero bias. Close to zero bias, $`\gamma_c(\eta)-1/2`$ itself is quadratic in $`\eta`$. [Derivation](../science/cycle.md)

The proofs determine the entanglement thresholds and when two-way quantum communication is possible in the resolved channel model. A positive capacity can have different magnitudes at different points in that region, and the thresholds do not quantify storage fidelity for a chosen input.

## Reproducing the examples

The [verification guide](../verification/README.md) explains how to reconstruct the Choi matrix from the Lindblad generator, evaluate both diagnostics, and check the threshold calculations. The [Rivas–Huelga bridge](ANCHOR_BRIDGE.md) gives the dynamical foundations. The [30-milestone map](MILESTONES.md) connects those foundations to the proofs.

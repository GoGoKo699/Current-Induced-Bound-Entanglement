# Exact entanglement lifetimes under circulation

## A matched three-level family

Let $`S|j\rangle=|j+1\bmod3\rangle`$ and $`Q=aS+bS^2-(a+b)I`$, with $`a,b\ge0`$ and $`a+b>0`$. Measure time in units of $`(a+b)^{-1}`$, define $`\eta=(a-b)/(a+b)\in[-1,1]`$, and add uniform dephasing $`\gamma(\Delta-\mathrm{id})`$ in these same units. The uniform distribution is stationary. Its oriented current per edge is $`\eta/3`$; detailed balance holds exactly at $`\eta=0`$.

The jump operators remain separately resolved; a single coherent cyclic shift as a jump gives a different channel. Uniform dephasing is within the model, using diagonal projectors with amplitudes $`\sqrt\gamma`$.

Define

```math
E=e^{-3t/2},\qquad \theta=\sqrt3\eta t/2,\qquad c=e^{-(1+\gamma)t}.
```

The Fourier diagonalization of the population generator yields

```math
\begin{aligned}
P(t)&=p_0I+p_1S+p_2S^2,\\
p_m(t)&=\frac{1+2E\cos(\theta-2\pi m/3)}3.
\end{aligned}
```

Its eigenvalues are $`1,Ee^{i\theta},Ee^{-i\theta}`$ and its singular values are $`1,E,E`$. Thus the bias changes oscillation phases, but not the singular-value contraction or coherence attenuation. The full eigenvalue spectrum is **not** held fixed.

## PPT and realignment

The channel is PPT exactly when $`D_\eta(t)=p_1p_2-c^2\ge0`$, where

```math
p_1p_2=\frac{1-2E\cos\theta+E^2(4\cos^2\theta-3)}9.
```

For clarity, realignment sends the matrix element $`\rho_{ij,kl}`$ to the entry with row $`(i,k)`$ and column $`(j,l)`$. Applied to the normalized Choi state, it gives one block $`P/3`$ and six scalar blocks $`c/3`$. Its trace norm is therefore

```math
R(t)=\|\mathcal R(\rho_t)\|_1=\frac{1+2E}3+2c.
```

## Exact entanglement-breaking time

The [cyclic-state separability criterion](separability.md) says that this Choi state is separable exactly when it is PPT and $`R(t)\le1`$. Define $`t_{\rm PPT}`$ as the first time $`p_1p_2=c^2`$ and $`t_*(\gamma)`$ as the unique solution of $`E+3c=1`$.

Both crossing times are unique. The realignment norm decreases strictly. For the PPT test, in these time units the cyclic master equation gives $`p'_m+p_m>0`$ at every positive time for $`m=1,2`$. All population probabilities are positive there, including for a cycle that runs only in one direction. Therefore $`p_m/c`$ increases strictly and $`p_1p_2/c^2`$ increases from zero to infinity. The exact time is

```math
t_{\rm EB}(\eta,\gamma)=\max\{t_{\rm PPT}(\eta,\gamma),\,t_*(\gamma)\}.
```

At zero bias $`p_1=p_2=(1-E)/3`$, so $`t_{\rm PPT}=t_{\rm EB}=t_*`$. The positive-to-zero boundary for two-way assisted capacity occurs at $`t_{\rm PPT}`$ by the [distillable pair argument](operational.md).

## Critical dephasing

At the matched reversible time, substitution into the PPT determinant gives

```math
D_\eta(t_*)=
\frac{2E_*(1-\cos\theta_*)[1-2E_*(1+\cos\theta_*)]}9.
```

For every nonzero bias, $`0\lt|\theta_*|\le\sqrt3\,t_*(0)/2\lt1.1`$. Only the last bracket can change sign. Along this interval of times, $`2e^{-3t/2}[1+\cos(\sqrt3\eta t/2)]`$ is strictly decreasing in $`t`$. As the dephasing rate increases from zero to infinity, $`t_*`$ decreases strictly from $`t_*(0)`$ toward zero. At $`\gamma=1/2`$, $`E_*=1/4`$ and the bracket is still strictly positive. These facts give one critical dephasing rate $`\gamma_c(\eta)>1/2`$ for each nonzero bias. Its defining equations are

```math
\begin{aligned}
2e^{-3t_c/2}\bigl[1+\cos(\sqrt3\eta t_c/2)\bigr]&=1,\\
\gamma_c(\eta)&=\frac1{t_c}\log\frac3{1-e^{-3t_c/2}}-1.
\end{aligned}
```

| For nonzero bias | Ordering | Effect relative to the reversible channel |
| --- | --- | --- |
| Below critical dephasing | $`t_{\rm PPT}\lt t_{\rm EB}=t_*`$ | Distillability ends earlier. Total entanglement survives to the same time. |
| At critical dephasing | $`t_{\rm PPT}=t_{\rm EB}=t_*`$ | The two lifetimes coincide with the reversible lifetime. |
| Above critical dephasing | $`t_*\lt t_{\rm PPT}=t_{\rm EB}`$ | Distillable and total entanglement lifetimes are both longer. |

A bound-entangled Choi interval exists exactly in the first row, from $`t_{\rm PPT}`$ inclusive to $`t_*`$ exclusive. At maximal bias, $`\gamma_c(1)=0.7186185654\ldots`$. For example, at $`\eta=1,\gamma=1`$, $`t_*=0.7467471159\ldots`$ and both biased thresholds are $`0.7552131478\ldots`$.

Expanding the defining equation at $`\eta=0`$ gives $`\gamma_c(\eta)=1/2+(\log 4)\eta^2/6+O(\eta^4)`$. In detail, for $`t_0=(2/3)\log 4`$, the root is $`t_c=t_0-t_0^2\eta^2/8+O(\eta^4)`$. The derivative of the dephasing expression with respect to $`t_c`$ at $`t_0`$ is $`-2/t_0`$. At exactly zero bias the two onsets agree at every dephasing rate.

## Weak circulation without extra dephasing

At $`\gamma=0`$, setting $`x=e^{-t_*/2}`$ gives $`x^3+3x^2=1`$ and

```math
t_*=-2\log\!\left[2\cos(2\pi/9)-1\right]
=1.26188944840409\ldots.
```

Write $`D_\eta=D_0+\eta^2A+O(\eta^4)`$. Expanding the determinant at fixed time gives

```math
A(t)=\frac{E(1-4E)t^2}{12},\qquad
D_0'(t_*)=\frac{(1-E_*)(E_*+2)}9>0.
```

The implicit-function theorem then gives the first-onset shift

```math
\begin{aligned}
t_*-t_{\rm PPT}&=K\eta^2+O(\eta^4),\\
K&=\frac{3E_*(1-4E_*)t_*^2}{4(1-E_*)(E_*+2)}\\
&=0.0391427404380864\ldots.
\end{aligned}
```

The even expansion reflects exchanging clockwise and counterclockwise rates. At the dephasing endpoint $`\gamma=1/2`$, the quadratic term vanishes and the opening is fourth order; the zero-dephasing coefficient must not be used there.

For $`\eta=1,\gamma=0`$, $`t_{\rm PPT}=1.21744501742084\ldots`$. At $`t=1.25`$, $`D_1=0.0075006931\ldots>0`$ and $`R=1.0085795716\ldots>1`$. The [verification](../verification/README.md) rebuilds these quantities from a full Lindblad matrix exponential rather than substituting the closed Choi formula.

## Physical conclusion

The damping diagnostics alone leave both lifetime orderings possible. With weak dephasing the directed flow separates loss of distillability from loss of all entanglement. With stronger dephasing it delays both losses in the matched comparison. The result concerns the times at which these capabilities disappear. Near those times the positive two-way capacity can be small, and this analysis gives no rate estimate.

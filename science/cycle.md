# Circulation separates two entanglement-loss thresholds

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

The standard realignment criterion says that $`R>1`$ certifies entanglement. The converse is not generally valid. This witness, like the population singular values, is bias independent.

Let $`t_*`$ be the unique solution of $`E+3c=1`$. Existence and uniqueness follow because the left side decreases continuously from four to zero. At zero bias, $`p_1=p_2=(1-E)/3`$, so $`t_*`$ is precisely the PPT onset and, by [reversibility](reversible_proof.md), the EB onset.

## Every nonzero bias opens an interval

At the same time $`t_*`$, the difference between biased and unbiased PPT determinants is

```math
D_\eta(t_*)-D_0(t_*)=
\frac{2E_*(1-\cos\theta_*)[1-2E_*(1+\cos\theta_*)]}9.
```

For $`0\le\gamma\le1/2`$, $`c\ge E`$, hence $`E_*\le1/4`$. Also $`0\lt t_*\le t_*(0)\lt1.27`$, so a nonzero bias has $`0\lt|\theta_*|\lt2\pi`$. Both factors in the numerator are strictly positive. At $`\gamma=1/2`$, the second bracket is $`(1-\cos\theta_*)/2`$, still positive.

Consequently the biased channel is strictly PPT at $`t_*`$. By continuity it is PPT on an interval immediately below $`t_*`$, where $`R>1`$. Its Choi state is therefore entangled and PPT: **bound entangled**. Equivalently,

```math
t_{\rm PPT}(\eta,\gamma)\lt t_*(\gamma)\le t_{\rm EB}(\eta,\gamma)
\qquad(0\lt|\eta|\le1,\ 0\le\gamma\le1/2).
```

Semigroup composition preserves PPT, so the interval from its first onset up to $`t_*`$ is certified. The true biased EB time is not identified by the witness equality.

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

Circulation makes the loss of two-way distillability occur earlier while some entanglement survives. It does not establish a longer total entanglement lifetime, a larger communication rate, or a useful quantum memory. The comparison isolates the direction of population flow from unchanged damping scales, within a particular finite-level Markovian model.

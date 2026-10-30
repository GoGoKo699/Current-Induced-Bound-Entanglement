# A nonzero cycle current produces a bound-entangled channel interval

Let `S` cyclically permute three basis states, and consider
```math
Q=aS+bS^2-(a+b)I,\quad a,b\ge0,\quad a+b>0.
```
Scale time by `a+b`, and let `eta=(a-b)/(a+b)`, so `|eta|<=1`. Uniform dephasing is `gamma(Delta-id)` in the same units. The uniform stationary distribution satisfies detailed balance exactly when `eta=0`; `eta!=0` gives stationary circulation.

Write
```math
E=e^{-3t/2},\quad\theta=\sqrt3\eta t/2,\quad c=e^{-(1+\gamma)t}.
```
The population transition matrix is circulant, with the `m`th cyclic offset
```math
p_m(t)=\frac{1+2E\cos(\theta-2\pi m/3)}3,\qquad m=0,1,2.
```
The PPT test reduces to `p_1 p_2>=c²`, with
```math
p_1p_2=\frac{1-2E\cos\theta+E^2(4\cos^2\theta-3)}9.
```
The normalized Choi state has realignment trace norm
```math
R(t)=\frac{1+2e^{-3t/2}}3+2e^{-(1+\gamma)t}.
```
If `R>1`, the computable cross-norm/realignment criterion certifies entanglement. The value `R`, coherence attenuation, and the nontrivial singular values `E` of the classical propagator are all independent of `eta`.

Let `t_*` be the unique solution of `R(t_*)=1`. For `eta=0`, one also has `c_*=(1-E_*)/3`, so `t_*` is exactly both PPT and EB onset by the [reversible theorem](reversible_proof.md). At the **same time** `t_*`, the biased-minus-unbiased PPT determinant is
```math
\Delta=\frac{2E_*(1-\cos\theta_*)[1-2E_*(1+\cos\theta_*)]}9.
```
For `0<=gamma<=1/2`, the root satisfies `E_*<=1/4` and `0<|theta_*|<2pi` whenever `eta!=0`. Both factors are positive (including the endpoint `gamma=1/2`, where the leading term becomes fourth order in bias). Hence the biased channel is **strictly PPT at** `t_*`. By continuity it stays PPT immediately before `t_*`, when `R>1`; these channels are PPT entangled, rather than EB. No formula for their exact EB time is asserted.

For `gamma=0`, the root and the weak-bias shift are
```math
t_*=-2\log[2\cos(2\pi/9)-1]=1.26188944840409\ldots,
```
```math
t_*-t_{\rm PPT}=K\eta^2+O(\eta^4),\qquad
K=\frac{3E_*(1-4E_*)t_*^2}{4(1-E_*)(E_*+2)}
=0.0391427404380864\ldots.
```
At `eta=1`, the PPT onset is approximately `1.21744501742`, with `R(t_PPT)~1.03265723>1`; at `t=5/4` it is still PPT entangled.

**Physical interpretation.** Classical circulation changes the orientation of population transfer without changing its nontrivial singular-value decay or the damping of individual coherences. The earlier onset of PPT means that **two-way distillable communication ends sooner** than in the reversible reference. The surviving correlations are bound entangled. This does not show an increase in the total entanglement lifetime or that the system is a more useful memory.
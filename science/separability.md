# Exact separability in the cyclic qutrit slice

Let $`p_0,p_1,p_2`$ be nonnegative with sum one. The trace-one state studied here is

```math
\rho(p,c)=\frac13\left(\sum_{i,j=0}^2 p_{i-j\bmod 3}|ij\rangle\langle ij|
+c\sum_{i\ne j}|ii\rangle\langle jj|\right),\qquad c\in\mathbb R.
```

Its diagonal block on the aligned pairs has eigenvalues $`(p_0+2c)/3`$ and $`(p_0-c)/3`$, the latter twice. Thus this is a state exactly when $`-p_0/2\le c\le p_0`$. Both reduced states are maximally mixed, so it is also a normalized Choi state. It includes the three-parameter Bell-diagonal family of [Bertlmann and Krammer](../references/RELATED_WORK.md#the-three-parameter-qutrit-slice).

## Criterion

Put $`z=p_0+\omega p_1+\omega^2p_2`$ with $`\omega=e^{2\pi i/3}`$. The state is separable if and only if both tests hold,

```math
p_1p_2\ge c^2,\qquad
\frac{1+2|z|}{3}+2|c|\le 1.
```

For positivity of the partial transpose, the three off-diagonal pair blocks each have determinant $`(p_1p_2-c^2)/9`$. For the second, the realigned matrix is a direct sum of the circulant population block divided by three and six scalar blocks with magnitude $`|c|/3`$. These tests are necessary for separability. The product decomposition below proves sufficiency on this slice.

## Product states and their coefficients

Let $`T`$ average local diagonal phase rotations $`U\otimes\overline U`$ and simultaneous cyclic shifts $`S^k\otimes S^k`$. Fix the first entry of $`U`$ to one and average its other two entries over third roots of unity. All off-pattern entries vanish. A twirled product gives coefficients $`(p_0,p_1,p_2;c)`$ in the normalization above, and the coefficients add under mixtures.

The product with both local vectors $`(1,1,1)/\sqrt3`$ has all four coefficients equal to $`1/3`$ after the twirl. For a second product, use the local vectors

```math
|x\rangle=(\sqrt{1-q},\,\pm\sqrt q,\,0)^T,\qquad
|y\rangle=(\sqrt q,\,\sqrt{1-q},\,0)^T,\qquad 0\lt q\lt 1.
```

The twirl gives $`(2q(1-q),q^2,(1-q)^2;\pm q(1-q))`$. Thus to contribute signed coherence of magnitude $`h`$, multiply the product orbit by $`h/[q(1-q)]`$. Its population costs are $`(2h,hR,h/R)`$ with $`R=q/(1-q)`$. A basis product and its cyclic shifts supply any unused population in a single sector without contributing coherence.

## How the two tests fund the decomposition

For $`c\ge0`$, set $`u=\max(0,2c-p_0)`$ and $`h=c-u`$. Positivity of the state gives $`0\le u\le c`$. Put weight $`3u`$ on the uniform product orbit. This contributes coherence $`u`$ and consumes $`u`$ from each population. The pair orbit must supply the remaining coherence $`h`$. Its aligned population requirement is within budget by construction, $`u+2h\le p_0`$.

Write $`q_1=p_1-u`$ and $`q_2=p_2-u`$ for the remaining off-aligned populations. If $`u=0`$, their product is at least $`h^2`$ by PPT. If $`u>0`$, PPT first gives $`q_1+q_2\ge 2h`$. Expanding the product and using $`p_0+p_1+p_2=1`$ gives

```math
q_1q_2-h^2=\frac{(1-3c)^2-|z|^2}{3}\ge0.
```

The inequality follows from realignment, which gives $`|z|\le1-3c`$. Together the product and sum bounds give $`q_1,q_2\ge0`$. If $`h>0`$, choose $`R=\sqrt{q_1/q_2}`$. Then $`hR\le q_1`$ and $`h/R\le q_2`$. If $`h=0`$, omit the pair orbit. Fill all remaining coefficients with cyclic averages of basis products. Each weight is nonnegative, and the weights sum to one because the reconstructed state has trace one.

For $`c<0`$, physical positivity already supplies $`p_0\ge2|c|`$. Set $`u=0`$, $`h=|c|`$, and use the negative relative sign in the pair orbit. PPT again supplies the remaining product bound. At $`c=0`$ the state is diagonal in a product basis.

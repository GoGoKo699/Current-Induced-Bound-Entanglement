# A separable decomposition from reversibility

Assume the [resolved-transition model](model.md) and faithful detailed balance. Fix a finite time $`t`$. Propagated detailed balance is

```math
P_{ij}(t)\pi_j=P_{ji}(t)\pi_i.
```

It follows either by exponentiating the generator's weighted symmetry or termwise from its power series. Keeping the identity in this form avoids division by transition probabilities that may vanish.

## 1. Nonnegative Gram factors

Put $`D_i=e^{-tq_i/2}`$ and extend the coherence matrix to its no-jump diagonal:

```math
C_{ij}=D_iD_j e^{-t\|v_i-v_j\|^2/2},\qquad C_{ii}=e^{-tq_i}.
```

For $`t>0`$ and $`m>0`$, define nonnegative normalized Gaussian functions

```math
f_i(x)=\left(\frac{2t}{\pi}\right)^{m/4}e^{-t\|x-v_i\|^2}.
```

Completing the square gives $`\int f_i(x)f_j(x)\,dx=e^{-t\|v_i-v_j\|^2/2}`$. Thus $`C`$ is an integral of outer products of nonnegative vectors. The finite-dimensional completely positive **matrix cone** is closed, so

```math
C=\sum_{k=1}^{K}a^{(k)}(a^{(k)})^T,\qquad a^{(k)}\ge0
```

for some finite $`K`$. This matrix-cone use of “completely positive” is different from complete positivity of a quantum channel. At $`t=0`$, or with no diagonal noise coordinates, the appropriate kernel is the all-ones matrix and the factorization is directly rank one after multiplying by the $`D_i`$. Closedness and nonnegative-factorization machinery are inherited mathematical ingredients; see [attribution](../references/RELATED_WORK.md).

## 2. Tilt each product state

For one factor $`a=a^{(k)}`$, take real nonnegative amplitudes satisfying

```math
|u_i|^2=a_i\sqrt{\pi_i},\qquad
|w_i|^2=a_i/\sqrt{\pi_i}.
```

The unnormalized product projector $`|u\rangle\langle u|\otimes|w\rangle\langle w|`$ is separable. Average it under $`U\otimes\overline U`$, with independent uniform diagonal phases. The average retains exactly the aligned coherences $`|ii\rangle\langle jj|`$ and the basis-state populations $`|ij\rangle\langle ij|`$. Summing these averages over $`k`$ produces

```math
\begin{aligned}
Z={}&\sum_{i,j}C_{ij}|ii\rangle\langle jj|\\
&+\sum_{i\ne j}C_{ij}\sqrt{\pi_i/\pi_j}|ij\rangle\langle ij|.
\end{aligned}
```

The diagonal $`|ii\rangle\langle ii|`$ is counted only once. Each summand is an average of product projectors, so $`Z`$ is separable. A finite average suffices: independent third roots of unity annihilate every nonzero phase exponent occurring in these fourth-order products.

## 3. The PPT inequalities pay for the residual

Faithful detailed balance and $`P_{ij}P_{ji}\ge c_{ij}^2`$ imply

```math
P_{ij}\ge c_{ij}\sqrt{\pi_i/\pi_j}\qquad(i\ne j).
```

This also covers vanishing transition probabilities; no ratio of two potentially zero probabilities is taken. On the diagonal, the classical event of making no transition gives $`P_{ii}(t)\ge e^{-tq_i}=C_{ii}`$.

All coherences of $`J_t-Z`$ vanish, and its remaining coefficients are

```math
\begin{cases}
P_{ii}-C_{ii},&i=j,\\
P_{ij}-c_{ij}\sqrt{\pi_i/\pi_j},&i\ne j.
\end{cases}
```

They are nonnegative. Therefore $`J_t-Z`$ is a nonnegative sum of basis product projectors. Together with the separability of $`Z`$, this proves the forward implication. Conversely, a separable Choi state is PPT. This completes the all-time equivalence.

## Why the assumptions matter

Faithful detailed balance supplies one consistent tilt for every pair; isolated pairwise PPT inequalities need not supply such a global tilt under circulation. Hermitian diagonal noise supplies a real Gaussian kernel. General complex diagonal dissipators can carry phases not removable by one output unitary, while unresolved transition operators can mix coherence sectors. Neither extension follows from the proof.

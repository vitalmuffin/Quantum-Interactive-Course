which has the solution (for any $\epsilon$ if $\mathbf{H}$ is time independent)

$$\psi(x, t + \epsilon) = \exp(-i\epsilon\mathbf{H}/\hbar)\psi(x, t). \quad (32)$$

Therefore, Eq. (18) expresses the operator $\exp(-i\epsilon\mathbf{H}/\hbar)$ by an approximate integral operator for small $\epsilon$.

From the point of view of Heisenberg one considers the position at time $t$, for example, as an operator $\mathbf{x}$. The position $\mathbf{x}'$ at a later time $t + \epsilon$ can be expressed in terms of that at time $t$ by the operator equation

$$\mathbf{x}' = \exp(i\epsilon\mathbf{H}/\hbar)\mathbf{x}\exp(-i\epsilon\mathbf{H}/\hbar). \quad (33)$$

The transformation theory of Dirac allows us to consider the wave function at time $t + \epsilon$, $\psi(x', t + \epsilon)$, as representing a state in a representation in which $\mathbf{x}'$ is diagonal, while $\psi(x, t)$ represents the same state in a representation in which $\mathbf{x}$ is diagonal. They are, therefore, related through the transformation function $(x'|x)_\epsilon$, which relates these representations:

$$\psi(x', t + \epsilon) = \int (x'|x)_\epsilon\psi(x, t)dx.$$

Therefore, the content of Eq. (18) is to show that for small $\epsilon$ we can set

$$(x'|x)_\epsilon = (1/A)\exp(iS(x', x)/\hbar) \quad (34)$$

with $S(x', x)$ defined as in (11).

The close analogy between $(x', |x)_\epsilon$ and the quantity $\exp(iS(x', x)/\hbar)$ has been pointed out on several occasions by Dirac.$^{17}$ In fact, we now see that to sufficient approximations the two quantities may be taken to be proportional to each other. Dirac's remarks were the starting point of the present development. The points he makes concerning the passage to the classical limit $\hbar \rightarrow 0$ are very beautiful, and I may perhaps be excused for briefly reviewing them here.

First we note that the wave function at $x''$ at time $t''$ can be obtained from that at $x'$ at time $t'$ by

$$\psi(x'', t'') = \lim_{\epsilon \rightarrow 0} \int \dots \int \times \times \exp\left[ \frac{i}{\hbar} \sum_{i=0}^{j-1} S(x_{i+1}, x_i) \right] \times \psi(x', t') \frac{dx_0}{A} \frac{dx_1}{A} \dots \frac{dx_{j-1}}{A}, \quad (35)$$

$^{17}$P. A. M. Dirac, *The Principles of Quantum Mechanics* (The Clarendon Press, Oxford, 1935), second edition, Section 33; also, Physik. Zeits. Sowjetunion **3**, 64 (1933).

20
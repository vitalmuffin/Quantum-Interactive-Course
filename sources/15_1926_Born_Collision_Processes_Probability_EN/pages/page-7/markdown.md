Born – Quantum mechanics of collision processes.

7

We examine the asymptotic behavior of the solution at infinity. In order to get a simple relationship, we assume that $V(x)$ vanishes faster than $x^{-2}$ at infinity; i.e.:

$$| V(x) | < \frac{K}{x^2}, \tag{4}$$

in which $K$ is a positive number ($^1$).

We now determine $\psi(x)$ by a process of iteration; let:

$$u_0(x) = e^{ikx}, \tag{5}$$

and let $u_1(x), u_2(x), \ldots$ be the solutions of the successive approximations:

$$\frac{d^2 u_n}{dx^2} + k^2 u_n = V u_{n-1},$$

which vanishes as $x \to +\infty$.

One then has:

$$u_n(x) = \frac{1}{k} \int_x^\infty u_{n-1}(\xi) V(\xi) \sin k(\xi - x) d\xi,$$

as one can verify directly. One has:

$$| u_n(x) | \le \frac{1}{k} \int_x^\infty | u_{n-1}(\xi) | \cdot | V(\xi) | d\xi.$$

We now show that:

$$| u_n(x) | \le \frac{1}{n!} \left( \frac{K}{kx} \right)^n.$$

This is correct for $n = 0$, since it follows from (5) that $| u_0(x) | \le 1$. We now assume that is it correct for $n - 1$:

$$| u_{n-1}(\xi) | \le \frac{1}{(n-1)!} \left( \frac{K}{k\xi} \right)^{n-1};$$

it then follows that:

$$| u_n(x) | \le \frac{1}{k} \frac{1}{(n-1)!} \left( \frac{K}{k} \right)^{n-1} \cdot K \int_x^\infty \xi^{-n+1} \xi^2 d\xi = \frac{1}{n!} \left( \frac{K}{kx} \right)^n,$$

as was asserted.

As a result, the series:

$$\psi(x) = \sum_{n=0}^\infty u_n(x) \tag{6}$$

($^1$) The cases of a pure Coulomb field and a dipole field are excluded by this assumption.
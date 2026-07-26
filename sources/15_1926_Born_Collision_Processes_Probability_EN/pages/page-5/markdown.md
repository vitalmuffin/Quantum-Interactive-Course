Born – Quantum mechanics of collision processes.

5

and expect that $|c(k)|^2$ will then be the measure of the frequency for the interval $\frac{1}{2\pi} dk$.

For a mixture of atoms for which the eigenfunctions appear in the distribution that is given by $c(k)$, let the number that is analogous to § 1, (4) be represented by the integral:

$$\int_{-\infty}^{+\infty} |\psi(x)|^2 dx = \frac{1}{(2\pi)^2} \int_{-\infty}^{+\infty} dx \left| \int_{-\infty}^{+\infty} c(k) e^{ikx} dk \right|^2. \tag{6}$$

If we take the case in which only the small interval $k_1 \le k \le k_2$ is occupied then:

$$\int_{-\infty}^{+\infty} c(k) e^{ikx} dk = \bar{c} \int_{k_1}^{k_2} e^{ikx} dk = \frac{\bar{c}}{ix} (e^{ik_2 x} - e^{ik_1 x}),$$

in which $\bar{c}$ is a mean value. One will then have:

$$\begin{aligned} \int_{-\infty}^{+\infty} |\psi(x)|^2 dx &= \frac{|\bar{c}|^2}{4\pi^2} \int_{-\infty}^{+\infty} \frac{dx}{x^2} (e^{ik_2 x} - e^{ik_1 x})(e^{-ik_2 x} - e^{-ik_1 x}) \\ &= \frac{|\bar{c}|^2}{4\pi^2} 4 \int_{-\infty}^{+\infty} \frac{dx}{x^2} \sin^2 \frac{k_2 - k_1}{2} = \frac{1}{2\pi} |\bar{c}|^2 (k_2 - k_1). \end{aligned}$$

Now, according to de Broglie, the impulse of the translatory motion that belongs to the eigenfunction (8) is equal to:

$$p = \frac{h}{\lambda} = \frac{h}{2\pi} k. \tag{7}$$

It is, perhaps, not superfluous to remark that one can also formulate this as a “matrix”; one must then define the matrices in the continuous spectrum here, not by integrals, but by mean values:

$$\begin{aligned} p(k, k') &= \frac{h}{2\pi i} \lim_{a \to \infty} \frac{1}{2a} \int_{-a}^{+a} \psi'(k, x) \frac{\partial \psi(k', x)}{\partial x} dx \\ &= \frac{h}{2\pi i} \lim_{a \to \infty} \frac{1}{2a} \int_{-a}^{+a} e^{-ikx} ik' e^{ik'x} dx. \end{aligned}$$

$$p(k, k') = \begin{cases} \frac{h}{2\pi} k & \text{ for } k = k', \\ 0 & \text{ " } k \neq k'. \end{cases} \tag{8}$$

If one now replaces $\Delta k = k_2 - k_1$ with $\frac{2\pi}{h} \Delta p$ then one will finally have:
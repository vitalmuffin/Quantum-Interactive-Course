Born – Quantum mechanics of collision processes.

4

$$W = \sum_n |c_n|^2 W_n. \quad (8)$$

According to our interpretation of the $|c_n|^2$, the right-hand side is the total energy of a system of atoms; this mean value can then be represented as the spatial integral of the energy density of the function $\psi$.

However, nothing will point to our Ansatz in favor of the others as long as we remain within the scope of periodic processes.

**§ 2. Aperiodic systems.** We now go on to the aperiodic processes and, for the sake of simplicity, we shall first consider the case of uniform, rectilinear motion along the $x$-axis. In that case, the differential equation reads:

$$\frac{d^2\psi}{dx^2} + k^2\psi = 0, \quad k^2 = \frac{8\pi^2\mu}{h^2}W; \quad (1)$$

it has all positive values $W$ for its eigenvalues and the eigenfunctions:

$$\psi = c e^{\pm ikx}.$$

In order to be able to define the weights and frequencies, one must, above all, normalize the eigenfunctions. The integral formula that is analogous to (2) breaks down (i.e., the integral is divergent); that is why one employs the “mean value” instead of it:

$$\lim_{a \to \infty} \frac{1}{2a} \int_{-a}^{+a} |\psi(k, x)|^2 dx = \lim_{a \to \infty} \frac{c^2}{2a} \int_{-a}^{+a} e^{ikx} e^{-ikx} dx = 1; \quad (2)$$

it follows from this that $c = 1$, and one has the *normalized eigenfunctions*:

$$\psi(k, x) = e^{\pm ikx}. \quad (3)$$

Any function of $x$ can be composed of these. In order to do that, one must choose the unit for the $k$-scale – i.e., one must establish which segments shall have the weight 1. For that, one considers the free motion to be a limiting case of a periodic one, namely, the eigenvibration of a finite piece of the $x$-axis. One then knows that the number per unit length and per interval $(k, k + dk)$ is equal to $\frac{\Delta k}{2\pi} = \Delta\left(\frac{1}{\lambda}\right)$, where $\lambda$ is the wave length. One will then set:

$$\psi(x) = \int_{-\infty}^{+\infty} c(k)\psi(k, x) d\frac{k}{2\pi} = \int_{-\infty}^{+\infty} c(k) e^{ikx} dk, \quad (4)$$

with

$$c(-k) = c^*(k) \quad (5)$$
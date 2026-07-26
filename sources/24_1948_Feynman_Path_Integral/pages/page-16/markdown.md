because of the almost complete cancelation of positive and negative contributions. Since only small $\xi$ are effective, $\psi(x - \xi, t)$ may be expanded as a Taylor series. Hence,

$$\psi(x, t + \epsilon) = \exp \left( \frac{-i\epsilon V(x)}{\hbar} \right) \times$$

$$\times \int \exp \left( \frac{im\xi^2}{2\hbar\epsilon} \right) \left[ \psi(x, t) - \xi \frac{\partial \psi(x, t)}{\partial x} + \frac{\xi^2}{2} \frac{\partial^2 \psi(x, t)}{\partial x^2} - \dots \right] d\xi / A. \quad (25)$$

Now

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) d\xi = (2\pi\hbar\epsilon i/m)^{1/2},$$

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) \xi d\xi = 0, \quad (26)$$

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) \xi^2 d\xi = (\hbar\epsilon i/m)(2\pi\hbar\epsilon i/m)^{1/2},$$

while the integral containing $\xi^2$ is zero, for like the one with $\xi$ it possesses an odd integrand, and the ones with $\xi^4$ are of at least the order $\epsilon$ smaller than the ones kept here.$^{13}$ If we expand the left-hand side to first order in $\epsilon$ (25) becomes

$$\psi(x, t) + \epsilon \frac{\partial \psi(x, t)}{\partial t} = \exp \left( \frac{-i\epsilon V(x)}{\hbar} \right) \frac{(2\pi\hbar\epsilon i/m)^{1/2}}{A} \times \left[ \psi(x, t) + \frac{\hbar\epsilon i}{m} \frac{\partial^2 \psi(x, t)}{\partial x^2} + \dots \right]. \quad (27)$$

In order that both sides may agree to zero order in $\epsilon$, we must set

$$A = (2\pi\hbar\epsilon i/m)^{1/2}. \quad (28)$$

Then expanding the exponential containing $V(x)$, we get

$$\psi(x, t) + \epsilon \frac{\partial \psi}{\partial t} = \left( 1 - \frac{i\epsilon}{\hbar} V(x) \right) \times \left( \psi(x, t) + \frac{\hbar\epsilon i}{2m} \frac{\partial^2 \psi}{\partial x^2} \right). \quad (29)$$

$^{13}$Really, these integrals are oscillatory and not defined, but they may be defined by using a convergence factor. Such a factor is automatically provided by $\psi(x - \xi, t)$ in (24). If a more formal procedure is desired replace $\hbar$ by $\hbar(1 - i\delta)$, for example, where $\delta$ is a small positive number, and then let $\delta \to 0$.

16
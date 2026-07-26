along a straight line. Under these circumstances it is sufficiently accurate to replace the integral by the trapezoidal rule

$$S(x_{i+1}, x_i) = \frac{\epsilon}{2} L \left( \frac{x_{i+1} - x_i}{\epsilon}, x_{i+1} \right) + \frac{\epsilon}{2} L \left( \frac{x_{i+1} - x_i}{\epsilon}, x_i \right) \tag{19}$$

or, if it proves more convenient,

$$S(x_{i+1}, x_i) = \epsilon L \left( \frac{x_{i+1} - x_i}{\epsilon}, \frac{x_{i+1} + x_i}{2} \right). \tag{20}$$

These are not valid in a general coordinate system, e.g., spherical. An even simpler approximation may be used if, in addition, there is no vector potential or other terms linear in the velocity (see page 376):

$$S(x_{i+1}, x_i) = \epsilon L \left( \frac{x_{i-1} - x_i}{\epsilon}, x_{i+1} \right). \tag{21}$$

Thus, for the simple example of a particle of mass $m$ moving in one dimension under a potential $V(x)$, we can set

$$S(x_{i+1}, x_i) = \frac{m\epsilon}{2} \left( \frac{x_{i+1} - x_i}{\epsilon} \right) - \epsilon V(x_{i+1}). \tag{22}$$

For this example, then, Eq. (18) becomes

$$\psi(x_{k+1}, t + \epsilon) = \int \exp \left[ \frac{i\epsilon}{\hbar} \left\{ \frac{m}{2} \left( \frac{x_{k+1} - x_k}{\epsilon} \right)^2 - \right. \right. \\ \left. \left. - V(x_{k+1}) \right\} \right] \psi(x_k, t) dx_k / A. \tag{23}$$

Let us call $x_{k+1} = x$ and $x_{k+1} - x_k = \xi$ so that $x_k = x - \xi$. Then (23) becomes

$$\psi(x, t + \epsilon) = \int \exp \frac{im\xi^2}{\epsilon \cdot 2\hbar} \cdot \exp \frac{-i\epsilon V(x)}{\hbar} \cdot \psi(x - \xi, t) \frac{d\xi}{A}. \tag{24}$$

The integral on $\xi$ will converge if $\psi(x, t)$ falls off sufficiently for large $x$ (certainly if $\int \psi^*(x) \psi(x) dx = 1$). In the integration on $\xi$, since $\epsilon$ is very small, the exponential of $im\xi^2/2\hbar\epsilon$ oscillates extremely rapidly except in the region about $\xi = 0$ ($\xi$ of order $(\hbar\epsilon/m)^{1/2}$). Since the function $\psi(x - \xi, t)$ is a relatively smooth function of $\xi$ (since $\epsilon$ may be taken as small as desired), the region where the exponential oscillates rapidly will contribute very little

15
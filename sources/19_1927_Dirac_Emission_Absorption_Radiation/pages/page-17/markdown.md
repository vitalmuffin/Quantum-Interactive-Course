For values of the $\alpha'_k$ such that $W(\alpha')$ differs appreciably from $W(\alpha^0), a(\alpha')$ is a periodic function of the time whose amplitude is small when the perturbing energy $V$ is small, so that the eigenfunctions corresponding to these stationary states are not excited to any appreciable extent. On the other hand, for values of the $\alpha'_k$ such that $W(\alpha') = W(\alpha^0)$ and $\alpha'_k \neq \alpha^0_k$ for some $k, a(\alpha')$ increases uniformly with respect to the time, so that the probability of the system being in the state $\alpha'$ at any time increases proportionally with the square of the time. Physically, the probability of the system being in a state with exactly the same proper energy as the initial proper energy $W(\alpha^0)$ is of no importance, being infinitesimal. We are interested only in the integral of the probability through a small range of proper energy values about the initial proper energy, which, as we shall find, increases linearly with the time, in agreement with the ordinary probability laws.

We transform from the variables $\alpha_1, \alpha_2 \dots \alpha_u$ to a set of variables that are arbitrary independent functions of the $\alpha$'s such that one of them is the proper energy $W$, say, the variables $W, \gamma_1, \gamma_2, \dots \gamma_{u-1}$. The probability at any time of the system lying in a stationary state for which each $\gamma_k$ lies between $\gamma'_k$ and $\gamma'_k + d\gamma'_k$ is now (apart from the normalising factor) equal to

$$d\gamma'_1 \cdot d\gamma'_2 \dots d\gamma_{u-1} \int |a(\alpha')|^2 \frac{\partial(\alpha'_1, \alpha'_2 \dots \alpha'_u)}{\partial(W', \gamma'_1 \dots \gamma'_{u-1})}. \quad (23)$$

For a time that is large compared with the periods of the system we shall find that practically the whole of the integral in (23) is contributed by values of $W'$ very close to $W^0 = W(\alpha^0)$. Put

$$a(\alpha') = a(W', \gamma') \quad \text{and} \quad \partial(\alpha'_1, \alpha'_2 \dots \alpha'_u) / \partial(W', \gamma'_1 \dots \gamma'_{u-1}) = J(W', \gamma').$$

Then for the integral in (23) we find, with the help of (22) (provided $\gamma'_k \neq \gamma^0_k$ for some $k$)

$$\begin{aligned} &\int |a(W', \gamma')|^2 J(W', \gamma') dW' = |a^0|^2 \int |v(W', \gamma'; W^0, \gamma^0)|^2 J(W', \gamma') \\ &= \frac{[e^{i(W'-W^0)t/h} - 1][e^{-i(W'-W^0)t/h} - 1]}{(W' - W^0)^2} dW' \\ &= \frac{2|a^0|^2 \int |v(W', \gamma'; W^0, \gamma^0)|^2 J(W', \gamma') [1 - \cos(W' - W^0)t/h]}{(W' - W^0)^2 \cdot dW'} \\ &= \frac{2|a^0|^2 t/h \cdot \int |v(W^0 + hx/t, \gamma'; W^0, \gamma^0)|^2 J(W^0 + hx/t, \gamma') (1 - \cos x)}{x^2 \cdot dx}, \end{aligned}$$

17
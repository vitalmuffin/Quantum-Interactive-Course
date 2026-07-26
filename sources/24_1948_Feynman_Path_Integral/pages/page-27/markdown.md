would require the factors in the second term on the left to be reversed in order. We see, therefore, that it corresponds to

$$\mathbf{px} - \mathbf{xp} = \hbar/i$$

where we have written $\mathbf{p}$ for the operator $m\hat{\mathbf{x}}$.

The relation between functionals and the corresponding operators is denned above in terms of the order of the factors in time. It should be remarked that this rule must be especially carefully adhered to when quantities involving velocities or higher derivatives are involved. The correct functional to represent the operator $(\dot{x})^2$ is actually $(x_{k+1} - x_k)/\epsilon(x_k - x_{k-1})/\epsilon$ rather than $[(x_{k+1} - x_k)/\epsilon]^2$. The latter quantity diverges as $1/\epsilon$ as $\epsilon \to 0$. This may be seen by replacing the second term in (49) by its value $x_{k+1} \cdot m(x_{k+1} - x_k)/\epsilon$ calculated an instant $\epsilon$ later in time. This does not change the equation to zero order in $\epsilon$. We then obtain (dividing by $\epsilon$)

$$\left(\frac{x_{k+1} - x_k}{\epsilon}\right)^2 \underset{S}{\leftrightarrow} -\frac{\hbar}{im\epsilon}. \tag{50}$$

This gives the result expressed earlier that the root mean square of the “velocity” $(x_{k+1} - x_k)/\epsilon$ between two successive positions of the path is of order $\epsilon^{-1/2}$.

It will not do then to write the functional for kinetic energy, say, simply as

$$\frac{1}{2}m[(x_{k+1} - x_k)/\epsilon]^2 \tag{51}$$

for this quantity is infinite as $\epsilon \to 0$. In fact, it is not an observable functional.

One can obtain the kinetic energy as an observable functional by considering the first-order change in transition amplitude occasioned by a change in the mass of the particle. Let $m$ be changed to $m(1 + \delta)$ for a short time, say $\epsilon$, around $t_k$. The change in the action is $\frac{1}{2}\delta\epsilon m[x_{k+1} - x_k)/\epsilon]^2$ the derivative of which gives an expression like (51). But the change in $m$ changes the normalization constant $1/A$ corresponding to $dx_k$ as well as the action. The constant is changed from $(2\pi\hbar\epsilon i/m)^{-1/2}$ to $(2\pi\hbar\epsilon i/m(1 + \delta))^{-1/2}$ or by $\frac{1}{2}\delta(2\pi\hbar\epsilon i/m)^{-1/2}$ to first order in $\delta$. The total effect of the change in mass in Eq. (38) to the first order in $\delta$ is

$$\langle\chi_{t'}|\frac{1}{2}\delta\epsilon im[(x_{k+1} - x_k)/\epsilon]^2/\hbar + \frac{1}{2}\delta|\psi_{t'}\rangle.$$

27
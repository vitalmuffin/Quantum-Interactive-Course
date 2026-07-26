is the statement of operator equations in the new language.

If $F$ depends on the various coordinates, we can, of course, define a new functional $\partial F/\partial x_k$ by differentiating it with respect to one of its variables, say $x_k (0 < k < j)$. If we calculate $\langle \chi_{t'} | \partial F/\partial x_k | \psi_{t'} \rangle_S$ by (39) the integral on the right-hand side will contain $\partial F/\partial x_k$. The only other place that the variable $x_k$ appears is in $S$. Thus, the integration on $x_k$ can be performed by parts. The integrated part vanishes (assuming wave functions vanish at infinity) and we are left with the quantity $-F(\partial/\partial x_k)\exp(iS/\hbar)$ in the integral. However, $(\partial/\partial x_k)\exp(iS/\hbar) = (i/\hbar)(\partial S/\partial x_k)\exp(iS/\hbar)$, so the right side represents the transition element of $-(i/\hbar)F(\partial S/\partial x_k)$, i.e.,

$$\left\langle \chi_{t'} \left| \frac{\partial F}{\partial x_k} \right| \psi_{t'} \right\rangle_S = -\frac{i}{\hbar} \left\langle \chi_{t'} \left| F \frac{\partial S}{\partial x_k} \right| \psi_{t'} \right\rangle_S. \tag{45}$$

This very important relation shows that two different functionals may give the same result for the transition element between any two states. We say they are equivalent and symbolize the relation by

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \frac{\partial S}{\partial x_k}, \tag{46}$$

the symbol $\underset{S}{\leftrightarrow}$ emphasizing the fact that functionals equivalent under one action may not be equivalent under another. The quantities in (46) need not be observable. The equivalence is, nevertheless, true. Making use of (36) one can write

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \left[ \frac{\partial S(x_{k+1}, x_k)}{\partial x_k} + \frac{\partial S(x_k, x_{k-1})}{\partial x_k} \right]. \tag{47}$$

This equation is true to zero and first order in $\epsilon$ and has as consequences the commutation relations of momentum and coordinate, as well as the Newtonian equations of motion in matrix form.

In the case of our simple one-dimensional problem, $S(x_{i+1}, x_i)$ is given by the expression (15), so that

$$\partial S(x_{k+1}, x_k)/\partial x_k = -m(x_{k+1} - x_k)/\epsilon,$$

and

$$\partial S(x_k, x_{k-1})/\partial x_k = +m(x_k - x_{k-1})/\epsilon - \epsilon V'(x_k);$$

where we write $V'(x)$ for the derivative of the potential, or force. Then (47) becomes

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \left[ -m \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - \epsilon V'(x_k) \right]. \tag{48}$$

25
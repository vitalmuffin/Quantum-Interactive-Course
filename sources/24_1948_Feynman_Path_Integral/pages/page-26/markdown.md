If $F$ does not depend on the variable $x_k$, this gives Newton's equations of motion. For example, if $F$ is constant, say unity, (48) just gives (dividing by $\epsilon$)

$$0 \leftrightarrow_S -\frac{m}{\epsilon} \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - V'(x_k).$$

Thus, the transition element of mass times acceleration $[(x_{k+1} - x_k)/\epsilon - (x_k - x_{k-1})/\epsilon]/\epsilon$ between any two states is equal to the transition element of force $-V'(x_k)$ between the same states. This is the matrix expression of Newton's law which holds in quantum mechanics.

What happens if $F$ does depend upon $x_k$? For example, let $F = x_k$. Then (48) gives, since $\partial F/\partial x_k = 1$,

$$-\frac{\hbar}{i} \leftrightarrow_S x_k \left[ -m \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - \epsilon V'(x_k) \right]$$

or, neglecting terms of order $\epsilon$,

$$m \left( \frac{x_{k+1} - x_k}{\epsilon} \right) x_k - m \left( \frac{x_k - x_{k-1}}{\epsilon} \right) x_k \leftrightarrow_S \frac{\hbar}{i}. \quad (49)$$

In order to transfer an equation such as (49) into conventional notation, we shall have to discover what matrix corresponds to a quantity such as $x_k x_{k+1}$. It is clear from a study of (39) that if $F$ is set equal to, say, $f(x_k)g(x_{k+1})$, the corresponding operator in (40) is

$$e^{-(i/\hbar)(t'' - t - \epsilon)\mathbf{H}} g(\mathbf{x}) e^{-(i/\hbar)\epsilon\mathbf{H}} f(\mathbf{x}) e^{-(i/\hbar)(t - t')\mathbf{H}},$$

the matrix element being taken between the states $\chi_{t''}$ and $\psi_{t'}$. The operators corresponding to functions of $x_{k+1}$ will appear to the left of the operators corresponding to functions of $x_k$, i.e., *the order of terms in a matrix operator product corresponds to an order in time of the corresponding factors in a functional*. Thus, if the functional can and is written in such a way that in each term factors corresponding to later times appear to the left of factors corresponding to earlier terms, the corresponding operator can immediately be written down if the order of the operators is kept the same as in the functional. $^{19}$ Obviously, the order of factors in a functional is of no consequence. The ordering just facilitates translation into conventional operator notation. To write Eq. (49) in the way desired for easy translation

$^{19}$Dirac has also studied operators containing quantities referring to different times. See reference 2.

26
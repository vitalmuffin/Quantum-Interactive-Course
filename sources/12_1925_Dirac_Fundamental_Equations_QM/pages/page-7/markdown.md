Fundamental Equations of Quantum Mechanics.

647

Equation (5) now reduces to

$$\begin{array}{l} dx/dv(nm) = \Sigma_{m' \neq m} a(nm; nm') x(nm') + \Sigma_{n' \neq n} a(nm; n'm) x(n'm) \\ \hspace{2.5em} + a(nm; nm) x(nm) \\ \hspace{2.5em} = \Sigma_{m' \neq m} a(m'm) x(nm') - \Sigma_{n' \neq n} a(nn') x(n'm) \\ \hspace{2.5em} + \{a(mm) - a(nn)\} x(nm) \\ \hspace{2.5em} = \Sigma_k \{x(nk) a(km) - a(nk) x(km)\}. \end{array}$$

Hence

$$dx/dv = xa - ax. \tag{8}$$

Thus the most general operation satisfying the laws I and II that one can perform upon a quantum variable is that of taking the difference of its Heisenberg products with some other quantum variable. It is easily seen that one cannot in general change the order of differentiations, i.e.,

$$\frac{d^2x}{du dv} \neq \frac{d^2x}{dv du}.$$

As an example in quantum differentiation we may take the case when (a) is a constant, so that a (nm) = 0 except when n = m. We get

$$dx/dv(nm) = x(nm) a(mm) - a(nn) x(nm).$$

In particular, if ia (mm) = Ω (m), the frequency level previously introduced, we have

$$dx/dv(nm) = i\omega(nm) x(nm),$$

and our differentiation with respect to v becomes ordinary differentiation with respect to t.

# § 4. The Quantum Conditions.

We shall now consider to what the expression (xy - yx) corresponds on the classical theory. To do this we suppose that x (n, n - α) varies only slowly with the n's, the n's being large numbers and the α's small ones, so that we can put

$$x(n, n - \alpha) = x_{\alpha\kappa}$$

where κ_r = n_r h or (n_r + α_r) h, these being practically equivalent. We now have

$$\begin{array}{l} x(n, n - \alpha) y(n - \alpha, n - \alpha - \beta) - y(n, n - \beta) x(n - \beta, n - \alpha - \beta) \\ \hspace{2.5em} = \{x(n, n - \alpha) - x(n - \beta, n - \beta - \alpha)\} y(n - \alpha, n - \alpha - \beta) \\ \hspace{2.5em} - \{y(n, n - \beta) - y(n - \alpha, n - \alpha - \beta)\} x(n - \beta, n - \alpha - \beta). \\ \hspace{2.5em} = h\Sigma_r \left\{ \beta_r \frac{\partial x_{\alpha\kappa}}{\partial \kappa_r} y_{\beta\kappa} - \alpha_r \frac{\partial y_{\beta\kappa}}{\partial \kappa_r} x_{\alpha\kappa} \right\}. \tag{9} \end{array}$$
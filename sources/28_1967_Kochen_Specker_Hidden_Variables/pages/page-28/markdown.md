QUANTUM MECHANICS

85

Let $K_1$ be the set of all equations of the form $\alpha + \beta = \gamma$ or $\xi\eta = \zeta$ which subsist among elements of $\mathfrak{N}$. (In the language of model theory, $K_1$ denotes the positive statements from the diagram of $\mathfrak{N}$.) Let $K_2$ be the elementary axioms describing the class of Boolean algebras. Write $K = K_1 \cup K_2$. Then the class of all models of $K$ consist precisely of the homomorphic images of $\mathfrak{N}$ which are Boolean algebras.

Suppose now that $\mathfrak{N}$ does not satisfy condition (i) ($i = 1, 2, \text{or } 3$). Then by Theorem 0 and its counterpart for weak imbeddings there exist two distinct elements $a, b$ in $\mathfrak{N}$ such that for every Boolean algebra $B$ and every homomorphism $h : \mathfrak{N} \to B$ we have $h(s_i(a)) = h(t_i(b))$. Since then $s_i(a)$ and $t_i(b)$ are identified in every model of $K$, we have by the Completeness Theorem for the Predicate Calculus that

$$K \vdash s_i(a) = t_i(b).$$

Hence, there is a finite subset

$$L = \{\alpha_j + \beta_j = \gamma_j, \xi_k\eta_k = \zeta_k \mid 1 \leq j \leq n, 1 \leq k \leq m\}$$

of $K_1$ such that

$$K_2 \cup L \vdash s_i(a) = t_i(b)$$

so that

$$K_2 \vdash (\bigwedge_i (\alpha_j + \beta_j + \gamma_j = 0) \wedge \bigwedge_k (\xi_k\eta_k + \zeta_k = 0)) \to s_i(a) = t_i(b)$$

or

$$K_2 \vdash (\bigvee_{j,k} (\alpha_j + \beta_j + \gamma_j)(\xi_k\eta_k + \zeta_k) = 0) \to s_i(a) = t_i(b),$$

i.e., $K_2 \vdash \rho(\alpha_1, \cdots, \zeta_m) = 0 \to s_i(a) = t_i(b)$ where

$$\rho(\alpha_1, \cdots, \zeta_m) = \bigvee_{j,k} (\alpha_j + \beta_j + \gamma_j)(\xi_k\eta_k + \zeta_k).$$

Since the constants $\alpha_1, \cdots, \zeta_m, a, b$ do not occur in $K_2$, we may replace them by variables $x_1, \cdots, x_n, x, y$ to obtain

$$(10) \quad K_2 \vdash \rho(x_1, \cdots, x_n) = 0 \to s_i(x) = t_i(y).$$

Hence, the implication $\rho(x_1, \cdots, x_n) = 0 \to s_i(x) = t_i(y)$ is valid in all Boolean algebras. Let

$$\varphi \text{ denote } s_i(x) \to \rho$$

and

$$\psi \text{ denote } t_i(y) \to \rho.$$

Then it follows from (10) that $\varphi = \psi$ is Boolean identity, i.e., $\varphi \equiv \psi$ is a classical tautology. (Note that for $i = 2, 3, \psi = 1$ so that $\varphi \equiv \psi$ reduces to $\varphi$.) On the other hand the substitution of the elements $\alpha_1, \cdots, \zeta_m, s_i(a), t_i(b)$ from $\mathfrak{N}$

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms
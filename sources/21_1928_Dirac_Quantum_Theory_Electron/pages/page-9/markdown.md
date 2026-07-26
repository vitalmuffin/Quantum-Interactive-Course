618

P. A. M. Dirac.

# § 4. The Hamiltonian for an Arbitrary Field.

To obtain the Hamiltonian for an electron in an electromagnetic field with scalar potential $A_0$ and vector potential $\mathbf{A}$, we adopt the usual procedure of substituting $p_0 + e/c \cdot A_0$ for $p_0$ and $\mathbf{p} + e/c \cdot \mathbf{A}$ for $\mathbf{p}$ in the Hamiltonian for no field. From equation (9) we thus obtain

$$\left[ p_0 + \frac{e}{c} A_0 + \rho_1 \left( \boldsymbol{\sigma}, \mathbf{p} + \frac{e}{c} \mathbf{A} \right) + \rho_3 mc \right] \psi = 0. \quad (14)$$

This wave equation appears to be sufficient to account for all the duplexity phenomena. On account of the matrices $\rho$ and $\sigma$ containing four rows and columns, it will have four times as many solutions as the non-relativity wave equation, and twice as many as the previous relativity wave equation (1). Since half the solutions must be rejected as referring to the charge $+e$ on the electron, the correct number will be left to account for duplexity phenomena. The proof given in the preceding section of invariance under a Lorentz transformation applies equally well to the more general wave equation (14).

We can obtain a rough idea of how (14) differs from the previous relativity wave equation (1) by multiplying it up analogously to (5). This gives, if we write $e'$ for $e/c$

$$\begin{aligned} 0 &= \left[ - (p_0 + e' A_0) + \rho_1 (\boldsymbol{\sigma}, \mathbf{p} + e' \mathbf{A}) + \rho_3 mc \right] \\ &\quad \times \left[ (p_0 + e' A_0) + \rho_1 (\boldsymbol{\sigma}, \mathbf{p} + e' \mathbf{A}) + \rho_3 mc \right] \psi \\ &= \left[ - (p_0 + e' A_0)^2 + (\boldsymbol{\sigma}, \mathbf{p} + e' \mathbf{A})^2 + m^2 c^2 \right. \\ &\quad \left. + \rho_1 \left\{ (\boldsymbol{\sigma}, \mathbf{p} + e' \mathbf{A}) (p_0 + e' A_0) - (p_0 + e' A_0) (\boldsymbol{\sigma}, \mathbf{p} + e' \mathbf{A}) \right\} \right] \psi. \quad (15) \end{aligned}$$

We now use the general formula, that if $\mathbf{B}$ and $\mathbf{C}$ are any two vectors that commute with $\boldsymbol{\sigma}$

$$\begin{aligned} (\boldsymbol{\sigma}, \mathbf{B}) (\boldsymbol{\sigma}, \mathbf{C}) &= \Sigma \sigma_1^2 B_1 C_1 + \Sigma (\sigma_1 \sigma_2 B_1 C_2 + \sigma_2 \sigma_1 B_2 C_1) \\ &= (\mathbf{B}, \mathbf{C}) + i \Sigma \sigma_3 (B_1 C_2 - B_2 C_1) \\ &= (\mathbf{B}, \mathbf{C}) + i (\boldsymbol{\sigma}, \mathbf{B} \times \mathbf{C}). \quad (16) \end{aligned}$$

Taking $\mathbf{B} = \mathbf{C} = \mathbf{p} + e' \mathbf{A}$, we find

$$\begin{aligned} (\boldsymbol{\sigma}, \mathbf{p} + e' \mathbf{A})^2 &= (\mathbf{p} + e' \mathbf{A})^2 + i \Sigma \sigma_3 \\ &\quad \left[ (p_1 + e' A_1) (p_2 + e' A_2) - (p_2 + e' A_2) (p_1 + e' A_1) \right] \\ &= (\mathbf{p} + e' \mathbf{A})^2 + h e' (\boldsymbol{\sigma}, \operatorname{curl} \mathbf{A}). \end{aligned}$$
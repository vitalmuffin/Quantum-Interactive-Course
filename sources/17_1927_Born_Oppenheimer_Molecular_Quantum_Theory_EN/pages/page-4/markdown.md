This represents the electronic motion for stationary nuclei. We assume this eigenvalue problem is solved. The eigenvalues depend only on the functions $\xi_i$ of the $X_i$; then one can use the coordinate system defined by the principal axes of inertia, i.e. let $X_i = \bar{X}_i(\xi)$. In this system of axes, the eigenfunctions depend, besides on $x_k$, only on the $\xi_i$; however, if one transforms back to the arbitrary space-fixed axes, the $\theta_i$ again become involved.

We designate the $n$th eigenvalue and the corresponding normalized eigenfunction as

$$W = V_n(\xi) \quad \psi = \phi_n(x; \xi, \theta) \tag{14}$$

so that the identity

$$\left\{ H_0 \left( x, \frac{\partial}{\partial x}; \xi, \theta \right) - V_n(\xi) \right\} \phi_n(x; \xi, \theta) = 0 \tag{15}$$

is valid. Here we assume that $V_n$ is a nondegenerate eigenvalue. As a matter of fact, this is never the case since the indistinguishability of the electrons introduces the resonance degeneracy, discovered by Heisenberg and Dirac; for diatomic molecules there is an additional degeneracy of the angular momentum about the axis. But since we are concerned here only with the systematics of the approximation procedure, we will not consider these degeneracies. Their consideration would result in secular equations in the higher approximation.

The most important goal of our investigation is the proof that the function $V_n(\xi)$ plays the role of a potential for the nuclear motion. For this we must have several auxiliary formulas which will be derived now. It is necessary to show that the matrix corresponding to the derivative of the operator $H_0(x, \frac{\partial}{\partial x}; \xi, \theta)$ with respect to $\xi_i$, (for constant $x, \frac{\partial}{\partial x}$) can be related to the derivative of the function $V_n(\xi)$.

Instead of taking the derivative with respect to the $\xi_i$ directly, we replace the $\xi_i$ by $\xi_i + \kappa\zeta_i$ and differentiate with respect to $\kappa$; the coefficient of a power of $\kappa$ is then a homogeneous polynomial in $\zeta_i$, these coefficients being derivatives with respect to $\xi_i$. Thus we write

$$V_n(\xi + \kappa\zeta) = V_n^{(0)} + \kappa V_n^{(1)} + \kappa^2 V_n^{(2)} + \dots, \tag{16}$$

where

$$\begin{array}{l} \text{a)} \quad V_n^{(0)} = V_n(\xi) \\ \text{b)} \quad V_n^{(1)} = \sum_i \zeta_i \frac{\partial V_n}{\partial \xi_i} \\ \text{c)} \quad V_n^{(2)} = \frac{1}{2} \sum_{ij} \zeta_i \zeta_j \frac{\partial^2 V_n}{\partial \xi_i \partial \xi_j}, \end{array} \tag{17}$$

...

and correspondingly

$$\begin{array}{l} H_0 = H_0^{(0)} + \kappa H_0^{(1)} + \kappa^2 H_0^{(2)} + \dots \\ \phi_n = \phi_n^{(0)} + \kappa \phi_n^{(1)} + \kappa^2 \phi_n^{(2)} + \dots \\ \dots \dots \dots \dots \dots \end{array} \tag{18}$$

One can now develop the quantities $\phi_n^{(1)}, \phi_n^{(2)}$ in the eigenfunctions $\phi_n^{(0)}(x; \xi, \theta)$, setting

$$\begin{array}{l} \text{a)} \quad \phi_n^{(1)} = \sum_{n'} u_{nn'}^{(1)} \phi_{n'}^{(0)}, \\ \text{b)} \quad \phi_n^{(2)} = \sum_{n'} u_{nn'}^{(2)} \phi_{n'}^{(0)}. \end{array} \tag{19}$$

4
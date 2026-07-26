76

S. KOCHEN & E. P. SPECKER

Let $V$ be the set of operators in $H_2$ of trace zero. $V$ forms a 3-dimensional vector space over $\mathbf{R}$. This is easily seen by noting that the Pauli spin matrices

$$\sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad \sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad \sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$

form an orthonormal basis for $V$. If we assign to $(\sigma_x, \sigma_y, \sigma_z)$ an orthonormal basis $(i, j, k)$ in 3-dimensional Euclidean space $E^3$, we obtain a vector isomorphism $P: V \to E^3$. To every spin matrix $\sigma$, i.e., a matrix $\sigma$ in $V$ with eigenvalues $\pm 1$, there corresponds under the map $P$ a point $P_\sigma$ on the unit sphere $S^2$ in $E^3$. Physically, one speaks of the spin matrix $\sigma$ as corresponding to the observable “the spin angular momentum of the electron (say) in the direction $0P_\sigma$,” where $0$ is the origin in $E^3$.

Now let $A$ be any matrix in $H_2$ with distinct eigenvalues $\lambda_1, \lambda_2$. We let

$$\sigma(A) = \left( \frac{2}{\lambda_1 - \lambda_2} \right) A - \left( \frac{\lambda_1 + \lambda_2}{\lambda_1 - \lambda_2} \right) I.$$

Then $\sigma(A)$ is a spin matrix such that the eigenvectors of $\sigma(A)$ corresponding to $+1$ and $-1$ are the same as the eigenvectors of $A$ corresponding to $\lambda_1$ and $\lambda_2$ respectively.

We are now ready to choose the appropriate space $\Omega$ and functions $f_A$. For $\Omega$ we choose $S^2$. If $A \in H_2$ with distinct eigenvalues $\lambda_1$ and $\lambda_2$, we let

$$f_A(p) = \begin{cases} \lambda_1 & \text{for } p \in S^*_{P_\sigma(A)} \\ \lambda_2 & \text{otherwise.} \end{cases}$$

Here $S^*_{P_\sigma(A)}$ denotes the upper hemisphere of $S^2$ with the North Pole at $P_{\sigma(A)}$. If the eigenvalues of $A$ are equal, so that $A = \lambda I$, say, then we let

$$f_A(p) = \lambda, \quad \text{for all} \quad p \in S^2.$$

With this definition, it is a simple matter to check that the condition (I): $f_{u(A)} = u(f_A)$ holds. We need only note that for 2-dimensional operators it is sufficient to consider linear functions: $u(A) = \alpha A + \beta I$, with $\alpha, \beta \in \mathbf{R}$. Then condition (I) follows immediately from the fact that $\sigma_{\alpha A + \beta I} = \sigma_A$.

Next we wish to assign a probability measure $\mu_\psi$ to each vector $\psi \in U^2$. Let $\sigma_\psi$ denote the spin matrix for which $\psi$ is the eigenvector belonging to the eigenvalue $+1$. We may thus assign to each $\psi \in U^2$ a point $P_{\sigma_\psi}$ of $S^2$. We shall write $P_\psi$ for $P_{\sigma_\psi}$. Physically, if $\psi$ is the state vector of an electron, then the electron is said to have “spin in the direction $0P_\psi$.”

To delimit the problem and at the same time to obtain a solution with natural isotropy properties, we shall assume that the probability measures $\mu_\psi$ satisfy the following conditions:

(a) For each $\psi \in U^2$, the measure $\mu_\psi$ arises from a continuous probability density $u_\psi(p)$ on $S^2$, so that

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms
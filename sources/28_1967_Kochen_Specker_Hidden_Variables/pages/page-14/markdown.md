QUANTUM MECHANICS

71

4. The operators as observables. Let us consider a system in which the total angular momentum operator $\bar{J}$ commutes with the Hamiltonian operator $H$, so that $\bar{J}$ is a constant of the motion. We assume further that the system is in a state for which the principal quantum number $n = 2$ and the azimuthal quantum number $j = 1$, so that the total angular momentum is $\sqrt{2}\hbar$. The eigenspace $N$ corresponding to the eigenvalue $2\hbar^2$ of $J^2$ is three-dimensional. We adopt the convention that $\hbar = 1$.

Let $J_x$, $J_y$, and $J_z$ be the components of $\bar{J}$ in three mutually orthogonal directions $x$, $y$, and $z$. We shall show that in the three dimensional representation given by $n = 2$, $j = 1$ the following relations hold.

$$(7) \quad [J_x^2, J_y^2] = [J_y^2, J_z^2] = [J_z^2, J_z^2] = 0.$$

In the usual representation in which $J^2$ and $J_z$ are diagonal we have (see Schiff [14] p. 146)

$$J_z = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{bmatrix}, \quad J_x = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \quad J_y = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 & -i & 0 \\ i & 0 & -i \\ 0 & i & 0 \end{bmatrix}.$$

It is now easily checked that the relations (7) follow. It may be of some interest to give a coordinate-free proof of these relations. The following proof was suggested to us by J. Chaiken. Let $J_\pm = J_x \pm iJ_y$. From the commutation relations $[J_x, J_y] = iJ_x$, etc., for $J_x$, $J_y$, and $J_z$ it follows that

$$[J_x^2, J_y^2] = (J_x - I)J_+^2 - (J_x + I)J_-^2.$$

Now if $J_x\psi = m\psi$ then

$$J_x J_+ \psi = \begin{cases} (m+1)J_+ \psi & \text{if } -j \le m < j \\ 0 & \text{if } m = j. \end{cases}$$

Hence, if $\varphi$ is any vector in the three-dimensional representation ($n = 2$, $j = 1$), then $J_+\varphi$ is either zero or an eigenvector of $J_z$ with eigenvalue $+1$. In either case, $(J_x - I)J_+\varphi = 0$. Hence $(J_x - I)J_+^2 = 0$ in this representation. Similarly, $(J_x + I)J_-^2 = 0$, so that $[J_x^2, J_y^2] = 0$. This establishes (7). Note that these relations do not hold in any higher dimensional representation.

We now show that there is an imbedding $\psi$ of the partial Boolean algebra $\mathbf{B}(E^3)$ into the partial Boolean algebra $\mathfrak{B}$ of quantum mechanical proposition. Let $P$ be the projection operator belonging to the 3-dimensional eigenspace $N$. To each one-dimensional linear subspace $\alpha$ of $E^3$ there corresponds an operator $J_\alpha$, the component of angular momentum in the direction in physical space defined by $\alpha$. Let $\psi(\alpha) = PJ_\alpha^2$. If $\beta$ is a two-dimensional linear subspace of $E^3$ let $\alpha$ be the orthogonal complement of $\beta$ in $E^3$. We define $\psi(\beta) = P - PJ_\alpha^2$. Finally we let $\psi(E^3) = P$ and $\psi(0) = 0$. This defines the map $\psi$. To show that $\psi$ is an imbedding it clearly suffices to prove that if $\alpha$ and $\beta$ are

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms
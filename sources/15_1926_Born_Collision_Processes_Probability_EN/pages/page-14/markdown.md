Born – Quantum mechanics of collision processes.

14

As in § 3, we determine $\psi$ by a process of iteration in which the function $u_0$ that we just introduced in (11), § 5 will serve as the initial function. We then calculate $u_1, u_2, \ldots$ in succession from the approximation equations:

$$\Delta u_n + k^2 u_n = V u_{n-1} = F_{n-1} \tag{2}$$

Green's theorem yields the solution that corresponds to the outgoing waves with the time factor $e^{ik\nu t}$ in the form of:

$$u_n(\tau) = -\frac{1}{4\pi} \int F_{n-1}(\tau') \frac{e^{-ik[\tau-\tau']}}{\tau - \tau'} dS', \tag{3}$$

in which $\tau'$ means the vector with the components $x', y', z'$, and $dS' = dx' dy' dz'$. The convergence of the process can be proved on the basis of the assumption that $V$ goes to zero like $r^{-2}$ ($^1$); however, we shall not go into that, but assume that the series:

$$\psi(\tau) = \sum_{n=0}^{\infty} u_n(\tau)$$

represents the solution.

We investigate the asymptotic behavior of $u_n(\tau)$. We write, more thoroughly:

$$u_n(x, y, z) = -\frac{1}{4\pi} \int F_{n-1}(x', y', z') \frac{e^{-ik\sqrt{(x-x')^2 + (y-y')^2 + (z-z')^2}}}{\sqrt{(x-x')^2 + (y-y')^2 + (z-z')^2}} dx' dy' dz'.$$

We now once more introduce the rotation of the coordinate system that was given in § 5 and subject the integration variables to that rotation. One will then have:

$$u_n(x, y, z) = u_n(a_{13}Z, a_{23}Z, a_{33}Z)$$

$$= -\frac{1}{4\pi} \int F'_{n-1}(X', Y', Z') \frac{e^{-ik\sqrt{X'^2 + Y'^2 + Z'^2}}}{\sqrt{X'^2 + Y'^2 + (Z-Z')^2}} dX' dY' dZ'; \tag{4}$$

in this, one has:

$$F'_{n-1}(X', Y', Z') = F_{n-1}(a_{11}X' + a_{11}Y' + a_{13}Z', \ldots). \tag{5}$$

We now introduce polar coordinates:

$$X' = \rho \sin \vartheta \cos \varphi, \quad Y' = \rho \sin \vartheta \sin \varphi, \quad Z' = \rho \cos \vartheta.$$

One will then have:

($^1$) The case of ions is excluded from this; for them, one would have to take a hyperbolic path of the electron as the starting estimate in the approximation process, instead of a rectilinear motion. On this, see a treatise of J. R. Oppenheimer that will appear soon in Proc. Cambridge Phil. Soc., 26 July 1926.
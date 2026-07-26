Born – Quantum mechanics of collision processes.

13

$$\mathfrak{S}_x = \sin \vartheta \cos \varphi, \quad \mathfrak{S}_y = \sin \vartheta \sin \varphi, \quad \mathfrak{S}_z = \cos \vartheta \tag{16}$$

and set $\cos \vartheta = \mu$; we will then have:

$$u_0 = \int_0^{2\pi} d\varphi \int_{-1}^{+1} d\mu c \left[ \sqrt{1-\mu^2} (a_{11} \cos \varphi + a_{12} \sin \varphi) + \mu a_{13}, \cdots \right] e^{ikZ\mu}.$$

It follows from this by partial integration that:

$$\begin{aligned} u_0 &= \frac{1}{ikZ} \int_0^{2\pi} d\varphi \left[ c(a_{13}, a_{23}, a_{33}) e^{ikZ} - c(-a_{13}, -a_{23}, -a_{33}) e^{-ikZ} \right] \\ &- \frac{1}{ikZ} \int_0^{2\pi} d\varphi \frac{d}{d\mu} c \left[ \sqrt{1-\mu^2} (a_{11} \cos \varphi + a_{12} \sin \varphi) + \mu a_{13}, \cdots \right] e^{ikZ\mu} d\mu. \end{aligned}$$

Repeated application of the same process shows that the second term vanishes like $Z^{-2}$. If one now introduces $Z = r$, $a_{13} = \frac{x}{Z} = \frac{x}{r}$, ... then one will get the asymptotic representation:

$$u_0^\infty(x, y, z) = \frac{2\pi}{ikr} \left\{ c\left(\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right) e^{ikr} - c\left(-\frac{x}{r}, -\frac{y}{r}, -\frac{z}{r}\right) e^{-ikr} \right\}, \tag{17}$$

or, in real notation, with $c = |c| e^{ik\gamma}$:

$$u_0^\infty(x, y, z) = \frac{4\pi}{k} \left| c\left(\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right) \right| \frac{\sin k \left[ r + \gamma \left(\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right) \right]}{r}. \tag{18}$$

That means that $u_0$ behaves asymptotically like a spherical wave with an amplitude and phase that depends upon the direction. The intensity, as a function of the direction $\mathfrak{s} = \mathfrak{r} / r$, determines the flux of the particles that flow through the solid angle element $d\omega$ with the axis $\mathfrak{s}$:

$$\Phi_0 d\omega = |c(\mathfrak{s})|^2 d\omega \tag{19}$$

§ 6. Elastic collisions. We now go on to the integration of the general equation (5), § 5:

$$\Delta\psi + (k^2 - V) \psi = 0; \tag{1}$$

physically, it represents the case in which an electron collides with an atom that cannot be excited by that.
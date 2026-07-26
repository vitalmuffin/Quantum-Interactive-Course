QUANTUM MECHANICS

77

$$\mu_\phi(E) = \int_E u_\phi(p) \, dp$$

for every measurable subset $E$ of $S^2$.

(b) The probability density $u_\phi(p)$ is a function only of the angle $\theta$ subtended at 0 by the points $p$ and $P_\phi$ on $S^2$. We may thus write $u_\phi(\theta)$ for the function $u_\phi(p)$.

(c) Let $u(\theta) (= u_{\phi_*}(\theta))$ be the probability density assigned to the state vector

$$\psi_0 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.$$

(Note that $\sigma_{\psi_*} = \sigma_\infty$, so that $P_{\psi_*} = (0, 0, 1)$.) Let $\psi \in U^2$. If $\alpha$ is the polar angle of the point $P_\phi$ on $S^2$, then we assume that $u_\phi(\theta) = u(\theta + \alpha)$. Thus, the probability takes the same functional form for all states $\psi$.

(d) We assume that $u(\theta) = 0$ for $\theta > \pi/2$.

An examination of the problem shows that these are natural properties to assign to the quantum states considered as probability distributions over the hidden states. We shall show that there do exist measures $\mu_\phi$ satisfying the above conditions as well as condition (II). In fact, we shall see that these conditions determine the density functions $u_\phi$ uniquely.

Using these assumptions we may simplify the problem of finding measures $\mu_\phi$ which satisfy condition (II) as follows. Since $f_A$ is a linear function of $A$, the integral $\int_\Omega f_A(\omega) \, d\mu_\phi(\omega)$ is a linear function of $A$. On the other hand the expectation function $\langle A\psi, \psi \rangle$ is also a linear function of $A$. Since every matrix $A$ in $H_2$ is a linear function of a projection matrix, it is sufficient to verify condition (II) for projection matrices. Next, by condition (c) we may assume that

$$\psi = \begin{pmatrix} 1 \\ 0 \end{pmatrix},$$

so that $P_\phi = (0, 0, 1)$. Furthermore, by condition (b), it is sufficient to consider the case where $P_{\sigma(A)}$ has azimuthal angle equal to zero. In what follows we shall make the above assumptions on $A$ and $\psi$.

It is now necessary to express the expectation $\langle A\psi, \psi \rangle$ as a function of the angle subtended at 0 by the points $P_\phi = (0, 0, 1)$ and $P_{\sigma(A)}$, i.e., as a function of the polar angle $\rho$ of $P_{\sigma(A)}$.

In spherical polar coordinates we may write

$$P_{\sigma(A)} = (\sin \rho, 0, \cos \rho).$$

Hence,

$$\begin{aligned} \sigma(A) &= \sigma_\infty \sin \rho + \sigma_\infty \cos \rho \\ &= \begin{pmatrix} \cos \rho & \sin \rho \\ \sin \rho & -\cos \rho \end{pmatrix}. \end{aligned}$$

The eigenvector $\eta$ of $\sigma(A)$ belonging to the eigenvalue $+1$ is

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms
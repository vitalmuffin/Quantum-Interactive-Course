coordinate $g(t)$, Lagrangian $\frac{1}{2}(\dot{q}^2 - \omega^2 q^2)$ through a term $\gamma(x,t)q(t)$ in the Lagrangian for the system. Here $\gamma(x,t)$ is any function of the coordinate $x(t)$ of the particle and the time. $^{24}$ Suppose we desire the probability of a transition from a state at time $t'$, in which the particle's wave function is $\psi_{t'}$ and the oscillator is in energy level $n$, to a state at $t''$ with the particle in $\chi_{t''}$ and oscillator in level $m$. This is the square of

$$\langle \chi_{t''} \varphi_m | 1 | \psi_{t'} \varphi_n \rangle_{S_p + S_0 + S_I} = \int \dots \int \varphi_m^*(q_i) \chi_{t''}^*(x_i)$$

$$\times \exp \frac{i}{\hbar} (S_p + S_0 + S_1) \psi_{t'}(x_0) \varphi_n(q_0) \cdot \frac{dx_0}{A} \frac{dq_0}{a} \dots \frac{dx_{j-1}}{A} \frac{dq_{j-1}}{a} dx_i dq_i. \tag{61}$$

Here $\varphi_n(9q)$ is the wave function for the oscillator in state $n$, $S_p$ is the action

$$\sum_{i=0}^{j-1} S_p(x_{i+1}, x_i)$$

calculated for the particle as though the oscillator were absent,

$$S_0 = \sum_{i=0}^{j-1} \left[ \frac{\epsilon}{2} \left( \frac{q_{i+1} - q_i}{\epsilon} \right)^2 - \frac{\epsilon \omega^2}{2} q_{i+1}^2 \right]$$

that of the oscillator alone, and

$$S_I = \sum_{i=0}^{j-1} \gamma_i q_i$$

(where $\gamma_i = \gamma(x_i, t_i)$) is the action of interaction between the particle and the oscillator. The normalizing constant, $a$, for the oscillator is $(2\pi\epsilon i / \hbar)^{-1/2}$. Now the exponential depends quadratically upon all the $q_i$. Hence, the integrations over all the variables $q_i$, for $0 < i < j$ can easily be performed. One is integrating a sequence of Gaussian integrals.

The result of these integrations is, writing $T = t'' - t'$, $(2\pi i \hbar \sin \omega T / \omega)^{-1/2} \exp i (S_p + Q(q_i, q_0)) / \hbar$, where $Q(q_j, q_0)$ go) turns out to be just the classical

$^{24}$The generalization to the case that $\gamma$ depends on the velocity, $\dot{x}$, of the particle presents no problem.

34
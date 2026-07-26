wave function $\psi(x,t)$ is sufficient to define those attributes which are left from past history which determine future behavior.

Likewise, the function $\chi(x,t)$ characterizes the experience, or, let us say, experiment to which the system is to be subjected. If a different region, $r''$ and different Lagrangian after $t$, were to give the same $\chi^*(x,t)$ *via* Eq. (16), as does region $R''$, then no matter what the preparation, $\psi$, Eq. (14) says that the chance of finding the system in $R''$ is always the same as finding it in $r''$. The two “experiments” $R''$ and $r''$ are equivalent, as they yield the same results. We shall say loosely that these experiments are to determine with what probability the system is in state $\chi$. Actually, this terminology is poor. The system is really in state $\psi$. The reason we can associate a state with an experiment is, of course, that for an ideal experiment there turns out to be a unique state (whose wave function is $\chi(x,t)$), for which the experiment succeeds with certainty.

Thus, we can say: the probability that a system in state $\psi$ will be found by an experiment whose characteristic state is $\chi$ (or, more loosely, the chance that a system in state $\psi$ will appear to be in $\chi$) is

$$\left| \int \chi^*(x,t)\psi(x,t)dx \right|^2. \quad (17)$$

These results agree, of course, with the principles of ordinary quantum mechanics. They are a consequence of the fact that the Lagrangian is a function of position, velocity, and time only.

## 6. The Wave Equation

To complete the proof of the equivalence with the ordinary formulation we shall have to show that the wave function defined in the previous section by Eq. (15) actually satisfies the Schroedinger wave equation. Actually, we shall only succeed in doing this when the Lagrangian $L$ in (11) is a quadratic, but perhaps inhomogeneous, form in the velocities $\dot{x}(t)$. This is not a limitation, however, as it includes all the cases for which the Schroedinger equation has been verified by experiment.

The wave equation describes the development of the wave function with time. We may expect to approach it by noting that, for finite $\epsilon$, Eq. (15) permits a simple recursive relation to be developed. Consider the appearance of Eq. (15) if we were to compute $\psi$ at the next instant of time:

$$\psi(x_{k+1}, t+\epsilon) = \int_{R'} \exp\left[ \frac{i}{\hbar} \sum_{i=-\infty}^k S(x_{i+1}, x_i) \right] \times \frac{dx_k}{A} \frac{dx_{k-1}}{A} \dots \quad (15')$$

13
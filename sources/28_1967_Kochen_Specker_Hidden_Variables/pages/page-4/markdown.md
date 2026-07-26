QUANTUM MECHANICS

61

1. Discussion of the problem. For our purposes it is convenient to describe a physical theory within the following framework. We are given a set $\mathcal{O}$ called the set of observables and a set $S$ called the set of states. In addition, we have a function $P$ which assigns to each observable $A$ and each state $\psi$ a probability measure $P_{A\psi}$ on the real line $\mathbf{R}$. Physically speaking, if $U$ is a subset of $\mathbf{R}$ which is measurable with respect to $P_{A\psi}$, then $P_{A\psi}(U)$ denotes the probability that the measurement of $A$ for a system in the state $\psi$ yields a value lying in $U$. From this we obtain in the usual manner the expectation of the observable $A$ for the state $\psi$,

$$\text{Exp}_\psi(A) = \int_{-\infty}^{\infty} \lambda \, dP_{A\psi}(\lambda).$$

States are generally divided into two kinds, pure states and mixed states. Roughly speaking, the pure states describe a maximal possible amount of knowledge available in the theory about the physical system in question; the mixed states give only incomplete information and describe our ignorance of the exact pure state the system is actually in.

We illustrate these remarks with an example from Newtonian mechanics. Suppose we are given a system of $N$ particles. Then each pure state $\psi$ of the system is given by a $6N$-tuple $(q_1, \dots, q_{2N}, p_1, \dots, p_{2N})$ of real numbers denoting the coordinates of position and momentum of the particles. In this case, the probability $P_{A\psi}$ assigned to each observable is an atomic measure, concentrated on a single real number $a$. That is, $P_{A\psi}(U) = 1$ if $a \in U$ and $P_{A\psi}(U) = 0$ if $a \notin U$. Thus, if we introduce the phase space $\Omega$ of pure states, which we may here identify with a subset of $6N$-dimensional Euclidean space, then each observable $A$ becomes associated with a real-valued function $f_A : \Omega \to \mathbf{R}$ given by $f_A(\psi) = a$.

If $N$ is large it is not feasible to determine the precise pure state the system may be in. We resort in this case to the notion of a mixed state which gives only the probability that the system is in a pure state which lies in a region of $\Omega$. More precisely, a mixed state $\psi$ is described by a probability measure $\mu_\psi$ on the space $\Omega$, so that, for each measurable subset $\Gamma$ of $\Omega$, $\mu_\psi(\Gamma)$ is the probability that the system is in a pure state lying in $\Gamma$. It follows immediately that the probability measure $P_{A\psi}$ assigned to an observable $A$ and mixed state $\psi$ is given by the formula

$$(1) \quad P_{A\psi}(U) = \mu_\psi(f_A^{-1}(U)).$$

Thus, we have

$$(2) \quad \text{Exp}_\psi(A) = \int_\Omega f_A(\omega) \, d\mu_\psi(\omega).$$

In the case of quantum mechanics the set $\mathcal{O}$ of observables is represented by self-adjoint operators on a separable Hilbert space $\mathcal{H}$. The pure states are given by the one-dimensional linear subspaces of $\mathcal{H}$. The probability $P_{A\psi}$ is defined

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms
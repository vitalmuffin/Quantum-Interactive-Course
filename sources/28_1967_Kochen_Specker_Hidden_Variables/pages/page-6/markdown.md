QUANTUM MECHANICS

63

for the existence of hidden variables. For we may always introduce, at least mathematically, a phase space $\Omega$ into a theory so that (1) is satisfied. To see this, let

$$\Omega = \mathbf{R}^0 = \{\omega \mid \omega : \mathcal{O} \to \mathbf{R}\}.$$

If $A \in \mathcal{O}$, let $f_A : \Omega \to \mathbf{R}$ be defined by $f_A(\omega) = \omega(A)$. If $\psi \in S$, let

$$\mu_\psi = \prod_{A \in \mathcal{O}} P_{A\psi},$$

the product measure of the probabilities $P_{A\psi}$. Then,

$$\mu_\psi f_A^{-1}(U) = \mu_\psi(\{\omega \mid \omega(A) \in U\}) = P_{A\psi}(U).$$

We have two reasons for mentioning this somewhat trivial construction. First, in the various attempts to introduce hidden variables into quantum mechanics, the only explicitly stated requirement that is to be fulfilled is the condition (1). (See Bohm [1] and [2], Bopp [3], Siegel and Wiener [16], and especially the review of [16] in Schwartz [15].) Of course, the above space $\Omega$ is far more artificial than the spaces proposed in these papers, but the only purpose here was to point out the insufficiency of the condition (1) as a test for the adequacy of the solution of the problem.

Our second reason for introducing the space $\mathbf{R}^0$ is that it indicates the direction in which the condition (1) is inadequate. For each state $\psi$, as interpreted in the space $\mathbf{R}^0$, the functions $f_A$ are easily seen to be measurable functions with respect to the probability measure $\mu_\psi$. In the language of probability theory the observables are thus interpreted as random variables for each state $\psi$. It is not hard to show furthermore that in this representation the observables appear as independent random variables.

Now it is clear that the observables of a theory are in fact not independent. The observable $A^2$ is a function of the observable $A$ and is certainly not independent of $A$. In any theory, one way of measuring $A^2$ consists in measuring $A$ and squaring the resulting value. In fact, this may be used as the *definition* of a function of an observable. Namely, we define the observable $g(A)$ for every observable $A$ and Borel function $g : \mathbf{R} \to \mathbf{R}$ by the formula

$$(3) \quad P_{g(A)\psi}(U) = P_{A\psi}(g^{-1}(U))$$

for each state $\psi$. If we assume that every observable is determined by the function $P$, i.e., $P_{A\psi} = P_{B\psi}$ for every state $\psi$ implies that $A = B$, then the formula (3) defines the observable $g(A)$. This definition coincides with the definition of a function of an observable in both quantum and classical mechanics.

Thus the measurement of a function $g(A)$ of an observable $A$ is independent of the theory considered—one merely writes $g(a)$ for the value of $g(A)$ if $a$ is the measured value of $A$. The set of observables of a theory thereby acquires an algebraic structure, and the introduction of hidden variables into a theory should preserve this structure. In more detail, we require for the successful

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms
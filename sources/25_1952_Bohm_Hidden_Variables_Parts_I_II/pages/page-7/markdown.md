172

DAVID BOHM

usual interpretation of the quantum theory would tend to lead us away from the direction of our suggested alternative interpretation. For in a theory involving hidden variables, one would normally expect that the behavior of an individual system should not depend on the statistical ensemble of which it is a member, because this ensemble refers to a series of similar but disconnected experiments carried out under equivalent initial conditions. In our interpretation, however, the "quantum-mechanical" potential, $U(\mathbf{x})$, acting on an individual particle depends on a wave intensity, $P(\mathbf{x})$, that is also numerically equal to a probability density in our ensemble. In the terminology of the usual interpretation of the quantum theory, in which one tacitly assumes that the wave function has only one interpretation; namely, in terms of a probability, our suggested new interpretation would look like a mysterious dependence of the individual on the statistical ensemble of which it is a member. In our interpretation, such a dependence is perfectly rational, because the wave function can consistently be interpreted both as a force and as a probability density.¹²

It is instructive to carry our analogy between the Schroedinger field and other kinds of fields a bit further. To do this, we can derive the wave Eqs. (5) and (6) from a Hamiltonian functional. We begin by writing down the expression for the mean energy as it is expressed in the usual quantum theory:

$$\begin{array}{l} \bar {H} = \int \psi^ {*} \left(- \frac {\hbar^ {2}}{2 m} \nabla^ {2} + V (\mathbf {x})\right) \psi d \mathbf {x} \\ = \int \left\{\frac {\hbar^ {2}}{2 m} | \nabla \psi | ^ {2} + V (\mathbf {x}) | \psi | ^ {2} \right\} d \mathbf {x}. \end{array}$$

Writing $\psi = P^{\frac{1}{2}}\exp (iS / \hbar)$, we obtain

$$\bar {H} = \int P (\mathbf {x}) \left\{\frac {(\nabla S) ^ {2}}{2 m} + V (\mathbf {x}) + \frac {\hbar^ {2}}{8 m} \frac {(\nabla P) ^ {2}}{P ^ {2}} \right\} d \mathbf {x}. \tag {9}$$

We shall now reinterpret $P(\mathbf{x})$ as a field coordinate, defined at each point, $\mathbf{x}$, and we shall tentatively assume that $S(\mathbf{x})$ is the momentum, canonically conjugate to $P(\mathbf{x})$. That such an assumption is appropriate can be verified by finding the Hamiltonian equations of motion for $P(\mathbf{x})$ and $S(\mathbf{x})$, under the assumption that the Hamiltonian functional is equal to $\bar{H}$ (See Eq. (9)). These equations of motion are

$$\begin{array}{l} \dot {P} = \frac {\delta \bar {H}}{\delta S} = - \frac {1}{m} \nabla \cdot (P \nabla S), \\ \dot {S} = \frac {\delta \bar {H}}{\delta P} = - \left[ \frac {(\nabla S) ^ {2}}{2 m} + V (\mathbf {x}) - \frac {\hbar^ {2}}{4 m} \left(\frac {\nabla^ {2} P}{P} - \frac {1}{2} \frac {(\nabla P) ^ {2}}{P ^ {2}}\right) \right]. \end{array}$$

¹² This consistency is guaranteed by the conservation Eq. (7). The questions of why an arbitrary statistical ensemble tends to decay into an ensemble with a probability density equal to $\psi^{*}\psi$ will be discussed in Paper II, Sec. 7.

These are, however, the same as the correct wave Eqs. (5) and (6).

We can now show that the mean particle energy averaged over our ensemble is equal to the usual quantum mechanical mean value of the Hamiltonian, $\bar{H}$. To do this, we note that according to Eqs. (3) and (6), the energy of a particle is

$$E (\mathbf {x}) = - \frac {\partial S (\mathbf {x})}{\partial t} = \left[ \frac {(\nabla S) ^ {2}}{2 m} + V (\mathbf {x}) - \frac {\hbar^ {2}}{2 m} \frac {\nabla^ {2} R}{R} \right]. \tag {10}$$

The mean particle energy is found by averaging $E(\mathbf{x})$ with the weighting function, $P(\mathbf{x})$. We obtain

$$\begin{array}{l} \langle E \rangle_ {\text { ensemble average }} = \int P (\mathbf {x}) E (\mathbf {x}) d \mathbf {x} \\ = \int P (\mathbf {x}) \left[ \frac {(\nabla S) ^ {2}}{2 m} + V (\mathbf {x}) \right] d \mathbf {x} - \frac {\hbar^ {2}}{2 m} \int R \nabla^ {2} R d \mathbf {x}. \end{array}$$

A little integration by parts yields

$$\begin{array}{l} \langle E \rangle_ {\text { ensemble average }} = \int P (\mathbf {x}) \left[ \frac {(\nabla S) ^ {2}}{2 m} + V (\mathbf {x}) \right. \\ \left. + \frac {\hbar^ {2}}{8 m} \frac {(\nabla P) ^ {2}}{P ^ {2}} \right] d \mathbf {x} = \bar {H}. \tag {11} \end{array}$$

# 5. THE STATIONARY STATE

We shall now show how the problem of stationary states is to be treated in our interpretation of the quantum theory.

The following seem to be reasonable requirements in our interpretation for a stationary state:

(1) The particle energy should be a constant of the motion.
(2) The quantum-mechanical potential should be independent of time.
(3) The probability density in our statistical ensemble should be independent of time.

It is easily verified that these requirements can be satisfied with the assumption that

$$\begin{array}{l} \psi (\mathbf {x}, t) = \psi_ {0} (\mathbf {x}) \exp (- i E t / \hbar) \\ = R _ {0} (\mathbf {x}) \exp [ i (\Phi (\mathbf {x}) - E t) / \hbar ]. \tag {12} \end{array}$$

From the above, we obtain $S = \Phi(\mathbf{x}) - Et$. According to the generalized Hamilton-Jacobi Eq. (4), the particle energy is given by

$$\partial S / \partial t = - E.$$

Thus, we verify that the particle energy is a constant of the motion. Moreover, since $P = R^2 = |\psi|^2$, it follows that $P$ (and $R$) are independent of time. This means that both the probability density in our ensemble and the quantum-mechanical potential are also time independent.
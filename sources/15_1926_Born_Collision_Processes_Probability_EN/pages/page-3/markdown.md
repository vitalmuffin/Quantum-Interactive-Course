Born – Quantum mechanics of collision processes.

3

$$\psi(q) = \sum_{n} c_{n} \psi_{n}(q). \tag{3}$$

Up to now, all of the attention has been focused upon the eigenvibrations $\psi_{n}$ and the eigenvalues $W_{n}$. The picture that we suggested in the introduction is closely related to the idea of connecting the superposition of functions that is represented in (3) with the probability that the state will appear with a certain frequency in a cloud of identical, uncoupled atoms.

The completeness relation:

$$\int |\psi(q)|^{2} \, dq = \sum_{n} |c_{n}|^{2} \tag{4}$$

leads to the idea that this integral can be regarded as the number of atoms. It then has the value 1 for the appearance of a single, normalized eigenvibration (or: the *a priori* weight of the state is 1), $|c_{n}|^{2}$ means the frequency of the state $n$, and the total numbers can be combined additively from these components.

In order to justify this interpretation, we shall consider, say, the motion of a massive point in three-dimensional space under the action of the potential energy $U(x, y, z)$; the differential equation (1) will then read:

$$\Delta\psi + \frac{8\pi^{2}\mu}{h^{2}}(W - U)\psi = 0. \tag{5}$$

If one sets $W$, $\psi$ in this equal to an eigenvalue $W_{n}$ and an eigenfunction $\psi_{n}$, resp., multiplies the equation by $\psi_{n}^{*}$, and integrates over all space ($dS = dx\,dy\,dz$) then one will obtain:

$$\iiint \left\{ \psi_{m}^{*} \Delta\psi_{n} + \frac{8\pi^{2}\mu}{h^{2}}(W_{n} - U)\psi_{n}\psi_{m}^{*} \right\} dS = 0.$$

From *Green's* theorem, and recalling the orthogonality conditions (2), that will give:

$$\delta_{mn} W_{n} = \iiint \left\{ \frac{h^{2}}{8\pi^{2}\mu}(\text{grad }\psi_{n} \cdot \text{grad }\psi_{m}^{*}) + U\psi_{n}\psi_{m}^{*} \right\} dS. \tag{6}$$

Each energy level can then be regarded as the spatial integral of the energy density of the eigenvibrations.

If one now defines the corresponding integral for any function:

$$W = \iiint \left\{ \frac{h^{2}}{8\pi^{2}\mu}|\text{grad }\psi_{n}|^{2} + U|\psi_{n}|^{2} \right\} dS \tag{7}$$

then if one substitutes the development (3), one will get the expression for this:
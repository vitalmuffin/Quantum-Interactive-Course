Born – Quantum mechanics of collision processes.

19

$$[H^a, \psi_{nk}^{(1)}] - \frac{h^2}{8\pi^2\mu} \Delta\psi_{nk}^{(1)} - W_{nk}^0 \psi_{nk}^{(1)} = -U \psi_{nk}^0.$$

We seek to solve this equation by the Ansatz:

$$\psi_{nk}^{(1)} = \sum_m u_{nk}^{(1)}(\tau) \psi_m^a;$$

i.e., in terms of a development in only the eigenfunctions of the unperturbed atom whose coefficients are undetermined functions of the position vector $\tau$ of the electron.

From (1), one will now have:

$$\begin{aligned} [H^a, \psi_{nk}^{(1)}] &= \sum_m u_{nm}^{(1)}(\tau) [H^a, \psi_m^a] \\ &= \sum_m u_{nm}^{(1)}(\tau) W_m^a \psi_m^a. \end{aligned}$$

We develop the given function on the right-hand side in the same way:

$$U \psi_{nk}^0 = \psi_k^e \cdot U \psi_n^a = \psi_k^e \sum_m U_{nm} \psi_m^a;$$

the coefficients define the matrix that is associated with the potential energy. If we introduce these expressions into the differential equation then we will get:

$$\sum_m \psi_m^a \left\{ u_{nm}^{(1)}(\tau) W_m^a - \frac{h^2}{8\pi^2\mu} \Delta u_{nm}^{(1)} - u_{nm}^{(1)} (W_m^a + W^e) \right\} = - \sum_m \psi_m^a U_{nm} \psi_k^e.$$

One obtains a differential equation for $u_{nm}^{(1)}(\tau)$ from this by equating the coefficients of $\psi_m^a$; if we multiply it by $-\frac{8\pi^2\mu}{h^2}$ and set, to abbreviate:

$$V = \frac{8\pi^2\mu}{h^2} U, \quad V_{nm} = \frac{8\pi^2\mu}{h^2} U_{nm}, \tag{6}$$

$$k_{nm}^2 = \frac{8\pi^2\mu}{h^2} (W_n^a - W_m^a + W^e) = \frac{8\pi^2\mu}{h^2} (h\nu_{nm}^a + W^e) \tag{7}$$

then we will find that:

$$\Delta u_{nm}^{(1)} + k_{nm}^2 u_{nm}^{(1)} = V_{nm} \psi_k^e. \tag{8}$$

We have then converted the problem into the previously-treated problem of inelastic collision; all of the following approximations then lead to the same wave equation.
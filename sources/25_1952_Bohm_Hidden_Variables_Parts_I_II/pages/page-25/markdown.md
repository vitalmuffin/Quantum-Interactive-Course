190

DAVID BOHM

tion of the ability of an oscillator, $q_{k,\mu}$, to transfer large quantities of energy and momentum rapidly even when $q_{k,\mu}$ is very small, for when $q_{k,\mu}$ is small, the right-hand side of Eq. (A8) may become very large.

The second interpretation of $R$ is that as in Paper I, Eq. (5), it defines a conserved probability density that each of the $q_{k,\mu}$ has a certain specified value. From this fact, we see that although large transfers of energy and momentum to a radiation oscillator can occur in a short time when $R$ is small, the probability of such a process is (as was also shown in Paper I, Sec. 7) very small.

In the lowest state (when no quanta are present) every oscillator is in the ground state. The super wave fields is then

$$\Psi_0^{(R)} = \exp[-\sum_{k,\mu} (k c q_{k,\mu} q_{k,\mu}^* + \frac{1}{2} i k c t)]. \tag{A9}$$

If the $\mathbf{k}'$, $\mu'$ oscillator is excited to the $n$th quantum state, the super wave field is

$$\Psi^{(R)} = h_n(q_{k',\mu'}) e^{-i n k' c t} \Psi_0^{(R)}, \tag{A10}$$

where $h_n$ is the $n$th hermite polynomial. As shown in Paper I, Sec. 5, the stationary states of such a system correspond to a quantized energy equal to the same value, $E_n = (n + \frac{1}{2})\hbar kc$, obtained from the usual interpretation. In nonstationary states, however, Eqs. (A7) and (A8) imply that the energy of each oscillator may fluctuate violently, as was also true of nonstationary states of the hydrogen atom (see Paper I, Sec. 7).

A nonstationary state of particular interest in the photoelectric and Compton effects is a state corresponding to the presence of an electromagnetic wave packet containing a single quantum. The super wave field for such a state is

$$\Psi_P^{(R)} = \sum_{k,\mu} f_\mu(\mathbf{k} - \mathbf{k}_0) q_{k,\mu} e^{-i k c t} \Psi_0^{(R)}, \tag{A11}$$

where $f_\mu(\mathbf{k} - \mathbf{k}_0)$ is a function that is large only near $\mathbf{k} = \mathbf{k}_0$ and the first hermite polynomial is represented by $q_{k,\mu}$, to which it is proportional.

To prove that Eq. (A11) represents an electromagnetic wave packet, we can evaluate the difference

$$\langle \Delta W \rangle_{\mu} = \langle W \rangle_{\mu} - \langle W_0 \rangle_{\mu}, \tag{A12}$$

where $\langle W(\mathbf{x}) \rangle_{\mu}$ is the actual mean energy density present (averaged over the ensemble), and $\langle W_0(\mathbf{x}) \rangle_{\mu}$ is the mean energy that would be present even in the ground state, because of zero-point fluctuations. We have

$$\langle W(\mathbf{x}) \rangle_{\mu} = \iint \cdots \int \Psi_P^{*(R)}(\cdots q_{k,\mu} \cdots) \times \frac{[\mathfrak{G}^2(\mathbf{x}) + \mathfrak{H}^2(\mathbf{x})]}{8\pi} \Psi_P^{(R)}(\cdots q_{k,\mu} \cdots) \times (\cdots d q_{k,\mu} \cdots), \tag{A13}$$

$$\langle W_0(\mathbf{x}) \rangle_{\mu} = \iint \cdots \int \Psi_0^{*(R)}(\cdots q_{k,\mu} \cdots) \times \frac{[\mathfrak{G}^2(\mathbf{x}) + \mathfrak{H}^2(\mathbf{x})]}{8\pi} \Psi_0^{(R)}(\cdots q_{k,\mu} \cdots) \times (\cdots d q_{k,\mu} \cdots). \tag{A14}$$

Obtaining $\mathfrak{G}(\mathbf{x})$ from Eq. (A2), $\mathfrak{H}(\mathbf{x})$ from Eq. (A3), $\Psi_P^{(R)}$ from Eq. (A10), $\Psi_0^{(R)}$ from Eq. (A9), we readily show that

$$\langle \Delta W(\mathbf{x}) \rangle_{\mu} = \sum_{k,\mu} \sum_{k',\mu'} f_\mu(\mathbf{k} - \mathbf{k}_0) f_{\mu'}(\mathbf{k}' - \mathbf{k}_0) \times e^{i(\mathbf{k} + \mathbf{k}') \cdot \mathbf{r}} \epsilon_{k,\mu} \cdot \epsilon_{k',\mu'}. \tag{A15}$$

This means that the wave packet implies an excess over zero-point energy that is localized within a region in which the packet function, $\mathbf{g}(\mathbf{x})$ is appreciable, where

$$\mathbf{g}(\mathbf{x}) = \sum_{k,\mu} f_\mu(\mathbf{k} - \mathbf{k}_0) e^{i \mathbf{k} \cdot \mathbf{r}} \epsilon_{k,\mu}. \tag{A16}$$

We are now ready to treat the photoelectric and Compton effects. The entire treatment is so similar to that of the Franck-Hertz experiment (Paper I, Sec. 7) that we need merely sketch it here. We begin by adding to the radiation Hamiltonian, $H^{(R)}$, the particle Hamiltonian,

$$H^{(P)} = (1/2m)[\mathbf{p} - (e/c)\mathbf{A}(\mathbf{x})]^2. \tag{A17}$$

(We restrict ourselves here to nonrelativistic treatment.) The photoelectric effect corresponds to the transition of a radiation oscillator from an excited state to the ground state, while the atomic electron is ejected, with an energy $E = h\nu - I$, where $I$ is the ionization potential of the atom. The initial super wave field, corresponding to an incident packet containing only one quantum, plus an atom in the ground state is (see Eq. (A11))

$$\Psi_i = \psi_0(\mathbf{x}) \exp(-i E_0 t / \hbar) \Psi_0^{(R)}(\cdots q_{k,\mu} \cdots) \times \sum_{k,\mu} f_\mu(\mathbf{k} - \mathbf{k}_0) q_{k,\mu} e^{-i k c t}. \tag{A18}$$

By solving Schroedinger's equation for the combined system, we obtain an asymptotic wave field analogous to Paper I, Eq. (26), containing terms corresponding to the photoelectric effect. These terms, which must be added to $\Psi_i$, to yield the complete superfield, are (asymptotically)

$$\delta \Psi_\mu = \Psi_0^{(R)}(\cdots q_{k,\mu} \cdots) \sum_{k,\mu} f_\mu(\mathbf{k} - \mathbf{k}_0) \times \frac{\exp[i \mathbf{k}' \cdot \mathbf{r} - i \hbar (k'^2 / 2m) t]}{r} g_\mu(\theta, \phi, k'), \tag{A19}$$

where the energy of the outgoing electron is $E = \hbar^2 k'^2 / 2m = \hbar kc + E_0$. The function $g_\mu(\theta, \phi, k')$ is the amplitude associated with the $\psi$-field of the outgoing electron. This quantity can be calculated from the matrix ele-
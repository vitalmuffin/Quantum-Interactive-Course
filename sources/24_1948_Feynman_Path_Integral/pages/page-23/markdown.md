where we have used the abbreviation (36).

In the language of ordinary quantum mechanics if the Hamiltonian, H, is constant, $\psi(x, t'') = \exp[-i(t'' - t')\mathbf{H}/\hbar]\psi(x, t')$ so that (38) is the matrix element of $\exp[-i(t'' - t')\mathbf{H}/\hbar]$ between states $\chi_{t''}$ and $\psi_{t'}$.

If $F$ is any function of the coordinates $x_i$ for $t' < t_i < t''$, we shall define the transition element of $F$ between the states $\psi$ at $t'$ and $\chi$ at $t''$ for the action $S$ as $(x'' \equiv x_j, x' \equiv x_0)$:

$$\langle \chi_{t''} | F | \psi_{t'} \rangle = \lim_{\epsilon \to 0} \int \dots \int \times \chi^*(x'', t'') F(x_0, x_1, \dots x_i) \cdot$$

$$\cdot \exp \left[ \frac{i}{\hbar} \sum_{i=0}^{j-1} S(x_{i+1}, x_i) \right] \psi(x', t') \frac{dx_0}{A} \dots \frac{dx_{j-1}}{A} dx_i. \tag{39}$$

In the limit $\epsilon \to 0$, $F$ is a functional of the path $x(t)$.

We shall see presently why such quantities are important. It will be easier to understand if we stop for a moment to find out what the quantities correspond to in conventional notation. Suppose $F$ is simply $x_k$, where $k$ corresponds to some time $t = t_k$. Then on the right-hand side of (39) the integrals from $x_0$ to $x_{k-1}$ may be performed to produce $\psi(x_k, t)$ or $\exp[-i(t - t')\mathbf{H}/\hbar]\psi_{t'}$. In like manner the integrals on $x_i$ for $j \ge i > k$ give $\chi^*(x_k, t)$ or $\{\exp[-i(t'' - t)\mathbf{H}/\hbar]\chi_{t''}\}$. Thus, the transition element of $x_k$,

$$\langle \chi_{t''} | F | \psi_{t'} \rangle_S = \int \chi_{t''}^* e^{(i/\hbar)\mathbf{h}(t'' - t)} x e^{-(i/\hbar)\mathbf{H}(t - t')} \psi_{t'} dx =$$
$$= \int \chi^*(x, t) x \psi(x, t) dx \tag{40}$$

is the matrix element of $\mathbf{x}$ at time $t = t_k$ between the state which would develop at time $t$ from $\psi_{t'}$ at $t'$ and the state which will develop from time $t$ to $\chi_{t''}$ at $t''$. It is, therefore, the matrix element of $\mathbf{x}(t)$ between these states.

Likewise, according to (39) with $F = x_{k+1}$, the transition element of $x_{k+1}$ is the matrix element of $\mathbf{x}(t + \epsilon)$. The transition element of $F = (x_{k+1} - x_k)/\epsilon$ is the matrix element of $(\mathbf{x}(t + \epsilon) - \mathbf{x}(t))/\epsilon$ or of $i(\mathbf{H}\mathbf{x} - \mathbf{x}\mathbf{H})/\hbar$, as is easily shown from (40). We can call this the matrix element of velocity $\dot{x}(t)$.

Suppose we consider a second problem which differs from the first because, for example, the potential is augmented by a small amount $U(\cdot, \mathbf{x}t)$. Then in the new problem the quantity replacing $S$ is $S' = S + \sum_i \epsilon U(x_i, t_i)$. Substitution into (38) leads directly to

$$\langle \chi_{t''} | 1 | \psi_{t'} \rangle_{S'} = \left\langle \chi_{t''} \left| \exp \frac{i\epsilon}{\hbar} \sum_{i=1}^j U(x_i, t_i) \right| \psi_{t'} \right\rangle_S. \tag{41}$$

23
176

DAVID BOHM

ergy with some other system. In order to treat the problem of transition between stationary states, we must therefore introduce another system capable of exchanging energy with the system of interest. In this section, we shall discuss the Franck-Hertz experiment, in which this other system consists of a bombarding particle. For the sake of illustration, let us suppose that we have hydrogen atoms of energy $E_0$ and wave function, $\psi_0(\mathbf{x})$, which are bombarded by particles that can be scattered inelastically, leaving the atom with energy $E_n$ and wave function, $\psi_n(\mathbf{x})$.

We begin by writing down the initial wave function, $\Psi_i(\mathbf{x}, \mathbf{y}, t)$. The incident particle, whose coordinates are represented by $\mathbf{y}$ must be associated with a wave packet, which can be written as

$$f_0(\mathbf{y}, t) = \int e^{i\mathbf{k}\cdot\mathbf{y}} f(\mathbf{k}-\mathbf{k}_0) \exp(-i\hbar k^2 t / 2m) d\mathbf{k}. \tag{21}$$

The center of this packet occurs where the phase has an extremum as a function of $\mathbf{k}$, or where $\mathbf{y} = \hbar\mathbf{k}_0 t / m$.

Now, as in the usual interpretation, we begin by writing the incident wave function for the combined system as a product

$$\Psi_i = \psi_0(\mathbf{x}) \exp(-iE_0 t / \hbar) f_0(\mathbf{y}, t). \tag{22}$$

Let us now see how this wave function is to be understood in our interpretation of the theory. As pointed out in Sec. 6, the wave function is to be regarded as a mathematical representation of a six-dimensional but objectively real field, capable of producing forces that act on the particles. We also assume a six-dimensional representative point, described by the coordinates of the two particles, $\mathbf{x}$ and $\mathbf{y}$. We shall now see that when the combined wave function takes the form (22) involving a product of a function of $\mathbf{x}$ and a function of $\mathbf{y}$, the six-dimensional system can correctly be regarded as being made up of two independent three-dimensional subsystems. To prove this, we write

$$\psi_0(\mathbf{x}) = R_0(\mathbf{x}) \exp[iS_0(\mathbf{x})/\hbar] \quad \text{and}$$

$$f_0(\mathbf{y}, t) = M_0(\mathbf{y}, t) \exp[iN_0(\mathbf{y}, t)/\hbar].$$

We then obtain for the particle velocities

$$d\mathbf{x}/dt = (1/m)\nabla S_0(\mathbf{x}); \quad d\mathbf{y}/dt = (1/m)\nabla N_0(\mathbf{y}, t), \tag{23}$$

and for the "quantum-mechanical" potential

$$U = -\frac{\hbar^2 \{(\nabla_x^2 + \nabla_y^2)R(\mathbf{x}, \mathbf{y})\}}{2mR(\mathbf{x}, \mathbf{y})} = \frac{-\hbar^2}{2m} \left\{ \frac{\nabla^2 R_0(\mathbf{x})}{R_0(\mathbf{x})} + \frac{\nabla^2 M_0(\mathbf{y}, t)}{M_0(\mathbf{y}, t)} \right\}. \tag{24}$$

Thus, the particle velocities are independent and the "quantum-mechanical" potential reduces to a sum of terms, one involving only $\mathbf{x}$ and the other involving only $\mathbf{y}$. This means that the particles move independently.

Moreover, the probability density, $P = R_0^2(\mathbf{x}) \times M_0^2(\mathbf{y}, t)$, is a product of a function of $\mathbf{x}$ and a function of $\mathbf{y}$, indicating that the distribution in $\mathbf{x}$ is statistically independent of that in $\mathbf{y}$. We conclude, then, that whenever the wave function can be expressed as a product of two factors, each involving only the coordinates of a single system, then the two systems are completely independent of each other.

As soon as the wave packet in $\mathbf{y}$ space reaches the neighborhood of the atom, the two systems begin to interact. If we solve Schroedinger's equation for the combined system, we obtain a wave function that can be expressed in terms of the following series:

$$\Psi = \Psi_i + \sum_n \psi_n(\mathbf{x}) \exp(-iE_n t / \hbar) f_n(\mathbf{y}, t), \tag{25}$$

where the $f_n(\mathbf{y}, t)$ are the expansion coefficients of the complete set of functions, $\psi_n(\mathbf{x})$. The asymptotic form of the wave function is$^{14}$

$$\Psi = \Psi_i(\mathbf{x}, \mathbf{y}) + \sum_n \psi_n(\mathbf{x}) \exp\left(-\frac{iE_n t}{\hbar}\right) \int f(\mathbf{k}-\mathbf{k}_0) \times \frac{\exp[ik_n \cdot \mathbf{r} - (\hbar k_n^2 / 2n)t]}{r} g_n(\theta, \phi, \mathbf{k}) d\mathbf{k}, \tag{26}$$

where

$$\hbar^2 k_n^2 / 2m = (\hbar^2 k_0^2 / 2m) + E_0 - E_n \quad (\text{conservation of energy}). \tag{27}$$

The additional terms in the above equation represent outgoing wave packets, in which the particle speed, $\hbar k_n / m$, is correlated with the wave function, $\psi_n(\mathbf{x})$, representing the state in which the hydrogen atom is left. The center of the $n$th packet occurs at

$$r_n = (\hbar k_n / m)t. \tag{28}$$

It is clear that because the speed depends on the hydrogen atom quantum number, $n$, every one of these packets will eventually be separated by distances which are so large that this separation is classically describable.

When the wave function takes the form (25), the two particles system must be described as a single six-dimensional system and not as a sum of two independent three-dimensional subsystems, for at this time, if we try to express the wave function as $\psi(\mathbf{x}, \mathbf{y}) = R(\mathbf{x}, \mathbf{y}) \times \exp[iS(\mathbf{x}, \mathbf{y})/\hbar]$, we find that the resulting expressions for $R$ and $S$ depend on $\mathbf{x}$ and $\mathbf{y}$ in a very complicated way. The particle momenta, $\mathbf{p}_1 = \nabla_x S(\mathbf{x}, \mathbf{y})$ and $\mathbf{p}_2 = \nabla_y S(\mathbf{x}, \mathbf{y})$, therefore become inextricably interdependent. The "quantum-mechanical" potential,

$$U = -\frac{\hbar^2}{2mR(\mathbf{x}, \mathbf{y})} (\nabla_x^2 R + \nabla_y^2 R)$$

ceases to be expressible as the sum of a term involving $\mathbf{x}$ and a term involving $\mathbf{y}$. The probability density,

$^{14}$ N. F. Mott and H. S. W. Massey, The Theory of Atomic Collisions (Clarendon Press, Oxford, 1933).
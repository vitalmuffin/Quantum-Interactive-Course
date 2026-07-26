“Quantenmechanik der Stoßvorgänge,” Zeit. Phys. **38** (1927), 803-827.

# Quantum mechanics of collision processes (¹).

By **Max Born** in Göttingen.

(Received on 21 July 1926)

Translated by D. H. Delphenich

The *Schrödinger* form of quantum mechanics allows one to define the frequency of a state in a natural way with the help of the intensity of the associated eigen-vibration. This viewpoint leads to a theory of collision processes in which the transition probabilities are determined by the asymptotic behavior of aperiodic solutions.

**Introduction.** Collision processes not only yield the most convincing experimental proof of the basic assumptions of quantum theory, but also seem suitable for explaining the physical meaning of the formal laws of the so-called “quantum mechanics.” Indeed, as it seems, it always produces the correct term values of the stationary states and the correct amplitudes for the oscillations that are radiated by the transitions, but opinions are divided regarding the physical interpretation of the formulas. The matrix form of quantum mechanics (²) that was founded by *Heisenberg* and developed by him and the author of this article starts from the thought that an exact representation of processes in space and time is quite impossible and that one must then content oneself with presenting the relations between the observed quantities, which can only be interpreted as properties of the motions in the limiting classical cases. On the other hand, *Schrödinger* (³) seems to have ascribed a reality of the same kind that light waves possessed to the waves that he regards as the carriers of atomic processes by using the *de Broglie* procedure; he attempts “to construct wave packets that have relatively small dimensions in all directions,” and which can obviously represent the moving corpuscle directly.

Neither of these viewpoints seems satisfactory to me. Here, I would like to try to give a third interpretation and probe its utility in collision processes. I shall recall a remark that *Einstein* made about the behavior of the wave field and light quanta. He said that perhaps the waves only have to be wherever one needs to know the path of the corpuscular light quanta, and in that sense, he spoke of a “ghost field.” It determines the probability that a light quantum – viz., the carrier of energy and impulse – follows a certain path; however, the field itself is ascribed no energy and no impulse.

(¹) A preliminary announcement appeared in Zeit. Phys. **37** (1926), 863.

(²) *W. Heisenberg*, Zeit. Phys. **33** (1925), 879; *M. Born* and *P. Jordan*, *ibidem* **34** (1925), 858; *M. Born*, *W. Heisenberg*, and *P. Jordan*, *ibidem* **35** (1926), 557. See also *P. A. M. Dirac*, Proc. Roy. Soc. **109** (1925), 642; **110** (1926), 561.

(³) *E. Schrödinger*, Ann. d. Phys. **79** (1926), 361, 489, 734. Cf., the second paper, pp. 499. Furthermore, Naturw. **14** (1926), 664.

Born – Quantum mechanics of collision processes.

2

One would do better to postpone these thoughts, when coupled directly to quantum mechanics, until the place of the electromagnetic field in the formalism has been established. However, from the complete analogy between light quanta and electrons, one might consider formulating the laws of electron motion in a similar manner. This is closely related to regarding the *de Broglie-Schrödinger* waves as “ghost fields,” or better yet, “guiding fields.”

I would then like to pursue the following idea heuristically: The guiding field, which is represented by a scalar function $\psi$ of the coordinates of all particles that are involved and time, propagates according to *Schrödinger’s* differential equation. However, impulse and energy will be carried along as when corpuscles (i.e., electrons) are actually flying around. The paths of these corpuscles are determined only to the extent that they are constrained by the law of energy and impulse; moreover, only a probability that a certain path will be followed will be determined by the function $\psi$. One can perhaps summarize this, somewhat paradoxically, as: The motion of the particle follows the laws of probability, but the probability itself propagates in accord with causal laws $^{(1)}$.

If one surveys the three levels in the development of quantum theory then one will see that the lowest one – viz., that of periodic processes – is entirely unsuitable for testing the utility of such a conception. The second level – namely, the level of aperiodic, stationary processes – achieves somewhat more; we would like to concern ourselves with it in the present paper. However, the third level – viz., that of non-stationary evolution – can actually be decisive; there, one must show whether the interference of damped “probability waves” suffices to explain the phenomena that apparently point to a coupling that does not relate to space-time.

Making this concept precise is possible only on the basis of some further mathematical development $^{(2)}$; therefore, we shall turn to that directly, so that we can then return to the hypothesis itself later on.

**§ 1. Definition of the weights and frequencies for periodic systems.** We begin with an entirely formal consideration of the discrete, stationary states of a non-degenerate system. They can be characterized by *Schrödinger’s* differential equation:

$$[H - W, \psi] = 0. \tag{1}$$

Let the eigenfunctions be normalized to 1 $^{(3)}$:

$$\int \psi_n(q) \psi_m^*(q) \, dq = \delta_{nn}. \tag{2}$$

Any arbitrary function $\psi(q)$ can be developed in eigenfunctions:

$^{(1)}$ That means that the knowledge of the state at all points at a moment will establish the distribution of states at all later times.

$^{(2)}$ *N. Wiener* of Cambridge, Mass. has graciously helped me with the mathematical details of this paper; I would like to express my thanks to him for that and acknowledge that I would not have reached my goal without him.

$^{(3)}$ For the sake of simplicity, I shall set the density function equal to 1 here.

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

Born – Quantum mechanics of collision processes.

4

$$W = \sum_n |c_n|^2 W_n. \quad (8)$$

According to our interpretation of the $|c_n|^2$, the right-hand side is the total energy of a system of atoms; this mean value can then be represented as the spatial integral of the energy density of the function $\psi$.

However, nothing will point to our Ansatz in favor of the others as long as we remain within the scope of periodic processes.

**§ 2. Aperiodic systems.** We now go on to the aperiodic processes and, for the sake of simplicity, we shall first consider the case of uniform, rectilinear motion along the $x$-axis. In that case, the differential equation reads:

$$\frac{d^2\psi}{dx^2} + k^2\psi = 0, \quad k^2 = \frac{8\pi^2\mu}{h^2}W; \quad (1)$$

it has all positive values $W$ for its eigenvalues and the eigenfunctions:

$$\psi = c e^{\pm ikx}.$$

In order to be able to define the weights and frequencies, one must, above all, normalize the eigenfunctions. The integral formula that is analogous to (2) breaks down (i.e., the integral is divergent); that is why one employs the “mean value” instead of it:

$$\lim_{a \to \infty} \frac{1}{2a} \int_{-a}^{+a} |\psi(k, x)|^2 dx = \lim_{a \to \infty} \frac{c^2}{2a} \int_{-a}^{+a} e^{ikx} e^{-ikx} dx = 1; \quad (2)$$

it follows from this that $c = 1$, and one has the *normalized eigenfunctions*:

$$\psi(k, x) = e^{\pm ikx}. \quad (3)$$

Any function of $x$ can be composed of these. In order to do that, one must choose the unit for the $k$-scale – i.e., one must establish which segments shall have the weight 1. For that, one considers the free motion to be a limiting case of a periodic one, namely, the eigenvibration of a finite piece of the $x$-axis. One then knows that the number per unit length and per interval $(k, k + dk)$ is equal to $\frac{\Delta k}{2\pi} = \Delta\left(\frac{1}{\lambda}\right)$, where $\lambda$ is the wave length. One will then set:

$$\psi(x) = \int_{-\infty}^{+\infty} c(k)\psi(k, x) d\frac{k}{2\pi} = \int_{-\infty}^{+\infty} c(k) e^{ikx} dk, \quad (4)$$

with

$$c(-k) = c^*(k) \quad (5)$$

Born – Quantum mechanics of collision processes.

5

and expect that $|c(k)|^2$ will then be the measure of the frequency for the interval $\frac{1}{2\pi} dk$.

For a mixture of atoms for which the eigenfunctions appear in the distribution that is given by $c(k)$, let the number that is analogous to § 1, (4) be represented by the integral:

$$\int_{-\infty}^{+\infty} |\psi(x)|^2 dx = \frac{1}{(2\pi)^2} \int_{-\infty}^{+\infty} dx \left| \int_{-\infty}^{+\infty} c(k) e^{ikx} dk \right|^2. \tag{6}$$

If we take the case in which only the small interval $k_1 \le k \le k_2$ is occupied then:

$$\int_{-\infty}^{+\infty} c(k) e^{ikx} dk = \bar{c} \int_{k_1}^{k_2} e^{ikx} dk = \frac{\bar{c}}{ix} (e^{ik_2 x} - e^{ik_1 x}),$$

in which $\bar{c}$ is a mean value. One will then have:

$$\begin{aligned} \int_{-\infty}^{+\infty} |\psi(x)|^2 dx &= \frac{|\bar{c}|^2}{4\pi^2} \int_{-\infty}^{+\infty} \frac{dx}{x^2} (e^{ik_2 x} - e^{ik_1 x})(e^{-ik_2 x} - e^{-ik_1 x}) \\ &= \frac{|\bar{c}|^2}{4\pi^2} 4 \int_{-\infty}^{+\infty} \frac{dx}{x^2} \sin^2 \frac{k_2 - k_1}{2} = \frac{1}{2\pi} |\bar{c}|^2 (k_2 - k_1). \end{aligned}$$

Now, according to de Broglie, the impulse of the translatory motion that belongs to the eigenfunction (8) is equal to:

$$p = \frac{h}{\lambda} = \frac{h}{2\pi} k. \tag{7}$$

It is, perhaps, not superfluous to remark that one can also formulate this as a “matrix”; one must then define the matrices in the continuous spectrum here, not by integrals, but by mean values:

$$\begin{aligned} p(k, k') &= \frac{h}{2\pi i} \lim_{a \to \infty} \frac{1}{2a} \int_{-a}^{+a} \psi'(k, x) \frac{\partial \psi(k', x)}{\partial x} dx \\ &= \frac{h}{2\pi i} \lim_{a \to \infty} \frac{1}{2a} \int_{-a}^{+a} e^{-ikx} ik' e^{ik'x} dx. \end{aligned}$$

$$p(k, k') = \begin{cases} \frac{h}{2\pi} k & \text{ for } k = k', \\ 0 & \text{ " } k \neq k'. \end{cases} \tag{8}$$

If one now replaces $\Delta k = k_2 - k_1$ with $\frac{2\pi}{h} \Delta p$ then one will finally have:

Born – Quantum mechanics of collision processes.

6

$$\int_{-\infty}^{+\infty} |\psi(x)|^2 dx = |\vec{c}|^2 \frac{\Delta p}{h}. \tag{9}$$

One then has the result that a cell of length $\Delta x = 1$ and impulse extension $\Delta p = h$ will have weight 1, in agreement with the Ansatz of Sackur and Tetrode $^{(1)}$, which has been confirmed many times by experiments, and that $|c(k)|^2$ is the frequency for a motion with the impulse $p = \frac{h}{2\pi}k$.

We now go onto accelerated motion. Here, one can naturally define a certain distribution of processes in an analogous way. However, that is not a rational question to pose for collision processes. For those processes, any motion will have a rectilinear asymptote before and after the collision. The particle is then found to be in a practically free state for a very long time (in comparison to the actual duration of the collision) before and after the collision. In agreement with the experimental statement of the problem, one thus comes to the following viewpoint: Let the distribution function $|c(k)|^2$ for the asymptotic motion be known before the collision; can one calculate the distribution function after the collision from it?

Naturally, we are speaking only of a stationary particle current here. Mathematically, the problem then comes down to the following one: The stationary vibration field $\psi$ must be distributed into ingoing and outgoing waves; they are asymptotically plane waves. One then represents both of them by means of a Fourier integral of the form (4) and chooses the coefficient function $c(k)$ for the ingoing waves arbitrarily; it shall then shown that the $c(k)$ is determined completely for the outgoing waves. It yields the distribution into which a prescribed particle mixture will be converted after the collision.

In order to see the relationship clearly, we first treat the one-dimensional case.

§ 3. The asymptotic behavior of the eigenfunctions in a continuous spectrum with one degree of freedom. Schrödinger's differential equation reads:

$$\frac{d^2\psi}{dx^2} + \frac{8\pi^2\mu}{h^2}(W - U(x))\psi = 0, \tag{1}$$

in which $U(x)$ means the potential energy. To abbreviate, we set:

$$\frac{8\pi^2\mu}{h^2}W = k^2, \quad \frac{8\pi^2\mu}{h^2}U(x) = V(x); \tag{2}$$

we will then have:

$$\frac{d^2\psi}{dx^2} + k^2\psi = V\psi. \tag{3}$$

$^{(1)}$ A. Sackur, Ann. d. Phys. 36 (1911), 958; 40 (1913), 67; H. Tetrode, Phys. Zeit. 14 (1913), 212; Ann. d. Phys. 38 (1912), 434.

Born – Quantum mechanics of collision processes.

7

We examine the asymptotic behavior of the solution at infinity. In order to get a simple relationship, we assume that $V(x)$ vanishes faster than $x^{-2}$ at infinity; i.e.:

$$| V(x) | < \frac{K}{x^2}, \tag{4}$$

in which $K$ is a positive number ($^1$).

We now determine $\psi(x)$ by a process of iteration; let:

$$u_0(x) = e^{ikx}, \tag{5}$$

and let $u_1(x), u_2(x), \ldots$ be the solutions of the successive approximations:

$$\frac{d^2 u_n}{dx^2} + k^2 u_n = V u_{n-1},$$

which vanishes as $x \to +\infty$.

One then has:

$$u_n(x) = \frac{1}{k} \int_x^\infty u_{n-1}(\xi) V(\xi) \sin k(\xi - x) d\xi,$$

as one can verify directly. One has:

$$| u_n(x) | \le \frac{1}{k} \int_x^\infty | u_{n-1}(\xi) | \cdot | V(\xi) | d\xi.$$

We now show that:

$$| u_n(x) | \le \frac{1}{n!} \left( \frac{K}{kx} \right)^n.$$

This is correct for $n = 0$, since it follows from (5) that $| u_0(x) | \le 1$. We now assume that is it correct for $n - 1$:

$$| u_{n-1}(\xi) | \le \frac{1}{(n-1)!} \left( \frac{K}{k\xi} \right)^{n-1};$$

it then follows that:

$$| u_n(x) | \le \frac{1}{k} \frac{1}{(n-1)!} \left( \frac{K}{k} \right)^{n-1} \cdot K \int_x^\infty \xi^{-n+1} \xi^2 d\xi = \frac{1}{n!} \left( \frac{K}{kx} \right)^n,$$

as was asserted.

As a result, the series:

$$\psi(x) = \sum_{n=0}^\infty u_n(x) \tag{6}$$

($^1$) The cases of a pure Coulomb field and a dipole field are excluded by this assumption.

Born – Quantum mechanics of collision processes.

8

converges uniformly for every finite interval; it can then be differentiated term-wise arbitrarily often, and is then, as is easy to see, the desired solution to our differential equation.

However, since all $u_1, u_2, \dots$ vanish as $x \to +\infty$, the function $\psi$ will be asymptotic to $u_0 = e^{ikx}$ at positive infinity.

In precisely the same way, one shows that there is a solution that is asymptotic to $e^{-ikx}$ as $x \to +\infty$. Since the general solution has only two constants, it must asymptotically have the form:

$$\psi^+(x) = a e^{ikx} + b e^{-ikx} \tag{7}$$

as $x \to +\infty$. Here, the degeneracy of the system makes its appearance; every energy value $W$ is associated with two values $k, -k$ and two linearly-independent solutions.

In an entirely similar way, it follows that the general solution must have the same form as $x \to -\infty$:

$$\psi^-(x) = A e^{ikx} + B e^{-ikx}. \tag{8}$$

In this, the amplitudes $A, B$ are well-defined functions of $a, b$.

We now decompose the solution into incoming and outgoing waves; for that, we add the time factor $e^{ik\upsilon} \left( k\upsilon = 2\pi\nu = \frac{2\pi}{h}W \right)$ and set:

$$\left. \begin{array}{l} a = c_e e^{i\varphi_e t}, \quad A = C_a e^{i\Phi_a t}, \\ b = c_a e^{-i\varphi_a t}, \quad B = C_e e^{-i\Phi_e t}. \end{array} \right\} \tag{9}$$

One will then have:

$$\left. \begin{array}{l} \psi^+(x) = c_e e^{ik(x+\upsilon t+\varphi_e)} + c_a e^{-ik(x-\upsilon t+\varphi_a)}, \\ \psi^-(x) = C_a e^{ik(x+\upsilon t+\Phi_a)} + C_e e^{-ik(x-\upsilon t+\Phi_a)}. \end{array} \right\} \tag{10}$$

The real parts of the terms that are denoted with the index $e$ represent the incoming waves, while the terms that are denoted with an $a$ represent the outgoing waves.

We are interested in the case in which only one wave is incoming at $x = +\infty$. One will then have $C_e = 0$, and one can arbitrarily set $\varphi_e = 0$, moreover. One will then have:

$$\left. \begin{array}{l} \psi^+(x) = c_e e^{ik(x+\upsilon t)} + c_a e^{-ik(x-\upsilon t+\varphi_a)}, \\ \psi^-(x) = C_a e^{ik(x+\upsilon t+\Phi_a)}. \end{array} \right\} \tag{11}$$

We have shown that $\psi^-(x)$ is determined in terms of $\psi^+(x)$ by integration; i.e., $A, B$ are well-defined functions of $a, b$. In our case $C_e = 0$, so we will have $B = 0$, and one thus has two equations of the form:

$$\left. \begin{array}{l} A = A(a,b), \\ 0 = B(a,b). \end{array} \right\} \tag{12}$$

Born – Quantum mechanics of collision processes.

9

One can express $b$ in terms of $a$ using the second one, and one will then get $A$ expressed in terms of $a$ from the first one. However, that means that the constants of the reflected wave and the constants of the transmitted wave can be calculated from the amplitude of the incoming wave.

One can now show that a relation exists between the intensities of the three waves. One obtains it most simply with the help of the energy theorem.

§ 4. The theorem of the conservation of energy. In order to derive this theorem, we return to the form of Schrödinger's differential equation for which the assumption of vibrations that are purely periodic in time is still not made, so one will have a wave equation of the form:

$$\frac{\partial^2 \psi}{\partial x^2} - \frac{1}{v^2} \frac{\partial^2 \psi}{\partial t^2} = 0. \tag{1}$$

In this, $v$ is the wave velocity. One comes to Schrödinger's equation when one, with de Broglie, sets (1):

$$h\nu = W = \frac{\mu}{2} u^2 + U, \qquad v = \lambda v, \qquad \frac{h}{\lambda} = p = \mu u;$$

one will then have:

$$\frac{1}{v^2} = \frac{h^2}{\lambda^2} \frac{1}{h^2 v^2} = \frac{\mu^2 u^2}{W^2} = \frac{\frac{\mu}{2} u^2 \cdot 2\mu}{W^2},$$

$$\frac{1}{v^2} = \frac{2\mu}{W^2} (W - U). \tag{2}$$

If one now seeks solutions whose time dependency is given by the factor $e^{2\pi i u} = e^{\frac{2\pi i}{h} W}$ then one will get:

$$\frac{d^2 \psi}{dx^2} + \frac{8\pi^2 \mu}{h^2} (W - U) \psi = 0.$$

However, we now fix our attention on the general formula (1) and multiply the equation by $\partial \psi / \partial t$.

One now has:

$$\frac{\partial^2 \psi}{\partial x^2} \frac{\partial \psi}{\partial t} = \frac{\partial}{\partial x} \left( \frac{\partial \psi}{\partial x} \frac{\partial \psi}{\partial t} \right) - \frac{\partial \psi}{\partial x} \frac{\partial^2 \psi}{\partial x \partial t}$$

(1) We neglect relativity and calculate with classical mechanics.

Born – Quantum mechanics of collision processes.

10

$$= \frac{\partial}{\partial x} \left( \frac{\partial \psi}{\partial x} \frac{\partial \psi}{\partial t} \right) - \frac{\partial}{\partial t} \frac{1}{2} \left( \frac{\partial \psi}{\partial x} \right)^2.$$

If $v$ depends upon only $v$ then we will get:

$$\frac{\partial}{\partial x} \left( \frac{\partial \psi}{\partial x} \frac{\partial \psi}{\partial t} \right) - \frac{\partial}{\partial t} \left[ \frac{1}{2} \left( \frac{\partial \psi}{\partial x} \right)^2 + \frac{1}{2v^2} \left( \frac{\partial \psi}{\partial t} \right)^2 \right] = 0. \tag{3}$$

If one integrates over all space then one will get:

$$\left[ \frac{\partial \psi}{\partial x} \frac{\partial \psi}{\partial t} \right]_{-\infty}^{+\infty} - \frac{\partial}{\partial t} \int_{-\infty}^{+\infty} \frac{1}{2} \left\{ \left( \frac{\partial \psi}{\partial x} \right)^2 + \frac{1}{v^2} \left( \frac{\partial \psi}{\partial t} \right)^2 \right\} dx = 0. \tag{4}$$

As was pointed out in § 1, the space integral in this is to be interpreted as the total energy that is present in space. However, its expression does not interest us, since for us it will enter into the in-streaming and out-streaming energy, which will be represented by limiting terms. The time mean of the two terms vanishes for a temporally periodic process, and, with the use of the notations that were introduced in § 3, (7), (8), one will get:

$$\overline{\frac{\partial \psi^-}{\partial x} - \frac{\partial \psi^+}{\partial t}} = \overline{\frac{\partial \psi^+}{\partial x} - \frac{\partial \psi^+}{\partial t}}. \tag{5}$$

This equation states that the in-streaming energy is equal to the out-streaming energy. When we substitute the real part of the expression § 3, (10) in this, we will get:

$$C_a^2 - C_e^2 = c_a^2 - c_e^2, \tag{6}$$

or, in the case $C_e = 0$ [as in equation (11), § 3]:

$$c_e^2 = c_a^2 + C_a^2. \tag{7}$$

However, that means that for any elementary wave of given $k$, the incoming intensity will be split into the intensities of the two waves that scatter to the right and left, or, in the language of the corpuscular theory: If a particle with a given energy enters the atom then it will either be reflected or it will continue on. The sum of the probabilities in these two outcomes is 1.

The theorem of the conservation of energy then has the conservation of particle number as a consequence. The basis for that lies in the degeneracy of the system; any energy value belongs to several motions, and they will be related to each other.

Born – Quantum mechanics of collision processes.

11

§ 5. Generalization to three degrees of freedom. The inertial motion. We now consider a particle that moves in space under the action of the potential energy $U(x, y, z)$. One then has the differential equation:

$$\Delta\psi - \frac{1}{v^2} \frac{\partial^2\psi}{\partial t^2} = 0, \tag{1}$$

which is analogous to (1), in which $v$ is once more given in the approximation of classical mechanics by (2), § 4. Here, the conservation law reads:

$$\text{div}\left(\frac{\partial\psi}{\partial t}\text{grad}\psi\right) - \frac{\partial}{\partial t}\frac{1}{2}\left\{(\text{grad}\psi)^2 + \frac{1}{v^2}\left(\frac{\partial\psi}{\partial t}\right)^2\right\} = 0, \tag{2}$$

or, when integrated over space:

$$\int_{-\infty}^{\infty} \frac{\partial\psi}{\partial t} \frac{\partial\psi}{\partial t} d\sigma - \frac{\partial}{\partial t}\int \frac{1}{2}\left\{(\text{grad}\psi)^2 + \frac{1}{v^2}\left(\frac{\partial\psi}{\partial t}\right)^2\right\} dS = 0, \tag{3}$$

in which $dS = dx\,dy\,dz$, and $d\sigma$ is the element of an infinitely-distant, closed surface with exterior normal $v$. For temporally periodic processes, it then follows from this that the temporal mean will be:

$$\overline{\int_{-\infty}^{\infty} \frac{\partial\psi}{\partial t} \frac{\partial\psi}{\partial t} d\sigma} = 0. \tag{4}$$

For this case, the differential equation reads:

$$\Delta\psi + (k^2 - V)\psi = 0, \tag{5}$$

where one has set:

$$k^2 = \frac{8\pi^2\mu}{h^2} W, \quad V(x, y, z) = \frac{8\pi^2\mu}{h^2} U(x, y, z). \tag{6}$$

For the inertial motion (viz., $V = 0$), one has the differential equation:

$$\Delta\psi + k^2\psi = 0 \tag{7}$$

and the solution:

$$\psi = e^{i(kx)}; \tag{8}$$

here, $x$ is the vector $x, y, z$, while the vector $k$ satisfies the equation:

$$|k|^2 = k_x^2 + k_y^2 + k_z^2 = k^2, \tag{9}$$

and it is equal to the impulse vector:

Born – Quantum mechanics of collision processes.

12

$$\mathfrak{p} = \frac{h}{2\pi}\mathfrak{k}, \tag{10}$$

up to a factor.

The de Broglie wave length will be given by $h / \lambda = p = |\mathfrak{p}| = \frac{h}{2\pi}k$. The solution (8) should be regarded as normalized in the sense of taking the mean [see (2), § 2]. We briefly denote a function of $x, y, t$ by $f(\mathfrak{r})$, a function of $k_x, k_y, k_z$ by $f(\mathfrak{k})$, etc. Let $dS = dx dy dz$.

The most general solution of (7) is:

$$\psi(\mathfrak{r}) = u_0(\mathfrak{r}) = \int c(\mathfrak{s})e^{ik(\mathfrak{r}\mathfrak{s})} d\omega, \quad d\mathfrak{s} = c^*(\mathfrak{s}), \tag{11}$$

in which $\mathfrak{s}$ is a unit vector and $d\omega$ is the element of solid angle. It represents inertial motion in all possible directions with the same energy. From our basic principles, $|c(\mathfrak{s})|^2$ is the number of particles that flow in the direction $\mathfrak{s}$ per unit solid angle.

We now derive an asymptotic representation for $u_0$ that shows clearly how $u_0$ behaves at infinity. Although one can obtain the result very simply, here, we would like to obtain it by a general method that can be carried over to the cases that will be developed later on. We think of a new rectangular coordinate system $X, Y, Z$ that has been introduced with the help of the orthogonal transformation:

$$\left. \begin{array}{ll} x = a_{11}X + a_{12}Y + a_{13}Z, & X = a_{11}x + a_{21}y + a_{31}z, \\ y = a_{21}X + a_{22}Y + a_{23}Z, & Y = a_{12}x + a_{22}y + a_{32}z, \\ z = a_{31}X + a_{32}Y + a_{33}Z, & Z = a_{13}x + a_{23}y + a_{33}z. \end{array} \right\} \tag{12}$$

At equal times, we introduce the new unit vector $\mathfrak{S}$, in place of the unit vector $\mathfrak{s}$, with the help of the same orthogonal transformation; the solid angle element $d\omega$ then goes over into a new $d\Omega$, and one will have:

$$\mathfrak{r}\,\mathfrak{s} = \Re\,\mathfrak{S}. \tag{13}$$

We now choose the new coordinate system especially such that:

$$X = 0, \quad Y = 0; \tag{14}$$

one will then have:

$$Z = r = \sqrt{x^2 + y^2 + z^2}. \tag{15}$$

Our integral will be:

$$\begin{array}{l} u_0(x, y, z) = u_0(a_{13}Z, a_{23}Z, a_{33}Z) \\ = \int d\Omega c (a_{11}\mathfrak{S}_x + a_{12}\mathfrak{S}_y + a_{13}\mathfrak{S}_z, \cdots) e^{ikZ\mathfrak{S}_z}. \end{array}$$

Moreover, we introduce polar coordinates for $\mathfrak{S}$:

Born – Quantum mechanics of collision processes.

13

$$\mathfrak{S}_x = \sin \vartheta \cos \varphi, \quad \mathfrak{S}_y = \sin \vartheta \sin \varphi, \quad \mathfrak{S}_z = \cos \vartheta \tag{16}$$

and set $\cos \vartheta = \mu$; we will then have:

$$u_0 = \int_0^{2\pi} d\varphi \int_{-1}^{+1} d\mu c \left[ \sqrt{1-\mu^2} (a_{11} \cos \varphi + a_{12} \sin \varphi) + \mu a_{13}, \cdots \right] e^{ikZ\mu}.$$

It follows from this by partial integration that:

$$\begin{aligned} u_0 &= \frac{1}{ikZ} \int_0^{2\pi} d\varphi \left[ c(a_{13}, a_{23}, a_{33}) e^{ikZ} - c(-a_{13}, -a_{23}, -a_{33}) e^{-ikZ} \right] \\ &- \frac{1}{ikZ} \int_0^{2\pi} d\varphi \frac{d}{d\mu} c \left[ \sqrt{1-\mu^2} (a_{11} \cos \varphi + a_{12} \sin \varphi) + \mu a_{13}, \cdots \right] e^{ikZ\mu} d\mu. \end{aligned}$$

Repeated application of the same process shows that the second term vanishes like $Z^{-2}$. If one now introduces $Z = r$, $a_{13} = \frac{x}{Z} = \frac{x}{r}$, ... then one will get the asymptotic representation:

$$u_0^\infty(x, y, z) = \frac{2\pi}{ikr} \left\{ c\left(\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right) e^{ikr} - c\left(-\frac{x}{r}, -\frac{y}{r}, -\frac{z}{r}\right) e^{-ikr} \right\}, \tag{17}$$

or, in real notation, with $c = |c| e^{ik\gamma}$:

$$u_0^\infty(x, y, z) = \frac{4\pi}{k} \left| c\left(\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right) \right| \frac{\sin k \left[ r + \gamma \left(\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right) \right]}{r}. \tag{18}$$

That means that $u_0$ behaves asymptotically like a spherical wave with an amplitude and phase that depends upon the direction. The intensity, as a function of the direction $\mathfrak{s} = \mathfrak{r} / r$, determines the flux of the particles that flow through the solid angle element $d\omega$ with the axis $\mathfrak{s}$:

$$\Phi_0 d\omega = |c(\mathfrak{s})|^2 d\omega \tag{19}$$

§ 6. Elastic collisions. We now go on to the integration of the general equation (5), § 5:

$$\Delta\psi + (k^2 - V) \psi = 0; \tag{1}$$

physically, it represents the case in which an electron collides with an atom that cannot be excited by that.

Born – Quantum mechanics of collision processes.

14

As in § 3, we determine $\psi$ by a process of iteration in which the function $u_0$ that we just introduced in (11), § 5 will serve as the initial function. We then calculate $u_1, u_2, \ldots$ in succession from the approximation equations:

$$\Delta u_n + k^2 u_n = V u_{n-1} = F_{n-1} \tag{2}$$

Green's theorem yields the solution that corresponds to the outgoing waves with the time factor $e^{ik\nu t}$ in the form of:

$$u_n(\tau) = -\frac{1}{4\pi} \int F_{n-1}(\tau') \frac{e^{-ik[\tau-\tau']}}{\tau - \tau'} dS', \tag{3}$$

in which $\tau'$ means the vector with the components $x', y', z'$, and $dS' = dx' dy' dz'$. The convergence of the process can be proved on the basis of the assumption that $V$ goes to zero like $r^{-2}$ ($^1$); however, we shall not go into that, but assume that the series:

$$\psi(\tau) = \sum_{n=0}^{\infty} u_n(\tau)$$

represents the solution.

We investigate the asymptotic behavior of $u_n(\tau)$. We write, more thoroughly:

$$u_n(x, y, z) = -\frac{1}{4\pi} \int F_{n-1}(x', y', z') \frac{e^{-ik\sqrt{(x-x')^2 + (y-y')^2 + (z-z')^2}}}{\sqrt{(x-x')^2 + (y-y')^2 + (z-z')^2}} dx' dy' dz'.$$

We now once more introduce the rotation of the coordinate system that was given in § 5 and subject the integration variables to that rotation. One will then have:

$$u_n(x, y, z) = u_n(a_{13}Z, a_{23}Z, a_{33}Z)$$

$$= -\frac{1}{4\pi} \int F'_{n-1}(X', Y', Z') \frac{e^{-ik\sqrt{X'^2 + Y'^2 + Z'^2}}}{\sqrt{X'^2 + Y'^2 + (Z-Z')^2}} dX' dY' dZ'; \tag{4}$$

in this, one has:

$$F'_{n-1}(X', Y', Z') = F_{n-1}(a_{11}X' + a_{11}Y' + a_{13}Z', \ldots). \tag{5}$$

We now introduce polar coordinates:

$$X' = \rho \sin \vartheta \cos \varphi, \quad Y' = \rho \sin \vartheta \sin \varphi, \quad Z' = \rho \cos \vartheta.$$

One will then have:

($^1$) The case of ions is excluded from this; for them, one would have to take a hyperbolic path of the electron as the starting estimate in the approximation process, instead of a rectilinear motion. On this, see a treatise of J. R. Oppenheimer that will appear soon in Proc. Cambridge Phil. Soc., 26 July 1926.

Born – Quantum mechanics of collision processes.

15

$$u _ { n } = - \frac { 1 } { 4 \pi } \int _ { 0 } ^ { 2 \pi } d \varphi \int _ { 0 } ^ { \infty } \rho ^ { 2 } d \rho \int _ { 0 } ^ { \pi } \sin \vartheta d \vartheta F _ { n - 1 } ^ { \prime } ( \rho \sin \vartheta , \cdots ) \frac { e ^ { - i k \sqrt { \rho ^ { 2 } + Z ^ { 2 } - 2 \rho Z \cos \vartheta } } } { \sqrt { \rho ^ { 2 } + Z ^ { 2 } - 2 \rho Z \cos \vartheta } } .$$

Finally, we introduce the integration variable $\mu$ in place of $\vartheta$ by way of:

$$\begin{array} { l } { { \sqrt { \rho ^ { 2 } + Z ^ { 2 } - 2 \rho Z \cos \vartheta } = Z \mu , } } \\ { { \sin \vartheta d \vartheta = \displaystyle \frac { Z } { \rho } \mu d \mu ; } } \end{array}$$

the limits of integration will then become:

$$\vartheta = 0 ; \mu = \left| \frac { \rho } { Z } - 1 \right| ; \qquad \vartheta = \pi ; \mu = \frac { \rho } { Z } + 1 ,$$

and $\cos \vartheta , \sin \vartheta$ will be certain functions $c ( \rho , Z , \mu ) , s ( \rho , Z , \mu )$ that will assume the values $c = 1 , s = 0$ at the lower limits and the values $c = - 1 , s = 0$ at the upper ones. One will then obtain:

$$u _ { n } = - \frac { 1 } { 4 \pi } \int _ { 0 } ^ { 2 \pi } d \varphi \int _ { 0 } ^ { \infty } \rho d \rho \int _ { \left| \frac { \rho } { Z } - 1 \right| } ^ { \frac { \rho } { Z } + 1 } F _ { n - 1 } ^ { \prime } ( \rho s \cos \vartheta , \rho s \sin \vartheta , \rho c ) e ^ { - i k \mu Z } d \mu .$$

As in § 5, one will obtain the asymptotic representation from this by partial integration:

$$u _ { n } ^ { \infty } = \frac { 1 } { 4 \pi } \int _ { 0 } ^ { 2 \pi } d \varphi \int _ { 0 } ^ { \infty } \rho d \rho \frac { 1 } { i k Z } \Big [ F _ { n - 1 } ^ { \prime } ( 0 , 0 , \rho ) e ^ { - i k ( Z + \rho ) } - F _ { n - 1 } ^ { \prime } ( 0 , 0 , - \rho ) e ^ { - i k | Z - \rho | } \Big ] .$$

Here, from (5), one has:

$$F _ { n - 1 } ^ { \prime } ( 0 , 0 , \rho ) = F _ { n - 1 } ( a _ { 1 3 } \rho , a _ { 2 3 } \rho , a _ { 3 3 } \rho ) = F _ { n - 1 } \left( \frac { \rho x } { r } , \frac { \rho y } { r } , \frac { \rho z } { r } \right) ,$$

$$F _ { n - 1 } ^ { \prime } ( 0 , 0 , - \rho ) = F _ { n - 1 } ( - a _ { 1 3 } \rho , - a _ { 2 3 } \rho , - a _ { 3 3 } \rho ) = F _ { n - 1 } \left( - \frac { \rho x } { r } , - \frac { \rho y } { r } , - \frac { \rho z } { r } \right) .$$

One will then have:

$$\begin{array} { l } { { u _ { n } ^ { \infty } = \displaystyle \frac { e ^ { - i k r } } { 2 i k r } \int _ { 0 } ^ { \infty } \rho d \rho F _ { n - 1 } \left( \frac { \rho x } { r } , \frac { \rho y } { r } , \frac { \rho z } { r } \right) e ^ { - i k \rho } } } \\ { { - \displaystyle \frac { e ^ { - i k r } } { 2 i k r } \int _ { 0 } ^ { r } \rho d \rho F _ { n - 1 } \left( - \frac { \rho x } { r } , \cdots \right) e ^ { i k \rho } - \frac { e ^ { i k r } } { 2 i k r } \int _ { r } ^ { \infty } \rho d \rho F _ { n - 1 } \left( - \frac { \rho x } { r } , \cdots \right) e ^ { - i k \rho } . } } \end{array}$$

Here, the last integral vanishes as $r \to \infty$; if we assume that $| V | \leq a r ^ { - 2 }$ there, then due to the fact that $| u _ { 0 } | \leq b r ^ { - 1 }$, we will have:

Born – Quantum mechanics of collision processes.

16

$$| F _ { n - 1 } | \leq \frac { A } { r ^ { 2 } } ,$$

so

$$\left| \int _ { r } ^ { \infty } \rho \, d \rho \, F _ { n - 1 } \left( - \frac { \rho x } { r } , \dots \right) e ^ { - i k \rho } \right| \leq A \int _ { r } ^ { \infty } \frac { d \rho } { \rho ^ { 2 } } = \frac { A } { r } .$$

We then finally obtain:

$$u _ { n } ^ { \infty } = \frac { e ^ { - i k r } } { 2 i k r } \int _ { 0 } ^ { \infty } \rho \, d \rho \left[ F _ { n - 1 } \left( \frac { \rho x } { r } , \dots \right) e ^ { - i k \rho } - F _ { n - 1 } \left( - \frac { \rho x } { r } , \dots \right) e ^ { - i k \rho } \right] . \tag { 6 }$$

However, this can be put into a more transparent form. In order to do that, we introduce the Fourier coefficients of the function $F _ { n - 1 }$ :

$$\begin{array} { l } { { f _ { n - 1 } ( \mathfrak { l } ) = \displaystyle \frac { 1 } { ( 2 \pi ) ^ { 3 } } \iiint F _ { n - 1 } ( \mathfrak { r } ) e ^ { - i \mathfrak { l } } d S } } \\ { { \qquad = \displaystyle \frac { 1 } { ( 2 \pi ) ^ { 3 } } \int _ { 0 } ^ { \infty } r ^ { 2 } d r \iint d \omega F _ { n - 1 } ( \mathfrak { r s } ) e ^ { - i k ( \mathfrak { r s } ) } . } } \end{array} \tag { 7 }$$

We determine the asymptotic value from the already twice-performed process, and obtain:

$$f _ { n - 1 } ^ { \infty } ( k _ { x } , k _ { y } , k _ { z } ) = \frac { 1 } { 4 \pi ^ { 2 } i k } \int _ { 0 } ^ { \infty } r \, d r \left[ F _ { n - 1 } \left( \frac { r k _ { x } } { k } , \dots \right) e ^ { i k r } - F _ { n - 1 } \left( - \frac { r k _ { x } } { k } , \dots \right) e ^ { - i k r } \right] .$$

One will then have:

$$f _ { n - 1 } ^ { \infty } \left( - k \frac { x } { r } , - k \frac { y } { r } , - k \frac { z } { r } \right) = \frac { 1 } { 4 \pi ^ { 2 } i k } \int _ { 0 } ^ { \infty } \rho \, d \rho \left[ F _ { n - 1 } \left( \frac { \rho x } { r } , \dots \right) e ^ { - i k \rho } - F _ { n - 1 } \left( - \frac { \rho x } { r } , \dots \right) e ^ { i k \rho } \right] . \tag { 8 }$$

If we substitute that into (6) then we will finally obtain:

$$u _ { n } ^ { \infty } ( x , y , z ) = 2 \pi ^ { 2 } \, f _ { n - 1 } ^ { \infty } \left( - k \frac { x } { r } , - k \frac { y } { r } , - k \frac { z } { r } \right) \frac { e ^ { - i k r } } { r } . \tag { 9 }$$

If we compare that with the formulas (11) and (18) of § 5 then we will see that an observer at infinity will see the scattered radiation as a plane wave with the amplitude:

$$\frac { k } { 2 \pi } 2 \pi ^ { 3 } \left| f _ { n - 1 } ^ { \infty } ( - k \mathfrak { s } ) \right| = k \pi \left| f _ { n - 1 } ^ { \infty } ( - k \mathfrak { s } ) \right| ,$$

which will depend upon the direction $\mathfrak { s }$ ; thus, the probability that an electron will be deflected into an element of solid angle $d \omega$ with the mean direction $\mathfrak { s }$ will be:

Born – Quantum mechanics of collision processes.

17

$$\Phi \, d\omega = \pi^2 k^2 \left| \sum_{n=0}^{\infty} f_n^{\infty}(-k\mathfrak{s}) \right|^2 d\omega. \tag{10}$$

The total solution has the asymptotic form:

$$\psi^{\infty} = u_0^{\infty} + \sum_{n=1}^{\infty} u_n^{\infty} = \frac{2\pi}{k} \left\{ |c(\mathfrak{s})| e^{ik(r+\delta)} + k\pi \sum_{n=1}^{\infty} f_n^{\infty}(-k\mathfrak{s}) e^{-ikr} \right\}.$$

If one adds the time factor $e^{ik\nu t}$ to this then formula (4), § 5 will easily give the “conservation of particle number.”

In the first approximation, one has:

$$\Phi \, d\omega = \pi^2 k^2 \left| f_0^{\infty}(-k\mathfrak{s}) \right|^2 d\omega, \tag{11}$$

in which one calculates $f_0$, either rigorously from the formula:

$$f_0(\mathfrak{k}) = \frac{1}{(2\pi)^3} \int F_0(\mathfrak{r}) e^{-i(\mathfrak{k}\mathfrak{r})} dS \tag{12}$$

or one can employ the asymptotic expression [from (8)]:

$$f_0^{\infty}(-k\mathfrak{s}) = \frac{1}{4\pi^2 i k} \int_0^{\infty} \rho \, d\rho \{ F_0(\rho\mathfrak{s}) e^{ik\rho} - F_0(-\rho\mathfrak{s}) e^{-ik\rho} \}. \tag{13}$$

§ 7. Inelastic electron collisions. Let an atom (or a molecule; however, we will still say “atom”) be given by the Hamiltonian function $H^a(p, q)$ ($^1$); let Schrödinger’s differential equation for this system be solved, so one knows the eigenvalues $W_n^a$ and eigenfunctions $\psi_n^a(q)$ that satisfy the equations:

$$[H^a - W_n^a, \psi_n^a] = 0 \tag{1}$$

identically.

An electron collides with this atom; the Hamiltonian function for the free electron is:

$$H^e = \frac{1}{2\mu} (p_x^2 + p_y^2 + p_z^2),$$

the eigenvalues are all positive numbers $W^e$, and the eigenfunctions are:

($^1$) We briefly write $p, q$, instead of $p_1, p_2, \dots, p_f, q_1, \dots, q_f$.

Born – Quantum mechanics of collision processes.

18

$$e^{\pm k(\mathfrak{s})}, \quad k^2 = \frac{8\pi^2\mu}{h^2} W^\varepsilon. \tag{2}$$

The general solution that corresponds to the incoming wave is:

$$\psi_k^\varepsilon = \int_{\mathfrak{s}>0} c^0(\mathfrak{s}) e^{ik(\mathfrak{s})} d\omega; \tag{3}$$

it satisfies the differential equation:

$$[H^\varepsilon - W^\varepsilon, \psi_k^\varepsilon] = 0 \quad \text{or} \quad \Delta\psi_k^\varepsilon + k^2\psi_k^\varepsilon = 0. \tag{4}$$

The potential energy:

$$U(q; x, y, z) \tag{5}$$

exists between the atom and the electron.

The interaction between the two particles leads to the *Hamiltonian* function:

$$H = H^0 + \lambda H^{(1)},$$

where

$$\left. \begin{array}{c} H^0 = H^a + H^\varepsilon, \\ \lambda H^{(1)} = U. \end{array} \right\}$$

The unperturbed system has the solution:

$$W_{nk}^0 = W_n^a + W^\varepsilon, \qquad \psi_{nk}^0 = \psi_n^a \psi_k^\varepsilon.$$

We solve *Schrödinger's* differential equation for the perturbed system:

$$[H - W, \psi] = 0$$

by the Ansatz:

$$\psi = \psi^0 + \lambda \psi^{(1)} + \dots$$

We will then get the approximation equations:

$$[H^0 - W_{nk}^0, \psi_{nk}^{(1)}] = -U \psi_{nk}^0,$$

$$[H^0 - W_{nk}^0, \psi_{nk}^{(2)}] = -U \psi_{nk}^{(1)},$$

whose left-hand sides agree. We write them out in detail:

$$[H^0, \psi_{nk}^{(1)}] + [H^\varepsilon, \psi_{nk}^{(1)}] - W_{nk}^0 \psi_{nk}^{(1)} = -U \psi_{nk}^0,$$

or

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

Born – Quantum mechanics of collision processes.

20

However, the difference between this problem and the former one is the following: Every transition ($n \to m$) of the atom corresponds to a special differential equation whose right-hand side is determined from the corresponding matrix element of the potential energy. Moreover, another value $k_{nm}$ that corresponds to the energy:

$$W_{nm}^{e} = \frac{h^{2}}{8\pi^{2}\mu} k_{nm}^{2} = h\nu_{nm}^{a} + W^{e} \tag{9}$$

enters in place of the $k$-value of the incoming wave. The basic qualitative law of electron collisions already follows from that: The energy of the electron after the collision is, in general, not equal to the energy before the collision, but differs from it by an energy jump $h\nu_{nm}^{a}$ of the atom. A probability function:

$$\Phi_{nm} = \pi^{2} k_{nm}^{2} |f_{0}^{\infty}(-k_{nm}s)|^{2} \tag{10}$$

belongs to any collision process that one can calculate with the help of formula (12) or (13), § 6.

§ 8. Physical consequences. We next show that our formulas correctly duplicate the qualitative behavior of atoms under collisions, and thus, the fact of “energy jumps,” which has always been regarded as the basic pillar of quantum theory, as well as the most egregious contradiction to classical mechanics.

We order the energy levels of the atom by their magnitudes:

$$W_{0}^{a} < W_{1}^{a} < W_{2}^{a} < \dots$$

The index 0 then denotes the normal state, and one has:

$$h\nu_{nm}^{a} = W_{n}^{a} - W_{m}^{a} > 0 \quad \text{for} \quad n > m.$$

We next consider the case in which the atom is initially in the normal state. One then has that all $\nu_{nm}^{a} > 0$, and it will follow from (9), § 7 that:

$$W_{0m}^{e} = W^{e} - h\nu_{m0}^{a}.$$

Now, if $W^{e} < h\nu_{10}^{a}$ then $W_{0m}^{e}$ would be negative for $m > 0$, which is impossible; thus, one must have $m = 0$, so:

$$W_{00}^{e} = W^{e}.$$

One then finds “elastic” reflection with the profit $\Phi_{00}$. If one lets $W^{e}$ increase until:

Born – Quantum mechanics of collision processes.

21

$$h v_{10}^a < W^e < h v_{20}^a$$

then $W_{0m}^e$ will become only positive for $m = 0$ and $m = 1$; one then has either elastic reflection with the profit $\Phi_{00}$ or stimulated resonance with the profit $\Phi_{01}$.

If $W^e$ increases further until:

$$h v_{20}^a < W^e < h v_{30}^a$$

then there will be three cases: Elastic reflection with profit $\Phi_{00}$, stimulation of the first quantum jump with $\Phi_{01}$, stimulation of the second quantum jump with $\Phi_{02}$. One proceeds further in the same way.

We now fix out attention on the fact that the atom is initially in the second quantum state ($n = 1$); one will then have $v_{10}^a > 0$ and $v_{1m}^a < 0$ for $m = 2, 3, \ldots$

One then has:

$$\begin{array}{l} W_{10}^e = W^e + h v_{10}^a, \\ W_{11}^e = W^e, \\ W_{1m}^e = W^e - h v_{m1}^a, \quad m = 2, 3, \ldots \end{array}$$

Now, if $W^e < h v_{21}^a$ then $W_{1m}^e$ will be negative for $m = 2, 3, \ldots$; therefore, there is only either a collision of the second kind with an energy increase for the electron by $h v_{10}^a$, with a profit of $\Phi_{10}$, or elastic reflection with the profit $\Phi_{11}$.

If one has:

$$h v_{21}^a < W^e < h v_{31}^a$$

then the stimulation of the state $n = 2$ with the profit $\Phi_{12}$ will enter into these processes. One proceeds further in the same way.

In the general case, if the atom is initially in the state $n$ then there will be only collisions of the second kind for:

$$W^e < h v_{n+1,n}^a,$$

for which, the atom will drop into the states $0, 1, \ldots, n - 1$ and give up the energy values $h v_{n0}^a, h v_{n1}^a, \ldots, h v_{n,n+1}^a$, to the electron, with the profits $\Phi_{n0}, \Phi_{n1}, \ldots, \Phi_{n,n-1}$, and the elastic reflection $\Phi_{nm}$. If $W^e$ increases over $h v_{n+1,n}^a$ then there will be stimulations with the profits $\Phi_{n,n+1}, \Phi_{n,n+2}, \ldots, \Phi_{n,m}$ when:

$$h v_{n+1,n}^a < W^e < h v_{m+1,n}^a.$$

The next problem would be to discuss the formula (10), § 7 for the profit; thus, we would like to content ourselves with an entirely tentative, if not truly debatable, consideration.

Born – Quantum mechanics of collision processes.

22

We assume that the potential $U$ can be developed in powers of $r^{-1}$; for a neutral atom, one will then have the dipole terms:

$$U(x, y, z) = \frac{e}{r^3} (\mathfrak{P}\mathfrak{r}) \tag{1}$$

in the first approximation, where $\mathfrak{P}(q)$ is the electric moment of the atom. We then associate it with the matrix $\mathfrak{P}_{nm}$. From (6), § 7, one will then have:

$$V_{nm} = \frac{8\pi^2 \mu e}{h^2} \left( \mathfrak{P}_{nm} \frac{\mathfrak{r}}{r^3} \right). \tag{2}$$

Naturally, this Ansatz can only be correct for electrons that pass by the atom at the distance considered. We therefore restrict our consideration to electrons for which $r > r_0$ ($^1$), and thus write, from (13), § 6:

$$f_0^\infty(-k_{nm}\mathfrak{s}) = \frac{1}{4\pi^2 i k_{nm}} \int_{r_0}^\infty \rho \, d\rho \left\{ F_{nm}(\rho\mathfrak{s}) e^{-i\rho k_{nm}} - F_{nm}(-\rho\mathfrak{s}) e^{i\rho k_{nm}} \right\}.$$

We now assume that that the incoming electrons define a parallel bundle, which corresponds to a plane wave; one will then have:

$$F_{nm}(r\mathfrak{s}) = V_{nm} e^{ik\rho\mathfrak{s}_z} = \frac{8\pi^2 \mu e}{h^2} (\mathfrak{P}_{nm}, \mathfrak{s}) \frac{e^{ik\rho\mathfrak{s}_z}}{\rho^2}.$$

Moreover, one will have:

$$i \pi k_{nm} f_0^\infty(-k_{nm}\mathfrak{s}) = 4\pi \frac{\mu e}{h^2} (\mathfrak{P}_{nm}, \mathfrak{s}) A, \tag{3}$$

for which, with $\mathfrak{s}_z = \cos \vartheta$, one will have:

$$A = \int_{r_0}^\infty \frac{d\rho}{\rho} \cos [r (k \cos \vartheta - k_{nm})], \tag{4}$$

or

$$A = - C_i (r_0 [k \cos \vartheta - k_{nm}]), \tag{5}$$

in which $C_i(x)$ means the integral cosine ($^2$).

From (10), § 7, the profit function then becomes:

($^1$) The exclusion of the central collisions means the temporary sacrifice of being able to interpret an especially interesting group of phenomena, namely, the penetrability of the atom for slow electrons (viz., the Ramsauer effect).

($^2$) S. E. Jahnke and P. Emde, Funktionentafeln, Leipzig, 1909, pp. 19.

Born – Quantum mechanics of collision processes.

23

$$\Phi_{nm} = \frac{16\pi^2\mu^2e^2}{h^4} |\mathfrak{P}_{nm}, s|^2 A^2. \tag{6}$$

If one finally takes the mean over all positions of the atoms then the mean value of the product of two components of $\mathfrak{P}_{nm}$ will vanish, and the mean value of the square of the components will be equal to $\frac{1}{2}|P_{nm}|^2$, where $P$ means the magnitude of the electric moment. One thus obtains:

$$\Phi_{nm} = \frac{16\pi^2\mu^2e^2}{3h^2} |P_{nm}|^2 A^2. \tag{6}$$

We would like to discuss this expression for the profit function briefly.

One first sees that in our approximation, the profit is proportional to $|P_{nm}|^2$; i.e., for $m \neq n$, to the coefficients of the transition probability $b_{nm}$ of Einstein's theory of radiation, which corresponds to the processes of absorption and stimulated emission in the radiation

processes (but not with the probabilities of spontaneous radiation $a_{nm} = \frac{8\pi h v_{nm}^3}{c^3} b_{nm}$) $^{(1)}$.

The profit for elastic reflection is proportional to $|P_{nm}|^2$, which is a quantity that is not optically effective. The diagonal elements of the matrix $P_{nm}$ will be zero, in general $^{(2)}$; namely, in addition to the small number of cases in which a linear Stark effect exist (as for the hydrogen atom). Pauli has informed me that he could even derive the vanishing of the diagonal elements of the quadrupole and higher moments for the s-terms of the alkali metals and the normal states of the noble gases and rare earths, which is a result that represents the exact expression for a spherically-symmetric domain of action of the atom. Our approximation thus does not suffice for the calculation of the elastic reflections, for which, one must carry out the approximation to one step further. That should be done next in order to arrive at the possibility of testing our theory for the large body of observations (Lenard and others) of free path lengths of electrons in unexcited gases. Without precise calculation, one can then see that the profit will be determined by terms that are of fourth order in $P_{nm}$. Naturally, these terms are much smaller than $|P_{nm}|^2$. From that, we can understand that the normal cross section of atoms ($n = 0$) for slow electrons is much smaller (with the order of magnitude of "gas kinetics") than it is for fast electrons, which can be stimulated $^{(3)}$.

The dependency of the profit upon direction will be determined by the function $A^2$ according to (5). It obviously corresponds to a diffraction phenomenon.

This consequence of de Broglie's theory was pointed out about a year ago by W. Elsasser $^{(4)}$. When he seriously considered the wave picture, he concluded that the slow

$^{(1)}$ See J. H. van Vleck, Phys. Rev. 23 (1924), 330; Journ. Opt. Soc. Amer. 9 (1924), 27. M. Born and P. Jordan, Zeit. Phys. 33 (1925), 479.

$^{(2)}$ For the harmonic oscillator, e.g., they are zero, but they are present for the anharmonic oscillator.
$^{(3)}$ One finds literature on this in the book that appeared just recently by J. Franck and P. Jordan, Anregung von quantensprüngen durch Stöße (Berlin, J. Springer, 1926).

$^{(4)}$ W. Elsasser, Die Naturwiss. 13 (1925), 711. The order of magnitude relationship that Elsasser's argument founded rests upon the de Broglie formula for the wave length:

Born – Quantum mechanics of collision processes.

24

electrons must be deflected by atoms in such a way that their distribution after the collision might correspond to the intensity of the light that is diffracted by a small sphere (¹). He coupled it with the observations of Ramsauer on the free path length of electrons (²) and the experiments of Davisson and Kunsman (³) in the angular distribution of electrons that were reflected from a platinum plate. In the meantime, the validity of the argument has been confirmed by experiment by Dymond (⁴), who observed the appearance of interference maxima for reflected electrons in helium directly. A test of our formula for the general body of observations shall result later.

§ 9. Concluding remarks. On the basis of the foregoing arguments, I would like to go into the meaning of the statement that quantum mechanics allows one to formulate not only the problem of stationary states, but also that of transition processes. The Schrödinger picture thus seems to be by far the easiest picture to calculate in; moreover, it makes it possible to preserve the usual conceptions of space and time, in which the events play out in a completely normal way. By contrast, the proposed theory does not correspond to the consequences of the causal determinacy of the individual events. In my tentative communication, I have emphasized this indeterminacy in particular, since it seems to me to be in the best agreement with the practice of experimenters. However, it is naturally indefensible (if one would not like to reassure oneself) to assume that it will give further parameters that have still not been introduced into the theory that would determine the individual events. In classical mechanics, they would be the “phases” of the motion – e.g., the coordinates of the particles at a certain moment. It seems at first improbable to me that one could insert quantities into the new theory informally that would correspond to these phases; however, Frenkel has informed me that this can perhaps happen. Be that as it may, this possibility would change nothing in the practical indeterminism of collision processes, since one cannot give the values of the phases; moreover, they must lead to the same formulas as the “phase-less” theory that is proposed here.

I would like to believe that the laws of motion of light quanta can be treated in a completely analogous way (⁵). However, as in the basic problem of the free radiation, one would not have a temporally-periodic process, but a deflection process, and thus, not

$$\lambda = \frac{2\pi}{k} = \frac{h}{\sqrt{2\mu W}}.$$

For 300 volt radiation, one has roughly $\lambda = 7 \cdot 10^{-9}$, and thus waves of atomic dimensions.

(¹) See K. Schwarzschild, Sitzungsber. d. Kgl. Bayer. Akad. d. Wiss. (1901), 293; G. Mie, Ann. d. Phys. 25 (1908), 377; P. Debye, Ann. d. Phys. 30 (1909), 57.

(²) C. Ramsauer, Ann. d. Phys. 64 (1921), 513; 72 (1923), 345. For further literature see Ergebnisse der exakten Naturwissenschaftler, 3 Bd. (Berlin, J. Springer, 1924), the article of R. Minkowski and H. Sponer, pp. 67.

(³) Davisson and Kunsman, Phys. Rev. 22 (1923), 243.

(⁴) Dymond, Nature. (To appear; I am grateful for a glimpse of that work in a letter that Dymond sent to J. Franck.)

(⁵) The complications that have been found up to now regarding the introduction of “ghost fields” into optics seem to me to be based, in part, upon the tacit assumption that the center of the wave and the particle that it determines are at the same place. However, from the Compton effect, this is certainly not the case, and indeed will never be true, in general.

Born – Quantum mechanics of collision processes.

25

a boundary-value problem, but an initial-value problem for the coupled wave equations for the Schrödinger ψ-quantity and the electromagnetic field. Finding the law of this coupling is certainly one of the most pressing problems; as I am aware, it has been addressed in several places (¹). Once that law has been formulated, it will perhaps be possible to devise a rational theory of the lifetimes of states, the transition probabilities for radiation processes, and the damping and line widths.

(¹) See, e.g., the soon-to-appear treatise of O. Klein, Zeit. Phys. 37 (1926), 895.
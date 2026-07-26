Royal Society Publishing
Informing the science
of the future

# The Fundamental Equations of Quantum Mechanics

Author(s): P. A. M. Dirac

Source: Proceedings of the Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character, Vol. 109, No. 752 (Dec. 1, 1925), pp. 642-653

Published by: The Royal Society

Stable URL: http://www.jstor.org/stable/94441

Accessed: 03/02/2011 04:27

Your use of the JSTOR archive indicates your acceptance of JSTOR's Terms and Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp. JSTOR's Terms and Conditions of Use provides, in part, that unless you have obtained prior permission, you may not download an entire issue of a journal or multiple copies of articles, and you may use content in the JSTOR archive only for your personal, non-commercial use.

Please contact the publisher regarding any further use of this work. Publisher contact information may be obtained at http://www.jstor.org/action/showPublisher?publisherCode=rs1.

Each copy of any part of a JSTOR transmission must contain the same copyright notice that appears on the screen or printed page of such transmission.

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

![img-0.jpeg](img-0.jpeg)

The Royal Society is collaborating with JSTOR to digitize, preserve and extend access to Proceedings of the Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character.

http://www.jstor.org

642

# *The Fundamental Equations of Quantum Mechanics.*

By P. A. M. DIRAC, 1851 Exhibition Senior Research Student, St. John's College, Cambridge.

(Communicated by R. H. Fowler, F.R.S.—Received November 7th, 1925.)

# § 1. *Introduction.*

It is well known that the experimental facts of atomic physics necessitate a departure from the classical theory of electrodynamics in the description of atomic phenomena. This departure takes the form, in Bohr's theory, of the special assumptions of the existence of stationary states of an atom, in which it does not radiate, and of certain rules, called quantum conditions, which fix the stationary states and the frequencies of the radiation emitted during transitions between them. These assumptions are quite foreign to the classical theory, but have been very successful in the interpretation of a restricted region of atomic phenomena. The only way in which the classical theory is used is through the assumption that the classical laws hold for the description of the motion in the stationary states, although they fail completely during transitions, and the assumption, called the Correspondence Principle, that the classical theory gives the right results in the limiting case when the action per cycle of the system is large compared to Planck's constant $h$, and in certain other special cases.

In a recent paper* Heisenberg puts forward a new theory, which suggests that it is not the equations of classical mechanics that are in any way at fault, but that the mathematical operations by which physical results are deduced from them require modification. *All* the information supplied by the classical theory can thus be made use of in the new theory.

# § 2. *Quantum Algebra.*

Consider a multiply periodic non-degenerate dynamical system of $u$ degrees of freedom, defined by equations connecting the co-ordinates and their time differential coefficients. We may solve the problem on the classical theory in the following way. Assume that each of the co-ordinates $x$ can be expanded in the form of a multiple Fourier series in the time $t$, thus,

$$\begin{aligned} x &= \sum_{\alpha_1 \dots \alpha_n} x(\alpha_1 \alpha_2 \dots \alpha_n) \exp. i(\alpha_1 \omega_1 + \alpha_2 \omega_2 + \dots + \alpha_n \omega_n) t \\ &= \sum_{\alpha} x_n \exp. i(\alpha \omega) t, \end{aligned}$$

* Heisenberg, 'Zeits. f. Phys.,' vol. 33, p. 879 (1925).

*Fundamental Equations of Quantum Mechanics.* 643

say, for brevity. Substitute these values in the equations of motion, and equate the coefficients on either side of each harmonic term. The equations obtained in this way (which we shall call the A equations) will determine each of the amplitudes $x_a$ and frequencies $(\alpha\omega)$, (the frequencies being measured in radians per unit time). The solution will not be unique. There will be a $u$-fold infinity of solutions, which may be labelled by taking the amplitudes and frequencies to be functions of $u$ constants $\kappa_1 \dots \kappa_u$. Each $x_a$ and $(\alpha\omega)$ is now a function of two sets of numbers, the $\alpha$'s and the $\kappa$'s, and may be written $x_{a\kappa}, (\alpha\omega)_\kappa$.

In the quantum solution of the problem, according to Heisenberg, we still assume that each co-ordinate can be represented by harmonic components of the form $\exp. i\omega t$, the amplitude and frequency of each depending on two sets of numbers $n_1 \dots n_u$ and $m_1 \dots m_u$, in this case all integers, and being written $x(nm)$, $\omega(nm)$. The differences $n_r - m_r$ correspond to the previous $\alpha_r$, but neither the $n$'s nor any functions of the $n$'s and $m$'s play the part of the previous $\kappa$'s in pointing out to which solution each particular harmonic component belongs. We cannot, for instance, take together all the components for which the $n$'s have a given set of values, and say that these by themselves form a single complete solution of the equations of motion. The quantum solutions are all interlocked, and must be considered as a single whole. The effect of this mathematically is that, while on the classical theory each of the A equations is a relation between amplitudes and frequencies having one particular set of $\kappa$'s, the amplitudes and frequencies occurring in a quantum A equation do not have one particular set of values for the $n$'s, or for any functions of the $n$'s and $m$'s, but have their $n$'s and $m$'s related in a special way, which will appear later.

On the classical theory we have the obvious relation

$$(\alpha\omega)_\kappa + (\beta\omega)_\kappa = (\alpha + \beta, \omega)_\kappa.$$

Following Heisenberg, we assume that the corresponding relation on the quantum theory is

$$\omega(n, n - \alpha) + \omega(n - \alpha, n - \alpha - \beta) = \omega(n, n - \alpha - \beta)$$

or

$$\omega(nm) + \omega(mk) = \omega(nk). \quad (1)$$

This means that $\omega(nm)$ is of the form $\Omega(n) - \Omega(m)$, the $\Omega$'s being frequency levels. On Bohr's theory these would be $2\pi/h$ times the energy levels, but we do not need to assume this.

2 x 2

644

P. A. M. Dirac.

On the classical theory we can multiply two harmonic components related to the same set of $\kappa$'s, as follows :—

$$a_{\alpha\kappa} \exp. i (\alpha\omega)_\kappa t \cdot b_{\beta\kappa} \exp. i (\beta\omega)_\kappa t = (ab)_{\alpha+\beta,\kappa} \exp. i (\alpha + \beta, \omega)_\kappa t$$

where

$$(ab)_{\alpha+\beta,\kappa} = a_{\alpha\kappa} b_{\beta\kappa}.$$

In a corresponding manner on the quantum theory we can multiply an $(nm)$ and an $(mk)$ component

$$a (nm) \exp. i\omega (nm) t \cdot b (mk) \exp. i\omega (mk) t = ab (nk) \exp. i\omega (nk) t$$

where

$$ab (nk) = a (nm) b (mk).$$

We are thus led to consider the product of the amplitudes of an $(nm)$ and an $(mk)$ component as an $(nk)$ amplitude. This, together with the rule that only amplitudes related to the same pair of sets of numbers can occur added together in an A equation, replaces the classical rule that all amplitudes occurring in an A equation have the same set of $\kappa$'s.

We are now in a position to perform the ordinary algebraic operations on quantum variables. The sum of $x$ and $y$ is determined by the equations

$$\{x + y\} (nm) = x (nm) + y (nm)$$

and the product by

$$xy (nm)_\kappa = \Sigma_k x(nk) y (km) \quad (2)$$

similar to the classical product

$$(xy)_{n\kappa} = \Sigma_r x_{r\kappa} y_{n-r,\kappa}.$$

An important difference now occurs between the two algebras. In general

$$xy (nm) \neq yx (nm)$$

and quantum multiplication is not commutative, although, as is easily verified, it is associative and distributive. The quantity with components $xy (nm)$ defined by (2) we shall call the Heisenberg product of $x$ and $y$, and shall write simply as $xy$. Whenever two quantum quantities occur multiplied together, the Heisenberg product will be understood. Ordinary multiplication is, of course, implied in the products of amplitudes and frequencies and other quantities that are related to sets of $n$'s which are explicitly stated.

The reciprocal of a quantum quantity $x$ may be defined by either of the relations

$$1/x \cdot x = 1 \quad \text{or} \quad x \cdot 1/x = 1. \quad (3)$$

These two equations are equivalent, since if we multiply both sides of the

*Fundamental Equations of Quantum Mechanics.* 645

former by $x$ in front and divide by $x$ behind we get the latter. In a similar way the square root of $x$ may be defined by

$$\sqrt{x} \cdot \sqrt{x} = x. \quad (4)$$

It is not obvious that there always should be solutions to (3) and (4). In particular, one may have to introduce sub-harmonics, *i.e.*, new intermediate frequency levels, in order to express $\sqrt{x}$. One may evade these difficulties by rationalising and multiplying up each equation before interpreting it on the quantum theory and obtaining the A equations from it.

We are now able to take over each of the equations of motion of the system into the quantum theory provided we can decide the correct order of the quantities in each of the products. Any equation deducible from the equations of motion by algebraic processes not involving the interchange of the factors of a product, and by differentiation and integration with respect to $t$, may also be taken over into the quantum theory. In particular, the energy equation may be thus taken over.

The equations of motion do not suffice to solve the quantum problem. On the classical theory the equations of motion do not determine the $x_{\alpha\epsilon}$, $(\alpha\omega)_\epsilon$ as functions of the $\kappa$'s until we assume something about the $\kappa$'s which serves to define them. We could, if we liked, complete the solution by choosing the $\kappa$'s such that $\partial E/\partial \kappa_r = \omega_r/2\pi$, where $E$ is the energy of the system, which would make the $\kappa_r$ equal the action variables $J_r$. There must be corresponding equations on the quantum theory, and these constitute the quantum conditions.

### § 3. *Quantum Differentiation.*

Up to the present the only differentiation that we have considered on the quantum theory is that with respect to the time $t$. We shall now determine the form of the most general quantum operation $d/dv$ that satisfies the laws

$$\frac{d}{dv}(x + y) = \frac{d}{dv}x + \frac{d}{dv}y, \quad (I)$$

and

$$\frac{d}{dv}(xy) = \frac{d}{dv}x \cdot y + x \cdot \frac{d}{dv}y. \quad (II)$$

(Note that the order of $x$ and $y$ is preserved in the last equation.)

The first of these laws requires that the amplitudes of the components of $dx/dv$ shall be linear functions of those of $x$, *i.e.*,

$$dx/dv(nm) = \sum_{nm} a(nm; n'm') x(n'm'). \quad (5)$$

646

P. A. M. Dirac.

There is one coefficient $a(nm; n'm')$ for any four sets of integral values for the $n$'s, $m$'s, $n'$'s and $m'$'s. The second law imposes conditions on the $a$'s. Substitute for the differential coefficients in II their values according to (5) and equate the $(nm)$ components on either side. The result is

$$\begin{aligned} \Sigma_{nm'k} a(nm; n'm') x(n'k) y(km') &= \Sigma_{kn'k'} a(nk; n'k') x(n'k') y(km) \\ &+ \Sigma_{kk'm} x(nk) a(km; k'm') y(k'm'). \end{aligned}$$

This must be true for all values of the amplitudes of $x$ and $y$, so that we can equate the coefficients of $x(n'k) y(k'm')$ on either side. Using the symbol $\delta_{mn}$ to have the value unity when $m=n$ (i.e., when each $m_r=n_r$) and zero when $m \neq n$, we get

$$\delta_{kk'} a(nm; n'm') = \delta_{mm'} a(nk'; n'k) + \delta_{nn'} a(km; k'm').$$

To proceed further, we have to consider separately the various cases of equality and inequality between the $kk'$, $mm'$ and $nn'$.

Take first the case when $k=k'$, $m \neq m'$, $n \neq n'$. This gives

$$a(nm; n'm') = 0.$$

Hence all the $a(nm; n'm')$ vanish except those for which either $n=n'$ or $m=m'$ (or both). The cases $k \neq k'$, $m=m'$, $n \neq n'$ and $k \neq k'$, $m \neq m'$, $n=n'$ do not give us anything new. Now take the case $k=k'$, $m=m'$, $n \neq n'$. This gives

$$a(nm; n'm) = a(nk; n'k).$$

Hence $a(nm; n'm)$ is independent of $m$ provided $n \neq n'$. Similarly, the case $k=k'$, $m \neq m'$, $n=n'$ tells us that $a(nm; nm')$ is independent of $n$ provided $m \neq m'$. The case $k \neq k'$, $m=m'$, $n=n'$ now gives

$$a(nk'; nk) + a(km; k'm) = 0.$$

We can sum up these results by putting

$$a(nk'; nk) = a(kk') = -a(km; k'm), \quad (6)$$

provided $k \neq k'$. The two-index symbol $a(kk')$ depends, of course, only on the two sets of integers $k$ and $k'$. The only remaining case is $k=k'$, $m=m'$, $n=n'$, which gives

$$a(nm; nm) = a(nk; nk) + a(km; km).$$

This means we can put

$$a(nm; nm) = a(mm) - a(nn). \quad (7)$$

Equation (7) completes equation (6) by defining $a(kk')$ when $k=k'$.

Fundamental Equations of Quantum Mechanics.

647

Equation (5) now reduces to

$$\begin{array}{l} dx/dv(nm) = \Sigma_{m' \neq m} a(nm; nm') x(nm') + \Sigma_{n' \neq n} a(nm; n'm) x(n'm) \\ \hspace{2.5em} + a(nm; nm) x(nm) \\ \hspace{2.5em} = \Sigma_{m' \neq m} a(m'm) x(nm') - \Sigma_{n' \neq n} a(nn') x(n'm) \\ \hspace{2.5em} + \{a(mm) - a(nn)\} x(nm) \\ \hspace{2.5em} = \Sigma_k \{x(nk) a(km) - a(nk) x(km)\}. \end{array}$$

Hence

$$dx/dv = xa - ax. \tag{8}$$

Thus the most general operation satisfying the laws I and II that one can perform upon a quantum variable is that of taking the difference of its Heisenberg products with some other quantum variable. It is easily seen that one cannot in general change the order of differentiations, i.e.,

$$\frac{d^2x}{du dv} \neq \frac{d^2x}{dv du}.$$

As an example in quantum differentiation we may take the case when (a) is a constant, so that a (nm) = 0 except when n = m. We get

$$dx/dv(nm) = x(nm) a(mm) - a(nn) x(nm).$$

In particular, if ia (mm) = Ω (m), the frequency level previously introduced, we have

$$dx/dv(nm) = i\omega(nm) x(nm),$$

and our differentiation with respect to v becomes ordinary differentiation with respect to t.

# § 4. The Quantum Conditions.

We shall now consider to what the expression (xy - yx) corresponds on the classical theory. To do this we suppose that x (n, n - α) varies only slowly with the n's, the n's being large numbers and the α's small ones, so that we can put

$$x(n, n - \alpha) = x_{\alpha\kappa}$$

where κ_r = n_r h or (n_r + α_r) h, these being practically equivalent. We now have

$$\begin{array}{l} x(n, n - \alpha) y(n - \alpha, n - \alpha - \beta) - y(n, n - \beta) x(n - \beta, n - \alpha - \beta) \\ \hspace{2.5em} = \{x(n, n - \alpha) - x(n - \beta, n - \beta - \alpha)\} y(n - \alpha, n - \alpha - \beta) \\ \hspace{2.5em} - \{y(n, n - \beta) - y(n - \alpha, n - \alpha - \beta)\} x(n - \beta, n - \alpha - \beta). \\ \hspace{2.5em} = h\Sigma_r \left\{ \beta_r \frac{\partial x_{\alpha\kappa}}{\partial \kappa_r} y_{\beta\kappa} - \alpha_r \frac{\partial y_{\beta\kappa}}{\partial \kappa_r} x_{\alpha\kappa} \right\}. \tag{9} \end{array}$$

648

P. A. M. Dirac.

Now

$$2\pi i \beta_r y_\beta \exp. i (\beta \omega) t = \frac{\partial}{\partial w_r} \{y_\beta \exp. i (\beta \omega) t$$

where the $w_r$ are the angle variables, equal to $\omega_r t / 2\pi$. Hence the $(nm)$ component of $(xy - yx)$ corresponds on the classical theory to

$$\frac{ih}{2\pi} \Sigma_{\alpha+\beta=n-m} \Sigma_r \left\{ \frac{\partial}{\partial \kappa_r} \{x_\alpha \exp. i (\alpha \omega) t\} \frac{\partial}{\partial w_r} \{y_\beta \exp. i (\beta \omega) t\} - \frac{\partial}{\partial \kappa_r} \{y_\beta \exp. i (\beta \omega) t\} \frac{\partial}{\partial w_r} \{x_\alpha \exp. i (\alpha \omega) t\} \right\}$$

or $(xy - yx)$ itself corresponds to

$$- \frac{ih}{2\pi} \Sigma_r \left\{ \frac{\partial x}{\partial \kappa_r} \frac{\partial y}{\partial w_r} - \frac{\partial y}{\partial \kappa_r} \frac{\partial x}{\partial w_r} \right\}.$$

If we make the $\kappa_r$ equal the action variables $J_r$, this becomes $ih/2\pi$ times the Poisson (or Jacobi) bracket expression

$$[x, y] = \Sigma_r \left\{ \frac{\partial x}{\partial w_r} \frac{\partial y}{\partial J_r} - \frac{\partial y}{\partial w_r} \frac{\partial x}{\partial J_r} \right\} = \Sigma_r \left\{ \frac{\partial x}{\partial q_r} \frac{\partial y}{\partial p_r} - \frac{\partial y}{\partial q_r} \frac{\partial x}{\partial p_r} \right\}$$

where the $p$'s and $q$'s are any set of canonical variables of the system.

The elementary Poisson bracket expressions for various combinations of the $p$'s and $q$'s are

$$\left. \begin{aligned} [q_r, q_s] &= 0, & [p_r, p_s] &= 0, \\ [q_r, p_s] &= \delta_{rs} = 0 & (r \neq s) \\ &= 1. & (r = s) \end{aligned} \right\} \quad (10)$$

The general bracket expressions satisfy the laws I and II, which now read

$$\begin{aligned} [x, z] + [y, z] &= [x + y, z], & \text{IA} \\ [xy, z] &= [x, z] y + x [y, z]. & \text{IIA} \end{aligned}$$

By means of these laws, together with $[x, y] = - [y, x]$, if $x$ and $y$ are given as algebraic functions of the $p_r$ and $q_r$, $[x, y]$ can be expressed in terms of the $[q_r, q_s]$, $[p_r, p_s]$ and $[q_r, p_s]$, and thus evaluated, without using the commutative law of multiplication (except in so far as it is used implicitly on account of the proof of IIA requiring it). The bracket expression $[x, y]$ thus has a meaning on the quantum theory when $x$ and $y$ are quantum variables, if we take the elementary bracket expressions to be still given by (10).

We make the fundamental assumption that the *difference between the Heisenberg products of two quantum quantities* is equal to $ih/2\pi$ times their Poisson bracket expression. In symbols,

$$xy - yx = ih/2\pi \cdot [x, y]. \quad (11)$$

Fundamental Equations of Quantum Mechanics.

649

We have seen that this is equivalent, in the limiting case of the classical theory, to taking the arbitrary quantities $\kappa_r$ that label a solution equal to the $J_r$, and it seems reasonable to take (11) as constituting the general quantum conditions.

It is not obvious that all the information supplied by equation (11) is consistent. Owing to the fact that the quantities on either side of (11) satisfy the same laws I and II or IA and IIA, the only independent conditions given by (11) are those for which $x$ and $y$ are $p$'s or $q$'s, namely

$$\left. \begin{aligned} q_r q_s - q_s q_r &= 0 \\ p_r p_s - p_s p_r &= 0 \\ q_r p_s - p_s q_r &= \delta_{rs} ih/2\pi \end{aligned} \right\} \quad (12)$$

If the only grounds for believing that the equations (12) were consistent with each other and with the equations of motion were that they are known to be consistent in the limit when $h \rightarrow 0$, the case would not be very strong, since one might be able to deduce from them the inconsistency that $h = 0$, which would not be an inconsistency in the limit. There is much stronger evidence than this, however, owing to the fact that the classical operations obey the same laws as the quantum ones, so that if, by applying the quantum operations, one can get an inconsistency, by applying the classical operations in the same way one must also get an inconsistency. If a series of classical operations leads to the equation $0 = 0$, the corresponding series of quantum operations must also lead to the equation $0 = 0$, and not to $h = 0$, since there is no way of obtaining a quantity that does not vanish by a quantum operation with quantum variables such that the corresponding classical operation with the corresponding classical variables gives a quantity that does vanish. The possibility mentioned above of deducing by quantum operations the inconsistency $h = 0$ thus cannot occur. *The correspondence between the quantum and classical theories lies not so much in the limiting agreement when $h \rightarrow 0$ as in the fact that the mathematical operations on the two theories obey in many cases the same laws.*

For a system of one degree of freedom, if we take $p = m\dot{q}$, the only quantum condition is

$$2\pi m (q\dot{q} - \dot{q}q) = ih.$$

Equating the constant part of the left-hand side to $ih$, we get

$$4\pi m \Sigma_k q(nk) q(kn) \omega(kn) = h.$$

650

P. A. M. Dirac.

This is equivalent to Heisenberg's quantum condition.* By equating the remaining components of the left-hand side to zero we get further relations not given by Heisenberg's theory.

The quantum conditions (12) get over, in many cases, the difficulties concerning the order in which quantities occurring in products in the equations of motion are to be taken. The order does not matter except when a $p_r$ and $q_r$ are multiplied together, and this never occurs in a system describable by a potential energy function that depends only on the $q$'s, and a kinetic energy function that depends only on the $p$'s.

It may be pointed out that the classical theory quantity occurring in Kramers' and Heisenberg's theory of scattering by atoms† has components which are of the form (8) (with $\kappa_r = J_r$), and which are interpreted on the quantum theory in a manner in agreement with the present theory. No classical expression involving differential coefficients can be interpreted on the quantum theory unless it can be put into this form.

### § 5. Properties of the Quantum Poisson Bracket Expressions.

In this section we shall deduce certain results that are independent of the assumption of the quantum conditions (11) or (12).

The Poisson bracket expressions satisfy on the classical theory the identity

$$[x, y, z] \equiv [[x, y]; z] + [[y, z], x] + [[z, x], y] = 0. \quad (13)$$

On the quantum theory this result is obviously true when $x$, $y$ and $z$ are $p$'s or $q$'s. Also, from IA and IIA

$$[x_1 + x_2, y, z] = [x_1, y, z] + [x_2, y, z]$$
$$[x_1, x_2, y, z] = x_1 [x_2, y, z] + [x_1, y, z] x_2.$$

Hence the result must still be true on the quantum theory when $x$, $y$ and $z$ are expressible in any way as sums and products of $p$'s and $q$'s, so that it must be generally true. Note that the identity corresponding to (13) when the Poisson bracket expressions are replaced by the differences of the Heisenberg products $(xy - yx)$ is obviously true, so that there is no inconsistency with equation (11).

If H is the Hamiltonian function of the system, the equations of motion may be written classically

$$\dot{p}_r = [p_r, \mathbf{H}] \quad \dot{q}_r = [q_r, \mathbf{H}].$$

* Heisenberg, loc. cit. equation (16).

† Kramers and Heisenberg, 'Zeits. f. Phys.,' vol. 31, p. 681, equation (18), (1925).

*Fundamental Equations of Quantum Mechanics.* 651

These equations will be true on the quantum theory for systems for which the orders of the factors of products occurring in the equations of motion are unimportant. They may be taken to be true for systems for which these orders are important if one can decide upon the orders of the factors in H. From laws IA and IIA it follows that

$$\dot{x} = [x, H] \quad (14)$$

on the quantum theory for any $x$.

If A is an integral of the equations of motion on the quantum theory, then

$$[A, H] = 0.$$

The action variables $J_r$ must, of course, satisfy this condition. If $A_1$ and $A_2$ are two such integrals, then, by a simple application of (13), it follows that

$$[A_1, A_2] = \text{const.}$$

as on the classical theory.

The conditions on the classical theory that a set of variables $P_r, Q_r$ shall be canonical are

$$[Q_r, Q_s] = 0 \quad [P_r, P_s] = 0$$

$$[Q_r, P_s] = \delta_{rs}.$$

These equations may be taken over into the quantum theory as the conditions for the quantum variables $P_r, Q_r$ to be canonical.

On the classical theory we can introduce the set of canonical variables $\xi_r, \eta_r$ related to the uniformising variables $J_r, w_r$, by

$$\xi_r = (2\pi)^{-\frac{1}{2}} J_r^{\frac{1}{2}} \exp. 2\pi i w_r, \quad \eta_r = -i (2\pi)^{-\frac{1}{2}} J_r^{\frac{1}{2}} \exp. -2\pi i w_r.$$

Presumably there will be a corresponding set of canonical variables on the quantum theory, each containing only one kind of component, so that $\xi_r(nm) = 0$ except when $m_r = n_r - 1$ and $m_s = n_s (s \neq r)$, and $\eta_r(nm) = 0$ except when $m_r = n_r + 1$ and $m_s = n_s (s \neq r)$. One may consider the existence of such variables as the condition for the system to be multiply periodic on the quantum theory. The components of the Heisenberg products of $\xi_r$ and $\eta_r$ satisfy the relation

$$\xi_r \eta_r(nn) = \xi_r(nm) \eta_r(mn) = \eta_r(mn) \xi_r(nm) = \eta_r \xi_r(mm) \quad (15)$$

where the $m$'s are related to the $n$'s by the formulae $m_r = n_r - 1$, $m_s = n_s (s \neq r)$.

The classical $\xi$'s and $\eta$'s satisfy $\xi_r \eta_r = -i/2\pi \cdot J_r$. This relation does not necessarily hold between the quantum $\xi$'s and $\eta$'s. The quantum relation

652

P. A. M. Dirac.

may, for instance, be $\eta_r\xi_r = -i/2\pi \cdot J_r$, or $\frac{1}{2}(\xi_r\eta_r + \eta_r\xi_r) = -i/2\pi \cdot J_r$. A detailed investigation of any particular dynamical system is necessary in order to decide what it is. In the event of the last relation being true, we can introduce the set of canonical variables $\xi_r'$, $\eta_r'$ defined by

$$\xi_r' = (\xi_r + i\eta_r)/\sqrt{2}, \quad \eta_r' = (i\xi_r + \eta_r)/\sqrt{2},$$

and shall then have

$$J_r = \pi (\xi_r'^2 + \eta_r'^2).$$

This is the case that actually occurs for the harmonic oscillator. In general $J_r$ is not necessarily even a rational function of the $\xi_r$ and $\eta_r$, an example of this being the rigid rotator considered by Heisenberg.

### § 6. *The Stationary States.*

A quantity $C$, that does not vary with the time, has all its $(nm)$ components zero, except those for which $n = m$. It thus becomes convenient to suppose each set of $n$'s to be associated with a definite state of the atom, as on Bohr's theory, so that each $C(nn)$ belongs to a certain state in precisely the same way in which *every* quantity occurring in the classical theory belongs to a certain configuration. The components of a varying quantum quantity are so interlocked, however, that it is impossible to associate the sum of certain of them with a given state.

A relation between quantum quantities reduces, when all the quantities are constants, to a relation between $C(nn)$'s belonging to a definite stationary state $n$. This relation will be the same as the classical theory relation, on the assumption that the classical laws hold for the description of the stationary states; in particular, the energy will be the same function of the $J$'s as on the classical theory. We have here a justification for Bohr's assumption of the mechanical nature of the stationary states. It should be noted though, that the variable quantities associated with a stationary state on Bohr's theory, the amplitudes and frequencies of orbital motion, have no physical meaning and are of no mathematical importance.

If we apply the fundamental equation (11) to the quantities $x$ and $H$ we get, with the help of (14),

$$x(nm)H(mm) - H(nn)x(nm) = ih/2\pi \cdot \dot{x}(nm) = -h/2\pi \cdot \omega(nm)x(nm),$$

or $$H(nn) - H(mm) = h/2\pi \cdot \omega(nm).$$

This is just Bohr's relation connecting the frequencies with the energy differences.

*Fundamental Equations of Quantum Mechanics.* 653

The quantum condition (11) applied to the previously introduced canonical variables $\xi_r, \eta_r$ gives

$$\xi_r \eta_r (nn) - \eta_r \xi_r (nn) = ih/2\pi \cdot [\xi_r, \eta_r] = ih/2\pi.$$

This equation combined with (15) shows that

$$\xi_r \eta_r (nn) = - n_r ih/2\pi + \text{const.}$$

It is known physically that an atom has a normal state in which it does not radiate. This is taken account of in the theory by Heisenberg's assumption that all the amplitudes $C(nm)$ having a negative $n_r$ or $m_r$ vanish, or rather do not exist, if we take the normal state to be the one for which every $n_r$ is zero. This makes $\xi_r \eta_r (nn) = 0$ when $n_r = 0$ on account of equation (15). Hence in general

$$\xi_r \eta_r (nn) = - n_r ih/2\pi.$$

If $\xi_r \eta_r = - i/2\pi \cdot J_r$, then $J_r = n_r h$. This is just the ordinary rule for quantising the stationary states, so that in this case the frequencies of the system are the same as those given by Bohr's theory. If $\frac{1}{2}(\xi_r \eta_r + \eta_r \xi_r) = - i/2\pi \cdot J_r$, then $J_r = (n_r + \frac{1}{2})h$. Hence in general in this case, half quantum numbers would have to be used to give the correct frequencies by Bohr's theory.*

Up to the present we have considered only multiply periodic systems. There does not seem to be any reason, however, why the fundamental equations (11) and (12) should not apply as well to non-periodic systems, of which none of the constituent particles go off to infinity, such as a general atom. One would not expect the stationary states of such a system to classify, except perhaps when there are pronounced periodic motions, and so one would have to assign a single number $n$ to each stationary state according to an arbitrary plan. Our quantum variables would still have harmonic components, each related to two $n$'s, and Heisenberg multiplication could be carried out exactly as before. There would thus be no ambiguity in the interpretation of equations (12) or of the equations of motion.

I would like to express my thanks to Mr. R. H. Fowler, F.R.S., for many valuable suggestions in the writing of this paper.

* In the special case of the Planck oscillator, since the energy is a linear function of $J$, the frequency would come right in any case.
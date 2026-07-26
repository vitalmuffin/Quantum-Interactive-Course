# On the quantum reinterpretation of kinematical and mechanical relationships

Werner Heisenberg

Institute of Theoretical Physics, Göttingen

*submitted July 29th, 1925*

Translation: December 2014 by Luca Doria

**Abstract** In this work we will try to obtain the basis for a quantum mechanics theory, which is based uniquely on relationships between in principle observable quantities.

## Introduction

It is known that against the formal rules of the quantum theory used for the calculation of the observable quantities (for example the energy levels of the Hydrogen atom) the serious objection can be raised that 1) those calculational rules contain as essential components relationships between quantities that seemingly in principle cannot be observed (like, for example, the electron position and period) and 2) also those rules apparently lack every clear physical basis unless one does not want to remain attached to the hope that those until now unobserved quantities will be made experimentally accessible in the future. This hope might be regarded as justified if the above-mentioned rules were internally consistent and applicable to a clearly defined range of quantum theoretical problems.

Anyway, experience shows that 1) only the Hydrogen atom and its Stark effect fit into those formal rules of quantum theory, 2) already in the "crossed fields" problem (Hydrogen atom in electric and magnetic fields in different directions) fundamental difficulties arise, 3) the reaction of atoms to periodically varying fields surely cannot be described by the mentioned rules and 4)

1

finally an expansion of the quantum rules for the treatment of many-electrons atoms has been proved unfeasible.

It became customary to characterize the failure of the quantum rules (that were already essentially characterized through the application of classical mechanics) as a deviation from classical mechanics. However, this description can hardly be viewed as logical when one considers that already the Einstein-Bohr frequency condition represents such a complete departure from classical mechanics or better, from the point of view the wave theory, from the underlying kinematics of this mechanics, that it is absolutely not possible even for the simplest quantum theoretical problem to maintain the validity of classical mechanics.

In this situation, it is advisable to completely give up any hope about the observation of hitherto unobserved quantities (like the electrons' position and period) and at the same time acknowledge that 1) the partial agreement with experience of the mentioned quantum rules is more or less an accident and 2) to try to construct a theory of quantum mechanics in which only relationships among observable quantities occur.

As first, most important approaches to such a theory of quantum mechanics, one can refer to the dispersion theory of Kreamer (cit 1) and following works based on it (cit 2).

In the following, we shall try to present some new quantum mechanical relationships and apply them to the detailed treatment of some special problems. We shall limit ourselves to problems with one degree of freedom.

### Article 1

In the classical theory, the radiation of a moving electron (in the wave-zone $E \sim H \sim 1/r$) is not completely given by the expressions

$$\vec{E} = \frac{e}{r^3 c^2} (\vec{r} \times (\vec{r} \times \vec{v})) \tag{1}$$

$$\vec{H} = \frac{e}{r^2 c^2} (\vec{v} \times \vec{r}) \tag{2}$$

but we have other terms at the next order, e.g. of the form

$$\frac{e}{r c^3} (\vec{v} \times \vec{r}) \tag{3}$$

2

that we can denote as quadrupole radiation. and at the next higher order we have terms of the form

$$\frac{e}{r c^4}(\vec{v} \times \vec{v}^2) \tag{4}$$

and in this way the approximation can be carried out at any desired order.

(In the previous expressions, $\vec{E}$ and $\vec{H}$ are the fields strengths at a point, e is the electron charge, $\vec{r}$ is the distance of the electron from the field point, $\vec{v}$ the electron velocity). One can ask himself how the higher terms look like in the quantum theory.

Since in the classical theory the higher orders can be easily calculated when the motion of the electron or its Fourier representation are given respectively, one can expect the same in the quantum theory. This question does not have to do with electrodynamics, but this is - and this seems particularly important to us - of pure kinematical nature. We can pose this question as follows: given instead of the classical quantity x(t) a quantum theoretical one, which quantum theoretical quantity enters in the place of $x(t)^2$?

Before being able to answer this question, we have to remember that in the quantum theory it was not possible to assign to the electron a point in space as a function of time through observable quantities. However, surely also in the quantum theory one can assign to the electron an emitted radiation. First, this radiation will be described by frequencies which quantum theoretically arise as function of two variables in the form:

$$\nu(n, n - \alpha) = \frac{1}{h}\{E(n) - E(n - \alpha)\} \tag{5}$$

and in the classical theory in the form:

$$\nu(n, \alpha) = \alpha \frac{1}{h} \frac{dE}{dn} \tag{6}$$

(From here onwards, we define $nh = J$ where $J$ is one of the canonical constants). As characteristic for the comparisons of the classical mechanics to the quantum theory, with regard to the frequencies one can write the "combination relations"

Classically:

$$\nu(n, \alpha) + \nu(n, \beta) = \nu(n, \alpha + \beta) \tag{7}$$

3

*Quantum theoretically:*

$$\nu(n, n - \alpha) + \nu(n - \alpha, n - \alpha - \beta) = \nu(n, n - \alpha - \beta) \quad (8)$$

$$\nu(n - \beta, n - \alpha - \beta) + \nu(n, n - \beta) = \nu(n, n - \alpha - \beta) \quad (9)$$

Secondly, besides the frequencies, the amplitudes are necessary for the description of radiation. The amplitudes can be written as complex vectors (each with six independent components) and determine polarization and phase. They are also function of the two variables $n$ and $\alpha$ so that the corresponding part of the radiation will be represented with

*Quantum theoretically:*

$$\Re\{\vec{X}(n, n - \alpha)e^{i\omega(n, n - \alpha)t}\} \quad (10)$$

*Classically:*

$$\Re\{\vec{X}_\alpha(n)e^{i\omega(n)\alpha t}\} \quad (11)$$

First of all, the phase (contained in $\vec{X}$) appears to have no meaning in the quantum theory since in this theory the frequencies are not in general commensurable with their harmonics. However, we will immediately see that also in the quantum theory the phase has a precise meaning which has an analog in the classical theory. Let us consider now a particular quantity $x(t)$ in the classical theory such that it can be regarded as represented by the totality of quantities of the form

$$\vec{A}_\alpha(n)e^{i\omega(n)\alpha t} \quad (12)$$

which depending on the motion being periodic or not, represents $x(t)$ with a sum or an integral

$$x(t) = \sum_{\alpha=-\infty}^{+\infty} \vec{X}_\alpha(n)e^{i\omega(n)\alpha t} \quad (13)$$

$$\text{or} \quad x(t) = \int_{-\infty}^{+\infty} \vec{X}_\alpha(n)e^{i\omega(n)\alpha t} d\alpha \quad (14)$$

A similar combination of the corresponding quantum-theoretical quantities seems to be impossible in a unique manner and therefore not meaningful in view of the equal weight of the quantities $n$ and $n - \alpha$. However, one may readily regard the ensemble of quantities

$$\vec{X}(n, n - \alpha)e^{i\omega(n, n - \alpha)t} \quad (15)$$

4

as a representation of the quantity x(t) and then try to answer the question posed before: how would the quantity $x(t)^2$ be represented? Classically, the answer is obviously

$$Y_\beta(n)e^{i\omega(n)\beta t} = \sum_{\alpha=-\infty}^{+\infty} \vec{X}_\alpha \vec{X}_{\beta-\alpha} e^{i\omega(n)(\alpha+\beta-\alpha)t} \tag{16}$$

$$\text{or} \quad = \int_{-\infty}^{+\infty} \vec{X}_\alpha \vec{X}_{\beta-\alpha} e^{i\omega(n)(\alpha+\beta-\alpha)t} d\alpha \tag{17}$$

so that

$$x(t)^2 = \sum_{\beta=-\infty}^{+\infty} \vec{Y}_\beta e^{i\omega(n)\beta t} \tag{18}$$

or, respectively

$$= \int_{-\infty}^{+\infty} \vec{Y}_\beta e^{i\omega(n)\beta t} d\beta \tag{19}$$

It seems that quantum theoretically the easiest and most natural assumption is to replace Eqs. 16, 17 with

$$Y(n, n-\beta)e^{i\omega(n,n-\beta)t} = \sum_{\alpha=-\infty}^{+\infty} X(n, n-\alpha)X(n-\alpha, n-\beta)e^{i\omega(n,n-\beta)t} \tag{20}$$

$$\text{or} \quad = \int_{-\infty}^{+\infty} X(n, n-\alpha)X(n-\alpha, n-\beta)e^{i\omega(n,n-\beta)t} d\alpha \tag{21}$$

and indeed this way of combination follows almost inevitably from the frequency combination relation. If we accept the assumptions 20, 21 one recognizes also that the phases of the quantum theoretical $\vec{X}$ have the same relevant physical significance as in the classical theory: only the beginning time and hence a phase constant common to all the $\vec{X}$ is arbitrary and without physical meaning but the phase of every single $\vec{X}$ enters in the quantity $\vec{Y}^1$. A geometric interpretation of these quantum theoretic phase relationships in analogy to the classical theory seems at first not possible.

We ask now about how to represent the quantity $x(t)^3$ and we find without difficulty:

$^1$Footnote of WH: Compare also to H.A. Kramers and W.Heisenberg, (add bib. In the expressions used there for the induced scattering momentum, the phases are essentially contained.

5

Classically:

$$Z(n, \gamma) = \sum_{\alpha=-\infty}^{+\infty} \sum_{\beta=-\infty}^{+\infty} X_{\alpha}(n) X_{\beta}(n) X_{\gamma-\alpha-\beta}(n) \quad (22)$$

Quantum theoretically:

$$Z(n, n - \gamma) = \sum_{\alpha=-\infty}^{+\infty} \sum_{\beta=-\infty}^{+\infty} X(n, n - \alpha) X(n - \alpha, n - \alpha - \beta) X(n - \alpha - \beta, n - \gamma) \quad (23)$$

or the corresponding formulae with integrals. In a similar way, all the quantities of the form $x(t)^n$ can be expressed quantum theoretically and when a function $f[x(t)]$ is given, one can always obviously find the quantum theoretical analog if it is possible to expand this function in powers of $x$. A substantial difficulty arises when we consider two quantities $x(t)$, $y(t)$ and we ask about the product $x(t)y(t)$. Let be $x(t)$ characterized with $X$ and $y(t)$ with $Y$ so the representation of $x(t)y(t)$ results:

Classically:

$$Z_{\beta} = \sum_{\alpha=-\infty}^{+\infty} X_{\alpha}(n) Y_{\beta-\alpha}(n) \quad (24)$$

Quantum theoretically:

$$Z(n, n - \beta) = \sum_{\alpha=-\infty}^{+\infty} X(n, n - \alpha) Y(n - \alpha, n - \beta) \quad . \quad (25)$$

While classically $x(t)y(t)$ always equal to $y(t)x(t)$ is, in general it must not be the case in the quantum theory. In special cases, for example when one considers $x(t)x(t)^2$, the difficulty does not arise.

As in the question posed at the beginning of this paragraph, when one considers a form like $v(t)v(t)$ one has to substitute $v\dot{v}$ quantum theoretically with $\frac{v\dot{v}+\dot{v}v}{2}$ for reaching that $v\dot{v}$ enters as the derivative of $\frac{v^2}{2}$.

## Article 2

After these considerations which subject was the kinematic of the quantum theory, we will turn to mechanical problems aiming at the determination of $X, \nu, E$ from the given forces of the system. In the previously presented theory, this problem will be solved in two steps:

6

1. Integration of the equations of motion

$$\ddot{x} + f(x) = 0 \tag{26}$$

2. Determination of the constants arising from periodic motion with

$$\oint p dq = \oint m \dot{x} dx = J(=nh) \quad . \tag{27}$$

If one want to construct a quantum theoretical mechanics which is the possible classical analog, it is probably very close to bring the equation of motion Eq. 26 directly into the quantum theory where it is only necessary to take over, for not abandoning the foundation of in principle observable quantities, instead of the quantities $\ddot{x}, f(x)$, their quantum theoretic representations known from Par. 1. In the classical theory, it is possible to search for a solution of Eq. 26 with the Ansatz for $x$ in Fourier series or Fourier integrals with undetermined coefficients (and frequencies); although in general we obtain infinitely many equations with infinitely many unknowns (or integral equations) which can be solved only in special cases with simple recursion formulae for $X$. However, in the quantum theory, we are dependent on this kind of solution for Eq. 26 which, as discussed before, prevents the definition of direct analogues of the function $x(t)$. This has as consequence that the quantum theoretical solution of Eq. 26 is feasible at first only in the simplest cases. Before going over these simple examples, we would like to derive quantum theoretically the value of the constant in Eq. 27. We assume also that the (classical) motion is periodic:

$$x = \sum_{\alpha=-\infty}^{+\infty} X_{\alpha}(n) e^{i\alpha\omega(n)t} \tag{28}$$

then:

$$m\dot{x} = m \sum_{\alpha=-\infty}^{+\infty} X_{\alpha}(n) \cdot i\alpha\omega(n) e^{i\alpha\omega(n)t} \tag{29}$$

and

$$\oint m\dot{x} dx = \oint m\dot{x}^2 dt = 2\pi m \sum_{\alpha=-\infty}^{+\infty} X_{\alpha}(n) a_{-\alpha}(n) \alpha^2 \omega(n) \quad . \tag{30}$$

7

Further, since $a_{-\alpha}(n) = a_{\alpha}(\bar{n})$ ($x$ must be real), it follows

$$\oint m \dot{x}^2 dt = 2\pi m \sum_{\alpha=-\infty}^{+\infty} |X_{\alpha}(n)|^2 \alpha^2 \omega(n) \quad . \tag{31}$$

Until now, this phase integral was set to a multiple of h (nh); such a condition is not only forced into the classical calculation, but it looks arbitrary also from the previous point of view of the correspondence principle, because correspondence-wise the J is set only up to an additive constant as a multiple integer of h and instead of Eq. 31 one should have had

$$\frac{d}{dn}(nh) = \frac{d}{dn} \cdot \oint m \dot{x}^2 dt \tag{32}$$

which means

$$h = 2\pi m \sum_{\alpha=\infty}^{-\infty} \alpha \frac{d}{dn} (\alpha \omega(n) \cdot |X_{\alpha}(n)|^2) \tag{33}$$

Such a relation though fixes the $X_{\alpha}$s only up to a constant and this indetermination led empirically to the difficulty of half-integer quantum numbers. If we ask for a quantum theoretical relation between observable quantities according to Eq. 31 and 33, the missing unambiguity comes out by itself again. Indeed only Eq. 33 has a simple quantum theoretical connection to the Kramer's dispersion theory:

$$h = 4\pi m \sum_{\alpha=0}^{\infty} \left\{ |X(n, n+\alpha)|^2 \omega(n, n+\alpha) - |X(n, n-\alpha)|^2 \omega(n, n-\alpha) \right\} \tag{34}$$

Indeed, this relationship is sufficient for an unique determination of the $X$s because the initially undetermined constant in the quantities $X$ will be fixed by itself by the condition which should give a normal state where no more radiation is present. Let the normal state be described by $n_0$, then it must be

$$X(n_0, n_0 - \alpha) = 0 \quad \text{for} \quad \alpha > 0 \tag{35}$$

The question about half-integer or integer quantization cannot be present in a quantum mechanics where only relations between observable quantities are used.

Eqs. 26 and 34 together contain, if solvable, a complete determination not only of the frequencies and energies, but also of the quantum theoretical transition probabilities. However, the actual mathematical procedure succeeds

8

only in the easiest cases. A particular complication comes also from systems like the Hydrogen atom: since the solutions represent partly periodic and partly aperiodic motions, it has the consequence that the quantum theoretic series 20, 21 and Eq. 34 always fall in both the sum and the integral case. Quantum mechanically, it is not possible to divide "periodic and aperiodic motions". Despite that, one might see Eq. 26 and Eq.34 at least in principle as a satisfactory solution of the mechanical problem, if it is possible to show that this solution coincides (or is not in contradiction) with the until now known quantum mechanical relationships and that a small perturbation of a mechanical problem gives rise to additional orders in the energies or frequencies respectively which correspond to the expressions found by Kramers and Born (in contrast to which would have lead the classical theory). Further, one must investigate if in general Eq. 26 in the suggested quantum theoretical interpretation corresponds an energy integral $m\frac{x^2}{2} + U(x) = \text{const}$ and if such obtained energy (analogously as classically holds $\nu = \frac{\partial W}{\partial J}$) the relation $\Delta W = h\nu$ is sufficient. A general answer to these questions might demonstrate the coherence of the present experiments and lead to a quantum mechanics which operates only with observable quantities. Apart from a general relationship between the Kramer's dispersion formula and Eq. 26 and 27, we can only answer the above stated questions in very special solvable cases through simple recursion. That general relationship between Kramer's dispersion theory and our Eq. 26 and 27 consists in the fact that in Eq. 26 (i.e. its quantum theoretical analog) like in the the classical theory follows, that the oscillating electron with respect to light which has a much shorter wavelength with respect to the eigenfrequencies of the system, behaves like a free electron. This result follows also from Kramer's theory when Eq. 34 is taken into account. Indeed, Kramers finds for the induced moment by the wave $E \cos 2\pi\nu t$

$$M = e^2 E \cos(2\pi\nu t) \frac{2}{h} \sum_{\alpha=0}^{\infty} \left\{ \frac{|X(n, n+\alpha)|^2 \nu(n, n+\alpha)}{\nu^2(n, n+\alpha) - \nu^2} - \frac{|X(n, n-\alpha)|^2 \nu(n, n-\alpha)}{\nu^2(n, n-\alpha) - \nu^2} \right\} \tag{36}$$

and for $\nu \gg \nu(n, n+\alpha)$

$$M = -\frac{2Ee^2 \cos(2\pi\nu t)}{\nu^2 h} \sum_{\alpha=0}^{\infty} \left\{ |X(n, n+\alpha)|^2 \nu(n, n+\alpha) - |X(n, n-\alpha)|^2 \nu(n, n-\alpha) \right\} \tag{37}$$

9

which using Eq. 34 becomes

$$M = - \frac {e ^ {2} E \cos (2 \pi \nu t)}{\nu^ {2} 4 \pi^ {2} m} \tag {38}$$

### Article 3

In the following, as the simplest example, the anharmonic oscillator will be treated:

$$\ddot {x} + \omega_ {0} ^ {2} x + \lambda x ^ {2} = 0 \tag {39}$$

Classically, this equation can be satisfied by a Anzatz for the solution of the form:

$$x = \lambda a _ {0} + a _ {1} \cos \omega t + \lambda a _ {2} \cos 2 \omega t + \lambda^ {2} a _ {3} \cos 3 \omega t + \dots + \lambda^ {\tau - 1} a _ {\tau} \cos \tau \omega t \tag {40}$$

where the $a$ are power series in $\lambda$, the first terms of which are independent from $\lambda$. Quantum theoretically, we try an analogous approach representing $x$ with terms of the form

$$\begin{array}{l} \lambda a (n, n) \quad ; \quad a (n, n - 1) \cos \omega (n, n - 1) t \quad ; \quad \lambda a (n, n - 2) t \quad ; \\ \dots \quad \lambda^ {\tau - 1} a (n, n - \tau) \cos \omega (n, n - \tau) t \quad \dots \end{array} \tag {41}$$

The recursion formulae for the determination of $a$ and $\omega$ (up to order $\lambda$) according to Eq. 16,17 or Eq. 20, 21 are:

Classically:

$$\left. \begin{array}{c} \omega_ {0} ^ {2} a _ {0} (n) + \frac {a _ {1} ^ {2} (n)}{2} = 0; \\ - \omega^ {2} + \omega_ {0} ^ {2} = 0; \\ (- 4 \omega^ {2} + \omega_ {0} ^ {2}) a _ {2} (n) + \frac {a _ {1} ^ {2}}{2} = 0; \\ (- 9 \omega^ {2} + \omega_ {0} ^ {2}) a _ {3} (n) + a _ {1} a _ {2} = 0; \\ . \quad . \quad . \quad . \quad . \quad . \quad . \quad . \quad . \end{array} \right\} \tag {42}$$

Quantum theoretically:

$$\left. \begin{array}{c} \omega_ {0} ^ {2} a _ {0} (n) + \frac {a ^ {2} (n + 1 , n) + a ^ {2} (n , n - 1)}{4} = 0; \\ - \omega^ {2} (n, n - 1) + \omega_ {0} ^ {2} = 0; \\ \left[ - \omega^ {2} (n, n - 2) + \omega_ {0} ^ {2} \right] a (n, n - 2) + \frac {a (n , n - 1) a (n - 1 , n - 2)}{2} = 0; \\ \left[ - \omega^ {2} (n, n - 3) + \omega_ {0} ^ {2} \right] a (n, n - 3) + \frac {a (n , n - 2) a (n - 1 , n - 3)}{2} + \frac {a (n , n - 2) a (n - 2 , n - 3)}{2} = 0; \\ . \quad . \quad . \quad . \quad . \quad . \quad . \quad . \quad . \end{array} \right\} \tag {43}$$

10

With this comes the quantum condition:

Classically(J=nh):

$$1 = 2 \pi m \frac {d}{d J} \sum_ {- \infty} ^ {\infty} \tau^ {2} \frac {| a _ {\tau} | ^ {2} \omega}{4} \tag {44}$$

Quantum theoretically:

$$h = \pi m \sum_ {0} ^ {\infty} \left[ | a (n + \tau , n) | ^ {2} \omega (n + \tau , n) - | a (n, n - \tau) | ^ {2} \omega (n, n - \tau) \right] \quad . \tag {45}$$

At the first order, this gives, both classically and quantum mechanically:

$$a _ {1} ^ {2} (n) \quad \text { or } \quad a ^ {2} (n, n - 1) = \frac {n + \operatorname{const} h}{\pi m \omega_ {0}} \tag {46}$$

Quantum theoretically, the constant in Eq. 46 can be determined with the condition that $a(n_0, n_0 - 1)$ must vanish in the ground state. If we number n such a way that n is equal to zero in the ground state i.e. $n_0 = 0$, then it follows that

$$a ^ {2} (n, n - 1) = \frac {n h}{\pi m \omega_ {0}} \tag {47}$$

Thus it follows from the recursion equations 42 that in the classical theory $a_{\tau}$ (to first order in $\lambda$) has the form $\chi(\tau)n^{\frac{\tau}{2}}$ where $\chi(\tau)$ represents a factor independent from $n$. In the quantum theory, Eq. 43 Implies

$$a (n, n - \tau) = \chi (\tau) \sqrt {\frac {n !}{(n - \tau) !}} \quad , \tag {48}$$

where $\chi(\tau)$ represents itself a proportionality factor independent from $n$. Naturally, for large values of $n$, the quantum theoretical value of $a_{\tau}$ tends asymptotically to the classical one.

For the energy, it is obvious to try the classical approach

$$E = \frac {m \dot {x} ^ {2}}{2} + m \omega_ {0} ^ {2} \frac {x ^ {2}}{2} + \frac {m \lambda}{3} x ^ {3} \tag {49}$$

since in the presently calculated approximation it is really constant also quantum theoretically. Its value is given by Eq. 43, 46 and ?? as:

11

Classically:

$$E = \frac{nh\omega_0}{2\pi} \quad . \tag{50}$$

Quantum theoretically (from Eq. 20, 21):

$$E = \frac{(n + \frac{1}{2})h\omega_0}{2\pi} \tag{51}$$

(up to $\lambda^2$ order).

From this point of view, it is already not possible to represent the energy of the harmonic oscillator with "classical mechanics", i.e. Eq. ?? but it has instead the form given in Eq. ??.

The precise calculation of the higher orders for E, $a$, and $\omega$ will now be carried out for the simpler example of the anharmonic oscillator of the type:

$$\ddot{x} + \omega_0^2 x + \lambda x^3 = 0 \quad . \tag{52}$$

Classically, we can set in this case:

$$x = a_1 \cos \omega t + \lambda a_3 \cos 3\omega t + \lambda^2 a_5 \cos 5\omega t + \quad ... \quad , \tag{53}$$

and quantum theoretically, we try by analogy the approach

$$a(n, n - 1) \cos \omega(n, n - 1)t \quad ; \quad \lambda a(n, n - 3) \cos \omega(n, n - 3)t \quad ... \tag{54}$$

The quantities $a$ are again power series in $\lambda$ whose first term (as in Eq. ??) has the form:

$$a(n, n - \tau) = \chi(\tau) \sqrt{\frac{n!}{(n - \tau)!}} \quad , \tag{55}$$

as one finds from the evaluation of the equations corresponding to Eq. ?? and 43. If the calculation of $\omega$ and $a$ from Eq. 42 and ?? is carried out to order $\lambda^2$ or $\lambda$ respectively, one obtains:

$$\omega(n, n - 1) = \omega_0 + \lambda \frac{3nh}{8\pi\omega_0^2 m} - \lambda^2 \frac{3h^2}{256\omega_0^5 m^2 \pi^2} (17n^2 + 7) + \quad ... \tag{56}$$

$$a(n, n - 1) = \sqrt{\frac{nh}{\pi\omega_0 m}} \left( 1 - \lambda \frac{3nh}{16\pi\omega^3 m} + \quad ... \right) \quad . \tag{57}$$

12

$$a ( n , n - 3 ) = \frac { 1 } { 3 2 } \sqrt { \frac { h ^ { 3 } } { \pi ^ { 3 } \omega ^ { 7 } m ^ { 3 } } n ( n - 1 ) ( n - 2 ) } \left( 1 - \lambda \frac { 3 9 ( n - 1 ) h } { 3 2 \pi \omega _ { 0 } ^ { 3 } m } \right) \quad . \quad ( 5 8 )$$

The energy, which is defined as the constant term in the expression

$$m \frac { \dot { x } ^ { 2 } } { 2 } + , \omega _ { 0 } ^ { 2 } \frac { x ^ { 2 } } { 2 } + \frac { m \lambda } { 4 } x ^ { 4 } \quad ( 5 9 )$$

(I could not prove in general that all the terms are zero, but it was the case in the evaluated ones) turns out to be

$$W = \frac { n + \textstyle { \frac { 1 } { 2 } } h \omega _ { 0 } } { 2 \pi } + \lambda \frac { 3 ( n ^ { 2 } + n + \textstyle { \frac { 1 } { 2 } } h ^ { 2 } ) } { 8 \cdot 4 \pi ^ { 2 } \omega _ { 0 } ^ { 2 } m } \quad ( 6 0 )$$

$$- \lambda ^ { 2 } \frac { h ^ { 3 } } { 5 1 2 \pi ^ { 3 } \omega _ { 0 } ^ { 5 } m ^ { 2 } } \left( 1 7 n ^ { 3 } + \frac { 5 1 } { 2 } n ^ { 2 } + \frac { 5 9 } { 2 } n + \frac { 2 1 } { 2 } \right) \quad . \quad ( 6 1 )$$

This energy can also be determined with the Kramers-Born procedure by treating the term $\textstyle { \frac { m \lambda } { 4 } } x ^ { 4 }$ as a perturbation to the harmonic oscillator. One comes again exactly to the result of Eq. ?? which seems to me to furnish remarkable support for the quantum-mechanical equations which are considered here as basis. Furthermore, the energy calculated from Eq. ?? satisfies the relation (cf. Eq. 56):

$$\frac { \omega ( n , n - 1 ) } { 2 \pi } = \frac { 1 } { h } \left[ W ( n ) - W ( n - 1 ) \right] \quad , \quad ( 6 2 )$$

which can be regarded as a necessary condition for the possibility of a determination of the transition probabilities according to Eq. 26 and 34.

In conclusion, let us introduce the rotator as example and pay attention to the relationship of Eq. 20, 21 to the intensity formulae for the Zeeman effect $^2$ and for multiplets $^3$. Let the rotator be represented by an electron which circles a nucleus with a constant distance $a$. The "equations of motion" predict, both classically and quantum-theoretically, that the electron simply describes a plane, uniform rotation at a distance $a$ with angular velocity $\omega$

$^2$Goudsmit and R. de L. Kronig, Naturw. **13**, 90, 1925;

H. Hönl, ZS. f. Phys. **31** 340, 1925.

$^3$R. de L. Kronig, ZS. f. Phys. **31** 885, 1925, p.141;

H.N. Russell, Nature **115**, 835, 1925.

13

about the nucleus. The "quantum condition" in Eq. 34 yields according to Eq. 27:

$$h = \frac{d}{dn}(2\pi m a^2 \omega) \quad , \tag{63}$$

and according to Eq. 34:

$$h = 2\pi m \left\{ a^2 \omega(n+1, n) - a^2 \omega(n, n-1) \right\} \quad , \tag{64}$$

from which, in both cases, it follows that:

$$\omega(n, n-1) = \frac{h(n + \text{const})}{2\pi m a^2} \quad . \tag{65}$$

The condition that the radiation should vanish in the ground state ($n_0 = 0$) leads to the formula:

$$\omega(n, n-1) = \frac{h n}{2\pi m a^2} \quad . \tag{66}$$

The energy is

$$W = \frac{m}{2} v^2 \tag{67}$$

or, from Eq. 20, 21

$$W = \frac{m}{2} a^2 \frac{\omega^2(n, n-1) + \omega^2(n+1, n)}{2} = \frac{h^2}{8\pi^2 m a^2} (n^2 + n + \frac{1}{2}) \quad , \tag{68}$$

which again satisfies the condition $\omega(n, n-1) = \frac{2\pi}{h} [W(n) - W(n-1)]$. As support for the validity of Eq. 66 and 68, which differ from those of the usual theory, it can be seen that according to Kratzer$^4$, many band spectra (also those where the existence of an electron momentum is improbable) seem to require formulae of the type of Eq. 66, 68 (which we up to now tried to explain in the context of the classical-mechanical theory with half integer quantization). In order to obtain the Goudsmit-Kronig-Hönl formula for the rotator we have to leave the field of one degree of freedom problems and assume that the rotator is subject to a very slow precession around the z-axis of an external field, whatever its direction in space is. Let the quantum

$^4$Cf. for example, B.A. Kratzer, Sitzungsber. d. Bayr. Akad. (1922) p 107.

14

number of the corresponding precession be $m$. The motion is then represented by the quantities

$$z : a(n, n - 1; m, m) \cos \omega(n, n - 1)t; \tag{69}$$

$$x + iz : b(n, n - 1; m, m - 1)e^{i[\omega(n, n - 1) + \phi]t}; \tag{70}$$

$$b(n, n - 1; m - 1, m)e^{i[-\omega(n, n - 1) + \phi]t} \quad . \tag{71}$$

(72)

The equations of motion are simply:

$$x^2 + y^2 + z^2 = a^2 \quad , \tag{73}$$

and because of Eq. 20 this leads to the equations: $^5$

$$\frac{1}{2} \left\{ \frac{1}{2} a^2(n, n - 1; m, m) + b^2(n, n - 1; m, m - 1) + b^2(n, n - 1; m, m + 1) \right. \tag{74}$$

$$\left. + \frac{1}{2} a^2(n + 1, n; m, m) + b^2(n + 1, n; m - 1, m) + b^2(n + 1, n; m + 1, m) \right\} = a^2 \quad . \tag{75}$$

$$\frac{1}{2} a(n, n - 1; m, m)a(n - 1, n - 2; m, m) \tag{76}$$

$$= b(n, n - 1; m, m + 1)b(n - 1, n - 2; m + 1, m) \tag{77}$$

$$+ b(n, n - 1; m, m - 1)b(n - 1, n - 2; m - 1, m) \quad . \tag{78}$$

Concerning this, from Eq. 34 comes the quantum relation:

$$2\pi m \left\{ b^2(n, n - 1; m, m - 1)\omega(n, n - 1) \right. \tag{79}$$

$$\left. - b^2(n, n - 1; m - 1, m)\omega(n, n - 1) \right\} = (m + \text{const})h \quad . \tag{80}$$

The classical relations corresponding to these equations:

$$\left. \begin{array}{l} \frac{1}{2} a_0^2 + b_1^2 + b_{-1}^2 = a^2; \\ \frac{1}{4} a_0^2 = b_1 b_{-1}; \\ 2\pi m(b_{+1}^2 - b_{-1}^2)\omega = (m + \text{const})h \end{array} \right\} \tag{81}$$

are sufficient (up to the undetermined constant added to m) for uniquely determine $a_0, b_1$ and $b_{-1}$.

$^5$Eq. 75 is essentially identical to the Ornstein-Burger sum rules.

15

The simplest solution of the quantum-theoretical equations 75, 78, 80 which presents itself is:

$$b ( n , n - 1 ; m , m - 1 ) = a { \sqrt { \frac { ( n + m + 1 ) ( n + m ) } { 4 ( n + { \frac { 1 } { 2 } } n ) } } } \quad ;$$

$$b ( n , n - 1 ; m - 1 , m ) = a { \sqrt { \frac { ( n - m ) ( n - m + 1 ) } { 4 ( n + { \frac { 1 } { 2 } } n ) } } } \quad ;$$

$$a ( n , n - 1 ; m , m ) = a { \sqrt { \frac { ( n + m + 1 ) ( n - m ) } { ( n + { \frac { 1 } { 2 } } n ) } } } \quad ;$$

These expressions agree with the formulae of Goudsmit, Kronig and Hönl. However, it is not easy to see that these expressions represent the only solution of equations 75, 78, 80 though this looks likely to me from considering the boundary conditions (vanishing of $a$ and $b$ at the "boundary"; cf. the previously cited works of Kroning, Sommerfeld and Hönl, Russel).

Similar considerations to the above, applied to the multiplet intensity formulae lead to the result that these intensity rules are in agreement with Eq. 20 and 34. This result can again be regarded as giving support to the correctness pf the kinematic equation 20.

Whether a method to determine quantum-theoretical data using relations between observable quantities as proposed here, can be regarded as satisfactory in principle, or whether this method indeed after all represents a too rough approach to the physical problem of constructing a theoretical quantum mechanics, an obviously very involved problem at the moment, can be decided only by a more deep mathematical investigation of the method which has been very superficially employed here.

Göttingen, Institute for Theoretical Physics.

16
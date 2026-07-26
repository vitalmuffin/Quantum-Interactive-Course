R. P. Feynman, Rev. of Mod. Phys., 20, 367

1948

# Space-Time Approach to Non-Relativistic Quantum Mechanics

R.P. Feynman  
Cornell University,  
Ithaca, New York

Reprinted in “Quantum Electrodynamics”, edited by Julian Schwinger

## Abstract

Non-relativistic quantum mechanics is formulated here in a different way. It is, however, mathematically equivalent to the familiar formulation. In quantum mechanics the probability of an event which can happen in several different ways is the absolute square of a sum of complex contributions, one from each alternative way. The probability that a particle will be found to have a path $x(t)$ lying somewhere within a region of space time is the square of a sum of contributions, one from each path in the region. The contribution from a single path is postulated to be an exponential whose (imaginary) phase is the classical action (in units of $\hbar$) for the path in question. The total contribution from all paths reaching $x, t$ from the past is the wave function $\psi(x, t)$. This is shown to satisfy Schroedinger’s equation. The relation to matrix and operator algebra is discussed. Applications are indicated, in particular to eliminate the coordinates of the field oscillators from the equations of quantum electrodynamics.

## 1. Introduction

It is a curious historical fact that modern quantum mechanics began with two quite different mathematical formulations: the differential equation of

1

Schroedinger, and the matrix algebra of Heisenberg. The two, apparently dissimilar approaches, were proved to be mathematically equivalent. These two points of view were destined to complement one another and to be ultimately synthesized in Dirac's transformation theory.

This paper will describe what is essentially a third formulation of non-relativistic quantum theory. This formulation was suggested by some of Dirac's¹,² remarks concerning the relation of classical action³ to quantum mechanics. A probability amplitude is associated with an entire motion of a particle as a function of time, rather than simply with a position of the particle at a particular time.

The formulation is mathematically equivalent to the more usual formulations. There are, therefore, no fundamentally new results. However, there is a pleasure in recognizing old things from a new point of view. Also, there are problems for which the new point of view offers a distinct advantage. For example, if two systems A and B, interact, the coordinates of one of the systems, say B, may be eliminated from the equations describing the motion of A. The interaction with B is represented by a change in the formula for the probability amplitude associated with a motion of A. It is analogous to the classical situation in which the effect of B, can be represented by a change in the equations of motion of A (by the introduction of terms representing forces acting on A). In this way the coordinates of the transverse, as well as of the longitudinal field oscillators, may be eliminated from the equations of quantum electrodynamics.

In addition, there is always the hope that the new point of view will inspire an idea for the modification of present theories, a modification necessary to encompass present experiments.

We first discuss the general concept of the superposition of probability amplitudes in quantum mechanics. We then show how this concept can be directly extended to define a probability amplitude for any motion or path (position vs. time) in space-time. The ordinary quantum mechanics is shown to result from the postulate that this probability amplitude has a phase proportional to the action, computed classically, for this path. This is true when the action is the time integral of a quadratic function of velocity. The relation to matrix and operator algebra is discussed in a way that

¹P. A. M. Dirac, The Principles of Quantum Mechanics (The Clarendon Press, Oxford, 1935), second edition, Section 33; also, Physik. Zeits. Sowjetunion 3, 64 (1933).

²P. A. M. Dirac, Rev. Mod. Phys. 17, 195 (1945).

³Throughout this paper the term "action" will be used for the time integral of the Lagrangian along a path. When this path is the one actually taken by a particle, moving classically, the integral should more properly be called Hamilton's first principle function.

2

stays as close to the language of the new formulation as possible. There is no practical advantage to this, but the formulae are very suggestive if a generalization to a wider class of action functionals is contemplated. Finally, we discuss applications of the formulation. As a particular illustration, we show how the coordinates of a harmonic oscillator may be eliminated from the equations of motion of a system with which it interacts. This can be extended directly for application to quantum electrodynamics. A formal extension which includes the effects of spin and relativity is described.

## 2. The Superposition of Probability Amplitudes

The formulation to be presented contains as its essential idea the concept of a probability amplitude associated with a completely specified motion as a function of time. It is, therefore, worthwhile to review in detail the quantum-mechanical concept of the superposition of probability amplitudes. We shall examine the essential changes in physical outlook required by the transition from classical to quantum physics.

For this purpose, consider an imaginary experiment in which we can make three measurements successive in time: first of a quantity $A$, then of $B$, and then of $C$. There is really no need for these to be of different quantities, and it will do just as well if the example of three successive position measurements is kept in mind. Suppose that $a$ is one of a number of possible results which could come from measurement $A$, $b$ is a result that could arise from $B$, and $c$ is a result possible from the third measurement $C$.$^{4}$ We shall assume that the measurements $A$, $B$, and $C$ are the type of measurements that completely specify a state in the quantum-mechanical case. That is, for example, the state for which $B$ has the value $b$ is not degenerate.

It is well known that quantum mechanics deals with probabilities, but naturally this is not the whole picture. In order to exhibit, even more clearly, the relationship between classical and quantum theory, we could suppose that classically we are also dealing with probabilities but that all probabilities either are zero or one. A better alternative is to imagine in the classical case that the probabilities are in the sense of classical statistical mechanics (where, possibly, internal coordinates are not completely specified).

We define $P_{ab}$ as the probability that if measurement $A$ gave the result $a$,

$^{4}$For our discussion it is not important that certain values of $a, b$, or $c$ might be excluded by quantum mechanics but not by classical mechanics. For simplicity, assume the values are the same for both but that the probability of certain values may be zero.

3

then measurement $B$ will give the result $b$. Similarly, $P_{bc}$ is the probability that if measurement $B$ gives the result $b$, then measurement $C$ gives $c$. Further, let $P_{ac}$ be the chance that if $A$ gives $a$, then $C$ gives $c$. Finally, denote by $P_{abc}$ the probability of all three, i.e., if $A$ gives $a$, then $B$ gives $b$, and $C$ gives $c$. If the events between $a$ and $b$ are independent of those between $b$ and $c$, then

$$P_{abc} = P_{ab}P_{bc}. \quad (1)$$

This is true according to quantum mechanics when the statement that $B$ is $b$ is a complete specification of the state.

In any event, we expect the relation

$$P_{ac} = \sum_b P_{abc}. \quad (2)$$

This is because, if initially measurement $A$ gives $a$ and the system is later found to give the result $c$ to measurement $C$ quantity $B$ must have had some value at the time intermediate to $A$ and $C$. The probability that it was $b$ is $P_{abc}$. We sum, or integrate, over all the mutually exclusive alternatives for $b$ (symbolized by $\sum_b$).

Now, the essential difference between classical and quantum physics lies in Eq. (2). In classical mechanics it is always true. In quantum mechanics it is often false. We shall denote the quantum-mechanical probability that a measurement of $C$ results in $c$ when it follows a measurement of $A$ giving $a$ by $P_{ac}^q$. Equation (2) is replaced in quantum mechanics by this remarkable law:$^5$ There exist complex numbers $\varphi_{ab}, \varphi_{bc}, \varphi_{ac}$ such that

$$P_{ab} = |\varphi_{ab}|^2, \quad P_{bc} = |\varphi_{bc}|^2, \quad \text{and} \quad P_{ac}^q = |\varphi_{ac}|^2. \quad (3)$$

The classical law, obtained by combining (1) and (2),

$$P_{ac} = \sum_b P_{ab}P_{bc} \quad (4)$$

is replaced by

$$\varphi_{ac} = \sum_b \varphi_{ab}\varphi_{bc}. \quad (5)$$

If (5) is correct, ordinarily (4) is incorrect. The logical error made in deducing (4) consisted, of course, in assuming that to get from $a$ to $c$ the system

$^5$We have assumed $b$ is a non-degenerate state, and that therefore (1) is true. Presumably, if in some generalization of quantum mechanics (1) were not true, even for pure states $b$, (2) could be expected to be replaced by: There are complex numbers $\varphi_{abc}$ such that $P_{abc} = |\varphi_{abc}|^2$. The analog of (5) is then $\varphi_{ac} = \sum_b \varphi_{abc}$

4

had to go through a condition such that $B$ had to have some definite value, $b$.

If an attempt is made to verify this, i.e., if $B$ is measured between the experiments $A$ and $C$, then formula (4) is, in fact, correct. More precisely, if the apparatus to measure $B$ is set up and used, but no attempt is made to utilize the results of the $B$ measurement in the sense that only the $A$ to $C$ correlation is recorded and studied, then (4) is correct. This is because the $B$ measuring machine has done its job; if we wish, we could read the meters at any time without disturbing the situation any further. The experiments which gave $a$ and $c$ can, therefore, be separated into groups depending on the value of $b$.

Looking at probability from a frequency point of view (4) simply results from the statement that in each experiment giving $a$ and $c$, $B$ had some value. The only way (4) could be wrong is the statement, “$B$ had some value,” must sometimes be meaningless. Noting that (5) replaces (4) only under the circumstance that we make no attempt to measure $B$, we are led to say that the statement, “$B$ had some value,” may be meaningless whenever we make no attempt to measure $B^6$.

Hence, we have different results for the correlation of $a$ and $c$, namely, Eq. (4) or Eq. (5), depending upon whether we do or do not attempt to measure $B$. No matter how subtly one tries, the attempt to measure $B$ must disturb the system, at least enough to change the results from those given by (5) to those of (4)$^7$. That measurements do, in fact, cause the necessary disturbances, and that, essentially, (4) could be false was first clearly enunciated by Heisenberg in his uncertainty principle. The law (5) is a result of the work of Schroedinger, the statistical interpretation of Born and Jordan, and the transformation theory of Dirac.$^8$

Equation (5) is a typical representation of the wave nature of matter.

$^6$It does not help to point out that we could have measured $B$ had we wished. The fact is that we did not.

$^7$How (4) actually results from (5) when measurements disturb the system has been studied particularly by J. von Neumann (*Mathematische Grundlagen der Quantenmahanik* (Dover Publications, New York, 1943)). The effect of perturbation of the measuring equipment is effectively to change the phase of the interfering components, by $\theta_b$, say, so that (5) becomes $\varphi_{ac} = \sum_b e^{i\theta_b} \varphi_{ab} \varphi_{bc}$. However, as von Neumann shows, the phase shifts must remain unknown if $B$ is measured so that the resulting probability $P_{ac}$ is the square of $\varphi_{ac}$, averaged over all phases, $\theta_b$. This results in (4).

$^8$If $\mathbf{A}$ and $\mathbf{B}$ are the operators corresponding to measurements $A$ and $B$, and if $\psi_a$, and $\psi_b$ are solutions of $\mathbf{A}\psi_a = a\psi_a$, and $\mathbf{B}\chi_b = b\chi_b$, then $\varphi_{ab} = \int \chi_b^* \psi_a dx = (\chi_b^*, \psi_a)$. Thus, $\psi_{ab}$ is an element $(a|b)$ of the transformation matrix for the transformation from a representation in which $\mathbf{A}$ is diagonal to one in which $\mathbf{B}$ is diagonal.

5

Here, the chance of finding a particle going from $a$ to $c$ through several different routes (values of $b$) may, if no attempt is made to determine the route, be represented as the square of a sum of several complex quantities—one for each available route.

Probability can show the typical phenomena of interference, usually associated with waves, whose intensity is given by the square of the sum of contributions from different sources. The electron acts as a wave, (5), so to speak, as long as no attempt is made to verify that it is a particle; yet one can determine, if one wishes, by what route it travels just as though it were a particle; but when one does that, (4) applies and it does act like a particle.

These things are, of course, well known. They have already been explained many times.$^{9}$ However, it seems worth while to emphasize the fact that they are all simply direct consequences of Eq. (5), for it is essentially Eq. (5) that is fundamental in my formulation of quantum mechanics.

The generalization of Eqs. (4) and (5) to a large number of measurements, say $A, B, C, D, \dots, K$, is, of course, that the probability of the sequence $a, b, c, d, \dots, k$, is

$$P_{abcd\dots k} = |\varphi_{abcd\dots k}|^2.$$

The probability of the result $a, c, k$, for example, if $b, d, \dots$ are measured, is the classical formula:

$$P_{ack} = \sum_b \sum_d \dots P_{abcd\dots k}, \quad (6)$$

while the probability of the same sequence $a, c, k$ if no measurements are made between $A$ and $C$ and between $C$ and $K$ is

$$P_{ack}^q = |\sum_b \sum_d \dots \varphi_{abcd\dots k}|^2. \quad (7)$$

The quantity $\varphi_{abcd\dots k}$ we can call the probability amplitude for the condition $A = a$, $B = b$, $C = c$, $D = d, \dots, K = k$. (It is, of course, expressible as a product $\varphi_{ab}\varphi_{bc}\varphi_{cd}\dots\varphi_{jk}$.)

### 3. The Probability Amplitude for a Space-Time Path

The physical ideas of the last section may be readily extended to define a probability amplitude for a particular completely specified space-time

$^{9}$See, for example, W. Heisenberg, *The Physical Principles of the Quantum Theory* (University of Chicago Press, Chicago, 1930), particularly Chapter IV.

6

path. To explain how this may be done, we shall limit ourselves to a one-dimensional problem, as the generalization to several dimensions is obvious.

Assume that we have a particle which can take up various values of a coordinate $x$. Imagine that we make an enormous number of successive position measurements, let us say separated by a small time interval $\epsilon$. Then a succession of measurements such as $A, B, C, \dots$ might be the succession of measurements of the coordinate $x$ at successive times $t_1, t_2, t_3, \dots$, where $t_{i+1} = t_i + \epsilon$. Let the value, which might result from measurement of the coordinate at time $t_i$ be $x_i$. Thus, if $A$ is a measurement of $x$ at $t_1$ then $x_1$ is what we previously denoted by $a$. From a classical point of view, the successive values, $x_1, x_2, x_3, \dots$ of the coordinate practically define a path $x(t)$. Eventually, we expect to go the limit $\epsilon \rightarrow 0$.

The probability of such a path is a function of $x_1, x_2, \dots, x_i, \dots$, say $P(\dots, x_i, x_{i+1}, \dots)$. The probability that the path lies in a particular region $R$ of space-time is obtained classically by integrating $P$ over that region. Thus, the probability that $x_i$, lies between $a_i$ and $b_i$ and $x_{i+1}$ lies between $a_{i+1}$ and etc., is

$$\begin{aligned} \dots \int_{a_i}^{b_i} \int_{a_{i+1}}^{b_{i+1}} \dots P(\dots, x_i, x_{i+1}, \dots) \dots dx, dx_{i+1} \dots &= \\ &= \int_R P(\dots, x_i, x_{i+1}, \dots) \dots dx, dx_{i+1} \dots, \end{aligned} \quad (8)$$

the symbol $\int_R$ meaning that the integration is to be taken over those ranges of the variables which lie within the region $R$. This is simply Eq. (6) with $a, b, \dots$ replaced by $x_1, x_2, \dots$ and integration replacing summation.

In quantum mechanics this is the correct formula for the case that $x_1, x_2, \dots, x_i, \dots$ were actually all measured, and then only those paths lying within $R$ were taken. We would expect the result to be different if no such detailed measurements had been performed. Suppose a measurement is made which is capable only of determining that the path lies somewhere within $R$.

The measurement is to be what we might call an “ideal measurement.” We suppose that no further details could be obtained from the same measurement without further disturbance to the system. I have not been able to find a precise definition. We are trying to avoid the extra uncertainties that must be averaged over if, for example, more information were measured but not utilized. We wish to use Eq. (5) or (7) for all $x_i$ and have no residual part to sum over in the manner of Eq. (4).

7

We expect that the probability that the particle is found by our “ideal measurement” to be, indeed, in the region $R$ is the square of a complex number $|\varphi(R)|^2$. The number $\varphi(R)$, which we may call the probability amplitude for region $R$ is given by Eq. (7) with $a, b, \dots$ replaced by $x_i, x_{i+1}, \dots$ and summation replaced by integration:

$$\varphi(R) = \lim_{\epsilon \rightarrow 0} \int_R \times \Phi(\dots x_i, x_{i+1} \dots) \dots dx_i dx_{i+1} \dots. \quad (9)$$

The complex number $\Phi(\dots x_i, x_{i+1} \dots)$ is a function of the variables $x_i$, defining the path. Actually, we imagine that the time spacing $e$ approaches zero so that $\Phi$ essentially depends on the entire path $x(t)$ rather than only on just the values of $x_i$, at the particular times $t_i$, $x_i = x(t_i)$. We might call $\Phi$ the probability amplitude functional of paths $x(t)$.

We may summarize these ideas in our first postulate:

*I. If an ideal measurement is performed, to determine whether a particle has a path lying in a region of space-time, then the probability that the result will be affirmative is the absolute square of a sum of complex contributions, one from each path in the region.*

The statement of the postulate is incomplete. The meaning of a sum of terms one for “each” path is ambiguous. The precise meaning given in Eq. (9) is this: A path is first defined only by the positions $x_i$; through which it goes at a sequence of equally spaced times, $^{10}$ $t_i = t_{i-1} + \epsilon$. Then all values of the coordinates within $R$ have an equal weight. The actual magnitude of the weight depends upon $\epsilon$ and can be so chosen that the probability of an event which is certain shall be normalized to unity. It may not be best to do so, but we have left this weight factor in a proportionality constant in the second postulate. The limit $\epsilon \rightarrow 0$ must be taken at the end of a calculation.

When the system has several degrees of freedom the coordinate space $x$ has several dimensions so that the symbol $x$ will represent a set of coordinates $(x^{(1)}, x^{(2)}, \dots, x^{(k)})$ for a system with $k$ degrees of freedom. A path is a sequence of configurations for successive times and is described by giving the configuration $x_i$, or $(x_i^{(1)}, x_i^{(2)}, \dots, x_i^{(k)})$, i.e., the value of each of the $k$ coordinates for each time $t_i$. The symbol $dx_i$, will be understood to mean

$^{10}$There are very interesting mathematical problems involved in the attempt to avoid the subdivision and limiting processes. Some sort of complex measure is being associated with the space of functions $x(t)$. Finite results can be obtained under unexpected circumstances because the measure is not positive everywhere, but the contributions from most of the paths largely cancel out. These curious mathematical problems are sidestepped by the subdivision process. However, one feels as Cavalieri must have felt calculating the volume of a pyramid before the invention of calculus.

8

the volume element in $k$ dimensional configuration space (at time $t_i$). The statement of the postulates is independent of the coordinate system which is used.

The postulate is limited to defining the results of position measurements. It does not say what must be done to define the result of a momentum measurement, for example. This is not a real limitation, however, because in principle the measurement of momentum of one particle can be performed in terms of position measurements of other particles, e.g., meter indicators. Thus, an analysis of such an experiment will determine what it is about the first particle which determines its momentum.

#### 4. The Calculation of the Probability Amplitude for a Path

The first postulate prescribes the type of mathematical framework required by quantum mechanics for the calculation of probabilities. The second postulate gives a particular content to this framework by prescribing how to compute the important quantity $\Phi$ for each path:

*II. The paths contribute equally in magnitude, but the phase of their contribution is the classical action (in units of $\hbar$); i.e., the time integral of the Lagrangian taken along the path.*

That is to say, the contribution $\Phi[x(t)]$ from a given path $x(t)$ is proportional to $\exp(i/\hbar S[x(t)])$, where the action $S[x(t)] = \int L(\dot{x}(t), x(t)) dt$ is the time integral of the classical Lagrangian $L(\dot{x}, x)$ taken along the path in question. The Lagrangian, which may be an explicit function of the time, is a function of position and velocity. If we suppose it to be a quadratic function of the velocities, we can show the mathematical equivalence of the postulates here and the more usual formulation of quantum mechanics.

To interpret the first postulate it was necessary to define a path by giving only the succession of points $x_i$, through which the path passes at successive times $t_i$. To compute $S = \int L(\dot{x}, x) dt$ we need to know the path at all points, not just at $x_i$. We shall assume that the function $x(t)$ in the interval between $t_i$ and $t_{i+1}$ is the path followed by a classical particle, with the Lagrangian $L$, which starting from $x_i$, at $t_i$ reaches $x_{i+1}$ at $t_{i+1}$. This assumption is required to interpret the second postulate for discontinuous paths. The quantity $\Phi(\dots, x_i, x_{i+1}, \dots)$ can be normalized (for various $\epsilon$) if desired, so that the probability of an event which is certain is normalized to unity as $\epsilon \rightarrow 0$.

There is no difficulty in carrying out the action integral because of the

9

sudden changes of velocity encountered at the times $t_i$ as long as $L$ does not depend upon any higher time derivatives of the position than the first. Furthermore, unless $L$ is restricted in this way the end points are not sufficient to define the classical path. Since the classical path is the one which makes the action a minimum, we can write

$$S = \sum_i S(x_{i+1}, x_i), \quad (10)$$

where

$$S(x_{i+1}, x_i) = \text{Min.} \int_{t_i}^{t_{i+1}} L(\dot{x}(t), x(t)) dt. \quad (11)$$

Written in this way, the only appeal to classical mechanics is to supply us with a Lagrangian function. Indeed, one could consider postulate two as simply saying, “$\Phi$ is the exponential of $i$ times the integral of a real function of $x(t)$ and its first time derivative.” Then the classical equations of motion might be derived later as the limit for large dimensions. The function of $x$ and $\dot{x}$ then could be shown to be the classical Lagrangian within a constant factor.

Actually, the sum in (10), even for finite $\epsilon$ is infinite and hence meaningless (because of the infinite extent of time). This reflects a further incompleteness of the postulates. We shall have to restrict ourselves to a finite, but arbitrarily long, time interval.

Combining the two postulates and using Eq. (10), we find

$$\varphi(R) = \lim_{\epsilon \to 0} \int_R \times \exp \left[ \frac{i}{\hbar} \sum_i S(x_{i+1}, x_i) \right] \cdots \frac{dx_{i+1}}{A} \frac{dx_i}{A} \cdots, \quad (12)$$

where we have let the normalization factor be split into a factor $1/A$ (whose exact value we shall presently determine) for each instant of time. The integration is just over those values $x_i, x_{i+1}, \dots$ which lie in the region $R$. This equation, the definition (11) of $S(x_{i+1}, x_i)$, and the physical interpretation of $|\varphi(R)|^2$ as the probability that the particle will be found in $R$, complete our formulation of quantum mechanics.

## 5. Definition of the Wave Function

We now proceed to show the equivalence of these postulates to the ordinary formulation of quantum mechanics. This we do in two steps. We show in this

10

section how the wave function may be defined from the new point of view. In the next section we shall show that this function satisfies Schroedinger's differential wave equation.

We shall see that it is the possibility, (10), of expressing $S$ as a sum, and hence $\Phi$ as a product, of contributions from successive sections of the path, which leads to the possibility of defining a quantity having the properties of a wave function.

To make this clear, let us imagine that we choose a particular time $t$ and divide the region $R$ in Eq. (12) into pieces, future and past relative to $t$. We imagine that $R$ can be split into: (a) a region $R'$, restricted in any way in space, but lying entirely earlier in time than some $t'$, such that $t' < t$; (b) a region $R''$ arbitrarily restricted in space but lying entirely later in time than $t''$, such that $t'' > t$; (c) the region between $t'$ and $t''$ in which all the values of $x$ coordinates are unrestricted, i.e., all of space-time between $t'$ and $t''$. The region (c) is not absolutely necessary. It can be taken as narrow in time as desired. However, it is convenient in letting us consider varying $t$ a little without having to redefine $R'$ and $R''$. Then $|\varphi(R', R'')|^2$ is the probability that the path occupies $R'$ and $R''$. Because $R'$ is entirely previous to $R''$, considering the time $t$ as the present, we can express this as the probability that the path had been in region $R'$ and will be in region $R''$. If we divide by a factor, the probability that the path is in $R'$, to renormalize the probability we find: $|\varphi(R', R'')|^2$ is the (relative) probability that if the system were in region $R'$ it will be found later in $R''$.

This is, of course, the important quantity in predicting the results of many experiments. We prepare the system in a certain way (e.g., it was in region $R'$) and then measure some other property (e.g., will it be found in region $R''$?). What does (12) say about computing this quantity, or rather the quantity $\varphi(R', R'')$ of which it is the square?

Let us suppose in Eq. (12) that the time $t$ corresponds to one particular point $k$ of the subdivision of time into steps $\epsilon$, i.e., assume $t = t_k$, the index $k$, of course, depending upon the subdivision $\epsilon$. Then, the exponential being the exponential of a sum may be split into a product of two factors

$$\exp \left[ \frac{i}{\hbar} \sum_{i=k}^{\infty} S(x_{i+1}, x_i) \right] \cdot \exp \left[ \frac{i}{\hbar} \sum_{i=-\infty}^{k-1} S(x_{i+1}, x_i) \right]. \quad (13)$$

The first factor contains only coordinates with index $k$ or higher, while the second contains only coordinates with index $k$ or lower. This split is possible because of Eq. (10), which results essentially from the fact that the Lagrangian is a function only of positions and velocities. First, the

11

integration on all variables $x_i$ for $i > k$ can be performed on the first factor resulting in a function of $x_k$ (times the second factor). Next, the integration on all variables $x_i$, for $i < k$ can be performed on the second factor also, giving a function of $x_k$. Finally, the integration on $x_k$ can be performed. That is, $\varphi(R', R'')$ can be written as the integral over $x_k$ of the product of two factors. We will call these $\chi^*(x_k, t)$ and $\psi(x_k, t)$:

$$\varphi(R', R'') = \int \chi^*(x, t) \psi(x, t) dx, \quad (14)$$

where

$$\psi(x_k, t) = \lim_{\epsilon \to 0} \int_{R'} \times \exp \left[ \frac{i}{\hbar} \sum_{i=-\infty}^{k-1} S(x_{i+1}, x_i) \right] \frac{dx_{k-1}}{A} \frac{dx_{k-2}}{A} \dots, \quad (15)$$

and

$$\chi^*(x_k, t) = \lim_{\epsilon \to 0} \int_{R''} \exp \left[ \frac{i}{\hbar} \sum_{i=k}^{\infty} S(x_{i+1}, x_i) \right] \cdot \frac{1}{A} \frac{dx_{k+1}}{A} \frac{dx_{k+2}}{A} \dots. \quad (16)$$

The symbol $R'$ is placed on the integral for $\psi$ to indicate that the coordinates are integrated over the region $R'$, and, for $t_i$ between $t'$ and $t$, over all space. In like manner, the integral for $\chi^*$ is over $R''$ and over all space for those coordinates corresponding to times between $t$ and $t''$. The asterisk on $\chi^*$ denotes complex conjugate, as it will be found more convenient to define (16) as the complex conjugate of some quantity, $\chi$.

The quantity $\psi$ depends only upon the region $R'$ previous to $t$, and is completely denned if that region is known. It does not depend, in any way, upon what will be done to the system after time $t$. This latter information is contained in $\chi$. Thus, with $\psi$ and $\chi$ we have separated the past history from the future experiences of the system. This permits us to speak of the relation of past and future in the conventional manner. Thus, if a particle has been in a region of space-time $R'$ it may at time $t$ be said to be in a certain condition, or state, determined only by its past and described by the so-called wave function $\psi(x, t)$. This function contains all that is needed to predict future probabilities. For, suppose, in another situation, the region $R'$ were different, say $r'$, and possibly the Lagrangian for times before $t$ were also altered. But, nevertheless, suppose the quantity from Eq. (15) turned out to be the same. Then, according to (14) the probability of ending in any region $R''$ is the same for $R'$ as for $r'$. Therefore, future measurements will not distinguish whether the system had occupied $R'$ or $r'$. Thus, the

12

wave function $\psi(x,t)$ is sufficient to define those attributes which are left from past history which determine future behavior.

Likewise, the function $\chi(x,t)$ characterizes the experience, or, let us say, experiment to which the system is to be subjected. If a different region, $r''$ and different Lagrangian after $t$, were to give the same $\chi^*(x,t)$ *via* Eq. (16), as does region $R''$, then no matter what the preparation, $\psi$, Eq. (14) says that the chance of finding the system in $R''$ is always the same as finding it in $r''$. The two “experiments” $R''$ and $r''$ are equivalent, as they yield the same results. We shall say loosely that these experiments are to determine with what probability the system is in state $\chi$. Actually, this terminology is poor. The system is really in state $\psi$. The reason we can associate a state with an experiment is, of course, that for an ideal experiment there turns out to be a unique state (whose wave function is $\chi(x,t)$), for which the experiment succeeds with certainty.

Thus, we can say: the probability that a system in state $\psi$ will be found by an experiment whose characteristic state is $\chi$ (or, more loosely, the chance that a system in state $\psi$ will appear to be in $\chi$) is

$$\left| \int \chi^*(x,t)\psi(x,t)dx \right|^2. \quad (17)$$

These results agree, of course, with the principles of ordinary quantum mechanics. They are a consequence of the fact that the Lagrangian is a function of position, velocity, and time only.

## 6. The Wave Equation

To complete the proof of the equivalence with the ordinary formulation we shall have to show that the wave function defined in the previous section by Eq. (15) actually satisfies the Schroedinger wave equation. Actually, we shall only succeed in doing this when the Lagrangian $L$ in (11) is a quadratic, but perhaps inhomogeneous, form in the velocities $\dot{x}(t)$. This is not a limitation, however, as it includes all the cases for which the Schroedinger equation has been verified by experiment.

The wave equation describes the development of the wave function with time. We may expect to approach it by noting that, for finite $\epsilon$, Eq. (15) permits a simple recursive relation to be developed. Consider the appearance of Eq. (15) if we were to compute $\psi$ at the next instant of time:

$$\psi(x_{k+1}, t+\epsilon) = \int_{R'} \exp\left[ \frac{i}{\hbar} \sum_{i=-\infty}^k S(x_{i+1}, x_i) \right] \times \frac{dx_k}{A} \frac{dx_{k-1}}{A} \dots \quad (15')$$

13

This is similar to (15) except for the integration over the additional variable $x_k$, and the extra term in the sum in the exponent. This term means that the integral of (15') is the same as the integral of (15) except for the factor $(1/A)\exp(i/\hbar)S(x_{k+1}, x_k)$. Since this does not contain any of the variables $x_i$, for $i$ less than $k$, all of the integrations on $dx$, up to $dx_{k-1}$ can be performed with this factor left out. However, the result of these integrations is by (15) simply $\psi(x_k, t)$. Hence, we find from (15') the relation

$$\psi(x_{k+1}, t + \epsilon) = \int \exp\left[\frac{i}{\hbar}S(x_{k+1}, x_k)\right] \psi(x_k, t) dx_k / A. \quad (18)$$

This relation giving the development of $\psi$ with time will be shown, for simple examples, with suitable choice of $A$, to be equivalent to Schroedinger's equation. Actually, Eq. (18) is not exact, but is only true in the limit $\epsilon \rightarrow 0$ and we shall derive the Schroedinger equation by assuming (18) is valid to first order in $\epsilon$. The Eq. (18) *need* only be true for small $\epsilon$ to the first order in $\epsilon$. For if we consider the factors in (15) which carry us over a finite interval of time, $T$, the number of factors is $T/\epsilon$. If an error of order $\epsilon^2$ is made in each, the resulting error will not accumulate beyond the order $\epsilon^2(T/\epsilon)$ or $T\epsilon$, which vanishes in the limit.

We shall illustrate the relation of (18) to Schroedinger's equation by applying it to the simple case of a particle moving in one dimension in a potential $V(x)$. Before we do this, however, we would like to discuss some approximations to the value $S(x_{i+1}, x_i)$ given in (11) which will be sufficient for expression (18).

The expression defined in (11) for $S(x_{i+1}, x_i)$ is difficult to calculate exactly for arbitrary $\epsilon$ from classical mechanics. Actually, it is only necessary that an approximate expression for $S(x_{i+1}, x_i)$ be used in (18), provided the error of the approximation be of an order smaller than the first in $\epsilon$. We limit ourselves to the case that the Lagrangian is a quadratic, but perhaps inhomogeneous, form in the velocities $\dot{x}(t)$. As we shall see later, the paths which are important are those for which $x_{i+1} - x_i$ is of order $\epsilon^{1/2}$. Under these circumstances, it is sufficient to calculate the integral in (11) over the classical path taken by a *free* particle.$^{11}$ In *Cartesian coordinates*$^{12}$ the path of a free particle is a straight line so the integral of (11) can be taken

$^{11}$It is assumed that the 'forces' enter through a scalar and vector potential and not in terms involving the square of the velocity. More generally, what is meant by a free particle is one for which the Lagrangian is altered by omission of the terms linear in, and those independent of, the velocities.

$^{12}$More generally, coordinates for which the terms quadratic in the velocity in $L(\dot{x}, x)$ appear with constant coefficients.

14

along a straight line. Under these circumstances it is sufficiently accurate to replace the integral by the trapezoidal rule

$$S(x_{i+1}, x_i) = \frac{\epsilon}{2} L \left( \frac{x_{i+1} - x_i}{\epsilon}, x_{i+1} \right) + \frac{\epsilon}{2} L \left( \frac{x_{i+1} - x_i}{\epsilon}, x_i \right) \tag{19}$$

or, if it proves more convenient,

$$S(x_{i+1}, x_i) = \epsilon L \left( \frac{x_{i+1} - x_i}{\epsilon}, \frac{x_{i+1} + x_i}{2} \right). \tag{20}$$

These are not valid in a general coordinate system, e.g., spherical. An even simpler approximation may be used if, in addition, there is no vector potential or other terms linear in the velocity (see page 376):

$$S(x_{i+1}, x_i) = \epsilon L \left( \frac{x_{i-1} - x_i}{\epsilon}, x_{i+1} \right). \tag{21}$$

Thus, for the simple example of a particle of mass $m$ moving in one dimension under a potential $V(x)$, we can set

$$S(x_{i+1}, x_i) = \frac{m\epsilon}{2} \left( \frac{x_{i+1} - x_i}{\epsilon} \right) - \epsilon V(x_{i+1}). \tag{22}$$

For this example, then, Eq. (18) becomes

$$\psi(x_{k+1}, t + \epsilon) = \int \exp \left[ \frac{i\epsilon}{\hbar} \left\{ \frac{m}{2} \left( \frac{x_{k+1} - x_k}{\epsilon} \right)^2 - \right. \right. \\ \left. \left. - V(x_{k+1}) \right\} \right] \psi(x_k, t) dx_k / A. \tag{23}$$

Let us call $x_{k+1} = x$ and $x_{k+1} - x_k = \xi$ so that $x_k = x - \xi$. Then (23) becomes

$$\psi(x, t + \epsilon) = \int \exp \frac{im\xi^2}{\epsilon \cdot 2\hbar} \cdot \exp \frac{-i\epsilon V(x)}{\hbar} \cdot \psi(x - \xi, t) \frac{d\xi}{A}. \tag{24}$$

The integral on $\xi$ will converge if $\psi(x, t)$ falls off sufficiently for large $x$ (certainly if $\int \psi^*(x) \psi(x) dx = 1$). In the integration on $\xi$, since $\epsilon$ is very small, the exponential of $im\xi^2/2\hbar\epsilon$ oscillates extremely rapidly except in the region about $\xi = 0$ ($\xi$ of order $(\hbar\epsilon/m)^{1/2}$). Since the function $\psi(x - \xi, t)$ is a relatively smooth function of $\xi$ (since $\epsilon$ may be taken as small as desired), the region where the exponential oscillates rapidly will contribute very little

15

because of the almost complete cancelation of positive and negative contributions. Since only small $\xi$ are effective, $\psi(x - \xi, t)$ may be expanded as a Taylor series. Hence,

$$\psi(x, t + \epsilon) = \exp \left( \frac{-i\epsilon V(x)}{\hbar} \right) \times$$

$$\times \int \exp \left( \frac{im\xi^2}{2\hbar\epsilon} \right) \left[ \psi(x, t) - \xi \frac{\partial \psi(x, t)}{\partial x} + \frac{\xi^2}{2} \frac{\partial^2 \psi(x, t)}{\partial x^2} - \dots \right] d\xi / A. \quad (25)$$

Now

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) d\xi = (2\pi\hbar\epsilon i/m)^{1/2},$$

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) \xi d\xi = 0, \quad (26)$$

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) \xi^2 d\xi = (\hbar\epsilon i/m)(2\pi\hbar\epsilon i/m)^{1/2},$$

while the integral containing $\xi^2$ is zero, for like the one with $\xi$ it possesses an odd integrand, and the ones with $\xi^4$ are of at least the order $\epsilon$ smaller than the ones kept here.$^{13}$ If we expand the left-hand side to first order in $\epsilon$ (25) becomes

$$\psi(x, t) + \epsilon \frac{\partial \psi(x, t)}{\partial t} = \exp \left( \frac{-i\epsilon V(x)}{\hbar} \right) \frac{(2\pi\hbar\epsilon i/m)^{1/2}}{A} \times \left[ \psi(x, t) + \frac{\hbar\epsilon i}{m} \frac{\partial^2 \psi(x, t)}{\partial x^2} + \dots \right]. \quad (27)$$

In order that both sides may agree to zero order in $\epsilon$, we must set

$$A = (2\pi\hbar\epsilon i/m)^{1/2}. \quad (28)$$

Then expanding the exponential containing $V(x)$, we get

$$\psi(x, t) + \epsilon \frac{\partial \psi}{\partial t} = \left( 1 - \frac{i\epsilon}{\hbar} V(x) \right) \times \left( \psi(x, t) + \frac{\hbar\epsilon i}{2m} \frac{\partial^2 \psi}{\partial x^2} \right). \quad (29)$$

$^{13}$Really, these integrals are oscillatory and not defined, but they may be defined by using a convergence factor. Such a factor is automatically provided by $\psi(x - \xi, t)$ in (24). If a more formal procedure is desired replace $\hbar$ by $\hbar(1 - i\delta)$, for example, where $\delta$ is a small positive number, and then let $\delta \to 0$.

16

Canceling $\psi(x,t)$ from both sides, and comparing terms to first order in $\epsilon$ and multiplying by $-\hbar/i$ one obtains

$$-\frac{\hbar}{i}\frac{\partial\psi}{\partial t}=\frac{1}{2\dot{m}}\left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right)^2\psi+V(x)\psi,\quad(30)$$

which is Schroedinger's equation for the problem in question.

The equation for $\chi^*$ can be developed in the same way, but adding a factor *decreases* the time by one step, i.e., $\chi^*$ satisfies an equation like (30) but with the sign of the time reversed. By taking complex conjugates we can conclude that $\chi$ satisfies the same equation as $\psi$, i.e., an experiment can be defined by the particular state $\chi$ to which it corresponds.$^{14}$

This example shows that most of the contribution to $\psi(x_{k+1},t+\epsilon)$ comes from values of $x_k$ in $\psi(x_k,t)$ which are quite close to $x_{k+1}$ (distant of order $\epsilon^{1/2}$) so that the integral equation (23) can, in the limit, be replaced by a differential equation. The 'velocities,' $(x_{k+1}-x_k)/\epsilon$ which are important are very high, being of order $(\hbar/m\epsilon)^{1/2}$ which diverges as $\epsilon\rightarrow 0$. The paths involved are, therefore, continuous but possess no derivative. They are of a type familiar from study of Brownian motion.

It is these large velocities which make it so necessary to be careful in approximating $S(x_{k+1},x_k)$ from Eq. (11).$^{15}$ To replace $V(x_{k+1})$ by $V(x_k)$ would, of course, change the exponent in (18) by $i\epsilon[V(x_k)-V(x_{k+1})]/\hbar$ which is of order $\epsilon(x_{k+1}-x_k)$, and thus lead to unimportant terms of higher order than $\epsilon$ on the right-hand side of (29). It is for this reason that (20) and (21) are equally satisfactory approximations to $S(x_{i+1},x_i)$ when there is no vector potential. A term, linear in velocity, however, arising from a vector potential, as $A\dot{x}dt$ must be handled more carefully. Here a term in $S(x_{k+1},x_k)$ such as $A(x_{k+1})\times(x_{k+1}-x_k)$ differs from $A(x_k)(x_{k+1}-x_k)$ by a term of order

$^{14}$Dr. Hartland Snyder has pointed out to me, in private conversation, the very interesting possibility that there may be a generalization of quantum mechanics in which the states measured by experiment cannot be prepared; that is, there would be no state into which a system may be put for which a particular experiment gives certainty for a result. The class of functions $\chi$ is not identical to the class of available states $\psi$. This would result if, for example, $\chi$ satisfied a different equation than $\psi$.

$^{15}$Equation (18) is actually exact when (11) is used for $S(x_{i+1},x_i)$ for arbitrary $\epsilon$ for cases in which the potential does not involve $x$ to higher powers than the second (e.g., free particle, harmonic oscillator). It is necessary, however, to use a more accurate value of $A$. One can define $A$ in this way. Assume classical particles with $k$ degrees of freedom start from the point $x_i,t_i$, with uniform density in momentum space. Write the number of particles having a given component of momentum in range $dp$ as $dp/p_1$, with $p_0$, constant. Then $A=(2\pi\hbar i/p_0)^{k/2}\rho^{-1/2}$, where $\rho$ is the density in $k$ dimensional coordinate space $x_{i+1}$ of these particles at time $t_{i+1}$.

17

$(x_{k+1} - x_k)^2$, and, therefore, of order $\epsilon$. Such a term would lead to a change in the resulting wave equation. For this reason the approximation (21) is not a sufficiently accurate approximation to (11) and one like (20), (or (19) from which (20) differs by terms of order higher than $\epsilon$) must be used. If $\mathbf{A}$ represents the vector potential and $\mathbf{p} = (\hbar/i)\nabla$, the momentum operator, then (20) gives, in the Hamiltonian operator, a term $(1/2m)(\mathbf{p} - (e/c)\mathbf{A}) \cdot (\mathbf{p} - e/c)\mathbf{A}$, while (21) gives $(1/2m)(\mathbf{p} \cdot \mathbf{p} - (2e/c)\mathbf{A} \cdot \mathbf{p} + (e^2/c^2)\mathbf{A} \cdot \mathbf{A})$. These two expressions differ by $(\hbar e/2imc) \nabla \cdot \mathbf{A}$ which may not be zero. The question is still more important in the coefficient of terms which are quadratic in the velocities. In these terms (19) and (20) are not sufficiently accurate representations of (11) in general. It is when the coefficients are constant that (19) or (20) can be substituted for (11). If an expression such as (19) is used, say for spherical coordinates, when it is not a valid approximation to (11), one obtains a Schroedinger equation in which the Hamiltonian operator has some of the momentum operators and coordinates in the wrong order. Equation (11) then resolves the ambiguity in the usual rule to replace $p$ and $q$ by the non-commuting quantities $(\hbar/i)(\partial/\partial q)$ and $q$ in the classical Hamiltonian $H(p, q)$.

It is clear that the statement (11) is independent of the coordinate system. Therefore, to find the differential wave equation it gives in any coordinate system, the easiest procedure is first to find the equations in Cartesian coordinates and then to transform the coordinate system to the one desired. It suffices, therefore, to show the relation of the postulates and Schroedinger's equation in rectangular coordinates.

The derivation given here for one dimension can be extended directly to the case of three-dimensional Cartesian coordinates for any number, $K$, of particles interacting through potentials with one another, and in a magnetic field, described by a vector potential. The terms in the vector potential require completing the square in the exponent in the usual way for Gaussian integrals. The variable $x$ must be replaced by the set $x^{(1)}$ to $x^{(3K)}$ where $x^{(1)}, x^{(2)}, x^{(3)}$ are the coordinates of the first particle of mass $m_1, x^{(4)}, x^{(5)}, x^{(6)}$ of the second of mass $m_2$, etc. The symbol $dx$ is replaced by $dx^{(1)}dx^{(2)} \dots dx^{(3K)}$, and the integration over $dx$ is replaced by a $3K$-fold integral. The constant $A$ has, in this case, the valued $A = (2\pi\hbar e i/m_1)^{1/2}(2\pi\hbar e i/m_2)^{1/2} \dots (2\pi\hbar e i/m_K)^{1/2}$. The Lagrangian is the classical Lagrangian for the same problem, and the Schroedinger equation resulting will be that which corresponds to the classical Hamiltonian, derived from this Lagrangian. The equations in any other coordinate system may be obtained by transformation. Since this includes all cases for which Schroedinger's equation has been checked with experiment, we may say our

18

postulates are able to describe what can be described by non-relativistic quantum mechanics, neglecting spin.

## 7. Discussion of the Wave Equation

### The Classical Limit

This completes the demonstration of the equivalence of the new and old formulations. We should like to include in this section a few remarks about the important equation (18).

This equation gives the development of the wave function during a small time interval. It is easily interpreted physically as the expression of Huygens' principle for matter waves. In geometrical optics the rays in an inhomogeneous medium satisfy Fermat's principle of least *time*. We may state Huygens' principle in wave optics in this way: If the amplitude of the wave is known on a given surface, the amplitude at a near by point can be considered as a sum of contributions from all points of the surface. Each contribution is delayed in phase by an amount proportional to the *time* it would take the light to get from the surface to the point along the ray of least *time* of geometrical optics. We can consider (22) in an analogous manner starting with Hamilton's first principle of least *action* for classical or 'geometrical' mechanics. If the amplitude of the wave $\psi$ is known on a given 'surface,' in particular the 'surface' consisting of all $x$ at time $t$, its value at a particular nearby point at time $t + \epsilon$, is a sum of contributions from all points of the surface at $t$. Each contribution is delayed in phase by an amount proportional to the *action* it would require to get from the surface to the point along the path of least action of classical mechanics. $^{16}$

Actually Huygens' principle is not correct in optics. It is replaced by Kirchhoff's modification which requires that both the amplitude and its derivative must be known on the adjacent surface. This is a consequence of the fact that the wave equation in optics is second order in the time. The wave equation of quantum mechanics is first order in the time; therefore, Huygens' principle *is* correct for matter waves, action replacing time.

The equation can also be compared mathematically to quantities appearing in the usual formulations. In Schroedinger's method the development of the wave function with time is given by

$$- \frac{\hbar}{i} \frac{\partial \psi}{\partial t} = \mathbf{H} \psi, \quad (31)$$

---$^{16}$See in this connection the very interesting remarks of Schroedinger, Ann. d. Physik **79**, 489 (1926).

19

which has the solution (for any $\epsilon$ if $\mathbf{H}$ is time independent)

$$\psi(x, t + \epsilon) = \exp(-i\epsilon\mathbf{H}/\hbar)\psi(x, t). \quad (32)$$

Therefore, Eq. (18) expresses the operator $\exp(-i\epsilon\mathbf{H}/\hbar)$ by an approximate integral operator for small $\epsilon$.

From the point of view of Heisenberg one considers the position at time $t$, for example, as an operator $\mathbf{x}$. The position $\mathbf{x}'$ at a later time $t + \epsilon$ can be expressed in terms of that at time $t$ by the operator equation

$$\mathbf{x}' = \exp(i\epsilon\mathbf{H}/\hbar)\mathbf{x}\exp(-i\epsilon\mathbf{H}/\hbar). \quad (33)$$

The transformation theory of Dirac allows us to consider the wave function at time $t + \epsilon$, $\psi(x', t + \epsilon)$, as representing a state in a representation in which $\mathbf{x}'$ is diagonal, while $\psi(x, t)$ represents the same state in a representation in which $\mathbf{x}$ is diagonal. They are, therefore, related through the transformation function $(x'|x)_\epsilon$, which relates these representations:

$$\psi(x', t + \epsilon) = \int (x'|x)_\epsilon\psi(x, t)dx.$$

Therefore, the content of Eq. (18) is to show that for small $\epsilon$ we can set

$$(x'|x)_\epsilon = (1/A)\exp(iS(x', x)/\hbar) \quad (34)$$

with $S(x', x)$ defined as in (11).

The close analogy between $(x', |x)_\epsilon$ and the quantity $\exp(iS(x', x)/\hbar)$ has been pointed out on several occasions by Dirac.$^{17}$ In fact, we now see that to sufficient approximations the two quantities may be taken to be proportional to each other. Dirac's remarks were the starting point of the present development. The points he makes concerning the passage to the classical limit $\hbar \rightarrow 0$ are very beautiful, and I may perhaps be excused for briefly reviewing them here.

First we note that the wave function at $x''$ at time $t''$ can be obtained from that at $x'$ at time $t'$ by

$$\psi(x'', t'') = \lim_{\epsilon \rightarrow 0} \int \dots \int \times \times \exp\left[ \frac{i}{\hbar} \sum_{i=0}^{j-1} S(x_{i+1}, x_i) \right] \times \psi(x', t') \frac{dx_0}{A} \frac{dx_1}{A} \dots \frac{dx_{j-1}}{A}, \quad (35)$$

$^{17}$P. A. M. Dirac, *The Principles of Quantum Mechanics* (The Clarendon Press, Oxford, 1935), second edition, Section 33; also, Physik. Zeits. Sowjetunion **3**, 64 (1933).

20

where we put $x_0 \equiv x''$ and $x_j \equiv x''$ where $i\epsilon = t'' - t'$ (between the times $t'$ and $t''$ we assume no restriction is being put on the region of integration). This can be seen either by repeated applications of (18) or directly from Eq. (15). Now we ask, as $\hbar \rightarrow 0$ what values of the intermediate coordinates $x_i$, contribute most strongly to the integral? These will be the values most likely to be found by experiment and therefore will determine, in the limit, the classical path. If $\hbar$ is very small, the exponent will be a very rapidly varying function of any of its variables $x_i$. As $x_i$, varies, the positive and negative contributions of the exponent nearly cancel. The region at which $x_i$, contributes most strongly is that at which the phase of the exponent varies least rapidly with $x_i$ (method of stationary phase). Call the sum in the exponent $S$;

$$S = \sum_{i=0}^{j-1} S(x_{i+1}, x_i). \quad (36)$$

Then the classical orbit passes, approximately, through those points $x_i$ at which the rate of change of $S$ with $x_i$, is small, or in the limit of small $\hbar$, zero, i.e., the classical orbit passes through the points at which $\partial S/\partial x_i$ for all $x_i$. Taking the limit $\epsilon \rightarrow 0$, (36) becomes in view of (11)

$$S = \int_{t'}^{t''} L(\dot{x}(t), x(t)) dt. \quad (37)$$

We see then that the classical path is that for which the integral (37) suffers no first-order change on varying the path. This is Hamilton's principle and leads directly to the Lagrangian equations of motion.

## 8. Operator Algebra

### Matrix Elements

Given the wave function and Schroedinger's equation, of course all of the machinery of operator or matrix algebra can be developed. It is, however, rather interesting to express these concepts in a somewhat different language more closely related to that used in stating the postulates. Little will be gained by this in elucidating operator algebra. In fact, the results are simply a translation of simple operator equations into a somewhat more cumbersome notation. On the other hand, the new notation and point of view are very useful in certain applications described in the introduction. Furthermore, the form of the equations permits natural extension to a wider

21

class of operators than is usually considered (e.g., ones involving quantities referring to two or more different times). If any generalization to a wider class of action functionals is possible, the formulae to be developed will play an important role.

We discuss these points in the next three sections. This section is concerned mainly with definitions. We shall define a quantity which we call a transition element between two states. It is essentially a matrix element. But instead of being the matrix element between a state $\psi$ and another $\chi$ corresponding to the *same* time, these two states will refer to different times. In the following section a fundamental relation between transition elements will be developed from which the usual commutation rules between coordinate and momentum may be deduced. The same relation also yields Newton's equation of motion in matrix form. Finally, in Section 10 we discuss the relation of the Hamiltonian to the operation of displacement in time.

We begin by defining a transition element in terms of the probability of transition from one state to another. More precisely, suppose we have a situation similar to that described in deriving (17). The region $R$ consists of a region $R'$ previous to $t'$, all space between $t'$ and $t''$ and the region $R''$ after $t''$. We shall study the probability that a system in region $R'$ is later found in region $R''$. This is given by (17). We shall discuss in this section how it changes with changes in the form of the Lagrangian between $t'$ and $t''$. In Section 10 we discuss how it changes with changes in the preparation $R'$ or the experiment $R''$.

The state at time $t'$ is defined completely by the preparation $R'$. It can be specified by a wave function $\psi(x', t')$ obtained as in (15), but containing only integrals up to the time $t'$. Likewise, the state characteristic of the experiment (region $R''$) can be defined by a function $\chi(x'', t'')$ obtained from (16) with integrals only beyond $t''$. The wave function $\psi(x'', t'')$ at time $t''$ can, of course, also be gotten by appropriate use of (15). It can also be gotten from $\psi(x', t')$ by (35). According to (17) with $t''$ used instead of $t$, the probability of being found in $\chi$ it prepared in $\psi$ is the square of what we shall call the transition amplitude $\int \chi^*(x'', t'') \psi(x'', t'') dx''$. We wish to express this in terms of $\chi$ at $t''$ and $\psi$ at $t'$. This we can do with the aid of (35). Thus, the chance that a system prepared in state $\psi_{t'}$ at time $t'$ will be found after $t''$ to be in a state $\chi_{t''}$ is the square of the transition amplitude

$$\langle \chi_{t''} | 1 | \psi_{t'} \rangle_S = \lim_{\epsilon \to 0} \int \dots \int \chi^*(x'', t'') \times \\ \times \exp(iS/\hbar) \psi(x', t') \frac{dx_0}{A} \dots \frac{dx_{j-1}}{A} dx_j, \quad (38)$$

22

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

Thus, transition elements such as (39) are important insofar as $F$ may arise in some way from a change $\delta S$ in an action expression. We denote, by observable functionals, those functionals $F$ which can be defined, (possibly indirectly) in terms of the changes which are produced by possible changes in the action $S$. The condition that a functional be observable is somewhat similar to the condition that an operator be Hermitian. The observable functionals are a restricted class because the action must remain a quadratic function of velocities. From one observable functional others may be derived, for example, by

$$\langle \chi_{t''} | F | \psi_{t'} \rangle_{S'} = \left\langle \chi_{t''} \left| F \exp \frac{i\epsilon}{\hbar} \sum_{i=1}^j U(x_i, t_i) \right| \psi_{t'} \right\rangle_S \quad (42)$$

which is obtained from (39).

Incidentally, (41) leads directly to an important perturbation formula. If the effect of $U$ is small the exponential can be expanded to first order in $U$ and we find

$$\langle \chi_{t''} | 1 | \psi_{t'} \rangle_{S'} = \left\langle \chi_{t''} | 1 | \psi_{t'} \right\rangle_S + \frac{i}{\hbar} \langle \chi_{t''} | \sum_i \epsilon U(x_i, t_i) | \psi_{t'} \right\rangle. \quad (43)$$

Of particular importance is the case that $\chi_{t''}$ is a state in which $\psi_{t'}$ would not be found at all were it not. for the disturbance, $U$ (i.e., $\langle \chi_{t''} | 1 | \psi_{t'} \rangle_S = 0$) Then

$$\frac{1}{\hbar^2} |\langle \chi_{t''} | \sum_i \epsilon U(x_i, t_i) | \psi_{t'} \rangle_S|^2 \quad (44)$$

is the probability of transition as induced to first order by the perturbation. In ordinary notation,

$$\langle \chi_{t''} | \sum_i \epsilon U(x_i, t_i) | \psi_{t'} \rangle_S = \int \left\{ \int \chi_{t''}^* e^{-(i/\hbar)\mathbf{H}(t''-t)} \mathbf{U} e^{-(i/\hbar)\mathbf{H}(t-t')} \psi_{t'} dx \right\} dt$$

so that (44) reduces to the usual expression $^{18}$ for time dependent perturbations.

## 9. Newton's Equations

### The Commutation Relation

In this section we find that different functionals may give identical results when taken between any two states. This equivalence between functionals

$^{18}$P. A. M. Dirac, *The Principles of Quantum Mechanics* (The Clarendon Press, Oxford, 1935), second edition, Section 47, Eq. (20)

24

is the statement of operator equations in the new language.

If $F$ depends on the various coordinates, we can, of course, define a new functional $\partial F/\partial x_k$ by differentiating it with respect to one of its variables, say $x_k (0 < k < j)$. If we calculate $\langle \chi_{t'} | \partial F/\partial x_k | \psi_{t'} \rangle_S$ by (39) the integral on the right-hand side will contain $\partial F/\partial x_k$. The only other place that the variable $x_k$ appears is in $S$. Thus, the integration on $x_k$ can be performed by parts. The integrated part vanishes (assuming wave functions vanish at infinity) and we are left with the quantity $-F(\partial/\partial x_k)\exp(iS/\hbar)$ in the integral. However, $(\partial/\partial x_k)\exp(iS/\hbar) = (i/\hbar)(\partial S/\partial x_k)\exp(iS/\hbar)$, so the right side represents the transition element of $-(i/\hbar)F(\partial S/\partial x_k)$, i.e.,

$$\left\langle \chi_{t'} \left| \frac{\partial F}{\partial x_k} \right| \psi_{t'} \right\rangle_S = -\frac{i}{\hbar} \left\langle \chi_{t'} \left| F \frac{\partial S}{\partial x_k} \right| \psi_{t'} \right\rangle_S. \tag{45}$$

This very important relation shows that two different functionals may give the same result for the transition element between any two states. We say they are equivalent and symbolize the relation by

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \frac{\partial S}{\partial x_k}, \tag{46}$$

the symbol $\underset{S}{\leftrightarrow}$ emphasizing the fact that functionals equivalent under one action may not be equivalent under another. The quantities in (46) need not be observable. The equivalence is, nevertheless, true. Making use of (36) one can write

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \left[ \frac{\partial S(x_{k+1}, x_k)}{\partial x_k} + \frac{\partial S(x_k, x_{k-1})}{\partial x_k} \right]. \tag{47}$$

This equation is true to zero and first order in $\epsilon$ and has as consequences the commutation relations of momentum and coordinate, as well as the Newtonian equations of motion in matrix form.

In the case of our simple one-dimensional problem, $S(x_{i+1}, x_i)$ is given by the expression (15), so that

$$\partial S(x_{k+1}, x_k)/\partial x_k = -m(x_{k+1} - x_k)/\epsilon,$$

and

$$\partial S(x_k, x_{k-1})/\partial x_k = +m(x_k - x_{k-1})/\epsilon - \epsilon V'(x_k);$$

where we write $V'(x)$ for the derivative of the potential, or force. Then (47) becomes

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \left[ -m \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - \epsilon V'(x_k) \right]. \tag{48}$$

25

If $F$ does not depend on the variable $x_k$, this gives Newton's equations of motion. For example, if $F$ is constant, say unity, (48) just gives (dividing by $\epsilon$)

$$0 \leftrightarrow_S -\frac{m}{\epsilon} \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - V'(x_k).$$

Thus, the transition element of mass times acceleration $[(x_{k+1} - x_k)/\epsilon - (x_k - x_{k-1})/\epsilon]/\epsilon$ between any two states is equal to the transition element of force $-V'(x_k)$ between the same states. This is the matrix expression of Newton's law which holds in quantum mechanics.

What happens if $F$ does depend upon $x_k$? For example, let $F = x_k$. Then (48) gives, since $\partial F/\partial x_k = 1$,

$$-\frac{\hbar}{i} \leftrightarrow_S x_k \left[ -m \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - \epsilon V'(x_k) \right]$$

or, neglecting terms of order $\epsilon$,

$$m \left( \frac{x_{k+1} - x_k}{\epsilon} \right) x_k - m \left( \frac{x_k - x_{k-1}}{\epsilon} \right) x_k \leftrightarrow_S \frac{\hbar}{i}. \quad (49)$$

In order to transfer an equation such as (49) into conventional notation, we shall have to discover what matrix corresponds to a quantity such as $x_k x_{k+1}$. It is clear from a study of (39) that if $F$ is set equal to, say, $f(x_k)g(x_{k+1})$, the corresponding operator in (40) is

$$e^{-(i/\hbar)(t'' - t - \epsilon)\mathbf{H}} g(\mathbf{x}) e^{-(i/\hbar)\epsilon\mathbf{H}} f(\mathbf{x}) e^{-(i/\hbar)(t - t')\mathbf{H}},$$

the matrix element being taken between the states $\chi_{t''}$ and $\psi_{t'}$. The operators corresponding to functions of $x_{k+1}$ will appear to the left of the operators corresponding to functions of $x_k$, i.e., *the order of terms in a matrix operator product corresponds to an order in time of the corresponding factors in a functional*. Thus, if the functional can and is written in such a way that in each term factors corresponding to later times appear to the left of factors corresponding to earlier terms, the corresponding operator can immediately be written down if the order of the operators is kept the same as in the functional. $^{19}$ Obviously, the order of factors in a functional is of no consequence. The ordering just facilitates translation into conventional operator notation. To write Eq. (49) in the way desired for easy translation

$^{19}$Dirac has also studied operators containing quantities referring to different times. See reference 2.

26

would require the factors in the second term on the left to be reversed in order. We see, therefore, that it corresponds to

$$\mathbf{px} - \mathbf{xp} = \hbar/i$$

where we have written $\mathbf{p}$ for the operator $m\hat{\mathbf{x}}$.

The relation between functionals and the corresponding operators is denned above in terms of the order of the factors in time. It should be remarked that this rule must be especially carefully adhered to when quantities involving velocities or higher derivatives are involved. The correct functional to represent the operator $(\dot{x})^2$ is actually $(x_{k+1} - x_k)/\epsilon(x_k - x_{k-1})/\epsilon$ rather than $[(x_{k+1} - x_k)/\epsilon]^2$. The latter quantity diverges as $1/\epsilon$ as $\epsilon \to 0$. This may be seen by replacing the second term in (49) by its value $x_{k+1} \cdot m(x_{k+1} - x_k)/\epsilon$ calculated an instant $\epsilon$ later in time. This does not change the equation to zero order in $\epsilon$. We then obtain (dividing by $\epsilon$)

$$\left(\frac{x_{k+1} - x_k}{\epsilon}\right)^2 \underset{S}{\leftrightarrow} -\frac{\hbar}{im\epsilon}. \tag{50}$$

This gives the result expressed earlier that the root mean square of the “velocity” $(x_{k+1} - x_k)/\epsilon$ between two successive positions of the path is of order $\epsilon^{-1/2}$.

It will not do then to write the functional for kinetic energy, say, simply as

$$\frac{1}{2}m[(x_{k+1} - x_k)/\epsilon]^2 \tag{51}$$

for this quantity is infinite as $\epsilon \to 0$. In fact, it is not an observable functional.

One can obtain the kinetic energy as an observable functional by considering the first-order change in transition amplitude occasioned by a change in the mass of the particle. Let $m$ be changed to $m(1 + \delta)$ for a short time, say $\epsilon$, around $t_k$. The change in the action is $\frac{1}{2}\delta\epsilon m[x_{k+1} - x_k)/\epsilon]^2$ the derivative of which gives an expression like (51). But the change in $m$ changes the normalization constant $1/A$ corresponding to $dx_k$ as well as the action. The constant is changed from $(2\pi\hbar\epsilon i/m)^{-1/2}$ to $(2\pi\hbar\epsilon i/m(1 + \delta))^{-1/2}$ or by $\frac{1}{2}\delta(2\pi\hbar\epsilon i/m)^{-1/2}$ to first order in $\delta$. The total effect of the change in mass in Eq. (38) to the first order in $\delta$ is

$$\langle\chi_{t'}|\frac{1}{2}\delta\epsilon im[(x_{k+1} - x_k)/\epsilon]^2/\hbar + \frac{1}{2}\delta|\psi_{t'}\rangle.$$

27

We expect the change of order $\delta$ lasting for a time $\epsilon$ to be of order $\delta\epsilon$. Hence, dividing by $\delta\epsilon i/\hbar$, we can define the kinetic energy functional as

$$\mathrm{K.E.} = \frac{1}{2}m[(x_{k+1} - x_k)/\epsilon]^2 + \hbar/2\epsilon i. \tag{52}$$

This is finite as $\epsilon \to 0$ in view of (50). By making use of an equation which results from substituting $m(x_{k+1} - x_k)/\epsilon$ for $F$ in (48) we can also show that the expression (52) is equal (to order $\epsilon$) to

$$\mathrm{K.E.} = \frac{1}{2}m\left(\frac{x_{k+1} - x_k}{\epsilon}\right)\left(\frac{x_k - x_{k-1}}{\epsilon}\right). \tag{53}$$

That is, the easiest way to produce observable functionals involving powers of the velocities is to replace these powers by a product of velocities, each factor of which is taken at a slightly different time.

## 10. The Hamiltonian

# **Momentum**

The Hamiltonian operator is of central importance in the usual formulation of quantum mechanics. We shall study in this section the functional corresponding to this operator. We could immediately define the Hamiltonian functional by adding the kinetic energy functional (52) or (53) to the potential energy. This method is artificial and does not exhibit the important relationship of the Hamiltonian to time. We shall define the Hamiltonian functional by the changes made in a state when it is displaced in time.

To do this we shall have to digress a moment to point out that the subdivision of time into *equal* intervals is not necessary. Clearly, any subdivision into instants $t_i$ will be satisfactory; the limits are to be taken as the largest spacing, $t_{i+1} - t_i$ approaches zero. The total action $S$ must now be represented as a sum

$$S = \sum_i S(x_{i+1}, t_{i+1}; x_i, t_i), \tag{54}$$

where

$$S(x_{i+1}, t_{i+1}; x_i, t_i) = \int_{t_i}^{t_i+1} L(\dot{x}(t), x(t)) dt, \tag{55}$$

28

the integral being taken along the classical path between $x_i$, at $t_i$ and $x_{i+1}$ at $t_{i+1}$. For the simple one-dimensional example this becomes, with sufficient accuracy,

$$S(x_{i+1}, t_{i+1}; x_i, t_i) = \left\{ \frac{m}{2} \left( \frac{x_{i+1} - x_i}{t_{i+1} - t_i} \right)^2 - V(x_{i+1}) \right\} (t_{i+1} - t_i); \quad (56)$$

the corresponding normalization constant for integration on $dx_i$ is $A = (2\pi\hbar i(t_{i+1} - t_i)/m)^{-1/2}$.

The relation of $H$ to the change in a state with displacement in time can now be studied. Consider a state $\psi(t)$ defined by a space-time region $R'$. Now imagine that we consider another state at time $t$, $\psi_\delta(t)$, denned by another region $R'_\delta$. Suppose the region $R'_\delta$ is exactly the same as $R'$ except that it is earlier by a time $\delta$, i.e., displaced bodily toward the past by a time $\delta$. All the apparatus to prepare the system for $R'_\delta$ is identical to that for $R'$ but is operated a time $\delta$ sooner. If $L$ depends explicitly on time, it, too, is to be displaced, i.e., the state $\psi_\delta$ is obtained from the $L$ used for state $\psi$ except that the time $t$ in $L_\delta$ is replaced by $t + \delta$. We ask how does the state $\psi_\delta$ differ from $\psi$? In any measurement the chance of finding the system in a fixed region $R''$ is different for $R'$ and $R'_\delta$. Consider the change in the transition element $\langle \chi | 1 | \psi_\delta \rangle_{S_\delta}$ produced by the shift $\delta$. We can consider this shift as effected by decreasing all values of $t_i$ by $\delta$ for $i \leq k$ and leaving all $t_i$ fixed for $i > k$, where the time $t$ lies in the interval between $t_{k+1}$ and $t_k$. $^{20}$ This change will have no effect on $S(x_{i+1}, t_{i+1}; x_i, t_i)$ as defined by (55) as long as both $t_{i+1}$ and $t_i$ are changed by the same amount. On the other hand, $S(x_{k+1}, t_{k+1}; x_k, t_k)$ is changed to $S(x_{k+1}, t_{k+1}; x_k, t_k - \delta)$. The constant $1/A$ for the integration on $dx_k$, is also altered to $(2\pi\hbar i(t_{k+1} - t_k + \delta)/m)^{-1/2}$. The effect of these changes on the transition element is given to the first order in $\delta$ by

$$\langle \chi | 1 | \psi \rangle_S - \langle \chi | 1 | \psi_\delta \rangle_{S_\delta} = \frac{i\delta}{\hbar} \langle \chi | H_k | \psi \rangle_S, \quad (57)$$

here the Hamiltonian functional $H_k$ is defined by

$$H_k = \frac{\partial S(x_{k+1}, t_{k+1}; x_k t_k)}{\partial t_k} + \frac{\hbar}{2i(t_{k+1} - t_k)}. \quad (58)$$

$^{20}$From the point of view of mathematical rigor, if $\delta$ is finite, as $\epsilon \rightarrow 0$ one gets into difficulty in that, for example, the interval $t_{k+1} - t_k$ is kept finite. This can be straightened out by assuming $\delta$ to vary with time and to be turned on smoothly before $t = t_k$ and turned off smoothly after $t = t_k$. Then keeping the time variation of $\delta$ fixed, let $\epsilon \rightarrow 0$. Then seek the first-order change as $\delta \rightarrow 0$. The result is essentially the same as that of the crude procedure used above.

29

The last term is due to the change in $1/A$ and serves to keep $H_k$ finite as $\epsilon \to 0$. For example, for the expression (56) this becomes

$$H_k = \frac{m}{2} \left( \frac{x_{k+1} - x_k}{t_{k+1} - t_k} \right) + \frac{\hbar}{2i(t_{k+1} - t_k)} + V(x_{k+1}),$$

which is just the sum of the kinetic energy functional (52) and that of the potential energy $V(x_{k+1})$.

The wave function $\psi_\delta(x, t)$ represents, of course, the same state as $\psi(x, t)$ will be after time $\delta$, i.e., $\psi(x, t + \delta)$. Hence, (57) is intimately related to the operator equation (31).

One could also consider changes occasioned by a time shift in the final state $\chi$. Of course, nothing new results in this way for it is only the relative shift of $\chi$ and $\psi$ which counts. One obtains an alternative expression

$$H_k = - \frac{\partial S(x_{k+1}, t_{k+1}; x_k, t_k)}{\partial t_{k+1}} + \frac{\hbar}{2i(t_{k+1} - t_k)}. \tag{59}$$

This differs from (58) only by terms of order $\epsilon$. The time rate of change of a functional can be computed by considering the effect of shifting both initial and final state together. This has the same effect as calculating the transition element of the functional referring to a later time. What results is the analog of the operator equation

$$\frac{\hbar}{i} \dot{\mathbf{f}} = \mathbf{H} \mathbf{f} - \mathbf{f} \mathbf{H}.$$

The momentum functional pt can be defined in an analogous way by considering the changes made by displacements of position:

$$\langle \chi | 1 | \psi \rangle_S - \langle \chi | 1 | \psi_\Delta \rangle_{S\Delta} = \frac{i\Delta}{\hbar} \langle \chi | p_k | \psi \rangle_S.$$

The state $\psi_\Delta$ is prepared from a region $R'_\Delta$ which is identical to region $R'$ except that it is moved a distance $\Delta$ in space. (The Lagrangian, if it depends explicitly on $x$, must be altered to $L_\Delta = L(\dot{x}, x - \Delta)$ for times previous to $t$.) One finds $^{21}$

$$p_k = \frac{\partial S(x_{k+1}, x_k)}{\partial x_{k+1}} = - \frac{\partial S(x_{k+1}, x_k)}{\partial x_k}. \tag{60}$$

$^{21}$We did not immediately substitute $p_i$ from (60) into (47) because (47) would then no longer have been valid to both zero order and the first order in $\epsilon$. We could derive the commutation relations, but not the equations of motion. The two expressions in (60) represent the momenta at each end of the interval $t_i$, to $t_{i+1}$. They differ by $\epsilon V'(x_{k+1})$ because of the force acting during the time $\epsilon$

30

Since $\psi_\Delta(x, t)$ is equal to $\psi(x - \Delta, t)$, the close connection between $p_k$ and the $x$-derivative of the wave function is established.

Angular momentum operators are related in an analogous way to rotations.

The derivative with respect to $t_{i+1}$ of $S(x_{i+1}, t_{i+1}; x_i, t_i)$ appears in the definition of $H_i$. The derivative with respect to $t_{i+1}$ defines $p_i$. But the derivative with respect to $t_{i+1}$ of $S(x_{i+1}, t_{i+1}; x_i, t_i)$ is related to the derivative with respect to $x_{i+1}$, for the function $S(x_{i+1}, t_{i+1}; x_i, t_i)$ defined by (55) satisfies the Hamilton-Jacobi equation. Thus, the Hamilton-Jacobi equation is an equation expressing $H_i$, in terms of the $p_i$. In other words, it expresses the fact that time displacements of states are related to space displacements of the same states. This idea leads directly to a derivation of the Schroedinger equation which is far more elegant than the one exhibited in deriving Eq. (30).

## 11. Inadequacies of the Formulation

The formulation given here suffers from a serious drawback. The mathematical concepts needed are new. At present, it requires an unnatural and cumbersome subdivision of the time interval to make the meaning of the equations clear. Considerable improvement can be made through the use of the notation and concepts of the mathematics of functionals. However, it was thought best to avoid this in a first presentation. One needs, in addition, an appropriate measure for the space of the argument functions $x(t)$ of the functionals.$^{22}$

It is also incomplete from the physical standpoint. One of the most important characteristics of quantum mechanics is its invariance under unitary transformations. These correspond to the canonical transformations of classical mechanics. Of course, the present formulation, being equivalent to ordinary formulations, can be mathematically demonstrated to be invariant under these transformations. However, it has not been formulated in such a way that it is *physically* obvious that it is invariant. This incompleteness shows itself in a definite way. No direct procedure has been outlined to

$^{22}$There are very interesting mathematical problems involved in the attempt to avoid the subdivision and limiting processes. Some sort of complex measure is being associated with the space of functions $x(t)$. Finite results can be obtained under unexpected circumstances because the measure is not positive everywhere, but the contributions from most of the paths largely cancel out. These curious mathematical problems are sidestepped by the subdivision process. However, one feels as Cavalieri must have felt calculating the volume of a pyramid before the invention of calculus.

31

describe measurements of quantities other than position. Measurements of momentum, for example, of one particle, can be defined in terms of measurements of positions of other particles. The result of the analysis of such a situation does show the connection of momentum measurements to the Fourier transform of the wave function. But this is a rather roundabout method to obtain such an important physical result. It is to be expected that the postulates can be generalized by the replacement of the idea of “paths in a region of space-time $R$” to “paths of class $R$,” or “paths having property $R$.” But which properties correspond to which physical measurements has not been formulated in a general way.

## 12. A Possibility Generalization

The formulation suggests an obvious generalization. There are interesting classical problems which satisfy a principle of least action but for which the action cannot be written as an integral of a function of positions and velocities. The action may involve accelerations, for example. Or, again, if interactions are not instantaneous, it may involve the product of coordinates at two different times, such as $\int x(t)x(t+T)dt$. The action, then, cannot be broken up into a sum of small contributions as in (10). As a consequence, no wave function is available to describe a state. Nevertheless, a transition probability can be defined for getting from a region $R'$ into another $R''$. Most of the theory of the transition elements $\langle \chi_{t''}|F|\psi_{t'} \rangle_S$ can be carried over. One simply invents a symbol, such as $\langle R''|F|R' \rangle_S$ by an equation such as (39) but with the expressions (19) and (20) for $\psi$ and $\chi$ substituted, and the more general action substituted for $S$. Hamiltonian and momentum functionals can be defined as in section (10). Further details may be found in a thesis by the author.$^{23}$

## 13. Application to Eliminate Field Oscillators

One characteristic of the present formulation is that it can give one a sort of bird's-eye view of the space-time relationships in a given situation. Before

$^{23}$The theory of electromagnetism described by J. A. Wheeler and R. P. Feynman, *Rev. Mod. Phys.* **17**, 157 (1945) can be expressed in a principle of least action involving the coordinates of particles alone. It was an attempt to quantize this theory, without reference to the fields, which led the author to study the formulation of quantum mechanics given here. The extension of the ideas to cover the case of more general action functions was developed in his Ph.D. thesis, “The principle of least action in quantum mechanics” submitted to Princeton University, 1942.

32

the integrations on the $x$, are performed in an expression such as (39) one has a sort of format into which various $F$ functionals may be inserted. One can study how what goes on in the quantum-mechanical system at different times is interrelated. To make these vague remarks somewhat more definite, we discuss an example.

In classical electrodynamics the fields describing, for instance, the interaction of two particles can be represented as a set of oscillators. The equations of motion of these oscillators may be solved and the oscillators essentially eliminated (Lienard and Wiechert potentials). The interactions which result involve relationships of the motion of one particle at one time, and of the other particle at another time. In quantum electrodynamics the field is again represented as a set of oscillators. But the motion of the oscillators cannot be worked out and the oscillators eliminated. It is true that the oscillators representing longitudinal waves may be eliminated. The result is instantaneous electrostatic interaction. The electrostatic elimination is very instructive as it shows up the difficulty of self-interaction very distinctly. In fact, it shows it up so clearly that there is no ambiguity in deciding what term is incorrect and should be omitted. This entire process is not relativistically invariant, nor is the omitted term. It would seem to be very desirable if the oscillators, representing transverse waves, could also be eliminated. This presents an almost insurmountable problem in the conventional quantum mechanics. We expect that the motion of a particle $a$ at one time depends upon the motion of $b$ at a previous time, and *vice versa*. A wave function $\psi(x_a, x_b; t)$, however, can only describe the behavior of both particles at one time. There is no way to keep track of what $b$ did in the past in order to determine the behavior of $a$. The only way is to specify the state of the set of oscillators at $t$, which serve to “remember” what $b$ (and $a$) had been doing.

The present formulation permits the solution of the motion of all the oscillators and their complete elimination from the equations describing the particles. This is easily done. One must simply solve for the motion of the oscillators before one integrates over the various variables $x_i$, for the particles. It is the integration over $x_i$, which tries to condense the past history into a single state function. This we wish to avoid. Of course, the result depends upon the initial and final states of the oscillator. If they are specified, the result is an equation for $\langle \chi_{t'} | 1 | \psi_{t'} \rangle$ like (38), but containing as a factor, besides $\exp(iS/\hbar)$ another functional $G$ depending only on the coordinates describing the paths of the particles.

We illustrate briefly how this is done in a very simple case. Suppose a particle, coordinate $x(t)$, Lagrangian $L(\dot{x}, x)$ interacts with an oscillator,

33

coordinate $g(t)$, Lagrangian $\frac{1}{2}(\dot{q}^2 - \omega^2 q^2)$ through a term $\gamma(x,t)q(t)$ in the Lagrangian for the system. Here $\gamma(x,t)$ is any function of the coordinate $x(t)$ of the particle and the time. $^{24}$ Suppose we desire the probability of a transition from a state at time $t'$, in which the particle's wave function is $\psi_{t'}$ and the oscillator is in energy level $n$, to a state at $t''$ with the particle in $\chi_{t''}$ and oscillator in level $m$. This is the square of

$$\langle \chi_{t''} \varphi_m | 1 | \psi_{t'} \varphi_n \rangle_{S_p + S_0 + S_I} = \int \dots \int \varphi_m^*(q_i) \chi_{t''}^*(x_i)$$

$$\times \exp \frac{i}{\hbar} (S_p + S_0 + S_1) \psi_{t'}(x_0) \varphi_n(q_0) \cdot \frac{dx_0}{A} \frac{dq_0}{a} \dots \frac{dx_{j-1}}{A} \frac{dq_{j-1}}{a} dx_i dq_i. \tag{61}$$

Here $\varphi_n(9q)$ is the wave function for the oscillator in state $n$, $S_p$ is the action

$$\sum_{i=0}^{j-1} S_p(x_{i+1}, x_i)$$

calculated for the particle as though the oscillator were absent,

$$S_0 = \sum_{i=0}^{j-1} \left[ \frac{\epsilon}{2} \left( \frac{q_{i+1} - q_i}{\epsilon} \right)^2 - \frac{\epsilon \omega^2}{2} q_{i+1}^2 \right]$$

that of the oscillator alone, and

$$S_I = \sum_{i=0}^{j-1} \gamma_i q_i$$

(where $\gamma_i = \gamma(x_i, t_i)$) is the action of interaction between the particle and the oscillator. The normalizing constant, $a$, for the oscillator is $(2\pi\epsilon i / \hbar)^{-1/2}$. Now the exponential depends quadratically upon all the $q_i$. Hence, the integrations over all the variables $q_i$, for $0 < i < j$ can easily be performed. One is integrating a sequence of Gaussian integrals.

The result of these integrations is, writing $T = t'' - t'$, $(2\pi i \hbar \sin \omega T / \omega)^{-1/2} \exp i (S_p + Q(q_i, q_0)) / \hbar$, where $Q(q_j, q_0)$ go) turns out to be just the classical

$^{24}$The generalization to the case that $\gamma$ depends on the velocity, $\dot{x}$, of the particle presents no problem.

34

action for the forced harmonic oscillator (see reference 15). Explicitly it is

$$\begin{array}{l} Q(q_{j},q_{0})=\frac{\omega}{2\sin\omega T}\left[(\cos\omega T)(q_{j}^{2}+q_{0}^{2})-2q_{j}q_{0}\right. \\ +\frac{2q_{0}}{\omega}\int_{t'}^{t''}\gamma(t)\sin\omega(t-t')dt+\frac{2q_{j}}{\omega}\int_{t'}^{t''}\gamma(t)\sin\omega(t''-t)dt \\ \left.-\frac{2}{\omega^{2}}\int_{t'}^{t''}\int_{t'}^{t}\gamma(t)\gamma(s)\sin\omega(t''-t)\times\sin\omega(s-t')dsdt\right]. \end{array}$$

It has been written as though $\gamma(t)$ were a continuous function of time. The integrals really should be split into Riemann sums and the quantity $\gamma(x_{i},t_{i})$ substituted for $\gamma(t_{i})$. Thus, $Q$ depends on the coordinates of the particle at all times through the $\gamma(x_{i},t_{i})$ and on that of the oscillator at times $t'$ and $t''$ only. Thus, the quantity (61) becomes

$$\begin{array}{l} \langle\chi_{t''}\varphi_{m}|1|\psi_{t'}\varphi_{n}\rangle_{Sp+S_{0}+S_{j}}=\int\dots\int\chi_{t''}^{*}(x_{i})G_{mn}\times \\ \times\exp\left(\frac{iS_{p}}{\hbar}\right)\psi_{t'}(x_{0})\frac{dx_{0}}{A}\dots\frac{dx_{j-1}}{A}dx_{i}=\langle\chi_{t''}|G_{mn}|\psi_{t'}\rangle_{S_{p}} \end{array}$$

which now contains the coordinates of the particle only, the quantity $G_{mn}$ being given by

$$G_{mn}=(2\pi i\hbar\sin\omega T/\omega)^{-1/2}\int\int\varphi_{m}^{*}(q_{i})\times\exp(iQ(q_{i},q_{0})/\hbar)\varphi_{n}(q_{0})dq_{j}dq_{0}.$$

Proceeding in an analogous manner one finds that all of the oscillators of the electromagnetic field can be eliminated from a description of the motion of the charges.

## Statistical Mechanics

### Spin and Relativity

Problems in the theory of measurement and statistical quantum mechanics are often simplified when set up from the point of view described here. For example, the influence of a perturbing measuring instrument can be integrated out in principle as we did in detail for the oscillator. The statistical density matrix has a fairly obvious and useful generalization. It results from considering the square of (38). It is an expression similar to (38) but containing integrations over two sets of variables $dx_{i}$, and $dx_{i}'$. The exponential

35

is replaced by $\exp i(S - S')/\hbar$, where $S'$ is the same function of the $x_i'$ as $S$ is of $x_i$. It is required, for example, to describe the result of the elimination of the field oscillators where, say, the final state of the oscillators is unspecified and one desires only the sum over all final states $m$.

Spin may be included in a formal way. The Pauli spin equation can be obtained in this way: One replaces the vector potential interaction term in $S(x_{i+1}, x_i)$,

$$\frac{e}{2c}(\mathbf{x}_{i+1} - \mathbf{x}_i) \cdot \mathbf{A}(\mathbf{x}_i) + \frac{e}{2c}(\mathbf{x}_{i+1} - \mathbf{x}_i) \cdot \mathbf{A}(\mathbf{x}_{i+1})$$

arising from expression (13) by the expression

$$\frac{e}{2c}(\sigma \cdot (\mathbf{x}_{i+1} - \mathbf{x}_i))(\sigma \cdot \mathbf{A}(\mathbf{x}_i)) + \frac{e}{2c}(\sigma \cdot \mathbf{A}(\mathbf{x}_{i+1}))(\sigma \cdot (\mathbf{x}_{i+1} - \mathbf{x}_i)).$$

Here $\mathbf{A}$ is the vector potential, $\mathbf{x}_{i+1}$ and $\mathbf{x}$, the vector positions of a particle at times $t_{i+1}$ and $t_i$, and $\sigma$ is Pauli's spin vector matrix. The quantity $\Phi$ must now be expressed as $\Pi_i \exp i S(x_{i+1}, x_i)/\hbar$ for this differs from the exponential of the sum of $S(x_{i+1}, x_i)$. Thus, $\Phi$ is now a spin matrix.

The Klein Gordon relativistic equation can also be obtained formally by adding a fourth coordinate to specify a path. One considers a "path" as being specified by four functions $x^{(\mu)}(\tau)$ of a parameter $\tau$. The parameter $\tau$ now goes in steps $\epsilon$ as the variable $t$ went previously. The quantities $x^{(1)}(t), x^{(2)}(t), x^{(3)}(t)$ are the space coordinates of a particle and $x^{(4)}(t)$ is a corresponding time. The Lagrangian used is

$$\sum_{\mu=1}^{t} [(dx^\mu/d\tau)^2 + (e/c)(dx^\mu/d\tau)\mathbf{A}_\mu],$$

where $A_\mu$ is the 4-vector potential and the terms in the sum for $\mu = 1, 2, 3$ are taken with reversed sign. If one seeks a wave function which depends upon $\tau$ periodically, one can show this must satisfy the Klein Gordon equation. The Dirac equation results from a modification of the Lagrangian used for the Klein Gordon equation, which is analogous to the modification of the non-relativistic Lagrangian required for the Pauli equation. What results directly is the square of the usual Dirac operator.

These results for spin and relativity are purely formal and add nothing to the understanding of these equations. There are other ways of obtaining the Dirac equation which offer some promise of giving a clearer physical interpretation to that important and beautiful equation.

The author sincerely appreciates the helpful advice of Professor and Mrs. H. C. Corben and of Professor H. A. Bethe. He wishes to thank Professor J. A. Wheeler for very many discussions during the early stages of the work.

36
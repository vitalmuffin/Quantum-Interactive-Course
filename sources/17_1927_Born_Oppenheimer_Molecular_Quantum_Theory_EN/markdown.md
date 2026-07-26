# On the Quantum Theory of Molecules

M. Bornᵃ, J.R. Oppenheimerᵇ

ᵃInstitute of Theoretical Physics, Göttingen

ᵇInstitute of Theoretical Physics, Göttingen

# Abstract

It will be shown that the familiar components of the terms of a molecule; the energy of electronic motion, of the nuclear vibration and of the rotation, correspond systematically to the terms of a power series in the fourth root of the ratio of electron mass to (average) nuclear mass. The treatment yields among other things an equation for the rotation, which represents a generalization of the treatment of Kramers and Pauli (top with built-in fly-wheel). Furthermore, there appears a justification of the considerations of Franck and Condon on the intensity of band lines. The relationships are illustrated for the diatomic molecule.

# Introduction

The terms of molecular spectra are usually made up of parts of various orders of magnitude; the largest contribution comes from the electronic motion about the nuclei, then follows the contribution of the nuclear vibration, and finally that from the nuclear rotation. The basis for the possibility of such a classification obviously rests in the comparative magnitudes of nuclear and electronic masses. From the standpoint of the old quantum theory, which computed stationary states with the aid of classical mechanics, this is the concept applied by Born and Heisenberg [1]; it was shown that the energy terms appear as the terms of increasing order with respect to the ratio $\sqrt{m/M}$, where m is the electronic mass and M an average nuclear mass. Thereby, however, nuclear rotation and vibration both appear in the second order, which contradicts empirical findings (for small rotational quantum numbers).

Here the problem will be approached anew from the standpoint of quantum mechanics.¹ It then becomes necessary to make our development with respect to $(m/M)^{1/4}$ rather than with respect to $\sqrt{m/M}$, so as to obtain the natural order of energy terms. The considerations also become much simpler and more transparent than in the old theory. The nuclear vibrations correspond to terms of second order and the rotations to fourth order in the energy, while the first and third order terms vanish. The absence of the first order terms is related to the existence of an equilibrium position of the nuclei, in which the electronic energy for stationary nuclei is at a minimum. The fourth order terms for the rotational motion illustrate the generalization of the treatment of Kramers and Pauli [2] in which the the behaviour of a molecule is compared to that of a top with a built-in fly-wheel. In order to determine the eigenfunctions and thereby the transition probabilities only to the zeroth approximation, the energy calculation must be carried out to terms of fourth order (rotations). One obtains expressions for the probabilities of simultaneous jumps of electronic, vibrational and rotational quantum number through which the representations developed by Franck [3] and elaborated by Condon [4] may be given precise interpretation.

Published originally as Annalen der Physik, 84, 457-484 (1927)

Translated by S M Blinder with emendations by Brian Sutcliffe and Wolf Geppert

¹Through the discussion of the basis of this work with us, Dr. P. Jordan has helped us with valuable comments, for which we express our thanks.

The approximations to higher than fourth order will not be treated in this work; they correspond to coupling among the three basic types of motion. A calculation of this effect is only meaningful for simultaneous consideration of all degeneracies of electronic motion for stationary nuclei, especially the Heisenberg resonance degeneracy which arises from the equivalence of electrons (also possibly of some nuclei) and in diatomic molecules, from the degeneracy of the eigenrotation about the internuclear axis; these complicated considerations will be forgone here.

As an example we will consider diatomic molecules in detail, using not only the general method but also another utilising the separation of variables in which the rotation becomes significant even in the zeroth order approximation, as Born and Hückel [5] have done it in the older quantum theory.

## Part I. Notation and Definitions

We denote the mass and rectangular coordinates of the electrons by $m, x_k, y_k, z_k$ and of the nuclei by $M_l, X_l, Y_l, Z_l$. Letting $M$ be any average value of the $M_l$, we set

$$\kappa = \left(\frac{m}{M}\right)^{1/4} \tag{1}$$

and

$$M_l = \frac{M}{\mu_l} = \frac{m}{\kappa^4 \mu_l}; \tag{2}$$

the $\mu_l$ being dimensionless numbers of order of magnitude 1. Let the potential energy of the system be

$$U(x_1, y_1, z_1, x_2, y_2, z_2, \dots; X_1, Y_1, Z_1, X_2, Y_2, Z_2, \dots) = U(x, X) \tag{3}$$

where we denote by $x$ the totality of electronic coordinates and by $X$, that of the nuclear coordinates. The function $U$ depends only on the relative positions of the particles; however, we make no use of its particular form (Coulomb's law). The kinetic energy of the electrons is represented by the operator

$$T_E = -\frac{h^2}{8\pi^2 m} \sum_x \sum_k \frac{\partial^2}{\partial x_k^2} \tag{4}$$

where the symbol $\sum_x$ denotes the sum which arises from the above expression by cyclic permutation of $x, y$ and $z$.

The kinetic energy of the nuclei is

$$T_K = -\kappa^4 \frac{h^2}{8\pi^2 m} \sum_x \sum_l \mu_l \frac{\partial^2}{\partial X_l^2}. \tag{5}$$

The total energy is represented by the operator

$$H = H_0 + \kappa^4 H_1 \tag{6}$$

where

$$T_E + U = H_0 \left(x, \frac{\partial}{\partial x}; X\right)$$

$$T_K = \kappa^4 H_1 \left(\frac{\partial}{\partial X}\right). \tag{7}$$

We introduce now, in place of the rectangular coordinates of the nuclei, $3N - 6$ functions

$$\xi_i = \xi_i(X) \tag{8}$$

2

which denote the relative positions of the nuclei with respect to one another, and 6 functions

$$\theta_i = \theta_i(X) \tag{9}$$

which determine the position and orientation of the nuclear configuration in space. One can in a symmetrical fashion introduce the rectangular coordinates $\bar{X}_l$, $\bar{Y}_l$, $\bar{Z}_l$ of the nuclei relative to the instantaneous principal axes of inertia; between these there are 6 relations:

$$\sum_l M_l \bar{X}_l = 0 \cdots \sum_l M_l \bar{Y}_l \bar{Z}_l = 0 \cdots$$

One can thus express the $\bar{X}_l$ by the $3N - 6$ independent parameters $\xi_1, \xi_2, \ldots$:

$$\bar{X}_l = \bar{X}_l(\xi), \ldots$$

There then exist transformations between the original and the new coordinates, of the form

$$X_l = X_0 + \sum_y \alpha_{xy}(\theta, \phi, \psi) \bar{Y}_l(\xi); \tag{10}$$

$X_0, Y_0, Z_0$ are the coordinates of the center of mass and the $\alpha_{xy}$ are the coefficients of the orthogonal rotation matrix, and are thus known functions of the Eulerian angles $\theta, \phi, \psi$. The quantities $X_0, Y_0, Z_0, \theta, \phi, \psi$ are the functions denoted by $\theta_i$ in (9). By (10), the $X_l$ are determined as functions of the $\theta_i$ and $\xi_i$; by solving, one obtains the expressions (8) and (9).$^2$

This transformation does not, of course, separate the energy $H$ into parts corresponding to translation, rotation and relative motion of the nuclei. However one can separate $H_1$ into three parts:

$$H_1 = H_{\xi\xi} + H_{\xi\theta} + H_{\theta\theta}; \tag{11}$$

$H_{\xi\xi}$ is linear homogeneous in the $\frac{\partial^2}{\partial \xi_i \partial \xi_j}$; $H_{\xi\theta}$ contains the $\frac{\partial}{\partial \xi_i}$; $H_{\theta\theta}$ is independent of all derivatives with respect to the $\xi_i$. One can make further generalizations about these operators. If we apply the entire operator $H_1$ to an arbitrary function $f(\xi)$ of the relative nuclear coordinates $\xi_i$, the resulting quantity $H_1 f(\xi)$ must be independent of the position in space, hence of the $\theta_i$. In particular, in $H_{\xi\xi}$ the coefficients of the $\frac{\partial^2}{\partial \xi_i \partial \xi_j}$ cannot depend on the $\theta_i$. In contrast, these do appear in $H_{\xi\theta}$, associated with the $\frac{\partial}{\partial \xi_i}$, the $\xi_i$, $\theta_i$ and $\frac{\partial}{\partial \theta_i}$; in $H_{\theta\theta}$ associated with $\frac{\partial^2}{\partial \theta_i \partial \theta_j}$ the $\frac{\partial}{\partial \theta_i}$, $\xi_i$ and $\theta_i$.

We will consider these operators explicitly for diatomic molecules.

The mechanical problem we must solve is

$$(H_0 + \kappa^4 H_1 - W)\psi = 0. \tag{12}$$

We will show that any arbitrary solution which corresponds to a combination of nuclei and electrons forming a stable molecule can be found by a development in a power series in $\kappa$.

# Part II. Electronic Motion for Stationary Nuclei

If one sets $\kappa = 0$ in (12) one obtains a differential equation in the $x_k$ alone, the $X_l$ appearing as parameters:

$$\left\{ H_0 \left( x, \frac{\partial}{\partial x}; X \right) - W \right\} \psi = 0. \tag{13}$$

$^2$It is of physical significance that this solution is in general made using ambiguous functions; compare [6].

3

This represents the electronic motion for stationary nuclei. We assume this eigenvalue problem is solved. The eigenvalues depend only on the functions $\xi_i$ of the $X_i$; then one can use the coordinate system defined by the principal axes of inertia, i.e. let $X_i = \bar{X}_i(\xi)$. In this system of axes, the eigenfunctions depend, besides on $x_k$, only on the $\xi_i$; however, if one transforms back to the arbitrary space-fixed axes, the $\theta_i$ again become involved.

We designate the $n$th eigenvalue and the corresponding normalized eigenfunction as

$$W = V_n(\xi) \quad \psi = \phi_n(x; \xi, \theta) \tag{14}$$

so that the identity

$$\left\{ H_0 \left( x, \frac{\partial}{\partial x}; \xi, \theta \right) - V_n(\xi) \right\} \phi_n(x; \xi, \theta) = 0 \tag{15}$$

is valid. Here we assume that $V_n$ is a nondegenerate eigenvalue. As a matter of fact, this is never the case since the indistinguishability of the electrons introduces the resonance degeneracy, discovered by Heisenberg and Dirac; for diatomic molecules there is an additional degeneracy of the angular momentum about the axis. But since we are concerned here only with the systematics of the approximation procedure, we will not consider these degeneracies. Their consideration would result in secular equations in the higher approximation.

The most important goal of our investigation is the proof that the function $V_n(\xi)$ plays the role of a potential for the nuclear motion. For this we must have several auxiliary formulas which will be derived now. It is necessary to show that the matrix corresponding to the derivative of the operator $H_0(x, \frac{\partial}{\partial x}; \xi, \theta)$ with respect to $\xi_i$, (for constant $x, \frac{\partial}{\partial x}$) can be related to the derivative of the function $V_n(\xi)$.

Instead of taking the derivative with respect to the $\xi_i$ directly, we replace the $\xi_i$ by $\xi_i + \kappa\zeta_i$ and differentiate with respect to $\kappa$; the coefficient of a power of $\kappa$ is then a homogeneous polynomial in $\zeta_i$, these coefficients being derivatives with respect to $\xi_i$. Thus we write

$$V_n(\xi + \kappa\zeta) = V_n^{(0)} + \kappa V_n^{(1)} + \kappa^2 V_n^{(2)} + \dots, \tag{16}$$

where

$$\begin{array}{l} \text{a)} \quad V_n^{(0)} = V_n(\xi) \\ \text{b)} \quad V_n^{(1)} = \sum_i \zeta_i \frac{\partial V_n}{\partial \xi_i} \\ \text{c)} \quad V_n^{(2)} = \frac{1}{2} \sum_{ij} \zeta_i \zeta_j \frac{\partial^2 V_n}{\partial \xi_i \partial \xi_j}, \end{array} \tag{17}$$

...

and correspondingly

$$\begin{array}{l} H_0 = H_0^{(0)} + \kappa H_0^{(1)} + \kappa^2 H_0^{(2)} + \dots \\ \phi_n = \phi_n^{(0)} + \kappa \phi_n^{(1)} + \kappa^2 \phi_n^{(2)} + \dots \\ \dots \dots \dots \dots \dots \end{array} \tag{18}$$

One can now develop the quantities $\phi_n^{(1)}, \phi_n^{(2)}$ in the eigenfunctions $\phi_n^{(0)}(x; \xi, \theta)$, setting

$$\begin{array}{l} \text{a)} \quad \phi_n^{(1)} = \sum_{n'} u_{nn'}^{(1)} \phi_{n'}^{(0)}, \\ \text{b)} \quad \phi_n^{(2)} = \sum_{n'} u_{nn'}^{(2)} \phi_{n'}^{(0)}. \end{array} \tag{19}$$

4

Thus $u_{nn'}^{(r)}$ is a homogeneous polynomial of the $r$th order in $\zeta_i$, for instance

$$u_{nn'}^{(1)} = \sum_i \zeta_i \int \overline{\phi_{n'}^{(0)}} \frac{\partial \phi_n^{(0)}}{\partial \xi_i} \mathrm{d}x$$

$$u_{nn'}^{(2)} = \sum_{ij} \zeta_i \zeta_j \int \overline{\phi_{n'}^{(0)}} \frac{\partial^2 \phi_n^{(0)}}{\partial \xi_i \partial \xi_j} \mathrm{d}x. \tag{20}$$

These integrals, in which $\mathrm{d}x$ denotes the volume element in configuration space, are independent of the orientation of the nuclear system in space, hence independent of the $\theta_i$; one can thus evaluate them in the principal axis system.

If now, $F$ denotes any operator on the $x_i$, we define the $r$th order matrix element of $F$

$$\int \overline{\phi_{n'}^{(0)}} F \phi_n^{(r)} \mathrm{d}x = F_{nn'}^{(r)}. \tag{21}$$

For $r = 0$ this becomes the usual matrix element

$$F_{nn'}^{(0)} = F_{nn'} = \int \overline{\phi_{n'}^{(0)}} F \phi_n^{(0)} \mathrm{d}x. \tag{22}$$

In general, by (19),

$$F_{nn'}^{(r)} = \sum_{n''} u_{nn''}^{(r)} F_{n''n'}. \tag{23}$$

Using (15) for $\kappa = 0$

$$(H_0^{(0)} - V_n^{(0)})_{nn'}^{(r)} = u_{nn'}^{(r)} (V_{n'}^{(0)} - V_n^{(0)}). \tag{24}$$

Furthermore, we obtain by substituting (16) and (18) in (15), the following identities:

a) $(H_0^{(0)} - V_n^{(0)})\phi_n^{(1)} + (H_0^{(1)} - V_n^{(1)})\phi_n^{(0)} = 0$

b) $(H_0^{(0)} - V_n^{(0)})\phi_n^{(2)} + (H_0^{(1)} - V_n^{(1)})\phi_n^{(1)} + (H_0^{(2)} - V_n^{(2)})\phi_n^{(0)} = 0$

...

Multiplying these by $\overline{\phi_{n'}^{(0)}}$ and integrating over the $x_i$, by virtue of (24) we find:

a) $u_{nn'}^{(1)}(V_{n'}^{(0)} - V_n^{(0)}) + (H_0^{(1)})_{nn'} - V_n^{(1)}\delta_{nn'} = 0$

b) $u_{nn'}^{(2)}(V_{n'}^{(0)} - V_n^{(0)}) + (H_0^{(1)} - V_n^{(1)})_{nn'} + (H_0^{(2)})_{nn'} - V_n^{(2)}\delta_{nn'} = 0$

...

From these one can compute the $(H_0^{(1)})_{nn'}$, $(H_0^{(2)})_{nn'}$, ..., $i$e the matrix elements $\left(\frac{\partial H_0}{\partial \xi_i}\right)_{nn'}$, $\left(\frac{\partial^2 H_0}{\partial \xi_i \partial \xi_j}\right)_{nn'}$, ... We will later apply these formulas.$^3$

### Part III. Setting-up the Approximate Equations

An arbitrary configuration of electrons and nuclei cannot always be treated by a general approximation procedure. We will here consider only states which correspond to a stable molecule. We will begin with the following question:

$^3$The classical analogue to the simplest deduction from these formulae, namely the identity $(H_0^{(1)})_{nn} = V_n^{(1)}$ which follows from (26a) for $n = n'$, is found in [7]; compare especially with § 4, formula (11).

5

Is there a system of values of the relative nuclear coordinates $\xi_i$ such that the eigenfunctions $\psi_n$ of the energy operator (6), in so far as they depend on the $\xi_i$, have values significantly different from zero only in a small neighbourhood of this set?

This wave-mechanical requirement corresponds obviously to the classical condition that the nuclei undergo only small oscillations about the equilibrium configuration; the $|\psi_n|^2$ is the probability of finding a certain configuration of given energy.

We consider, as the unperturbed system, the electronic motion for an arbitrary but henceforth fixed nuclear configuration, $\xi_i$. We then develop all quantities with respect to small changes of the $\xi_i$, which we designate by $\kappa\zeta_i$; we presume then that the “domain” of oscillation is such that $\kappa$ is close to zero, an assumption which is only justified by its success.

We have then as in (18), part II, the development

$$H_0(x, \frac{\partial}{\partial x}; \xi + \kappa\zeta, \theta) = H_0^{(0)} + \kappa H_0^{(1)} + \kappa^2 H_0^{(2)} + \dots, \tag{27}$$

where

$$a) \quad H_0^{(0)} = H_0(x, \frac{\partial}{\partial x}; \xi),$$

$$b) \quad H_0^{(1)} = \sum_i \zeta_i \frac{\partial H_0}{\partial \xi_i}, \tag{28}$$

$$c) \quad H_0^{(2)} = \frac{1}{2} \sum_{ij} \zeta_i \zeta_j \frac{\partial^2 H_0}{\partial \xi_i \partial \xi_j},$$

and from (11) since $\frac{\partial}{\partial \xi} = \frac{1}{\kappa} \frac{\partial}{\partial \zeta}$

$$\kappa^4 H_1(X, \frac{\partial}{\partial X}) = \kappa^4 \left( \frac{1}{\kappa^2} H_{\zeta\zeta} + \frac{1}{\kappa} H_{\zeta\theta} + H_{\theta\theta} \right) \tag{29}$$

$$= \kappa^2 H_{\zeta\zeta}^{(0)} + \kappa^3 \left( H_{\zeta\theta}^{(0)} + H_{\zeta\zeta}^{(1)} \right) + \kappa^4 \left( H_{\theta\theta}^{(0)} + H_{\zeta\theta}^{(1)} + H_{\zeta\zeta}^{(2)} \right) + \dots$$

where

$$a) \quad H_{\zeta\zeta}^{(0)} = H_{\zeta\zeta}^{(0)}(\xi, \frac{\partial^2}{\partial \zeta_i \partial \zeta_j})$$

$$b) \quad H_{\zeta\zeta}^{(1)} = \sum_i \zeta_i \frac{\partial H_{\zeta\zeta}^{(0)}}{\partial \xi_i} \tag{30}$$

$$a) \quad H_{\zeta\theta}^{(0)} = H_{\zeta\theta}^{(0)}(\xi, \theta, \frac{\partial}{\partial \zeta}, \frac{\partial}{\partial \theta})$$

$$b) \quad H_{\zeta\theta}^{(1)} = \sum_i \zeta_i \frac{\partial H_{\zeta\theta}^{(0)}}{\partial \xi_i} \tag{31}$$

$$a) \quad H_{\theta\theta}^{(0)} = H_{\theta\theta}^{(0)}(\xi, \theta, \frac{\partial^2}{\partial \theta_i \partial \theta_j})$$

$$b) \quad H_{\theta\theta}^{(1)} = \sum_i \zeta_i \frac{\partial H_{\theta\theta}^{(0)}}{\partial \xi_i} \tag{32}$$

6

The arguments $\xi_i$ are hereafter to be considered constants.

The total energy operator is then

$$\begin{array}{l} H = H_0 + \kappa H_0^{(1)} + \kappa^2 \left(H_0^{(2)} + H_{\zeta\zeta}^{(0)}\right) \\ + \kappa^3 \left(H_0^{(3)} + H_{\zeta\theta}^{(0)} + H_{\zeta\zeta}^{(1)}\right) \\ + \kappa^4 \left(H_0^{(4)} + H_{\theta\theta}^{(0)} + H_{\zeta\theta}^{(1)} + H_{\zeta\zeta}^{(2)}\right) + \dots \end{array} \tag{33}$$

The succeeding terms all have the same form and can be formed from the term in $\kappa^4$ by increasing the superscript by 1.

We also develop the desired eigenfunction and energy parameter with respect to $\kappa$ :

$$\begin{array}{l} \psi = \psi^{(0)} + \kappa\psi^{(1)} + \kappa^2\psi^{(2)} + \dots \\ W = W^{(0)} + \kappa W^{(1)} + \kappa^2 W^{(2)} + \dots \end{array} \tag{34}$$

We then obtain the following approximation equations:

$$\begin{array}{l} a) \quad (H_0^{(0)} - W^{(0)})\psi^{(0)} = 0 \\ b) \quad (H_0^{(0)} - W^{(0)})\psi^{(1)} = (W^{(1)} - H_0^{(1)})\psi^{(0)} \\ c) \quad (H_0^{(0)} - W^{(0)})\psi^{(2)} = (W^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)})\psi^{(0)} + (W^{(1)} - H_0^{(1)})\psi^{(1)} \\ d) \quad (H_0^{(0)} - W^{(0)})\psi^{(3)} = (W^{(3)} - H_0^{(3)} - H_{\zeta\theta}^{(0)} - H_{\zeta\zeta}^{(1)})\psi^{(0)} \\ \quad + (W^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)})\psi^{(1)} + (W^{(1)} - H_0^{(1)})\psi^{(2)} \end{array} \tag{35}$$

$$e) \quad (H_0^{(0)} - W^{(0)})\psi^{(4)} = (W^{(4)} - H_0^{(4)} - H_{\theta\theta}^{(0)} - H_{\zeta\theta}^{(1)} - H_{\zeta\zeta}^{(2)})\psi^{(0)} \\ \quad + (W^{(3)} - H_0^{(3)} - H_{\zeta\theta}^{(0)} - H_{\zeta\zeta}^{(1)})\psi^{(1)} \\ \quad + (W^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)})\psi^{(2)} + (W^{(1)} - H_0^{(1)})\psi^{(3)} \\ \dots \dots \dots \dots \dots \dots$$

### Part IV. Solution of the Approximate Equations of zeroth and first Order: Equilibrium of the Nuclei

The zeroth order equation (35a) describes the electronic motion for stationary nuclei as discussed in Part II. From the normalized eigensolution $\phi_n^{(0)}(x; \xi, \theta)$ belonging to the eigenvalue $V_n^{(0)} = V_n(\xi)$, we find the general solution in the form:

$$\psi_n^{(0)} = \chi_n^{(0)}(\zeta, \theta)\phi_n^{(0)}(x; \xi, \theta) \tag{36}$$

where $\chi_n^{(0)}$ is an, as yet, arbitrary function of the arguments $\zeta_i, \theta_j$; this must be included in order to enable solutions of the following approximation equations.

The following approximation equation (35b)

$$(H_0^{(0)} - W^{(0)})\psi^{(1)} = (W^{(1)} - H_0^{(1)})\psi^{(0)} \tag{37}$$

is soluble only when the right-hand side is orthogonal to $\psi_n^{(0)}$ (relative to the electronic coordinates $x_i$).$^4$

This gives the condition

$$\left\{\left(H_0^{(1)}\right)_{nn} - W^{(1)}\right\}\chi_n^{(0)}(\zeta, \theta) = 0 \tag{38}$$

$^4$We define the orthogonality of two functions $f(x)$ and $g(x)$ by $\int \overline{f(x)}g(x)\mathrm{d}x = 0$.

7

where $\left(H_{0}^{(1)}\right)_{nn}$ is the diagonal matrix element of the operator $H_{0}^{(1)}$ relative to the $x_{i}$, thus by (28b) a homogeneous linear function of $\zeta_{i}$. This must however, by (38), be constant, since $\chi_{n}^{(0)}(\zeta,\theta)$ cannot vanish identically without the same being true for $\psi_{n}^{(0)}$.

Thus it follows that

$$W^{(1)} = 0, \quad \left(H_{0}^{(1)}\right)_{nn} = 0. \tag{39}$$

From (26a) and (17) we have however

$$\left(H_{0}^{(1)}\right)_{nn} = V_{n}^{(1)} = \sum_{i} \zeta_{i} \frac{\partial V_{n}}{\partial \xi_{i}}.$$

Thus:

$$\frac{\partial V_{n}}{\partial \xi_{i}} = 0. \tag{40}$$

The validity of continuing our approximation procedure requires that the relative nuclear coordinates $\xi_{i}$ must not be arbitrarily chosen, but must correspond to an extremum of the electronic energy $V_{n}(\xi)$. The existence of this is therefore the condition for the existence of the molecule, a law which is usually assumed to be self-evident. We will show later that it must necessarily be a minimum as well.

The function $\chi_{n}^{(0)}(\zeta,\theta)$ remains, as yet, undetermined. Setting in (37) $W_{n}^{(0)} = V_{n}(\xi)$, $W_{n}^{(1)} = 0$ and $\psi_{n}^{(0)} = \chi_{n}^{(0)}\phi_{n}^{(0)}$ we find the equation which determines $\phi_{n}^{(1)}$

$$\left(H_{0}^{(0)} - V_{n}^{(0)}\right)\psi_{n}^{(1)} = -H_{0}^{(1)}\phi_{n}^{(0)}\chi_{n}^{(0)}. \tag{41}$$

A solution of this by (25a) is $\psi_{n}^{(1)} = \chi_{n}^{(0)}\phi_{n}^{(1)}$ where $\phi_{n}^{(1)}$ is the function (19a) defined by (18). The general solution is obtained by adding a solution $\phi_{n}^{(0)}$ of the homogeneous equation with the yet undetermined factor $\chi_{n}^{(1)}(\xi,\theta)$:

$$\psi_{n}^{(1)} = \chi_{n}^{(0)}\phi_{n}^{(1)} + \chi_{n}^{(1)}\phi_{n}^{(0)}. \tag{42}$$

### Part V. Solution of the Approximate Equations of second and third Order:Nuclear Vibration

We now reach the approximation equation (35c), which after substitution of the solutions for the lower order approximations is

$$\begin{array}{l} \left(H_{0}^{(0)} - V_{n}^{(0)}\right)\psi_{n}^{(2)} = \left(W_{n}^{(2)} - H_{0}^{(2)} - H_{\zeta\zeta}^{(0)}\right)\chi_{n}^{(0)}\phi_{n}^{(0)} \\ \quad - H_{0}^{(1)}\left(\chi_{n}^{(0)}\phi_{n}^{(1)} + \chi_{n}^{(1)}\phi_{n}^{(0)}\right). \tag{43} \end{array}$$

In order for this to be solvable, the right-hand side must again be orthogonal to $\phi_{n}^{(0)}$; using the notation of part II this yields, because of (39):

$$\left\{\left(H_{0}^{(2)} + H_{\zeta\zeta}^{(0)}\right)_{nn} + \left(H_{0}^{(1)}\right)_{nn} - W_{n}^{(2)}\right\}\chi_{n}^{(0)} = 0.$$

It follows from (26b) with $V_{n}^{(1)} = 0$ that

$$\left(H_{0}^{(2)}\right)_{nn} + \left(H_{0}^{(1)}\right)_{nn}^{(1)} = V_{n}^{(2)}. \tag{44}$$

Since $H_{\zeta\zeta}^{(0)}$ by (30a) is seen to be independent of the $x_{k}$ we find:

$$\left\{H_{\xi\xi}^{(0)} + V_{n}^{(2)} - W_{n}^{(2)}\right\}\chi_{n}^{(0)} = 0. \tag{45}$$

Noting the meanings of $H_{\zeta\zeta}^{(0)}$ and $V_{n}^{(2)}$ given by (17c) and (30a) we see that (45) represents the equation for harmonic nuclear vibration:

$$\left\{H_{\zeta\zeta}^{(0)}\left(\xi_{i}\frac{\partial^{2}}{\partial\zeta_{i}\partial\zeta_{j}}\right) + \frac{1}{2}\sum_{ij}\zeta_{i}\zeta_{j}\frac{\partial^{2}V_{n}}{\partial\xi_{i}\partial\xi_{j}} - W_{n}^{(2)}\right\}\chi_{n}^{(0)} = 0. \tag{46}$$

8

This equation shows that the function $V_n(\xi)$ plays the role of a potential energy for the nuclei, up to terms of 2nd order. For the existence of a stable molecule there is a further condition that the extremum of $V_n(\xi)$ determined by (40) must be a minimum; then the quadratic form $V_n^{(2)}$ must be positive definite, thereby all degrees of freedom $\zeta_i$ stable and oscillating about the equilibrium configuration are possible. It is known that the equation for the vibration (46) is separable through a linear transformation of the $\zeta_i$ to normal coordinates $\eta_i$. If $\sigma_{ns}^{(0)}(\zeta)$ be the normalized eigensolution of (46) belonging to the eigenvalue $W_{ns}^{(2)}$, the general solution is

$$\begin{array}{l} a) \quad W^{(2)} = W_{ns}^{(2)}, \quad \chi_n^{(0)} = \chi_{ns}^{(0)}, \text{ where} \\ b) \quad \chi_{ns}^{(0)} = \rho_{ns}^{(0)}(\theta)\sigma_{ns}^{(0)}(\zeta). \end{array} \tag{47}$$

The index $s$ thus represents the set of vibrational quantum numbers. $\rho_{ns}^{(0)}$ is an, as yet, undetermined function of the $\theta_i$, the introduction of which is necessary for the continuation of the procedure.

It is known that $\sigma_{ns}^{(0)}(\zeta)$ is a linear combination of products of orthogonal Hermite functions for the individual normal coordinates $\eta_i$; these functions have the property that they approach zero very rapidly (exponentially) outside the limit of classical vibration. So our substitution of $(\xi + \kappa\zeta)$ is justified since it indeed leads to a solution, with regard to the $\xi$-oscillation within the limit, which vanish with $\kappa$. We apply the further property of the orthogonal Hermite functions that they are either even or odd functions of their argument.

Let $\Phi$ be any operator on the $\zeta_i$. We can then construct the corresponding matrix

$$\Phi_{nn'}_{ss'} = \int \overline{\sigma_{n's'}^{(0)}}\Phi\sigma_{ns}^{(0)}\mathrm{d}\zeta \tag{48}$$

where $\mathrm{d}\zeta$ is the volume element in the space of the $\zeta_i$.

In order to solve equation (43) we substitute on the right-hand side, using (45),

$$\left(W_{ns}^{(2)} - H_{\zeta\zeta}^{(0)}\right)\chi_{ns}^{(0)} = V_n^{(2)}\chi_{ns}^{(0)};$$

(43) then becomes:

$$\left(H_0^{(0)} - V_n^{(0)}\right)\psi_n^{(2)} = \left(V_n^{(2)} - H_0^{(2)}\right)\chi_{ns}^{(0)}\phi_n^{(0)} - H_0^{(1)}\left(\chi_{ns}^{(0)}\phi_n^{(1)} + \chi_{ns}^{(1)}\phi_n^{(0)}\right). \tag{49}$$

The general solution is

$$\psi_n^{(2)} = \chi_{ns}^{(0)}\phi_n^{(2)} + \chi_{ns}^{(1)}\phi_n^{(1)} + \chi_{ns}^{(2)}\phi_n^{(0)}, \tag{50}$$

where $\chi_{ns}^{(2)}$ denotes a new, undetermined function of the $\zeta_i, \theta_i$; this is easily verified using the identities (25).

We now consider the approximation equation of 3rd order (35d); after substitution of the already determined quantities, this becomes:

$$\begin{array}{l} \left(H_0^{(0)} - V_n^{(0)}\right)\psi_n^{(3)} = \left(W^{(3)} - H_0^{(3)} - H_{\zeta\theta}^{(0)} - H_{\zeta\zeta}^{(1)}\right)\chi_{ns}^{(0)}\phi_n^{(0)} \\ + \quad \left(W_{ns}^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)}\right)\left(\chi_{ns}^{(0)}\phi_n^{(1)} + \chi_{ns}^{(1)}\phi_n^{(0)}\right) \\ - \quad H_0^{(1)}\left(\chi_{ns}^{(0)}\phi_n^{(2)} + \chi_{ns}^{(1)}\phi_n^{(1)} + \chi_{ns}^{(2)}\phi_n^{(0)}\right). \end{array} \tag{51}$$

We may consider the right-hand side as a development in the $\phi_n^{(0)}$; we write

$$\left(H_0^{(0)} - V_n^{(0)}\right)\psi_n^{(3)} = W^{(3)}\chi_{ns}^{(0)}\phi_n^{(0)} - \sum_{n'} F_{nn'}^{(3)}\phi_{n'}^{(0)}, \tag{52}$$

where

$$F_{nn'}^{(3)} = F_{nn'}^{(3,1)}\chi_{ns}^{(2)} + F_{nn'}^{(3,2)}\chi_{ns}^{(1)} + F_{nn'}^{(3,3)}\chi_{ns}^{(0)}; \tag{53}$$

9

where the $F$ are operators on $\zeta$ and $\theta$, and

$$\begin{aligned} a) & F_{nn'}^{(3,1)} = \left(H_0^{(1)}\right)_{nn'} \\ b) & F_{nn'}^{(3,2)} = \left(H_{\zeta\zeta}^{(0)} - H_0^{(2)} - W_{ns}^{(2)}\right)_{nn'} + \left(H_0^{(1)}\right)_{nn'}^{(1)}, \end{aligned} \tag{54}$$

we can say about $F_{nn'}^{(3,3)}$ only that it is a homogeneous function of 3rd degree in the $\xi_i$ and the $\partial/\partial\zeta_i$.

If (52) is solvable, we must have

$$W^{(3)}\chi_{ns}^{(0)} - F_{nn}^{(3)} = 0$$

because of (53) and (54a)

$$F_{nn}^{(3,2)}\chi_{ns}^{(1)} = \left(W^{(3)} - F_{nn}^{(3,3)}\right)\chi_{ns}^{(0)}, \tag{55}$$

where, by (54b) and (44)

$$F_{nn}^{(3,2)} = H_{\zeta\zeta}^{(0)} - V_n^{(2)} - W_{ns}^{(2)}.$$

Thus (55) is the inhomogeneous equation corresponding to the vibration equation (45); since (45) has the normalized solution $\sigma_{ns}^{(0)}$ belonging to the eigenvalue $W_{ns}^{(2)}$, (55) is solvable only when the right-hand side multiplied by $\overline{\sigma_{ns}^{(0)}}$ has a vanishing integral over $\zeta$-space. This gives, using (47b), a differential equation for $\rho_{ns}^{(0)}(\theta)$:

$$\left(F_{\underset{ss}{nn}}^{(3,3)} - W^{(3)}\right)\rho_{ns}^{(0)} = 0.$$

However, $F_{nn}^{(3,3)}$ is odd in the $\xi_i$ and $\partial/\partial\zeta_i$ so the diagonal element of the $\zeta$-matrix must vanish. When one transforms to the normal coordinates $\eta_i$, $\sigma_{ns}^{(0)}$ becomes a sum of products of orthogonal Hermite functions, $F_{nn}^{(3,3)}$, a polynomial of odd order in the $\eta_i$ and $\partial/\partial\eta_i$, so that every term contains at least one of $\eta_i$ or $\partial/\partial\eta_i$ in an odd power; therefore every term in the $\zeta$-matrix vanishes. It follows therefore

$$W^{(3)} = 0 \tag{56}$$

and $\rho_{ns}^{(0)}$ remains, as before, undetermined.

Now we may solve:

$$\chi_{ns}^{(1)} = S_{ns}^{(1)}\rho_{ns}^{(0)} \tag{57}$$

where $S_{ns}^{(1)}$ is the following operator with respect to the $\theta_i$:

$$S_{ns}^{(1)} = \sum_{s'}' \frac{F_{nn}^{(3,3)}\sigma_{ns'}^{(0)}}{W_{ns}^{(2)} - W_{ns'}^{(2)}}. \tag{58}$$

Finally the solution of (52):

$$\psi_n^{(3)} = \sum_{n'}' \frac{F_{nn}^{(3)}\phi_{n'}^{(0)}}{V_n^{(0)} - V_{n'}^{(0)}} \tag{59}$$

and by (53), this has the form:

$$\psi_n^{(3)} = \sum_{n'}' \left(G_{nn'}^{(3,1)}\chi_{ns}^{(2)}\phi_{n'}^{(0)} + G_{nn'}^{(3,2)}\chi_{ns}^{(1)}\phi_{n'}^{(0)} + G_{nn'}^{(3,3)}\chi_{ns}^{(0)}\phi_{n'}^{(0)}\right), \tag{60}$$

where

$$G_{nn'}^{(3,2)} = \frac{F_{nn'}^{(3,2)}}{V_n^{(0)} - V_{n'}^{(0)}}. \tag{61}$$

10

Noting (54) we see that $G_{nn'}^{(3,1)}$ is a number, $G_{nn'}^{(3,2)}$ a differential operator with respect to the $\zeta_i$ and $G_{nn'}^{(3,3)}$ an operator with respect to the $\zeta_i$ and $\theta_i$.

By (26a), Part II

$$\begin{aligned} \sum_{n'}' G_{nn'}^{(3,1)} \chi_{ns}^{(2)} \phi_{n'}^{(0)} &= \sum \frac{(H_0^{(1)})_{nn'} \phi_{n'}^{(0)} \chi_{ns}^{(2)}}{V_n^{(0)} - V_{n'}^{(0)}} \\ &= \sum_{n'}' u_{nn'}^{(1)} \phi_{n'}^{(0)} \chi_{ns}^{(2)} \\ &= \phi_n^{(1)} \chi_{ns}^{(2)} \end{aligned}$$

thus

$$\psi_n^{(3)} = \phi_n^{(1)} \chi_{ns}^{(2)} + \sum_{n'}' \left( G_{nn'}^{(3,2)} \chi_{ns}^{(1)} \phi_{n'}^{(0)} + G_{nn'}^{(3,3)} \chi_{ns}^{(0)} \phi_{n'}^{(0)} \right). \tag{62}$$

## Part VI. Solution of the Approximate Equations of fourth and higher Order: Rotation and Coupling Effects

After substitution of the quantities already determined, the 4th order approximation equation (35e) becomes:

$$\begin{aligned} \left( H_0^{(0)} - V_n^{(0)} \right) \psi_n^{(4)} &= \left( W^{(4)} - H_0^{(4)} - H_{\theta\theta}^{(0)} - H_{\zeta\theta}^{(1)} - H_{\zeta\zeta}^{(2)} \right) \chi_{ns}^{(0)} \phi_n^{(0)} \\ &\quad - \left( H_0^{(3)} + H_{\zeta\theta}^{(0)} + H_{\zeta\zeta}^{(1)} \right) \left( \chi_{ns}^{(1)} \phi_n^{(0)} + \chi_{ns}^{(0)} \phi_n^{(1)} \right) \\ &\quad + \left( W_{ns}^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)} \right) \left( \chi_{ns}^{(2)} \phi_n^{(0)} + \chi_{ns}^{(1)} \phi_n^{(1)} + \chi_{ns}^{(0)} \phi_n^{(2)} \right) \\ &\quad - H_0^{(1)} \left\{ \phi_n^{(1)} \chi_{ns}^{(2)} + \sum_{n'}' \left( G_{nn'}^{(3,2)} \chi_{ns}^{(1)} \phi_{n'}^{(0)} + G_{nn'}^{(3,3)} \chi_{ns}^{(0)} \phi_{n'}^{(0)} \right) \right\}. \end{aligned} \tag{63}$$

We develop again the right-hand side in the $\phi_n^{(0)}$:

$$\left( H_0^{(0)} - V_n^{(0)} \right) \psi_n^{(4)} = W^{(4)} \chi_{ns}^{(0)} \phi_n^{(0)} - \sum_{n'}' F_{nn'}^{(4)} \phi_{n'}^{(0)}, \tag{64}$$

where

$$F_{nn'}^{(4)} = F_{nn'}^{(4,2)} \chi_{ns}^{(2)} + F_{nn'}^{(4,3)} \chi_{ns}^{(1)} + F_{nn'}^{(4,4)} \chi_{ns}^{(0)}; \tag{65}$$

here we have

$$F_{nn'}^{(4,2)} = \left( H_{\zeta\zeta}^{(0)} - H_0^{(2)} - W_{ns}^{(2)} \right)_{nn'} + \left( H_0^{(1)} \right)_{nn'}^{(1)} \tag{66}$$

and is identical with $F_{nn'}^{(3,2)}$ (54b). While $F_{nn'}^{(4,3)}$ is of odd order in the $\zeta_i, \partial/\partial\zeta_i$, $F_{nn'}^{(4,3)}$ is of even order. The integrability of (64) requires:

$$W^{(4)} \chi_{ns}^{(0)} - F_{nn}^{(4)} = 0;$$

this means that by (65)

$$F_{nn}^{(4,2)} \chi_{ns}^{(2)} = \left( W^{(4)} - F_{nn}^{(4,4)} \right) \chi_{ns}^{(0)} - F_{nn}^{(4,3)} \chi_{ns}^{(1)}. \tag{67}$$

The left side agrees again with the vibration equation (45) because of (66). The right-hand side must also be orthogonal to $\sigma_{ns}^{(0)}$. Substituting the expressions for $\chi_{ns}^{(0)}$ and $\chi_{ns}^{(1)}$ from (47b) and (57), and using the symbol

$$(\Phi)_{ss'}^{(1)} = \int \overline{\sigma_{ns}^{(0)}} \Phi S_{ns}^{(1)} \mathrm{d}\zeta = \sum_{s''}' \frac{\left[ \Phi F_{nn}^{(3,3)} \right]_{ss'}}{W_{ns}^{(2)} - W_{ns''}^{(2)}}, \tag{68}$$

11

we find

$$\left\{F_{ss}^{(4,4)} + \left(F_{nn}^{(4,3)}\right)_{ss}^{(1)} - W^{(4)}\right\} \rho_{ns}^{(0)} = 0. \tag{69}$$

This equation determines finally the function $\rho_{ns}^{(0)}(\theta)$, hence the motion of the principal axes of inertia: the translations and rotations. The principal term of the operator in (69) is the one which contains the second derivative with respect to the $\theta_i$; a glance at (63) shows that it arises from $H_{\theta\theta}^{(0)}\chi_{ns}^{(0)}\phi_n^{(0)}$, the term corresponds in $F_{nn}^{(4,4)}$ to

$$\left(\overline{H_{\theta\theta}^{(0)}}\right)_n = \int \overline{\phi_n^{(0)}} H_{\theta\theta}^{(0)}(\phi_n^{(0)} \dots) dx, \tag{70}$$

where in the place of the dots we have to put in the function which is operated upon. Since the operator (70) is independent of the $\zeta_i$, the diagonal elements of the corresponding s-matrix are identical with it. Physically the fact that the complicated operators $\left(\overline{H_{\theta\theta}^{(0)}}\right)_n$ appear instead of the simple operators $H_{\theta\theta}^{(0)}$ indicates a coupling between the top motion of the nuclei and the electronic motion.

These are, as we will later see for the case of the diatomic molecule, the same effects that Kramers and Pauli [2] have tried to demonstrate using the assumption of a 'fly-wheel' built in to the top. Thus there are terms in (69) that contribute to the operator $H_{\zeta\theta}$; these correspond to a coupling of the top motion with angular momenta which are a consequence of nuclear vibration. Finally, there are terms which do not concern the $\theta_I$; these are the additions to the vibrational energy of order $\kappa^4$.

Since the translations can always be separated in a trivial fashion, we consider only the rotations. If $r$ be the rotational quantum number, we have for the solution of (70)

$$W^{(4)} = W_{nsr}^{(4)}; \quad \rho_{ns}^{(0)} = \rho_{nsr}^{(0)}(\theta). \tag{71}$$

Then one can solve (67) and finally also (64). It is of no use to write out the formulae explicitly.

Clearly, the procedure may be continued; however nothing new of significance will appear. The higher approximations describe couplings among rotations, vibrations and electronic motions. Quantum numbers other than the ones already introduced do not enter.

We summarize now the consequences of our solutions. The most obvious result is that in order to determine completely the eigenfunctions to 0th order it is necessary to solve the approximation differential equations to 4th order; we have

$$\psi_{nsr}(x, \zeta, \theta) = \phi_n^{(0)}(x, \xi, \theta) \sigma_{ns}^{(0)}(\zeta) \rho_{nsr}^{(0)}(\theta) + \dots \tag{72}$$

where $\phi_n^{(0)}$ is the eigenfunction for electronic motion for stationary nuclei, $\sigma_{ns}^{(0)}$ that for nuclear vibration, and $\rho_{nsr}^{(0)}$ that for rotation. Thus are defined the vibrational coordinates $\zeta_i$ from an equilibrium configuration $\xi_i$ which is defined by the requirement that in this configuration the electronic energy $V_n(\xi)$ is a minimum. The determination of the three functions $\phi_n^{(0)}$, $\sigma_{ns}^{(0)}$ and $\rho_{nsr}^{(0)}$ yield the energy to 4th order:

$$W_{nsr} = V_n^{(0)} + \kappa^2 W_{ns}^{(2)} + \kappa^4 W_{nsr}^{(4)} + \dots; \tag{73}$$

where $V_n^{(0)}$ is the minimum value of the electronic energy which characterizes the molecule at rest, $W_{ns}^{(2)}$ is the energy of nuclear vibration, and $W_{nsr}^{(4)}$ contains (along with additional terms for the vibrational energy) the rotational energy. In this approximation (to $\kappa^4$) the three basic types of motion are 'separated'; the coupling among them involves terms of higher powers of $\kappa$.

Given (72) we can now calculate transition probabilities (intensities of bands).

The electrical moment of a molecule $\mathcal{M}$ consists of a nuclear part $\mathcal{P}$ and an electronic part $p$; the $x$-component is:

$$\mathcal{M}_x = \mathcal{P}_x + p_x, \quad \text{where} \quad \left\{ \begin{array}{l} \mathcal{P}_x = \sum_l e_l X_l \\ p_x = e \sum_k x_k \end{array} \right. . \tag{74}$$

12

Hence from the set of matrix elements with respect to $x_k$, $\zeta_i$ and $\theta_j$;

$$(p_x)_{n'}^n = \int p_x \phi_n^{(0)} \overline{\phi_n^{(0)}} \mathrm{d}x \tag{75}$$

is a function of the $\zeta_i$ and $\theta_j$, then the

$$(p_x)_{n's'}^{ns} = \int (p_x)_{n'}^{n} \sigma_{ns'}^{(0)} \overline{\sigma_{ns'}^{(0)}} \mathrm{d}\zeta$$

$$(\mathcal{P}_x)_{n's'}^{ns} = \int (\mathcal{P}_x) \sigma_{ns}^{(0)} \overline{\sigma_{n's'}^{(0)}} \mathrm{d}\zeta \tag{76}$$

are functions of the $\theta_j$, finally

$$(p_x)_{n's'r'}^{nsr} = \int (p_x)_{n's'}^{ns} \rho_{nsr}^{(0)} \overline{\rho_{n's'r'}^{(0)}} \mathrm{d}\theta$$

$$(\mathcal{P}_x)_{n's'r'}^{nsr} = \int (\mathcal{P}_x)_{n's'}^{ns} \rho_{nsr}^{(0)} \overline{\rho_{n's'r'}^{(0)}} \mathrm{d}\theta \tag{77}$$

are numerical constants which determine the radiation and the transition probability for $nsr \to n's'r'$. We can interpret this step by step procedure as follows: for every electronic transition $n \to n'$, there corresponds a virtual oscillator with moment $(p_x)_{n'}^n$; from this one obtains the matrix $(p_x)_{n's'}^{ns}$ which corresponds to a system of vibrational bands (transitions from $s \to s'$), by a rule (somewhat different from the ordinary one) in which one uses one eigenfunction of the lower and one of the upper electronic level (equation (76)). We repeat the procedure for the line of the band corresponding to the transition $r \to r'$. The method of evaluation of the intensity of vibrational bands contained here is first given by Franck [3] and further developed by Condon [4].

These are determined by variation of the functions $V_n(\xi)$ and $V_{n'}(\xi)$; only in the neighbourhood of their minima are the corresponding eigenfunctions $\sigma_{ns}^{(0)}$ and $\sigma_{n's'}^{(0)}$ significantly different from zero; their product is so only when these regions overlap. When the function $V_n(\xi)$ changes only slightly in an electronic transition $n \to n'$, the bands corresponding to a small change of $s$ will be intense; however if $V_n(\xi)$ changes greatly in the transition, an overlap of the intervals in which $\sigma_{ns}^{(0)}$ and $\sigma_{n's'}^{(0)}$ do not vanish becomes possible only when the difference $s - s'$ is large. These relations are quantitatively discussed by Condon. Similar considerations apply for the rotations *mutatis mutandis*.

### Part VII. Special Case of the Diatomic Molecule

As an example we will briefly treat the diatomic molecule. Besides the resonance degeneracy, which is a consequence of the indistinguishability of the electrons, there is an additional degeneracy since corresponding to every energy value there are two possible modes of motion in which the angular momentum about the internuclear axis is oppositely directed. Since we are not concerned here with the fine structure of bands, we will not consider this degeneracy; we limit our consideration to cases in which the angular momentum about the axis vanishes or when the electronic energy is independent or only slightly dependent on the angular momentum component.

For two nuclei we have only one $\xi$ coordinate, the nuclear separation, and five $\theta$ coordinates: the coordinates of the center of mass $X_0, Y_0, Z_0$, and the polar coordinates of the internuclear axis $\theta, \omega$.

The kinetic energy of the nuclei becomes

$$T_K = -\kappa^4 \frac{h^2}{8\pi^2 m} \left\{ \Delta_0 + \frac{\mu}{\xi^2} \frac{\partial}{\partial \xi} \left( \xi^2 \frac{\partial}{\partial \xi} \right) + \frac{\mu}{\xi^2} \Delta_0 \right\} \tag{78}$$

where

$$\kappa = \left( \frac{m}{M_1 + M_2} \right)^{1/4} \quad \text{and} \quad \mu = \frac{(M_1 + M_2)^2}{M_1 M_2} \tag{79}$$

13

and

$$\Delta_{0} = \frac{\partial^{2}}{\partial X_{0}^{2}} + \frac{\partial^{2}}{\partial Y_{0}^{2}} + \frac{\partial^{2}}{\partial Z_{0}^{2}},$$

$$\Delta_{\theta} = \frac{1}{\sin^{2}\theta} \frac{\partial^{2}}{\partial \omega^{2}} + \frac{1}{\sin\theta} \frac{\partial}{\partial \theta} \left( \sin\theta \frac{\partial}{\partial \theta} \right). \tag{80}$$

Thus:

$$H_{\xi\xi} = -\frac{h^{2}}{8\pi^{2}m} \mu \frac{\partial^{2}}{\partial \xi^{2}},$$

$$H_{\xi\theta} = -\frac{h^{2}}{8\pi^{2}m} \frac{2\mu}{\xi} \frac{\partial}{\partial \xi}, \tag{81}$$

$$H_{\theta\theta} = -\frac{h^{2}}{8\pi^{2}m} \left( \Delta_{0} + \frac{\mu}{\xi^{2}} \Delta_{\theta} \right).$$

Substituting $\xi + \kappa\zeta$ for $\xi$ and developing in $\kappa$, we find:

$$H_{\zeta\zeta}^{(0)} = -\frac{h^{2}}{8\pi^{2}m} \mu \frac{\partial^{2}}{\partial \zeta^{2}},$$

$$H_{\zeta\zeta}^{(p)} = 0, \quad p = 1, 2, \dots \tag{82}$$

$$H_{\zeta\theta}^{(0)} = -\frac{h^{2}}{8\pi^{2}m} \frac{2\mu}{\xi} \frac{\partial}{\partial \zeta},$$

$$H_{\zeta\theta}^{(1)} = \frac{h^{2}}{8\pi^{2}m} \frac{\mu}{\xi^{2}} \zeta \frac{\partial}{\partial \zeta}, \tag{83}$$

...

$$H_{\theta\theta}^{(0)} = -\frac{h^{2}}{8\pi^{2}m} \left( \Delta_{0} + \frac{\mu}{\xi^{2}} \Delta_{\theta} \right),$$

$$H_{\theta\theta}^{(1)} = \frac{h^{2}}{8\pi^{2}m} \frac{2\mu}{\xi^{3}} \zeta \Delta_{\theta}. \tag{84}$$

...

The nuclear separation is determined by the equation

$$V_{n}^{\prime} = \frac{\partial V_{n}}{\partial \xi} = 0. \tag{85}$$

The equation for nuclear vibration is

$$\left\{ -\frac{h^{2}}{8\pi^{2}m} \mu \frac{\partial^{2}}{\partial \zeta^{2}} + \frac{1}{2} \zeta^{2} V_{n}^{\prime\prime}(\xi) W_{n}^{(2)} \right\} \chi_{n}^{(0)} = 0. \tag{86}$$

If we set

$$a = \frac{8\pi^{2}m}{h^{2}\mu} W_{n}^{(2)} \quad b = \frac{8\pi^{2}m}{h^{2}\mu} V_{n}^{\prime\prime} \quad \eta = \zeta b^{1/4} \tag{87}$$

we have [8]

$$\left\{ \frac{\partial^{2}}{\partial \eta^{2}} + \left( \frac{a}{\sqrt{b}} - \eta^{2} \right) \right\} \chi_{n}^{(0)} = 0.$$

14

The eigenvalues are

$$a / b ^ { 1 / 2 } = 2 s + 1 \ ( s = 0 , 1 , 2 , \dots ) ,$$

with eigenfunctions

$$\sigma _ { n s } ^ { ( 0 ) } = \exp { - ( \eta ^ { 2 } / 2 ) } H _ { s } ( \eta ) ,$$

where $H _ { s }$ is the $s$th Hermite polynomial.

The energy of the vibrations is thus:

$$\begin{array} { l l l } { { \kappa ^ { 2 } W _ { n s } ^ { ( 2 ) } } } & { { = } } & { { a \displaystyle \frac { h ^ { 2 } } { 8 \pi ^ { 2 } } \frac { \kappa ^ { 2 } \mu } { m } = ( 2 s + 1 ) b ^ { 1 / 2 } \frac { h ^ { 2 } } { 8 \pi ^ { 2 } } \frac { \kappa ^ { 2 } \mu } { m } } } \\ { { } } & { { = } } & { { \left( s + \displaystyle \frac { 1 } { 2 } \right) \displaystyle \frac { h } { 4 \pi } \sqrt { \kappa ^ { 4 } \displaystyle \frac { \mu } { m } V _ { n } ^ { \prime \prime } } } } \end{array}$$

or

$$\kappa ^ { 2 } W _ { n s } ^ { ( 2 ) } = \left( s + \frac { 1 } { 2 } \right) h \nu _ { 0 }$$

with

$$\frac { 1 } { 4 \pi } \sqrt { \kappa ^ { 4 } \frac { \mu } { m } V _ { n } ^ { \prime \prime } } = \frac { 1 } { 4 \pi } \sqrt { \left( \frac { 1 } { M _ { 1 } } + \frac { 1 } { M _ { 2 } } \right) V _ { n } ^ { \prime \prime } } = \nu _ { 0 }$$

the frequency of the oscillator.

We set up now the equation (69) for the rotation, neglecting any detailed estimation of the correction to the vibrational energy. Since $H _ { \xi \theta }$ by (81) does not contain derivatives with respect to the $\theta _ { j }$ , we need consider only the term $\overline { { \left( H _ { \theta \theta } ^ { ( 0 ) } \right) } } _ { n }$ in (69); all remaining terms we include in the constant $C _ { n s }$ . The rotational equation (69) is then:

$$\left\{ \overline { { \left( H _ { \theta \theta } ^ { ( 0 ) } \right) } } _ { n } + C _ { n s } - W ^ { ( 4 ) } \right\} \rho _ { n s } ^ { ( 0 ) } = 0 .$$

Since we have dropped the translational part from $H _ { \theta \theta ^ { ( 0 ) } }$ , we have by (70) and (84) for an arbitrary function $f ( \theta )$ :

$$\overline { { \left( H _ { \theta \theta } ^ { ( 0 ) } \right) } } _ { n } f ( \theta ) = - \frac { h ^ { 2 } \mu } { 8 \pi ^ { 2 } m \xi ^ { 2 } } \int \overline { { \phi _ { n } ^ { ( 0 ) } } } \Delta _ { \theta } ( \phi _ { n } ^ { ( 0 ) } f ) \mathrm { d } x$$

and by (80)

$$\Delta _ { \theta } ( \phi _ { n } ^ { ( 0 ) } f ) = \phi _ { n } ^ { ( 0 ) } \Delta _ { \theta } f + f \Delta _ { \theta } \phi _ { n } ^ { ( 0 ) } + 2 \left( \frac { 1 } { \sin ^ { 2 } \theta } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \omega } \frac { \partial f } { \partial \omega } + \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \theta } \frac { \partial f } { \partial \theta } \right) .$$

Thus

$$\begin{array} { l l l } { { \overline { { { \left( H _ { \theta \theta } ^ { ( 0 ) } \right) } } } _ { n } f } } } & { { = } } & { { - \displaystyle \frac { h ^ { 2 } \mu } { 8 \pi ^ { 2 } m \xi ^ { 2 } } \left\{ \Delta _ { \theta } f + f \int \overline { { \phi _ { n } ^ { ( 0 ) } } } \Delta _ { \theta } \phi _ { n } ^ { ( 0 ) } \mathrm { d } x \right. } } \\ { { } } & { { + } } & { { \displaystyle \left. \cdot \frac { 2 } { \sin ^ { 2 } \theta } \frac { \partial f } { \partial \omega } \int \overline { { \phi _ { n } ^ { ( 0 ) } } } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \omega } \mathrm { d } x + 2 \frac { \partial f } { \partial \theta } \int \overline { { \phi _ { n } ^ { ( 0 ) } } } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \theta } \mathrm { d } x \right\} . } } \end{array}$$

If we write $\Delta _ { \theta }$ in the form:

$$\Delta _ { \theta } = \frac { \partial ^ { 2 } } { \partial \theta ^ { 2 } } + \mathrm { c t g } \, \theta \frac { \partial } { \partial \theta } + \frac { 1 } { \sin ^ { 2 } \theta } \frac { \partial ^ { 2 } } { \partial \omega ^ { 2 } }$$

we see that it is convenient to introduce the following notation:

$$\begin{array} { l l } { { \overline { { { \Theta _ { n } } } } = \displaystyle \int \overline { { { \phi _ { n } ^ { ( 0 ) } } } } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \theta } \mathrm { d } x , } } & { { \overline { { { \Omega _ { n } } } } = \displaystyle \int \overline { { { \phi _ { n } ^ { ( 0 ) } } } } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \omega } \mathrm { d } x , } } \\ { { \overline { { { \Theta _ { n } ^ { ( 2 ) } } } } = \displaystyle \int \overline { { { \phi _ { n } ^ { ( 0 ) } } } } \frac { \partial ^ { 2 } \phi _ { n } ^ { ( 0 ) } } { \partial \theta ^ { 2 } } \mathrm { d } x , } } & { { \overline { { { \Omega _ { n } ^ { ( 2 ) } } } } = \displaystyle \int \overline { { { \phi _ { n } ^ { ( 0 ) } } } } \frac { \partial ^ { 2 } \phi _ { n } ^ { ( 0 ) } } { \partial \omega ^ { 2 } } \mathrm { d } x . } } \end{array}$$

15

These quantities are the diagonal matrix elements of $p_{\theta}$, $p_{\omega}$, $p_{\theta}^{2}$ and $p_{\omega}^{2}$ (aside from a factor $\frac{h}{2\pi^{2}}$, $-\frac{h^{2}}{4\pi^{2}}$ respectively); the first two denote the average value of the electronic angular momentum about their corresponding Eulerian angle; the second two, the average of the square of the angular momentum of electronic motion. We write then for (90) explicitly:

$$\left\{\left(\frac{\partial^{2}}{\partial\theta^{2}}+2\overline{\Theta_{n}}\frac{\partial}{\partial\theta}+\overline{\Theta_{n}^{(2)}}\right)+\operatorname{ctg}\theta\left(\frac{\partial}{\partial\theta}+\overline{\Theta_{n}}\right)\right.$$ $$\left.\frac{1}{\sin^{2}\theta}\left(\frac{\partial^{2}}{\partial\omega^{2}}+2\overline{\Omega_{n}}\frac{\partial}{\partial\omega}+\overline{\Omega_{n}^{(2)}}\right)+\frac{8\pi^{2}m\xi^{2}}{h^{2}\mu}\left(W^{(4)}-C_{ns}\right)\right\}\rho_{ns}^{(0)}=0 \quad (92)$$

This is very similar to the equation of Kramers and Pauli for a rotor with a built-in fly-wheel; the difference is essentially that they use the squares of the average values $\overline{\Theta_{n}}^{2}$ and $\overline{\Omega_{n}}^{2}$, instead of the average of the squares $\overline{\Theta_{n}^{2}}$ and $\overline{\Omega_{n}^{2}}$.

The dependence of the quantities in (91) on the angles $\theta$ and $\omega$ may be established by elementary considerations if it is assumed that for this purpose the diagonal elements of the quantum mechanical matrix may be replaced by the corresponding classical averages. One may decompose the motion of the electronic angular momentum vector into an irregular variation without average rotations and a superimposed uniform rotation about the molecular axis. We represent the variation in the average by a constant vector; this rotates uniformly about the axis. This exhibits the same behaviour as a symmetric top with angular momentum components with respect to the top-fixed coordinate system having values $L$, $M$ and $N$. From this we may express the components of the angular momentum in the $\theta$, $\omega$ direction as follows:

$$\begin{array}{l} \Theta = L\cos\gamma - M\sin\gamma \\ \Omega = L\sin\theta\sin\gamma + M\sin\theta\cos\gamma + N\cos\theta, \end{array}$$

where $\gamma$ is the angle of the eigenrotation about the axis. Averaging over $\gamma$, we find:⁵

$$\begin{array}{l} \overline{\Theta}=0 \quad \overline{\Omega}=N\cos\theta \\ \overline{\Theta^{2}}=\frac{1}{2}(L^{2}+M^{2}) \quad \overline{\Omega^{2}}=\frac{1}{2}(L^{2}+M^{2})\sin^{2}\theta+N^{2}\cos^{2}\theta. \end{array}$$

We identify $N$ with the quantum number $\rho$ which gives the angular momentum about the axis, and $\frac{1}{2}(L^{2}+M^{2})$ and $\frac{1}{2}N^{2}$ with the averages $\overline{p_{\perp}^{2}}$ and $\overline{p_{\parallel}^{2}}$ of the total electronic angular momentum perpendicular and parallel to the axis; since $N$ is constant, $\overline{p_{\parallel}^{2}}=p^{2}$. We have finally:

$$\begin{array}{l} \overline{\Theta_{n}}=0 \quad \overline{\Omega_{\mu}}=p\cos\theta \\ \overline{\Theta_{n}^{2}}=\overline{p_{\perp}^{2}} \quad \overline{\Omega^{2}}=\overline{p_{\perp}^{2}}\sin^{2}\theta+p^{2}\cos^{2}\theta. \end{array} \quad (93)$$

This result requires naturally a rigorous quantum mechanical verification; presumably $p^{2}$ is replaced by $p(p+1)$.

In the eigenvalue problem (92), the quantity $\frac{8\pi^{2}m\xi^{2}}{h^{2}\mu}W^{(4)}$ is equal to a numerical function of the rotational quantum number $r$, say $g_{ns}(r)$; the rotational energy is thus:

$$\kappa^{4}W_{nsr}^{(4)}=\frac{h^{2}\mu\kappa^{4}}{8\pi^{2}m\xi^{2}}g_{ns}(r)=\frac{h^{2}}{8\pi^{2}J}g_{ns}(r), \quad (94)$$

where

$$J=\frac{m}{\mu\kappa^{4}}\xi^{2}=\frac{M_{1}M_{2}}{M_{1}+M_{2}}\xi^{2}, \quad (95)$$

⁵Compare, for instance [9]

16

the moment of inertia of the nuclei at equilibrium.

A discussion of the higher approximation is meaningless unless we consider the degeneracies; we will not attempt this here.

We will now show briefly that one can treat the diatomic by a completely different perturbation procedure; the classical analogue of this treatment was carried out by Born and Hückel [5]. The motion of the electronic system is considered to be unperturbed not for stationary nuclei but rather for uniform rotation of the nuclei.

### Part VIII. Independent Treatment of the Diatomic Molecule.

We go back to equation (12), and rewrite, substituting (11):

$$\left\{H_{0}+\kappa^{4}\left(H_{\xi\xi}+H_{\xi\theta}+H_{\theta\theta}\right)-W\right\}\psi=0.$$

Diatomic molecules have the peculiarity that $H_{\xi\theta}$ is generally independent of the $\theta$. In this case, the method enables separation from the translations and rotations. From (81), dropping the translational terms:

$$\left\{H_{0}-\frac{h^{2}\mu}{8\pi^{2}m}\kappa^{4}\left(\frac{\partial^{2}}{\partial\xi^{2}}+\frac{2}{\xi}\frac{\partial}{\partial\xi}+\frac{1}{\xi^{2}}\Delta_{\theta}\right)-W\right\}\psi=0. \tag{96}$$

We set

$$\psi=Y_{r}(\theta,\omega)\Psi_{r}(x;\xi), \tag{97}$$

where $Y_{r}$ is a spherical function of $r$th order which satisfies the equation:

$$\Delta_{\theta}Y_{r}+r(r+1)Y_{r}=0;$$

thus we find for $\Psi_{r}$ the condition

$$\left\{H_{0}-\frac{h^{2}\mu}{8\pi^{2}m}\kappa^{4}\left(\frac{\partial^{2}}{\partial\xi^{2}}+\frac{2}{\xi}\frac{\partial}{\partial\xi}-\frac{r(r+1)}{\xi^{2}}\right)-W\right\}\Psi_{r}=0. \tag{98}$$

We again substitute $\xi+\kappa\zeta$ for $\xi$; thus considering vibrations about the state of uniform rotation. Denoting the energy of this state as:

$$R=\frac{h^{2}\mu\kappa^{2}}{8\pi^{2}m}\frac{r(r+1)}{\xi^{2}}=\frac{h^{2}}{8\pi^{2}J}r(r+1) \tag{99}$$

and setting

$$W=E+R, \tag{100}$$

we find for (98)

$$\left(\mathsf{H}^{(0)}+\kappa\mathsf{H}^{(1)}+\kappa^{2}\mathsf{H}^{(2)}+\cdots-\mathsf{E}\right)\Psi_{r}=0 \tag{101}$$

where

$$\mathsf{H}^{(0)}=H_{0}^{(0)}$$

$$\mathsf{H}^{(1)}=H_{0}^{(1)}+\zeta R'$$

$$\mathsf{H}^{(2)}=H_{0}^{(2)}+\frac{1}{2}\zeta^{2}R''-\frac{h^{2}\mu}{8\pi^{2}m}\frac{\partial^{2}}{\partial\zeta^{2}} \tag{102}$$

$$\mathsf{H}^{(3)}=H_{0}^{(3)}+\frac{1}{6}\zeta^{3}R'''-\frac{h^{2}\mu}{8\pi^{2}m}\frac{2}{\zeta}\frac{\partial}{\partial\zeta}$$

$$\cdots;$$

17

$H_0^{(0)}, H_0^{(1)}, \ldots$ are the operators given earlier. All the formulas of Part II are valid without modification. The approximation equations are:

$$
\begin{array}{l}
a) \quad \left(\mathsf{H}^{(0)} - \mathsf{E}^{(0)}\right) \Psi_r^{(0)} = 0 \\
b) \quad \left(\mathsf{H}^{(0)} - \mathsf{E}^{(0)}\right) \Psi_r^{(1)} = \left(\mathsf{E}^{(1)} - \mathsf{H}^{(1)}\right) \Psi_r^{(0)} \\
c) \quad \left(\mathsf{H}^{(0)} - \mathsf{E}^{(0)}\right) \Psi_r^{(2)} = \left(\mathsf{E}^{(2)} - \mathsf{H}^{(2)}\right) \Psi_r^{(0)} + \left(\mathsf{E}^{(1)} - \mathsf{H}^{(1)}\right) \Psi_r^{(1)}
\end{array}
\tag{103}
$$

The first has the solution:

$$
\mathsf{E}^{(0)} = V_n(\xi), \quad \Psi_r^{(0)} = \Psi_{rn}^{(0)} = \sigma_{rn}^{(0)}(\zeta) \phi_n^{(0)}(x; \xi),
\tag{104}
$$

where $V_n(\xi)$ and $\phi_n^{(0)}(x; \xi)$ are the previously introduced functions and $\sigma_{rn}^{(0)}(\zeta)$ is, to begin with, arbitrary. The condition for integrability of (103b) is

$$
\left(\mathsf{E}^{(1)} - \mathsf{H}^{(1)}\right) \sigma_{rn}^{(0)}(\zeta) = 0.
$$

Now, by (26a) (Part II):

$$
\mathsf{H}_{nn}^{(1)} = \left(H_0^{(1)}\right)_{nn} + \zeta R' = V_n^{(1)} + \zeta R' = \zeta \frac{\partial}{\partial \xi}(V_n + R).
$$

Hence, as before (Part IV),

$$
\mathsf{E}^{(1)} = 0, \quad \frac{\partial}{\partial \xi}(V_n + R) = 0.
\tag{105}
$$

This condition obviously states that for the unperturbed rotation, equilibrium must prevail between the centrifugal force and the quasi-electric force, which, as a consequence of the electronic motion, resists a displacement of the nuclei. The centrifugal force is:

$$
-\left(\frac{1}{M_1} + \frac{1}{M_2}\right) \frac{p_r^2}{\xi^3} = -\left(\frac{1}{M_1} + \frac{1}{M_2}\right) \frac{h^2}{4\pi^2} \frac{r(r+1)}{\xi^3},
$$

where the quantum mechanical value $\frac{h}{2\pi} \sqrt{r(r+1)}$ for the angular momentum is substituted for $p_r$; by (99) and (95), this agrees with $R'$.

From relation (105), how to calculate the equilibrium separation $\xi_r$; depends on the rotational quantum number $r$. For small values of the rotational energy $R$, one can develop $\xi_r$ in powers of $\beta$, where:

$$
\beta = \kappa^4 \frac{\mu}{m} \frac{h^2}{4\pi^2} r(r+1) = \left(\frac{1}{M_1} + \frac{1}{M_2}\right) \frac{h^2}{4\pi^2} r(r+1);
\tag{106}
$$

we find:⁶

$$
\xi_r = \xi + \frac{1}{\xi^3 V_n''} \beta - \frac{3}{\xi^7 V_n''^2} \left(1 + \frac{\xi}{6} \frac{V_n''}{V_n''}\right) \beta^2 + \cdots
\tag{107}
$$

Since $\beta$ is of order $\kappa^4$, we will use by systematic procedure only as many terms of this set as correspond to the order of the approximation in the perturbation method.

Since we consider this again, we will shortly see that this is the same method as before, only simplified by the previous consideration of the rotation. The solution of (103b) is:

$$
\Psi_{rn}^{(1)} = \sigma_{rn}^{(0)} \phi_n^{(1)} + \sigma_{rn}^{(1)} \phi_n^{(0)}
\tag{108}
$$

this corresponds to (42); and the condition for integrability of (102c):

$$
\left\{ \mathsf{H}_{nn}^{(2)} + \left(\mathsf{H}_{nn}^{(1)}\right)_{nn}^{(1)} - \mathsf{E}_n^{(2)} \right\} \sigma_{rn}^{(0)} = 0.
$$

⁶One can easily deduce this formula from the cited work of Born and Hückel.

18

This is, however, the vibration equation

$$\left\{ - \frac { h ^ { 2 } \mu } { 8 \pi ^ { 2 } m } \frac { \partial ^ { 2 } } { \partial \zeta ^ { 2 } } + \frac { 1 } { 2 } \zeta ^ { 2 } ( V _ { n } ^ { \prime \prime } + R ^ { \prime \prime } ) - \mathsf { E } _ { n } ^ { ( 2 ) } \right\} \sigma _ { r n } = 0 . \tag { 1 0 9 }$$

Thus, as in Part VII:

$$\kappa ^ { 2 } \mathsf { E } _ { r n s } ^ { ( 2 ) } = \left( s + \frac { 1 } { 2 } \right) h \nu _ { r } , \tag { 1 1 0 }$$

where the frequency,

$$\nu _ { r } = \frac { 1 } { 4 \pi } \sqrt { \left( \frac { 1 } { M _ { 1 } } + \frac { 1 } { M _ { 2 } } \right) ( V _ { n } ^ { \prime \prime } + R ^ { \prime \prime } ) } \tag { 1 1 1 }$$

still depends on the rotational quantum number $r$, from the $R$.

Further, as in Part VII,

$$\sigma _ { r n s } ^ { ( 0 ) } = \exp ( - \eta ^ { 2 } / 2 ) H _ { s } ( \eta ) \tag { 1 1 2 }$$

with

$$\eta = \zeta b ^ { 1 / 4 } , \quad b = \frac { 8 \pi ^ { 2 } } { h ^ { 2 } } \frac { m } { 2 \mu } ( V _ { n } ^ { \prime \prime } + R ^ { \prime \prime } ) .$$

The procedure may be continued in the usual fashion. We find $\mathsf { E } ^ { ( 3 ) } = 0$, while $\mathsf { E } ^ { ( 4 ) }$, besides the deviation from the harmonic vibration law, contains a coupling with the electronic motion. A thorough consideration of the formulae would, however, be beyond the scope of this work, which demonstrates only the principle of the development; also the calculation of the higher approximations is meaningful only when the degeneracies are taken into account.

[1] M. Born and W. Heisenberg Ann. d. Phys. 74 1 (1924)

[2] H. A. Kramers Zeitschr. f. Phys. 13 343 (1923); H. A. Kramers and W. Pauli jr. ibid. 13 351 (1923)

[3] J. Franck Trans. Faraday. Soc. (1925)

[4] E. Condon, Phys. Rev. 28 1182 (1926); Proc. Nat. Acad. 13 462 (1927)

[5] M. Born and E. Hückel Phys. Ztschr. 24 1 (1923)

[6] F. Hund Ztschr. f. Phys. 43 805 (1927)

[7] W. Pauli Ann. d. Phys. 68 177 (1922)

[8] S. E. Schrödinger Ann. d. Phys. 79 361, §3 (1926).

[9] F. Klein and A. Sommerfeld Theorie des Kreisels 1 p 108

19
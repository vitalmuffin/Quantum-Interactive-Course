1926

№ 18

# ANNALS OF PHYSICS
## FOURTH EPISODE. VOLUME 81

### 1. Quantization as an eigenvalue problem;
by E. Schrödinger

(Fourth Communication¹)

Table of contents: § 1. Elimination of the energy parameter from the vibration equation. The actual wave equation. Non-conservative systems. — § 2. Extension of the perturbation theory to perturbations which explicitly contain time. Dispersion theory. — § 3. Additions to § 2: Excited atoms, degenerate systems, range of routes. — § 4. — § 5. Generalization for any disorder. — § 6. Relativistic-magnetic generalization of basic equations. — § 7. On the physical significance of the field scalar.

#### § 1. Elimination of the energy parameter from the vibration equation. The actual wave equation. Non-conservative systems

The wave equation (18) and (18') of page 510 of the second communication

$$\Delta \psi - \frac{2(E - V)}{E^2} \frac{\partial^2 \psi}{\partial t^2} = 0$$

or

$$\Delta \psi + \frac{8\pi^2}{h^2} (E - V) \psi = 0,$$

which forms the foundation of the new foundation of mechanics attempted in this series of treatises, suffers from the evil that it ignores the law of change for the "mechanical field scalar" $\psi$ does not pronounce uniformly and not generally. Equation (1) contains the energy or frequency parameter $E$ and, as loc. cit. expressly emphasizes, is to be incompatible with a certain $E$value valid for operations that

1) Cf. Ann. d. Phys. 79. pp. 361, 489; 80. p. 437. 1926; furthermore on the connection with Heisenberg's theory: ibid. 79, p. 734.

Annals of Physics. IV. Folge. 81.

8

110

E. Schrödinger

from the *Time* exclusively by a *certain* periodic factor

$$(2) \quad \psi \sim P \cdot R \cdot \left( e^{\pm \frac{2\pi i E t}{h}} \right).$$

Equation (1), therefore, is in reality no more general than equation (1'), which takes account of the circumstance just mentioned, and no longer contains time at all.

So if we have occasionally called equation (1) or (1') a "wave equation", this was actually wrong, it would be more correct to call it an "oscillation" or "amplitude" equation. But we found it to be sufficient, because it was *these* The Sturm-Liouville eigenvalue problem is linked — just as with the mathematically completely analogous problem of the free oscillations of strings and diaphragms — and not to the *Actual* Wave equation.

In doing so, we had always assumed that the potential energy $V$ is a pure coordinate function and *not* explicitly depends on the time. However, there is an urgent need to base the theory on *Non-conservatives* systems, because only in this way can the behavior of the system under the influence of predetermined external forces, e.g. a light wave or a passing foreign atom, be studied. But as soon as $V$ contains time explicitly, it is evidently *impossible*, satisfy equation (1) or (1') by a function $\psi$, which depends only after (2) on time. So you can no longer find the amplitude equation sufficient, but have to resort to the actual wave equation.

For conservative systems, the same can be easily indicated. (2) is equivalent to

$$(3) \quad \frac{\partial^2 \psi}{\partial t^2} = - \frac{4\pi^2 E^2}{h^2} \psi.$$

From (1') and (3) you can $E$ through differentiations and obtains in an easily understandable symbolic notation

$$(4) \quad \left( \Delta - \frac{8\pi^2}{h^2} V \right)^2 \psi + \frac{16\pi^2}{h^2} \frac{\partial^2 \psi}{\partial t^2} = 0.$$

This equation has every $\psi$ which is referred to in (2), but *with any* $E$, depends on the time; consequently also

Quantization as an eigenvalue problem

111

each $\psi$, which can be developed by a Fourier series according to time (of course with coordinate functions as coefficients). equation (4) therefore appears to be the *uniform and general wave equation for the field scalar* $\psi$.

As you can see, it is no longer of the very simple type of vibrating membrane, but rather in the coordinates of the *fourth* order and of a very similar type to that which occurs in many problems of the theory of elasticity.¹⁾ However, one need not fear an excessive complication of the theory from this, or even the necessity of a revision of the methods hitherto given, which are based on equation (1'). Contains $V$ the time *not*, you can start with (4) and then split the operator into (4) as follows:

$$(4') \left( \Delta - \frac{8\pi^2}{h^2} V + \frac{8\pi^2}{h^2} E \right) \left( \Delta - \frac{8\pi^2}{h^2} V - \frac{8\pi^2}{h^2} E \right) \dot{\psi} = 0.$$

This equation can be *Experimental* into two equations connected by "either — or", namely equation (1') and another which differs from (1') only in that in it the eigenvalue parameter minus $E$ *is called*, instead of plus $E$, which does not lead to new solutions according to (2). The splitting of (4') is not inevitable because the proposition that "a product can only disappear if at least *a* Factor disappears". This lack of inevitability, however, adheres to the methods for solving partial differential equations at every turn. The procedure is subsequently justified by the proof of the *Completeness* of the eigenfunctions found as functions of the coordinates. In connection with the fact that not only the real part but also the imaginary part of (2) satisfies equation (4), it allows any initial conditions for $\psi$ and $\partial \psi / \partial t$ .

We see, therefore, that the wave equation (4), which already carries the law of dispersion, really has as its basis

¹⁾ E.g. in the case of the oscillating plate: $\Delta \Delta u + \frac{\partial^2 u}{\partial t^2} = 0$. Cf. Courant-Hilbert, chap. V. § 8. p. 256.

8\*

112

E. Schrödinger

the theory of conservative systems developed so far. Their generalization for the case of a temporally variable potential function requires some caution, because it involves terms with temporal derivatives of $V$ about which equation (4) can of course give us no information according to the way in which it is obtained. In fact, in the attempt to apply equation (4) as it stands to non-conservative systems, one encounters complications that are caused by a term with $\partial V/\partial t$ . In the following, I have therefore taken a somewhat different path, which is mathematically extraordinarily much simpler and which I consider to be correct in principle.

You don't have to push the order of the wave equation up to four to remove the energy parameter from it. The time dependence of $\psi$ can be replaced by (3) by

$$(3') \quad \frac{\partial \psi}{\partial t} = \pm \frac{2\pi i}{h} E \psi$$

express. One then arrives at one of the two equations

$$(4'') \quad \Delta \psi - \frac{8\pi^2}{h^2} V \psi \mp \frac{4\pi i}{h} \frac{\partial \psi}{\partial t} = 0.$$

We will demand that the complex wave function $\psi$ one of these two equations. Since then the conjugated complex function $\psi$ of the other equation, the real wave function (if needed) is the real part of $\psi$ . — In the case of a conservative system, (4'') is essentially equivalent to (4) since, if $V$ does not contain time, the real operator can be decomposed into the product of the two conjugated complexes.

## § 2. Extension of the perturbation theory to perturbations which explicitly contain time. Dispersion theory

The main interest is not directed at systems in which the temporal fluctuations of the potential energy $V$ are of the same order of magnitude as the spatial ones, but are based on systems which, conservative in themselves, are characterized by the addition of small predetermined functions of time (and the

Quantization as an eigenvalue problem

113

coordinates) to the potential energy. So let's take the approach:

$$(5) \quad V = V_0(x) + r(x, t),$$

where $x$, as has often been the case in the past, as a representative of the totality of the configuration coordinates. The undisturbed eigenvalue problem ($r = 0$) we see as solved. Then the disturbance problem can be solved by quadraturing.

However, we do not want to deal with the general problem at once, but will pick out the problem of dispersion theory from the large number of important applications that fall under the above question, because of its prominent importance, which probably justifies a separate treatment in any case. Here the disturbing forces come from an alternating electric field that is homogeneous and synchronously oscillating in the region of the atom, so when it comes to linearly polarized monochromatic light of the frequency $\nu$ to make the following for the disturbance potential:

$$(6) \quad r(x, t) = A(x) \cos 2\pi \nu t$$

so

$$(5') \quad V = V_0(x) + A(x) \cos 2\pi \nu t.$$

Here's $A(x)$ the negative product of the light amplitude into the coordinate function which, according to ordinary mechanics, means the component of the electric moment of the atom in the direction of the electric light vector (e.g. $-F \sum e_i z_i$if $F$ the light amplitude, $e_i, z_i$ the cargoes and $z$coordinates of the mass points, and the light in the $z$direction (we take the temporally variable part of the potential function with as much or as little right from ordinary mechanics as before, e.g. in the Kepler problem, the constant ones).

With the approach (5'), equation (4'') is:

$$(7) \quad \Delta \psi - \frac{8\pi^2}{h^2} (V_0 + A \cos 2\pi \nu t) \psi \mp \frac{4\pi i}{h} \frac{\partial \psi}{\partial t} = 0.$$

For $A = 0$ these equations are transformed by the approach:

$$(8) \quad \psi = u(x) e^{\pm \frac{2\pi i E t}{h}},$$

114

E. Schrödinger

(which is now initially *not* as "pars realis", but in the proper sense), into the amplitude equation (1') of the undisturbed problem, and it is known (cf. § 1) that in this way the totality of the solutions to the undisturbed problem is found. Let it be

$$E_k \text{ und } u_k(x); \quad k = 1, 2, 3 \dots$$

the eigenvalues and normalized eigenfunctions of the undisturbed problem, which we call *known* and, in order not to lose ourselves in secondary questions, which will have to be given special consideration, *discreet* and among each other *Miscellaneous* (non-degenerate system without route spectrum).

We will then find solutions to the disturbed problem, just as in the case of a disturbance potential independent of time, in the neighbourhood *everyone* possible solution of the undisturbed problem, i.e. in the vicinity of an arbitrary linear combination with constant coefficients of the [according to (8) with the appropriate time factors

$e^{\pm \frac{2\pi i E_k t}{h}}$ to be stapled] $u_k(x)$. Those in the vicinity of a *certain* linear combination solution of the perturbed problem becomes physically *the* have the importance that *they* it is the one that initially occurs when this particular linear combination of free natural oscillations was present when the light wave arrived (perhaps with slight changes in the process of "rocking").

But since the equation of the disturbed problem is also *homogeneous* — this lack of analogy with the "forced oscillations" of acoustics should be emphatically emphasized! — it is evidently sufficient to determine the disturbed solution in the vicinity of each *individual*

$$(9) \quad u_k(x) e^{\pm \frac{2\pi i E_k t}{h}}$$

which can then be combined ad libitum linearly, just as well as the undisturbed solutions.

So we now take the following approach to solve the first equation (7):

$$(10) \quad \psi = u_k(x) e^{\frac{2\pi i E_k t}{h}} + w(x, t).$$

Quantization as an eigenvalue problem

115

[From now on, we will leave aside the lower sign, i.e., the second equation (7), as it would not provide anything new.] The additional link $w(x, t)$ may be regarded as small, its product with the potential for interference may be neglected. If we take this into account when inserting (10) into (7) and take into account that $u_k(x)$ and $E_k$ eigenfunction and eigenwert of the undisturbed problem are, so comes:

$$(11) \begin{cases} \Delta w - \frac{8\pi^2}{h^2} V_0 w - \frac{4\pi i}{h} \frac{\partial w}{\partial t} = \frac{8\pi^2}{h^2} A \cos 2\pi v t \cdot u_k e^{\frac{2\pi i E_k t}{h}} \\ = \frac{4\pi^2}{h^2} A u_k \cdot \left( e^{\frac{2\pi i t}{h} (E_k + h\nu)} + e^{\frac{2\pi i t}{h} (E_k - h\nu)} \right). \end{cases}$$

This equation is easy and essential *only* through the approach:

$$(12) \quad w = w_+(x) e^{\frac{2\pi i t}{h} (E_k + h\nu)} + w_-(x) e^{\frac{2\pi i t}{h} (E_k - h\nu)},$$

if you use the two functions $w_\pm$ or the two equations

$$(13) \quad \Delta w_\pm + \frac{8\pi^2}{h^2} (E_k \pm h\nu - V_0) w_\pm = \frac{4\pi^2}{h^2} A u_k.$$

This step is essential *unambiguously*. It seems at first that one can add to (12) any aggregate of undisturbed natural vibrations. But this aggregate would have to be assumed small of the first order (since this assumption is $w$ and then offers no interest for the time being, since it at most causes disturbances of the second order.

In equations (13) we finally have those *inhomogeneous* Equations before us, which we could reasonably expect to come across — despite the lack of analogy with actual forced oscillations emphasized above. This lack of analogy is extremely important, and is manifested in equations (13) in the following two circumstances. *First,* the perturbative function does not occur as a "second link" ("excitatory force") $A(x)$ *alone* but her *Product* with the already existing free oscillation amplitude. This is indispensable in order to do justice to the physical facts, because the reaction of the atom to an incident light wave

116

E. Schrödinger

depends to an eminent extent on the *Condition* in which the atom is currently located, while the forced oscillations of a membrane, plate, etc., are known to be quite independent of the superimposed natural oscillations, and would therefore provide a completely useless picture. *Secondly* takes the place of the eigenvalue on the left side of (13), i.e. not the frequency as the "excitatory frequency" $\nu$ of the perturbing force *alone* rather the one time their sum, the other time their difference compared to that of the already existing free vibration. This is also an indispensable requirement, because otherwise the natural frequencies themselves, which are the *Term frequencies* as *Resonance points* and not as is to be demanded, and as equation (13) really shows, the *Differences* of natural frequencies, as one recognizes with satisfaction: *only* the differences of a natural frequency, *that is really stimulated*, against all the rest, *not* the differences of natural frequency pairs, of which *none* is stimulated.

In order to get a closer look at this, we will take the solution procedure to the end. According to the well-known method$^{1)}$ we find as *unique* Solutions of (13):

$$(14) \quad w_{\pm}(x) = \frac{1}{2} \sum_{n=1}^{\infty} \frac{a_{kn}' u_n(x)}{E_k - E_n \pm h\nu}$$

with

$$(15) \quad a_{kn}' = \int A(x) u_k(x) u_n(x) \varrho(x) \, dx.$$

$\varrho(x)$ is the "density function", i.e. the function of the positional coordinates, must be multiplied by the equation (1') in order to make it a self-adjoint. The $u_n(x)$ are presupposed to be normalized. It is also presumed that: $h\nu$ with *none of the eigenvalue differences* $E_k - E_n$ *exactly matches*. We will speak of this "resonance case" later (cf. § 4).

If we now form the entire disturbed vibration from (14) after (12) and (10), the result is:

1) Cf. 3rd communication §§ 1 and 2, text at equations (8) and (24).

Quantization as an eigenvalue problem

117

$$(16) \left\{ \begin{aligned} \psi &= u_k(x) e^{\frac{2\pi i E_k t}{h}} \\ &+ \frac{1}{2} \sum_{n=1}^{\infty} a_{kn}' u_n(x) \left( \frac{e^{\frac{2\pi i t}{h}(E_k + h\nu)}}{E_k - E_n + h\nu} + \frac{e^{\frac{2\pi i t}{h}(E_k - h\nu)}}{E_k - E_n - h\nu} \right). \end{aligned} \right.$$

So in the event of a malfunction, each *free* Vibration $u_k(x)$ all those vibrations $u_n(x)$ in small amplitude, for which $a_{kn}' \neq 0$. These are exactly the ones who, when they are $u_k$ as free oscillations, give rise to a radiation which is (wholly or partially) polarized in the direction of polarization of the incident wave. Because $a_{kn}'$ is, apart from one factor, nothing other than the amplitude component of the amplitude component of the frequency falling in this polarization direction $(E_k - E_n)/h$ oscillating *electric torque* of the atom *according to the undulation mechanism*, which is the case with the coexistence of $u_k$ and $u_n$ — The resonance, however, does not take place with the natural frequency peculiar to these oscillations. $E_n/h$, not even with the frequency $\nu$ of the light wave, rather with the sum and with the difference of $E_k/h$ (i.e. the frequency of the *a* existing *free* oscillation) and $\nu$.

As a *Real* solution, the real part or the imaginary part of (16) can be considered. — In the following, however, we will operate with the complex solution itself.

In order to recognize the significance of our result for the dispersion theory, one has to examine the radiation that arises from the coexistence of the excited forced oscillations with the originally already existing free oscillation. If, for this purpose, according to the method always used hitherto — a critique follows in § 7 — let us form the product of the complex wave function (16) into the conjugate complex value, i.e., the norm of the complex wave function $\psi$. In doing so, we note that the perturbations are small

1) Cf. the following and § 7.

2) Cf. Ann. d. Phys. 79. p. 755. 1926; furthermore, the calculation of the strong-effect intensities in the third communication. In the first place, instead of $\psi \bar{\psi}$ the real part of $\psi \bar{\psi}$ proposed. This was a mistake that had already been made in the 3rd mid. has been improved.

118

E. Schrödinger

so that their squares and products are to be left aside from each other. After a slight reduction¹, you get):

$$(17) \quad \psi \bar{\psi} = u_k(x)^2 + 2 \cos 2\pi \nu t \sum_{n=1}^{\infty} \frac{(E_k - E_n) a_{kn}' u_k(x) u_n(x)}{(E_k - E_n)^2 - h\nu}$$

After the *heuristic hypothesis* on the electrodynamic significance of the field scalar $\psi$, which has led us to the correct rules of selection and polarization in the case of the strong effect of hydrogen, and to a quite satisfactory representation of the intensity ratios, the above quantity represents — apart from a multiplicative constant — the density of electricity as a function of spatial coordinates and time when $x$ represents only three spatial coordinates, i.e. when it comes to the *One-electron problem* . In a generalization of this hypothesis — of which more details are given in § 7 — we now see, in the general case, as the density of electricity, which is *a* of the classical-mechanical mass points, or "derives from it" or "corresponds to it in wave mechanics", indicates the following: multiplied by a certain constant, the classical "charge" of the mass point in question *Integral* by $\psi \bar{\psi}$ over all those system coordinates which classically mechanically determine the position of the *Other* Set mass points. The total charge density in a space point is then represented by the *Total* of the above-mentioned integrals.

In order to then find any spatial component of the entire wave-mechanical *Dipole momentes* as a function of time, according to this hypothesis we have to multiply the expression (17) by the coordinate function which *classical-mechanical* the dipole component in question as a function of the configuration of the point system, e.g. with

$$(18) \quad M_y = \sum e_i y_i,$$

1) For the sake of simplicity, we take the eigenfunctions as always before $u_n(x)$ as *real* but note that under certain circumstances it is much more convenient, even necessary, to work with complex aggregates of the real eigenfunctions, e.g. in the eigenfunctions of the Kepler problem with $e^{\pm m\varphi i}$ instead of with $\frac{\cos}{\sin} m\varphi$.

Quantization as an eigenvalue problem

119

when it comes to the dipole moment in the $y$direction. Then you have to *all* configuration coordinates.

Let's elaborate on that. Let's use the abbreviation

$$(19) \quad b_{kn} = \int M_y(x) u_k(x) u_n(x) \varrho(x) \, dx \ .$$

Let us also clarify the definition of $a_{kn}'$ after (15), remembering that if the incident electric light vector is replaced by

$$(20) \quad \mathfrak{E}_z = F \cos 2\pi \nu t$$

is given, $A(x)$ that has meaning

$$(21) \quad \begin{cases} A(x) = -F \cdot M_z(x) \ , \\ \text{wobei } M_z(x) = \sum e_i z_i \ . \end{cases}$$

If you then, analogously with (19),

$$(22) \quad a_{kn} = \int M_z(x) u_k(x) u_n(x) \varrho(x) \, dx \ ,$$

for example, $a_{kn}' = -F a_{kn}$ and by executing the planned integration, one finds:

$$(23) \quad \begin{cases} \int M_y \psi \bar{\psi} \varrho \, dx = a_{kk} \\ \qquad + 2F \cos 2\pi \nu t \sum_{n=1}^{\infty} \frac{(E_n - E_k) a_{kn} b_{kn}}{(E_k - E_n)^2 - h^2 \nu^2} \end{cases}$$

for the resulting electric moment to which the secondary radiation to which the incident wave (20) gives rise is to be attributed.

For the radiation, of course, only the second, temporally variable part is important, while the first represents the temporally constant dipole moment, which may be linked to the originally existing free oscillation. This variable part looks quite reasonable and should meet all the requirements that one is used to placing on a "dispersion formula". Note above all the appearance of those so-called "negative" links which — in the usual language — correspond to the possibility of transition to a lower level ($E_n < E_k$) and to which

120

E. Schrödinger

first drew attention to Kramers¹⁾ on the basis of correspondenceal considerations. In general, our formula — despite the very different designation and way of thinking — can probably be described as formally identical to Kramer's secondary radiation formula. The important relationship between secondary radiation coefficients and spontaneous radiation coefficients $a_{kn}$, $b_{kn}$ is put into evidence and the secondary radiation is also described in detail with regard to its polarization state.²⁾

As far as the absolute amount of the scattered radiation or the induced dipole moment is concerned, I would like to believe that it is also correctly represented by formula (23), although a mistake in the numerical factor in the application of the heuristic hypothesis introduced above is of course within the realm of possibility. In any case, the physical dimension is the correct one, because since the square integrals of the eigenfunctions are normalized to one, the $a_{kn}$, $b_{kn}$ according to (18), (19), (21), (22) electrical moments. The ratio of the induced dipole moment to the spontaneous one is when $\nu$ is far away from the emission frequency in question, in order of magnitude equal to the ratio of the potential additional energy $F a_{kn}$ to the "energy level" $E_k - E_n$.

### § 3. Additions to § 2: Excited Atoms, Degenerate Systems, Range of Sections

For the sake of clarity, some special assumptions were made in the previous paragraph and some questions were set aside, which now have to be considered retrospectively.

First, what happens when the light wave transforms the atom

1) H. A. Kramers, Nature 10 May 1924; there 30 August 1924; H. A. Kramers and W. Heisenberg, Ztschr. f. Phys. 31. p. 681. 1925. The correspondenceal description of the polarization of scattered light given at the latter place (Gl. 27) is identical with ours *formal* almost identical.

2) It is hardly necessary to say that the two directions which we have called "x-direction" and "y-direction" for the sake of simplicity need not be directly perpendicular to each other. One is the polarization direction of the incident wave, the other is the polarization component of the secondary wave in which one is currently interested.

Quantization as an eigenvalue problem

121

in a state in which, as previously assumed, not only the *a* free oscillation $u_k$ but several, let's say two, $u_k$ and $u_l$? As already mentioned above, in the event of a malfunction, the two following the index $k$ and the index $l$ corresponding perturbation solutions (16) after they have been attached to constant (possibly complex) coefficients which are the *Strength* and the phase ratio of their excitation. One can probably overlook, without actually carrying out the calculation, that then in the expression for $\psi \bar{\psi}$ and likewise in the expression (23) for the resultant electric moment *not only* the corresponding linear aggregate of the previously obtained terms, i.e., the expressions (17) or (23), occurs once with $k$, the other time with $l$ ; but there are also "combination links", namely *First,*, of the highest order of magnitude, a limb with

$$24) \quad u_k(x) u_l(x) e^{\frac{2\pi i}{h} (E_k - E_l)t}$$

which the *spontaneous* charisma that has to do with the coexistence of the two *free* vibrations; *Secondly,* first-order perturbations that are proportional to the perturbing field amplitude and are proportional to the interaction of the $u_k$ forced oscillations with the free oscillation $u_l$ — and the $u_l$ forced oscillations with $u_k$ . The *Frequency* of these new members appearing in (17) or (23) is, as one can probably see even without carrying out the calculation, *not* $v$, but

$$(25) \quad |v \pm (E_k - E_l)/h|.$$

(New "*Resonance denominator*", however, occur in these members *not* .) So we are dealing here with secondary radiation, the frequency of which does not coincide with the excitatory light frequency, nor with a spontaneous frequency of the system, but is a combination frequency of both.

The existence of this strange kind of secondary radiation was first postulated by Kramers and Heisenberg, loc. cit., on the basis of correspondence, and then by Born, Heisenberg and Jordan on the basis of the Heisen

122

E. Schrödinger

Berg's quantum mechanics.¹) As far as I know, it has not yet been experimentally proven in any case. The *present* Theory also shows very clearly that the occurrence of this scattered radiation is connected with special conditions, which probably require experiments to be carried out specifically for this purpose. Firstly, it is necessary to *two* Natural vibrations $u_k$ and $u_l$ *strong* so that all experiments carried out on atoms in the normal state are ruled out — and that is the vast majority. Secondly, at least *a* Third state of natural oscillation $u_n$ *exist* (i.e. *possible*, he does not need *aroused* which is compatible with both $u_k$ as well as with $u_l$ combined leads to strong spontaneous emission. This is because the product of the spontaneous emission coefficients concerned ($a_{kn} b_{ln}$ and $a_{ln} b_{kn}$), the exceptional scattered radiation to be found is proportional. The combination ($u_k, u_l$) did not need to emit vigorously in and of itself, it would do no harm if even — in the language of the older theory — this "transition were forbidden". Nevertheless, in practice one will also have to add this demand, namely the demand that the line ($u_k, u_l$) is really sent out vigorously during the experiment, because this is actually the only means of making sure that really *both* natural vibrations, and indeed in the same atomic individuals and in a sufficient number of such, are strongly excited. If we now consider that in the strong and most frequently studied series of terms, i.e., in the ordinary $s$-, $p$-, $d$-, $f$series, the ratios are usually such that two terms which strongly combine with a third do not do so among themselves, then a special selection of the test object and the experimental conditions really seems necessary in order to be able to expect the scattered radiation in question with certainty, especially since it is of a different frequency than the incident light and *therefore* do not give rise to dispersion or rotational polarization, but can only be noticed as scattered light on all sides.

The quantum mechanical dispersion theory of Born, Heisenberg and Jordan quoted above allows, as far as I can

1) Born, Heisenberg and Jordan, Ztschr. f. Phys. 35. p. 572. 1926.

Quantization as an eigenvalue problem

123

overlooked, despite its great formal similarity to the present one, *none* Considerations of the kind just carried out. Because she only speaks of *a* Mode of reaction of the atom against incident radiation. It conceives of the atom as a timeless whole, and has not yet been able to say how to express in its language the indisputable fact that the atom can be expressed at different times in the *various* conditions and then reacts in various ways to incident radiation.¹)

We now turn to another question. In § 2, all intrinsic values were defined as *discreet* and among each other *Miscellaneous* provided. We first drop the second premise and ask: what changes when *Multiple* eigenvalues, i.e. if *Degeneracy* ? Perhaps it is expected that similar complications will then arise as we have encountered in the case of a temporally constant perturbation (third communication, § 2), i.e., that only by solving a "secular equation" can a system of proper functions of the undisturbed atom adapted to the particular perturbation be determined and used to carry out the perturbation calculation. This applies in the case of a *any* Disruption $r(x, t)$, as we had set it up in Eq. (5), but it is precisely in the case of disturbance by a light wave, Eq. (6) that it is true *not* at least in the first approximation pursued so far and as long as the assumption is adhered to that the frequency of light $\nu$ does not coincide with any of the spontaneous emission frequencies under consideration. In this case, the parameter value in the double equation established for the amplitudes of the perturbation vibrations (13) *none* eigenvalue and the pair of equations always has the unique solution pair (14), in which no vanishing denominators occur, even if $E_k$ is a multiple intrinsic value. The following are *not* the totals for which $E_n = E_k$ is to be suppressed, just as little as the sum term $n = k$ himself. It is noteworthy that through these links — if any of them are really, i.e., with

1) To this difficulty, the *Timeline* To comprehend an event, compare especially the concluding words in Heisenberg's most recent exposition of his theory, Math. Ann. 95, p. 683, 1926.

124

E. Schrödinger

non-vanishing $a_{kn}$, occurs — so does the frequency $v = 0$ among the resonant frequencies. To the "ordinary" scattered radiation, these members certainly furnish, as can be seen from (23), because of $E_k - E_n = 0$ no contribution.

The simplification that one does not need to take special account of a possible degeneracy, at least in the first approximation, always occurs, as we shall consider below (cf. § 5), when, as is the case with the light wave, the temporal mean value of the perturbation function disappears or, which is the same thing, when its temporal Fourier development does not have a constant,  i.e. contains a term independent of time.

So while our *first* prerequisite for eigenvalues — that they *Simple* — has actually proven to be a superfluous caution, a departure from the *second* — that they are quite *discreet* — although there are also no *principle* changes, but nevertheless quite considerable changes in the external habitus of the calculation, namely in addition to the discrete sums in (14), (16), (17), (23) *Integrals* via the range of distances of equation (1'). The theory of such integral representations is by H. Weyl$^{1)}$, however, was only developed for ordinary differential equations, but the transfer to partial equations should probably be permitted. The facts of the case are this in a nutshell.$^{2)}$ If the homogeneous equation belonging to the inhomogeneous equations (13), i.e., the oscillation equation (1') of the unperturbed system, possesses, in addition to a point spectrum, a range of distances which is of $E = a$ to $E = b$ may be sufficient, then an arbitrary function can be $f(x)$ of course no longer according to the standardised discrete eigenfunctions $u_n(x)$ develop alone:

$$(26) \quad f(x) = \sum_{n=1}^{\infty} \varphi_n \cdot u_n(x) \quad \text{mit} \quad \varphi_n = \int f(x) u_n(x) \varrho(x) \, dx,$$

1) H. Weyl, Math. Ann. 68. p. 220. 1910; God. Nachr. 1910. Cf. also E. Hilb, Sitz.-Ber. d. Physics. Mediz. Soc. Erlangen 43. p. 68. 1911; Math. Ann. 71, p. 76, 1911. — I am indebted to Mr. H. Weyl not only for these references, but also for very valuable oral instruction in these not very simple things.

2) I owe the presentation given here to Mr. E. Fues.

Quantization as an eigenvalue problem

125

but an integral development according to the intrinsic solutions $u(x, E)$, which belongs to the eigenvalues $a \leqslant E \leqslant b$ are added:

$$(27) \quad f(x) = \sum_{n=1}^{\infty} \varphi_n \cdot u_n(x) + \int_a^b u(x, E) \varphi(E) \, dE,$$

where, in order to emphasize the analogy for the "coefficient function" $\varphi(E)$ deliberately choose the same letter as for the discrete coefficients $\varphi_n$. If you now have your own solution $u(x, E)$ once and for all by attaching it with a suitable function of $E$ in such a way *standardised*that

$$(28) \quad \int dx \, \varrho(x) \int_{E'}^{E'+\Delta} u(x, E) u(x, E') \, dE' = 1 \\ \text{bzw.} = 0,$$

depending on the $E$ the interval $E'$, $E' + \Delta$ *listened to* or not, then in development (27) under the integral sign is to be placed:

$$(29) \quad \varphi(E) = \lim_{\Delta=0} \frac{1}{\Delta} \int \varrho(\xi) f(\xi) \cdot \int_{E}^{E'+\Delta} u(\xi, E') \, dE' \cdot d\xi,$$

whereby the *first* integral signs, as always, refer to the basic area of the variable group $x$ ¹⁾ Assuming the satisfiability of (28) and the existence of development (27) — both of which, as Weyl has said, has been proved for ordinary differential equations — the determination of the "coefficient function" according to (29) is almost as obvious as the well-known determination of Fourier coefficients.

The most important and most difficult task in a specific individual case is the implementation of the standardization of $u(x, E)$, i.e. the search for the function of $E$ by which the intrinsic solution of the range of distances, which is initially not standardized, is to be multiplied in order to satisfy condition (28). For this practical task, too, Mr. Weyl's above-quoted works contain very much

¹⁾ As Mr. E. Fues informs me, in practice it is very often permissible to suppress the borderline process and for the inner integral $u(\xi, E)$ writing; namely, whenever $\int \varrho(\xi) f(\xi) u(\xi, E) \, d\xi$ exists.

Annals of Physics. IV. Folge. 81.

9

126

E. Schrödinger

valuable instructions and some calculated examples. An example from atomic dynamics is given in a treatise by Mr. Fues on the intensities of the band spectra, which appears at the same time in these annals.

We now apply this to our problem, i.e. to the solution of the pair of equations (13) for the amplitudes $w_{\pm}$ of the disturbance vibrations, although we still assume that the *a* aroused *free* Vibration $u_k$ belongs to the discrete point spectrum. We develop the right side of (13) according to the scheme (27)

$$(30) \quad \frac{4\pi^2}{h^2} A(x) u_k(x) = \frac{4\pi^2}{h^2} \sum_{n=1}^{\infty} a'_{kn} u_n(x) + \frac{4\pi^2}{h^2} \int_a^b u(x, E) a'_k(E) dE,$$

where $a'_{kn}$ by (15) and $a'_k(E)$ after (29) by

$$(15') \quad a'_k(E) = \lim_{\Delta=0} \frac{1}{\Delta} \int \varrho(\xi) A(\xi) u_k(\xi) \cdot \int_E^{E+\Delta} u(\xi, E') dE' \cdot d\xi$$

is given. If you think of the development (30) in (13), then the solution you are looking for will also develop $w_{\pm}(x)$ in a completely analogous way according to the in-house solutions $u_n(x)$ and $u(x, E)$ and takes into account that for the latter functions the left side of (13)

$$\frac{8\pi^2}{h^2} (E_k \pm h\nu - E_n) u_n(x)$$

or

$$\frac{8\pi^2}{h^2} (E_k \pm h\nu - E) u(x, E)$$

, then by "coefficient comparison" as a generalization of (14)

$$(14') \quad w_{\pm}(x) = \frac{1}{2} \sum_{n=1}^{\infty} \frac{a'_{kn} u_n(x)}{E_k - E_n \pm h\nu} + \frac{1}{2} \int_a^b \frac{a'_k(E) u(x, E)}{E_k - E \pm h\nu} dE.$$

The further implementation is completely analogous to that in § 2. After all, as a *Additional link* To (23)

$$(23') + 2 \cos 2\pi\nu t \int d\xi \varrho(\xi) M_y(\xi) u_k(\xi) \int_a^b \frac{(E_k - E)a'_k(E) u(\xi, E)}{(E_k - E)^2 - h^2\nu^2} dE.$$

Quantization as an eigenvalue problem

127

In this case, the sequence of integration may not always be easily reversed, because the integral is $\xi$ may not converge. However, one can — a vivid surrogate of an exact border crossing, which may be passed over here — use the integral $\int_a^b$ into many small pieces, let's say of the length $\Delta$ sufficiently small to accommodate all the functions of the $E$ to be regarded as constant on such a piece, with the exception of $u(x, E)$, for which, as follows from the general theory, this is not determined by a fixed $\xi$ independent interval division can be achieved. Then you can lift out the other functions from the sub-path integrals and finally get exactly as *Auxiliary element to the secondary radiating dipole moment* (23) The following:

$$(23') \quad 2 F \cos 2 \pi \nu t \int_a^b \frac{(E - E_b) \alpha_b(E) \beta_b(E)}{(E_b - E)^2 - h^2 \nu^2} dE$$

with

$$(22') \quad \alpha_b(E) = \lim_{\Delta = 0} \frac{1}{\Delta} \int \varrho(\xi) M_z(\xi) u_k(\xi) \cdot \int_E^{E+\Delta} u(\xi, E') dE' \cdot d\xi$$

$$(19') \quad \beta_b(E) = \lim_{\Delta = 0} \frac{1}{\Delta} \int \varrho(\xi) M_y(\xi) u_k(\xi) \cdot \int_E^{E+\Delta} u(\xi, E') dE' \cdot d\xi$$

(I ask you to note the full analogy to the formulas of § 2, which are provided with the same number, without dashes).

The foregoing sketch of the calculation cannot, of course, be more than a general framework, it is merely intended to show that the much-discussed influence of the continuous spectrum on dispersion, which experience has shown to be present, seems to be present$^{1)}$, is demanded by the present theory exactly in the expected form, and it should outline the way in which the problem will have to be tackled mathematically.

#### § 4. Discussion of the Resonance Case

So far, we have always assumed that the frequency $\nu$ of the incident light wave with none of the

1) K. F. Herzfeld and K. L. Wolf, Ann. d. Phys. 76. S. 71. 567. 1925; H. Kollmann and H. Mark, Die NW. 14. p. 648. 1926.

9\*

128

E. Schrödinger

emission frequencies. We now assume that it is about

$$(31) \quad h\nu = E_n - E_k > 0,$$

whereby, for the sake of the simpler way of speaking, we return to the restrictive assumptions of § 2 (simple, discrete eigenvalues, a single free oscillation $u_k$ excited). In the equation pair (13), the eigenvalue parameter then receives the values

$$(32) \quad E_k \pm E_n \mp E_k = \begin{cases} E_n \\ 2E_k - E_n \end{cases}$$

This means that for the upper character there is a *Intrinsic value*, namely $E_n$. — Then two cases are possible. Either the $\varrho(x)$ multiplied right side of this equation *stands vertically* on the corresponding eigenfunction $u_n(x)$, i.e. it is

$$(33) \quad \int A(x)u_k(x)u_n(x)\varrho(x)dx = a'_{kn} = 0$$

or physically: $u_k$ and $u_n$ If they exist side by side as free oscillations, they would give rise either to none at all or to a spontaneous emission polarized perpendicular to the polarization direction of the incident light. In this case, the critical equation (13) still has a solution, which is still given by (14), in which the catastrophic term disappears. Physically, this means — in the old way of speaking — that a "forbidden transition" cannot be stimulated by resonance, or that a "transition", even if it is not forbidden, cannot be stimulated by light that oscillates perpendicular to the polarization direction of the light that would be emitted during the "spontaneous transition".

Or secondly, (33) is *not* fulfilled. Then the critical equation *none* Solution. The approach (10), which assumes an oscillation which is only *little* — by quantities of the order of the light amplitude $F$ — differs from the original free oscillation, and *under this assumption* the *most common* is, *does not lead to the goal*. So there is no solution that is only about quantities of the order $F$ from the originally existing free oscillation, the incident

Quantization as an eigenvalue problem

129

Light has thus contributed to the state of the system *a changing influence that is disproportionate to the magnitude of the light amplitude*. Which one? This, too, can still be judged without a new calculation, since we assume the case that the resonance condition (31) is not fulfilled exactly, but only approximately. Then you can see (16) that $u_n(x)$ is stimulated to unusually strong forced oscillations because of the low denominator, and that — what is no less important — the frequency of these forced oscillations corresponds to the natural natural frequency. $E_n/h$ of natural oscillation $u_n$ approaches. (All of this is very *Similar*, but still in a peculiar way *different* than with other known resonance phenomena, otherwise I wouldn't discuss it in such detail.)

Thus, with a gradual approach to the critical frequency, the previously unexcited natural oscillation $u_n$, the possibility of which is responsible for the crisis, is stimulated more and more strongly and at the same time more and more approximate and approached with its peculiar natural frequency. In contrast to ordinary resonance phenomena, however, there comes a moment, and indeed even before the critical frequency is reached, when our solution no longer grasps the facts correctly, even under the assumption that our apparently "damping-free" wave approach is exactly right. Because we have the forced vibration $w$ considered small compared to the existing free oscillation and [in Equation (11)] a square member was omitted.

I believe that the foregoing considerations already show with sufficient clarity that in the event of resonance the theory will really produce the result it must give in order to be in agreement with Wood's resonance phenomenon: an escalation of the natural vibration which gives rise to the crisis $u_n$ to finite, with that of the originally existing $u_k$ of comparable size, which of course then results in "spontaneous emission" of the spectral line ($u_k, u_n$) follows. At this point, however, I do not want to try to really carry out the calculation for the resonance case, because the result would only be of little value as long as the *Retroactive effect* of the emitted radiation on the emitting radiation

130

E. Schrödinger

system is not invoiced. Such a reaction must exist, not only because there is no reason at all to make a fundamental distinction between the light wave incident from outside and the light wave emitted by the system itself, but also because otherwise in a system left to itself, if several natural vibrations are excited at the same time, the spontaneous emission would continue indefinitely. The feedback to be required must have the effect that in this case, hand in hand with the emission of light, the higher natural vibrations gradually subside and finally the only basic vibration remains, which corresponds to the normal state of the system. The feedback is apparently the exact analogue of the reaction force of radiation $$\left( \frac{2e^2}{3m\sigma^3} \ddot{v} \right)$$ with the classical electron. This analogy also appeases the rising concern about the previous failure to take feedback into account. The influence of the relevant (probably no longer linear) term in the wave equation will generally be small, just as in the case of the electron the reaction force of the radiation is generally very small against the inertial force and against the external field force. In the case of resonance, however, just as in the electron theory, the coupling with the intrinsic light wave will be of the same order of magnitude as that with the incident wave, and will have to be taken into account if one wants to correctly calculate the "equilibrium" between the various natural oscillations that occurs under a given irradiation.

However, it should be expressly noted: *to avoid a resonance catastrophe* would be the feedback link *not* required! Such a situation cannot occur under any circumstances because, according to the sentence of the *Persistence of normalization* the configuration space integral of $$\psi\ddot{\psi}$$ always remains normalized to the same value even under the action of any external forces — and quite automatically, as a result of the wave equations (4'). The amplitudes of the $$\psi$$oscillations can therefore not grow indefinitely, they always have the same value "on average". If *a* natural oscillation, another must decrease for it.

Quantization as an eigenvalue problem

131

# § 5. Generalization for any disorder

If there is a *any* disturbance, as was initially assumed in Gl. (5) at the beginning of § 2, then the disturbance energy will be $r(x, t)$ into a Fourier series or into a Fourier integral according to time. The members of this development then have the form (6) of the perturbation potential of a light wave. You can easily overlook the fact that you are then simply in the Eq. (11) on the right side two *Rows* (or possibly integrals) of imaginary *e*potencies, instead of just two. If none of the exciting frequencies coincides with a critical frequency, the solution is obtained exactly in the way indicated in § 2, namely as Fourier series (or possibly Fourier integrals) of time. There seems to be no point in writing down the formal developments here, and a closer follow-up of individual problems is outside the scope of this Communication. However, an important circumstance, which has already been touched upon in § 3, must be mentioned.

Among the critical frequencies of equation (13) is generally the frequency $v = E_k - E_k = 0$. For them, too, an eigenvalue occurs as an eigenvalue parameter on the left, namely $E_k$. So in the Fourier development of the perturbation function $r(x, t)$ if the frequency 0, i.e. a term independent of time, occurs, one does not arrive exactly on the earlier path to the goal. But it is easy to see how it is to be changed, because the case of a constant disturbance in time is known to us from earlier times (see third communication). One must then take into account a slight displacement and possibly splitting of the eigenvalue or eigenvalues of the excited free oscillations, i.e., one has in the exponent of the *e*power of the first member of the right hand of the Eq. (10) $E_k$ to write: $E_k$ plus a small constant, the eigenvalue disorder. This intrinsic value disturbance is determined, exactly as described in the third communication § 1 and § 2, from the requirement that the right side of the critical Fourier component of the present Equ. (13) should be reduced to $u_k$ (or possibly: on *all* to $E_k$ proper functions) should be vertical.

The number of special problems that fall under the question of the present paragraph is extraordinary

132

E. Schrödinger

great. By superpositioning the disturbance by a constant electric or magnetic field and by a light wave, magnetic and electric birefringence and magnetic rotational polarization are achieved. The resonance radiation in the magnetic field also belongs here, but for this purpose the resonance case discussed in § 4 must first be given an exact solution. Furthermore, the effect of a passing atom will be $\alpha$particle or electron in the specified way$^{1)}$if the encounter is not too close to be able to calculate the disturbance of each of the two systems from the undisturbed movement of the other. All these questions are a mere matter of calculation as soon as the eigenvalues and eigenfunctions of the unperturbed systems are known. It is therefore very much to be hoped that it will be possible to determine these functions at least approximately, at least approximately, for higher atoms, by analogy with the approximate determination of Bohr's electron orbits, which belong to the different types of terms.

#### § 6. Relativistic-magnetic generalization of the basic equations

Following on from the physical problems mentioned above, where the *Magnetic field* plays an important role, I would now like to briefly share the presumed relativistic-magnetic generalization of the basic equations (4') here, even if I can only do it for the one-electron problem and only with the greatest reserve for the time being. The latter for two reasons. First, the generalization is based on purely formal analogy for the time being. Secondly, as already stated in the *first* Announcement$^{1)}$ In the case of the Kepler problem, it is true that Sommerfeld's fine-structure formula is formally reduced, namely with a "half-numbered" azimuthal

1) A very interesting and successful attempt to compare the effect of charged particles flying by Fourier decomposition of their field with the effect of light waves can be found in E. Fermi, Ztschr. f. Phys. 29, p. 315, 1924.

1) Ann. d. Phys., 79. p. 372. 1926.

Quantization as an eigenvalue problem

133

and radialquant, which is generally considered correct today; only the supplement necessary for the production of numerically correct splitting images of the hydrogen lines is still missing, which is supplied in Bohr's picture by Goudsmit-Uhlenbeck's electron spin.

Hamilton's partial differential equation for Lorentz's electron can easily be put into the following form

$$(34) \begin{cases} \left( \frac{1}{c} \frac{\partial W}{\partial t} + \frac{e}{c} V \right)^2 - \left( \frac{\partial W}{\partial x} - \frac{e}{c} \mathfrak{A}_x \right)^2 - \left( \frac{\partial W}{\partial y} - \frac{e}{c} \mathfrak{A}_y \right)^2 \\ - \left( \frac{\partial W}{\partial z} - \frac{e}{c} \mathfrak{A}_z \right)^2 - m^2 c^2 = 0 \ . \end{cases}$$

Here are $e, m, c$ charge, mass of the electron and speed of light; $V, \mathfrak{A}$ are the electromagnetic potentials of the external electromagnetic field at the electron location. $W$ is the effect function.

From the classical (relativistic) equation (34) I now try to derive the wave equation for the electron by the following purely formal procedure, which, as one might easily consider, would lead to equations (4") if applied to Hamilton's equation of a mass point of ordinary (non-relativistic) mechanics moving in any force field. — I replace the sizes in (34) after squaring

$$(35) \begin{cases} \frac{\partial W}{\partial t}, \frac{\partial W}{\partial x}, \frac{\partial W}{\partial y}, \frac{\partial W}{\partial z}, \\ \text{bezw. durch die Operatoren} \\ \pm \frac{h}{2\pi i} \frac{\partial}{\partial t}, \pm \frac{h}{2\pi i} \frac{\partial}{\partial x}, \pm \frac{h}{2\pi i} \frac{\partial}{\partial y}, \pm \frac{h}{2\pi i} \frac{\partial}{\partial z} \ . \end{cases}$$

The linear double operator obtained in this way, exercised on a wave function $\psi$ I set it to zero:

$$(36) \begin{cases} \Delta \psi - \frac{1}{c^2} \frac{\partial^2 \psi}{\partial t^2} \mp \frac{4\pi i e}{hc} \left( \frac{V}{c} \frac{\partial \psi}{\partial t} + \mathfrak{A} \text{grad } \psi \right) \\ + \frac{4\pi^2 e^2}{h^2 c^2} \left( V^2 - \mathfrak{A}^2 - \frac{m^2 c^4}{c^2} \right) \psi = 0 \ . \end{cases}$$

(The signs $\Delta$ and degrees have the elementary three-dimensional Euclidean significance here.) The pair of equations (36) would be the presumed relativistic-magnetic generalization

134

E. Schrödinger

of (4') for the case of a single electron, and it would also be understood in the sense that the complex wave function has to satisfy either one or the other equation.

For the hydrogen atom, Sommerfeld's fine-structure formula can be obtained from (36) exactly according to the method described in the first communication, and likewise (neglecting the term with $\mathfrak{N}^2$) derive the normal Zeemanffekt, as well as the well-known rules of selection and polarization together with intensity formulas; they follow from the integral relations between the spherical functions given at the end of the third communication.

For the reasons given in the first paragraph of this paragraph, I will refrain from the detailed reproduction of these calculations for the time being, and in the following final paragraph I will also refer to the "classical" and not to the still imperfect relativistic-magnetic version of the theory.

#### § 7. On the physical significance of the field scalar

In § 2, the *One-electron problem* heuristic hypothesis about the electrodynamic significance of the field scalar $\psi$ unceremoniously generalized to an arbitrary system of loaded mass points and promised a more detailed discussion of this procedure. We had calculated the density of electricity in any point of space as follows: *a* point of mass, holds the coordinate triple, which, according to ordinary mechanics, *its* Location describes, fixed, integrated $\psi \bar{\psi}$ over all other system coordinates and multiplies the result by a certain constant, the "charge" of the mass point picked out; in the same way one proceeds with each point of mass (triple of coordinates), whereby the mass point taken out in each case is given the same position each time, namely the position of the one *Space Point*, in which one wishes to learn about the electricity density. The latter is equal to the algebraic sum of the partial results.

This provision is now equivalent to the following view, which defines the actual meaning of $\psi$ better

Quantization as an eigenvalue problem

135

emerges. $\psi \bar{\psi}$ is a kind of *Weight function* in the configuration space of the system. The *Wave mechanical* configuration of the system is a *Superposition* many, strictly speaking *of all*, kinematically possible point mechanical configurations. Each point mechanical configuration controls with a certain *Weight* contribute to the true wave-mechanical configuration, which means that the weight is $\psi \bar{\psi}$ is given. If you love paradoxes, you can say that the system is in all kinematically conceivable positions at the same time, but not in all of them "equally strong". In macroscopic movements, the weight function practically contracts to a small area of practically indistinguishable layers, whose center of gravity covers macroscopically perceptible distances in the configuration space. In any case, microscopic movement problems are of interest *also*, and for certain questions even *first and foremost*, the changing *Distribution* about the area.

This reinterpretation may be choquing at first, after we have so far often spoken in such a vividly concrete form of the "$\psi$vibrations" as something very real. According to the current view, however, they are also based on something tangibly real, namely the highly real, electrodynamically effective fluctuations in the electrical density of space. The $\psi$function should be or achieve nothing more and nothing less than that it allows mathematically to control and overlook the totality of these fluctuations by means of a single partial differential equation. The fact that the $\psi$function itself in general cannot and must not be interpreted directly three-dimensionally spatially, as much as the one-electron problem tempts us to do so, because it is generally a function in configuration space, not in real space, has been emphasized several times.¹)

From a weight function in the sense described above, one would wish that its integral would remain constantly normalized over the entire configuration space to one and the same unchangeable value, preferably to one. In fact, it is easy to convince oneself that this is necessary so that

1) Ann. d. Phys. 79. S. 526. 754. 1926.

136

E. Schrödinger

according to the above definitions, the total charge of the system remains constant. And of course, this demand must also be made for non-conservative systems. Because, of course, the charge of a system must not change if, for example, a light wave enters, lasts for a while, then stops again. (NB.: This also applies to ionization processes. A separated particle must initially continue to be counted as part of the system until the separation is also *Logical* — by splitting the configuration space.)

The question now arises as to whether this *Persistence of normalization* by the equations of change (4') of p. 112, which are $\psi$ is actually guaranteed. If this were not the case, it would be quite catastrophic for our whole conception. Fortunately, it is. Let's form

$$(37) \quad \frac{d}{dt} \int \psi \, \bar{\psi} \, \varrho \, dx = \int \left( \psi \frac{\partial \psi}{\partial t} + \bar{\psi} \frac{\partial \psi}{\partial t} \right) \varrho \, dx \ .$$

Now all it takes is $\psi$ one of the two equations (4'), $\bar{\psi}$ i.e. the other. Therefore, apart from a multiplicative constant, the above integral becomes:

$$(38) \quad \int (\psi \, \Delta \bar{\psi} - \bar{\psi} \, \Delta \psi) \varrho \, dx = 2i \int (J \, \Delta R - R \, \Delta J) \varrho \, dx \ ,$$

whereby for the moment

$$\psi = R + iJ$$

is set. The integral (38) disappears identically according to Green's theorem; the only condition that makes the functions $R$ and $J$ have to suffice for this — to disappear sufficiently strongly into infinity — means physically nothing other than that the system under consideration is practically limited to a *finite* area.

One can turn the foregoing somewhat differently by not integrating over the entire configuration space, but merely transforming the temporal differential quotient of the weight function into a divergence by Green's transformation. This gives an insight into the flow conditions, first of all of the weight function and through it: of electricity. The Two Equations

Quantization as an eigenvalue problem

137

$$(4') \left\{ \begin{array}{l} \frac{\partial \psi}{\partial t} = \frac{h}{4\pi i} \left( \Delta - \frac{8\pi^2}{h^2} V \right) \psi \\ \frac{\partial \psi}{\partial t} = - \frac{h}{4\pi i} \left( \Delta - \frac{8\pi^2}{h^2} V \right) \bar{\psi} \end{array} \right.$$

multiply by $\varrho \bar{\psi}$ or $\varrho \psi$ and add them:

$$(39) \quad \frac{\partial}{\partial t} (\varrho \psi \bar{\psi}) = \frac{h}{4\pi i} \varrho \cdot (\bar{\psi} \Delta \psi - \psi \Delta \bar{\psi}) .$$

In order to perform the transformation of the right side into extenso, one must remember the explicit form of our multidimensional non-Euclidean Laplacean operator$^{1)}$:

$$(40) \quad \varrho \Delta = \sum_k \frac{\partial}{\partial q_k} \left[ \varrho T_{p_k} \left( q_i, \frac{\partial \psi}{\partial q_i} \right) \right] .$$

You can then easily find by a small transformation:

$$(41) \left\{ \begin{array}{l} \frac{\partial}{\partial t} (\varrho \psi \bar{\psi}) = \frac{h}{4\pi i} \sum_k \frac{\partial}{\partial q_k} \left[ \varrho \bar{\psi} T_{p_k} \left( q_i, \frac{\partial \psi}{\partial q_i} \right) - \right. \\ \left. - \varrho \psi T_{p_k} \left( q_i, \frac{\partial \psi}{\partial q_i} \right) \right] . \end{array} \right.$$

The right side appears as a divergence of a multidimensional real vector, which appears to be the *Current Density of Weight Function* is to be interpreted in the configuration space. Eq. (41) is the *Continuity equation* the weight function.

From it you can use the *Continuity equation of electricity* and this applies individually to the charge density "originating from each individual point of mass". For example, if we take the $\alpha$-th point of mass, its "charge" is $e_a$, its mass $m_a$, its coordinate space is described by Cartesian coordinates for simplicity's sake, $x_a, y_a, z_a$. We denote the product of the differentials of the *Other* Coordinates abbreviated with $dx'$. It is used to integrate the

1) Ann. d. Phys. 79. p. 748. 1926, equation (31). The $\Delta_p - \frac{1}{2}$ is our "density function" $\varrho(x)$ (e.g. $r^2$ sin $\vartheta$ for a polar coordinate triple). $T$ is the kinetic energy as a function of the position coordinates and *Impulses*, the index at $T$ means the derivative according to an impulse coordinate. — In equations (31) and (32), loc. cit., the index was unfortunately inadvertently $k$ twice, once as a summation index, but then also as a representative index in the argument of functions.

138

E. Schrödinger

Eq. (41), with a fixed $x_a, y_a, z_a$. In this integration, all but three of the links on the right hand are removed, and one obtains:

$$(42) \begin{cases} \frac{\partial}{\partial t} \left[ e_a \int \psi \bar{\psi} \, dx' \right] = \frac{h e_a}{4 \pi i m_a} \left\{ \frac{\partial}{\partial x_a} \left[ \int \left( \bar{\psi} \frac{\partial \psi}{\partial x_a} - \psi \frac{\partial \psi}{\partial x_a} \right) dx' \right] + \right. \\ \left. + \frac{\partial}{\partial y_a} \left[ \int \left( \bar{\psi} \frac{\partial \psi}{\partial y_a} - \psi \frac{\partial \psi}{\partial y_a} \right) dx' \right] + \cdot \right\} \\ = \frac{h e_a}{4 \pi i m_a} \text{div}_a \left[ \int (\bar{\psi} \text{grad}_a \psi - \psi \text{grad}_a \bar{\psi}) \, dx' \right]. \end{cases}$$

In this equation, div and grad have the usual three-dimensional-Euclidean meaning and they are $x_a, y_a, z_a$ as Cartesian coordinates of real space. The equation is the continuity equation of the charge density, which is "determined by the $\alpha$-th mass point". If you form the others analogously and add them all, you get the general continuity equation. Of course, it must be emphasized that, as always in such cases, the conception of the integrals on the right hand as components of the current density is not absolutely inevitable, because a divergence-free vector could be added.

To give an example, for the conservative one-electron problem, if $\psi$ by

$$(43) \quad \psi = \sum_k c_k u_k e^{2 \pi i v_k t + i \vartheta_k} \quad (c_k, \vartheta_k \text{ reelle Konstante})$$

given as current density $J$

$$(44) \begin{cases} J = \frac{h e_l}{2 \pi m_l} \sum_{(k,l)} c_k c_l (u_l \text{grad } u_k - u_k \text{grad } u_l) \\ \cdot \sin [2 \pi (v_k - v_l) t + \vartheta_k - \vartheta_l]. \end{cases}$$

It can be seen, and this is generally true of conservative systems, that if only a single natural oscillation is excited, the current components disappear and the distribution of electricity becomes constant in time; which one immediately overlooks, since $\psi \bar{\psi}$ becomes constant over time. This is also true if several natural oscillations are excited, but all belong to the same eigenvalue. On the other hand, the current density does not have to disappear anymore, but there can and generally will be stationary current distribution. Since one or the other is true in the undisturbed normal state, one can in a certain sense assume a return to electrostatic and magnetostatic

Quantization as an eigenvalue problem

139

static atomic models. In this way, however, the absence of radiation in the normal state finds an amazingly simple solution.

I hope and believe that the above approaches will prove useful in explaining the magnetic properties of atoms and molecules and also in explaining the flow of electricity in solid bodies.

There is no doubt that there is still a certain hardship in the use of a *complex* Wave function. Would she *Basically* unavoidable and not a mere calculation facilitation, this would mean that in principle *two* wave functions exist that only *together* provide information about the state of the system. This somewhat unsympathetic conclusion admits, I believe, of the much more sympathetic interpretation that the state of the system is given by a real function and its derivation according to time. The fact that we are not yet able to give more precise information on this is due to the fact that in the pair of equations (4') we have only the — which, however, is extremely convenient for the calculation — *Surrogate* of a real wave equation of probably the fourth order, which I did not want to succeed in establishing in the non-conservative case.

Zurich, Institute of Physics of the University.

(Received June 21, 1926)
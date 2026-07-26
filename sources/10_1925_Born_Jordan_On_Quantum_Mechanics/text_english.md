858

## On quantum mechanics.

By M. Born and P. Jordan in Göttingen.

(Received September 27, 1925.)

The approaches recently given by Heisenberg are developed (initially for systems of one degree of freedom) into a systematic theory of quantum mechanics. The mathematical tool is the matrix calculus. After this has been briefly presented, the mechanical equations of motion are derived from a principle of variation and the proof is presented that on the basis of Heisenberg's quantum condition, the energy law and Bohr's frequency condition follow from the mechanical equations. Using the example of the anharmonic oscillator, the question of the uniqueness of the solution and the significance of the phases in the partial oscillations is discussed. The conclusion is an attempt to insert the laws of the electromagnetic field into the new theory.

Introduction. The approaches to a new kinematics and mechanics recently shared by Heisenberg¹⁾ in this journal, which correspond to the basic requirements of quantum theory, seem to us to be of great importance. They mean an attempt to do justice to the new facts — instead of by more or less artificial and forced adaptation of the old familiar concepts — by creating a new, really appropriate system of concepts. Heisenberg has expressed the physical thoughts that guided him in such a clear way that any additional remark seems superfluous. But from a formal, mathematical point of view, his considerations, as he himself emphasizes, are only in the early stages. He explained his hypotheses only with simple examples and did not advance to a general theory. Favoured by the fact that we have already been able to get to know his reflections in statu nascendi, we have endeavored to clarify the mathematical and formal content of his approaches after completing his investigations and present here some of our results. They show that it is indeed possible to erect the edifice of a closed mathematical theory of quantum mechanics on the basis given by Heisenberg, in a remarkably close analogy to classical mechanics, but while preserving the features characteristic of quantum phenomena.

With Heisenberg, we first limit ourselves to systems of a degree of freedom, of which we assume that they are — classically speaking — periodic. The generalization of the

¹⁾ W. Heisenberg, ZS. f. Phys. 33, 879, 1925.

M. Born and P. Jordan, On Quantum Mechanics.

859

mathematical theory on systems of arbitrary degrees of freedom as well as on aperiodic motions will occupy us in the continuation of this treatise. In an essential generalization of Heisenberg's approaches, we will not limit ourselves to the treatment of non-relativistic mechanics, nor to the calculation with Cartesian coordinates. The only limitation we impose on ourselves with regard to coordinates is that our considerations refer to libration coordinates, which in classical theory are periodic functions of time. However, in some cases it seems obvious to use other coordinates, for example the rotation angle for the rotator $\varphi$, which becomes a linear function of time. Heisenberg also proceeded in this way in his treatment of the rotator; however, it remains to be seen whether the procedure used can be justified from the point of view of consistent quantum mechanics.

The mathematical basis of Heisenberg's consideration is the multiplication law of quantum-theoretical quantities, which he has deduced through an ingenious correspondence consideration. The elaboration of his formalism, which we here give, is based on the remark that this rule is nothing but the law of the multiplication of matrices, well known to mathematicians. The quadratic scheme (with discrete or continuously running indices) that is infinite on two sides, the so-called matrix, is the representative of a physical quantity that is given as a function of time in classical theory. The mathematical method of the new quantum mechanics is therefore characterized by the use of matrix analysis instead of ordinary number analysis.

With this method, we have tried to tackle the simplest questions of mechanics and electrodynamics. A principle of variation suggested by correspondence considerations provides equations of motion for the most general Hamiltonian function in the closest analogy to the classical canonical equations. The quantum condition summarized with a relation flowing from the equations of motion allows a simple matrix notation. With their help, it is possible to prove the universality of the energy law and Bohr's frequency condition in the sense assumed by Heisenberg, a proof that he could not fully prove even for the simple examples he treated. We will then come to one of these examples in more detail

Journal of Physics. Vol. XXXIV.

57

860

M. Born and P. Jordan,

to gain a clue about the role that the phases of partial oscillations play in the new theory. In conclusion, we show that the fundamental laws of the electromagnetic field in a vacuum also fit into the new method without constraint, and give a justification of Heisenberg's assumption that the squares of the magnitudes of the elements of the matrix representing the electric moment of an atom are a measure of the transition probabilities.

### Chapter I. Matrix calculation.

§ 1. Elementary operations. Features. We calculate with square infinite matrices¹), which we will here designate with bold letters, while weak letters are always meant to mean ordinary numbers:

$$\boldsymbol{a} = (a(nm)) = \begin{pmatrix} a(00) & a(01) & a(02) \dots \\ a(10) & a(11) & a(12) \dots \\ a(20) & a(21) & a(22) \\ \dots & \dots & \dots & \dots \end{pmatrix}$$

Equality of two matrices means equality of corresponding components:

$$\boldsymbol{a} = \boldsymbol{b} \text{ heißt } a(nm) = b(nm). \quad (1)$$

Addition is defined by the addition of corresponding components

$$\boldsymbol{a} = \boldsymbol{b} + \boldsymbol{c} \text{ heißt } a(nm) = b(nm) + c(nm). \quad (2)$$

Multiplication is defined by the rule "rows times columns" known from determinant theory:

$$\boldsymbol{a} = \boldsymbol{b}\boldsymbol{c} \text{ heißt } a(nm) = \sum_{k=0}^{\infty} b(nk)c(km). \quad (3)$$

Powers are to be defined by repeated multiplication. The associative law applies to multiplication and the distributive law to the combination of addition and multiplication:

$$(\boldsymbol{a}\boldsymbol{b})\boldsymbol{c} = \boldsymbol{a}(\boldsymbol{b}\boldsymbol{c}): \quad (4)$$

$$\boldsymbol{a}(\boldsymbol{b} + \boldsymbol{c}) = \boldsymbol{a}\boldsymbol{b} + \boldsymbol{a}\boldsymbol{c}. \quad (5)$$

On the other hand, the commutative law for multiplication does not apply: the equation $\boldsymbol{a}\boldsymbol{b} = \boldsymbol{b}\boldsymbol{a}$ is not generally correct. If it applies,

¹) For more information on matrix calculus, see M. Böcher, Einführung in die höhere Algebra: aus dem Englischer von Hans Beck, Leipzig, Teubner, 1910, § 22 to 25; also in R. Courant and D. Hilbert, Methoden der mathematischen Physik I. Berlin, Springer, 1924, 1st chap.

On quantum mechanics.

861

will be $\boldsymbol{a}$ and $\boldsymbol{b}$ interchangeable. The

$$\boldsymbol{1} = (\delta_{nm}), \quad \begin{cases} \delta_{nm} = 0 & \text{für } n \neq m, \\ \delta_{nn} = 1 \end{cases} \quad (6)$$

defined unit matrix has the property

$$\boldsymbol{a}\boldsymbol{1} = \boldsymbol{1}\boldsymbol{a} = \boldsymbol{a}. \quad (6a)$$

The $\boldsymbol{a}$ reciprocal matrix $\boldsymbol{a}^{-1}$ is defined by$^{1)}$

$$\boldsymbol{a}^{-1}\boldsymbol{a} = \boldsymbol{a}\boldsymbol{a}^{-1} = \boldsymbol{1}. \quad (7)$$

As the "mean" of a matrix $\boldsymbol{a}$ we designate the matrix whose diagonal elements are identical with those of $\boldsymbol{a}$ while all other elements are zero:

$$\overline{\boldsymbol{a}} = (\delta_{nm} a (nn)). \quad (8)$$

The sum of these diagonal elements is supposed to be "diagonal sum of the matrix $\boldsymbol{a}$" and with $D(\boldsymbol{a})$ may refer to:

$$D(\boldsymbol{a}) = \sum_n a(nn). \quad (9)$$

According to (3), it is easy to prove: If the diagonal sum of a product $\boldsymbol{y} = \boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_m$ is finite, it remains unchanged when the factors are cyclically reversed:

$$D(\boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_m) = D(\boldsymbol{x}_r \boldsymbol{x}_{r+1} \dots \boldsymbol{x}_m \boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_{r-1}). \quad (10)$$

It is apparently sufficient to satisfy oneself of the correctness of the sentence for two factors.

Are the components of the matrices $\boldsymbol{a}, \boldsymbol{b}$ Functions of a parameter $t$, it will be

$$\frac{d}{dt} \sum_k a(nk) b(km) = \sum_k \{\dot{a}(nk) b(km) + a(nk) \dot{b}(km)\}$$

or according to the definition (3):

$$\frac{d}{dt}(\boldsymbol{a}\boldsymbol{b}) = \dot{\boldsymbol{a}}\boldsymbol{b} + \boldsymbol{a}\dot{\boldsymbol{b}}. \quad (11)$$

Repeated use of (11) gives

$$\frac{d}{dt}(\boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_n) = \dot{\boldsymbol{x}}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_n + \boldsymbol{x}_1 \dot{\boldsymbol{x}}_2 \dots \boldsymbol{x}_n + \dots + \boldsymbol{x}_1 \boldsymbol{x}_2 \dots \dot{\boldsymbol{x}}_n. \quad (11')$$

The computational processes (2), (3) can be used to define functions of matrices. As the most general function $f(\boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_m)$ should first of all be considered here, which is accompanied by a

$^{1)}$ As is well known, for finite quadratic matrices, $\boldsymbol{a}^{-1}$ is always clearly defined by this definition if the determinant $A$ by $\boldsymbol{a}$ is different from zero. Is $A = 0$, there are no $\boldsymbol{a}$ reciprocal matrix.

862

M. Born and P. Jordan,

Sum of finite or infinitely many potency products in the arguments $\mathbf{x}_k$ can be formally represented with numbers as coefficients. It can then also be determined by equations

$$\left. \begin{array}{l} f_1(y_1, \dots, y_n; x_1, \dots, x_n) = 0, \\ \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \end{array} \right\} \quad (12)$$

Features $\mathbf{y}_l(\mathbf{x}_1, \dots, \mathbf{x}_n)$ can be defined. Namely, in order to $\mathbf{y}_l$ of the form described above, which satisfies equations (12), one has only the $\mathbf{y}_l$ as series, which are based on potency products of the $\mathbf{x}_k$ and to determine the coefficients in turn by inserting them into (12). One recognizes that there are always as many equations as unknowns. The number of equations and unknowns is, of course, greater than in the application of the method of indeterminate coefficients in ordinary analysis, which calculates with commutative multiplication. In each of the equations (12), after inserting the series for the $\mathbf{y}_l$ and summary of the members belonging together except for a summand $C'\mathbf{x}_1\mathbf{x}_2$ also a summand $C''\mathbf{x}_2\mathbf{x}_1$ and has both $C'$ and $C''$ (not only $C' + C''$) to disappear. However, this is also reflected in the development of each $\mathbf{y}_l$ two links $\mathbf{x}_1\mathbf{x}_2$ and $\mathbf{x}_2\mathbf{x}_1$ with two available coefficients.

§ 2. Symbolic Differentiation. A computational process that was used much later on, which we want to take a closer look at here, should be called the differentiation of a matrix function. It must be observed, however, that this process possesses only in some points similar properties to the differentiation of ordinary analysis. For example, the product rule of differentiation or the rule for differentiating a function from a function are no longer generally valid. Only if all occurring matrices are interchangeable with each other do all the rules of ordinary analysis apply to this differentiation.

Let it be

$$\mathbf{y} = \prod_{m=1}^s \mathbf{x}_{l_m} = \mathbf{x}_{l_1}\mathbf{x}_{l_2} \dots \mathbf{x}_{l_r} \quad (13)$$

We define

$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}_k} = \sum_{r=1}^s \delta_{l_r k} \prod_{m=r+1}^s \mathbf{x}_{l_m} \prod_{m=1}^{m=r-1} \mathbf{x}_{l_m}, \quad \begin{cases} \delta_{jk} = 0 \text{ für } j \neq k, \\ \delta_{kk} = 1. \end{cases} \quad (14)$$

In words, this rule is: Think of all factors in the given product individually (e.g. not $\mathbf{x}_1^2 \mathbf{x}_2^2$, but

On quantum mechanics.

863

$x_1 x_1 x_2 x_2$); take any factor $x_k$ and form the product of all the factors that follow it and all the factors that precede it (in that order). The sum of all the terms thus formed is the differential quotient of the product according to this $x_k$.

A few examples may illustrate the procedure:

$$y = x^n, \quad \frac{dy}{dx} = nx^{n-1}$$

$$y = x_1^n x_2^m, \quad \frac{\partial y}{\partial x_1} = x_1^{n-1} x_2^m + x_1^{n-2} x_2^m x_1 + \dots + x_k^m x_1^{n-1},$$

$$y = x_1^2 x_2 x_1 x_3, \quad \frac{\partial y}{\partial x_1} = x_1 x_2 x_1 x_3 + x_2 x_1 x_3 x_1 + x_3 x_1^2 x_2.$$

Let us also demand

$$\frac{\partial(y_1 + y_2)}{\partial x_k} = \frac{\partial y_1}{\partial x_k} + \frac{\partial y_2}{\partial x_k}, \tag{15}$$

so is the derivation $\frac{\partial y}{\partial x}$ for the most general analytical functions $y$ defined.

With these definitions and that of the diagonal sum (9), the relationship

$$\frac{\partial D(y)}{\partial x_k (nm)} = \frac{\partial y}{\partial x_k} (mn), \tag{16}$$

where on the right the $mn$component of the matrix $\frac{\partial y}{\partial x_k}$ . This relationship can also be used to define the derivation $\frac{\partial y}{\partial x_k}$ can be used. In order to prove (16) it is evidently sufficient to have a function $y$ form (13). After (14) and (3),

$$\frac{\partial y}{\partial x_k} (mn) = \sum_{r=1}^s \delta_{l_r k} \sum_{\tau} \prod_{p=r+1}^s x_{l_p} (\tau_p \tau_{p+1}) \prod_{p=1}^{r-1} x_{l_p} (\tau_p \tau_{p+1}); \tag{17}$$

$$\tau_{r+1} = m, \quad \tau_{s+1} = \tau_1, \quad \tau_r = n.$$

On the other hand, it can be inferred from (3) and (9):

$$\frac{\partial D(y)}{\partial x_k (mn)} = \sum_{r=1}^s \delta_{l_r k} \sum_{\tau} \prod_{p=1}^{r-1} x_{l_p} (\tau_p \tau_{p+1}) \prod_{p=r+1}^s x_{l_p} (\tau_p \tau_{p+1}); \tag{17'}$$

$$\tau_1 = \tau_{s+1}, \quad \tau_r = n, \quad \tau_{r+1} = m.$$

Comparison of (17) and (17') gives (16).

A fact that is important for later and can be read from the definition (14) should be emphasized right here: the partial derivatives

864

M. Born and P. Jordan,

of a product are invariant to cyclic reversals of the factors. Because of (16), this sentence can also be inferred from (10).

At the end of these preparations, the functions of the $g(pq)$ of two variables. For

$$y = p^s q^r \quad (18)$$

will be named after (14)

$$\frac{\partial y}{\partial p} = \sum_{l=0}^{s-1} p^{s-1-l} q^r p^l, \quad \frac{\partial y}{\partial q} = \sum_{j=0}^{r-1} q^{r-1-j} p^s q^j. \quad (18')$$

The most general function to consider $g(pq)$ is to be represented according to § 1 by a linear aggregate of terms

$$z = \prod_{j=1}^k (p^{s_j} q^{r_j}). \quad (19)$$

With the abbreviation

$$P_l = \prod_{j=l+1}^k (p^{s_j} q^{r_j}) \prod_{j=1}^{l-1} (p^{s_j} q^{r_j}) \quad (20)$$

the derivatives can be written:

$$\left. \begin{aligned} \frac{\partial z}{\partial p} &= \sum_{l=1}^k \sum_{m=0}^{s_l-1} p^{s_l-1-m} q^{r_l} P_l p^m, \\ \frac{\partial z}{\partial q} &= \sum_{l=1}^k \sum_{m=0}^{r_l-1} q^{r_l-1-m} P_l p^{s_l} q^m. \end{aligned} \right\} \quad (21)$$

An important conclusion can be drawn from these equations. We look at the matrices

$$d_1 = q \frac{\partial z}{\partial q} - \frac{\partial z}{\partial q} q, \quad d_2 = p \frac{\partial z}{\partial p} - \frac{\partial z}{\partial p} p. \quad (22)$$

After (21),

$$d_1 = \sum_{l=1}^k (q^{r_l} P_l p^{s_l} - P_l p^{s_l} q^{r_l}),$$

$$d_2 = \sum_{l=1}^k (p^{s_l} q^{r_l} P_l - q^{r_l} P_l p^{s_l}),$$

and it follows from this

$$d_1 + d_2 = \sum_{l=1}^k (p^{s_l} q^{r_l} P_l - P_l p^{s_l} q^{r_l}).$$

Here the second term of a term always rises against the first of the next, and also the first and last members of the whole sum destroy each other. So it is

$$d_1 + d_2 = 0. \quad (23)$$

On quantum mechanics.

865

Because of its linear nature, this relationship is considered to be $\mathbf{z}$ not only for expressions $\mathbf{z}$ form (19), but at the same time also for arbitrary analytic functions $\mathbf{g}(\mathbf{p}\mathbf{q})^{1)}$.

At the end of this brief presentation of matrix analysis, we want to prove the theorem: Every matrix equation

$$F(\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_r) = 0$$

remains correct if you use all argument matrices $\mathbf{x}_j$ one and the same permutation of all lines and columns. For this purpose, it is evidently sufficient to show that for two matrices $\mathbf{a}, \mathbf{b}$, which is caused by this operation in $\mathbf{a}', \mathbf{b}'$ the invariances

$$\mathbf{a}' + \mathbf{b}' = (\mathbf{a} + \mathbf{b})'. \quad \mathbf{a}'\mathbf{b}' = (\mathbf{a}\mathbf{b})'$$

where the right-hand sides signify those matrices which are $\mathbf{a} + \mathbf{b}$ and $\mathbf{a}\mathbf{b}$ through those exchanges.

We make this proof by replacing the operation of permuting with multiplication by a suitable matrix$^{2)}$.

We write a permutation

$$\begin{pmatrix} 0 & 1 & 2 & 3 & \dots \\ k_0 & k_1 & k_2 & k_3 & \dots \end{pmatrix} = \begin{pmatrix} n \\ k_n \end{pmatrix}.$$

We assign the permutation matrix to this

$$\mathbf{p} = (p(nm)), \quad p(nm) = \begin{cases} 1 & \text{für } m = k_n, \\ 0 & \text{sonst} \end{cases}$$

to. The $\mathbf{p}$ transposed matrix

$$\tilde{\mathbf{p}} = (\tilde{p}(nm)), \quad \tilde{p}(nm) = \begin{cases} 1 & \text{für } n = k_m, \\ 0 & \text{sonst.} \end{cases}$$

By multiplying both,

$$\mathbf{p}\tilde{\mathbf{p}} = \left( \sum_k p(nk)\tilde{p}(km) \right) = (\delta_{nm}) = 1,$$

as both factors $p(nk)$ and $\tilde{p}(km)$ only then at the same time from zero

$^{1)}$ More generally, functions of $r$ Variables

$$\sum_r \left( \mathbf{x}_r \frac{\partial \mathbf{g}}{\partial \mathbf{x}_r} - \frac{\partial \mathbf{g}}{\partial \mathbf{x}_r} \mathbf{x}_r \right) = 0.$$

$^{2)}$ This method of proof chosen here has the advantage that it shows the close connection of the permutations with an important class of general transformations of the matrices. However, the correctness of the theorem in question can also be inferred directly from the remark that in the definitions of equality and the addition and multiplication of matrices, no use is made of regulatory relationships between the rows or columns.

866

M. Born and P. Jordan,

are different if $k = k_n = k_m$, i.e. $n = m$ . Consequently, $\tilde{p}$ the reciprocal of $p$:

$$\tilde{p} = p^{-1}.$$

Let us now $a$ any matrix, then

$$pa = \left( \sum_k p(nk) a(km) \right) = (a(k_n, m))$$

a matrix consisting of $a$ by permutation $\binom{n}{k_n}$ of the lines. and likewise

$$ap^{-1} = \left( \sum_k a(nk) \tilde{p}(km) \right) = (a(n, k_m))$$

the matrix created by permuting the columns. One and the same permutation applied to rows and columns thus yields the matrix

$$a' = pap^{-1}.$$

From this it follows without further ado:

$$\begin{aligned} a' + b' &= p(a + b)p^{-1} = (a + b)', \\ a'b' &= pabp^{-1} = (ab)', \end{aligned}$$

which proves our assertion.

It is thus evident that any order or ranking of the elements can never be determined by matrix equations.

By the way, the much more general theorem that every matrix equation is invariant to transformations of the form apparently applies

$$a' = bab^{-1},$$

where $b$ any matrix. Of course, we will see later that this is no longer automatically true for matrix differential equations.

# Chapter II. Dynamics.

§ 3. The Basic Laws. The dynamical system is to be described by the coordinate $q$ and the impulse $p$. They are to be used as matrices

$$q = (q(nm)e^{2\pi i r(nm)t}), \quad p = (p(nm)e^{2\pi i r(nm)t}) \quad (24)$$

can be applied. In it, the $v(nm)$ the quantum theoretical frequencies, which correspond to the transitions between the states with the quantum numbers $n$ and $m$ belong. The matrices (24) are supposed to be Hermitian ones, i.e. when the matrices are transposed, each component is supposed to pass into its conjugate value, and that is to say, for all real $t$ apply. So we have

$$q(nm)q(mn) = |q(nm)|^2 \quad (25)$$

and

$$v(nm) = -v(mn). \quad (26)$$

On quantum mechanics.

867

Is $\boldsymbol{q}$ a Cartesian coordinate, the magnitude (25) is decisive for the probabilities$^{1)}$ of transitions $n \rightleftarrows m$.

We also want to demand that

$$v(jk) + v(kl) + v(lj) = 0 \quad (27)$$

. With (26) together this can be expressed as follows: There are sizes $W_n$, so that

$$h v(nm) = W_n - W_m \quad (28)$$

.

It follows, with (2), (3), that a function $\boldsymbol{g}(\boldsymbol{p}\boldsymbol{q})$ always the form

$$\boldsymbol{g} = (g(nm) e^{2\pi i v(nm)t}) \quad (29)$$

, namely the matrix $(g(nm))$ by the same process from the matrices $(q(nm))$, $(p(nm))$ through which the $\boldsymbol{g}$ Off $\boldsymbol{q}$, $\boldsymbol{p}$ was preserved. We can, therefore, instead of the presentation (24), which is now to be abandoned, use the shorter notation

$$\boldsymbol{q} = (q(nm)), \boldsymbol{p} = (p(nm)) \quad (30)$$

.

As a temporal derivative of the matrix $\boldsymbol{g} = (g(nm))$ by remembering (24) and (29) respectively, we get the matrix

$$\dot{\boldsymbol{g}} = 2\pi i (v(nm)g(nm)). \quad (31)$$

If, as we want to assume, $v(nm) \neq 0$ for $n \neq m$ , then means $\dot{\boldsymbol{g}} = 0$that $\boldsymbol{g}$ a diagonal matrix with $g(nm) = \delta_{nm}g(nn)$ .

A differential equation $\dot{\boldsymbol{g}} = \boldsymbol{a}$ is invariant to the process in which rows and columns of all matrices as well as the numbers $W_n$ be subjected to the same permutation. To see this, let's look at the diagonal matrix

$$\boldsymbol{W} = (\delta_{nm}W_n);$$

then

$$\boldsymbol{W}\boldsymbol{g} = (\sum_k \delta_{nk} W_n g(km)) = (W_n g(nm)),$$

$$\boldsymbol{g}\boldsymbol{W} = (\sum_k g(nk) \delta_{km} W_k) = (W_m g(nm)),$$

also after (31)

$$\dot{\boldsymbol{g}} = \frac{2\pi i}{h} ((W_n - W_m)g(nm)) = \frac{2\pi i}{h} (\boldsymbol{W}\boldsymbol{g} - \boldsymbol{g}\boldsymbol{W}).$$

Is now $p$ a permutation matrix, so is the transformed

$$\boldsymbol{W}' = \boldsymbol{p}\boldsymbol{W}\boldsymbol{p}^{-1} = (\delta_{n_k m} W_{n_k})$$

$^{1)}$ See § 8.

868

M. Born and P. Jordan,

the diagonal matrix with the permuted $W_n$ on the diagonal. One has therefore

$$p \dot{g} p^{-1} = \frac{2 \pi i}{h} (W' g' - g' W') = \dot{g}',$$

where $g' = p g p^{-1}$ and $\dot{g}'$ which, according to rule (31), are treated with permuted $W_n$ formed temporal derivation of $g'$ means.

The lines and columns of $\dot{g}$ suffer the same permutation as that of $g$, and from this follows our assertion.

It should be noted that a corresponding theorem for arbitrary transformation of the form $a' = b a b^{-1}$ does not apply; for in such cases $W'$ no longer diagonal matrix. In spite of this difficulty, a detailed study of these general transformations seems indispensable to us, because it promises insight into the deeper connections of the new theory; We will come back to this later$^{1)}$.

For the case of a Hamiltonian function of the figure

$$H = \frac{1}{2 m} p^2 + U(q)$$

we will assume, with Heisenberg, that the equations of motion are the same as the classical ones, so that we can write with the symbolism of § 2:

$$\left. \begin{aligned} \dot{q} &= \frac{\partial H}{\partial p} = \frac{1}{m} p, \\ \dot{p} &= -\frac{\partial H}{\partial q} = -\frac{\partial U}{\partial q}. \end{aligned} \right\} \quad (32)$$

It will be attempted to establish by means of a correspondenceal consideration also for the general case of any Hamiltonian function $H(p q)$ equations of motion. This is necessary in view of relativistic mechanics and especially of the treatment of the motion of electrons with the help of magnetic fields. In the latter case, the function $H$ in Cartesian coordinates can no longer be represented as the sum of two functions, one of which depends only on the momentum and the other only on the coordinates.

Classically, the equations of motion are derived from the principle of action

$$\int_{t_0}^{t_1} L dt = \int_{t_0}^{t_1} \{p \dot{q} - H(p q)\} dt = \text{Extremum.} \quad (33)$$

$^{1)}$ Cf. the forthcoming continuation of this work.

On quantum mechanics.

869

Let us imagine in this the Fourier development of $L$ and let's take the time period $t_1 - t_0$ sufficiently large, then only the constant term of $L$ contribute to the integral. The form that the principle of action thus acquires suggests the following transfer into quantum mechanics:

The diagonal sum $D(L) = \sum_k L(kk)$ should be made to the extreme:

$$D(L) = D(\boldsymbol{p}\dot{\boldsymbol{q}} - \boldsymbol{H}(\boldsymbol{p}\boldsymbol{q})) = \text{Extremum}, \quad (34)$$

by appropriate choice of $\boldsymbol{p}$ and $\boldsymbol{q}$ in the case of detained $\boldsymbol{v}(nm)$.

Thus, by taking the derivatives of $D(L)$ according to the elements of $\boldsymbol{p}$ and $\boldsymbol{q}$ equal to zero, the equations of motion

$$\begin{aligned} 2\pi i \boldsymbol{v}(nm) q(nm) &= \frac{\partial D(\boldsymbol{H})}{\partial p(mn)}, \\ 2\pi i \boldsymbol{v}(mn) p(mn) &= \frac{\partial D(\boldsymbol{H})}{\partial q(mn)}. \end{aligned}$$

From (26), (31) and (16) it is recognized that these equations of motion are generally expressed in the canonical form

$$\left. \begin{aligned} \dot{\boldsymbol{q}} &= \frac{\partial \boldsymbol{H}}{\partial \boldsymbol{p}}, \\ \dot{\boldsymbol{p}} &= -\frac{\partial \boldsymbol{H}}{\partial \boldsymbol{q}} \end{aligned} \right\} \quad (35)$$

can be written.

As a quantum condition, Heisenberg uses one developed by Thomas$^{1)}$ and Kuhn$^{2)}$ established relationship. The Equation

$$J = \oint p \, dq = \int_0^{1/r} p \, \dot{q} \, dt$$

of "classical" quantum theory, if one considers the Fourier evolution of $p$ and $q$

$$p = \sum_{\tau=-\infty}^{\infty} p_\tau e^{2\pi i \nu \tau t}, \quad q = \sum_{\tau=-\infty}^{\infty} q_\tau e^{2\pi i \nu \tau t},$$

are transformed into

$$1 = 2\pi i \sum_{\tau=-\infty}^{\infty} \tau \frac{\partial}{\partial J} (q_\tau p_{-\tau}). \quad (36)$$

$^{1)}$ W. Thomas, Naturw. **13**, 627, 1925.

$^{2)}$ W. Kuhn, ZS. f. Phys. **33**, 408, 1925.

870

M. Born and P. Jordan,

Is there $p = m\dot{q}$, the $p_\tau$ through the $q_\tau$ and one thus obtains the classical equation whose correspondenceal transformation into an equation of differences results in the relationship between Thomas and Kuhn. Since the prerequisite here $p = m\dot{q}$ is not to be done, we must translate equation (36) directly into an equation of differences.

It should correspond

$$\sum_{\tau=-\infty}^{\infty} \tau \frac{\partial}{\partial J} (q_\tau p_{-\tau}) \text{ mit } \frac{1}{h} \sum_{\tau=-\infty}^{\infty} (q(n+\tau, n) p(n, n+\tau) - q(n, n-\tau) p(n-\tau, n));$$

on the right are those $q(n m)$, $p(n, m)$, which receive a negative index, is equal to zero. This gives us the quantum condition as a correspondence transformation of (36)

$$\sum_k (p(n k) q(kn) - q(n k) p(kn)) = \frac{h}{2\pi i}. \quad (37)$$

That's an infinite number of equations, one for each $n$. For $p = m\dot{q}$ in particular, this results in

$$\sum_k \nu(kn) |q(n k)|^2 = \frac{h}{8\pi^2 m},$$

which, as is easy to determine, agrees with Heisenberg's form of the quantum condition or Thomas-Kuhn's equation. (37) must be regarded as the appropriate generalization of this equation.

By the way, it can be seen from (37) that the diagonal sum $D(pq)$ necessarily becomes infinite. Because otherwise (10) would follow $D(pq) - D(qp) = 0$, while (37) to $D(pq) - D(qp) = \infty$ . The matrices under consideration are therefore never finite$^{1)}$.

§ 4. Conclusions. Energy and frequency set. With the statements of the preceding paragraph, the basic laws of the new mechanics are completely given. All other laws of quantum mechanics, which are to be accorded universal validity, must be proven from them. The theorems to be proved as such are primarily the energy theorem and the Bohr frequency condition. The law of energy states that if $H$ the energy is, $\dot{H} = 0$ or that $H$ is a diagonal matrix. The diagonal

$^{1)}$ Nor do they belong to the class of "bounded" infinite matrices, which has so far been considered almost exclusively by mathematicians.

On quantum mechanics.

871

Links $H(n n)$ by $\pmb{H}$ are then interpreted according to Heisenberg as energies of the various states of the system, and Bohr's frequency condition requires

$$h \nu (n m) = H (n n) - H (m m),$$

or

$$W_n = H (n n) + \text{konst.}$$

We look at the size

$$d = p q - q p.$$

After (11), (35)

$$\begin{aligned} \dot{d} &= \dot{p} q + p \dot{q} - \dot{q} p - q \dot{p} \\ &= q \frac{\partial H}{\partial q} - \frac{\partial H}{\partial q} q + p \frac{\partial H}{\partial p} - \frac{\partial H}{\partial p} p. \end{aligned}$$

After (22), (23) is therefore $\dot{d} = 0$ and $d$ a diagonal matrix. The diagonal members of $d$ but are precisely determined by the quantum condition (37). In summary, using the unit matrix defined by (6), we get $\pmb{I}$ the equation

$$p q - q p = \frac{h}{2 \pi i} \pmb{I}, \quad (38)$$

which we call the "tightened quantum condition" and on which all further conclusions are based.

From the form of this equation it can be inferred: If (38) becomes an equation ($A$), ($A$) is correct, if you $p$ with $q$ and at the same time $h$ by $-h$ . Therefore, for example, from the equations

$$p^n q = q p^n + n \frac{h}{2 \pi i} p^{n-1}, \quad (39)$$

$$q^n p = p q^n - n \frac{h}{2 \pi i} q^{n-1} \quad (39')$$

only one of (38) can be proved, which can easily be carried out by induction.

We now want to prove the energy and frequency theorem, as they have been pronounced above, for the case

$$H = H_1(p) + H_2(q).$$

According to the explanations of § 1, the following may be used in this $H_1(p)$ and $H_2(q)$ formally by power sums

$$H_1 = \sum_s a_s p^s, \quad H_2 = \sum_s b_s q^s$$

872

M. Born and P. Jordan,

be replaced. The formulas (39), (39') then show that

$$\left. \begin{aligned} Hq - qH &= \frac{h}{2\pi i} \frac{\partial H}{\partial p}, \\ Hp - pH &= -\frac{h}{2\pi i} \frac{\partial H}{\partial q} \end{aligned} \right\} \quad (40)$$

and the comparison with the equations of motion (35) provides

$$\left. \begin{aligned} \dot{q} &= \frac{2\pi i}{h} (Hq - qH), \\ \dot{p} &= \frac{2\pi i}{h} (Hp - pH). \end{aligned} \right\} \quad (41)$$

If the matrix $Hg - gH$ briefly with $\left| \begin{matrix} H \\ g \end{matrix} \right|$ , the following shall apply:

$$\left| \begin{matrix} H \\ ab \end{matrix} \right| = \left| \begin{matrix} H \\ a \end{matrix} \right| b + a \left| \begin{matrix} H \\ b \end{matrix} \right|; \quad (42)$$

From this, however, it is generally necessary to $g = g(pq)$

$$\dot{g} = \frac{2\pi i}{h} \left| \begin{matrix} H \\ g \end{matrix} \right| = \frac{2\pi i}{h} (Hg - gH) \quad (43)$$

. For one only needs to prove it $\dot{g}$ by means of (11), (11') as a function of $p, q$ and $\dot{p}, \dot{q}$, and $\left| \begin{matrix} H \\ g \end{matrix} \right|$ by means of (42) as a function of $p, q$ and $\left| \begin{matrix} H \\ p \end{matrix} \right|, \left| \begin{matrix} H \\ q \end{matrix} \right|$ and then (41) applied. If one puts in (43) in particular $g = H$, one obtains

$$\dot{H} = 0. \quad (44)$$

After the law of energy has thus been proven and $H$ is recognized as a diagonal matrix, (41) is given the shape

$$\begin{aligned} hv(nm)q(nm) &= (H(nn) - H(mm))q(nm), \\ hv(nm)p(nm) &= (H(nn) - H(mm))p(nm), \end{aligned}$$

from which the frequency condition follows.

Now let's move on to more general Hamiltonian functions $H^* = H^*(pq)$ can be easily recognized by examples, such as $H^* = p^2q$that in general no longer $\dot{H}^* = 0$ . However, it can be seen that the Hamiltonian function $H = \frac{1}{2}(p^2q + qp^2)$ the same equations of motion as $H^*$ and that $\dot{H}$ becomes zero again. We then pronounce the energy and frequency theorem as follows: For each function $H^* = H^*(pq)$ there is a function $H = H(pq)$, so that $H^*$ and $H$ as Hamiltonian

On quantum mechanics.

873

functions yield the same equations of motion, and that $H$ takes on the role of the temporally constant energy fulfilling the frequency condition for these equations of motion.

In the light of the considerations set out above, it is sufficient to show that the function to be specified $H$ except

$$\frac{\partial H}{\partial p} = \frac{\partial H^*}{\partial p}, \quad \frac{\partial H}{\partial q} = \frac{\partial H^*}{\partial q} \quad (45)$$

nor equations (40). According to § 1, $H^*$ formally as the sum of potency products in $p$ and $q$ and because of the linearity of equations (40), (45) in $H$, $H^*$ we will simply calculate for each individual summand in $H^*$ the corresponding summand in $H$ . So we just need the case

$$H^* = \prod_{j=1}^k (p^{r_j} q^{r_j}) \quad (46)$$

. According to the remarks in § 2, equations (45) are to be fulfilled by $H$ as a linear form of those potency products in $p, q$ which consists of $H^*$ are caused by cyclical reversals of factors; only the sum of the coefficients must be kept equal to 1. The question of how to choose these coefficients so that equations (40) are also fulfilled is less easy to answer. It may suffice to describe the case here $k = 1$, i.e.

$$H^* = p^r q^r \quad (47)$$

.

The formula (39) can be generalized to ¹)

$$p^m q^n - q^n p^m = m \frac{h}{2\pi i} \sum_{l=0}^{n-1} q^{n-1-l} p^{m-l} q^l. \quad (48)$$

For $n = 1$ is that again (39); In general, it follows (48) that because of (39)

$$p^m q^{n+1} - q^{n+1} p^m = (p^m q^n - q^n p^m) q + m \frac{h}{2\pi i} q^n p^{m+1}$$

¹) Another generalization is given by the formulas

$$\begin{aligned} p^m q^n &= \sum_{j=0}^{m,n} j! \binom{m}{j} \binom{n}{j} \left(\frac{h}{2\pi i}\right)^j q^{n-j} p^{m-j}, \\ q^n p^m &= \sum_{j=0}^{m,n} j! \binom{m}{j} \binom{n}{j} \left(\frac{-h}{2\pi i}\right)^j p^{m-j} q^{n-j}, \end{aligned}$$

wherein $j$ up to the smaller of the numbers $m, n$ grows.

874

M. Born and P. Jordan.

. Swapping of $p$ and $q$ with sign change of $h$ results in the new formula

$$p^m q^n - q^n p^m = n \frac{h}{2\pi i} \sum_{j=0}^{m-1} p^{m-1-j} q^{n-1} p^j. \quad (48')$$

Comparison with (48) provides

$$\frac{1}{s+1} \sum_{l=0}^s p^{s-l} q^r p^l = \frac{1}{r+1} \sum_{j=0}^r q^{r-j} p^s q^j. \quad (49)$$

We now claim: $H^*$ after (47)

$$H = \frac{1}{s+1} \sum_{l=0}^s p^{s-l} q^r p^l. \quad (50)$$

We only have to prove (40), whereby we have to remember formula (18') from § 2.

Now, after (50)

$$Hp - pH = \frac{1}{s+1} (q^r p^{s+1} - p^{s+1} q^r),$$

and according to (48) this is equivalent to the lower equation (40).

Using (49) we further obtain

$$Hq - qH = \frac{1}{r+1} (p^s q^{r+1} - q^{r+1} p^s),$$

which, according to (48'), is equivalent to the upper equation (40). This means that the required proof has been provided in full.

While in classical mechanics the energy constancy $\dot{H} = 0$ can be read directly from the canonical equations, the law of energy $\dot{H} = 0$ of quantum mechanics, as you can see, much less on the surface.

How far its provability is from being trivial on the basis of the presuppositions made can be seen if one considers the constancy of $H$ simply by calculating $\dot{H}$ tries to prove. For this purpose, one has first of all (11), (11') $\dot{H}$ as a function of $p$, $q$ and $\dot{p}$, $\dot{q}$ what the $\dot{p}$, $\dot{q}$ the values $-\frac{\partial H}{\partial q}$, $\frac{\partial H}{\partial p}$ are to be introduced. This results in $\dot{H}$ as a function of $p$ and $q$. Equation (38) and the formulas derived from it, given in the footnote on page 873, allow this function to be converted into a sum of terms $a p^s q^r$ and it must be proved that the coefficient $a$ of each such limb disappears. This calculation is used for the most general above in a different way

On quantum mechanics.

875

case so exceedingly complicated¹) that it hardly seems practicable. If, in spite of this, the law of energy and frequency could be proved to such a general extent, it seems to us to give us a strong support for the hope that this theory really grasps deep physical laws.

Finally, here is a result that can be easily taken from the formulas of this paragraph: The equations (35), (37) can be replaced by (38) and (44) (where H means the energy); the frequencies are to be determined from the frequency condition.

We will discuss the important applications that this theorem allows in the continuation of this work.

# Chapter III. Investigation of the Anharmonic Oscillator.

The anharmonic oscillator with

$$H = \frac{1}{2} p^2 + \frac{\omega_0^2}{2} q^2 + \frac{1}{3} \lambda q^3 \quad (51)$$

has already been considered in detail by Heisenberg. Nevertheless, a new study will be devoted to it here, with the aim of establishing the most general solution of the basic equations for this case. When the basic equations of the theory are really complete and no longer need to be supplemented, the absolute values $|q(nm)|$, $|p(nm)|$ of the components of $q$ and $p$ clearly defined by them, and it will be important to test this using the example (51). On the other hand, it is to be expected that with regard to the phases $\varphi_{nm}$, $\psi_{nm}$ in

$$q(nm) = |q(nm)| e^{i\varphi_{nm}},$$

$$p(nm) = |p(nm)| e^{i\psi_{nm}}$$

still an indeterminacy remains. For the statistics, e.g. of the interaction of quantum atoms with external radiation fields, it will be of fundamental importance to precisely determine the degree of this indeterminacy.

§ 5. Harmonic Oscillator. The starting point of our considerations is the theory of the harmonic oscillator; for little ones $\lambda$

¹) In case $H = \frac{1}{2m} p^2 + U(q)$ it can be performed immediately with the help of (39').

Journal of Physics, Vol. XXXIV.

58

876

M. Born and P. Jordan,

according to equation (51), the motion can be described as a disturbance of the harmonic oscillation with the energy

$$H = \frac{1}{2} p^2 + \frac{\omega_0^2}{2} q^2 \quad (52)$$

.

Even with this simple problem, an addition to Heisenberg's considerations is necessary. The latter derives an essential statement about the form of the solution from a correspondence consideration; since classically there is only one harmonic component, Heisenberg sets up a matrix that only represents transitions between neighboring states, i.e. has the form

$$q = \begin{pmatrix} 0 & q^{(01)} & 0 & 0 & 0 & \dots \\ q^{(10)} & 0 & q^{(12)} & 0 & 0 & \dots \\ 0 & q^{(21)} & 0 & q^{(23)} & 0 & \dots \\ \dots & \dots & \dots & \dots & \dots & \dots \end{pmatrix}. \quad (53)$$

Our endeavour is to build up the whole theory independently, without drawing help from classical theory on the basis of the principle of correspondence. Therefore, we will investigate whether the form (53) of the matrix can not be derived from the basic equations themselves, or, if this is not possible, what additional demands are to be made.

It can be seen without further ado from what has been said in § 3 about the invariance against permutations of rows and columns, that the exact form of the matrix (53) can never be deduced from the basic equations; for if you swap rows and columns in the same way, the canonical equations and the quantum condition remain invariant, so you have found a new, apparently different solution. But all these solutions are of course different only in the way they are written, i.e. in the numbering of the elements. We want to prove that by a mere renumbering of the elements the solution can always be reduced to the form (53). The equation of motion

$$\ddot{q} + \omega_0^2 q = 0 \quad (54)$$

is for the elements:

$$(v^2 (nm) - v_0^2) q (nm) = 0, \quad (55)$$

where

$$\omega^0 = 2\pi v_0, \quad h\nu (nm) = W_n - W_m.$$

From the tightened quantum condition

$$pq - qp = \frac{h}{2\pi i} I \quad (56)$$

On quantum mechanics.

877

follows that to every $n$ a $n'$ must exist, so that $q(nn') \neq 0$ is; because if there were a $n$, for which all $q(nn') = 0$ it would be $n$ Diagonal term of $pq - qp$ zero, which contradicts the quantum condition. According to this, it follows (55) that there is always a $n'$ exists, for which

$$|W_n - W_{n'}| = h\nu_0$$

. However, since we have assumed in our basic principles that for $n \neq m$ always $W_n \neq W_m$ , a maximum of two such indices, $n'$ and $n''$, exist; because the associated $W_{n'}$, $W_{n''}$ are solutions of the quadratic equation

$$(W_n - x)^2 = h^2\nu_0^2;$$

if really two such indices $n'$, $n''$ exists, follows for the corresponding frequencies

$$\nu(nn') = -\nu(nn''). \quad (57)$$

Now (56)

$$\sum_k \nu(kn)|q(nk)|^2 = \nu(n'n)\{|q(nn')|^2 - |q(nn'')|^2\} = \frac{h}{8\pi^2}, \quad (58)$$

and the energy (52) becomes:

$$\begin{aligned} H(nm) &= \frac{1}{2}4\pi^2 \sum_k \{-\nu(nk)\nu(km)q(nk)q(km) + \nu_0^2 q(nk)q(km)\} \\ &= 2\pi^2 \sum_k q(nk)q(km)\{\nu_0^2 - \nu(nk)\nu(km)\}. \end{aligned}$$

In particular, the following applies to $m = n$:

$$H(nn) = W_n = 4\pi^2 \nu_0^2 (|q(nn')|^2 + |q(nn'')|^2). \quad (59)$$

Three cases are now still possible:

- a) There is no $n''$ and it is $W_{n'} > W_n$;
- b) there is no $n''$ and it is $W_{n'} < W_n$;
- c) there are $n''$.

In case b), instead of $n$ Now $n'$; this includes a maximum of two indices $(n')'$ and $(n')'$, and one of these must be $n$ . This brings us back to one of the cases a) or c) and can therefore omit b).

In case (a), $\nu(n'n) = +\nu_0$, and from (58) it follows:

$$\nu_0 \cdot |q(nn')|^2 = \frac{h}{8\pi^2}, \quad (60)$$

so according to (59):

$$W_n = H(nn) = 4\pi^2 \nu_0^2 |q(nn')|^2 = \frac{1}{2}\nu_0 h.$$

Because of the prerequisite $W_n \neq W_m$ for $n \neq m$ so there is at most one index $n = n_0$, for which case (a) applies.

58*

878

M. Born and P. Jordan,

If such a $n_0$ exists, we can get a series of numbers

$$n_0, n_1, n_2, n_3 \dots$$

in such a way that

$$(n_k)' = n_{k+1} \quad \text{und} \quad W_{k+1} > W_k$$

Then every time

$$(n_{k+1})'' = n_k$$

So for $k > 0$ from (58) and (59):

$$H(n_k, n_k) = 4\pi^2 v_0^2 \{|q(n_k, n_{k+1})|^2 + |q(n_k, n_{k-1})|^2\}, \quad (61)$$

$$\frac{1}{2}h = 4\pi^2 v_0 \{|q(n_k, n_{k+1})|^2 - |q(n_k, n_{k-1})|^2\}. \quad (62)$$

From (60) and (62) it follows

$$|q(n_k, n_{k+1})|^2 = \frac{h}{8\pi^2 v_0} (k+1), \quad (63)$$

and then off (61)

$$W_{n_k} = H(n_k, n_k) = v_0 h(k + \frac{1}{2}). \quad (64)$$

Now let us see whether it is possible that there is no $n$ to which case a) applies. We can then, with arbitrary $n_0$ Beginning, $n_0' = n_1$ and $n_0'' = n_{-1}$ form; to each of these again $n_1' = n_2$, $n_1'' = n_0$ and $n_{-1}' = n_0$, $n_{-1}'' = n_{-2}$ etc. In this way, we get a series of numbers

$$\dots n_{-2}, n_{-1}, n_0, n_1, n_2 \dots \quad (65)$$

and equations (61), (62) apply to each $k$ between $-\infty$ and $+\infty$. But that is impossible; for according to (62) the magnitudes $x_k = |q(n_{k+1}, n_k)|^2$ an equidistant series of numbers, and since they are positive, there must be a smallest. We can use the corresponding index again with $n_0$ and thus return to the previous case; therefore the formulas (63), (64) also apply here.

You can also see that every number $n$ must be among the numbers $n_k$ be included; because otherwise you could use $n$ form a new series (65) as starting terms, whereby the formula (60) again applies. The initial members of both series would therefore have the same values $W_n = H(nn)$, which is impossible.

This proves that the indices 0, 1, 2, 3 ... so in a new order $n_0, n_1, n_2, n_3 \dots$ can be rearranged so that the formulas (63), (64) apply; in these new indices, the solution then has Heisenberg's form (53). This thus appears as the "normal form" of the general solution. According to (64) it has the property that:

$$W_{n_{k+1}} > W_{n_k}$$

Conversely, if it is demanded that $W_n = H(nn)$ with $n$ is to grow constantly, it becomes necessary $n_k = k$; this principle therefore lays down the normal form

On quantum mechanics.

879

clearly established. But this only fixes the spelling and makes the invoice clearer; physically, nothing new is given by it.

This is a profound difference from the semi-classical determination of stationary states that has been used up to now. The classically calculated orbits are continuously connected to each other, which means that a certain sequence is also placed in the quantum orbits that are subsequently separated from the outset. The new mechanics presents itself as a true theory of the discontinuum, in that there is no question here of such a sequence of quantum states defined by the physical process, but the quantum numbers are really nothing but discriminating indices which can be interpreted according to some practical point of view (e.g., according to increasing energy $W_n$) can order and standardize.

§ 6. Anharmonic Oscillator. The equations of motion

$$\ddot{\boldsymbol{q}} + \omega_0^2 \boldsymbol{q} + \lambda \boldsymbol{q}^2 = 0 \quad (66)$$

together with the quantum condition, give the following system of equations for the elements:

$$\left. \begin{aligned} (\omega_0^2 - \omega^2(n m)) q(n m) + \lambda \sum_k q(n k) q(k m) &= 0, \\ \sum_k \omega(n k) q(n k) q(k n) &= -\frac{h}{4\pi}. \end{aligned} \right\} \quad (67)$$

We are looking for it through series developments

$$\left. \begin{aligned} \omega(n m) &= \omega^0(n m) + \lambda \omega^{(1)}(n m) + \lambda^2 \omega^{(2)}(n m) + \dots \\ q(n m) &= q^0(n m) + \lambda q^{(1)}(n m) + \lambda^2 q^{(2)}(n m) + \dots \end{aligned} \right\} \quad (68)$$

.

For $\lambda = 0$ we have the case of the harmonic oscillator dealt with in the previous paragraph; we write the solution (53) in the form

$$q^0(n m) = a_n \delta_{n, m-1} + \bar{a}_m \delta_{n-1, m}, \quad (69)$$

where the overstroke is supposed to denote the conjugate-complex size. If you form the square and higher powers of the matrix $\boldsymbol{q}^0 = (q^0(n m))$, matrices of similar shape occur, namely sums of terms

$$(\xi)_{n m}^{(p)} = \xi_n \delta_{n, m-p} + \bar{\xi}_m \delta_{n-p, m}. \quad (70)$$

Therefore, it makes sense to find the solution in the form

$$\left. \begin{aligned} q^0(n m) &= (a)_{n m}^{(1)}, \\ q^{(1)}(n m) &= (x)_{n m}^0 + (x')_{n m}^{(2)}, \\ q^{(2)}(n m) &= (y)_{n m}^{(1)} + (y')_{n m}^{(3)}, \\ \dots & \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \end{aligned} \right\} \quad (71)$$

880

M. Born and P. Jordan,

whereby always odd and even values of the index $p$ .

In fact, you put that in the approximation equations

$$\lambda : \left\{ \begin{array}{l} \left( \omega_0^2 - \omega^0(nm)^2 \right) q^{(1)}(nm) - 2\omega^0(nm)\omega^{(1)}(nm)q^0(nm) \\ \quad + \sum_k q_0(nk)q^0(km) = 0, \\ \sum_k \left\{ \omega^0(nk) \left( q^0(nk)q^{(1)}(kn) + q^{(1)}(nk)q^0(kn) \right) \right. \\ \quad \left. \left. + \omega^{(1)}(nk)q^0(nk)q^0(kn) \right\} = 0, \end{array} \right. \right\} \quad (72)$$

$$\lambda^2 : \left\{ \begin{array}{l} \left( \omega_0^2 - \omega^0(nm)^2 \right) q^{(2)}(nm) - 2\omega^0(nm)\omega^{(1)}(nm)q^{(1)}(nm) \\ \quad - \left( \omega^{(1)}(nm)^2 + 2\omega^0(nm)\omega^{(2)}(nm) \right) q^0(nm) \\ \quad + \sum_k \left( q^0(nk)q^{(1)}(km) + q^{(1)}(nk)q^0(km) \right) = 0, \\ \sum_k \left\{ \omega^0(nk) \left( q^0(nk)q^{(2)}(km) + q^{(1)}(nk)q^{(1)}(km) \right. \right. \\ \quad \left. \left. + q^{(2)}(nk)q^0(km) \right) + \omega^{(1)}(nk) \left( q^0(nk)q^{(1)}(km) \right. \right. \\ \quad \left. \left. + q^{(1)}(nk)q^0(km) \right) + \omega^{(2)}(nk)q^0(nk)q^0(km) \right\} = 0 \end{array} \right\} \quad (73)$$

and observes the multiplication rule

$$\left. \begin{array}{l} \sum_k \Omega_{nkm}(\xi)_{nk}^{(p)}(\eta)_{km}^{(q)} = \Omega_{n,n+p,n+p+q} \xi_n \eta_{m+p} \delta_{n,m-p-q} \\ \quad + \Omega_{n,n+p,n+p-q} \xi_n \bar{\eta}_{n+p-q} \delta_{n,m-p+q} \\ \quad + \Omega_{n,n-p,n-p+q} \bar{\xi}_{n-p} \eta_{n-p} \delta_{n,m+p-q} \\ \quad + \Omega_{n,n-p,n-p-q} \bar{\xi}_{n-p} \eta_{n-p-q} \delta_{n,m+p+q} \end{array} \right\} \quad (74)$$

one sees, by taking into account the factors of $\delta_{n,m-s}$ that all conditions can be fulfilled by the beginning (71) and that higher terms would disappear identically in (71).

In detail, the invoice gives the following:

The first of the equations (72) yields after inserting the expressions (71):

$$\left. \begin{array}{l} 2\omega_0^2 x_n + |a_n|^2 + |a_{n-1}|^2 = 0, \\ - 3\omega_0^2 x_{n'} + a_n a_{n+1} = 0, \\ \omega_{n,n-1}^{(1)} = 0, \end{array} \right\} \quad (75)$$

the second is fulfilled identically. So you have:

$$\left. \begin{array}{l} x_n = - \frac{|a_n|^2 + |a_{n-1}|^2}{2\omega_0^2}, \\ x_n' = \frac{a_n a_{n+1}}{3\omega_0^2}. \end{array} \right\} \quad (76)$$

On quantum mechanics.

881

The first of the equations (73) provides:

$$\left. \begin{aligned} 2 \omega_0 a_n \omega_{n,n+1}^{(2)} + 2 a_n x_{n+1} + 2 a_n x_n + \bar{a}_{n-1} x'_{n-1} + a_{n+1} x'_n &= 0, \\ - 8 \omega_0^2 y'_n + a_n x'_{n+1} + a_{n+2} x'_n &= 0, \\ \omega_{n,n-2}^{(1)} &= 0, \end{aligned} \right\} (77)$$

the second equation is not fulfilled identically, but provides a determination equation for $y_n$:

$$\left. \begin{aligned} a_n \bar{y}_n + \bar{a}_n y_n - a_{n-1} \bar{y}_{n-1} - \bar{a}_{n-1} y_{n-1} + 2 |x'|^2 - 2 |x'_{n-2}|^2 \\ - \frac{\omega_{n,n+1}^{(2)}}{\omega_0} |a_n|^2 - \frac{\omega_{n,n-1}^{(2)}}{\omega_0} |a_{n-1}|^2 &= 0. \end{aligned} \right\} (78)$$

The solution is:

$$\left. \begin{aligned} \omega_{n,n+1}^{(2)} &= \frac{1}{3 \omega_0^3} (|a_{n+1}|^2 + |a_{n-1}|^2 + 3 |a_n|^2), \\ y'_n &= \frac{1}{12 \omega_0^4} a_n a_{n+1} a_{n+2}. \end{aligned} \right\} (79)$$

If one also sets the abbreviation

$$\eta_n = a_n \bar{y}_n + \bar{a}_n y_n, \quad (80)$$

this is how $\eta$ from the equation

$$\left. \begin{aligned} \eta_n - \eta_{n-1} &= \frac{1}{\omega_0^4} (|a_n|^4 - |a_{n-1}|^4 + \frac{1}{9} |a_n|^2 |a_{n+1}|^2 \\ - \frac{1}{9} |a_{n-1}|^2 |a_{n-2}|^2). \end{aligned} \right\} (81)$$

The expressions (76) and (79) show that the quantities $x_n, x'_n, y'_n$ by solving the zeroth approximation $a_n$ express. Their phases are therefore determined by those of the harmonic oscillator. It seems different with the size $y_n$ ; because although $\eta_n$ from (81), but then it is possible to $y_n$ from (80). It is probable that in the following approximation a supplementary equation of determination for $y_n$ is created; we must leave this question open here, but we would like to point out its fundamental significance for the coherence of the whole theory. For all statistical questions it depends on whether our assumption is correct that the phases of the $q(nm)$ one in each row (or column) of the matrix remains indeterminate.

In conclusion, we will give the explicit formulas which are obtained when we consider the solution of the harmonic

882

M. Born and P. Jordan,

oscillator. In the normal form, this reads according to (63):

$$a_n = \sqrt{C(n+1)} e^{i\varphi_n}, \quad C = \frac{h}{4\pi\omega_0} = \frac{h}{8\pi^2 v_0}. \quad (82)$$

Thus, according to (76), (79), (81):

$$\left. \begin{aligned} x_n &= -\frac{C}{2\omega_0^3}(2n+1), \\ x_n' &= \frac{C}{3\omega_0^3}\sqrt{(n+1)(n+2)}e^{i(\varphi_n + \varphi_{n+1})}, \\ y_n &= \frac{\sqrt{C^3}}{12\omega_0^4}\sqrt{(n+1)(n+2)(n+3)}e^{i(\varphi_n + \varphi_{n+1} + \varphi_{n+2})}; \\ &\omega_{n,n-1}^{(1)} = 0, \quad \omega_{n,n-2}^{(1)} = 0, \\ &\omega_{n,n-1}^{(2)} = -\frac{5}{3}\frac{C}{\omega_0^3}n; \end{aligned} \right\} \quad (83) \quad (84)$$

so

$$\eta_n - \eta_{n-1} = \frac{11}{9}\frac{C^2}{\omega_0^4}(2n+1),$$

$$\eta_n = a_n\bar{y}_n + \bar{a}_n y_n = \frac{11}{9}\frac{C^2}{\omega_0^4}(n+1)^2.$$

If you put $y_n = |y_n|e^{i\psi_n}$, it will be

$$|y_n|\cos(\varphi_n - \psi_n) = \frac{\eta_n}{2|a_n|} = \frac{11}{18}\frac{\sqrt{C^3}}{\omega_0^4}\sqrt{n+1}^3. \quad (85)$$

More can be said in this approximation about $y_n$ testify.

But we want to use the concluding formulas under the assumption that $\psi_n = \varphi_n$ tender. Then they are (except for terms of higher than second order in $\lambda$):

$$\left. \begin{aligned} \omega(n,n-1) &= \omega_0 - \lambda^2\frac{5}{3}\frac{C}{\omega_0^3}n + \dots, \\ \omega(n,n-2) &= 2\omega_0 + \dots; \end{aligned} \right\} \quad (86)$$

$$\left. \begin{aligned} q(n,n) &= -\lambda\frac{C}{\omega_0^3}(2n+1) + \dots, \\ q(n,n-1) &= \sqrt{Cn}e^{i\varphi_{n-1}}\left(1 + \lambda^2\frac{11}{18}\frac{Cn}{\omega_0^4} + \dots\right), \\ q(n,n-2) &= \lambda\frac{C}{3\omega_0^3}\sqrt{n(n-1)}e^{i(\varphi_{n-1} + \varphi_{n-2})} + \dots, \\ q(n,n-3) &= \lambda^2\frac{\sqrt{C^3}}{12\omega_0^4}\sqrt{n(n-1)(n-2)}e^{i(\varphi_{n-1} + \varphi_{n-2} + \varphi_{n-3})} + \dots \end{aligned} \right\} \quad (87)$$

On quantum mechanics.

883

We have also calculated and found the energy directly:

$$W_n = h\nu_0\left(n + \frac{1}{2}\right) - \lambda^2 \frac{5}{3} \frac{C^2}{\omega_0^2} \left(n(n+1) + \frac{17}{30}\right) + \cdots \quad (88)$$

The frequency condition is indeed fulfilled, because with regard to (82):

$$W_n - W_{n-1} = h\nu_0 - \lambda^2 \frac{2 C^2}{\omega_0^2} n + \cdots = \frac{h}{2\pi} \omega(n, n-1),$$

$$W_n - W_{n-2} = 2h\nu_0 + \cdots = \frac{h}{2\pi} \omega(n, n-2).$$

To the formula (88) one can connect with Heisenberg the remark that even in the terms of the lowest order there is a deviation from the classical theory, which can be achieved by introducing a "half-numbered" quantum number $n' = n + \frac{1}{2}$ formally. By the way, our expressions are correct $\omega(n, n-1)$ according to (86) and the classical frequencies coincide exactly. Because classical energy is ¹):

$$W_n^{(kl)} = h\nu_0 n - \lambda^2 \cdot \frac{5}{3} \frac{C^2}{\omega_0^2} n^2 + \cdots,$$

i.e. the classical frequency:

$$\begin{aligned} \omega_{kl} &= \frac{1}{h} \frac{\partial W_n^{(kl)}}{\partial n} = h\nu_0 - \lambda^2 \frac{5}{3} \frac{C^2}{\omega_0^2} n + \cdots \\ &= \omega_{qu}(n, n-1) = \frac{1}{h} \left( W_n^{(qu)} - W_{n-1}^{(qu)} \right). \end{aligned}$$

Finally, we have tested that the expression (88) can also be obtained from the Kramers-Born perturbation formula (except for the additive constant).

#### Chapter IV. Remarks on Electrodynamics.

According to Heisenberg, the squares of the absolute values $|q(nm)|^2$ of the elements of $\boldsymbol{q}$ in the event that $\boldsymbol{q}$ Cartesian coordinate is decisive for the jump probabilities. In conclusion, we would like to explain in what way this assumption can be justified on the basis of more general considerations. It is necessary to address the question of how the basic equations of electrodynamics are to be reinterpreted in the sense of the new theory. However, we would like to emphasize that the considerations presented here are only provisional; they are intended to show our fundamental position on the task. A detailed discussion of the

¹) S. M. Born, Atommechanik (Berlin 1925), Chapter 4, § 42, p. 294; in formula (6) is $a = 1/3$ in order to be in line with our approach.

884

M. Born and P. Jordan,

questions that arise will be given later, whereby above all the relationship of the theory presented to the theory of light quanta will be discussed.

We only want to bring up those points here that can be obtained without going into the exact form of the quantum condition for systems of several degrees of freedom. That one has already come quite far in electrodynamics can be seen by the following consideration. The electromagnetically oscillating cavity represents a system of infinite degrees of freedom. Nevertheless, the principles developed in the preceding chapters, which refer only to systems of one degree of freedom, are sufficient for its treatment, because, analyzed according to natural oscillations, it passes into a system of uncoupled oscillators. There can hardly be any doubt as to how this system should be treated. In this context, the fact that the basic electromagnetic equations are linear (superposition principle) proves to be of particular importance; for it follows that the substitute oscillators are harmonic, and it is precisely in the case of the harmonic oscillator — in contrast to the behavior of other systems — that the validity of the law of energy consists independently of the quantum condition:

$$H = \frac{1}{2}(p^2 + \omega_0^2 q^2)$$

follows

$$\begin{aligned} \dot{H} &= \frac{1}{2}(\dot{p}p + p\dot{p} + \omega_0^2 \dot{q}q + \omega_0^2 q\dot{q}) \\ &= \frac{1}{2}\omega_0^2(-qp - pq + pq + qp) \\ &= 0. \end{aligned}$$

It will therefore be expected that the integral theorems of the electrodynamics of the vacuum (energy and momentum theorem) can be obtained in a corresponding way in general from Maxwell's equations, which have been reinterpreted in terms of matrixes, without going into the quantum condition. By showing this, we at the same time gain the means of resolving Heisenberg's assertion of the importance of the $|q(nm)|^2$ .

§ 7. Maxwell's Equations, Energy and Momentum Theorem. We want to agree that vectors; are always designated by German letters, as usual, while the distinction between numbers and matrices is maintained by weak and bold type. We choose the units of measurement according to the textbook of Abraham.

The electromagnetic processes in the vacuum can be represented as the superposition of plane waves. In such a flat wave

¹) M. Abraham, Theorie der Elektrizität, II. Leipzig 1914.

On quantum mechanics.

885

we will measure the electric and magnetic field strengths $\mathfrak{E}$, $\mathfrak{H}$ as matrices whose elements are harmonically oscillating plane waves, e.g. if the coordinate system is in a suitable position

$$\mathfrak{E} = \left( \mathfrak{E}(nm) e^{2\pi i r (nm) \left( t - \frac{x}{c} \right)} \right). \quad (89)$$

Of course, it must be expected that $n, m$ In general, they are no longer limited to a discrete set of values and no longer denote individual numbers, but number systems (vectors).

Maxwell's equations will be retained as matrix equations:

$$\text{rot } \mathfrak{H} - \frac{1}{c} \dot{\mathfrak{E}} = 0, \quad \text{rot } \mathfrak{E} + \frac{1}{c} \dot{\mathfrak{H}} = 0. \quad (90)$$

The differentiations according to $x, y, z, t$ are to be thought of in each individual element of the matrix$^{1)}$.

We now want to derive the energy impulse law; for this it is necessary to preface some remarks on the multiplication of matrix vectors.

We define the scalar product by

$$(\mathfrak{A}, \mathfrak{B}) = \mathfrak{A}\mathfrak{B} = \mathfrak{A}_x \mathfrak{B}_x + \mathfrak{A}_y \mathfrak{B}_y + \mathfrak{A}_z \mathfrak{B}_z, \quad (91)$$

the vector product by

$$[\mathfrak{A}\mathfrak{B}]_x = \mathfrak{A}_y \mathfrak{B}_z - \mathfrak{A}_z \mathfrak{B}_y. \quad (92)$$

Since matrix multiplication is not commutative, the relationships

$$\mathfrak{A}\mathfrak{B} = \mathfrak{B}\mathfrak{A}, \quad [\mathfrak{A}\mathfrak{B}] = -[\mathfrak{B}\mathfrak{A}]$$

In general, no.

On the other hand, we claim:

$$\text{div } [\mathfrak{A}\mathfrak{B}] = (\text{rot } \mathfrak{A}, \mathfrak{B}) - (\mathfrak{A}, \text{rot } \mathfrak{B}). \quad (93)$$

We now define the energy $\mathcal{W}$ (as a scalar matrix) by

$$\mathcal{W} = \frac{1}{8\pi} (\mathfrak{E}^2 + \mathfrak{H}^2). \quad (94)$$

Then after (11)

$$8\pi \dot{\mathcal{W}} = \mathfrak{E}\dot{\mathfrak{E}} + \dot{\mathfrak{E}}\mathfrak{E} + \mathfrak{H}\dot{\mathfrak{H}} + \dot{\mathfrak{H}}\mathfrak{H},$$

and after (90):

$$\frac{8\pi}{c} \mathcal{W} = (\mathfrak{E}, \text{rot } \mathfrak{H}) + (\text{rot } \mathfrak{H}, \mathfrak{E}) - (\mathfrak{H}, \text{rot } \mathfrak{E}) - (\text{rot } \mathfrak{E}, \mathfrak{H}),$$

$^{1)}$ Under certain circumstances, a different conception of the electromagnetic field is necessary, in which the spatial coordinates do not appear as numbers, but themselves as matrices; this results in a corresponding change in the meaning of the spatial differential quotients in Maxwell's equations. We will return to this in the continuation of the work.

886

M. Born and P. Jordan,

also after (93) $\dot{\mathbf{W}} + \text{div } \mathbf{S} = 0,$ (95)

where $\mathbf{S} = \frac{c}{8\pi} ([\mathbf{E}\mathbf{H}] - [\mathbf{H}\mathbf{E}]).$ (96)

This is Poynting's theorem for matrix electrodynamics; $\mathbf{S}$ means the ray vector.

The momentum theorem can be derived in a similar way: Maxwell's stresses are defined by:

$$\left. \begin{aligned} T_{xx} &= \frac{1}{8\pi} (\mathbf{E}_x^2 - \mathbf{E}_y^2 - \mathbf{E}_z^2) + (\mathbf{H}_x^2 - \mathbf{H}_y^2 - \mathbf{H}_z^2), \\ T_{yz} &= \frac{1}{8\pi} (\mathbf{E}_y\mathbf{E}_z + \mathbf{E}_z\mathbf{E}_y + \mathbf{H}_y\mathbf{H}_z + \mathbf{H}_z\mathbf{H}_y) \end{aligned} \right\} \quad (97)$$

and the pulse density of the radiation by

$$\mathbf{g} = \frac{1}{c^2} \mathbf{S} = \frac{1}{8\pi c} ([\mathbf{E}\mathbf{H}] - [\mathbf{H}\mathbf{E}]). \quad (98)$$

Then you get by similar calculation:

$$\dot{\mathbf{g}}_x = \frac{\partial T_{xx}}{\partial x} + \frac{\partial T_{xy}}{\partial y} + \frac{\partial T_{xz}}{\partial z}. \quad (99)$$

Of course, these relationships gain clarity when one uses the four-dimensional mode of representation of the theory of relativity. A systematic treatment of four-dimensional vector analysis and the theory of relativity on the basis of matrix theory with its non-communicative multiplication will be given elsewhere.

§ 8. Ball Shafts. Radiation of a dipole. As we pursue our goal of calculating the radiation of an oscillator, we now have to consider spherical waves.

To do this, we will use the Hertzian vector $\mathbf{3}$ as a matrix vector; Off $\mathbf{3}$ you win $\mathbf{E}$ and $\mathbf{H}$ by virtue of the equations:

$$\mathbf{E} = \text{grad div } \mathbf{3} - \frac{1}{c^2} \dot{\mathbf{3}}, \quad \mathbf{H} = \frac{1}{c} \text{ rot } \dot{\mathbf{3}}. \quad (100)$$

In classical theory, for a spherical shaft $\mathbf{3}$ proportionally with

$$\frac{1}{r} e^{2\pi i r \left(t - \frac{r}{c}\right)}.$$

Now, as is well known, this expression can be written as the superposition of plane waves$^{1)}$, on the basis of identity

$$\frac{e^{i\pi r}}{r} = \frac{i\pi}{2\pi} \int e^{i\pi (r s)} d\omega; \quad (101)$$

$^{1)}$ See, for example, P. Debye, Ann. d. Phys. 30, 755, 1909; Formula (7''), p. 758.

On quantum mechanics.

887

where $r$ the number vector from the center of the spherical wave to the point, $\mathfrak{s}$ a unit vector, $d\omega = d\mathfrak{s}_x d\mathfrak{s}_y d\mathfrak{s}_z$. Consequently, even in our theory, the representation of a spherical wave can be obtained from plane waves, represented by matrices of the form (89), by means of integration via the direction of the wave normals:

$$\mathfrak{J} = \left( e \mathfrak{q} (n m) \frac{e^{2\pi i r (n m) \left( t - \frac{r}{c} \right)}}{r} \right); \quad (102)$$

where the matrix $e \mathfrak{q} = (e \mathfrak{q} (n m))$ represents the electrical moment that excites the wave.

The calculations which lead from here to the determination of the electronagnetic field and the radiation are the same as in classical theory, since $r$ as a number vector is interchangeable with any matrix. You get

$$\left. \begin{array}{l} \mathfrak{H} = - \frac{e}{c^2} \frac{1}{r^2} [r \ddot{\mathfrak{q}}], \\ \mathfrak{E} = \frac{e}{c^2} \frac{1}{r^2} [r [r \ddot{\mathfrak{q}}]] \end{array} \right\} \quad (103)$$

and from this

$$\mathfrak{S} = \frac{e}{4\pi c^2} \frac{r}{r} [r \ddot{\mathfrak{q}}]. \quad (104)$$

The integration across all spatial directions takes place in the same way as in classical theory. The result for the energy emitted per second is:

$$\int \mathfrak{S} d\mathfrak{f} = \frac{2e^2}{3c^3} \ddot{\mathfrak{q}}^2. \quad (105)$$

In order to obtain the average radiation, this expression must be averaged over time; this creates the diagonal matrix:

$$\frac{2e^2}{3c^3} \ddot{\mathfrak{q}}^2. \quad (106)$$

If the oscillator oscillates in a fixed direction, we can use the matrix vector $\mathfrak{q}$ by the matrix scalar $\mathfrak{q} = (q (n m))$ replace; then the broadcast

$$\frac{2e^2}{3c^3} \ddot{\mathfrak{q}}^2 = \frac{32\pi^4 e^2}{3c^3} \left( \sum_k v (n k)^4 |q (n k)|^2 \right). \quad (107)$$

We cannot yet give here a complete theory of radiation, from which one could necessarily conclude that the individual members of this series belong to the stationary states; for this would require a precise investigation of the reaction of radiation on the oscillator, i.e. a theory of attenuation. We will come back to this later. Here we just want to check whether the charisma is really due to the sizes $|q (n k)|^2$ is determined; Expression (107)

888

M. Born and P. Jordan, On Quantum Mechanics.

shows that this is the case, but at the same time we see that the quantity written down is not the total spontaneous radiation emanating from a stationary state. This is because the spontaneous transitions always take place only according to states of lower energy, or, if numbered appropriately, according to states of smaller quantum numbers. We can now state in a very formal way how this circumstance will express itself in our theory; for this we do not form the mean value, but the diagonal sum of the radiation matrix (105); This gives

$$D \left( \frac{2 e^2}{3 c^3} \ddot{\boldsymbol{q}}^2 \right) = \frac{32 \pi^4 e^2}{3 c^3} \sum_{n k} v(n k)^4 |q(n k)|^2. \quad (108)$$

Here we can summarise on the right hand side and write:

$$\frac{64 \pi^4 e^2}{3 c^3} \sum_n \left( \sum_{k < n} v(n k)^4 \cdot |q(n k)|^2 \right). \quad (109)$$

This achieves the desired assignment: To each state $n$ belongs to the radiation that corresponds to the transitions to all states $k < n$ each with the intensity known from classical theory. This is consistent with experience if one assumes that the indices $n$ for growing energies $W_n$ ordered.

This justifies Heisenberg's assumption in the limited sense described above.

It should be emphasized at once that this statement with regard to the probabilities of jumps is independent of the prerequisite of the non-degeneration of the system, i.e., the diversity of all $W_n$. Finally, we would like to point out that the statistical weights of the states are also fixed with the transition probabilities, and that is to say, each one who is separated by a row and column or a diagonal term of $\boldsymbol{W}$ the same statistical weight can be attributed to the marked states. The fact that this result (in its generalization to systems of several degrees of freedom) leads by itself to the basic principle of Bose-Einstein's light quantum statistics will be explained later.

Note on correction. The announced generalization of the theory to several degrees of freedom has meanwhile been worked out together with Mr. W. Heisenberg and will be presented in the continuation of this work. There will also be a more detailed discussion of various points already touched upon here, which have now been further clarified.
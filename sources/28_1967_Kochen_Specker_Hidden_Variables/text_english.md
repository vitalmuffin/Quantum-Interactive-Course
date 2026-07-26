# The Problem of Hidden Variables in Quantum Mechanics

Author(s): SIMON KOCHEN and E. P. SPECKER

Source: *Journal of Mathematics and Mechanics*, July, 1967, Vol. 17, No. 1 (July, 1967), pp. 59-87

Published by: Indiana University Mathematics Department

Stable URL: https://www.jstor.org/stable/24902153

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at https://about.jstor.org/terms

JSTOR

is collaborating with JSTOR to digitize, preserve and extend access to *Journal of Mathematics and Mechanics*

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

# *The Problem of Hidden Variables in Quantum Mechanics*

SIMON KOCHEN & E. P. SPECKER

*Communicated by A. M. GLEASON*

**0. Introduction.** Forty years after the advent of quantum mechanics the problem of hidden variables, that is, the possibility of imbedding quantum theory into a classical theory, remains a controversial and obscure subject. Whereas to most physicists the possibility of a classical reinterpretation of quantum mechanics remains remote and perhaps irrelevant to current problems, a minority have kept the issue alive throughout this period. (See Freistadt [5] for a review of the problem and a comprehensive bibliography up to 1957.) As far as results are concerned there are on the one hand purported proofs of the non-existence of hidden variables, most notably von Neumann's proof, and on the other, various attempts to introduce hidden variables such as de Broglie [4] and Bohm [1] and [2]. One of the difficulties in evaluating these contradictory results is that no exact mathematical criterion is given to enable one to judge the degree of success of these proposals.

The main aim of this paper is to give a proof of the nonexistence of hidden variables. This requires that we give at least a precise necessary condition for their existence. This is carried out in Sections 1 and 2. The proposals in the literature for a classical reinterpretation usually introduce a phase space of hidden pure states in a manner reminiscent of statistical mechanics. The attempt is then shown to succeed in the sense that the quantum mechanical average of an observable is equal to the phase space average. However, this statistical condition does not take into account the algebraic structure of the quantum mechanical observables. A minimum such structure is given by the fact that some observables are functions of others. This structure is independent of the particular theory under consideration and should be preserved in a classical reinterpretation. That this is not provided for by the above statistical condition is easily shown by constructing a phase space in which the statistical condition is satisfied but the quantum mechanical observables become interpreted as independent random variables over the space.

The algebraic structure to be preserved is formalized in Section 2 in the

59

*Journal of Mathematics and Mechanics*, Vol. 17, No. 1 (1967).

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

60

S. KOCHEN & E. P. SPECKER

concept of a partial algebra. The set of quantum mechanical observables viewed as operators on Hilbert space form a partial algebra if we restrict the operations of sum and product to be defined only when the operators commute. A necessary condition then for the existence of hidden variables is that this partial algebra be imbeddable in a commutative algebra (such as the algebra of all real-valued functions on a phase space). In Sections 3 and 4 it is shown that there exists a finite partial algebra of quantum mechanical observables for which no such imbedding exists. The physical description of this result may be understood in an intuitive fashion quite independently of the formal machinery introduced. An electric field of rhombic symmetry may be applied to an atom of orthohelium in its lowest energy state in any one of a specified finite number of directions. The proposed classical interpretation must then predict the resulting change in the energy state of the atom in every one of these directions. For each such prediction there exists a direction in this specified set in which the field may be applied such that the predicted value is contradicted by the experimentally measured value.

The last section deals with the logic of quantum mechanics. It is proved there that the imbedding problem we considered earlier is equivalent to the question of whether the logic of quantum mechanics is essentially the same as classical logic. The precise meaning of this statement is given in that section. Roughly speaking a propositional formula $\psi(x_1, \cdots, x_n)$ is valid in quantum mechanics if for every "meaningful" substitution of quantum mechanical propositions $P_i$ for the variables $x_i$ this formula is true, where a meaningful substitution is one such that the propositions $P_i$ are only conjoined by the logical connectives in $\psi(P_1, \cdots P_n)$ if they are simultaneously measurable. It then follows from our results that there is a formula $\varphi(x_1, \cdots, x_{16})$ which is a classical tautology but is false for some meaningful substitution of quantum mechanical propositions. In this sense the logic of quantum mechanics differs from classical logic. The positive problem of describing quantum logic has been studied in Kochen and Specker [10] and [11].

In Section 5 the present proof has been compared with von Neumann's well-known proof of the non-existence of hidden variables. von Neumann's proof is essentially based on the non-existence of a real-valued function on the set of quantum mechanical observables which is multiplicative on commuting observables and linear. In our proof we show the non-existence of a real-valued function which is both multiplicative and linear only on commuting observables. Thus, in a formal sense our result is stronger than von Neumann's. In Section 5 we attempt to show that this difference is essential. We show that von Neumann's criterion applies to a single particle of spin $\frac{1}{2}$, implying that there is no classical description of this system. On the other hand, we contradict this conclusion by constructing a classical model of a spin $\frac{1}{2}$ particle. This is done by imbedding the partial algebra of self-adjoint operators on a two-dimensional complex Hilbert space into the algebra of real-valued functions on a suitable phase space in such a way that the statistical condition is satisfied.

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

61

1. Discussion of the problem. For our purposes it is convenient to describe a physical theory within the following framework. We are given a set $\mathcal{O}$ called the set of observables and a set $S$ called the set of states. In addition, we have a function $P$ which assigns to each observable $A$ and each state $\psi$ a probability measure $P_{A\psi}$ on the real line $\mathbf{R}$. Physically speaking, if $U$ is a subset of $\mathbf{R}$ which is measurable with respect to $P_{A\psi}$, then $P_{A\psi}(U)$ denotes the probability that the measurement of $A$ for a system in the state $\psi$ yields a value lying in $U$. From this we obtain in the usual manner the expectation of the observable $A$ for the state $\psi$,

$$\text{Exp}_\psi(A) = \int_{-\infty}^{\infty} \lambda \, dP_{A\psi}(\lambda).$$

States are generally divided into two kinds, pure states and mixed states. Roughly speaking, the pure states describe a maximal possible amount of knowledge available in the theory about the physical system in question; the mixed states give only incomplete information and describe our ignorance of the exact pure state the system is actually in.

We illustrate these remarks with an example from Newtonian mechanics. Suppose we are given a system of $N$ particles. Then each pure state $\psi$ of the system is given by a $6N$-tuple $(q_1, \dots, q_{2N}, p_1, \dots, p_{2N})$ of real numbers denoting the coordinates of position and momentum of the particles. In this case, the probability $P_{A\psi}$ assigned to each observable is an atomic measure, concentrated on a single real number $a$. That is, $P_{A\psi}(U) = 1$ if $a \in U$ and $P_{A\psi}(U) = 0$ if $a \notin U$. Thus, if we introduce the phase space $\Omega$ of pure states, which we may here identify with a subset of $6N$-dimensional Euclidean space, then each observable $A$ becomes associated with a real-valued function $f_A : \Omega \to \mathbf{R}$ given by $f_A(\psi) = a$.

If $N$ is large it is not feasible to determine the precise pure state the system may be in. We resort in this case to the notion of a mixed state which gives only the probability that the system is in a pure state which lies in a region of $\Omega$. More precisely, a mixed state $\psi$ is described by a probability measure $\mu_\psi$ on the space $\Omega$, so that, for each measurable subset $\Gamma$ of $\Omega$, $\mu_\psi(\Gamma)$ is the probability that the system is in a pure state lying in $\Gamma$. It follows immediately that the probability measure $P_{A\psi}$ assigned to an observable $A$ and mixed state $\psi$ is given by the formula

$$(1) \quad P_{A\psi}(U) = \mu_\psi(f_A^{-1}(U)).$$

Thus, we have

$$(2) \quad \text{Exp}_\psi(A) = \int_\Omega f_A(\omega) \, d\mu_\psi(\omega).$$

In the case of quantum mechanics the set $\mathcal{O}$ of observables is represented by self-adjoint operators on a separable Hilbert space $\mathcal{H}$. The pure states are given by the one-dimensional linear subspaces of $\mathcal{H}$. The probability $P_{A\psi}$ is defined

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

62

S. KOCHEN & E. P. SPECKER

by taking the spectral resolution of $A$:

$$A = \int_{-\infty}^{\infty} \lambda \, dE_A(\lambda),$$

where $E_A$ is the spectral measure corresponding to $A$. Then

$$P_{A\psi}(U) = \langle E_A(U)\psi, \psi \rangle,$$

where $\psi$ is any unit vector in the one-dimensional linear subspace corresponding to the pure state $\psi$. Hence, by the spectral theorem

$$\text{Exp}_\psi(A) = \int_{-\infty}^{\infty} \lambda \, d\langle E_A(U)\psi, \psi \rangle = \langle A\psi, \psi \rangle.$$

Although there may be states $\psi$ for each observable $A$ in this theory such that $P_{A\psi}$ is atomic, there are no longer, as in classical mechanics, states $\psi$ such that $P_{A\psi}$ is atomic simultaneously for all observables.

The problem of hidden variables may be described within the preceding framework. Let us recall that the hidden variables problem was successfully solved in a classical case, namely, the theory of thermodynamics. The theory of macroscopic thermodynamics is a discipline which is independent of classical mechanics. This theory has its own set of observables such as pressure, volume, temperature, energy, and entropy and its own set of states. This theory shares with quantum mechanics the property that the probability $P_{A\psi}$ is not atomic even for pure states $\psi$. In most cases this probability is sufficiently concentrated about a single point so that it is in practice replaced by an atomic measure. However, there are cases where distinct macroscopic phenomena (such as critical opalescence) depend upon these fluctuations.

It proves possible in this case to introduce an underlying theory of classical mechanics on which thermodynamics may be based. In terms of the preceding description a phase space $\Omega$ of "hidden" pure states is introduced. In physical terms the system is assumed to consist of a large number of molecules and $\Omega$ is the space of the coordinates of position and momentum of all the molecules. Every pure state $\psi$ of the original theory of thermodynamics is now interpreted as a mixed state of the new theory, i.e., as a probability measure $\mu_\psi$ over the space $\Omega$. Every observable $A$ of thermodynamics is interpreted as a function $f_A : \Omega \to \mathbb{R}$, and it is assumed that condition (1) and hence (2) holds. It is in this way that the laws of thermodynamics become consequences of classical Newtonian mechanics via statistical mechanics. The formula (2) is the familiar statistical mechanical averaging process. This example has been considered as the classic case of a successful introduction of hidden variables into a theory.

The problem of hidden variables for quantum mechanics may be interpreted in a similar fashion as introducing a phase space $\Omega$ of hidden states for which condition (1) is true. This statistical condition (1) has in fact been taken as a proof of the success of various attempts to introduce a phase space into quantum mechanics. Now, in fact the condition (1) can hardly be the only requirement

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

63

for the existence of hidden variables. For we may always introduce, at least mathematically, a phase space $\Omega$ into a theory so that (1) is satisfied. To see this, let

$$\Omega = \mathbf{R}^0 = \{\omega \mid \omega : \mathcal{O} \to \mathbf{R}\}.$$

If $A \in \mathcal{O}$, let $f_A : \Omega \to \mathbf{R}$ be defined by $f_A(\omega) = \omega(A)$. If $\psi \in S$, let

$$\mu_\psi = \prod_{A \in \mathcal{O}} P_{A\psi},$$

the product measure of the probabilities $P_{A\psi}$. Then,

$$\mu_\psi f_A^{-1}(U) = \mu_\psi(\{\omega \mid \omega(A) \in U\}) = P_{A\psi}(U).$$

We have two reasons for mentioning this somewhat trivial construction. First, in the various attempts to introduce hidden variables into quantum mechanics, the only explicitly stated requirement that is to be fulfilled is the condition (1). (See Bohm [1] and [2], Bopp [3], Siegel and Wiener [16], and especially the review of [16] in Schwartz [15].) Of course, the above space $\Omega$ is far more artificial than the spaces proposed in these papers, but the only purpose here was to point out the insufficiency of the condition (1) as a test for the adequacy of the solution of the problem.

Our second reason for introducing the space $\mathbf{R}^0$ is that it indicates the direction in which the condition (1) is inadequate. For each state $\psi$, as interpreted in the space $\mathbf{R}^0$, the functions $f_A$ are easily seen to be measurable functions with respect to the probability measure $\mu_\psi$. In the language of probability theory the observables are thus interpreted as random variables for each state $\psi$. It is not hard to show furthermore that in this representation the observables appear as independent random variables.

Now it is clear that the observables of a theory are in fact not independent. The observable $A^2$ is a function of the observable $A$ and is certainly not independent of $A$. In any theory, one way of measuring $A^2$ consists in measuring $A$ and squaring the resulting value. In fact, this may be used as the *definition* of a function of an observable. Namely, we define the observable $g(A)$ for every observable $A$ and Borel function $g : \mathbf{R} \to \mathbf{R}$ by the formula

$$(3) \quad P_{g(A)\psi}(U) = P_{A\psi}(g^{-1}(U))$$

for each state $\psi$. If we assume that every observable is determined by the function $P$, i.e., $P_{A\psi} = P_{B\psi}$ for every state $\psi$ implies that $A = B$, then the formula (3) defines the observable $g(A)$. This definition coincides with the definition of a function of an observable in both quantum and classical mechanics.

Thus the measurement of a function $g(A)$ of an observable $A$ is independent of the theory considered—one merely writes $g(a)$ for the value of $g(A)$ if $a$ is the measured value of $A$. The set of observables of a theory thereby acquires an algebraic structure, and the introduction of hidden variables into a theory should preserve this structure. In more detail, we require for the successful

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

64

S. KOCHEN & E. P. SPECKER

introduction of hidden variables that a space Ω be constructed such that condition (1) is satisfied and also that

$$f_{g(A)} = g(f_A) \tag{4}$$

for every Borel function g and observable A of the theory. Note that this condition is satisfied in the statistical mechanical description of thermodynamics.

Our aim is to show that for quantum mechanics no such construction satisfying condition (4) is possible. However, condition (4) as it stands proves too unwieldy and we shall first replace it by a more tractable condition.

2. Partial algebras. We shall say that the observables $A_i, i \in I$, in a theory are commeasurable if there exists an observable B and (Borel) functions $f_i, i \in I$, such that $A_i = f_i(B)$ for all $i \in I$. Clearly in this case it is possible to measure the observables $A_i, i \in I$, simultaneously for it is only necessary to measure B and apply the function $f_i$ to the measured value to obtain the value of $A_i$. In quantum mechanics a set $\{A_i \mid i \in I\}$ of observables is said to be simultaneously measurable if as operators they pairwise commute. A classical theorem on operators shows that this coincides with the above definition (see, e.g., Neumark [12, Thm. 6]). (Note that as a result in the case of quantum mechanics the $A_i, i \in I$, are commeasurable if they are pairwise commeasurable.)

If $A_1$ and $A_2$ are commeasurable then we may define the observables $\mu_1 A_1 + \mu_2 A_2$ and $A_1 A_2$ for all real $\mu_1, \mu_2$. For then $A_1 = f_1(B)$ and $A_2 = f_2(B)$ for some observable B and functions $f_1$ and $f_2$. Hence we have

$$\mu_1 A_1 + \mu_2 A_2 = (\mu_1 f_1 + \mu_2 f_2)(B),$$
$$A_1 A_2 = (f_1 f_2)(B). \tag{5}$$

With linear combinations and products of commeasurable observables defined the set of observables acquires the structure of a partial algebra. Note that condition (4) implies that the partial operations defined in (5) are preserved under the map f. These ideas will now be formalized in the following definitions.

Definition. A set A forms a partial algebra over a field K if there is a binary relation $\wp$ (commeasurability) on A, (i.e., $\wp \subseteq A \times A$), operations of addition and multiplication from $\wp$ to A, scalar multiplication from $K \times A$ to A, and an element 1 of A, satisfying the following properties:

1. The relation $\wp$ is reflexive and symmetric, i.e., $a \wp a$ and $a \wp b$ implies $b \wp a$ for all $a, b \in A$.

2. For all $a \in A, a \wp 1$.

3. The relation $\wp$ is closed under the operations, i.e., if $a_i \wp a_j$ for all $1 \leq i, j \leq 3$ then $(a_1 + a_2) \wp a_3, a_1 a_2 \wp a_3$ and $\lambda a_1 \wp a_3$, for all $\lambda \in K$.

4. If $a_i \wp a_j$ for all $1 \leq i, j \leq 3$, then the values of the polynomials in $a_1, a_2, a_3$ form a commutative algebra over the field K.

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

65

It follows immediately from the definition of a partial algebra that if $D$ is a set of pairwise commasurable elements of $A$ then the set $D$ generates a commutative algebra in $A$.

We have defined the notion of a partial algebra over an arbitrary field $K$ but there are two cases which are of interest to us. The first is the field $\mathbf{R}$ of real numbers and the second is the field $Z_2$ of two elements. For the case of a partial algebra over $Z_2$ we may define the Boolean operations in terms of the ring operations in the usual manner: $a \cap b = ab$, $a \cup b = a + b - ab$, $a' = 1 - a$. It follows that if $a_i \circ a_j$, $1 \leq i, j \leq 3$, then the polynomials in $a_1, a_2, a_3$ form a Boolean algebra. We shall call a partial algebra over $Z_2$ a *partial Boolean algebra*. It is clear how we may define this notion directly in terms of the operations $\cap, \cup, \prime$. What makes a partial Boolean algebra important for our purposes is that the set of idempotent elements of a partial algebra $\mathfrak{R}$ forms a partial Boolean algebra. This is a counterpart of the familiar fact that the set of idempotents of a commutative algebra forms a Boolean algebra.

We consider some examples of partial algebras. Let $H(U^\alpha)$ be the set of all self-adjoint operators on a complex Hilbert space $U^\alpha$ of dimension $\alpha$. If we take the relation $\wp$ to be the relation of commutativity then $H(U^\alpha)$ forms a partial algebra over the field $\mathbf{R}$ of reals. In this case the idempotents are the projections of $U^\alpha$. Thus the set $\mathbf{B}(U^\alpha)$ of projections forms a partial Boolean algebra. Because every projection corresponds uniquely to a closed linear subspace of $U^\alpha$, we may alternatively consider $\mathbf{B}(U^\alpha)$ as the partial Boolean algebra of closed linear subspaces of $U^\alpha$. The direct definition of the relation $\wp$ in this interpretation of $\mathbf{B}(U^\alpha)$ is: $a \wp b$ if there exists elements $c, d, e$ in $\mathbf{B}(U^\alpha)$ which are mutually orthogonal with $a = c \oplus d$ and $b = d \oplus e$. Furthermore $a \cap b$ denotes the intersection of the two subspaces $a$ and $b$, $a \cup b$ denotes the space spanned by $a$ and $b$, and $a'$ denotes the orthogonal complement of $a$.

We have seen that the set $\mathfrak{O}$ of observables of a physical theory forms a partial algebra over $\mathbf{R}$ if we take $\wp$ to be the relation of commasurability. If $A$ is an idempotent in $\mathfrak{O}$, then it follows from the definition of $A^2$, that the measured values of the observable $A$ can only be 1 or 0. By identifying these values with truth and falsity we may consider each such idempotent observable as a proposition of the theory. (See von Neumann [19, Ch. III.5] for a more detailed discussion of this point.) Thus, the set of propositions of a physical theory form a partial Boolean algebra. It is a basic tenet of quantum theory that the set of its observables may be identified with a partial sub-algebra $Q$ of $H(U^\alpha)$, the partial algebra of self-adjoint operators on a separable complex Hilbert space. This implies then that the propositions of quantum mechanics form a partial Boolean sub-algebra $\mathfrak{B}$ of $\mathbf{B}(U^\alpha)$.

Every commutative algebra $A$ forms a partial algebra if we take the relation $\wp$ to be $A \times A$. The following construction of a partial algebra is of interest because it gives us an alternative way of viewing partial algebras. Let $C_i$, $i \in I$, be a non-empty family of commutative algebras over a fixed field $K$ which satisfy the following conditions:

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

66

S. KOCHEN & E. P. SPECKER

(a) For every $i, j \in I$ there is a $k \in I$ such that $C_i \cap C_j = C_k$.
(b) If $a_1, \dots, a_n$ are elements of $C = \bigcup_{i \in I} C_i$ such that any two of them lie in a common algebra $C_i$, then there is a $k \in I$ such that $a_1, \dots, a_n \in C_k$.

The set $C$ forms a partial algebra over $K$ if we define the relations (i) $a \nmid b$, (ii) $ab = c$, and (iii) $a + b = c$ in $C$ by the condition that there exist an $i \in I$ such that (i) $a, b \in C_i$, (ii) $ab = c$ in $C_i$ and (iii) $a + b = c$ in $C_i$ respectively. It is not difficult to show that every partial algebra is isomorphic to an algebra of this type. (We may thus view a partial algebra as a category in which the objects are commutative algebras and the maps are imbeddings.)

**Definition.** A map $h : U \to V$ between two partial algebras over a common field $K$ is a *homomorphism* if for all $a, b \in U$ such that $a \nmid b$ and all $\mu, \lambda \in K$,

$$\begin{aligned} h(a) \nmid h(b), \\ h(\mu a + \lambda b) &= \mu h(a) + \lambda h(b), \\ h(ab) &= h(a)h(b), \\ h(1) &= 1. \end{aligned}$$

Given this definition we may state what our condition (4) of Section 1 on the existence of hidden variables implies for the partial algebra $Q$ of observables of quantum mechanics. The set $\mathbf{R}^\Omega$ of all functions $f : \Omega \to \mathbf{R}$ from a space $\Omega$ of hidden states into the reals forms a commutative algebra over $\mathbf{R}$. From the way in which the partial operations on the set of observables of a theory are defined (equation (5)), condition (4) implies that there is an imbedding of the partial algebra into the algebra $\mathbf{R}^\Omega$. Our conclusion of this discussion is then the following:

*A necessary condition for the existence of hidden variables for quantum mechanics is the existence of an imbedding of the partial algebra $Q$ of quantum mechanical observables into a commutative algebra.*

A possible objection to this conclusion is that the map of $Q$ into the commutative algebra $C$ need not be single-valued since a given quantum-mechanical observable may split into several observables in $C$. Thus, $Q$ might be a homomorphic image of $C$. We shall meet this objection in Section 5 by showing that even such a many-valued map of $Q$ into $C$ does not exist.

Now if $\varphi : \mathfrak{N} \to C$ is an imbedding of a partial algebra $\mathfrak{N}$ into a commutative algebra, it follows immediately that $\varphi$ restricted to the partial Boolean algebra of idempotents of $\mathfrak{N}$ is an imbedding into the Boolean algebra of idempotents of $C$. Thus, the existence of hidden variables implies the existence of an imbedding of the partial Boolean algebra of propositions of quantum mechanics into a Boolean algebra. We may justify the last statement independently of the previous discussion. For the set of propositions of a classical reinterpretation of quantum mechanics must form a Boolean algebra. But the conjunction of

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

67

two commasurable propositions has the same meaning in quantum mechanics as in classical physics and so should be preserved in the classical interpretation.

Let $h : Q \rightarrow \mathbb{R}$ be a homomorphism of the partial algebra $Q$ of quantum mechanical observables into $\mathbb{R}$. Physically speaking $h$ may be considered as a *prediction* function which simultaneously assigns to every observable a predicted measured value. If we assume the existence of a hidden state space $\Omega$, so that $Q$ is imbeddable by a map $f$ into the algebra $\mathbb{R}^2$, then each hidden state $\omega \in \mathbb{R}^2$ defines such a homomorphism $h : Q \rightarrow \mathbb{R}$, namely $h(A) = f_A(\omega)$. Thus, the existence of hidden variables implies the existence of a large number of prediction functions. Every homomorphism $h : \mathfrak{N} \rightarrow \mathbb{R}$ is by restriction a homomorphism of the partial Boolean algebra of idempotents onto $Z_2$. The following theorem characterizes the imbedding of a partial Boolean algebra into a Boolean algebra in terms of its homomorphisms onto $Z_2$.

**Theorem 0.** Let $\mathfrak{N}$ be a partial Boolean algebra. A necessary and sufficient condition that $\mathfrak{N}$ is imbeddable in a Boolean algebra $B$ is that for every pair of distinct elements $a, b$ in $\mathfrak{N}$ there is a homomorphism $h : \mathfrak{N} \rightarrow Z_2$ such that $h(a) \neq h(b)$.

**Proof.** Suppose $\varphi : \mathfrak{N} \rightarrow B$ is an imbedding. Since $\varphi(a) \neq \varphi(b)$ if $a \neq b$, there exists by the semi-simplicity property of Boolean algebras (see *e.g.*, Halmos [8, sect. 18, Lemma 1]), a homomorphism $h : B \rightarrow Z_2$ such that $h\varphi(a) \neq h\varphi(b)$. Hence $k = h\varphi$ is the required homomorphism of $\mathfrak{N}$ onto $Z_2$.

To prove the converse, let $S$ be the set of all non-trivial homomorphisms of $\mathfrak{N}$ into $Z_2$. Define the map $\varphi : \mathfrak{N} \rightarrow Z_2^S$ by letting $\varphi(a)$ be the function $g : S \rightarrow Z_2$ such that $g(h) = h(a)$ for every $h \in S$. Then it is easily checked that $\varphi$ is an imbedding of $\mathfrak{N}$ into the Boolean algebra $Z_2^S$.

The next two sections are devoted to showing that there does not exist even a single homomorphism of the partial Boolean algebra $\mathfrak{B}$ of the propositions of quantum mechanics onto $Z_2$.

**3. The partial Boolean algebra $\mathbf{B}(\mathbf{E}^\alpha)$.** Let $\mathbf{B}(E^\alpha)$ denote the partial Boolean algebra of linear subspaces of $\alpha$-dimensional Euclidean space $E^\alpha$. Our aim in this section is to show that there is a finite partial Boolean subalgebra $D$ of $\mathbf{B}(E^\alpha)$ such that there is no homomorphism $h : D \rightarrow Z_2$. In the next section we shall show that the elements of $D$ in fact correspond to quantum mechanical observables.

Let $D$ be a partial Boolean subalgebra of $\mathbf{B}(E^\alpha)$ with a homomorphism $h : D \rightarrow Z_2$. If $s_1, s_2, s_3$ are mutually orthogonal one-dimensional linear subspaces of $D$, then

$$h(s_1) \cup h(s_2) \cup h(s_3) = h(s_1 \cup s_2 \cup s_3) = h(E^\alpha) = 1 \text{ and}$$
$$h(s_i) \cap h(s_j) = h(s_i \cap s_j) = h(0) = 0 \quad (6)$$

for $1 \leq i \neq j \leq 3$. Hence, exactly one of every three mutually orthogonal lines is mapped by $h$ onto 1. If we replace the lines by lines of unit length then $h$

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

68

S. KOCHEN & E. P. SPECKER

induces a map $h^* : T \to \{0, 1\}$ from a subset $T$ of the unit sphere $S$ into $\{0, 1\}$ such that for any three mutually orthogonal points in $T$ exactly one is mapped by $h^*$ into 1.

It will be convenient in what follows to represent points on $S$ by the vertices of a graph. Two vertices which are joined by an edge in the graph represent orthogonal points on $S$. When we say that a graph $\Gamma$ is realizable on $S$ we mean that there is an assignment of points of $S$ to the vertices of $\Gamma$, distinct points for distinct vertices, with the orthogonality relations as indicated in $\Gamma$.

Lemma 1. The following graph $\Gamma_1$ is realizable on $S$.

![img-0.jpeg](img-0.jpeg)

In fact, if $p$ and $q$ are points on $S$ such that $0 \leq \sin \theta \leq \frac{1}{2}$ where $\theta$ is the angle subtended by $p$ and $q$ at the center of $S$, then there exists a map $u : \Gamma_1 \to S$ such that $u(a_0) = p$ and $u(a_q) = q$.

Proof. Since $u(a_8)$ is orthogonal to $u(a_0) \cup u(a_9)$ and $u(a_7)$ is orthogonal to $u(a_8)$, $u(a_7)$ lies in the plane $u(a_0) \cup u(a_9)$. Also since $u(a_7)$ is orthogonal to $u(a_8)$, we have that $\varphi = \pi/2 - \theta$, where $\varphi$ is the angle subtended at the center of $S$ by $u(a_0)$ and $u(a_7)$. Let $u(a_3) = \bar{\imath}$ and $u(a_8) = \bar{k}$. Then we may take

$$u(a_1) = (\bar{j} + x\bar{k})(1 + x^2)^{-1/2} \quad \text{and} \quad u(a_2) = (\bar{\imath} + y\bar{j})(1 + y^2)^{-1/2}.$$

The orthogonality conditions then force

$$u(a_3) = (x\bar{j} - \bar{k})(1 + x^2)^{-1/2},$$

$$u(a_4) = (y\bar{\imath} - \bar{j})(1 + y^2)^{-1/2},$$

and hence,

$$u(a_0) = (xy\bar{\imath} - x\bar{j} + \bar{k})(1 + x^2 + x^2y^2)^{-1/2},$$

$$u(a_7) = (\bar{\imath} + y\bar{j} + xy\bar{k})(1 + y^2 + x^2y^2)^{-1/2}.$$

Thus

$$\cos \varphi = \frac{xy}{((1 + x^2 + x^2y^2)(1 + y^2 + x^2y^2))^{1/2}}.$$

By elementary calculus the maximum value of this expression is $\frac{1}{2}$. Hence $\Gamma_1$ is realizable if $0 \leq \cos \varphi \leq \frac{1}{2}$, i.e., $0 \leq \sin \theta \leq \frac{1}{2}$.

Lemma 2. The following graph $\Gamma_2$ is realizable on $S$.

This content downloaded from 140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

69

![img-1.jpeg](img-1.jpeg)

The graph $\Gamma_2$ is obtained from the above diagram by identifying the points $p_0$ and $a$, $q_0$ and $b$, and $r_0$ and $c$. The vertices of $\Gamma_2$ are the points on the rim of this diagram.

Proof. For $0 \leq k \leq 4$, let

$$P_k = \cos \frac{\pi k}{10} \bar{i} + \sin \frac{\pi k}{10} \bar{j},$$

$$Q_k = \cos \frac{\pi k}{10} \bar{j} + \sin \frac{\pi k}{10} \bar{k},$$

$$R_k = \sin \frac{\pi k}{10} \bar{i} + \cos \frac{\pi k}{10} \bar{k}.$$

Let $u(p_k) = P_k$, $u(q_k) = Q_k$, $u(r_k) = R_k$, for $0 \leq k \leq 4$. Since the subgraph of $\Gamma_2$ contained between the points $p_0$, $p_1$, and $r_0$ is a copy of $\Gamma_1$ and the angle subtended by $P_0$, $P_1$ is $\pi/10$ ($\sin \pi/10 < \frac{1}{3}$), we may extend $u$ to a realization of this subgraph on $S$. A realization of the subgraph of $\Gamma_2$ contained between the points $p_1$, $p_2$, and $r_0$ is then obtained by rotating $P_0$ to $P_1$ about $R_0$. The remainder of the realization $u$ is obtained by similar rotations about $R_0$, $P_0$, and $Q_0$.

Let $T$ be the image of $\Gamma_2$ under $u$, consisting of 117 points on $S$. Let $D$ be the partial Boolean subalgebra generated by $T$ in $\mathbf{B}(E^3)$. (This corresponds to completing the graph $\Gamma_2$ so that every edge lies in a triangle. In the resulting graph the points and edges correspond to one and two dimensional linear subspaces of $\mathbf{B}(E^3)$ respectively.)

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

70

S. KOCHEN & E. P. SPECKER

**Theorem 1.** *The finite partial Boolean algebra D has no homomorphism onto $Z_2$.*

**Proof.** As we have seen, such a homomorphism $h : D \to Z_2$ induces a map $h^* : T \to \{0, 1\}$ satisfying condition (6). Reverting to the graph $\Gamma_2$, we shall assume that there is a map $k : \Gamma_2 \to \{0, 1\}$ satisfying condition (6). Let us consider the action of $k$ on a copy in $\Gamma_2$ of the graph $\Gamma_1$. Suppose that $k(a_0) = 1$, then it follows that $k(a_9) = 1$. For if $k(a_9) = 0$, then since $k(a_8) = 0$ we must have $k(a_7) = 1$. Hence, $k(a_1) = k(a_2) = k(a_3) = k(a_4) = 0$; so that $k(a_3) = k(a_6) = 1$, a contradiction.

Now since $p_0$, $q_0$, and $r_0$ lie in a triangle in $\Gamma_2$, exactly one of these points is mapped by $k$ onto 1, say $k(p_0) = 1$. Hence, by the above argument $k(p_1) = 1$. Continuing in this manner in $\Gamma_2$ we find $k(p_2) = k(p_3) = k(p_4) = k(q_0) = 1$. But $k(q_0) = 1$ contradicts the condition that $k(p_0) = 1$, and proves the theorem.

**Remark.** Theorem 1 implies that there is no map of the sphere $S$ onto $\{0, 1\}$ satisfying condition (4), and hence no homomorphism from $\mathbf{B}(E^3)$ onto $Z_2$. This result, first stated in Specker [17], can be obtained more simply either by a direct topological argument or by applying a theorem of Gleason [6]. However, it seems to us important in the demonstration of the non-existence of hidden variables that we deal with a small finite partial Boolean algebra. For otherwise a reasonable objection can be raised that in fact it is not physically meaningful to assume that there are a continuum number of quantum mechanical propositions.

To obtain a partial Boolean subalgebra of $\mathbf{B}(E^3)$ which is not imbeddable in a Boolean algebra a far smaller graph than $\Gamma_2$ suffices. The following graph $\Gamma_3$ may be shown to be realizable on $S$ in similar fashion to the proof of Lemma 2.

![img-2.jpeg](img-2.jpeg)

Let $F$ be the partial Boolean algebra generated by the set of 17 points on $S$ corresponding to $\Gamma_3$. If $h : F \to Z_2$ is a homomorphism then as we have seen in the proof of Theorem 1, if $h(a) = 1$ then $h(b) = 1$; by symmetry also $h(b) = 1$ implies $h(a) = 1$. That is, $h(a) = h(b)$ in every homomorphism $h : F \to Z_2$. If $\varphi : F \to B$ is an imbedding of $F$ into a Boolean algebra, then by the semi-simplicity of $B$ there exists a homomorphism $h' : B \to Z_2$ such that $h'(\varphi(a)) \neq h'(\varphi(b))$. Hence, $h = h'\varphi$ is a homomorphism from $F$ onto $Z_2$ such that $h(a) \neq h(b)$, a contradiction.

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

71

4. The operators as observables. Let us consider a system in which the total angular momentum operator $\bar{J}$ commutes with the Hamiltonian operator $H$, so that $\bar{J}$ is a constant of the motion. We assume further that the system is in a state for which the principal quantum number $n = 2$ and the azimuthal quantum number $j = 1$, so that the total angular momentum is $\sqrt{2}\hbar$. The eigenspace $N$ corresponding to the eigenvalue $2\hbar^2$ of $J^2$ is three-dimensional. We adopt the convention that $\hbar = 1$.

Let $J_x$, $J_y$, and $J_z$ be the components of $\bar{J}$ in three mutually orthogonal directions $x$, $y$, and $z$. We shall show that in the three dimensional representation given by $n = 2$, $j = 1$ the following relations hold.

$$(7) \quad [J_x^2, J_y^2] = [J_y^2, J_z^2] = [J_z^2, J_z^2] = 0.$$

In the usual representation in which $J^2$ and $J_z$ are diagonal we have (see Schiff [14] p. 146)

$$J_z = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{bmatrix}, \quad J_x = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \quad J_y = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 & -i & 0 \\ i & 0 & -i \\ 0 & i & 0 \end{bmatrix}.$$

It is now easily checked that the relations (7) follow. It may be of some interest to give a coordinate-free proof of these relations. The following proof was suggested to us by J. Chaiken. Let $J_\pm = J_x \pm iJ_y$. From the commutation relations $[J_x, J_y] = iJ_x$, etc., for $J_x$, $J_y$, and $J_z$ it follows that

$$[J_x^2, J_y^2] = (J_x - I)J_+^2 - (J_x + I)J_-^2.$$

Now if $J_x\psi = m\psi$ then

$$J_x J_+ \psi = \begin{cases} (m+1)J_+ \psi & \text{if } -j \le m < j \\ 0 & \text{if } m = j. \end{cases}$$

Hence, if $\varphi$ is any vector in the three-dimensional representation ($n = 2$, $j = 1$), then $J_+\varphi$ is either zero or an eigenvector of $J_z$ with eigenvalue $+1$. In either case, $(J_x - I)J_+\varphi = 0$. Hence $(J_x - I)J_+^2 = 0$ in this representation. Similarly, $(J_x + I)J_-^2 = 0$, so that $[J_x^2, J_y^2] = 0$. This establishes (7). Note that these relations do not hold in any higher dimensional representation.

We now show that there is an imbedding $\psi$ of the partial Boolean algebra $\mathbf{B}(E^3)$ into the partial Boolean algebra $\mathfrak{B}$ of quantum mechanical proposition. Let $P$ be the projection operator belonging to the 3-dimensional eigenspace $N$. To each one-dimensional linear subspace $\alpha$ of $E^3$ there corresponds an operator $J_\alpha$, the component of angular momentum in the direction in physical space defined by $\alpha$. Let $\psi(\alpha) = PJ_\alpha^2$. If $\beta$ is a two-dimensional linear subspace of $E^3$ let $\alpha$ be the orthogonal complement of $\beta$ in $E^3$. We define $\psi(\beta) = P - PJ_\alpha^2$. Finally we let $\psi(E^3) = P$ and $\psi(0) = 0$. This defines the map $\psi$. To show that $\psi$ is an imbedding it clearly suffices to prove that if $\alpha$ and $\beta$ are

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

72

S. KOCHEN & E. P. SPECKER

orthogonal one-dimensional linear subspaces of $E^3$, then $[PJ_\alpha^2, PJ_\beta^2] = 0$. But this is precisely the relation (7) which we have established. Note that the projection operator $PJ_\alpha^2$ is an element of $\mathfrak{B}$; it corresponds to the proposition $P_\alpha$: "For the system in energy state $n = 2$ and total angular momentum state $j = 1$, the component of angular momentum in the direction $\alpha$ is not 0."

Since then the finite partial Boolean algebra $D$ has been imbedded in $\mathfrak{B}$, it follows by Section 3 that there is no homomorphism of $\mathfrak{B}$ onto $Z_2$.

In the above argument we have assumed that in the three-dimensional representation the observables $J_\alpha^2, J_\beta^2$ and $J_\beta^2$ are commasurable. This remains to be justified. Of course, we have seen that these operators commute and it is a generally accepted assumption of quantum mechanics that commuting operators correspond to commasurable observables. A rationale for this assumption, as we pointed out in Section 2, is that if $A_i, i \in I$, is a set of mutually pairwise commuting self-adjoint operators, then there exists a self-adjoint operator $B$ and Borel functions $f_i, i \in I$ such that $A_i = f_i(B)$. However this justification hinges on the existence of a physical observable which corresponds to the operator $B$. We shall now show that there is in this case an operator $H_J$ of which $J_\alpha^2, J_\beta^2$, and $J_\beta^2$ are functions and which corresponds to an observable.

Let $a, b$, and $c$ be distinct real numbers and define

$$H_J = aJ_\alpha^2 + bJ_\beta^2 + cJ_\beta^2.$$

Then it is easily checked that in the three dimensional representation

$$\begin{aligned} J_\alpha^2 &= (a - b)^{-1}(c - a)^{-1}(H_J - (b + c))(H_J - 2a), \\ J_\beta^2 &= (b - c)^{-1}(a - b)^{-1}(H_J - (c + a))(H_J - 2b), \\ J_\beta^2 &= (c - a)^{-1}(b - c)^{-1}(H_J - (a + b))(H_J - 2c). \end{aligned} \quad (8)$$

Consider now a physical system the total angular momentum of which is spin angular momentum $S$, with $S$ having the constant value $\sqrt{2}\hbar$. An example of such a system is an atom of orthohelium in the $2^3S_1$ state, i.e., the lowest triplet state of helium, with the principal quantum number $n = 2$, the orbital quantum number $l = 0$, and spin $s = 1$. (Note that this is a stable state for the atom even though it is not the ground state. (It is called a metastable state.) The reason for the stability is that the ground state ($n = 1$) of the atom occurs only for parahelium, i.e., the singlet state of helium with $s = 0$; and transitions are forbidden between the singlet and the triplet states of helium.)

We now apply to the system in this state a small electric field $E$ which has rhombic symmetry about the atom. (Such a field, for instance, results from placing point charges at the points $(\pm u, 0, 0)$, $(0, \pm v, 0)$ $(0, 0, \pm w)$, with $u$, $v$, and $w$ distinct, the atom being at the origin.) By perturbation methods it may be shown that the Hamiltonian $H$ of the system is perturbed to a new Hamiltonian $H + H_S$, where, from the rhombic symmetry of the field, the additional term $H_S$, called the spin-Hamiltonian, has the form $H_S = aS_\alpha^2 +$

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

73

$bS_y^2 + cS_y^2$ with $a$, $b$, and $c$ distinct in the three dimensional representation. (See e.g., Stevens [18] and Pryce [13] for a proof.)

Thus the operator $H_s = aS_x^2 + bS_y^2 + cS_z^2$ corresponds to a physical observable—the change in the energy of the lowest orbital state of orthohelium resulting from the application of a small electric field with rhombic symmetry. The change in energy levels may be measured by studying the spectrum of the helium atom after the field is applied. The possible measured values in the change in energy levels is either $a + b$, $b + c$, or $c + a$, since these are the eigenvalues of $H_s$ in the three-dimensional representation. Since $a$, $b$, and $c$ are distinct, so are $a + b$, $b + c$, and $c + a$. Thus, a measurement of $H_s$ leads immediately to the simultaneous measurement of $S_x^2$, $S_y^2$ and $S_z^2$. If, for instance the measured value of $H_s$ is $a + b$, then we infer that the values of $S_x^2$ and $S_y^2$ are each 1 and the value of $S_z^2$ is 0. (This is equivalent to applying the relations (8) to $H_s$.)

We remark that although such an experiment has probably not been carried out on the helium atom, related experiments are described in the literature. For instance Griffith and Owen [7] investigated in paramagnetic resonance experiments a nickel Tulton salt, nickel fluosilicate. This salt consists of a nickel ion surrounded by an octahedron of water molecules and it occurs in the state $J^2 = S^2 = 2\hbar^2$. The water molecules form a crystalline electric field with rhombic symmetry about the nickel ion. The resulting spin-Hamiltonian $H_s$ takes the form $aS_x^2 + bS_y^2 + cS_z^2$ with $a$, $b$, and $c$ distinct. This is in all respects similar to the situation we have discussed above. Of course, in this case the electric field is supplied by the crystal and cannot be switched on and off or rotated at will to measure $S_x^2$, $S_y^2$, and $S_z^2$ in any three prescribed orthogonal directions. Nevertheless, the experimental agreement with the quantum mechanical predictions here suggests a similar agreement for the case of an external electric field applied to a helium atom.

To sum up the last two sections we shall recapitulate our case against the existence of hidden variables for quantum mechanics. We have used the formal technique of introducing the concept of a partial algebra to discuss this question but we may now give a direct intuitive argument. If a physicist $X$ believes in hidden variables he should be able to predict (in theory) the measured value of every quantum mechanical observable. We now confront $X$ with the problem of simultaneously answering the question:

"Is the component of spin angular momentum in the direction $\alpha$ equal to zero for the lowest orbital state of orthohelium ($n = 2, l = 0, s = 1$)" where $\alpha$ varies over the 117 directions provided in the proof of Theorem 1. For each such prediction by $X$ we can find, by Theorem 1, three orthogonal directions $x, y, z$ among the 117 for which this prediction contradicts the statement

"Exactly one of the three components of spin angular momentum $S_x$, $S_y$, $S_z$ of the lowest orbital state of orthohelium is zero."

This statement is what is predicted by quantum mechanics since

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

74

S. KOCHEN & E. P. SPECKER

$$S_x^2 + S_y^2 + S_z^2 = S^2 = 2\hbar^2$$

and each of $S_x^2$, $S_y^2$, $S_z^2$ thus has the value 0 or $\hbar^2$. Thus the prediction of $X$ contradicts the prediction of quantum mechanics. Furthermore as we have seen in this section this prediction may be experimentally verified by simultaneously measuring $S_x^2$, $S_y^2$, and $S_z^2$. Our conclusion is that every prediction by physicist $X$ may be contradicted by experiment. (It has been argued (See Bohm [2 Sect. 9]) that with the introduction of a hidden state space $\Omega$ the present quantum mechanical observables such as spin will not be the fundamental observables of the new theory. Certainly, many new possible observables are thereby introduced (namely, functions $f : \Omega \to \mathbb{R}$). The quantum observables represent not true observables of the system itself which is under study, but reflect rather properties of the disturbed system and the apparatus. This is nevertheless no argument against the above proof. For in a classical interpretation of quantum mechanics observables such as spin will still be functions on the phase space of the combined apparatus and system and as such should be simultaneously predictable).

**5. Homomorphic relations.** In Section 1 we reduced the question of hidden variables to the existence of an imbedding of $Q$ into a commutative algebra $C$. We discuss here a possible objection to this reduction. It may be argued that in a classical reinterpretation of quantum mechanics a given observable may split into several new observables. Thus, the correspondence between $Q$ and $C$ may take the form of a homomorphism $\psi : C \to Q$ from $C$ onto $Q$. This possibility is provided for in the following theorem.

**Definition.** Let $\mathfrak{N}$ and $\mathfrak{L}$ be partial algebras over a common field $K$. A relation $R \subseteq \mathfrak{N} \times \mathfrak{L}$ is called a *homomorphic relation* between $\mathfrak{N}$ and $\mathfrak{L}$ if, for all $x \notin y$ in $\mathfrak{N}$ and $\alpha \notin \beta$ in $\mathfrak{L}$, $R(x, \alpha)$ and $R(y, \beta)$ imply that $R(\lambda x + \mu y, \lambda \alpha + \mu \beta)$ and $R(xy, \alpha \beta)$ for every $\lambda, \mu \in K$ and also $R(1, 1)$.

The homomorphic relation $R \subseteq \mathfrak{N} \times \mathfrak{L}$ has *domain* $\mathfrak{N}$ if for all $x \in \mathfrak{N}$ there is an $\alpha \in \mathfrak{L}$ such that $R(x, \alpha)$. The relation $R$ is *non-trivial* if not $R(1, 0)$.

If $\varphi : \mathfrak{N} \to \mathfrak{L}$ is a homomorphism then the graph of $\varphi$, i.e., the relation $R(x, \alpha)$ defined by $\varphi(x) = \alpha$, is a non-trivial homomorphic relation with domain $\mathfrak{N}$. Similarly a homomorphism $\psi : \mathfrak{L} \to \mathfrak{N}$ of $\mathfrak{L}$ onto $\mathfrak{N}$ defines the non-trivial homomorphic relation $R$ with domain $\mathfrak{N}$ by taking $R(x, \alpha)$ if $\psi(\alpha) = x$.

**Theorem. 2.** Let $\mathfrak{N}$ be a partial algebra and assume that there exists a non-trivial homomorphic relation $R$ with domain $\mathfrak{N}$ between $\mathfrak{N}$ and a commutative algebra $C$. Then there exists a commutative algebra $C'$ and a homomorphism $h : \mathfrak{N} \to C'$ from $\mathfrak{N}$ onto $C'$.

**Proof.** Let $S$ be the set of all elements $\alpha$ in $C$ such that $R(x, \alpha)$ for some $x \in \mathfrak{N}$. Let $\tilde{S}$ be the subalgebra generated by $S$ in $C$. Define $I$ to be the set of all $\alpha \in C$ such that $R(0, \alpha)$. Then $I$ is clearly closed under linear combinations. Next

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

75

let $\beta \in \bar{S}$, so that

$$\beta = \sum_i \lambda_i \beta_{i1} \beta_{i2} \cdots \beta_{in_i}$$

for some $\lambda_i \in K$, and $\beta_{ij} \in S$.

If $\alpha \in I$, then $\alpha \beta_{ij} \in I$. Hence $\alpha \beta = \Sigma_i \lambda_i \alpha \beta_{i1} \cdots \beta_{in_i} \in I$. Finally, $1 \notin I$. We have shown that $I$ is a proper ideal of the algebra $\bar{S}$. Let $C' = \bar{S}/I$ and let $\varphi : \bar{S} \to C'$ be the canonical homomorphism. Define $h : \mathfrak{N} \to C'$ by $h(x) = \varphi(\alpha)$ where $\alpha \in S$ is such that $R(x, \alpha)$. Then it is easily checked that $h$ is well-defined and a homomorphism.

If we now take $\mathfrak{N}$ to be the partial algebra $Q$, it follows from this theorem that there is no non-trivial homomorphic relation with domain $Q$ between $Q$ and a commutative algebra.

**6. A classical model of electron spin.** We prove here that the problem of hidden variables as we have formulated it in Section 1 has a positive solution for a restricted part of quantum mechanics. The portion of quantum mechanics with which we deal is obtained by restricting our Hilbert space to be two-dimensional. Thus, the state vectors are assumed to range over two-dimensional unitary space $U^2$, and the observables to range over the set $H_2$ of two-dimensional self-adjoint operators.

As will be seen, the problem reduces to considering the case of spin operators. Thus, our problem becomes essentially that of constructing a classical model for a single particle of spin $\frac{1}{2}$, say an electron. Needless to say, we do not maintain that this classical model of electron spin remains valid in the general context of quantum mechanics. In fact, as was shown in Section 4, there exists a system of two electrons in a suitable external field such that there is no classical model for the spin of the system.

Our aim in constructing a classical model for electron spin is two-fold. In the first place, we wish to exhibit a classical interpretation of a part of quantum mechanics so that it may be compared with various attempts to introduce hidden variables into quantum mechanics. We believe these attempts to be unsuccessful, so it would be as well if we could give an example of what is for us a successful introduction of hidden variables into a theory. In the second place, we shall use this model in discussing von Neumann's proof in [19] of the non-existence of hidden variables.

As formulated in Section 1, our problem is to define a "phase" space $\Omega$ such that for each operator $A \in H_2$ there is a real-valued function $f_A : \Omega \to \mathbb{R}$ and for each vector $\psi \in U^2$ there exists a probability measure $\mu_\psi$ on $\Omega$ such that

(I) $f_{u(A)} = u(f_A)$ for each (Borel) function $u$; and

(II) the quantum mechanical expectation

$$\langle A \psi, \psi \rangle = \int_\Omega f_A(\omega) \, d\mu_\psi(\omega).$$

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

76

S. KOCHEN & E. P. SPECKER

Let $V$ be the set of operators in $H_2$ of trace zero. $V$ forms a 3-dimensional vector space over $\mathbf{R}$. This is easily seen by noting that the Pauli spin matrices

$$\sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad \sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad \sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$

form an orthonormal basis for $V$. If we assign to $(\sigma_x, \sigma_y, \sigma_z)$ an orthonormal basis $(i, j, k)$ in 3-dimensional Euclidean space $E^3$, we obtain a vector isomorphism $P: V \to E^3$. To every spin matrix $\sigma$, i.e., a matrix $\sigma$ in $V$ with eigenvalues $\pm 1$, there corresponds under the map $P$ a point $P_\sigma$ on the unit sphere $S^2$ in $E^3$. Physically, one speaks of the spin matrix $\sigma$ as corresponding to the observable “the spin angular momentum of the electron (say) in the direction $0P_\sigma$,” where $0$ is the origin in $E^3$.

Now let $A$ be any matrix in $H_2$ with distinct eigenvalues $\lambda_1, \lambda_2$. We let

$$\sigma(A) = \left( \frac{2}{\lambda_1 - \lambda_2} \right) A - \left( \frac{\lambda_1 + \lambda_2}{\lambda_1 - \lambda_2} \right) I.$$

Then $\sigma(A)$ is a spin matrix such that the eigenvectors of $\sigma(A)$ corresponding to $+1$ and $-1$ are the same as the eigenvectors of $A$ corresponding to $\lambda_1$ and $\lambda_2$ respectively.

We are now ready to choose the appropriate space $\Omega$ and functions $f_A$. For $\Omega$ we choose $S^2$. If $A \in H_2$ with distinct eigenvalues $\lambda_1$ and $\lambda_2$, we let

$$f_A(p) = \begin{cases} \lambda_1 & \text{for } p \in S^*_{P_\sigma(A)} \\ \lambda_2 & \text{otherwise.} \end{cases}$$

Here $S^*_{P_\sigma(A)}$ denotes the upper hemisphere of $S^2$ with the North Pole at $P_{\sigma(A)}$. If the eigenvalues of $A$ are equal, so that $A = \lambda I$, say, then we let

$$f_A(p) = \lambda, \quad \text{for all} \quad p \in S^2.$$

With this definition, it is a simple matter to check that the condition (I): $f_{u(A)} = u(f_A)$ holds. We need only note that for 2-dimensional operators it is sufficient to consider linear functions: $u(A) = \alpha A + \beta I$, with $\alpha, \beta \in \mathbf{R}$. Then condition (I) follows immediately from the fact that $\sigma_{\alpha A + \beta I} = \sigma_A$.

Next we wish to assign a probability measure $\mu_\psi$ to each vector $\psi \in U^2$. Let $\sigma_\psi$ denote the spin matrix for which $\psi$ is the eigenvector belonging to the eigenvalue $+1$. We may thus assign to each $\psi \in U^2$ a point $P_{\sigma_\psi}$ of $S^2$. We shall write $P_\psi$ for $P_{\sigma_\psi}$. Physically, if $\psi$ is the state vector of an electron, then the electron is said to have “spin in the direction $0P_\psi$.”

To delimit the problem and at the same time to obtain a solution with natural isotropy properties, we shall assume that the probability measures $\mu_\psi$ satisfy the following conditions:

(a) For each $\psi \in U^2$, the measure $\mu_\psi$ arises from a continuous probability density $u_\psi(p)$ on $S^2$, so that

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

77

$$\mu_\phi(E) = \int_E u_\phi(p) \, dp$$

for every measurable subset $E$ of $S^2$.

(b) The probability density $u_\phi(p)$ is a function only of the angle $\theta$ subtended at 0 by the points $p$ and $P_\phi$ on $S^2$. We may thus write $u_\phi(\theta)$ for the function $u_\phi(p)$.

(c) Let $u(\theta) (= u_{\phi_*}(\theta))$ be the probability density assigned to the state vector

$$\psi_0 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.$$

(Note that $\sigma_{\psi_*} = \sigma_\infty$, so that $P_{\psi_*} = (0, 0, 1)$.) Let $\psi \in U^2$. If $\alpha$ is the polar angle of the point $P_\phi$ on $S^2$, then we assume that $u_\phi(\theta) = u(\theta + \alpha)$. Thus, the probability takes the same functional form for all states $\psi$.

(d) We assume that $u(\theta) = 0$ for $\theta > \pi/2$.

An examination of the problem shows that these are natural properties to assign to the quantum states considered as probability distributions over the hidden states. We shall show that there do exist measures $\mu_\phi$ satisfying the above conditions as well as condition (II). In fact, we shall see that these conditions determine the density functions $u_\phi$ uniquely.

Using these assumptions we may simplify the problem of finding measures $\mu_\phi$ which satisfy condition (II) as follows. Since $f_A$ is a linear function of $A$, the integral $\int_\Omega f_A(\omega) \, d\mu_\phi(\omega)$ is a linear function of $A$. On the other hand the expectation function $\langle A\psi, \psi \rangle$ is also a linear function of $A$. Since every matrix $A$ in $H_2$ is a linear function of a projection matrix, it is sufficient to verify condition (II) for projection matrices. Next, by condition (c) we may assume that

$$\psi = \begin{pmatrix} 1 \\ 0 \end{pmatrix},$$

so that $P_\phi = (0, 0, 1)$. Furthermore, by condition (b), it is sufficient to consider the case where $P_{\sigma(A)}$ has azimuthal angle equal to zero. In what follows we shall make the above assumptions on $A$ and $\psi$.

It is now necessary to express the expectation $\langle A\psi, \psi \rangle$ as a function of the angle subtended at 0 by the points $P_\phi = (0, 0, 1)$ and $P_{\sigma(A)}$, i.e., as a function of the polar angle $\rho$ of $P_{\sigma(A)}$.

In spherical polar coordinates we may write

$$P_{\sigma(A)} = (\sin \rho, 0, \cos \rho).$$

Hence,

$$\begin{aligned} \sigma(A) &= \sigma_\infty \sin \rho + \sigma_\infty \cos \rho \\ &= \begin{pmatrix} \cos \rho & \sin \rho \\ \sin \rho & -\cos \rho \end{pmatrix}. \end{aligned}$$

The eigenvector $\eta$ of $\sigma(A)$ belonging to the eigenvalue $+1$ is

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

78

S. KOCHEN & E. P. SPECKER

$$\eta = \begin{bmatrix} \cos (\rho/2) \\ \sin (\rho/2) \end{bmatrix}.$$

Since $A$ was assumed to be a projection matrix, $\eta$ is also the eigenvector of $A$ belonging to the eigenvalue $+1$. Thus,

$$\begin{aligned} \langle A\psi, \psi \rangle &= \langle\langle\psi, \eta\rangle\eta, \psi\rangle \\ &= |\langle\psi, \eta\rangle|^2 \\ &= \cos^2 (\rho/2). \end{aligned}$$

Our problem is thus reduced to solving for $u(\theta)$ the integral equation

$$\cos^2 (\rho/2) = \int_{S^*} f_A(p)u(\theta) \, dp.$$

Since

$$f_A(p) = \begin{cases} 1 & \text{on } S_{P_{\epsilon(A)}}^+ \\ 0 & \text{otherwise} \end{cases}$$

this equation becomes

$$\cos^2 (\rho/2) = \int_T u(\theta) \, dp$$

where $T = S_{P_{\epsilon(A)}}^+ \cap S_{P_\theta}^+$. Thus,

$$\cos^2 (\rho/2) = \int_{\rho-\pi/2}^{\pi/2} \int_{-\varphi_\theta}^{\varphi_\theta} u(\theta) \sin \theta \, d\varphi \, d\theta$$

where $\varphi_\theta$ is the azimuthal angle of the point $Q = (\sin \theta \cos \varphi_\theta, \sin \theta \sin \varphi_\theta, \cos \theta)$ with polar angle $\theta$ which lies on the great circle $C$ perpendicular to the point $P_{\epsilon(A)} = (\sin \rho, 0, \cos \rho)$.

![img-3.jpeg](img-3.jpeg)

This content downloaded from 140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

79

Using the orthogonality of $Q$ and $P_{\sigma(A)}$, we have

$$\sin \rho \sin \theta \cos \varphi_\theta + \cos \rho \cos \theta = 0$$

or

$$\varphi_\theta = \cos^{-1} (-\cot \rho \cot \theta).$$

Thus

$$\frac{1}{2}(1 + \cos \rho) = 2 \int_{\rho - \pi/2}^{\pi/2} u(\theta) \sin \theta \cos^{-1} (-\cot \rho \cot \theta) \, d\theta.$$

Letting $x = \rho - \pi/2$, we have

$$\frac{1}{2}(1 - \sin x) = -2 \int_{\pi/2}^{x} u(\theta) \sin \theta \cos^{-1} (\cot \theta \tan x) \, d\theta.$$

Now, differentiating both sides with respect to $x$, we obtain

$$-\frac{1}{2} \cos x = -2u(x) \sin x \cos^{-1} (\cot x \tan x) + \int_{\pi/2}^{x} \frac{u(\theta) \sin \theta \cot \theta \sec^2 x}{(1 - \cot^2 \theta \tan^2 x)^{1/2}} \, d\theta$$

or,

$$\cos^2 x = -4 \int_{\pi/2}^{x} \frac{u(\theta) \cos \theta}{(1 - \cot^2 \theta \tan^2 x)^{1/2}} \, d\theta.$$

If we set $z = \cos^2 x$, $s = \cos^2 \theta$, and $w(s) = u(\theta)$, we find

$$z = \int_0^s \frac{2w(s)}{(s - s)^{1/2}} \, ds.$$

This is a special case of Abel's integral equation, and is easily solved by Laplace transforms. Namely, if $*$ denotes convolution and $L(f) = \int_0^\infty f(x)e^{-tx} \, dx$, the Laplace transform, then

$$z = w * 2z^{-1/2}.$$

Hence,

$$L(z) = L(w)L(2z^{-1/2}),$$

or

$$\begin{aligned} L(w) &= L(z)/L(2z^{-1/2}) \\ &= \frac{1}{2\sqrt{\pi}} t^{-3/2} \\ &= L((1/\pi)s^{1/2}), \end{aligned}$$

so that

$$w(s) = (1/\pi)s^{1/2}.$$

This content downloaded from 140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC All use subject to https://about.jstor.org/terms

80

S. KOCHEN & E. P. SPECKER

We thus have shown that

$$u(\theta) = \begin{cases} (1/\pi) \cos \theta & \text{if } 0 \leq \theta \leq \pi/2 \\ 0 & \text{otherwise.} \end{cases}$$

On the basis of this mathematical solution, we may construct a simple classical model of electron spin. The same model then serves (by linearity) for the more general case of operators in $H_2$.

We start with a sphere with fixed center 0. A point $P$ on the sphere represents the quantum state "spin in the direction $0P$". If the sphere is in such a quantum state it is at the same time in a hidden state which is represented by another point $T \in S_P^*$. The point $T$ has been determined as follows. A disk $D$ of the same radius as the sphere is placed perpendicular to the $0P$ axis with center directly above $P$. A particle is placed on the disk and the disk shaken "randomly". That is the disk is so shaken that the probability of the particle being in a region $U$ in $D$ is proportional to the area of $U$ (i.e., the probability is uniformly distributed). The point $T$ is the orthogonal projection of the particle (after shaking) onto the sphere. It is easily seen that the probability density function for the projection is given by

$$u(T) = \begin{cases} (1/\pi) \cos \theta & 0 \leq \theta \leq \pi/2 \\ 0 & \text{otherwise,} \end{cases}$$

where $\theta$ is the angle subtended by $T$ and $P$ at 0.

Suppose we now wish to measure the spin angular momentum in a direction $0Q$. This is determined as follows. If $T \in S_Q^*$, then the spin angular momentum is $+\hbar/2$, if $T \notin S_Q^*$ then the spin is $-\hbar/2$. The sphere is now in the new quantum state of spin in the direction $0Q$ if $T \in S_Q^*$ or spin in the direction $0Q^*$ (where $Q^*$ is the antipodal point of $Q$) if $T \notin S_Q^*$. The new hidden state of the sphere is now determined as before, by shaking the particle on the disk $D$, the disk being placed with center above $Q$ if $T \in S_Q^*$ or with center above $Q^*$ if $T \notin S_Q^*$.

It should be clear from the preceding analysis that the probabilities and expectations that arise from this model are precisely the same as those arising from quantum mechanical calculations for free electron spin. In the model the disk $D$, the particle, and its projection are to be considered as the hidden apparatus. The probabilities arise through the ignorance of the observer of the sphere of the actual location of the particle on the disk. To an observer of the complete system of sphere and disk the model is a deterministic classical system.

Note that in the above model we could keep the disk fixed vertically above the sphere and instead rotate the sphere to determine each new hidden state. If we now further replace the shaking disk by a random vertically falling water drop, we may say that rain falling on a ball forms a classical model of electron spin.

We remark finally that the conditions (I) and (II) say nothing about the propagation of the probabilities in time. That is to say, although these conditions

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

81

give the probabilities arising at each experiment, they do not deal with the change of probabilities during the time between experiments. However, in the situation we are examining of free electron spin this causes no difficulty since every state is in this case stationary, and the probabilities remain constant in the time between experiments.

We now consider the bearing of this model on von Neumann's discussion of the hidden variables problem given in [19, Chapter IV]. In that chapter von Neumann gives what he considers to be a necessary condition for the existence of hidden variables for quantum mechanics. This condition is the existence of a function

$$\mathcal{E}: H \rightarrow \mathbb{R},$$

where $H$ is the set of self-adjoint operators, such that

- (1) $\mathcal{E}(I) = 1$.
- (2) $\mathcal{E}(aA) = a\mathcal{E}(A)$, for all $a \in \mathbb{R}$, $A \in H$.
- (3) $\mathcal{E}(A^2) = \mathcal{E}^2(A)$, for all $A \in H$.
- (4) $\mathcal{E}(A + B) = \mathcal{E}(A) + \mathcal{E}(B)$, for all $A, B \in H$.

In [19] it is then shown that there does not exist a function satisfying these conditions. (In [19] a further condition is added on $\mathcal{E}$: (5) If $A$ is "essentially positive" then $\mathcal{E}(A) \geq 0$. But we shall not require this condition in our proof.) We present another proof below. This is done for two reasons. First, our proof is simpler, and is in fact trivial. Second, this proof shows that there is even no function $\mathcal{E}: H_2 \rightarrow \mathbb{R}$ satisfying conditions (1)-(4), a result we require for our later discussion.

**Lemma.** *If the function $\mathcal{E}: H \rightarrow \mathbb{R}$ satisfies (1)-(3) together with condition*

$$(4)' \mathcal{E}(A + B) = \mathcal{E}(A) + \mathcal{E}(B), \text{ for all } A, B \in H \text{ such that } AB = BA,$$

*then $\mathcal{E}(AB) = \mathcal{E}(A)\mathcal{E}(B)$, for all $A, B \in H$ such that $AB = BA$. (In the terminology of Section 2, $\mathcal{E}$ is thus a homomorphism of the partial algebra $H$ into $\mathbb{R}$.)*

**Proof.** Assume $AB = BA$. Then

$$\begin{aligned} \mathcal{E}^2(A) + 2\mathcal{E}(A)\mathcal{E}(B) + \mathcal{E}^2(B) &= (\mathcal{E}(A) + \mathcal{E}(B))^2 \\ &= \mathcal{E}^2(A + B) \\ &= \mathcal{E}((A + B)^2) \\ &= \mathcal{E}(A^2 + 2AB + B^2) \\ &= \mathcal{E}(A^2) + \mathcal{E}(2AB) + \mathcal{E}(B^2) \\ &= \mathcal{E}^2(A) + 2\mathcal{E}(AB) + \mathcal{E}^2(B). \end{aligned}$$

Hence, $\mathcal{E}(A)\mathcal{E}(B) = \mathcal{E}(AB)$.

**Corollary.** *If the function $\mathcal{E}$ satisfies conditions (1), (2), (3), (4)', then $\mathcal{E}(A)$ lies in the spectrum of $A$.*

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

82

S. KOCHEN & E. P. SPECKER

Proof. Suppose to the contrary that $A - \varepsilon(A)$ has an inverse $B$. Then by the Lemma,

$$\begin{aligned} 1 &= \varepsilon(I) \\ &= \varepsilon((A - \varepsilon(A))B) \\ &= \varepsilon(A - \varepsilon(A))\varepsilon(B) \\ &= (\varepsilon(A) - \varepsilon(\varepsilon(A)))\varepsilon(B) \\ &= (\varepsilon(A) - \varepsilon(A))\varepsilon(B) \\ &= 0. \end{aligned}$$

Theorem. 3. There is no function $\varepsilon: H \to \mathbb{R}$ satisfying conditions (1)-(4).

Proof. Consider the two matrices

$$A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad B = \frac{1}{2} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}.$$

The matrices $A$ and $B$ are projection matrices and hence have eigenvalues 0 and 1. The matrix $A + B$ has eigenvalues $1 \pm \frac{1}{2}(2)^{1/2}$. Hence, $\varepsilon(A + B) \neq \varepsilon(A) + \varepsilon(B)$, by the above corollary.

As the proof shows, there is no function $\varepsilon$ with properties (1)-(4) even when the domain of $\varepsilon$ is restricted to $H_2$.

Now, von Neumann's criterion has been criticized in the literature in requiring the additivity of $\varepsilon$ even for non-commuting operators, i.e., in requiring condition (4) rather than (4)'. (See for example Hermann [9, pp. 99-104].) As the above Lemma shows, it is precisely on this point that von Neumann's criterion differs from our point of view. For we showed that there does not exist a function satisfying (1), (2), (3), and (4)'. We may now go further. We have here constructed a classical system $C$ (the sphere and the disk). From this system we obtained a new system $Q$ (the sphere without the disk) such that the pure states of $Q$ are certain mixed states of $C$ and the observables of $Q$ are among the observables of $C$. The pure states of $Q$ may then be described by vectors in $U^2$ and the observables of $Q$ by operators in $H_2$, just as in quantum mechanics. If we now accept von Neumann's criterion, we must conclude that we cannot introduce hidden variables into the system $Q$. But this can hardly be a reasonable conclusion, since we may reintroduce into $Q$ the states and observables of $C$ which we ignored in forming $Q$, to recover the classical system $C$.

7. The logic of quantum mechanics. In this section we discuss the non-existence of an imbedding of $\mathfrak{B}$ into a Boolean algebra from a different point of view. It will turn out that a consequence of this result is that the logic of quantum mechanics is different from classical logic. Since the set of propositions of a classical physical theory forms a Boolean algebra $B$ it follows that the

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

83

propositions valid in such a theory are precisely the classical tautologies. This means that if we are given a classical tautology such as

$$(9) \quad x_1 \wedge (x_2 \wedge x_3) \equiv (x_1 \wedge x_2) \wedge x_3$$

then every substitution of elements of $B$ for $x_1, x_2, x_3$ yields the element 1 of $B$. In the case of a theory such as quantum mechanics where the set of propositions form a partial Boolean algebra $\mathfrak{B}$ it is not clear what it means for a proposition to be valid. To take the preceding proposition (9) as an example, it is not possible to substitute arbitrary elements of $a_1, a_2, a_3$ of $\mathfrak{B}$ for $x_1, x_2, x_3$. It is necessary in this case that the commasurability relations $a_2 \upharpoonright a_3, a_1 \upharpoonright a_2, a_1 \upharpoonright a_3 \wedge a_3, a_1 \wedge a_2 \upharpoonright a_3$, and $a_1 \wedge (a_2 \wedge a_3) \upharpoonright (a_1 \wedge a_2) \wedge a_3$ be satisfied, to allow an application of the partial operations in $\mathfrak{B}$. A proposition is then valid in $\mathfrak{B}$ if every such "meaningful" substitution of elements yields the element 1 of $\mathfrak{B}$.

A Boolean function $\varphi(x_1, \dots, x_n)$ such as (9) may be considered as a polynomial over $Z_2$. We shall now give a formal definition for a polynomial $\varphi(x_1, \dots, x_n)$ over a field $K$ to be identically 1 in a partial algebra $\mathfrak{N}$ over $K$. We first recursively define the domain $D_\varphi$ of $\varphi(x_1, \dots, x_n)$ in $\mathfrak{N}$. We simultaneously define a map $\varphi^*$ corresponding to $\varphi(x_1, \dots, x_n)$. $D_\varphi$ is a subset of the $n$-fold Cartesian product $\mathfrak{N}^n$ of $\mathfrak{N}$ and $\varphi^*$ is a map from $D_\varphi$ into $\mathfrak{N}$. Let $a = \langle a_1, \dots, a_n \rangle$ be an arbitrary element of $\mathfrak{N}^n$.

1. If $\varphi$ is the polynomial 1, then $D_\varphi = \mathfrak{N}^n$ and $\varphi^*(a) = 1$.
2. If $\varphi$ is the polynomial $x_i$ ($i = 1, 2, \dots, n$), then $D_\varphi = \mathfrak{N}^n$ and $\varphi^*(a) = a_i$.
3. If $\varphi = k\psi$ with $k \in K$, then $D_\varphi = D_\psi$ and $\varphi^*(a) = k\psi^*(a)$.
4. If $\varphi = \psi \otimes \chi$ (where $\otimes$ is either $+$ or $\cdot$), then $a \in D_\varphi$ if and only if $a \in D_\psi \cap D_\chi$ and $\psi^*(a) \upharpoonright \chi^*(a)$; $\varphi^*(a) = \psi^*(a) \otimes \chi^*(a)$.

We say that the identity $\varphi(x_1, \dots, x_n) = 1$ holds in $\mathfrak{N}$ if $\varphi^*(a) = 1$ for all $a \in D_\varphi$. More generally, if $\varphi(x_1, \dots, x_n)$ and $\psi(x_1, \dots, x_n)$ are two polynomials over $K$, we shall say that the identity $\varphi(x_1, \dots, x_n) = \psi(x_1, \dots, x_n)$ holds in $\mathfrak{N}$ if $\varphi^*(a) = \psi^*(a)$ for all $a \in D_\varphi \cap D_\psi$.

Let $\varphi(x_1, \dots, x_n)$ be a propositional (i.e., a Boolean) function. Then $\varphi(x_1, \dots, x_n)$ may be considered as a polynomial over $Z_2$. Let $\mathfrak{N}$ be a partial Boolean algebra. Then $\varphi$ is valid in $\mathfrak{N}$ if the identity $\varphi = 1$ holds in $\mathfrak{N}$. If for some $a \in D_\varphi$ we have $\varphi^*(a) = 0$, then $\varphi$ is refutable in $\mathfrak{N}$. If $\varphi$ and $\psi$ are two propositional functions, then $\varphi = \psi$ is valid in $\mathfrak{N}$ if the identity $\varphi = \psi$ holds in $\mathfrak{N}$. We illustrate these definitions with an example. We shall show that the tautology (9) is valid in every partial Boolean algebra $\mathfrak{N}$. In fact, we show that the identity $x_1 \wedge (x_2 \wedge x_3) = (x_1 \wedge x_2) \wedge x_3$ is valid in $\mathfrak{N}$; this means that we do not require that $a_1 \wedge (a_2 \wedge a_3) \upharpoonright (a_1 \wedge a_2) \wedge a_3$. To see this note that if $a_2 \upharpoonright a_3, a_1 \upharpoonright a_2, a_1 \upharpoonright a_3 \wedge a_3, a_1 \wedge a_2 \upharpoonright a_3$ then

$$\begin{aligned} a_1 \wedge (a_2 \wedge a_3) &= a_1 \wedge (a_2 \wedge (a_3 \wedge a_3)) \\ &= (a_1 \wedge a_2) \wedge (a_2 \wedge a_3). \end{aligned}$$

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

84

S. KOCHEN & E. P. SPECKER

The last equality holds because the elements $a_1, a_2$ and $a_2 \wedge a_3$ are pairwise commasurable and hence by the definition of a partial algebra generate a Boolean algebra in $\mathfrak{N}$. Similarly, $(a_1 \wedge a_2) \wedge a_3 = (a_1 \wedge a_2) \wedge (a_2 \wedge a_3)$, proving the result.

In the case of quantum mechanics these considerations are more than theoretical possibilities, they occur in ordinary reasoning about physical systems. For instance, the orbital angular momentum $\bar{L}$ of an atom is commasurable with the spin angular momentum $\bar{S}$. If the system has spherical symmetry then a component of $\bar{L} + \bar{S}$ (= total angular momentum $\bar{J}$) is commasurable with the Hamiltonian $H$, although components of $\bar{L}$ and $\bar{S}$ are separately not commasurable with $H$. Thus a statement specifying $H$ and a component of $\bar{L} + \bar{S}$ is of the type considered here.

If $\mathfrak{N}$ is a Boolean algebra this definition of validity coincides with the usual definition. In that case the set of valid propositional functions coincides with the classical tautologies, *i.e.*, those propositional functions which are valid in $Z_2$. In the following theorem we connect the validity of classical tautologies in a partial Boolean algebra $\mathfrak{N}$ with the imbeddability of $\mathfrak{N}$ into a Boolean algebra.

For the sake of obtaining a complete correspondence in this theorem we introduce the following weakening of the notion of imbedding.

**Definition.** Let $\mathfrak{N}, \mathfrak{L}$ be partial Boolean algebras. A homomorphism $\varphi : \mathfrak{N} \to \mathfrak{L}$ is a *weak imbedding* of $\mathfrak{N}$ into $\mathfrak{L}$ if $\varphi(a) \neq \varphi(b)$ whenever $a \not\supset b$ and $a \neq b$ in $\mathfrak{N}$. Thus a weak imbedding is a homomorphism which is an imbedding on Boolean subalgebras of $\mathfrak{N}$.

The counterpart of Theorem 0 of Section 2 is that $\mathfrak{N}$ is weakly imbeddable in a Boolean algebra if and only if for every non-zero element $a$ in $\mathfrak{N}$ there is a homomorphism $h : \mathfrak{N} \to Z_2$ such that $h(a) \neq 0$.

**Theorem 4.** Let $\mathfrak{N}$ be a partial Boolean algebra.

1. $\mathfrak{N}$ is imbeddable into a Boolean algebra if and only if, for every classical tautology of the form $\varphi \equiv \psi, \varphi = \psi$ is valid in $\mathfrak{N}$.
2. $\mathfrak{N}$ is weakly imbeddable into a Boolean algebra if and only if every classical tautology $\varphi$ is valid in $\mathfrak{N}$.
3. $\mathfrak{N}$ may be mapped homomorphically into a Boolean algebra if and only if every classical tautology $\varphi$ is not refutable in $\mathfrak{N}$.

**Proof.** The necessity of the condition in each case is clear. We shall give a uniform proof of sufficiency for the three cases where $\mathfrak{N}$ satisfies the condition that $\mathfrak{N}$ is (1) imbeddable, (2) weakly imbeddable or (3) mapped homomorphically into a Boolean algebra. Let

$$s_i(x) = \begin{cases} x & i = 1, 2 \\ 1 & i = 3, \end{cases} \quad t_i(y) = \begin{cases} y & i = 1 \\ 0 & i = 2, 3. \end{cases}$$

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

85

Let $K_1$ be the set of all equations of the form $\alpha + \beta = \gamma$ or $\xi\eta = \zeta$ which subsist among elements of $\mathfrak{N}$. (In the language of model theory, $K_1$ denotes the positive statements from the diagram of $\mathfrak{N}$.) Let $K_2$ be the elementary axioms describing the class of Boolean algebras. Write $K = K_1 \cup K_2$. Then the class of all models of $K$ consist precisely of the homomorphic images of $\mathfrak{N}$ which are Boolean algebras.

Suppose now that $\mathfrak{N}$ does not satisfy condition (i) ($i = 1, 2, \text{or } 3$). Then by Theorem 0 and its counterpart for weak imbeddings there exist two distinct elements $a, b$ in $\mathfrak{N}$ such that for every Boolean algebra $B$ and every homomorphism $h : \mathfrak{N} \to B$ we have $h(s_i(a)) = h(t_i(b))$. Since then $s_i(a)$ and $t_i(b)$ are identified in every model of $K$, we have by the Completeness Theorem for the Predicate Calculus that

$$K \vdash s_i(a) = t_i(b).$$

Hence, there is a finite subset

$$L = \{\alpha_j + \beta_j = \gamma_j, \xi_k\eta_k = \zeta_k \mid 1 \leq j \leq n, 1 \leq k \leq m\}$$

of $K_1$ such that

$$K_2 \cup L \vdash s_i(a) = t_i(b)$$

so that

$$K_2 \vdash (\bigwedge_i (\alpha_j + \beta_j + \gamma_j = 0) \wedge \bigwedge_k (\xi_k\eta_k + \zeta_k = 0)) \to s_i(a) = t_i(b)$$

or

$$K_2 \vdash (\bigvee_{j,k} (\alpha_j + \beta_j + \gamma_j)(\xi_k\eta_k + \zeta_k) = 0) \to s_i(a) = t_i(b),$$

i.e., $K_2 \vdash \rho(\alpha_1, \cdots, \zeta_m) = 0 \to s_i(a) = t_i(b)$ where

$$\rho(\alpha_1, \cdots, \zeta_m) = \bigvee_{j,k} (\alpha_j + \beta_j + \gamma_j)(\xi_k\eta_k + \zeta_k).$$

Since the constants $\alpha_1, \cdots, \zeta_m, a, b$ do not occur in $K_2$, we may replace them by variables $x_1, \cdots, x_n, x, y$ to obtain

$$(10) \quad K_2 \vdash \rho(x_1, \cdots, x_n) = 0 \to s_i(x) = t_i(y).$$

Hence, the implication $\rho(x_1, \cdots, x_n) = 0 \to s_i(x) = t_i(y)$ is valid in all Boolean algebras. Let

$$\varphi \text{ denote } s_i(x) \to \rho$$

and

$$\psi \text{ denote } t_i(y) \to \rho.$$

Then it follows from (10) that $\varphi = \psi$ is Boolean identity, i.e., $\varphi \equiv \psi$ is a classical tautology. (Note that for $i = 2, 3, \psi = 1$ so that $\varphi \equiv \psi$ reduces to $\varphi$.) On the other hand the substitution of the elements $\alpha_1, \cdots, \zeta_m, s_i(a), t_i(b)$ from $\mathfrak{N}$

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

86

S. KOCHEN & E. P. SPECKER

for the variables $x_1, \dots, x_n, s_i(x), t_i(y)$ yields a value 0 for $\rho$, and hence a value $s_i(a)'$ for $\varphi$ and $t_i(b)'$ for $\psi$. (Here $u'$ denotes $1 - u$.) Hence, under this valuation of $\varphi$ and $\psi$ in $\mathfrak{A}$, we have

$$\begin{aligned} \varphi &= a', \quad \psi = b', \quad \text{so that} \quad \varphi \neq \psi, \quad \text{for} \quad i = 1 \\ \varphi &= a', \quad \text{so that} \quad \varphi \neq 1, \quad \text{for} \quad i = 2 \\ \varphi &= 0, \quad \text{for} \quad i = 3, \end{aligned}$$

proving the theorem.

Since in the case of quantum mechanics there is, by Theorem 1, no homomorphism of $D$ onto $Z_2$, we obtain the following consequence of Theorem 4.

**Corollary.** *There is a propositional formula $\varphi$ which is a classical tautology but which is false under a (meaningful) substitution of quantum mechanical propositions for the propositional variables of $\varphi$.*

It is in fact not difficult to construct such a formula. Assign to each one-dimensional linear subspace $L_i$ of $D$ a distinct propositional variable $x_i$. To each orthogonal triple $L_1, L_2, L_3$ of $D$ assign the Boolean function

$$x_i + x_j + x_k + x_i x_j x_k.$$

Note that classically this formula is valid if and only if exactly one of $x_i, x_j, x_k$ is valid. Hence the formula

$$\varphi = 1 - \prod (x_i + x_j + x_k + x_i x_j x_k),$$

where the product extends over all orthogonal triples of $D$, is classically valid, by Theorem 1. On the other hand, the substitution of the quantum mechanical statement $P_i$ of Section 4 for each $x_i$ makes $\varphi$ false since each factor of the product takes the value 1. Thus, the formula $\varphi$ is the formal counterpart of the argument given at the end of Section 4. Actually, the formula $\varphi$ is uneconomical in the number of variables used. A more judicious choice of variables corresponding to the graph $\Gamma_2$ yields a formula in 86 variables which is classically valid and quantum mechanically refutable.

This way of viewing the results of Sections 3 and 4, seems to us to display a new feature of quantum mechanics in its departure from classical mechanics. It is of course true that the Uncertainty Principle, say, already marks a departure from classical physics. However, the statement of the Uncertainty Principle involves two observables which are not commasurable, and so may be refuted in the future with the addition of new states. This is the view of those who believe in hidden variables. Thus, the Uncertainty Principle as applied to the two-dimensional situation described in Section 6 becomes inapplicable once the system is imbedded in the classical one. The statement $\varphi(P_1, \dots, P_n)$ we have constructed deals only in each of the steps of its construction with commasurable observables, and so cannot be refuted at a later date.

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms

QUANTUM MECHANICS

87

# BIBLIOGRAPHY

[1] D. BOHM, Quantum theory in terms of "hidden" variables I, Phys. Rev., 85 (1952) 166-179.
[2] ———, A suggested interpretation of the quantum theory in terms of "hidden" variables II, Phys. Rev., 85 (1952) 180-193.
[3] F. BOPP, La méchanique quantique est-elle une méchanique statistique classique particulière?, Ann. L'Inst. H. Poincaré, 15 II(1956) 81-112.
[4] L. de Broglie, Non-linear wave mechanics, Elsevier, 1960.
[5] H. FREISTADT, The causal formulation of the quantum mechanics of particles, Nuovo Cimento Supp., Ser. 10, 5 (1957) 1-70.
[6] A. GLEASON, Measures on closed subspaces of Hilbert space, J. of Math. and Mech., 6 (1957) 885-893.
[7] J. H. E. GRIFFITH & J. OWEN, Paramagnetic resonance in the nickel Tutton salts, Proc. Royal Society of London, Ser. A, 213 (1952) 459-473.
[8] P. HALMOS, Lectures on Boolean Algebras, Van Nostrand Studies, 1963.
[9] G. HERMANN, Die naturphilosophischen Grundlagen der Quantenmechanik, Abhandlungen der Fries'schen Schule, 1935.
[10] S. KOCHEN & E. SPECKER, Logical structures arising in quantum theory, The Theory of Models, 1963 Symposium at Berkeley, pp. 177-189.
[11] ———, The calculus of partial propositional functions, Logic, Methodology and Philosophy of Science, 1964 Congress at Jerusalem, pp. 45-57.
[12] M. A. NEUMARK, Operatorenalgebren im Hilbertschen Raum in Sowjetische Arbeiten zur Funktional analysis, Verlag Kultur und Fortschritt, Berlin, 1954.
[13] M. H. L. PRYCE, A modified perturbation method for a problem in paramagnetism, Phys. Soc. Proc. A, 63 (1950) 25-29.
[14] L. SCHIFF, Quantum Mechanics, 2nd Ed., McGraw-Hill, 1955.
[15] J. SCHWARTZ, The Wiener-Siegel causal theory of quantum mechanics, in Integration of Functionals, New York University, 1957.
[16] A. SIEGEL & N. WIENER, The differential space of quantum theory, Phys. Rev. 101 (1956).
[17] E. SPECKER, Die Logik nicht gleichzeitig entscheidbarer Aussagen, Dialectica, 14 (1960) 239-246.
[18] K. W. H. STEVENS, The spin-Hamiltonian and line widths in Nickel Tutton salts, Proc. Roy. Soc. of London, Ser. A. 214 (1952) 237-244.
[19] J. VON NEUMANN, Mathematical foundations of quantum mechanics, P. V. P., 1955.

Cornell University

and

E. T. H., Zürich, Switzerland

Date Communicated: OCTOBER 31, 1966

This content downloaded from
140.0.246.18 on Thu, 30 Sep 2021 02:54:11 UTC
All use subject to https://about.jstor.org/terms
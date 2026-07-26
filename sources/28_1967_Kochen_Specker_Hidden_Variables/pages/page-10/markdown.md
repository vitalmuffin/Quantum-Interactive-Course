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
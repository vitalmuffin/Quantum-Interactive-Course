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
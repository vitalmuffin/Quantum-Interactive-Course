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
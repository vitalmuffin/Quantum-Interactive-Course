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
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
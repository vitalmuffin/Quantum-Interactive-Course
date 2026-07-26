to be the tensor product of $H_1$ and $H_2$ (written $H = H_1 \otimes H_2$). This has the consequence that if the sets $\{\xi_i^{S_1}\}$ and $\{\eta_j^{S_2}\}$ are complete orthonormal sets of states for $S_1$ and $S_2$, respectively, then the general state of $S$ can be written as a superposition:

$$\psi^S = \sum_{i,j} a_{ij} \xi_i^{S_1} \eta_j^{S_2}. \tag{1}$$

From (3.1) [sic] although $S$ is in a definite state $\psi^S$, the subsystems $S_1$ and $S_2$ do not possess anything like definite states independently of one another (except in the special case where all but one of the $a_{ij}$ are zero).

We can, however, for any choice of a state in one subsystem, uniquely assign a corresponding relative state in the other subsystems. For example, if we choose $\xi_k$ as the state for $S_1$, while the composite system $S$ is in the state $\psi^S$ given by (3.1) [sic], then the corresponding relative state in $S_2$, $\psi(S_2; \text{rel}\xi_k, S_1)$, will be:

$$\psi(S_2; \text{rel}\xi_k, S_1) = N_k \sum_j a_{kj} \eta_j^{S_2} \tag{2}$$

where $N_k$ is a normalization constant. This relative state for $\xi_k$ is independent of the choice of basis $\{\xi_i\}$ ($i \neq k$) for the orthogonal complement of $\xi_k$, and is hence determined uniquely by $\xi_k$ alone. To find the relative state in $S_2$ for an arbitrary state of $S_1$ therefore, one simply carries out the above procedure using any pair of bases for $S_1$ and $S_2$ which contains the desired state as one element of the basis for $S_1$. To find states in $S_1$ relative to states in $S_2$, interchange $S_1$ and $S_2$ in the procedure.

In the conventional or “external observation” formulation, the relative state in $S_2$, $\psi(S_2; \text{rel}\phi, S_1)$, for a state $\phi^{S_1}$ in $S_1$, gives the conditional probability distributions for the results of all measurements in $S_2$, given that $S_1$ has been measured and found to be in state $\phi^{S_1}$—i.e., that $\phi^{S_1}$ is the eigenfunction of the measurement in $S_1$ corresponding to the observed eigenvalue.

For any choice of basis in $S_1$, $\{\xi_i\}$, it is always possible to represent the state of $S$, (1), as a single superposition of pairs of states, each consisting of a state from the basis $\{\xi_i\}$ in $S_1$ and its relative state in $S_2$. Thus, from (2), (1) can be written in the form:

$$\psi^S = \sum_i \frac{1}{N_i} \xi_i^{S_1} \psi(S_2; \text{rel}\xi_i, S_1). \tag{3}$$

6
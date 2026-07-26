apply to a non-periodic physical phenomenon such as a collision. (The more definite method that will now be given shows that Born's assumption is not quite right, it being necessary to multiply the square of the amplitude by a certain factor.)

An alternative method of solving a collision problem is to find a *non-periodic* solution of the wave equation which consists initially simply of plane waves moving over the whole of space in the necessary direction with the necessary frequency to represent the incident electron. In course of time waves moving in other directions must appear in order that the wave equation may remain satisfied. The probability of the electron being scattered in any direction with any energy will then be determined by the rate of growth of the corresponding harmonic component of these waves. The way the mathematics is to be interpreted is by this method quite definite, being the same as that of the beginning of § 2.

We shall apply this method to the general problem of a system which makes transitions from one state to others of the same energy under the action of a perturbation. Let $H_0$ be the Hamiltonian of the unperturbed system and $V$ the perturbing energy, which must not involve the time explicitly. If we take the case of a continuous range of stationary states, specified by the first integrals, $\alpha_k$ say, of the unperturbed motion, then, following the method of § 2, we obtain

$$ih\dot{a}(\alpha') = \int V(\alpha'\alpha'')d\alpha'' \cdot a(\alpha''), \quad (21)$$

corresponding to equation (4). The probability of the system being in a state for which each $\alpha_k$ lies between $\alpha_{k'}$ and $\alpha'_k + d\alpha'_k$ at any time is $|a(\alpha')|^2 d\alpha'_1 \cdot d\alpha'_2 \dots$ when a $a(\alpha')$ is properly normalised and satisfies the proper initial conditions. If initially the system is in the state $\alpha^0$ we must take the initial value of $a(\alpha')$ to be of the form $a^0 \cdot \delta(\alpha' - \alpha^0)$. We shall keep $a^0$ arbitrary, as it would be inconvenient to normalise $a(\alpha')$ in the present case. For a first approximation we may substitute for $a(\alpha'')$ in the right-hand side of (21) its initial value. This gives

$$ih\dot{a}(\alpha') = a^0 V(\alpha'\alpha^0) = \alpha^0 v(\alpha'\alpha^0)e^{i[W(\alpha') - W(\alpha^0)]t/h},$$

where $v(\alpha'\alpha^0)$ is a constant and $W(\alpha')$ is the energy of the state $\alpha'$. Hence

$$iha(\alpha') = a^0 \delta(\alpha' - \alpha^0) + a^0 v(\alpha'\alpha^0)\frac{e^{i[W(\alpha') - W(\alpha^0)]t/h} - 1}{i[W(\alpha') - W(\alpha^0)]/h}. \quad (22)$$

16
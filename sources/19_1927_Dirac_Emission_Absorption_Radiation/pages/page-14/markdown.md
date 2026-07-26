system being taken into account. (The distinction between the perturbing system and the perturbed system is, of course, not real, but it will be kept up for convenience.)

We now consider a perturbing system, described, say, by the canonical variables $J_k, \omega_k$, the $J$'s being its first integrals when it is alone, interacting with an assembly of perturbed systems with no mutual interaction, that satisfy the Einstein-Bose statistics. The total Hamiltonian will be of the form

$$H_T = H_P(J) + \Sigma_n H(n),$$

where $H_P$ is the Hamiltonian of the perturbing system (a function of the $J$'s only) and $H(n)$ is equal to the proper energy $H_0(n)$ plus the perturbation energy $V(n)$ of the $n$th system of the assembly. $H(n)$ is a function only of the variables of the $n$th system of the assembly and of the $J$'s and $\omega$'s, and does not involve the time explicitly.

The Schrödinger equation corresponding to equation (14) is now

$$ih\dot{b}(J', r_1 r_2 \dots) = \Sigma_{J''} \Sigma_{s_1, s_2} \dots H_r(J', r_1 r_2 \dots; J'' s_1 s_2 \dots) b(J'', s_1 s_2 \dots),$$

in which the eigenfunction $b$ involves the additional variables $J'_k$. The matrix element $H_T(J', r_1 r_2 \dots; J', s_1 s_2 \dots)$ is now always a constant. As before, it vanishes when more than one $s_n$ differs from the corresponding $r_n$. When $s_m$ differs from $r_m$ and every other $s_n$ equals $r_n$, it reduces to $H(J' r_m; J'' s_m)$, which is the $(J', r_m; J'' s_m)$, matrix element (with the time factor removed) of $H = H_0 + V$, the proper energy plus the perturbation energy of a single system of the assembly; while when every $s_n$ equals $r_n$ it has the value $H_P(J') \delta_{J'J''} + \Sigma_n H(J' r_n; J'' r_n)$. If, as before, we restrict the eigenfunctions to be symmetrical in the variables $r_1, r_2 \dots$ we can again transform to the variables $N_1, N_2 \dots$, which will lead, as before, to the result

$$\begin{array}{c} ih\dot{b}(J', N'_1, N'_2 \dots) = H_P(J') b(J', N'_1, N'_2 \dots) + \Sigma_{J''} \Sigma_{r,s} N'^{1/2} \\ (N'_s + 1 - \delta_{rs})^{1/2} H(J' r; J'' s) b(J'', N'_1, N'_2 \dots N'_r - 1 \dots N'_s + 1 \dots) \end{array} \tag{18}$$

This is the Schrödinger equation corresponding to the Hamiltonian function

$$F = H_P(J) + \Sigma_{r,s} H_{rs} N^{1/2} (N_s + 1 - \delta_{rs})^{1/2} e^{i(\Theta_1 - \Theta_2)/h}, \tag{19}$$

in which $H_{rs}$ is now a function of the $J$'s and $\omega$'s, being such that when represented by a matrix in the $(J)$ scheme its $(J'J'')$ element is $H(J' r; J'' s)$. (It should be noticed that $H_{rs}$ still commutes with the $N$'s and $\Theta$'s.)

Thus the interaction of a perturbing system and an assembly satisfying the Einstein-Bose statistics can be described by a Hamiltonian of the form

14
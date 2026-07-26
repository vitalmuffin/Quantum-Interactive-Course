the assembly is defined by the numbers $r_1, r_2 \dots r_n \dots$ which are the labels of the stationary states in which the separate systems lie. The Schrödinger equation for the assembly in a set of variables that specify the stationary states will be of the form (6) [with $H_A$ instead of $H$], and we can write it in the notation of equation (5) thus: –

$$ih\dot{b}(r_1 r_2 \dots) = \Sigma_{s_1, s_2 \dots} H_A(r_1 r_2 \dots; s_1 s_2 \dots) b(s_1 s_2 \dots), \quad (14)$$

where $H_A(r_1 r_2 \dots; s_1 s_2 \dots)$ is the general matrix element of $H_A$ [with the time factor removed]. This matrix element vanishes when more than one $s_n$ differs from the corresponding $r_n$; equals $H_{r_m s_m}$ when $s_m$ differs from $r_m$ and every other $s_n$ equals $r_n$; and equals $\Sigma_n H_{r_n r_n}$ when every $s_n$ equals $r_n$. Substituting these values in (14), we obtain

$$\begin{aligned} ih\dot{b}(r_1 r_2 \dots) &= \Sigma_m \Sigma_{s_m \neq r_m} H_{r_m s_m} b(r_1 r_2 \dots r_{m-1} s_m r_{m+1} \dots) \\ &\quad + \Sigma_n H_{r_n r_n} (r_1 r_2 \dots). \end{aligned} \quad (15)$$

We must now restrict $b(r_1 r_2 \dots)$ to be a symmetrical function of the variables $r_1, r_2 \dots$ in order to obtain the Einstein-Bose statistics. This is permissible since if $b(r_1 r_2 \dots)$ is symmetrical at any time, then equation (15) shows that $\dot{b}(r_1 r_2 \dots)$ is also symmetrical at that time, so that $b(r_1 r_2 \dots)$ will remain symmetrical.

Let $N_r$ denote the number of systems in the state $r$. Then a stationary state of the assembly describable by a symmetrical eigenfunction may be specified by the numbers $N_1, N_2 \dots N_r \dots$ just as well as by the numbers $r_1, r_2 \dots r_n \dots$, and we shall be able to transform equation (15) to the variables $N_1, N_2 \dots$. We cannot actually take the new eigenfunction $b(N_1, N_2 \dots)$ equal to the previous one $b(r_1 r_2 \dots)$ but must take one to be a numerical multiple of the other in order that each may be correctly normalised with respect to its respective variables. We must have, in fact,

$$\Sigma_{r_1, r_2 \dots} |b(r_1 r_2 \dots)|^2 = 1 = \Sigma_{N_1, N_2 \dots} |b(N_1, N_2 \dots)|^2,$$

and hence we must take $|b(N_1, N_2 \dots)|^2$ equal to the sum of $|b(r_1 r_2 \dots)|^2$ for all values of the numbers $r_1 r_2 \dots$ such that there are $N_1$ of them equal to $1, N_2$ equal to $2$, etc. There are $N!/N_1!N_2!\dots$ terms in this sum, where $N = \Sigma_r N_r$ is the total number of systems, and they are all equal, since $b(r_1 r_2 \dots)$ is a symmetrical function of its variables $r_1, r_2 \dots$. Hence we must have

$$b(N_1, N_2 \dots) = (N!/N_1!N_2!\dots)^{1/2} b(r_1 r_2 \dots).$$

12
where the $V_{rs}$'s are the elements of the matrix representing $V$. The conjugate imaginary equation is

$$-ih\dot{a}_r^* = \Sigma_s V_{rs}^* a_s^* = \Sigma_s a_s^* V_{sr}. \tag{4'}$$

If we regard $a_r$ and $ih\dot{a}_r^*$ as canonical conjugates, equations (4) and (4') take the Hamiltonian form with the Hamiltonian function $F_1 = \Sigma_{rs} a_r^* V_{rs} a_s$, namely,

$$\frac{da_r}{dt} = \frac{1}{ih} \frac{\partial F_1}{\partial a_r^*}, \quad ih \frac{\partial a_r^*}{dt} = -\frac{\partial F_1}{\partial a_r}.$$

We can transform to the canonical variables $N_r, \phi_r$ by the contact transformation

$$a_r = N_r^{1/2} e^{-i\phi_r/h}, \quad a_r^* = N_r^{1/2} e^{i\phi_r/h}.$$

This transformation makes the new variables $N_r$ and $\phi_r$ real, $N_r$ being equal to $a_r a_r^* = |a_r|^2$, the probable number of systems in the state $r$, and $\phi_r/h$ being the phase of the eigenfunction that represents them. The Hamiltonian $F_1$ now becomes

$$F_1 = \Sigma_{rs} V_{rs} N_r^{1/2} N_s^{1/2} e^{i(\phi_r - \phi_s)/h},$$

and the equations that determine the rate at which transitions occur have the canonical form

$$N_r = -\frac{\partial F_1}{\partial \phi_r}, \quad \dot{\phi}_r = \frac{\partial F_1}{\partial N_r}.$$

A more convenient way of putting the transition equations in the Hamiltonian form may be obtained with the help of the quantities

$$b_r = a_r e^{-iW_r t/h}, \quad b_r^* = a_r^* e^{iW_r t/h},$$

$W_r$ being the energy of the state $r$. We have $|b_r|^2$ equal to $|a_r|^2$ the probable number of systems in the state $r$. For $b_r$ we find

$$\begin{array}{l} ih\dot{b}_r = W_r b_r + ih\dot{a}_r e^{-W_r t/h} \\ = W_r b_r + \Sigma_s V_{rs} b_s e^{i(W_s - W_r)t/h} \end{array}$$

with the help of (4). If we put $V_{rs} = c_{rs} e^{i(W_r - W_s)t/h}$, so that $v_{rs}$ is a constant when $V$ does not involve the: time explicitly, this reduces to

$$\begin{array}{l} ih\dot{b}_r = W_r b_r + \Sigma_s v_{rs} b_s \\ = \Sigma_s H_{rs} b_s, \end{array} \tag{5}$$

7
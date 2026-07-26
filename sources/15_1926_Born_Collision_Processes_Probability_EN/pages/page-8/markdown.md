Born – Quantum mechanics of collision processes.

8

converges uniformly for every finite interval; it can then be differentiated term-wise arbitrarily often, and is then, as is easy to see, the desired solution to our differential equation.

However, since all $u_1, u_2, \dots$ vanish as $x \to +\infty$, the function $\psi$ will be asymptotic to $u_0 = e^{ikx}$ at positive infinity.

In precisely the same way, one shows that there is a solution that is asymptotic to $e^{-ikx}$ as $x \to +\infty$. Since the general solution has only two constants, it must asymptotically have the form:

$$\psi^+(x) = a e^{ikx} + b e^{-ikx} \tag{7}$$

as $x \to +\infty$. Here, the degeneracy of the system makes its appearance; every energy value $W$ is associated with two values $k, -k$ and two linearly-independent solutions.

In an entirely similar way, it follows that the general solution must have the same form as $x \to -\infty$:

$$\psi^-(x) = A e^{ikx} + B e^{-ikx}. \tag{8}$$

In this, the amplitudes $A, B$ are well-defined functions of $a, b$.

We now decompose the solution into incoming and outgoing waves; for that, we add the time factor $e^{ik\upsilon} \left( k\upsilon = 2\pi\nu = \frac{2\pi}{h}W \right)$ and set:

$$\left. \begin{array}{l} a = c_e e^{i\varphi_e t}, \quad A = C_a e^{i\Phi_a t}, \\ b = c_a e^{-i\varphi_a t}, \quad B = C_e e^{-i\Phi_e t}. \end{array} \right\} \tag{9}$$

One will then have:

$$\left. \begin{array}{l} \psi^+(x) = c_e e^{ik(x+\upsilon t+\varphi_e)} + c_a e^{-ik(x-\upsilon t+\varphi_a)}, \\ \psi^-(x) = C_a e^{ik(x+\upsilon t+\Phi_a)} + C_e e^{-ik(x-\upsilon t+\Phi_a)}. \end{array} \right\} \tag{10}$$

The real parts of the terms that are denoted with the index $e$ represent the incoming waves, while the terms that are denoted with an $a$ represent the outgoing waves.

We are interested in the case in which only one wave is incoming at $x = +\infty$. One will then have $C_e = 0$, and one can arbitrarily set $\varphi_e = 0$, moreover. One will then have:

$$\left. \begin{array}{l} \psi^+(x) = c_e e^{ik(x+\upsilon t)} + c_a e^{-ik(x-\upsilon t+\varphi_a)}, \\ \psi^-(x) = C_a e^{ik(x+\upsilon t+\Phi_a)}. \end{array} \right\} \tag{11}$$

We have shown that $\psi^-(x)$ is determined in terms of $\psi^+(x)$ by integration; i.e., $A, B$ are well-defined functions of $a, b$. In our case $C_e = 0$, so we will have $B = 0$, and one thus has two equations of the form:

$$\left. \begin{array}{l} A = A(a,b), \\ 0 = B(a,b). \end{array} \right\} \tag{12}$$
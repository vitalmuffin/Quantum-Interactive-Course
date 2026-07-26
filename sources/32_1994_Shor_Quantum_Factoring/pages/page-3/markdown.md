within the laws of quantum mechanics. Some suggestions have been made as to possible designs for such computers [29, 21, 22, 12], but there will be substantial difficulty in building any of these [18, 31]. Even if it is possible to build small quantum computers, scaling up to machines large enough to do interesting computations could present fundamental difficulties. It is hoped that this paper will stimulate research on whether it is feasible to actually construct a quantum computer.

Even if no quantum computer is ever built, this research does illuminate the problem of simulating quantum mechanics on a classical computer. Any method of doing this for an arbitrary Hamiltonian would necessarily be able to simulate a quantum computer. Thus, any general method for simulating quantum mechanics with at most a polynomial slowdown would lead to a polynomial algorithm for factoring.

## 2 Quantum computation

In this section we will give a brief introduction to quantum computation, emphasizing the properties that we will use. For a more complete overview I refer the reader to Simon's paper in this proceedings [28] or to earlier papers on quantum computational complexity theory [5, 32].

In quantum physics, an experiment behaves as if it proceeds down all possible paths simultaneously. Each of these paths has a complex probability amplitude determined by the physics of the experiment. The probability of any particular outcome of the experiment is proportional to the square of the absolute value of the sum of the amplitudes of all the paths leading to that outcome. In order to sum over a set of paths, the outcomes have to be identical in all respects, i.e., the universe must be in the same state. A quantum computer behaves in much the same way. The computation proceeds down all possible paths at once, and each path has associated with it a complex amplitude. To determine the probability of any final state of the machine, we add the amplitudes of all the paths which reach that final state, and then square the absolute value of this sum.

An equivalent way of looking at this process is to imagine that the machine is in some superposition of states at every step of the computation. We will represent this superposition of states as

$$\sum_{i} a_{i} |S_{i}\rangle, \tag{2.1}$$

where the amplitudes $a_{i}$ are complex numbers such that $\sum_{i} |a_{i}|^{2} = 1$ and each $|S_{i}\rangle$ is a basis state of the machine; in a quantum Turing machine, a basis state is defined by what is written on the tape and by the position and state of the head. In a quantum circuit a basis state is defined by

the values of the signals on all the wires at some level of the circuit. If the machine is examined at a particular step, the probability of seeing basis state $|S_{i}\rangle$ is $|a_{i}|^{2}$; however, by the Heisenberg uncertainty principle, looking at the machine during the computation will disturb the rest of the computation.

The laws of quantum mechanics only permit unitary transformations of the state. A unitary matrix is one whose conjugate transpose is equal to its inverse, and requiring state transformations to be represented by unitary matrices ensures that the probabilities of obtaining all possible outcomes will add up to one. Further, the definitions of quantum Turing machine and quantum circuit only allow local unitary transformations, that is, unitary transformations on a fixed number of bits.

Perhaps an example will be informative at this point. Suppose our machine is in the superposition of states

$$\frac{1}{\sqrt{2}} |000\rangle + \frac{1}{2} |100\rangle - \frac{1}{2} |110\rangle \tag{2.2}$$

and we apply the unitary transformation

$$\begin{array}{c|cccc} & 00 & 01 & 10 & 11 \\ 00 & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ 01 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\ 10 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ 11 & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \end{array} \tag{2.3}$$

to the last two bits of our state. That is, we multiply the last two bits of the components of the vector (2.2) by the matrix (2.3). The machine will then go to the superposition of states

$$\frac{1}{2\sqrt{2}} (|000\rangle + |001\rangle + |010\rangle + |011\rangle) + \frac{1}{2} |101\rangle + \frac{1}{2} |111\rangle. \tag{2.4}$$

Notice that the result would have been different had we started with the superposition of states

$$\frac{1}{\sqrt{2}} |000\rangle + \frac{1}{2} |100\rangle + \frac{1}{2} |110\rangle, \tag{2.5}$$

which has the same probabilities of being in any particular configuration if it is observed.

We now give certain properties of quantum computation that will be useful. These facts are not immediately apparent from the definition of quantum Turing machine or quantum circuit, and they are very useful for constructing algorithms for quantum machines.

Fact 1: A deterministic computation is performable on a quantum computer if and only if it is reversible. From results on reversible computation [3, 30], we can compute any polynomial time function $f(a)$ as long as we keep the input, $a$, on the machine. To

126
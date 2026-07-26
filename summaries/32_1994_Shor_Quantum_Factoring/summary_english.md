# Algorithms for Quantum Computation: Discrete Logarithms and Factoring

> This extended summary is based entirely on the English version of the paper. Equations and image references retain the notation of the source text.

## Bibliographic overview

- **Authors:** Peter W. Shor
- **Year:** 1994
- **Journal:** IEEE Journal on Selected Areas in Communications
- **DOI:** `10.1109/49.317578`
- **Collection folder:** `32_1994_Shor_Quantum_Factoring`

## Central claims

- This paper gives Las Vegas algorithms for finding discrete logarithms and factoring integers on a quantum computer that take a number of steps which is polynomial in the input size, e.g., the number of digits of the integer to be factored.
- These two problems are generally considered hard on a classical computer and have been used as the basis of several proposed cryptosystems. (We thus give the first examples of quantum cryptanalysis.)
- He also suggested the possibility of using a computer based on quantum mechanical principles to avoid this problem, thus implicitly asking the converse question: by using quantum mechanics in a computer can you compute more efficiently than on a classical computer.
- Although he did not ask whether quantum mechanics conferred extra power to computation, he did show that a Turing machine could be simulated by the reversible unitary evolution of a quantum process, which is a necessary prerequisite for quantum computation.
- One of the results contained in this paper was an oracle problem (a problem involving a "black box" subroutine) which can be done in polynomial time on a quantum Turing machine and requires super-polynomial time on a classical computer.
- This was the first indication, other than the fact that nobody knew how to simulate a quantum computer on a classical computer without an exponential slowdown, that quantum computation might obtain a greater than polynomial speedup over classical computation augmented with a random number generator.
- This result was improved by Simon [28], who gave a much simpler construction of an oracle problem which takes polynomial time on a quantum computer and requires exponential time on a classical computer.
- In another result in Bernstein and Vazirani's paper, a particular class of quantum Turing machine was rigorously defined and a universal quantum Turing machine was given which could simulate any other quantum Turing machine of this class.
- Fact 2: Any polynomial size unitary matrix can be approximated using a polynomial number of elementary unitary transformations [10, 5, 32] and thus can be approximated in polynomial time on a quantum computer.
- In this section we give some techniques for constructing unitary transformations on quantum machines, which will result in our showing how to construct one particular unitary transformation in polynomial time.
- Suppose further that the state transformation $B'$ can be done in time $T(B')$ on a quantum Turing machine.
- [4] have shown that it is sufficient to use polynomial precision for any computation on a quantum Turing machine to obtain the answer with high probability.
- Instead of giving a quantum computer algorithm to factor n, we will give a quantum computer algorithm for finding the order of an element x in the multiplicative group (mod n); that is, the least integer r such that \( x^{r} \equiv 1 \pmod{n} \) .
- Thus, we will be able to find a set of c''s such that all prime powers p i^α i 20 dividing p - 1 are relatively prime to at least one of these c''s.

## Section-by-section summary

### Abstract

- This paper gives Las Vegas algorithms for finding discrete logarithms and factoring integers on a quantum computer that take a number of steps which is polynomial in the input size, e.g., the number of digits of the integer to be factored.
- These two problems are generally considered hard on a classical computer and have been used as the basis of several proposed cryptosystems. (We thus give the first examples of quantum cryptanalysis.)

### 1 Introduction

- He also suggested the possibility of using a computer based on quantum mechanical principles to avoid this problem, thus implicitly asking the converse question: by using quantum mechanics in a computer can you compute more efficiently than on a classical computer.
- This question was addressed in [11, 6, 7], but it was not shown how to solve any problem in quantum polynomial time that was not known to be solvable in BPP (the class of problems which can be solved in polynomial time with a bounded probability of error).
- One of the results contained in this paper was an oracle problem (a problem involving a "black box" subroutine) which can be done in polynomial time on a quantum Turing machine and requires super-polynomial time on a classical computer.
- This result was improved by Simon [28], who gave a much simpler construction of an oracle problem which takes polynomial time on a quantum computer and requires exponential time on a classical computer.
- In another result in Bernstein and Vazirani's paper, a particular class of quantum Turing machine was rigorously defined and a universal quantum Turing machine was given which could simulate any other quantum Turing machine of this class.
- Even if no quantum computer is ever built, this research does illuminate the problem of simulating quantum mechanics on a classical computer.
- Thus, any general method for simulating quantum mechanics with at most a polynomial slowdown would lead to a polynomial algorithm for factoring.

### 2 Quantum computation

- If the machine is examined at a particular step, the probability of seeing basis state $ S {i}\rangle$ is $ a {i} ^{2}$; however, by the Heisenberg uncertainty principle, looking at the machine during the computation will disturb the rest of the computation.
- Further, the definitions of quantum Turing machine and quantum circuit only allow local unitary transformations, that is, unitary transformations on a fixed number of bits.
- Suppose our machine is in the superposition of states
- Fact 2: Any polynomial size unitary matrix can be approximated using a polynomial number of elementary unitary transformations [10, 5, 32] and thus can be approximated in polynomial time on a quantum computer.

### 3 Building unitary transformations

- Since quantum computation deals with unitary transformations, it is helpful to be able to build certain useful unitary transformations.
- In this section we give some techniques for constructing unitary transformations on quantum machines, which will result in our showing how to construct one particular unitary transformation in polynomial time.
- Suppose further that the state transformation $B'$ can be done in time $T(B')$ on a quantum Turing machine.
- We will decompose $A q$ into a product of a polynomial number of unitary transformations, all of which are performable in polynomial time; this enables us to construct $A q$ in polynomial time.
- We also need to show how to find a smooth $q$ that lies between $n$ and $2n$ in polynomial time.

### 4 Discrete log: the easy case

- The discrete log problem is: given a prime $p$, a generator $g$ of the multiplicative group (mod $p$) and an $x$ (mod $p$), find an $r$ such that $g^r \equiv x \pmod p$.
- We will start by giving a polynomial-time algorithm for discrete log on a quantum computer in the case that $p - 1$ is smooth.
- We now compute the probability that the computation ends with the machine in state $ c, d, y\rangle$ with $y \equiv g^k \pmod{p}$.
- In fact, we can find a set of $c$'s such that at least one is relatively prime to every prime divisor of $p-1$ by repeating the experiment only an expected constant number of times.

### 5 A note on precision

- We thus need to show that the computations in the previous section need to use only polynomial precision in the amplitudes.
- Each positive case, i.e., one resulting in $d \equiv -rc$, will still occur with nearly as large probability as before; instead of adding $p-1$ amplitudes which have exactly the same phase angle, we add $p-1$ amplitudes which have nearly the same phase angle, and thus the size of the sum will only be reduced by a constant factor.
- [4] have shown that it is sufficient to use polynomial precision for any computation on a quantum Turing machine to obtain the answer with high probability.
- Although Bernstein and Vazirani [4] show that the number of bits of precision needed is never more than the logarithm of the number of computational steps a quantum computer takes, in some algorithms it could conceivably require less.

### 6 Factoring

- \[ \frac {1}{q} \sum {a = 0} ^ {q - 1} \exp (2 \pi i a c / q) c, x ^ {a} (\mathrm{mod} n) \rangle . \tag {6.3} \]
- \[ \left \frac {1}{q} \sum {a: x ^ {a} \equiv x ^ {k}} \exp (2 \pi i a c / q) \right ^ {2}. \tag {6.4} \]
- \[ \left \frac {1}{q} \sum {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i (b r + k) c / q) \right ^ {2}. \tag {6.5} \]
- \[ \left \frac {1}{q} \sum {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i b \{r c \} {q} / q) \right ^ {2}. \tag {6.6} \]
- Using the theorem that $\phi(r)/r k/\log \log r$ for some fixed $k$ [17, Theorem 328], this shows that we find $r$ at least a $k/\log \log r$ fraction of the time, so by repeating this experiment only $O(\log \log r)$ times, we are assured of a high probability of success.

### 7 Discrete log: the general case

- What we have is that each good $(c, d)$ pair is generated with probability at least $.137p/q 1/16q$, and that at least a tenth of the possible $c$'s are in a good $(c, d)$ pair.
- Thus, for a prime power $p t^{n t}$, a random good $c'$ is divisible by $p t^{n t}$ with probability at most $10/p t^{n t}$.
- If we have $t$ good $c'$'s, the probability of having a prime power over 20 that divides all of them is therefore at most
- Thus, we will be able to find a set of c''s such that all prime powers p i^α i 20 dividing p - 1 are relatively prime to at least one of these c''s.
- We can thus try all possibilities for residues modulo powers of primes less than 20: for each possibility we can calculate the corresponding r using the Chinese remainder theorem, and then check to see whether it is the desired discrete logarithm.

### Acknowledgements

- I would like to thank Jeff Lagarias for finding and fixing a critical bug in the first version of the discrete log algorithm.
- I would also like to thank him, Charles Bennett, Gilles Brassard, Andrew Odlyzko, Dan Simon, Umesh Vazirani, as well as other correspondents too numerous to list, for productive discussions, for corrections to and improvements of early drafts of this paper, and for pointers to the literature.

### References

- P. Benioff, "Quantum mechanical Hamiltonian models of Turing machines," J. Stat.
- C. H. Bennett, E. Bernstein, G. Brassard and U. Vazirani, "What is feasible on a quantum computer," manuscript (1994).
- A. Berthiaume and G. Brassard, "The quantum challenge to structural complexity theory," in Proc.
- D. Deutsch, "Quantum theory, the Church-Turing principle and the universal quantum computer," Proc.

## Important equations

### 1. Section: 1 Introduction

**Context:** The other is P P, which are those problems which could be solved in polynomial time if sums of exponentially many terms could be computed efficiently (where these sums must satisfy the requirement that each term is computable in polynomial time).

$$\mathrm{P} \subseteq \mathrm{BPP}, \mathrm{NP} \subseteq \mathrm{P}^{\# \mathrm{P}} \subseteq \mathrm{PSPACE}.$$

### 2. Section: 2 Quantum computation

**Context:** We will represent this superposition of states as

$$\sum_{i} a_{i} |S_{i}\rangle, \tag{2.1}$$

### 3. Section: 2 Quantum computation

**Context:** Suppose our machine is in the superposition of states

$$\frac{1}{\sqrt{2}} |000\rangle + \frac{1}{2} |100\rangle - \frac{1}{2} |110\rangle \tag{2.2}$$

### 4. Section: 2 Quantum computation

**Context:** Suppose our machine is in the superposition of states

$$\begin{array}{c|cccc} & 00 & 01 & 10 & 11 \\ 00 & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ 01 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\ 10 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ 11 & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \end{array} \tag{2.3}$$

### 5. Section: 2 Quantum computation

**Context:** The machine will then go to the superposition of states

$$\frac{1}{2\sqrt{2}} (|000\rangle + |001\rangle + |010\rangle + |011\rangle) + \frac{1}{2} |101\rangle + \frac{1}{2} |111\rangle. \tag{2.4}$$

### 6. Section: 2 Quantum computation

**Context:** Notice that the result would have been different had we started with the superposition of states

$$\frac{1}{\sqrt{2}} |000\rangle + \frac{1}{2} |100\rangle + \frac{1}{2} |110\rangle, \tag{2.5}$$

### 7. Section: 3 Building unitary transformations

**Context:** We will perform the transformation that takes the state $ a\rangle$ to the state

$$\frac{1}{q^{1/2}} \sum_{b=0}^{q-1} |b\rangle \exp(2\pi i ab/q). \tag{3.1}$$

### 8. Section: 3 Building unitary transformations

**Context:** Note the asymmetry in the definitions of $a$, $b$ and $c$.

$$C(a, b) = \left\{ \begin{array}{cl} 0 & \text{if } \alpha_2 \neq \beta_1 \\ \frac{1}{q_1^{1/2}} \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1)} & \text{otherwise,} \end{array} \right. \tag{3.2}$$

### 9. Section: 3 Building unitary transformations

**Context:** Note the asymmetry in the definitions of $a$, $b$ and $c$.

$$D(b, c) = \left\{ \begin{array}{cl} 0 & \text{if } \beta_2 \neq \gamma_2 \\ \frac{1}{q_2^{1/2}} \omega^{\beta_1 \gamma_1 q_1 - \beta_1 \beta_2 u} & \text{otherwise.} \end{array} \right. \tag{3.3}$$

### 10. Section: 3 Building unitary transformations

**Context:** Within a given block $\alpha 2 = \beta 1$, the entries look like

$$\begin{array}{l} \sqrt{q_1} C(a, b) = \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1)} \\ = \exp(2\pi i(\alpha_1 \beta_2 + \beta_1 \beta_2 t)q_2/q) \\ = \exp(2\pi i(\alpha_1 + \alpha_2 t)\beta_2/q_1). \tag{3.5} \end{array}$$

### 11. Section: 4 Discrete log: the easy case

**Context:** The algorithm starts out by "choosing" numbers $a$ and $b$ (mod $p - 1$) uniformly, so the state of the machine after this step is

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b\rangle. \tag{4.1}$$

### 12. Section: 4 Discrete log: the easy case

**Context:** We now substitute the equation $a \equiv k + rb \pmod{p-1}$ in the above exponential.

$$\left| \frac{1}{(p-1)^2} \sum_{b=0}^{p-2} \exp \left( \frac{2\pi i}{p-1} (kc + b(d+rc)) \right) \right|^2. \tag{4.5}$$

### 13. Section: 6 Factoring

**Context:** The probability of seeing a given state \( c, x^{k} (\text{mod } n)\rangle \) will thus be at least \( 1/3r^{2} \) if

$$\frac{-r}{2} \leq rc - dq \leq \frac{r}{2}. \tag{6.9}$$

### 14. Section: 6 Factoring

**Context:** Dividing by $rq$ and rearranging the terms gives

$$\left| \frac{c}{q} - \frac{d}{r} \right| \leq \frac{1}{2q}. \tag{6.10}$$

### 15. Section: 7 Discrete log: the general case

**Context:** Next, we do the same thing as in the easy case, that is, we choose $a$ and $b$ uniformly (mod $p-1$), and then compute $g^a x^{-b} \pmod{p}$.

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b, g^a x^{-b} \pmod{p}\rangle. \tag{7.1}$$

### 16. Section: 7 Discrete log: the general case

**Context:** We will show that if we get enough "good" outputs, then we still can deduce $r$, and that furthermore, the chance of getting a "good" output is constant.

$$|\{T\}_q| = |rc + d - \frac{r}{p-1} \{c(p-1)\}_q - jq| \leq \frac{1}{2}, \tag{7.9}$$

### 17. Section: 7 Discrete log: the general case

**Context:** Since $p < q$, and from Condition (7.9), $ W \le 1/2$, putting everything together, the probability of arriving at a state $ c, d, y)$ that satisfies both Condition (7.9) and (7.10) is at least

$$\left( \frac{1}{q} \frac{2}{\pi} \int_{\pi/10}^{7\pi/20} \cos t \, dt \right)^2, \tag{7.13}$$

### 18. Section: 7 Discrete log: the general case

**Context:** If we have $t$ good $c'$'s, the probability of having a prime power over 20 that divides all of them is therefore at most

$$\sum_{\substack{p_t^{n_t} > 20 \\ p_t^{n_t} \le p - 1}} \left( \frac{10}{p_t^{n_t}} \right)^t, \tag{7.16}$$

## Figures and image references

No Markdown image references were found in the text.
## Important tables

No Markdown tables were found in the text.
## Results and significance

- We now give a lower bound on the probability of each good output, i.e., an output that satisfies Conditions (7.9) and (7.10).
- What we have is that each good $(c, d)$ pair is generated with probability at least $.137p/q 1/16q$, and that at least a tenth of the possible $c$'s are in a good $(c, d)$ pair.
- Thus, for a prime power $p t^{n t}$, a random good $c'$ is divisible by $p t^{n t}$ with probability at most $10/p t^{n t}$.
- If we have $t$ good $c'$'s, the probability of having a prime power over 20 that divides all of them is therefore at most
- Thus, we will be able to find a set of c''s such that all prime powers p i^α i 20 dividing p - 1 are relatively prime to at least one of these c''s.
- We can thus try all possibilities for residues modulo powers of primes less than 20: for each possibility we can calculate the corresponding r using the Chinese remainder theorem, and then check to see whether it is the desired discrete logarithm.
- C. H. Bennett, E. Bernstein, G. Brassard and U. Vazirani, "What is feasible on a quantum computer," manuscript (1994).
- D. Simon, "On the power of quantum computation," in Proc.

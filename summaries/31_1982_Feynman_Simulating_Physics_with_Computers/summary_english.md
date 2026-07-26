# Simulating Physics with Computers

> This extended summary is based entirely on the English version of the paper. Equations and image references retain the notation of the source text.

## Bibliographic overview

- **Authors:** Richard P. Feynman
- **Year:** 1982
- **Journal:** International Journal of Theoretical Physics
- **DOI:** `10.1007/BF02650179`
- **Collection folder:** `31_1982_Feynman_Simulating_Physics_with_Computers`

## Central claims

- I want to talk about the problem of simulating physics with computers and I mean that in a specific way which I am going to explain.
- The first question is, What kind of computer are we going to use to simulate physics?
- I would like to have the elements of this computer locally interconnected , and therefore sort of think about cellular automata as an example (but I don't want to force it).
- First, I am going to describe the possibility of simulating physics in the classical approximation, a thing which is usually described by local differential equations.
- But the physical world is quantum mechanical, and therefore the proper problem is the simulation of quantum physics—which is what I really want to talk about, but I'll come to that later.
- If this is to be proved and the type of computer is as I've already explained, then it's going to be necessary that everything that happens in a finite volume of space and time would have to be exactly analyzable with a finite number of logical operations.
- So I know that quantum mechanics seem to involve probability—and I therefore want to talk about simulating probability.
- So let us now think about the characteristics of a local probabilistic computer, because I'll see if I can imitate nature with that (by 'nature' I'm now going to mean quantum mechanics).
- Can you make a cellular automaton, or something, imitate with the same probability what nature does, where I'm going to suppose that quantum mechanics is correct, or at least after I discretize space and time it's correct, and see if I can do it.
- For example, if you would like to know whether the first index is positive, the probability of that would be
- If you can invent a probability $M$ like that, you write the equations for it according to normal logic, those are the correct equations, the real, correct, quantum mechanical equations for this $F$, and therefore you'd say, Okay, so I can imitate it with a probabilistic computer!
- Now suppose we measure at $\phi 2 - \phi 1 = 30^{\circ}$, and ask, With what probability do we get the same result?
- Then you go and you say, Now can I imitate that with a device which is going to produce the same results, and which will operate locally, and you try to invent some kind of way of doing that, and if you do it in the ordinary way of thinking, you find that you can't get there with the same probability.
- Therefore some new kind of thinking is necessary, but physicists, being kind of dull minded, only look at nature, and don't know how to think in these new ways.

## Section-by-section summary

### 1. INTRODUCTION

- I want to talk about the problem of simulating physics with computers and I mean that in a specific way which I am going to explain.
- The first question is, What kind of computer are we going to use to simulate physics?
- But the physical world is quantum mechanical, and therefore the proper problem is the simulation of quantum physics—which is what I really want to talk about, but I'll come to that later.
- So this is an interesting subject because it tells us something about computer rules, and might tell us something about physics.
- That is, if you say I want to explain this much physics, I can do it exactly and I need a certain-sized computer.

### 2. SIMULATING TIME

- You know that we don't have infinite accuracy in physical measurements so time might be discrete on a scale of less than $10^{-27}$ sec. (You'd have to have it at least like to this to avoid clashes with experiment—but make it $10^{-41}$ sec. if you like, and then you've got us!)
- And therefore the time (by the way, like the space in the case of cellular automata) is not simulated at all, it's imitated in the computer.
- An interesting question comes up: 'Is there a way of simulating it, rather than imitating it?' Well, there's a way of looking at the world that is called the space-time view, imagining that the points of space and time are all laid out, so to speak, ahead of time.
- So classical physics is local , causal , and reversible , and therefore apparently quite adaptable (except for the discreteness and so on, which I already mentioned) to computer simulation.

### 3. SIMULATING PROBABILITY

- And therefore, some of the younger students ... you know how it always is, every new idea, it takes a generation or two until it becomes obvious that there's no real problem.
- So I know that quantum mechanics seem to involve probability—and I therefore want to talk about simulating probability.
- Well, one way that we could have a computer that simulates a probabilistic theory, something that has a probability in it, would be to calculate the probability and then interpret this number to represent nature.
- In other words, we could imagine and be perfectly happy, I think, with a probabilistic simulator of a probabilistic nature, in which the machine doesn't exactly do what nature does, but if you repeated a particular type of experiment a sufficient number of times to determine nature's probability, then you did the corresponding experiment on the computer, you'd get the corresponding probability with the corresponding accuracy (with the same kind of accuracy of statistics).
- So let us now think about the characteristics of a local probabilistic computer, because I'll see if I can imitate nature with that (by 'nature' I'm now going to mean quantum mechanics).
- And let the probability to find some configuration $\{s i\}$ (a set of values of the state $s i$ at each point $i$) be some number $P(\{s i\})$.
- Now I explicitly go to the question of how we can simulate with a computer—a universal automaton or something—the quantum-mechanical effects. (The usual formulation is that quantum mechanics has some sort of a differential equation for a function $\psi$.) If you have a single particle, $\psi$ is a function of $x$ and $t$, and this differential equation could be simulated just like my probabilistic equation was before.

### 4. QUANTUM COMPUTERS—UNIVERSAL QUANTUM SIMULATORS

- I therefore believe it's true that with a suitable class of quantum machines you could imitate any quantum system, including the physical world.
- The same way we should try to find out what kinds of quantum mechanical systems are mutually intersimulatable, and try to find a specific class, or a character of that class which will simulate everything.
- Suppose that we try the following guess: that every finite quantum mechanical system can be described exactly , imitated exactly, by supposing that we have another system such that at each point in space-time this system has only two possible base states.
- I'm not sure that it's sufficient, because I'm not sure that it takes care of Fermi particles.

### 5. CAN QUANTUM SYSTEMS BE PROBABILISTICALLY SIMULATED BY A CLASSICAL COMPUTER?

- Now the next question that I would like to bring up is, of course, the interesting one, i.e., Can a quantum system be probabilistically simulated by a classical (probabilistic, I'd assume) universal computer?
- I must point out that you must directly generate the probabilities, the results, with the correct quantum probability.
- These two equations are correct, and therefore you would hope that maybe $W(x, p)$ is the probability of finding $x$ and $p$.
- For example, if you would like to know whether the first index is positive, the probability of that would be
- You can ask, for example, what is the probability that the two indices are the same?

### 6. NEGATIVE PROBABILITIES

- These equations unfortunately cannot be so interpreted on the basis of the so-called 'probability', or this probabilistic computer can't simulate them, because the $F$ is not necessarily positive.
- The probability of finding the first index negative is the sum $f {-+} + f {-+}$ which is also 50%.
- The only difference between a probabilistic classical world and the equations of the quantum world is that somehow or other it appears as if the probabilities would have to go negative, and that we do not know, as far as I know, how to simulate.

### 7. POLARIZATION OF PHOTONS—TWO-STATES SYSTEMS

- If you put a polarized photon in, then it will go to one beam called the ordinary ray, or another, the extraordinary one.
- If you put detectors there you find that each photon that you put in, it either comes out in one or the other 100% of the time, and not half and half.
- The probability of finding it in the ordinary ray plus the probability of finding it in the extraordinary ray is always 1—you have to have that rule.
- If the photon is $O$ from the first calcite, then the second calcite gives $O-O$ with probability $\cos^2\phi$ or $O-E$ with the complementary probability $1-\cos^1\phi=\sin^2\phi$.

### 8. TWO-PHOTON CORRELATION EXPERIMENT

- Let us turn now to the two photon correlation experiment (see Figure 4).
- Quantum theory and experiment agree that the probability $P {OO}$ that both of us detect an ordinary photon is
- Photon 1 must be in some condition $\alpha$ with the probability $f \alpha(\phi 1)$, that determines it to go through as an ordinary ray [the probability it would pass as $E$ is $1 - f \alpha(\phi 1)$].
- Therefore, whatever condition it's in, it has some predictive pattern in which you either have a prediction of ordinary or of extraordinary—three and three—because at right angles they're not the same color.
- You just measure at $60^{\circ}$, and you'll find white, and therefore you'll predict white, or ordinary, for me.
- If we measure at the same angle, we always find that with this kind of arrangement we would get the same result.
- Now suppose we measure at $\phi 2 - \phi 1 = 30^{\circ}$, and ask, With what probability do we get the same result?

### 9. DISCUSSION

- Question: Just to interpret, you spoke first of the probability of A given B, versus the probability of A and B jointly—that's the probability of one observer seeing the result, assigning a probability to the other; and then you brought up the paradox of the quantum mechanical result being $3/4$, and this being $2/3$.
- Because the laws of physics as written now have, in the classical limit, a continuous variable everywhere, space and time.
- If, for example, in your theory you were going to have an electric field, then the electric field could not have (if it's going to be imitable, computable by a finite number of elements) an
- Because you see, if you would imagine that the electric field is coming out of some ‘ones’ or something, the lowest you could get would be a full one, but that’s what we see, you get a full photon.
- All these things suggest that it’s really true, somehow, that the physical world is representable in a discretized way, because every time you get into a bind like this, you discover that the experiment does just what’s necessary to escape the trouble that would come if the electric field went to zero, or you’d never be able to see a star beyond a certain distance, because the field would have gotten below the number of digits that your world can carry.

## Important equations

### 1. Section: 2. SIMULATING TIME

**Context:** And then we could say that a 'computer' rule (now computer would be in quotes, because it's not the standard kind of computer which operates in time) is: We have a state $s i$ at each point $i$ in space-time. (See Figure 1.) The state $s i$ at the space time point $i$ is a given function $F i(s j, s k, \ldots)$ of the state at the points $j, k$ in some neighborhood of $i$:

$$
s_i = F_i(s_j, s_k, \ldots)
$$

### 2. Section: 3. SIMULATING PROBABILITY

**Context:** A typical example of such a probability might satisfy a differential equation, as, for example, if the particle is diffusing:

$$
\frac{\partial P(x, t)}{\partial t} = - \nabla^2 P(x, t)
$$

### 3. Section: 3. SIMULATING PROBABILITY

**Context:** If we had computed this probability, we would still have to do the integration

$$
P_A(x_A) = \int P(x_A, x_B) dx_B
$$

### 4. Section: 3. SIMULATING PROBABILITY

**Context:** It satisfies an equation such that at each jump in time

$$
P_{i+1}(\{s\}) = \sum_{\{s'\}} \left[ \prod_i m(s_i | s'_j, s'_k \ldots) \right] P_i(\{s'\})
$$

### 5. Section: 4. QUANTUM COMPUTERS—UNIVERSAL QUANTUM SIMULATORS

**Context:** The mathematics of the quantum mechanical operators associated with that point would be very simple.

$$
\begin{array}{l}
a = \text{ANNIHILATE} = \begin{array}{c|c|c}
\text{OCC} & \text{ON} & \\
\text{ON} & 0 & 0 \\
\hline
\text{ON} & 1 & 0
\end{array}
= \frac{1}{2}(\sigma_x - i\sigma_y) \\
a^* = \text{CREATE} = \begin{array}{c|c|c}
\hline 0 & 1 & \\
\hline 0 & 0 &
\end{array}
= \frac{1}{2}(\sigma_x + i\sigma_y) \\
n = \text{NUMBER} = \begin{array}{c|c|c}
\hline 1 & 0 & \\
\hline 0 & 0 &
\end{array}
= a^*a = \frac{1}{2}(1 + \sigma_z) \\
\mathbb{1} = \text{IDENTITY} = \begin{array}{c|c|c}
\hline 1 & 0 & \\
\hline 0 & 1 &
\end{array}
\end{array}
$$

### 6. Section: 4. QUANTUM COMPUTERS—UNIVERSAL QUANTUM SIMULATORS

**Context:** They have invented another set of matrices, the Pauli $\sigma$ matrices:

$$
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \mathbb{1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

### 7. Section: 5. CAN QUANTUM SYSTEMS BE PROBABILISTICALLY SIMULATED BY A CLASSICAL COMPUTER?

**Context:** And so with a slight increase in the complexity of the equations (and not very much increase) I turn to the density matrix, which for a single particle of coordinate $x$ in a pure state of wave function $\psi(x)$ is

$$
\rho(x, x') = \psi^*(x)\psi(x')
$$

### 8. Section: 5. CAN QUANTUM SYSTEMS BE PROBABILISTICALLY SIMULATED BY A CLASSICAL COMPUTER?

**Context:** For example if a state $\psi(x)$ is not certain but is $\psi \alpha$ with the probability $p \alpha$ then the density matrix is the appropriate weighted sum of the matrix for each state $\alpha$:

$$
\rho(x, x') = \sum_\alpha p_\alpha \psi_\alpha^*(x)\psi a(x').
$$

### 9. Section: 5. CAN QUANTUM SYSTEMS BE PROBABILISTICALLY SIMULATED BY A CLASSICAL COMPUTER?

**Context:** A quantity which has properties even more similar to classical probabilities is the Wigner function, a simple reexpression of the density matrix; for a

$$W(x, p) = \int \rho \left( x + \frac{y}{2}, x - \frac{y}{2} \right) e^{ipy} dy$$

### 10. Section: 5. CAN QUANTUM SYSTEMS BE PROBABILISTICALLY SIMULATED BY A CLASSICAL COMPUTER?

**Context:** For example, if you would like to know whether the first index is positive, the probability of that would be

$$\text{Prob(first index is } +) = f_{++} + f_{+-} \quad [\text{spin } z \text{ up}]$$

### 11. Section: 5. CAN QUANTUM SYSTEMS BE PROBABILISTICALLY SIMULATED BY A CLASSICAL COMPUTER?

**Context:** Or the probability that there's no match between the indices, that they're different,

$$
\operatorname{Prob}(\text{no match}) = f_{+-} + f_{-+} \quad [\text{spin } y \text{ down}]
$$

### 12. Section: 6. NEGATIVE PROBABILITIES

**Context:** Now, for many interacting spins on a lattice we can give a 'probability' (the quotes remind us that there is still a question about whether it's a probability) for correlated possibilities:

$$
F(s_1, s_2, \dots, s_N) \quad (s_i \in \{++, +-, -+, --\})
$$

### 13. Section: 6. NEGATIVE PROBABILITIES

**Context:** Next, if I look for the quantum mechanical equation which tells me what the changes of $F$ are with time, they are exactly of the form that I wrote above for the classical theory:

$$
F_{i+1}(\{s\}) = \sum_{(s')} \left[ \prod_i M(s_i | s'_j, s'_k \dots) \right] F_i(\{s'\})
$$

### 14. Section: 6. NEGATIVE PROBABILITIES

**Context:** The $M$, the 'probability' (so-called) of moving from one condition to another is itself not positive; if I had gone all the way back to the $f$ for a single object, it again is not necessarily positive.

$$
f_{++} = 0.6 \quad f_{+-} = -0.1 \quad f_{-+} = 0.3 \quad f_{--} = 0.2
$$

### 15. Section: 8. TWO-PHOTON CORRELATION EXPERIMENT

**Context:** Quantum theory and experiment agree that the probability $P {OO}$ that both of us detect an ordinary photon is

$$P_{OO} = \frac{1}{2} \cos^2(\phi_2 - \phi_1)$$

### 16. Section: 8. TWO-PHOTON CORRELATION EXPERIMENT

**Context:** If $p {\alpha\beta}$ is the conjoint probability to find the condition pair $\alpha, \beta$, the probability $P {OO}$ that both of us observe $O$ rays is

$$
P_{OO}(\phi_1, \phi_2) = \sum_{\alpha\beta} p_{\alpha\beta} f_\alpha(\phi_1) g_\beta(\phi_2) \quad \sum_{\alpha\beta} p_{\alpha\beta} = 1
$$

### 17. Section: 8. TWO-PHOTON CORRELATION EXPERIMENT

**Context:** If $p {\alpha\beta}$ is the conjoint probability to find the condition pair $\alpha, \beta$, the probability $P {OO}$ that both of us observe $O$ rays is

$$
P_{OE}(\phi_1, \phi_2) = \sum_{\alpha\beta} p_{\alpha\beta} (1 - f_\alpha(\phi_1)) g_\beta(\phi_2) \quad \text{etc.}
$$

### 18. Section: 9. DISCUSSION

**Context:** Answer: No, they are the same. $P {OO}$ is the joint probability that both you and I observe an ordinary ray, and $P {EE}$ is the joint probability for two

$$
P_{OO} + P_{EE} = \cos^2 30^\circ = 3/4
$$

## Figures and image references

### 1. 2. SIMULATING TIME

![img-0.jpeg](img-0.jpeg)

**Context:** And then we could say that a 'computer' rule (now computer would be in quotes, because it's not the standard kind of computer which operates in time) is: We have a state $s i$ at each point $i$ in space-time. (See Figure 1.) The state $s i$ at the space time point $i$ is a given function $F i(s j, s k, \ldots)$ of the state at the points $j, k$ in some neighborhood of $i$:

### 2. 7. POLARIZATION OF PHOTONS—TWO-STATES SYSTEMS

![img-1.jpeg](img-1.jpeg)

**Context:** And then the extraordinary ray from the first one comes out as the $E-O$ ray, and then there's an $E-E$ ray, alright.

### 3. 7. POLARIZATION OF PHOTONS—TWO-STATES SYSTEMS

![img-2.jpeg](img-2.jpeg)

**Context:** And then the extraordinary ray from the first one comes out as the $E-O$ ray, and then there's an $E-E$ ray, alright.

### 4. 8. TWO-PHOTON CORRELATION EXPERIMENT

![img-3.jpeg](img-3.jpeg)

**Context:** The probability $P {OE}$ that I find $O$ and you find $E$ is

### 5. 8. TWO-PHOTON CORRELATION EXPERIMENT

![img-4.jpeg](img-4.jpeg)

**Context:** With what probability would we get the same result, that they're

## Important tables

No Markdown tables were found in the text.
## Results and significance

- Question: Just to interpret, you spoke first of the probability of A given B, versus the probability of A and B jointly—that's the probability of one observer seeing the result, assigning a probability to the other; and then you brought up the paradox of the quantum mechanical result being $3/4$, and this being $2/3$.
- Then you go and you say, Now can I imitate that with a device which is going to produce the same results, and which will operate locally, and you try to invent some kind of way of doing that, and if you do it in the ordinary way of thinking, you find that you can't get there with the same probability.
- Therefore some new kind of thinking is necessary, but physicists, being kind of dull minded, only look at nature, and don't know how to think in these new ways.
- And yet it seems to me that there are some differences between things like space and time, and probability that might exist at some place, or energy, or some field value.
- Because the laws of physics as written now have, in the classical limit, a continuous variable everywhere, space and time.
- If, for example, in your theory you were going to have an electric field, then the electric field could not have (if it's going to be imitable, computable by a finite number of elements) an
- Because you see, if you would imagine that the electric field is coming out of some ‘ones’ or something, the lowest you could get would be a full one, but that’s what we see, you get a full photon.
- All these things suggest that it’s really true, somehow, that the physical world is representable in a discretized way, because every time you get into a bind like this, you discover that the experiment does just what’s necessary to escape the trouble that would come if the electric field went to zero, or you’d never be able to see a star beyond a certain distance, because the field would have gotten below the number of digits that your world can carry.

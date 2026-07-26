Simulating Physics with Computers

477

possible to classical equations so that we can see what the difficulty is and what happens. Well, first of all we can't simulate $\psi$ in the normal way. As I've explained already, there're too many variables. Our only hope is that we're going to simulate probabilities, that we're going to have our computer do things with the same probability as we observe in nature, as calculated by the quantum mechanical system. Can you make a cellular automaton, or something, imitate with the same probability what nature does, where I'm going to suppose that quantum mechanics is correct, or at least after I discretize space and time it's correct, and see if I can do it. I must point out that you must directly generate the probabilities, the results, with the correct quantum probability. Directly, because we have no way to store all the numbers, we have to just imitate the phenomenon directly.

It turns out then that another thing, rather than the wave function, a thing called the *density matrix*, is much more useful for this. It's not so useful as far as the mathematical equations are concerned, since it's more complicated than the equations for $\psi$, but I'm not going to worry about mathematical complications, or which is the easiest way to calculate, because with computers we don't have to be so careful to do it the very easiest way. And so with a slight increase in the complexity of the equations (and not very much increase) I turn to the density matrix, which for a single particle of coordinate $x$ in a pure state of wave function $\psi(x)$ is

$$
\rho(x, x') = \psi^*(x)\psi(x')
$$

This has a special property that is a function of two coordinates $x, x'$. The presence of two quantities $x$ and $x'$ associated with each coordinate is analogous to the fact that in classical mechanics you have to have two variables to describe the state, $x$ and $\hat{x}$. States are described by a second-order device, with two informations ('position' and 'velocity'). So we have to have two pieces of information associated with a particle, analogous to the classical situation, in order to describe configurations. (I've written the density matrix for one particle, but of course there's the analogous thing for $R$ particles, a function of $2R$ variables).

This quantity has many of the mathematical properties of a probability. For example if a state $\psi(x)$ is not certain but is $\psi_\alpha$ with the probability $p_\alpha$ then the density matrix is the appropriate weighted sum of the matrix for each state $\alpha$:

$$
\rho(x, x') = \sum_\alpha p_\alpha \psi_\alpha^*(x)\psi a(x').
$$

A quantity which has properties even more similar to classical probabilities is the Wigner function, a simple reexpression of the density matrix; for a
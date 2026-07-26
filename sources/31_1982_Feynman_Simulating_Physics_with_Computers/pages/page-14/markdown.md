480

Feynman

Next, if I look for the quantum mechanical equation which tells me what the changes of $F$ are with time, they are exactly of the form that I wrote above for the classical theory:

$$
F_{i+1}(\{s\}) = \sum_{(s')} \left[ \prod_i M(s_i | s'_j, s'_k \dots) \right] F_i(\{s'\})
$$

but now we have $F$ instead of $P$. The $M(s_i | s'_j, s'_k \dots)$ would appear to be interpreted as the 'probability' per unit time, or per time jump, that the state at $i$ turns into $s_i$ when the neighbors are in configuration $s'$. If you can invent a probability $M$ like that, you write the equations for it according to normal logic, those are the correct equations, the real, correct, quantum mechanical equations for this $F$, and therefore you'd say, Okay, so I can imitate it with a probabilistic computer!

There's only one thing wrong. These equations unfortunately cannot be so interpreted on the basis of the so-called 'probability', or this probabilistic computer can't simulate them, because the $F$ is not necessarily positive. Sometimes it's negative! The $M$, the 'probability' (so-called) of moving from one condition to another is itself not positive; if I had gone all the way back to the $f$ for a single object, it again is not necessarily positive.

An example of possibilities here are

$$
f_{++} = 0.6 \quad f_{+-} = -0.1 \quad f_{-+} = 0.3 \quad f_{--} = 0.2
$$

The sum $f_{++} + f_{+-}$ is 0.5, that's 50% chance of finding the first index positive. The probability of finding the first index negative is the sum $f_{-+} + f_{-+}$ which is also 50%. The probability of finding the second index positive is the sum $f_{++} + f_{-+}$ which is nine tenths, the probability of finding it negative is $f_{+-} + f_{--}$ which is one-tenth, perfectly alright, it's either plus or minus. The probability that they match is eight-tenths, the probability that they mismatch is plus two-tenths; every physical probability comes out positive. But the original $f$'s are not positive, and therein lies the great difficulty. The only difference between a probabilistic classical world and the equations of the quantum world is that somehow or other it appears as if the probabilities would have to go negative, and that we do not know, as far as I know, how to simulate. Okay, that's the fundamental problem. I don't know the answer to it, but I wanted to explain that if I try my best to make the equations look as near as possible to what would be imitable by a classical probabilistic computer, I get into trouble.
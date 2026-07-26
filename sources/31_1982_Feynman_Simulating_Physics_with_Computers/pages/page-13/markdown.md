Simulating Physics with Computers

479

These two formulas are exactly correct in quantum mechanics. You see I'm hedging on whether or not 'probability' $f$ can really be a probability without quotes. But when I write probability without quotes on the left-hand side I'm not hedging; that really is the quantum mechanical probability. It's interpreted perfectly fine here. Likewise the probability that the second index is positive can be obtained by finding

$$
\operatorname{Prob}(\text{second index is } +) = f_{++} + f_{-+} \quad [\text{spin } x \text{ up}]
$$

and likewise

$$
\operatorname{Prob}(\text{second index is } -) = f_{+-} + f_{--} \quad [\text{spin } x \text{ down}]
$$

You could also ask other questions about the system. You might like to know, What is the probability that both indices are positive? You'll get in trouble. But you could ask other questions that you won't get in trouble with, and that get correct physical answers. You can ask, for example, what is the probability that the two indices are the same? That would be

$$
\operatorname{Prob}(\text{match}) = f_{++} + f_{--} \quad [\text{spin } y \text{ up}]
$$

Or the probability that there's no match between the indices, that they're different,

$$
\operatorname{Prob}(\text{no match}) = f_{+-} + f_{-+} \quad [\text{spin } y \text{ down}]
$$

All perfectly all right. All these probabilities are correct and make sense, and have a precise meaning in the spin model, shown in the square brackets above. There are other 'probability' combinations, other linear combinations of these $f$'s which also make physically sensible probabilities, but I won't go into those now. There are other linear combinations that you can ask questions about, but you don't seem to be able to ask questions about an individual $f$.

## 6. NEGATIVE PROBABILITIES

Now, for many interacting spins on a lattice we can give a 'probability' (the quotes remind us that there is still a question about whether it's a probability) for correlated possibilities:

$$
F(s_1, s_2, \dots, s_N) \quad (s_i \in \{++, +-, -+, --\})
$$
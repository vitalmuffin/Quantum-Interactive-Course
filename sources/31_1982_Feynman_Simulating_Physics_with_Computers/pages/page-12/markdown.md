478

Feynman

single particle

$$W(x, p) = \int \rho \left( x + \frac{y}{2}, x - \frac{y}{2} \right) e^{ipy} dy$$

We shall be emphasizing their similarity and shall call it “probability” in quotes instead of Wigner function. Watch these quotes carefully, when they are absent we mean the real probability. If “probability” had all the mathematical properties of a probability we could remove the quotes and simulate it. $W(x, p)$ is the “probability” that the particle has position $x$ and momentum $p$ (per $dx$ and $dp$). What properties does it have that are analogous to an ordinary probability?

It has the property that if there are many variables and you want to know the “probabilities” associated with a finite region, you simply disregard the other variables (by integration). Furthermore the probability of finding a particle at $x$ is $\int W(x, p)dp$. If you can interpret $W$ as a probability of finding $x$ and $p$, this would be an expected equation. Likewise the probability of $p$ would be expected to be $\int W(x, p)dx$. These two equations are correct, and therefore you would hope that maybe $W(x, p)$ is the probability of finding $x$ and $p$. And the question then is can we make a device which simulates this $W$? Because then it would work fine.

Since the quantum systems I noted were best represented by spin one-half (occupied versus unoccupied or spin one-half is the same thing), I tried to do the same thing for spin one-half objects, and it’s rather easy to do. Although before one object only had two states, occupied and unoccupied, the full description—in order to develop things as a function of time—requires twice as many variables, which mean two slots at each point which are occupied or unoccupied (denoted by $+$ and $-$ in what follows), analogous to the $x$ and $\hat{x}$, or the $x$ and $p$. So you can find four numbers, four “probabilities” $\{f_{++}, f_{+-}, f_{-+}, f_{--}\}$ which act just like, and I have to explain why they’re not exactly like, but they act just like, probabilities to find things in the state in which both symbols are up, one’s up and one’s down, and so on. For example, the sum $f_{++} + f_{+-} + f_{-+} + f_{--}$ of the four “probabilities” is 1. You’ll remember that one object now is going to have two indices, two plus/minus indices, or two ones and zeros at each point, although the quantum system had only one. For example, if you would like to know whether the first index is positive, the probability of that would be

$$\text{Prob(first index is } +) = f_{++} + f_{+-} \quad [\text{spin } z \text{ up}]$$

i.e., you don’t care about the second index. The probability that the first index is negative is

$$\text{Prob(first index is } -) = f_{-+} + f_{--}, \quad [\text{spin } z \text{ down}]$$
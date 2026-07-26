Simulating Physics with Computers

473

or minus the square root of $n$ and all that) as it happens in nature. In other words, we could imagine and be perfectly happy, I think, with a probabilistic simulator of a probabilistic nature, in which the machine doesn't exactly do what nature does, but if you repeated a particular type of experiment a sufficient number of times to determine nature's probability, then you did the corresponding experiment on the computer, you'd get the corresponding probability with the corresponding accuracy (with the same kind of accuracy of statistics).

So let us now think about the characteristics of a local probabilistic computer, because I'll see if I can imitate nature with that (by 'nature' I'm now going to mean quantum mechanics). One of the characteristics is that you can determine how it behaves in a local region by simply disregarding what it's doing in all other regions. For example, suppose there are variables in the system that describe the whole world $(x_A, x_B)$—the variables $x_A$ you're interested in, they're 'around here'; $x_B$ are the whole result of the world. If you want to know the probability that something around here is happening, you would have to get that by integrating the total probability of all kinds of possibilities over $x_B$. If we had *computed* this probability, we would still have to do the integration

$$
P_A(x_A) = \int P(x_A, x_B) dx_B
$$

which is a hard job! But if we have *imitated* the probability, it's very simple to do it: you don't have to do anything to do the integration, you simply disregard what the values of $x_B$ are, you just look at the region $x_A$. And therefore it does have the characteristic of nature: if it's local, you can find out what's happening in a region not by integrating or doing an extra operation, but merely by disregarding what happens elsewhere, which is no operation, nothing at all.

The other aspect that I want to emphasize is that the equations will have a form, no doubt, something like the following. Let each point $i = 1, 2, \ldots, N$ in space be in a state $s_i$ chosen from a small state set (the size of this set should be reasonable, say, up to $2^5$). And let the probability to find some configuration $\{s_i\}$ (a set of values of the state $s_i$ at each point $i$) be some number $P(\{s_i\})$. It satisfies an equation such that at each jump in time

$$
P_{i+1}(\{s\}) = \sum_{\{s'\}} \left[ \prod_i m(s_i | s'_j, s'_k \ldots) \right] P_i(\{s'\})
$$

where $m(s_i | s'_j, s'_k \ldots)$ is the probability that we move to state $s_i$ at point $i$
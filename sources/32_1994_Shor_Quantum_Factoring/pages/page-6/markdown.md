in polynomial time on a quantum machine. This leaves the machine in state

$$\frac{1}{(p-1)^2} \sum_{a,b,c,d=0}^{p-2} \exp \left( \frac{2\pi i}{p-1} (ac+bd) \right) |c, d, g^a x^{-b} \pmod{p} \tag{4.3}$$

We now compute the probability that the computation ends with the machine in state $|c, d, y\rangle$ with $y \equiv g^k \pmod{p}$. This probability is the absolute value of the square of the sum over all ways the machine could produce this state, or

$$\left| \frac{1}{(p-1)^2} \sum_{\substack{a,b \\ a-rb \equiv k}} \exp \left( \frac{2\pi i}{p-1} (ac+bd) \right) \right|^2, \tag{4.4}$$

where the sum is over all $a, b$ satisfying $a - rb \equiv k \pmod{p-1}$. This condition arises from the fact that computational paths can only interfere when they give the same $y \equiv g^{a-rb} \equiv g^k \pmod{p}$. We now substitute the equation $a \equiv k + rb \pmod{p-1}$ in the above exponential. The above sum then reduces to

$$\left| \frac{1}{(p-1)^2} \sum_{b=0}^{p-2} \exp \left( \frac{2\pi i}{p-1} (kc + b(d+rc)) \right) \right|^2. \tag{4.5}$$

However, if $d+rc \not\equiv 0 \pmod{p-1}$ the above sum is over a set of $(p-1)^{\text{st}}$ roots of unity evenly spaced around the unit circle, and thus the probability is 0. If $d \equiv -rc$ the above sum is over the same root of unity $p-1$ times, giving $(p-1)e^{2\pi i k c / (p-1)}$, so the probability is $1 / (p-1)^2$. We can check that these probabilities add up to one by counting that there are $(p-1)^2$ states $|c, -rc, y\rangle$ since there are $p-1$ choices of $c \pmod{p-1}$ and $p-1$ choices of $y \not\equiv 0 \pmod{p}$.

Our computation thus produces a random $c \pmod{p-1}$ and the corresponding $d \equiv -rc \pmod{p-1}$. If $c$ and $p-1$ are relatively prime, we can find $r$ by division. Because we are choosing among all possible $c$'s with equal probability, the chance that $c$ and $p-1$ are relatively prime is $\phi(p-1)/(p-1)$, where $\phi$ is the Euler $\phi$-function. It is easy to check that $\phi(p-1)/(p-1) > 1/\log(p)$. (Actually, from [17, Theorem 328], limit $\phi(p-1)/(p-1) \approx e^{-\gamma}/\log \log p$.) Thus we only need a number of experiments that is polynomial in $\log p$ to obtain $r$ with high probability. In fact, we can find a set of $c$'s such that at least one is relatively prime to every prime divisor of $p-1$ by repeating the experiment only an expected constant number of times. This would also give us enough information to obtain $r$.

## 5 A note on precision

The number of bits of precision needed in the amplitude of quantum mechanical computers could be a barrier to practicality. The generally accepted theoretical dividing line between feasible and infeasible is that polynomial precision (i.e., a number of bits logarithmic in the problem size) is feasible and that more is infeasible. This is because on a quantum computer the phase angle would need to be obtained through some physical device, and constructing such devices with better than polynomial precision seems unquestionably impractical. In fact, even polynomial precision may prove to be impractical; however, using this as the theoretical dividing line results in nice theoretical properties.

We thus need to show that the computations in the previous section need to use only polynomial precision in the amplitudes. The very act of writing down the expression $\exp(2\pi i a c / (p-1))$ seems to imply that we need exponential precision, as this phase angle is exponentially precise. Fortunately, this is not the case. Consider the same matrix $A_{p-1}$ with every term $\exp(2\pi i a c / (p-1))$ replaced by $\exp(2\pi i a c / (p-1) \pm \pi i / 20)$. Each positive case, i.e., one resulting in $d \equiv -rc$, will still occur with nearly as large probability as before; instead of adding $p-1$ amplitudes which have exactly the same phase angle, we add $p-1$ amplitudes which have nearly the same phase angle, and thus the size of the sum will only be reduced by a constant factor. The algorithm will thus give a $(c, d)$ with $d \equiv -rc$ with constant probability (instead of probability 1).

Recall that we obtain the matrix $A_{p-1}$ by multiplying at most $\log p$ matrices $A_{q_i}$. Further, each entry in $A_{p-1}$ is the product of at most $\log p$ terms. Suppose that each phase angle were off by at most $\epsilon / \log p$ in the $A_{q_i}$'s. Then in the product, each phase angle would be off by at most $\epsilon$, which is enough to perform the computation with constant probability of success. A similar argument shows that the magnitude of the amplitudes in the $A_{q_i}$ can be off by a polynomial fraction. Similar arguments hold for the general case of discrete log and for factoring to show that we need only polynomial precision for the amplitudes in these cases as well.

We still need to show how to construct $A_{q_i}$ from constant size unitary matrices having limited precision. The arguments are much the same as above, but we will not give them in this paper because, in fact, Bennett et al. [4] have shown that it is sufficient to use polynomial precision for any computation on a quantum Turing machine to obtain the answer with high probability.

Since precision could easily be the limiting factor for practicality of quantum computation, it might be advisable to investigate how much precision is actually needed for

129
where $j$ is the closest integer to $T/q$, then as $b$ varies between 0 and $p - 2$, the phase of the first exponential term in Eq. (7.6) only varies over at most half of the unit circle. Further, if

$$|\{c(p - 1)\}_q| \le q/20, \tag{7.10}$$

then $|V|$ is always at most $q/20$, so the phase of the second exponential term in Eq. (7.6) never is farther than $\exp(\pi i/10)$ from 1. By combining these two observations, we will show that if both conditions hold, then the contribution to the probability from the corresponding term is significant. Furthermore, both conditions will hold with constant probability, and a reasonable sample of $c$'s for which Condition (7.9) holds will allow us to deduce $r$.

We now give a lower bound on the probability of each good output, i.e., an output that satisfies Conditions (7.9) and (7.10). We know that as $b$ ranges from 0 to $p - 2$, the phase of $\exp(2\pi i U/q)$ ranges from 0 to $2\pi i W$ where

$$W = \frac{p - 2}{q} \left( rc + d - \frac{r}{p-1} \{c(p - 1)\}_q - jq \right) \tag{7.11}$$

and $j$ is as in Eq. (7.9). Thus, the component of the amplitude of the first exponential in Eq. (7.6) in the direction

$$\exp(\pi i W) \tag{7.12}$$

is at least $\cos(2\pi |W/2 - Wb/(p - 2)|)$. Now, by Condition (7.10), the phase can vary by at most $\pi i/10$ due to the second exponential $\exp(2\pi i V/q)$. Applying this variation in the manner that minimizes the component in the direction (7.12), we get that the component in this direction is at least $\cos(2\pi |W/2 - Wb/(p - 2)| + \pi/10)$. Since $p < q$, and from Condition (7.9), $|W| \le 1/2$, putting everything together, the probability of arriving at a state $|c, d, y)$ that satisfies both Condition (7.9) and (7.10) is at least

$$\left( \frac{1}{q} \frac{2}{\pi} \int_{\pi/10}^{7\pi/20} \cos t \, dt \right)^2, \tag{7.13}$$

or at least $.137/q^2$.

We will now count the number of pairs $(c, d)$ satisfying Conditions (7.9) and (7.10). The number of pairs $(c, d)$ such that (7.9) holds is exactly the number of possible $c$'s, since for every $c$ there is exactly one $d$ such that (7.9) holds (round off the fraction to the nearest integer to obtain this $d$). The number of $c$'s for which (7.10) holds is approximately $q/10$. Thus, there are $q/10$ pairs $(c, d)$ satisfying both conditions. Multiplying by $p - 1$, which is the number of possible $y$'s, gives approximately $pq/10$ states $|c, d, y)$. Combining this calculation with the lower bound on the probability of each good state gives us that the probability of obtaining any good state is at least $p/80q$, or at least $1/160$ (since $q < 2p$).

We now want to recover $r$ from a pair $c, d$ such that

$$-\frac{1}{2q} \le \frac{d}{q} + \frac{r}{q} \left( c - \frac{\{c(p - 1)\}_q}{p - 1} \right) \le \frac{1}{2q} \pmod{1}, \tag{7.14}$$

where this equation was obtained from Condition (7.9) by dividing by $q$. The first thing to notice is that the multiplier on $r$ is a fraction with denominator $p - 1$, since $q$ evenly divides $c(p - 1) - \{c(p - 1)\}_q$. Thus, we need only round $d/q$ off to the nearest multiple of $1/(p - 1)$ and divide $(\mod p - 1)$ by

$$c' = \frac{c(p - 1) - \{c(p - 1)\}_q}{q} \tag{7.15}$$

to find a candidate $r$. To show that this experiment need only be repeated a polynomial number of times to find the correct $r$ requires only a few more details. The problem is again that we cannot divide by a number which is not relatively prime to $p - 1$.

For the general case of the discrete log algorithm, we do not know that all possible values of $c'$ are generated with reasonable likelihood; we only know this about one-tenth of them. This additional difficulty makes the next step harder than the corresponding step in the two previous algorithms. If we knew the remainder of $r$ modulo all prime powers dividing $p - 1$, we could use the Chinese remainder theorem to recover $r$ in polynomial time. We will only be able to find this remainder for primes larger than 20, but with a little extra work we will still be able to recover $r$.

What we have is that each good $(c, d)$ pair is generated with probability at least $.137p/q > 1/16q$, and that at least a tenth of the possible $c$'s are in a good $(c, d)$ pair. From Eq. (7.15), it follows that these $c$'s are mapped from $c/q$ to $c'/(p - 1)$ by rounding to the nearest integer multiple of $1/(p - 1)$. Further, the good $c$'s are exactly those in which $c/q$ is close to $c'/(p - 1)$. Thus, each good $c$ corresponds with exactly one $c'$. We would like to show that for any prime power $p_t^{n_t}$ dividing $p - 1$, a random good $c'$ is unlikely to contain $p_t$. If we are willing to accept a large constant for the algorithm, we can just ignore the prime powers under 20; if we know $r$ modulo all prime powers over 20, we can try all possible residues for primes under 20 with only a (large) constant factor increase in running time. Because at least one tenth of the $c$'s were in a good $(c, d)$ pair, at least one tenth of the $c'$'s are good. Thus, for a prime power $p_t^{n_t}$, a random good $c'$ is divisible by $p_t^{n_t}$ with probability at most $10/p_t^{n_t}$. If we have $t$ good $c'$'s, the probability of having a prime power over 20 that divides all of them is therefore at most

$$\sum_{\substack{p_t^{n_t} > 20 \\ p_t^{n_t} \le p - 1}} \left( \frac{10}{p_t^{n_t}} \right)^t, \tag{7.16}$$

132
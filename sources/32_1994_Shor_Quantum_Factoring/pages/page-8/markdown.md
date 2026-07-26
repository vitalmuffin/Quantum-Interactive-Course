i.e., if there is a $d$ such that

$$\frac{-r}{2} \leq rc - dq \leq \frac{r}{2}. \tag{6.9}$$

Dividing by $rq$ and rearranging the terms gives

$$\left| \frac{c}{q} - \frac{d}{r} \right| \leq \frac{1}{2q}. \tag{6.10}$$

We know $c$ and $q$. Because $q \geq 2n^2$, there is at most one fraction $d/r$ with $r < n$ that satisfies the above inequality. Thus, we can obtain the fraction $d/r$ in lowest terms by rounding $c/q$ to the nearest fraction having a denominator smaller than $n$. This fraction can be found in polynomial time by using a continued fraction expansion of $c/q$, which finds all the best approximations of $c/q$ by fractions [17, Chapter X].

If we have the fraction $d/r$ in lowest terms, and if $d$ happens to be relatively prime to $r$, this will give us $r$. We will now count the number of states $|c, x^k \pmod{n}\rangle$ which enable us to compute $r$ in this way. There are $\phi(r)$ possible values for $d$ relatively prime to $r$, where $\phi$ is Euler's $\phi$ function. Each of these fractions $d/r$ is close to one fraction $c/q$ with $|c/q - d/r| \leq 1/2q$. There are also $r$ possible values for $x^k$, since $r$ is the order of $x$. Thus, there are $r\phi(r)$ states $|c, x^k \pmod{n}\rangle$ which would enable us to obtain $r$. Since each of these states occurs with probability at least $1/3r^2$, we obtain $r$ with probability at least $\phi(r)/3r$. Using the theorem that $\phi(r)/r > k/\log \log r$ for some fixed $k$ [17, Theorem 328], this shows that we find $r$ at least a $k/\log \log r$ fraction of the time, so by repeating this experiment only $O(\log \log r)$ times, we are assured of a high probability of success.

Note that in the algorithm for order, we did not use many of the properties of multiplication (mod $n$). In fact, if we have a permutation $f$ mapping the set $\{0, 1, 2, \dots, n-1\}$ into itself such that its $k$th iterate, $f^{(k)}(a)$, is computable in time polynomial in $\log n$ and $\log k$, the same algorithm will be able to find the order of an element $a$ under $f$, i.e., the minimum $r$ such that $f^{(r)}(a) = a$.

## 7 Discrete log: the general case

For the general case, we first find a smooth number $q$ such that $q$ is close to $p$, i.e., with $p \leq q \leq 2p$ (see Lemma 3.2).

Next, we do the same thing as in the easy case, that is, we choose $a$ and $b$ uniformly (mod $p-1$), and then compute $g^a x^{-b} \pmod{p}$. This leaves our machine in the state

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b, g^a x^{-b} \pmod{p}\rangle. \tag{7.1}$$

As before, we use the Fourier transform $A_q$ to send $a \to c$ and $b \to d \pmod{q}$, with amplitude $\frac{1}{q} \exp(2\pi i(ac+bd)/q)$, giving us the state

$$\frac{1}{(p-1)q} \sum_{a,b=0}^{p-2} \sum_{c,d=0}^{q-1} \exp\left(\frac{2\pi i}{q}(ac+bd)\right) |c, d, g^a x^{-b} \pmod{p}\rangle. \tag{7.2}$$

Note that we now have two moduli to deal with, $p-1$ and $q$. While this makes keeping track of things more confusing, we will still be able to obtain $r$ using a algorithm similar to the easy case. The probability of observing a state $|c, d, y\rangle$ with $y \equiv g^k \pmod{p}$ is, almost as before,

$$\left| \frac{1}{(p-1)q} \sum_{\substack{a,b \\ a-rb \equiv k}} \exp\left(\frac{2\pi i}{q}(ac+bd)\right) \right|^2 \tag{7.3}$$

where the sum is over all $(a, b)$ such that $a - rb \equiv k \pmod{p-1}$. We now use the relation

$$a = br + k - (p-1) \left\lfloor \frac{br+k}{p-1} \right\rfloor \tag{7.4}$$

and substitute in the above expression to obtain the amplitude

$$\frac{1}{(p-1)q} \sum_{b=0}^{p-2} \exp\left(\frac{2\pi i}{q} (brc + kc + bd - c(p-1) \left\lfloor \frac{br+k}{p-1} \right\rfloor)\right). \tag{7.5}$$

The absolute value of the square of this amplitude is the probability of observing the state $|c, d, g^k \pmod{p}\rangle$. We will now analyze this expression. First, a factor of $\exp(2\pi ikc/q)$ can be taken out of all the terms and ignored, because it does not change the probability. Next, we split the exponent into two parts and factor out $b$ to obtain

$$\frac{1}{(p-1)q} \sum_{b=0}^{p-2} \exp\left(\frac{2\pi i}{q} U\right) \exp\left(\frac{2\pi i}{q} V\right), \tag{7.6}$$

where

$$\begin{array}{l} U = bT, \\ T = rc + d - \frac{r}{p-1} \{c(p-1)\}_q, \tag{7.7} \end{array}$$

and

$$V = \left(\frac{kr}{p-1} - \left\lfloor \frac{br+k}{p-1} \right\rfloor\right) \{c(p-1)\}_q. \tag{7.8}$$

Here by $\{z\}_q$ we mean the residue of $z \pmod{q}$ with $-q/2 < \{z\}_q \leq q/2$. We will show that if we get enough "good" outputs, then we still can deduce $r$, and that furthermore, the chance of getting a "good" output is constant. The idea is that if

$$|\{T\}_q| = |rc + d - \frac{r}{p-1} \{c(p-1)\}_q - jq| \leq \frac{1}{2}, \tag{7.9}$$

131
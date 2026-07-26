quantum algorithms. Although Bernstein and Vazirani [4] show that the number of bits of precision needed is never more than the logarithm of the number of computational steps a quantum computer takes, in some algorithms it could conceivably require less. Interesting open questions are whether it is possible to do discrete logarithms or factoring with less than polynomial precision and whether some tradeoff between precision and time is possible.

## 6 Factoring

The algorithm for factoring is similar to the one for the general case of discrete log, only somewhat simpler. I present this algorithm before the general case of discrete log so as to give the three algorithms in this paper in order of increasing complexity. Readers interested in discrete log may skip to the next section.

Instead of giving a quantum computer algorithm to factor n, we will give a quantum computer algorithm for finding the order of an element x in the multiplicative group (mod n); that is, the least integer r such that  \( x^{r} \equiv 1 \pmod{n} \) . There is a randomized reduction from factoring to the order of an element [23].

To factor an odd number n, given a method for computing the order of an element, we choose a random x, find the order  \( r_{x} \)  of x, and compute  \( \gcd(x^{r_{x}/2}-1,n) \) . This fails to give a non-trivial divisor of n only if  \( r_{x} \)  is odd or if  \( x^{r_{x}/2}\equiv-1\pmod{n} \) . Using this criterion, it can be shown that the algorithm finds a factor of n with probability at least  \( 1-1/2^{k} \) , where k is the number of distinct prime factors of n. This scheme will thus work as long as n is not a prime power; however, factoring prime powers can be done efficiently with classical methods.

Given x and n, to find r such that  \( x^{r} \equiv 1 \pmod{n} \) , we do the following. First, we find a smooth q with  \( 2n^{2} \leq q < 4n^{2} \) . Next, we put our machine in the uniform superposition of states representing numbers  \( a \pmod{q} \) . This leaves our machine in state

\[
\frac {1}{q ^ {1 / 2}} \sum_ {a = 0} ^ {q - 1} | a \rangle . \tag {6.1}
\]

As in the algorithm for discrete log, we will not write n, x, or q in the state of our machine, because we never change these values.

Next, we compute \( x^a \pmod{n} \). Since we keep \( x \) and \( a \) on the tape, this can be done reversibly. This leaves our machine in the state

\[
\frac {1}{q ^ {1 / 2}} \sum_ {a = 0} ^ {q - 1} | a, x ^ {a} (\mathrm{mod} n) \rangle . \tag {6.2}
\]

We then perform our Fourier transform \(A_{q}\) mapping \(a \to c\)

with amplitude \(\frac{1}{q^{1/2}}\exp(2\pi iac/q)\). This leaves our machine in state

\[
\frac {1}{q} \sum_ {a = 0} ^ {q - 1} \exp (2 \pi i a c / q) | c, x ^ {a} (\mathrm{mod} n) \rangle . \tag {6.3}
\]

Finally, we observe the machine. It would be sufficient to observe solely the value of \( c \), but for clarity we will assume that we observe both \( c \) and \( x^a \pmod{n} \). We now compute the probability that our machine ends in a particular state \( |c, x^k \pmod{n}\rangle \), where we may assume \( 0 \leq k < r \). Summing over all possible ways to reach this state, we find that this probability is

\[
\left| \frac {1}{q} \sum_ {a: x ^ {a} \equiv x ^ {k}} \exp (2 \pi i a c / q) \right| ^ {2}. \tag {6.4}
\]

where the sum is over all \(a\), \(0 \leq a < q\), such that \(x^{a} \equiv x^{k} (\bmod n)\). Because the order of \(x\) is \(r\), this sum is equivalently over all \(a\) satisfying \(a \equiv k (\bmod r)\). Writing \(a = br + k\), we find that the above probability is

\[
\left| \frac {1}{q} \sum_ {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i (b r + k) c / q) \right| ^ {2}. \tag {6.5}
\]

We can ignore the term of \(\exp(2\pi ikc/q)\), as it can be factored out of the sum and has magnitude 1. We can also replace \(rc\) with \(\{rc\}_q\), where \(\{rc\}_q\) is the residue which is congruent to \(rc (\bmod q)\) and is in the range \(-q/2 < \{rc\}_q \leq q/2\). This leaves us with the expression

\[
\left| \frac {1}{q} \sum_ {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i b \{r c \} _ {q} / q) \right| ^ {2}. \tag {6.6}
\]

We will now show that if  \( \{rc\}_{q} \)  is small enough, all the amplitudes in this sum will be in nearly the same direction, giving a large probability. If  \( \{rc\}_{q} \)  is small with respect to q, we can use the change of variables t = b/q and approximate this sum with the integral

\[
\left| \int_ {0} ^ {\frac {1}{q} \lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i \{r c \} _ {q} t) d t \right| ^ {2}. \tag {6.7}
\]

If \( |\{rc\}_{q}| \leq r/2 \), this quantity can be shown to be asymptotically bounded below by \( 4/(\pi^{2}r^{2}) \), and thus at least \( 1/3r^{2} \). The probability of seeing a given state \( |c, x^{k} (\text{mod } n)\rangle \) will thus be at least \( 1/3r^{2} \) if

\[
\frac {- r}{2} \leq \{r c \} _ {q} \leq \frac {r}{2}, \tag {6.8}
\]

130
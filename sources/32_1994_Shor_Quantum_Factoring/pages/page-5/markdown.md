We can now define $C$ and $D$:

$$C(a, b) = \left\{ \begin{array}{cl} 0 & \text{if } \alpha_2 \neq \beta_1 \\ \frac{1}{q_1^{1/2}} \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1)} & \text{otherwise,} \end{array} \right. \tag{3.2}$$

and

$$D(b, c) = \left\{ \begin{array}{cl} 0 & \text{if } \beta_2 \neq \gamma_2 \\ \frac{1}{q_2^{1/2}} \omega^{\beta_1 \gamma_1 q_1 - \beta_1 \beta_2 u} & \text{otherwise.} \end{array} \right. \tag{3.3}$$

It is easy to see that $CD(a, c) = C(a, b)D(b, c)$ where $b = \alpha_2 q_1 + \gamma_2$ since we need $\alpha_2 = \beta_1$ and $\beta_2 = \gamma_2$ to ensure non-zero entries in $C(a, b)$ and $D(b, c)$. Now,

$$\begin{array}{l} CD(a, c) = \frac{1}{q_1^{1/2} q_2^{1/2}} \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1) + \beta_1 \gamma_1 q_1 - \beta_1 \beta_2 u} \\ = \frac{1}{q^{1/2}} \omega^{\alpha_1 \gamma_2 q_2 + \alpha_2 \gamma_1 q_1 + \alpha_2 \gamma_2} \\ = \frac{1}{q^{1/2}} \omega^{(\alpha_1 q_2 + \alpha_2)(\gamma_1 q_1 + \gamma_2)} \\ = \frac{1}{q^{1/2}} \omega^{ac} \tag{3.4} \end{array}$$

so $CD(a, c) = A_q(a, c)$.

We will now sketch how to rearrange the rows and columns of $C$ to get the matrix $\bigoplus_{q_2} A_{q_1}$. The matrix $C$ can be put in block-diagonal form where the blocks are indexed by $\alpha_2 = \beta_1$ (since all entries with $\alpha_2 \neq \beta_1$ are 0). Let $u + 1 \equiv tq_2 \pmod q$. Within a given block $\alpha_2 = \beta_1$, the entries look like

$$\begin{array}{l} \sqrt{q_1} C(a, b) = \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1)} \\ = \exp(2\pi i(\alpha_1 \beta_2 + \beta_1 \beta_2 t)q_2/q) \\ = \exp(2\pi i(\alpha_1 + \alpha_2 t)\beta_2/q_1). \tag{3.5} \end{array}$$

Thus, if we rearrange the rows within this block so that they are indexed by $\alpha' \equiv \alpha_1 + \alpha_2 t \pmod q_1$, we obtain the transformation $\alpha' \to \beta_2$ with amplitude $\frac{1}{q_1^{1/2}} \exp(2\pi i \alpha' \beta_2 / q_1)$; that is, the transformation given by the unitary matrix with the $(\alpha', \beta_2)$ entry equal to $\frac{1}{q_1^{1/2}} \exp(2\pi i \alpha' \beta_2 / q_1)$, which is $A_{q_1}$. The matrix $D$ can similarly be rearranged to obtain the matrix $\bigoplus_{q_1} A_{q_2}$.

We also need to show how to find a smooth $q$ that lies between $n$ and $2n$ in polynomial time. There are actually smooth $q$ much closer to $n$ than this, but this is all we need. It is not known how to find smooth numbers very close to $n$ in polynomial time.

Lemma 3.2 Given $n$, there is a polynomial-time algorithm to find a number $q$ with $n \le q < 2n$ such that no prime power larger than $c \log q$ divides $q$, for some constant $c$ independent of $n$.

Proof: To find such a $q$, multiply the primes $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdots p_k$ until the product is larger than $n$. Now, if this

product is larger than $2n$, divide it by the largest prime that keeps the number larger than $n$. This produces the desired $q$. There is always a prime between $m$ and $2m$ [17, Theorem 418], so $n \le q < 2n$. The prime number theorem [17, Theorem 6] and some calculation show that the largest prime dividing $q$ is of size $O(\log n)$.

Note that if we are using Coppersmith's transformation $A_{2^k}$ using the $2^k$th roots of unity, we set $q = 2^k$ where $k = \lfloor \log_2 n \rfloor + 1$.

## 4 Discrete log: the easy case

The discrete log problem is: given a prime $p$, a generator $g$ of the multiplicative group (mod $p$) and an $x$ (mod $p$), find an $r$ such that $g^r \equiv x \pmod p$. We will start by giving a polynomial-time algorithm for discrete log on a quantum computer in the case that $p - 1$ is smooth. This algorithm is analogous to the algorithm in Simon's paper [28], with the group $Z_2^k$ replaced by $Z_{p-1}$. The smooth case is not in itself an interesting accomplishment, since there are already polynomial time algorithms for classical computers in this case [24]; however, explaining this case is easier than explaining either the general case of discrete log or the factoring algorithm, and as the three algorithms are similar, this example will illuminate how the more complicated algorithms work.

We will start our algorithm with $x$, $g$ and $p$ on the tape (i.e., in the quantum memory of our machine). We are trying to compute $r$ such that $g^r \equiv x \pmod p$. Since we will never delete them, $x$, $g$, and $p$ are constants, and we will specify a state of our machine by the other contents of the tape.

The algorithm starts out by "choosing" numbers $a$ and $b$ (mod $p - 1$) uniformly, so the state of the machine after this step is

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b\rangle. \tag{4.1}$$

The algorithm next computes $g^a x^{-b} \pmod p$ reversibly, so we must keep the values $a$ and $b$ on the tape. The state of the machine is now

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b, g^a x^{-b} \pmod p\rangle. \tag{4.2}$$

What we do now is use the transformation $A_{p-1}$ to map $a \to c$ with amplitude $\frac{1}{(p-1)^{1/2}} \exp(2\pi i ac / (p-1))$ and $b \to d$ with amplitude $\frac{1}{(p-1)^{1/2}} \exp(2\pi i bd / (p-1))$. As was discussed in the previous section, this is a unitary transformation, and since $p - 1$ is smooth it can be accomplished

128
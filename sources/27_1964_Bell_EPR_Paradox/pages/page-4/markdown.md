198

J. S. BELL

Vol. 1, No. 3

It follows that $\vec{c}$ is another unit vector

$$\begin{array}{l} P(\vec{a}, \vec{b}) - P(\vec{a}, \vec{c}) = - \int d\lambda\rho(\lambda) [A(\vec{a}, \lambda) A(\vec{b}, \lambda) - A(\vec{a}, \lambda) A(\vec{c}, \lambda)] \\ = \int d\lambda\rho(\lambda) A(\vec{a}, \lambda) A(\vec{b}, \lambda) [A(\vec{b}, \lambda) A(\vec{c}, \lambda) - 1] \end{array}$$

using (1), whence

$$|P(\vec{a}, \vec{b}) - P(\vec{a}, \vec{c})| \leq \int d\lambda\rho(\lambda) [1 - A(\vec{b}, \lambda) A(\vec{c}, \lambda)]$$

The second term on the right is $P(\vec{b}, \vec{c})$, whence

$$1 + P(\vec{b}, \vec{c}) \geq |P(\vec{a}, \vec{b}) - P(\vec{a}, \vec{c})| \tag{15}$$

Unless $P$ is constant, the right hand side is in general of order $|\vec{b}-\vec{c}|$ for small $|\vec{b}-\vec{c}|$. Thus $P(\vec{b}, \vec{c})$ cannot be stationary at the minimum value ($-1$ at $\vec{b} = \vec{c}$) and cannot equal the quantum mechanical value (3).

Nor can the quantum mechanical correlation (3) be arbitrarily closely approximated by the form (2). The formal proof of this may be set out as follows. We would not worry about failure of the approximation at isolated points, so let us consider instead of (2) and (3) the functions

$$\overline{P}(\vec{a}, \vec{b}) \text{ and } \overline{-\vec{a} \cdot \vec{b}}$$

where the bar denotes independent averaging of $P(\vec{a}', \vec{b}')$ and $-\vec{a}' \cdot \vec{b}'$ over vectors $\vec{a}'$ and $\vec{b}'$ within specified small angles of $\vec{a}$ and $\vec{b}$. Suppose that for all $\vec{a}$ and $\vec{b}$ the difference is bounded by $\epsilon$:

$$|\overline{P}(\vec{a}, \vec{b}) + \vec{a} \cdot \vec{b}| \leq \epsilon \tag{16}$$

Then it will be shown that $\epsilon$ cannot be made arbitrarily small.

Suppose that for all $a$ and $b$

$$|\overline{\vec{a} \cdot \vec{b}} - \vec{a} \cdot \vec{b}| \leq \delta \tag{17}$$

Then from (16)

$$|\overline{P}(\vec{a}, \vec{b}) + \vec{a} \cdot \vec{b}| \leq \epsilon + \delta \tag{18}$$

From (2)

$$\overline{P}(\vec{a}, \vec{b}) = \int d\lambda\rho(\lambda) \overline{A}(\vec{a}, \lambda) \overline{B}(\vec{b}, \lambda) \tag{19}$$

where

$$|\overline{A}(\vec{a}, \lambda)| \leq 1 \text{ and } |\overline{B}(\vec{b}, \lambda)| \leq 1 \tag{20}$$

From (18) and (19), with $\vec{a} = \vec{b}$,

$$d\lambda\rho(\lambda) [\overline{A}(\vec{b}, \lambda) \overline{B}(\vec{b}, \lambda) + 1] \leq \epsilon + \delta \tag{21}$$

From (19)

$$\begin{array}{l} \overline{P}(\vec{a}, \vec{b}) - \overline{P}(\vec{a}, \vec{c}) = \int d\lambda\rho(\lambda) [\overline{A}(\vec{a}, \lambda) \overline{B}(\vec{b}, \lambda) - \overline{A}(\vec{a}, \lambda) \overline{B}(\vec{c}, \lambda)] \\ = \int d\lambda\rho(\lambda) \overline{A}(\vec{a}, \lambda) \overline{B}(\vec{b}, \lambda) [1 + \overline{A}(\vec{b}, \lambda) \overline{B}(\vec{c}, \lambda)] \\ - \int d\lambda\rho(\lambda) \overline{A}(\vec{a}, \lambda) \overline{B}(\vec{c}, \lambda) [1 + \overline{A}(\vec{b}, \lambda) \overline{B}(\vec{b}, \lambda)] \end{array}$$
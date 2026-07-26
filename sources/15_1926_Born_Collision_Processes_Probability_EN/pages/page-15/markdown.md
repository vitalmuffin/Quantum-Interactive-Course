Born – Quantum mechanics of collision processes.

15

$$u _ { n } = - \frac { 1 } { 4 \pi } \int _ { 0 } ^ { 2 \pi } d \varphi \int _ { 0 } ^ { \infty } \rho ^ { 2 } d \rho \int _ { 0 } ^ { \pi } \sin \vartheta d \vartheta F _ { n - 1 } ^ { \prime } ( \rho \sin \vartheta , \cdots ) \frac { e ^ { - i k \sqrt { \rho ^ { 2 } + Z ^ { 2 } - 2 \rho Z \cos \vartheta } } } { \sqrt { \rho ^ { 2 } + Z ^ { 2 } - 2 \rho Z \cos \vartheta } } .$$

Finally, we introduce the integration variable $\mu$ in place of $\vartheta$ by way of:

$$\begin{array} { l } { { \sqrt { \rho ^ { 2 } + Z ^ { 2 } - 2 \rho Z \cos \vartheta } = Z \mu , } } \\ { { \sin \vartheta d \vartheta = \displaystyle \frac { Z } { \rho } \mu d \mu ; } } \end{array}$$

the limits of integration will then become:

$$\vartheta = 0 ; \mu = \left| \frac { \rho } { Z } - 1 \right| ; \qquad \vartheta = \pi ; \mu = \frac { \rho } { Z } + 1 ,$$

and $\cos \vartheta , \sin \vartheta$ will be certain functions $c ( \rho , Z , \mu ) , s ( \rho , Z , \mu )$ that will assume the values $c = 1 , s = 0$ at the lower limits and the values $c = - 1 , s = 0$ at the upper ones. One will then obtain:

$$u _ { n } = - \frac { 1 } { 4 \pi } \int _ { 0 } ^ { 2 \pi } d \varphi \int _ { 0 } ^ { \infty } \rho d \rho \int _ { \left| \frac { \rho } { Z } - 1 \right| } ^ { \frac { \rho } { Z } + 1 } F _ { n - 1 } ^ { \prime } ( \rho s \cos \vartheta , \rho s \sin \vartheta , \rho c ) e ^ { - i k \mu Z } d \mu .$$

As in § 5, one will obtain the asymptotic representation from this by partial integration:

$$u _ { n } ^ { \infty } = \frac { 1 } { 4 \pi } \int _ { 0 } ^ { 2 \pi } d \varphi \int _ { 0 } ^ { \infty } \rho d \rho \frac { 1 } { i k Z } \Big [ F _ { n - 1 } ^ { \prime } ( 0 , 0 , \rho ) e ^ { - i k ( Z + \rho ) } - F _ { n - 1 } ^ { \prime } ( 0 , 0 , - \rho ) e ^ { - i k | Z - \rho | } \Big ] .$$

Here, from (5), one has:

$$F _ { n - 1 } ^ { \prime } ( 0 , 0 , \rho ) = F _ { n - 1 } ( a _ { 1 3 } \rho , a _ { 2 3 } \rho , a _ { 3 3 } \rho ) = F _ { n - 1 } \left( \frac { \rho x } { r } , \frac { \rho y } { r } , \frac { \rho z } { r } \right) ,$$

$$F _ { n - 1 } ^ { \prime } ( 0 , 0 , - \rho ) = F _ { n - 1 } ( - a _ { 1 3 } \rho , - a _ { 2 3 } \rho , - a _ { 3 3 } \rho ) = F _ { n - 1 } \left( - \frac { \rho x } { r } , - \frac { \rho y } { r } , - \frac { \rho z } { r } \right) .$$

One will then have:

$$\begin{array} { l } { { u _ { n } ^ { \infty } = \displaystyle \frac { e ^ { - i k r } } { 2 i k r } \int _ { 0 } ^ { \infty } \rho d \rho F _ { n - 1 } \left( \frac { \rho x } { r } , \frac { \rho y } { r } , \frac { \rho z } { r } \right) e ^ { - i k \rho } } } \\ { { - \displaystyle \frac { e ^ { - i k r } } { 2 i k r } \int _ { 0 } ^ { r } \rho d \rho F _ { n - 1 } \left( - \frac { \rho x } { r } , \cdots \right) e ^ { i k \rho } - \frac { e ^ { i k r } } { 2 i k r } \int _ { r } ^ { \infty } \rho d \rho F _ { n - 1 } \left( - \frac { \rho x } { r } , \cdots \right) e ^ { - i k \rho } . } } \end{array}$$

Here, the last integral vanishes as $r \to \infty$; if we assume that $| V | \leq a r ^ { - 2 }$ there, then due to the fact that $| u _ { 0 } | \leq b r ^ { - 1 }$, we will have:
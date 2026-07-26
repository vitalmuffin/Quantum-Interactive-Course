Born – Quantum mechanics of collision processes.

16

$$| F _ { n - 1 } | \leq \frac { A } { r ^ { 2 } } ,$$

so

$$\left| \int _ { r } ^ { \infty } \rho \, d \rho \, F _ { n - 1 } \left( - \frac { \rho x } { r } , \dots \right) e ^ { - i k \rho } \right| \leq A \int _ { r } ^ { \infty } \frac { d \rho } { \rho ^ { 2 } } = \frac { A } { r } .$$

We then finally obtain:

$$u _ { n } ^ { \infty } = \frac { e ^ { - i k r } } { 2 i k r } \int _ { 0 } ^ { \infty } \rho \, d \rho \left[ F _ { n - 1 } \left( \frac { \rho x } { r } , \dots \right) e ^ { - i k \rho } - F _ { n - 1 } \left( - \frac { \rho x } { r } , \dots \right) e ^ { - i k \rho } \right] . \tag { 6 }$$

However, this can be put into a more transparent form. In order to do that, we introduce the Fourier coefficients of the function $F _ { n - 1 }$ :

$$\begin{array} { l } { { f _ { n - 1 } ( \mathfrak { l } ) = \displaystyle \frac { 1 } { ( 2 \pi ) ^ { 3 } } \iiint F _ { n - 1 } ( \mathfrak { r } ) e ^ { - i \mathfrak { l } } d S } } \\ { { \qquad = \displaystyle \frac { 1 } { ( 2 \pi ) ^ { 3 } } \int _ { 0 } ^ { \infty } r ^ { 2 } d r \iint d \omega F _ { n - 1 } ( \mathfrak { r s } ) e ^ { - i k ( \mathfrak { r s } ) } . } } \end{array} \tag { 7 }$$

We determine the asymptotic value from the already twice-performed process, and obtain:

$$f _ { n - 1 } ^ { \infty } ( k _ { x } , k _ { y } , k _ { z } ) = \frac { 1 } { 4 \pi ^ { 2 } i k } \int _ { 0 } ^ { \infty } r \, d r \left[ F _ { n - 1 } \left( \frac { r k _ { x } } { k } , \dots \right) e ^ { i k r } - F _ { n - 1 } \left( - \frac { r k _ { x } } { k } , \dots \right) e ^ { - i k r } \right] .$$

One will then have:

$$f _ { n - 1 } ^ { \infty } \left( - k \frac { x } { r } , - k \frac { y } { r } , - k \frac { z } { r } \right) = \frac { 1 } { 4 \pi ^ { 2 } i k } \int _ { 0 } ^ { \infty } \rho \, d \rho \left[ F _ { n - 1 } \left( \frac { \rho x } { r } , \dots \right) e ^ { - i k \rho } - F _ { n - 1 } \left( - \frac { \rho x } { r } , \dots \right) e ^ { i k \rho } \right] . \tag { 8 }$$

If we substitute that into (6) then we will finally obtain:

$$u _ { n } ^ { \infty } ( x , y , z ) = 2 \pi ^ { 2 } \, f _ { n - 1 } ^ { \infty } \left( - k \frac { x } { r } , - k \frac { y } { r } , - k \frac { z } { r } \right) \frac { e ^ { - i k r } } { r } . \tag { 9 }$$

If we compare that with the formulas (11) and (18) of § 5 then we will see that an observer at infinity will see the scattered radiation as a plane wave with the amplitude:

$$\frac { k } { 2 \pi } 2 \pi ^ { 3 } \left| f _ { n - 1 } ^ { \infty } ( - k \mathfrak { s } ) \right| = k \pi \left| f _ { n - 1 } ^ { \infty } ( - k \mathfrak { s } ) \right| ,$$

which will depend upon the direction $\mathfrak { s }$ ; thus, the probability that an electron will be deflected into an element of solid angle $d \omega$ with the mean direction $\mathfrak { s }$ will be:
Zur Quantenmechanik. II.

587

Nach unserer Voraussetzung haben nun die Koeffizienten der Gleichungen (15), Kap. 3, die Form:

$$H(kl) = \delta_{kl} W_l^0 + \lambda H_1(kl) + \lambda^2 H_2(kl) + \cdots$$

Daher suchen wir die Lösung von (15), Kap. 3, durch Entwicklungen der Form:

$$\left. \begin{aligned} W &= W^0 + \lambda W^{(1)} + \lambda^2 W^{(2)} + \cdots \\ x_k &= x_k^0 + \lambda x_k^{(1)} + \lambda^2 x_k^{(2)} + \cdots \end{aligned} \right\} \quad (16)$$

zu gewinnen. Setzen wir das in (15), Kap. 3, ein, so bekommen wir die Näherungsgleichungen:

$$\left. \begin{aligned} a) & x_k^0 (W^0 - W_k^0) = 0, \\ b) & x_k^{(1)} (W^0 - W_k^0) = -x_k^0 W^{(1)} + \sum_l H^{(1)}(kl) x_l^0, \\ c) & x_k^{(2)} (W^0 - W_k^0) = -(x_k^{(1)} W^{(1)} + x_k^{(0)} W^{(2)}) \\ & \quad + \sum_l (H^{(1)}(kl) x_l^{(1)} + H^{(2)}(kl) x_l^0). \end{aligned} \right\} \quad (17)$$

Aus (17a), Kap. 3, folgt, daß $W$ gleich einem der $W_k$ werden muß; denn sonst würden alle $x_k^0$ verschwinden, und dann würde man aus den folgenden Näherungsgleichungen auch das Verschwinden von $x_k^{(1)}, x_k^{(2)} \dots$ der Reihe nach erschließen können.

Nehmen wir nun das Ausgangssystem als nicht entartet, also alle $W_k^0$ als verschieden an, so lautet die Lösung von (17a), Kap. 3:

$$W = W_n^0; \quad x_{nn}^0 = y_n^0; \quad x_{kn}^0 = 0 \text{ für } k \neq n. \quad (18)$$

Dabei ist $y_n^0$ eine beliebige Zahl.

Setzen wir das in (17b), Kap. 3, ein, so hat man, je nachdem $k = n$ oder $k \neq n$ ist:

$$\begin{aligned} 0 &= y_n^0 (-W^{(1)} + H^{(1)}(nn)), \\ x_k^{(1)} (W_n^0 - W_k^0) &= H^{(1)}(kn) y_n^0, \quad k \neq n. \end{aligned}$$

Die Lösung lautet also:

$$W^{(1)} = H^{(1)}(nn); \quad x_{nn}^{(1)} = y_n^{(1)}; \quad x_{kn}^{(1)} = -\frac{H^{(1)}(kn)}{h \nu_0(kn)} y_n^0 \text{ für } k \neq n, \quad (19)$$

wo $y_n^{(1)}$ wiederum eine beliebige Zahl ist.

Nunmehr folgt ebenso aus (17c), Kap. 3:

$$\left. \begin{aligned} W^{(2)} &= H^{(2)}(nn) - \frac{1}{h} \sum_l \frac{H^{(1)}(nl) H^{(1)}(ln)}{\nu_0(ln)}, \\ x_{nn}^{(2)} &= y_n^{(2)} \\ x_{kn}^{(2)} &= \left( \frac{1}{h^2} \sum_l \frac{H^{(1)}(kl) H^{(1)}(ln)}{\nu_0(kn) \nu_0(ln)} - \frac{H^{(1)}(nn) H^{(1)}(kn)}{h^2 \nu_0(kn)^2} \right. \\ & \left. - \frac{H^{(2)}(kn)}{h \nu_0(kn)} \right) y_n^0 - \frac{H^{(1)}(kn)}{h \nu_0(kn)} y_n^{(1)}. \end{aligned} \right\} \quad (20)$$
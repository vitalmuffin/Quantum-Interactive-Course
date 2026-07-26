878

M. Born und P. Jordan,

Wenn ein solches $n_0$ existiert, können wir eine Reihe von Zahlen

$$n_0, n_1, n_2, n_3 \dots$$

angeben derart, daß

$$(n_k)' = n_{k+1} \quad \text{und} \quad W_{k+1} > W_k$$

Dann ist jedesmal

$$(n_{k+1})'' = n_k$$

Also wird für $k > 0$ aus (58) und (59):

$$H(n_k, n_k) = 4\pi^2 v_0^2 \{|q(n_k, n_{k+1})|^2 + |q(n_k, n_{k-1})|^2\}, \quad (61)$$

$$\frac{1}{2}h = 4\pi^2 v_0 \{|q(n_k, n_{k+1})|^2 - |q(n_k, n_{k-1})|^2\}. \quad (62)$$

Aus (60) und (62) folgt

$$|q(n_k, n_{k+1})|^2 = \frac{h}{8\pi^2 v_0} (k+1), \quad (63)$$

und dann aus (61)

$$W_{n_k} = H(n_k, n_k) = v_0 h(k + \frac{1}{2}). \quad (64)$$

Nun wollen wir noch sehen, ob es möglich ist, daß es kein $n$ gibt, für das der Fall a) gilt. Wir können dann, mit beliebigem $n_0$ anfangend, $n_0' = n_1$ und $n_0'' = n_{-1}$ bilden; zu jedem von diesen wieder $n_1' = n_2$, $n_1'' = n_0$ und $n_{-1}' = n_0$, $n_{-1}'' = n_{-2}$ usw. Auf diese Weise erhalten wir eine Zahlenreihe

$$\dots n_{-2}, n_{-1}, n_0, n_1, n_2 \dots \quad (65)$$

und es gelten die Gleichungen (61), (62) für jedes $k$ zwischen $-\infty$ und $+\infty$. Das ist aber unmöglich; denn nach (62) bilden die Größen $x_k = |q(n_{k+1}, n_k)|^2$ eine äquidistante Zahlenreihe, und da sie positiv sind, muß es eine kleinste geben. Den entsprechenden Index können wir wieder mit $n_0$ bezeichnen und kommen damit auf den vorigen Fall zurück; es gelten also auch hier die Formeln (63), (64).

Man sieht ferner: jede Zahl $n$ muß unter den Zahlen $n_k$ enthalten sein; denn sonst könnte man mit $n$ als Ausgangsgliede eine neue Reihe (65) bilden, wobei wieder die Formel (60) gilt. Die Ausgangsglieder beider Reihen hätten also dieselben Werte $W_n = H(nn)$, was unmöglich ist.

Damit ist der Beweis geführt, daß die Indizes 0, 1, 2, 3 ... so in eine neue Reihenfolge $n_0, n_1, n_2, n_3 \dots$ umgeordnet werden können, daß die Formeln (63), (64) gelten; in diesen neuen Indizes hat dann die Lösung die Heisenbergsche Form (53). Diese erscheint also als „Normalform“ der allgemeinen Lösung. Sie hat nach (64) die Eigenschaft, daß

$$W_{n_{k+1}} > W_{n_k}$$

Fordert man umgekehrt, daß $W_n = H(nn)$ mit $n$ stets wachsen soll, so wird notwendig $n_k = k$; dieses Prinzip legt also die Normalform
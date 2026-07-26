586

M. Born, W. Heisenberg und P. Jordan,

Konvergenz der Potenzreihe nach $\lambda$ wesentlich von der geschickten Wahl von $H_0$ abhängen.

Um die Hermitesche Form

$$\sum_{mn} H_{mn} x_m x_n^*$$

auf ihre Hauptachsen zu transformieren, kann man bekanntlich so verfahren:

Man suche die linearen Gleichungen

$$W x_k - \sum_l H(kl) x_l = 0 \quad (15)$$

zu lösen; das ist nur möglich für gewisse Werte des Parameters $W$, nämlich $W = W_n$, wo $W_n$ wieder die Eigenwerte (Energiewerte) bedeuten. Wir nehmen zunächst an, daß keine Entartung vorliegt, also alle $W_n$ verschieden sind. Dann gehört zu jedem $W_n$ eine bis auf einen Faktor bestimmte Lösung $x_k = x_{kn}$; es gelten also die Identitäten

$$W_n x_{kn} - \sum_l H(kl) x_{ln} = 0,$$

$$W_m x_{km}^* - \sum_l H^*(kl) x_{lm}^* = 0.$$

Multipliziert man die erste mit $x_{km}^*$, die zweite mit $x_{kn}$ und summiert über $k$, so folgt durch Subtraktion wegen des Hermiteschen Charakters von $H$:

$$(W_n - W_m) \sum_k x_{kn} x_{km}^* = 0.$$

Durch geeignete Wahl des Proportionalitätsfaktors kann man es ferner erreichen, daß

$$\sum_k x_{kn} x_{kn}^* = 1$$

ist. Folglich bilden die $x_{kn}$ eine orthogonale Matrix

$$S = (x_{kn}).$$

Diese ist es gerade, welche die gegebene Form auf eine Quadratsumme transformiert; denn setzt man

$$x_k = \sum_n x_{kn} y_n$$

in die Form ein, so erhält man

$$\begin{aligned} \sum_{kl} H(kl) x_k x_l^* &= \sum_{kl} \sum_{mn} H(kl) x_{km} x_{ln}^* y_m y_n^* \\ &= \sum_{mn} \sum_l W_m x_{lm} x_{ln}^* y_m y_n^* \\ &= \sum_m W_m y_m y_m^*. \end{aligned}$$
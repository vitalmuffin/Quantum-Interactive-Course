Zur Quantenmechanik. II.

593

im Sinne von (31), Kap. 3, zu interpretieren sind; diese Differentiallösungen sind dann in gewöhnlicher Weise orthogonal, aber nicht auf 1, sondern auf das Differential der Basisfunktion $\varphi(W)$ normiert.

Die Gesamtheit der diskreten Werte $x_{kn}$ und der in einem Index diskret, im anderen kontinuierlich verteilten $x_k(W)$ bildet die Elemente der „orthogonalen“ Matrix:

$$S = (x_{kn}, x_k(W) \, dW),$$

die man schematisch so darstellen kann:

$$S = \left( \begin{array}{c} \uparrow \quad \downarrow \quad \downarrow \\ \downarrow \quad \downarrow \quad \downarrow \\ \uparrow \quad \downarrow \quad \downarrow \quad \downarrow \\ \downarrow \quad \downarrow \quad \downarrow \quad \downarrow \end{array} \right) \quad (33)$$

Die Orthogonalitäts- und Normalisierungsgleichungen für die ganze Matrix zerfallen in vier verschiedene Typen:

$$\left. \begin{array}{l} \sum_k x_{km} x_{kn}^* = \delta_{mn}; \\ \sum_k x_{kn} x_k^*(W) \, dW = 0; \quad \sum_k x_k(W) \, dW \cdot x_{kn}^* = 0; \\ \sum_k x_k(W') \, dW' \, x_k^*(W'') \, dW'' = d\varphi. \end{array} \right\} \quad (34)$$

Man kann aber auch die Orthogonalitätsrelationen für die Kolonnen anschreiben; diese lauten:

$$\begin{aligned} &\sum_n x_{kn} x_{ln}^* + \int \frac{x_k(W) \, dW \cdot x_l^*(W) \, dW}{d\varphi} \\ &= \sum_n x_{kn} x_{ln}^* + \int \frac{dW}{\varphi'} x_k(W) x_l^*(W) = \delta_{kl}, \end{aligned} \quad (35)$$

wo $\varphi' = \frac{d\varphi}{dW}$ gesetzt ist.

Mit Hilfe dieser Matrix hat man die Variablen $x_n$ in neue $y_n, y(\varphi) \, d\varphi$ zu transformieren; man setze:

$$\left. \begin{array}{l} y_n = \sum_k x_{kn} \cdot x_k \\ y(\varphi) \, d\varphi = \sum_k x_k(W) \, dW \cdot x_k. \end{array} \right\} \quad (36)$$
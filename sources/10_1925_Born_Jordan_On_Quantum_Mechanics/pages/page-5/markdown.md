862

M. Born und P. Jordan,

Summe von endlich oder unendlich vielen Potenzprodukten in den Argumenten $\mathbf{x}_k$ mit Zahlen als Koeffizienten formal dargestellt werden kann. Es können dann auch durch Gleichungen

$$\left. \begin{array}{l} f_1(y_1, \dots, y_n; x_1, \dots, x_n) = 0, \\ \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \end{array} \right\} \quad (12)$$

Funktionen $\mathbf{y}_l(\mathbf{x}_1, \dots, \mathbf{x}_n)$ definiert werden. Um nämlich Funktionen $\mathbf{y}_l$ der oben beschriebenen Form zu erhalten, welche den Gleichungen (12) genügt, hat man nur die $\mathbf{y}_l$ als Reihen, die nach Potenzprodukten der $\mathbf{x}_k$ fortschreiten, anzusetzen und durch Einsetzen in (12) die Koeffizienten der Reihe nach zu bestimmen. Man erkennt, daß sich stets ebenso viele Gleichungen wie Unbekannte ergeben. Die Anzahl der Gleichungen und Unbekannten ist freilich größer, als bei der Anwendung der Methode der unbestimmten Koeffizienten in der gewöhnlichen, mit kommutativer Multiplikation rechnenden Analysis. Man erhält in jeder der Gleichungen (12) nach Einsetzen der Reihen für die $\mathbf{y}_l$ und Zusammenfassung der zusammengehörigen Glieder außer einem Summanden $C'\mathbf{x}_1\mathbf{x}_2$ auch einen Summanden $C''\mathbf{x}_2\mathbf{x}_1$ und hat sowohl $C'$ als auch $C''$ (nicht nur $C' + C''$) zum Verschwinden zu bringen. Dafür treten jedoch auch in der Entwicklung eines jeden $\mathbf{y}_l$ zwei Glieder $\mathbf{x}_1\mathbf{x}_2$ und $\mathbf{x}_2\mathbf{x}_1$ mit zwei verfügbaren Koeffizienten auf.

§ 2. Symbolische Differentiation. Ein später viel benutzter Rechenprozeß, den wir hier näher betrachten wollen, soll als Differentiation einer Matrizenfunktion bezeichnet werden. Es ist jedoch zu beachten, daß dieser Prozeß nur in einigen Punkten ähnliche Eigenschaften besitzt, wie die Differentiation der gewöhnlichen Analysis. Zum Beispiel sind hier die Produktregel der Differentiation oder die Regel für die Differentiation einer Funktion von einer Funktion nicht mehr allgemein in Gültigkeit. Nur dann, wenn alle vorkommenden Matrizen miteinander vertauschbar sind, gelten für diese Differentiation alle Regeln der gewöhnlichen Analysis.

Es sei

$$\mathbf{y} = \prod_{m=1}^s \mathbf{x}_{l_m} = \mathbf{x}_{l_1}\mathbf{x}_{l_2} \dots \mathbf{x}_{l_r} \quad (13)$$

Wir definieren

$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}_k} = \sum_{r=1}^s \delta_{l_r k} \prod_{m=r+1}^s \mathbf{x}_{l_m} \prod_{m=1}^{m=r-1} \mathbf{x}_{l_m}, \quad \begin{cases} \delta_{jk} = 0 \text{ für } j \neq k, \\ \delta_{kk} = 1. \end{cases} \quad (14)$$

In Worten lautet diese Regel: Man denke in dem gegebenen Produkt alle Faktoren einzeln angeschrieben (also z. B. nicht $\mathbf{x}_1^2 \mathbf{x}_2^2$, sondern
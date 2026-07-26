180

Bose,

Indessen muß die Gesamtzahl der Zellen als die Zahl der möglichen Anordnungen eines Quants in dem gegebenen Volumen angesehen werden. Um der Tatsache der Polarisation Rechnung zu tragen, erscheint es dagegen geboten, diese Zahl noch mit 2 zu multiplizieren, so daß wir für die Zahl der zu $d\pmb{v}$ gehörigen Zellen $8\pi V \frac{\pmb{v}^2 d\pmb{v}}{c^3}$ erhalten.

Nun ist es einfach, die thermodynamische Wahrscheinlichkeit eines (makroskopisch definierten) Zustandes zu berechnen. Es sei $N^s$ die Zahl der zum Frequenzbereich $d\pmb{v}^s$ gehörigen Quanten. Auf wie viele Arten können diese auf die zu $d\pmb{v}^s$ gehörigen Zellen verteilt werden? Sei $p_0^s$ die Zahl der vakanten Zellen, $p_1^s$ die Zahl derer, die ein Quant enthalten, $p_2^s$ die Zahl der Zellen, die zwei Quanten enthalten usf. Die Zahl der möglichen Verteilungen ist dann

$$\frac{A^s!}{p_0^s! p_1^s! \dots}, \text{ wobei } A^s = \frac{8\pi\pmb{v}^2}{c^3} d\pmb{v}^s,$$

und wobei

$$N^s = 0 \cdot p_0^s + 1 \cdot p_1^s + 2 p_2^s \dots$$

die Zahl der zu $d\pmb{v}^s$ gehörigen Quanten ist.

Die Wahrscheinlichkeit des durch sämtliche $p_r^s$ definierten Zustandes ist offenbar

$$\prod_s \frac{A^s!}{p_0^s! p_1^s! \dots}.$$

Mit Rücksicht darauf, daß wir die $p_r^s$ als große Zahlen betrachten können, haben wir

$$\lg W = \sum_s A^s \lg A^s - \sum_s \sum_r p_r^s \lg p_r^s,$$

wobei

$$A^s = \sum_r p_r^s.$$

Dieser Ausdruck soll ein Maximum sein unter der Nebenbedingung

$$E = \sum_s N^s h \pmb{v}^s; \quad N^s = \sum_r r p_r^s.$$

Die Durchführung der Variation liefert die Bedingungen

$$\begin{aligned} \sum_s \sum_r \delta p_r^s (1 + \lg p_r^s) &= 0, & \sum_s \delta N^s h \pmb{v}^s &= 0 \\ \sum_r \delta p_r^s &= 0 & \delta N^s &= \sum_r r \delta p_r^s. \end{aligned}$$

Hieraus folgt

$$\sum_s \sum_r \delta p_r^s (1 + \lg p_r^s + \lambda^s) + \frac{1}{\beta} \sum_s h \pmb{v}^s \sum_r r \delta p_r^s = 0.$$
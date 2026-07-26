Zur Quantenmechanik.

885

werden wir die elektrische und die magnetische Feldstärke $\mathfrak{E}$, $\mathfrak{H}$ als Matrizen ansehen, deren Elemente harmonisch schwingende ebene Wellen sind, also z. B. bei geeigneter Lage des Koordinatensystems

$$\mathfrak{E} = \left( \mathfrak{E}(nm) e^{2\pi i r (nm) \left( t - \frac{x}{c} \right)} \right). \quad (89)$$

Freilich muß damit gerechnet werden, daß $n, m$ sich im allgemeinen nicht mehr auf eine diskrete Menge von Werten beschränken und auch nicht mehr einzelne Zahlen, sondern Zahlensysteme (Vektoren) bezeichnen.

Die Maxwellschen Gleichungen wird man als Matrizengleichungen beibehalten:

$$\text{rot } \mathfrak{H} - \frac{1}{c} \dot{\mathfrak{E}} = 0, \quad \text{rot } \mathfrak{E} + \frac{1}{c} \dot{\mathfrak{H}} = 0. \quad (90)$$

Die Differentiationen nach $x, y, z, t$ sind dabei in jedem einzelnen Element der Matrix ausgeführt zu denken$^{1)}$.

Wir wollen nun den Energie-Impulssatz ableiten; dazu ist es notwendig, einige Bemerkungen über die Multiplikation von Matrizenvektoren vorauszuschicken.

Wir definieren das skalare Produkt durch

$$(\mathfrak{A}, \mathfrak{B}) = \mathfrak{A}\mathfrak{B} = \mathfrak{A}_x \mathfrak{B}_x + \mathfrak{A}_y \mathfrak{B}_y + \mathfrak{A}_z \mathfrak{B}_z, \quad (91)$$

das Vektorprodukt durch

$$[\mathfrak{A}\mathfrak{B}]_x = \mathfrak{A}_y \mathfrak{B}_z - \mathfrak{A}_z \mathfrak{B}_y. \quad (92)$$

Da die Matrizenmultiplikation nicht kommutativ ist, gelten die Beziehungen

$$\mathfrak{A}\mathfrak{B} = \mathfrak{B}\mathfrak{A}, \quad [\mathfrak{A}\mathfrak{B}] = -[\mathfrak{B}\mathfrak{A}]$$

im allgemeinen nicht.

Dagegen behaupten wir:

$$\text{div } [\mathfrak{A}\mathfrak{B}] = (\text{rot } \mathfrak{A}, \mathfrak{B}) - (\mathfrak{A}, \text{rot } \mathfrak{B}). \quad (93)$$

Wir definieren nun die Energichte $\mathcal{W}$ (als skalare Matrix) durch

$$\mathcal{W} = \frac{1}{8\pi} (\mathfrak{E}^2 + \mathfrak{H}^2). \quad (94)$$

Dann wird nach (11)

$$8\pi \dot{\mathcal{W}} = \mathfrak{E}\dot{\mathfrak{E}} + \dot{\mathfrak{E}}\mathfrak{E} + \mathfrak{H}\dot{\mathfrak{H}} + \dot{\mathfrak{H}}\mathfrak{H},$$

und nach (90):

$$\frac{8\pi}{c} \mathcal{W} = (\mathfrak{E}, \text{rot } \mathfrak{H}) + (\text{rot } \mathfrak{H}, \mathfrak{E}) - (\mathfrak{H}, \text{rot } \mathfrak{E}) - (\text{rot } \mathfrak{E}, \mathfrak{H}),$$

$^{1)}$ Unter Umständen ist eine andere Auffassung des elektromagnetischen Feldes erforderlich, bei der die räumlichen Koordinaten nicht als Zahlen, sondern selbst wieder als Matrizen erscheinen; das hat eine entsprechende Änderung der Bedeutung der räumlichen Differenzialquotienten in den Maxwellschen Gleichungen zur Folge. Wir kommen hierauf in der Fortsetzung der Arbeit zurück.
Zur Quantenmechanik.

865

Diese Beziehung gilt wegen ihres linearen Charakters in $\mathbf{z}$ nicht nur für Ausdrücke $\mathbf{z}$ der Form (19), sondern zugleich auch für beliebige analytische Funktionen $\mathbf{g}(\mathbf{p}\mathbf{q})^{1)}$.

Zum Schluß dieser kurzen Darstellung der Matrizenanalysis wollen wir noch den Satz beweisen: Jede Matrizengleichung

$$F(\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_r) = 0$$

bleibt richtig, wenn man in allen Argumentmatrizen $\mathbf{x}_j$ ein und dieselbe Permutation aller Zeilen und Kolonnen vornimmt. Hierzu genügt es offenbar zu zeigen, daß für zwei Matrizen $\mathbf{a}, \mathbf{b}$, die durch diese Operation in $\mathbf{a}', \mathbf{b}'$ übergehen, die Invarianzen

$$\mathbf{a}' + \mathbf{b}' = (\mathbf{a} + \mathbf{b})'. \quad \mathbf{a}'\mathbf{b}' = (\mathbf{a}\mathbf{b})'$$

gelten, wo die rechten Seiten diejenigen Matrizen bedeuten, die aus $\mathbf{a} + \mathbf{b}$ und $\mathbf{a}\mathbf{b}$ durch jene Vertauschungen entstehen.

Wir führen diesen Beweis, indem wir die Operation des Permutierens durch Multiplikation mit einer geeigneten Matrix ersetzen$^{2)}$.

Eine Permutation schreiben wir

$$\begin{pmatrix} 0 & 1 & 2 & 3 & \dots \\ k_0 & k_1 & k_2 & k_3 & \dots \end{pmatrix} = \begin{pmatrix} n \\ k_n \end{pmatrix}.$$

Dieser ordnen wir die Permutationsmatrix

$$\mathbf{p} = (p(nm)), \quad p(nm) = \begin{cases} 1 & \text{für } m = k_n, \\ 0 & \text{sonst} \end{cases}$$

zu. Die zu $\mathbf{p}$ transponierte Matrix sei

$$\tilde{\mathbf{p}} = (\tilde{p}(nm)), \quad \tilde{p}(nm) = \begin{cases} 1 & \text{für } n = k_m, \\ 0 & \text{sonst.} \end{cases}$$

Durch Multiplikation beider folgt

$$\mathbf{p}\tilde{\mathbf{p}} = \left( \sum_k p(nk)\tilde{p}(km) \right) = (\delta_{nm}) = 1,$$

da beide Faktoren $p(nk)$ und $\tilde{p}(km)$ nur dann gleichzeitig von Null ver-

$^{1)}$ Allgemeiner wird für Funktionen von $r$ Variabeln

$$\sum_r \left( \mathbf{x}_r \frac{\partial \mathbf{g}}{\partial \mathbf{x}_r} - \frac{\partial \mathbf{g}}{\partial \mathbf{x}_r} \mathbf{x}_r \right) = 0.$$

$^{2)}$ Dieses hier gewählte Beweisverfahren besitzt den Vorzug, daß es den engen Zusammenhang der Permutationen mit einer wichtigen Klasse allgemeiner Transformationen der Matrizen erkennen läßt. Die Richtigkeit des fraglichen Satzes kann jedoch auch unmittelbar aus der Bemerkung gefolgert werden, daß in den Definitionen der Gleichheit sowie der Addition und Multiplikation von Matrizen kein Gebrauch von Ordnungsbeziehungen zwischen den Zeilen bzw. Spalten gemacht wird.
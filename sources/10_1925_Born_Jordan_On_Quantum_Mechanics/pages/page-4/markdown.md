Zur Quantenmechanik.

861

werden $\boldsymbol{a}$ und $\boldsymbol{b}$ vertauschbar genannt. Die durch

$$\boldsymbol{1} = (\delta_{nm}), \quad \begin{cases} \delta_{nm} = 0 & \text{für } n \neq m, \\ \delta_{nn} = 1 \end{cases} \quad (6)$$

definierte Einheitsmatrix hat die Eigenschaft

$$\boldsymbol{a}\boldsymbol{1} = \boldsymbol{1}\boldsymbol{a} = \boldsymbol{a}. \quad (6a)$$

Die zu $\boldsymbol{a}$ reziproke Matrix $\boldsymbol{a}^{-1}$ ist definiert durch$^{1)}$

$$\boldsymbol{a}^{-1}\boldsymbol{a} = \boldsymbol{a}\boldsymbol{a}^{-1} = \boldsymbol{1}. \quad (7)$$

Als „Mittelwert“ einer Matrix $\boldsymbol{a}$ bezeichnen wir diejenige Matrix, deren Diagonalelemente mit denen von $\boldsymbol{a}$ übereinstimmen, während alle übrigen Elemente Null sind:

$$\overline{\boldsymbol{a}} = (\delta_{nm} a (nn)). \quad (8)$$

Die Summe dieser Diagonalelemente soll „Diagonalsumme der Matrix $\boldsymbol{a}$“ heißen und mit $D(\boldsymbol{a})$ bezeichnet werden:

$$D(\boldsymbol{a}) = \sum_n a(nn). \quad (9)$$

Nach (3) beweist man leicht: Wenn die Diagonalsumme eines Produkts $\boldsymbol{y} = \boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_m$ endlich ist, so bleibt sie unverändert bei zyklischer Vertauschung der Faktoren:

$$D(\boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_m) = D(\boldsymbol{x}_r \boldsymbol{x}_{r+1} \dots \boldsymbol{x}_m \boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_{r-1}). \quad (10)$$

Es genügt offenbar, sich von der Richtigkeit des Satzes für zwei Faktoren zu überzeugen.

Sind die Komponenten der Matrizen $\boldsymbol{a}, \boldsymbol{b}$ Funktionen eines Parameters $t$, so wird

$$\frac{d}{dt} \sum_k a(nk) b(km) = \sum_k \{\dot{a}(nk) b(km) + a(nk) \dot{b}(km)\}$$

oder nach der Definition (3):

$$\frac{d}{dt}(\boldsymbol{a}\boldsymbol{b}) = \dot{\boldsymbol{a}}\boldsymbol{b} + \boldsymbol{a}\dot{\boldsymbol{b}}. \quad (11)$$

Wiederholte Anwendung von (11) gibt

$$\frac{d}{dt}(\boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_n) = \dot{\boldsymbol{x}}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_n + \boldsymbol{x}_1 \dot{\boldsymbol{x}}_2 \dots \boldsymbol{x}_n + \dots + \boldsymbol{x}_1 \boldsymbol{x}_2 \dots \dot{\boldsymbol{x}}_n. \quad (11')$$

Durch die Rechenprozesse (2), (3) können Funktionen von Matrizen definiert werden. Als allgemeinste Funktion $f(\boldsymbol{x}_1 \boldsymbol{x}_2 \dots \boldsymbol{x}_m)$ soll hier zunächst eine solche in Betracht gezogen werden, welche durch eine

$^{1)}$ Bekanntlich ist bei endlichen quadratischen Matrizen $\boldsymbol{a}^{-1}$ durch diese Definition stets eindeutig festgelegt, wenn die Determinante $A$ von $\boldsymbol{a}$ von Null verschieden ist. Ist $A = 0$, so gibt es keine zu $\boldsymbol{a}$ reziproke Matrix.
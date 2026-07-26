Zur Quantenmechanik.

863

$x_1 x_1 x_2 x_2$); man greife irgend einen Faktor $x_k$ heraus und bilde das Produkt aller ihm folgenden Faktoren und aller ihm voraufgehenden Faktoren (in dieser Reihenfolge). Die Summe aller so gebildeten Glieder ist der Differentialquotient des Produkts nach diesem $x_k$.

Einige Beispiele mögen das Verfahren erläutern:

$$y = x^n, \quad \frac{dy}{dx} = nx^{n-1}$$

$$y = x_1^n x_2^m, \quad \frac{\partial y}{\partial x_1} = x_1^{n-1} x_2^m + x_1^{n-2} x_2^m x_1 + \dots + x_k^m x_1^{n-1},$$

$$y = x_1^2 x_2 x_1 x_3, \quad \frac{\partial y}{\partial x_1} = x_1 x_2 x_1 x_3 + x_2 x_1 x_3 x_1 + x_3 x_1^2 x_2.$$

Fordern wir ferner

$$\frac{\partial(y_1 + y_2)}{\partial x_k} = \frac{\partial y_1}{\partial x_k} + \frac{\partial y_2}{\partial x_k}, \tag{15}$$

so ist die Ableitung $\frac{\partial y}{\partial x}$ für allgemeinste analytische Funktionen $y$ definiert.

Mit diesen Definitionen und der der Diagonalsumme (9) gilt die Beziehung

$$\frac{\partial D(y)}{\partial x_k (nm)} = \frac{\partial y}{\partial x_k} (mn), \tag{16}$$

wobei rechts die $mn$-Komponente der Matrix $\frac{\partial y}{\partial x_k}$ steht. Diese Beziehung kann auch zur Definition der Ableitung $\frac{\partial y}{\partial x_k}$ benutzt werden. Zum Beweis von (16) genügt es offenbar, eine Funktion $y$ der Form (13) zu betrachten. Nach (14) und (3) wird

$$\frac{\partial y}{\partial x_k} (mn) = \sum_{r=1}^s \delta_{l_r k} \sum_{\tau} \prod_{p=r+1}^s x_{l_p} (\tau_p \tau_{p+1}) \prod_{p=1}^{r-1} x_{l_p} (\tau_p \tau_{p+1}); \tag{17}$$

$$\tau_{r+1} = m, \quad \tau_{s+1} = \tau_1, \quad \tau_r = n.$$

Andererseits ist aus (3) und (9) zu entnehmen:

$$\frac{\partial D(y)}{\partial x_k (mn)} = \sum_{r=1}^s \delta_{l_r k} \sum_{\tau} \prod_{p=1}^{r-1} x_{l_p} (\tau_p \tau_{p+1}) \prod_{p=r+1}^s x_{l_p} (\tau_p \tau_{p+1}); \tag{17'}$$

$$\tau_1 = \tau_{s+1}, \quad \tau_r = n, \quad \tau_{r+1} = m.$$

Vergleich von (17) und (17') gibt (16).

Hervorgehoben sei gleich hier eine für später wichtige Tatsache, die aus der Definition (14) abzulesen ist: Die partiellen Ableitungen
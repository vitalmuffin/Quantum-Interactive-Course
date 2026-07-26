126

E. Schrödinger

wertvolle Anleitung und einige durchgerechnete Beispiele. Ein Beispiel aus der Atomdynamik ist in einer gleichzeitig in diesen Annalen erscheinenden Abhandlung des Hrn. Fues über die Intensitäten der Bandensprektren durchgeführt.

Wir wenden das jetzt auf unser Problem, d. h. auf die Auflösung des Gleichungspaares (13) für die Amplituden $w_{\pm}$ der Störungsschwingungen an, wobei wir jedoch nach wie vor voraussetzen, daß die *eine* erregte *freie* Schwingung $u_k$ dem diskreten Punktspektrum angehöre. Wir entwickeln die rechte Seite von (13) nach dem Schema (27)

$$(30) \quad \frac{4\pi^2}{h^2} A(x) u_k(x) = \frac{4\pi^2}{h^2} \sum_{n=1}^{\infty} a'_{kn} u_n(x) + \frac{4\pi^2}{h^2} \int_a^b u(x, E) a'_k(E) dE,$$

wo $a'_{kn}$ durch (15) und $a'_k(E)$ nach (29) durch

$$(15') \quad a'_k(E) = \lim_{\Delta=0} \frac{1}{\Delta} \int \varrho(\xi) A(\xi) u_k(\xi) \cdot \int_E^{E+\Delta} u(\xi, E') dE' \cdot d\xi$$

gegeben ist. Denkt man sich die Entwicklung (30) in (13) eingesetzt, entwickelt dann auch die gesuchte Lösung $w_{\pm}(x)$ in ganz analoger Weise nach den Eigenlösungen $u_n(x)$ und $u(x, E)$ und berücksichtigt, daß für die letztgenannten Funktionen die linke Seite von (13) den Wert

$$\frac{8\pi^2}{h^2} (E_k \pm h\nu - E_n) u_n(x)$$

bzw.

$$\frac{8\pi^2}{h^2} (E_k \pm h\nu - E) u(x, E)$$

annimmt, dann erhält man durch „Koeffizientenvergleichung“ als Verallgemeinerung von (14)

$$(14') \quad w_{\pm}(x) = \frac{1}{2} \sum_{n=1}^{\infty} \frac{a'_{kn} u_n(x)}{E_k - E_n \pm h\nu} + \frac{1}{2} \int_a^b \frac{a'_k(E) u(x, E)}{E_k - E \pm h\nu} dE.$$

Die weitere Durchführung ist völlig analog mit der in § 2. Man erhält schließlich als *Zusatzglied* zu (23)

$$(23') + 2 \cos 2\pi\nu t \int d\xi \varrho(\xi) M_y(\xi) u_k(\xi) \int_a^b \frac{(E_k - E)a'_k(E) u(\xi, E)}{(E_k - E)^2 - h^2\nu^2} dE.$$
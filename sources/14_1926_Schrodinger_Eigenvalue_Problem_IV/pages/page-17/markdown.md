Quantisierung als Eigenwertproblem

125

sondern es muß eine Integralentwicklung nach den Eigenlösungen $u(x, E)$, welche zu den Eigenwerten $a \leqslant E \leqslant b$ gehören, hinzutreten:

$$(27) \quad f(x) = \sum_{n=1}^{\infty} \varphi_n \cdot u_n(x) + \int_a^b u(x, E) \varphi(E) \, dE,$$

wobei wir zur Betonung der Analogie für die „Koeffizientenfunktion“ $\varphi(E)$ absichtlich denselben Buchstaben wählen, wie für die diskreten Koeffizienten $\varphi_n$. Hat man nun die Eigenlösung $u(x, E)$ ein für allemal durch Beheftung mit einer passenden Funktion von $E$ derart *normiert*, daß

$$(28) \quad \int dx \, \varrho(x) \int_{E'}^{E'+\Delta} u(x, E) u(x, E') \, dE' = 1 \\ \text{bzw.} = 0,$$

je nachdem $E$ dem Intervall $E'$, $E' + \Delta$ *angehört* oder nicht, dann ist in der Entwicklung (27) unter dem Integralzeichen zu setzen:

$$(29) \quad \varphi(E) = \lim_{\Delta=0} \frac{1}{\Delta} \int \varrho(\xi) f(\xi) \cdot \int_{E}^{E'+\Delta} u(\xi, E') \, dE' \cdot d\xi,$$

wobei das *erste* Integralzeichen sich wie immer auf das Grundgebiet der Variablengruppe $x$ bezieht.¹⁾ Die Erfüllbarkeit von (28) und die Existenz der Entwicklung (27) vorausgesetzt — welch beides, wie gesagt von Weyl für gewöhnliche Differentialgleichungen bewiesen ist — leuchtet die Bestimmung der „Koeffizientenfunktion“ nach (29) fast ebenso unmittelbar ein, wie die wohlbekannte Bestimmung von Fourierkoeffizienten.

Die wichtigste und schwierigste Aufgabe im konkreten Einzelfall ist dabei die Durchführung der Normierung von $u(x, E)$, d. h. die Aufsuchung derjenigen Funktion von $E$ mit welcher die zunächst nichtnormiert vorliegende Eigenlösung des Streckenspektrums zu multiplizieren ist, um darnach der Bedingung (28) genüge zu tun. Auch für diese praktische Aufgabe enthalten Hrn. Weyls obenzitierte Arbeiten sehr

¹⁾ Wie mir Hr. E. Fues mitteilt, darf man in praxi sehr häufig den Grenzprozeß unterdrücken und für das innere Integral $u(\xi, E)$ schreiben; nämlich immer dann, wenn $\int \varrho(\xi) f(\xi) u(\xi, E) \, d\xi$ existiert.

Annalen der Physik. IV. Folge. 81.

9
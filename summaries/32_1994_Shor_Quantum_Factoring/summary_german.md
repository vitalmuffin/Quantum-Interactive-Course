# Algorithms for Quantum Computation: Discrete Logarithms and Factoring

> Diese ausführliche Zusammenfassung basiert vollständig auf der deutschen Fassung des Papers. Gleichungen und Bildverweise werden in der Schreibweise des Ausgangstextes wiedergegeben.

## Bibliografischer Überblick

- **Autor:innen:** Peter W. Shor
- **Jahr:** 1994
- **Journal:** IEEE Journal on Selected Areas in Communications
- **DOI:** `10.1109/49.317578`
- **Sammlungsordner:** `32_1994_Shor_Quantum_Factoring`

## Zentrale Aussagen

- Eines davon sind BPP, das sind Probleme, die mit hoher Wahrscheinlichkeit in polynomieller Zeit gelöst werden können, wenn man auf einen Zufallszahlengenerator zugreifen kann.
- Diese Frage wurde in [11, 6, 7], aber es wurde nicht gezeigt, wie man ein Problem in quantenpolynomischer Zeit löst, das in BPP (der Klasse von Problemen, die in polynomieller Zeit mit beschränkter Fehlerwahrscheinlichkeit gelöst werden können) nicht als lösbar bekannt war.
- Eines der in dieser Arbeit enthaltenen Ergebnisse war ein Orakelproblem (ein Problem mit einer "Black-Box"-Subroutine), das in polynomieller Zeit auf einer quantenmechanischen Turingmaschine gelöst werden kann und auf einem klassischen Computer superpolynomiale Zeit benötigt.
- Dies scheint zu zeigen, dass die Klasse von Problemen, die in polynomieller Zeit auf einer dieser Maschinen gelöst werden können, möglicherweise mit beschränkter Wahrscheinlichkeit ε < 1/3 von Fehler, ist relativ robust.
- Fakt 2: Jede unitäre Matrix der Polynomgröße kann mit einer polynomiellen Anzahl elementarer unitärer Transformationen angenähert werden [10, 5, 32] und kann daher in polynomieller Zeit auf einem Quantencomputer angenähert werden.
- Da wir verwenden werden $A q$ für $q$ von exponentialer Größe müssen wir zeigen, wie diese Transformation in polynomieller Zeit durchgeführt werden kann.
- Es ist auch möglich, diese Transformation in polynomialer Zeit für alle glatten Zahlen durchzuführen $q$; Coppersmith zeigt, wie man das für $q = 2^k$ wobei im Wesentlichen die schnelle Fourier-Transformation verwendet wird, was die Anzahl der Operationen zur Faktorisierung erheblich reduziert [8].
- Tatsächlich können wir eine Menge von finden $c$, so dass mindestens einer relativ prim zu jedem Primteiler von ist $p-1$ indem das Experiment nur eine erwartete konstante Anzahl von Zeiten wiederholt wird.
- [4] gezeigt haben, dass es ausreicht, polynomielle Präzision für jede Berechnung auf einer quantenmechanischen Turingmaschine zu verwenden, um mit hoher Wahrscheinlichkeit die Antwort zu erhalten.
- Mit diesem Kriterium kann gezeigt werden, dass der Algorithmus mit mindestens einer Wahrscheinlichkeit einen Faktor n findet \( 1-1/2^{k} \) , wobei k die Anzahl der verschiedenen Primfaktoren von n ist.
- Wir berechnen nun die Wahrscheinlichkeit, dass unsere Maschine in einem bestimmten Zustand endet \( c, x^k \pmod{n}\rangle \), wobei wir annehmen können \( 0 \leq k < r \).
- \[ \left \frac {1}{q} \sum {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i (b r + k) c / q) \right ^ {2}. \tag {6.5} \]
- Die Kombination dieser Berechnung mit der unteren Schranke für die Wahrscheinlichkeit jedes guten Zustands ergibt uns, dass die Wahrscheinlichkeit, einen guten Zustand zu erhalten, mindestens bei mindestens beträgt $p/80q$, oder zumindest $1/160$ (da $q < 2p$).
- Erinnern Sie sich, dass jedes Gut c' mit mindestens einer Wahrscheinlichkeit erhalten wird 1/16q von jedem Experiment.

## Abschnittsweise Zusammenfassung

### Zusammenfassung

- Ein Computer wird allgemein als universelles Rechengerät betrachtet; d. h. es wird angenommen, dass es in der lage ist, jedes physikalische rechnergerät mit einem Rechenzeitaufwand von höchstens einem Polynomfaktor zu simulieren.
- Diese beiden Probleme gelten im Allgemeinen als schwierig auf einem klassischen Computer und dienen als Grundlage mehrerer vorgeschlagener Kryptosysteme. (Wir geben somit die ersten Beispiele der Quantenkryptoanalyse.)

### 1 Einführung

- Diese Frage wurde in [11, 6, 7], aber es wurde nicht gezeigt, wie man ein Problem in quantenpolynomischer Zeit löst, das in BPP (der Klasse von Problemen, die in polynomieller Zeit mit beschränkter Fehlerwahrscheinlichkeit gelöst werden können) nicht als lösbar bekannt war.
- Eines der in dieser Arbeit enthaltenen Ergebnisse war ein Orakelproblem (ein Problem mit einer "Black-Box"-Subroutine), das in polynomieller Zeit auf einer quantenmechanischen Turingmaschine gelöst werden kann und auf einem klassischen Computer superpolynomiale Zeit benötigt.
- Tatsächlich wird dieses Ergebnis, wenn man Simons Orakel als Unterprogramm betrachtet, zu einem Versprechensproblem, das auf einem Quantencomputer polynomiale Zeit benötigt und auf einem klassischen Computer sehr schwierig aussieht.
- Dies scheint zu zeigen, dass die Klasse von Problemen, die in polynomieller Zeit auf einer dieser Maschinen gelöst werden können, möglicherweise mit beschränkter Wahrscheinlichkeit ε < 1/3 von Fehler, ist relativ robust.
- Auch wenn nie ein Quantencomputer gebaut wird, beleuchtet diese Forschung das Problem, die Quantenmechanik auf einem klassischen Computer zu simulieren.

### 2 Quantenberechnung

- Die Wahrscheinlichkeit eines bestimmten Ergebnisses des Experiments ist proportional zum Quadrat des Absolutwerts der Summe der Amplituden aller zu diesem Ergebnis führenden Wege.
- Wenn die Maschine in einem bestimmten Schritt untersucht wird, ist die Wahrscheinlichkeit, die Basis zu sehen, der Zustand $ S {i}\rangle$ ist $ a {i} ^{2}$; nach dem Heisenbergschen Unschärfeprinzip wird jedoch das Betrachten der Maschine während der Berechnung den Rest der Berechnung stören.
- Darüber hinaus erlauben die Definitionen von Quanten-Turingmaschine und Quantenschaltung nur lokale unitäre Transformationen, also unitäre Transformationen auf einer festen Bitzahl.
- Fakt 2: Jede unitäre Matrix der Polynomgröße kann mit einer polynomiellen Anzahl elementarer unitärer Transformationen angenähert werden [10, 5, 32] und kann daher in polynomieller Zeit auf einem Quantencomputer angenähert werden.

### 3 Unitarische Umwandlungen des Gebäudes

- In diesem Abschnitt stellen wir einige Techniken zur Konstruktion unitärer Transformationen auf Quantenmaschinen vor, was dazu führt, dass wir zeigen, wie man eine bestimmte unitäre Transformation in polynomieller Zeit konstruiert.
- Diese Transformationen werden in der Regel als Matrizen angegeben, wobei sowohl Zeilen als auch Spalten nach Zuständen indiziert sind.
- Da wir verwenden werden $A q$ für $q$ von exponentialer Größe müssen wir zeigen, wie diese Transformation in polynomieller Zeit durchgeführt werden kann.
- Es ist auch möglich, diese Transformation in polynomialer Zeit für alle glatten Zahlen durchzuführen $q$; Coppersmith zeigt, wie man das für $q = 2^k$ wobei im Wesentlichen die schnelle Fourier-Transformation verwendet wird, was die Anzahl der Operationen zur Faktorisierung erheblich reduziert [8].
- Wir werden nun skizzieren, wie wir die Zeilen und Spalten von $C$ um die Matrix zu erhalten $\bigoplus {q 2} A {q 1}$.

### 4 Diskretes Logbuch: der einfache Fall

- Wir beginnen damit, einen polynomiellen Algorithmus für diskrete Logitaritümen auf einem Quantencomputer zu geben, falls $p - 1$ ist geschmeidig.
- Der Algorithmus beginnt damit, Zahlen zu "wählen" $a$ und $b$ (mod $p - 1$) gleichmäßig, sodass der Zustand der Maschine nach diesem Schritt ist
- Wir berechnen nun die Wahrscheinlichkeit, dass die Berechnung mit der Maschine im Zustand endet $ c, d, y\rangle$ mit $y \equiv g^k \pmod{p}$.
- Tatsächlich können wir eine Menge von finden $c$, so dass mindestens einer relativ prim zu jedem Primteiler von ist $p-1$ indem das Experiment nur eine erwartete konstante Anzahl von Zeiten wiederholt wird.

### 5 Eine Anmerkung zur Präzision

- Die allgemein akzeptierte theoretische Trennlinie zwischen machbar und unmöglich ist, dass polynomielle Genauigkeit (d. h. eine Anzahl von Bits logarithmisch in der Problemgröße) machbar ist und mehr nicht machbar.
- Wir müssen daher zeigen, dass die Berechnungen im vorherigen Abschnitt nur polynomielle Genauigkeit in den Amplituden verwenden müssen.
- Dann wäre im Produkt jeder Phasenwinkel höchstens um etwas anderes $\epsilon$, was ausreicht, um die Berechnung mit konstanter Erfolgswahrscheinlichkeit durchzuführen.
- [4] gezeigt haben, dass es ausreicht, polynomielle Präzision für jede Berechnung auf einer quantenmechanischen Turingmaschine zu verwenden, um mit hoher Wahrscheinlichkeit die Antwort zu erhalten.

### 6 Faktorisierung

- \[ \frac {1}{q} \sum {a = 0} ^ {q - 1} \exp (2 \pi i a c / q) c, x ^ {a} (\mathrm{mod} n) \rangle . \tag {6.3} \]
- \[ \left \frac {1}{q} \sum {a: x ^ {a} \equiv x ^ {k}} \exp (2 \pi i a c / q) \right ^ {2}. \tag {6.4} \]
- \[ \left \frac {1}{q} \sum {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i (b r + k) c / q) \right ^ {2}. \tag {6.5} \]
- \[ \left \frac {1}{q} \sum {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i b \{r c \} {q} / q) \right ^ {2}. \tag {6.6} \]
- Unter Verwendung des Theorems, dass $\phi(r)/r k/\log \log r$ für einige fest $k$ [17, Satz 328], dies zeigt, dass wir finden $r$ mindestens ein $k/\log \log r$ Bruchteil der Zeit, also nur durch Wiederholung dieses Experiments $O(\log \log r)$ Manchmal ist uns eine hohe Erfolgswahrscheinlichkeit sicher.

### 7 Diskretes Logarithmus: der allgemeine Fall

- Was wir haben, ist, dass jedes Gut $(c, d)$ Das Paar wird mit mindestens einer Wahrscheinlichkeit erzeugt $.137p/q 1/16q$, und dass mindestens ein Zehntel des Möglichen ist $c$'s sind in einer guten Situation $(c, d)$ Paar.
- Daher gilt für eine Primzahl $p t^{n t}$, ein zufälliges Gut $c'$ ist teilbar durch $p t^{n t}$ mit höchstens einer Wahrscheinlichkeit $10/p t^{n t}$.
- Wenn wir haben $t$ Gut $c'$ist die Wahrscheinlichkeit, eine Primzahl über 20 zu haben, die alle teilt, daher höchstens höchstens
- Erinnern Sie sich, dass jedes Gut c' mit mindestens einer Wahrscheinlichkeit erhalten wird 1/16q von jedem Experiment.
- Wir können somit alle Möglichkeiten für Reste modulo Potenzen von Primzahlen kleiner als 20 ausprobieren: Für jede Möglichkeit können wir das entsprechende r mit dem chinesischen Restsatz berechnen und dann prüfen, ob es sich um den gewünschten diskreten Logarithmus handelt.

### Danksagungen

- Ich möchte Jeff Lagarias dafür danken, dass er einen kritischen Fehler in der ersten Version des diskreten Log-Algorithmus gefunden und behoben hat.
- Ich möchte auch ihm, Charles Bennett, Gilles Brassard, Andrew Odlyzko, Dan Simon, Umesh Vazirani sowie anderen zu zahlreichen Korrespondenten danken, um sie aufzuzählen, für produktive Diskussionen, für Korrekturen und Verbesserungen der frühen Entwürfe dieses Artikels sowie für Hinweise auf die Literatur.

### Quellen

- P. Benioff, "Quantenmechanische Hamiltonsche Modelle von Turingmaschinen, die keine Energie dissipieren", Phys.
- C. H. Bennett, E. Bernstein, G. Brassard und U. Vazirani, "Was auf einem Quantencomputer möglich ist", Manuskript (1994).
- A. Berthiaume und G. Brassard, "Die quantenmechanische Herausforderung für die Strukturkomplexitätstheorie", in Proc.

## Wichtige Gleichungen

### 1. Abschnitt: 1 Einführung

**Kontext:** Das andere ist P P, das sind jene Probleme, die in polynomialer Zeit gelöst werden könnten, wenn Summen von exponentiell vielen Termen effizient berechnet werden könnten (wobei diese Summen die Anforderung erfüllen müssen, dass jeder Term in polynomieller Zeit berechenbar ist).

$$\mathrm{P} \subseteq \mathrm{BPP}, \mathrm{NP} \subseteq \mathrm{P}^{\# \mathrm{P}} \subseteq \mathrm{PSPACE}.$$

### 2. Abschnitt: 2 Quantenberechnung

**Kontext:** Wir werden diese Überlagerung der Zustände als folgt darstellen:

$$\sum_{i} a_{i} |S_{i}\rangle, \tag{2.1}$$

### 3. Abschnitt: 2 Quantenberechnung

**Kontext:** Angenommen, unsere Maschine befindet sich in der Überlagerung von Zuständen

$$\frac{1}{\sqrt{2}} |000\rangle + \frac{1}{2} |100\rangle - \frac{1}{2} |110\rangle \tag{2.2}$$

### 4. Abschnitt: 2 Quantenberechnung

**Kontext:** Angenommen, unsere Maschine befindet sich in der Überlagerung von Zuständen

$$\begin{array}{c|cccc} & 00 & 01 & 10 & 11 \\ 00 & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ 01 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\ 10 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ 11 & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \end{array} \tag{2.3}$$

### 5. Abschnitt: 2 Quantenberechnung

**Kontext:** Die Maschine wechselt dann zur Superposition der Zustände

$$\frac{1}{2\sqrt{2}} (|000\rangle + |001\rangle + |010\rangle + |011\rangle) + \frac{1}{2} |101\rangle + \frac{1}{2} |111\rangle. \tag{2.4}$$

### 6. Abschnitt: 2 Quantenberechnung

**Kontext:** Beachten Sie, dass das Ergebnis anders gewesen wäre, wenn wir mit der Superposition der Zustände begonnen hätten

$$\frac{1}{\sqrt{2}} |000\rangle + \frac{1}{2} |100\rangle + \frac{1}{2} |110\rangle, \tag{2.5}$$

### 7. Abschnitt: 3 Unitarische Umwandlungen des Gebäudes

**Kontext:** Wir führen die Transformation durch, die den Zustand annimmt $ a\rangle$ An den Staat

$$\frac{1}{q^{1/2}} \sum_{b=0}^{q-1} |b\rangle \exp(2\pi i ab/q). \tag{3.1}$$

### 8. Abschnitt: 3 Unitarische Umwandlungen des Gebäudes

**Kontext:** Innerhalb eines bestimmten Blocks $\alpha 2 = \beta 1$, sehen die Einträge so aus wie

$$\begin{array}{l} \sqrt{q_1} C(a, b) = \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1)} \\ = \exp(2\pi i(\alpha_1 \beta_2 + \beta_1 \beta_2 t)q_2/q) \\ = \exp(2\pi i(\alpha_1 + \alpha_2 t)\beta_2/q_1). \tag{3.5} \end{array}$$

### 9. Abschnitt: 4 Diskretes Logbuch: der einfache Fall

**Kontext:** Der Algorithmus beginnt damit, Zahlen zu "wählen" $a$ und $b$ (mod $p - 1$) gleichmäßig, sodass der Zustand der Maschine nach diesem Schritt ist

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b\rangle. \tag{4.1}$$

### 10. Abschnitt: 4 Diskretes Logbuch: der einfache Fall

**Kontext:** Wir setzen nun die Gleichung ein $a \equiv k + rb \pmod{p-1}$ im obigen Exponential.

$$\left| \frac{1}{(p-1)^2} \sum_{b=0}^{p-2} \exp \left( \frac{2\pi i}{p-1} (kc + b(d+rc)) \right) \right|^2. \tag{4.5}$$

### 11. Abschnitt: 6 Faktorisierung

**Kontext:** Die Wahrscheinlichkeit, einen gegebenen Zustand zu sehen \( c, x^{k} (\text{mod } n)\rangle \) wird somit zumindest \( 1/3r^{2} \) wenn

$$\frac{-r}{2} \leq rc - dq \leq \frac{r}{2}. \tag{6.9}$$

### 12. Abschnitt: 6 Faktorisierung

**Kontext:** Division durch $rq$ und das Umordnen der Terme ergibt

$$\left| \frac{c}{q} - \frac{d}{r} \right| \leq \frac{1}{2q}. \tag{6.10}$$

### 13. Abschnitt: 7 Diskretes Logarithmus: der allgemeine Fall

**Kontext:** Als Nächstes machen wir dasselbe wie im einfachen Fall, nämlich wählen wir $a$ und $b$ einheitlich (Mod) $p-1$), und dann berechnen $g^a x^{-b} \pmod{p}$.

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b, g^a x^{-b} \pmod{p}\rangle. \tag{7.1}$$

### 14. Abschnitt: 7 Diskretes Logarithmus: der allgemeine Fall

**Kontext:** Wir werden zeigen, dass wir, wenn wir genügend "gute" Ausgaben erhalten, trotzdem ableiten können $r$, und dass außerdem die Chance, ein "gutes" Ergebnis zu erzielen, konstant ist.

$$|\{T\}_q| = |rc + d - \frac{r}{p-1} \{c(p-1)\}_q - jq| \leq \frac{1}{2}, \tag{7.9}$$

### 15. Abschnitt: 7 Diskretes Logarithmus: der allgemeine Fall

**Kontext:** wobei $j$ ist die ganzzahligste Zahl zu $T/q$, dann gilt als $b$ variiert zwischen 0 und $p - 2$, die Phase des ersten Exponentialterms in Gleichung (7.6) variiert höchstens über die Hälfte des Einheitskreises.

$$|\{c(p - 1)\}_q| \le q/20, \tag{7.10}$$

### 16. Abschnitt: 7 Diskretes Logarithmus: der allgemeine Fall

**Kontext:** Somit ist die Komponente der Amplitude der ersten Exponentialgröße in Gleichung (7,6) in Richtung

$$\exp(\pi i W) \tag{7.12}$$

### 17. Abschnitt: 7 Diskretes Logarithmus: der allgemeine Fall

**Kontext:** Da $p < q$, und aus Bedingung (7.9), $ W \le 1/2$, wenn man alles zusammensetzt, die Wahrscheinlichkeit, in einen Zustand zu gelangen, $ c, d, y)$ die sowohl Bedingung (7.9) als auch (7.10) erfüllt, mindestens ist

$$\left( \frac{1}{q} \frac{2}{\pi} \int_{\pi/10}^{7\pi/20} \cos t \, dt \right)^2, \tag{7.13}$$

### 18. Abschnitt: 7 Diskretes Logarithmus: der allgemeine Fall

**Kontext:** Wenn wir haben $t$ Gut $c'$ist die Wahrscheinlichkeit, eine Primzahl über 20 zu haben, die alle teilt, daher höchstens höchstens

$$\sum_{\substack{p_t^{n_t} > 20 \\ p_t^{n_t} \le p - 1}} \left( \frac{10}{p_t^{n_t}} \right)^t, \tag{7.16}$$

## Abbildungen und Bildverweise

Im Text wurden keine Markdown-Bildverweise gefunden.
## Wichtige Tabellen

Im Text wurden keine Markdown-Tabellen gefunden.
## Ergebnisse und Bedeutung

- Ein Computer wird allgemein als universelles Rechengerät betrachtet; d. h. es wird angenommen, dass es in der lage ist, jedes physikalische rechnergerät mit einem Rechenzeitaufwand von höchstens einem Polynomfaktor zu simulieren.
- Es ist nicht klar, ob dies unter Berücksichtigung der Quantenmechanik noch gilt.
- Mehrere Forscher, beginnend mit David Deutsch, haben Modelle für quantenmechanische Computer entwickelt und deren rechnerische Eigenschaften untersucht.
- Dieses Paper stellt Las Vegas Algorithmen vor, um diskrete Logarithmen zu finden und ganze Zahlen auf einem Quantencomputer zu faktorisieren, die eine Anzahl von Schritten durchführen, die polynomiell in der Eingabegröße sind, z. B. die Anzahl der Ziffern der zu faktorisierenden Ganzzahl.
- Diese beiden Probleme gelten im Allgemeinen als schwierig auf einem klassischen Computer und dienen als Grundlage mehrerer vorgeschlagener Kryptosysteme. (Wir geben somit die ersten Beispiele der Quantenkryptoanalyse.)

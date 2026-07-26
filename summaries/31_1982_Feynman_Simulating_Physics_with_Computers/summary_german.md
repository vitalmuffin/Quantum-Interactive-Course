# Simulating Physics with Computers

> Diese ausführliche Zusammenfassung basiert vollständig auf der deutschen Fassung des Papers. Gleichungen und Bildverweise werden in der Schreibweise des Ausgangstextes wiedergegeben.

## Bibliografischer Überblick

- **Autor:innen:** Richard P. Feynman
- **Jahr:** 1982
- **Journal:** International Journal of Theoretical Physics
- **DOI:** `10.1007/BF02650179`
- **Sammlungsordner:** `31_1982_Feynman_Simulating_Physics_with_Computers`

## Zentrale Aussagen

- Die erste Frage ist: Welche Art von Computer werden wir verwenden, um Physik zu simulieren?
- Daher ist meine Frage: Kann Physik von einem universellen Computer simuliert werden?
- Es gibt natürlich eine Art approximative Simulation, bei der man numerische Algorithmen für Differentialgleichungen entwirft und dann den Computer verwendet, um diese Algorithmen zu berechnen und eine ungefähre Vorstellung davon zu bekommen, was die Physik eigentlich tun sollte.
- Ich möchte über die Möglichkeit sprechen, dass es eine Genau Simulation, die der Computer machen wird Genau Dasselbe wie die Natur.
- Wenn dies bewiesen werden soll und die Art des Computers so ist, wie ich es bereits erklärt habe, dann wird es notwendig sein, dass Alles das in einem endlichen Volumen von Raum und Zeit geschieht, müsste mit einer endlichen Anzahl logischer Operationen exakt analytierbar sein.
- Ich weiß also, dass Quantenmechanik offenbar Wahrscheinlichkeit beinhaltet – und deshalb möchte ich über die Simulation der Wahrscheinlichkeit sprechen.
- Eine Möglichkeit, einen Computer zu haben, der eine probabilistische Theorie simuliert, also etwas, das eine Wahrscheinlichkeit enthält, wäre, die Wahrscheinlichkeit zu berechnen und diese Zahl dann so zu interpretieren, dass sie die Natur darstellt.
- Mit anderen Worten, wir könnten uns einen probabilistischen Simulator probabilistischer Natur vorstellen und vollkommen zufrieden damit sein, bei dem die Maschine nicht genau das tut, was die Natur tut, aber wenn man eine bestimmte Art von Experiment ausreichend oft wiederholt, um die Wahrscheinlichkeit der Natur zu bestimmen, dann führt man das entsprechende Experiment am Computer durch, Du bekommst die entsprechende Wahrscheinlichkeit mit der entsprechenden Genauigkeit (mit derselben Art von Genauigkeit wie Statistiken).
- Jetzt gehe ich explizit zur Frage, wie wir mit einem Computer – einem universellen Automaten oder so etwas – die quantenmechanischen Effekte simulieren können. (Die übliche Formulierung ist, dass die Quantenmechanik eine Art Differentialgleichung für eine Funktion besitzt $\psi$.) Wenn du ein einzelnes Teilchen hast, $\psi$ ist eine Funktion von $x$ und $t$, und diese Differentialgleichung könnte simuliert werden, genau wie meine vorherige probabilistische Gleichung.
- Diese beiden Gleichungen sind korrekt, und daher würde man hoffen, dass vielleicht $W(x, p)$ ist die Wahrscheinlichkeit zu finden $x$ und $p$.
- Wenn du eine Wahrscheinlichkeit erfinden kannst. $M$ So schreibst du die Gleichungen entsprechend der normalen Logik, das sind die korrekten Gleichungen, die reellen, korrekten, quantenmechanischen Gleichungen dafür. $F$, und deshalb würdest du sagen: Okay, ich kann es mit einem probabilistischen Computer nachahmen!
- Die Wahrscheinlichkeit, es im gewöhnlichen Strahl zu finden, plus die Wahrscheinlichkeit, es im außergewöhnlichen Strahl zu finden, beträgt immer 1 – diese Regel muss man haben.
- Antwort: Nein, sie sind gleich. $P {OO}$ ist die Gemeinsame Wahrscheinlichkeit dass sowohl du als auch ich einen gewöhnlichen Strahl beobachten, und $P {EE}$ ist die Gemeinsame Wahrscheinlichkeit für zwei
- Dann sagt man: Kann ich das mit einem Gerät imitieren, das die gleichen Ergebnisse liefert und lokal funktioniert, und man versucht, eine Art Methode dafür zu erfinden, und wenn man es im normalen Denken macht, stellt man fest, dass man nicht mit der gleichen Wahrscheinlichkeit dorthin kommt.

## Abschnittsweise Zusammenfassung

### 1. EINLEITUNG

- Ich möchte über das Problem sprechen, Physik mit Computern zu simulieren, und das meine ich auf eine bestimmte Weise, die ich erklären werde.
- Aber die physikalische Welt ist quantenmechanisch, und daher ist das eigentliche Problem die Simulation der Quantenphysik – worüber ich eigentlich sprechen möchte, aber darauf komme ich später noch ein.
- Es gibt natürlich eine Art approximative Simulation, bei der man numerische Algorithmen für Differentialgleichungen entwirft und dann den Computer verwendet, um diese Algorithmen zu berechnen und eine ungefähre Vorstellung davon zu bekommen, was die Physik eigentlich tun sollte.
- Das ist ein interessantes Thema, aber nicht das, worüber ich sprechen möchte.
- Das heißt, wenn du sagst, ich möchte so viel Physik erklären, kann ich es genau machen und brauche einen Computer in einer bestimmten Größe.

### 2. ZEIT SIMULIEREN

- Eine Art, wie wir Zeit simulieren – zum Beispiel bei zellulären Automaten – ist, zu sagen, dass "der Computer von Zustand zu Zustand wechselt." Aber eigentlich benutzt man Intuition, die die Idee von Zeit beinhaltet – man geht von Zustand zu Zustand.
- Und deshalb wird die Zeit (übrigens, wie der Raum im Fall von zellulären Automaten) überhaupt nicht simuliert, sondern im Computer nachgebildet.
- Die Position zu zwei verschiedenen Zeiten in der Vergangenheit (so oder so braucht man an jedem Punkt zwei Informationen) berechnet prinzipiell die Zukunft.
- Also ist klassische Physik Lokal , Kausal , und Reversibel , und daher offenbar recht anpassungsfähig (abgesehen von der Diskretheit und so weiter, die ich bereits erwähnt habe) für Computersimulationen.

### 3. WAHRSCHEINLICHKEITSSIMULATION

- Du weißt ja, wie es immer ist: Jede neue Idee dauert ein oder zwei Generationen, bis klar wird, dass es kein wirkliches Problem gibt.
- Ich kann das eigentliche Problem nicht definieren, daher vermute ich, dass es kein wirkliches Problem gibt, aber ich bin mir ziemlich sicher, dass es kein wirkliches Problem gibt.
- Eine Möglichkeit, einen Computer zu haben, der eine probabilistische Theorie simuliert, also etwas, das eine Wahrscheinlichkeit enthält, wäre, die Wahrscheinlichkeit zu berechnen und diese Zahl dann so zu interpretieren, dass sie die Natur darstellt.
- Wenn du dasselbe Experiment im Computer eine große Anzahl von Mal wiederholst (und das dauert natürlich nicht länger als dasselbe in der Natur), ergibt es die Frequenz eines bestimmten Endzustands proportional zur Anzahl der Male, mit ungefähr derselben Rate (plus
- Mit anderen Worten, wir könnten uns einen probabilistischen Simulator probabilistischer Natur vorstellen und vollkommen zufrieden damit sein, bei dem die Maschine nicht genau das tut, was die Natur tut, aber wenn man eine bestimmte Art von Experiment ausreichend oft wiederholt, um die Wahrscheinlichkeit der Natur zu bestimmen, dann führt man das entsprechende Experiment am Computer durch, Du bekommst die entsprechende Wahrscheinlichkeit mit der entsprechenden Genauigkeit (mit derselben Art von Genauigkeit wie Statistiken).
- Jetzt gehe ich explizit zur Frage, wie wir mit einem Computer – einem universellen Automaten oder so etwas – die quantenmechanischen Effekte simulieren können. (Die übliche Formulierung ist, dass die Quantenmechanik eine Art Differentialgleichung für eine Funktion besitzt $\psi$.) Wenn du ein einzelnes Teilchen hast, $\psi$ ist eine Funktion von $x$ und $t$, und diese Differentialgleichung könnte simuliert werden, genau wie meine vorherige probabilistische Gleichung.
- Wir können unsere Regel darüber aufgeben, was der Computer war, wir können sagen: Lass den Computer selbst aus quantenmechanischen Elementen bestehen, die quantenmechanischen Gesetzen gehorchen.

### 4. QUANTENCOMPUTER – UNIVERSELLE QUANTENSIMULATOREN

- Es gäbe einen Operator $a$ die vernichtet wenn der Punkt besetzt ist, ändert er sich zu unbesetzt.
- Die Frage ist: Wenn wir einen Hamiltonoperator schreiben würden, der nur diese Operatoren enthält, lokal mit entsprechenden Operatoren an den anderen Raumzeitpunkten gekoppelt, könnten wir dann jedes quantenmechanische System imitieren, das diskret ist und eine endliche Anzahl von Freiheitsgraden besitzt?
- Ich weiß fast sicher, dass wir das für jedes quantenmechanische System tun könnten, das Bose-Teilchen beinhaltet.
- Ich bin mir nicht sicher, ob das ausreicht, weil ich mir nicht sicher bin, ob es Fermi-Partikel beseitigt.

### 5. KÖNNEN QUANTENSYSTEME PROBABILISTISCH VON EINEM KLASSISCHEN COMPUTER SIMULIERT WERDEN?

- Dies wird als das Problem der versteckten Variablen bezeichnet: Es ist unmöglich, die Ergebnisse der Quantenmechanik mit einem klassischen universellen Bauelement darzustellen.
- Wenn "Wahrscheinlichkeit" alle mathematischen Eigenschaften einer Wahrscheinlichkeit hätte, könnten wir die Anführungszeichen entfernen und simulieren. $W(x, p)$ ist die "Wahrscheinlichkeit", dass das Teilchen Position hat $x$ und Impuls $p$ (per $dx$ und $dp$).
- Diese beiden Gleichungen sind korrekt, und daher würde man hoffen, dass vielleicht $W(x, p)$ ist die Wahrscheinlichkeit zu finden $x$ und $p$.
- Wenn Sie zum Beispiel wissen möchten, ob der erste Index positiv ist, wäre die Wahrscheinlichkeit für
- Es gibt andere lineare Kombinationen, zu denen Sie Fragen stellen können, aber Sie scheinen keine Fragen zu einer Person stellen zu können $f$.

### 6. NEGATIVE WAHRSCHEINLICHKEITEN

- Die Wahrscheinlichkeit, den ersten Index negativ zu finden, ist die Summe $f {-+} + f {-+}$ Das sind auch 50 %.
- Die Wahrscheinlichkeit, den zweiten Index positiv zu finden, ist die Summe $f {++} + f {-+}$ was neun Zehntel ist, die Wahrscheinlichkeit, es negativ zu finden, ist $f {+-} + f {--}$ Das ist ein Zehntel, völlig in Ordnung, es ist entweder Plus oder Minus.
- Der einzige Unterschied zwischen einer probabilistischen klassischen Welt und den Gleichungen der Quantenwelt besteht darin, dass es irgendwie so aussieht, als müssten die Wahrscheinlichkeiten negativ werden, und dass wir, soweit ich weiß, nicht wissen, wie man simuliert.

### 7. POLARISATION VON PHOTONEN – ZWEIZUSTANDSSYSTEME

- Wenn man ein polarisiertes Photon einsetzt, geht es zu einem Strahl, dem gewöhnlichen Strahl, oder einem anderen, dem außergewöhnlichen.
- Die Wahrscheinlichkeit, es im gewöhnlichen Strahl zu finden, plus die Wahrscheinlichkeit, es im außergewöhnlichen Strahl zu finden, beträgt immer 1 – diese Regel muss man haben.
- Wenn das Photon ist $O$ Aus dem ersten Calcit ergibt der zweite Calcit $O-O$ mit Wahrscheinlichkeit $\cos^2\phi$ oder $O-E$ mit der komplementären Wahrscheinlichkeit $1-\cos^1\phi=\sin^2\phi$.
- Ebenso gilt ein $E$ Photon ergibt ein $E-O$ mit der Wahrscheinlichkeit $\sin^2\phi$ oder ein $E-E$ mit der Wahrscheinlichkeit $\cos^2\phi$.

### 8. ZWEI-PHOTONEN-KORRELATIONSEXPERIMENT

- Quantentheorie und Experiment sind sich einig, dass die Wahrscheinlichkeit $P {OO}$ dass wir beide ein gewöhnliches Photon detektieren, ist
- Übrigens ergänzen sich die Ergebnisse voneinander im rechten Winkel, denn denken Sie daran, es ist immer entweder außergewöhnlich oder gewöhnlich; Also, wenn du dich drehst $90^{\circ}$, was früher ein gewöhnlicher Strahl war, wird zum außergewöhnlichen Strahl.
- Daher hat es in welchem Zustand er sich befindet, ein vorhersehbares Muster, bei dem man entweder eine Vorhersage von gewöhnlich oder von außergewöhnlich hat – drei und drei –, weil sie im rechten Winkel nicht dieselbe Farbe haben.
- Jedes Mal, wenn wir ein Paar Photonen herstellen und dieses Experiment immer wieder wiederholen, muss es nicht dasselbe sein wie Abbildung 5a.
- Nehmen wir an, dass beim nächsten Experiment mein Photon sein wird $O$ oder $E$ für jeden Winkel wie in Abbildung 5c.
- Aber was auch immer es ist, dein Muster muss genau mein Muster sein – sonst könntest du nicht genau vorhersagen, was ich bekomme, indem du den entsprechenden Winkel messst.
- Jedes Mal, wenn wir das Experiment durchführen, erhalten wir unterschiedliche Muster; Und es ist einfach: Es gibt nur sechs Punkte, und drei davon sind weiß, und man jagt ihnen auf verschiedene Arten hinterher – alles kann passieren.

### 9. DISKUSSION

- Frage: Um es zu interpretieren: Sie sprachen zunächst von der Wahrscheinlichkeit von A gegeben B gegenüber der Wahrscheinlichkeit von A und B gemeinsam – das ist die Wahrscheinlichkeit, dass ein Beobachter das Ergebnis sieht und dem anderen eine Wahrscheinlichkeit zuweist; Und dann hast du das Paradoxon des quantenmechanischen Ergebnisses angesprochen, dass $3/4$, und dieses Wesen $2/3$.
- Ist nicht die eine eine gemeinsame Wahrscheinlichkeit und die andere eine bedingte?
- Wenn du zum Beispiel in deiner Theorie ein elektrisches Feld haben würdest, dann könnte das elektrische Feld nicht (wenn es imizitierbar, berechenbar mit einer endlichen Anzahl von Elementen sein soll) ein
- All diese Dinge deuten darauf hin, dass es irgendwie wahr ist, dass die physische Welt auf diskrete Weise darstellbar ist, denn jedes Mal, wenn man in so eine Zwickmühle gerät, entdeckt man, dass das Experiment genau das tut, was nötig ist, um den Problemen zu entkommen, die entstehen würden, wenn das elektrische Feld auf null steigt oder man niemals einen Stern jenseits einer bestimmten Entfernung sehen könnte, Weil das Feld unter die Anzahl der Ziffern gefallen wäre, die deine Welt tragen kann.

## Wichtige Gleichungen

### 1. Abschnitt: 2. ZEIT SIMULIEREN

**Kontext:** Und dann könnten wir sagen, dass eine 'Computer'-Regel (jetzt würde Computer in Anführungszeichen stehen, weil es nicht die Standardart von Computer ist, die in der Zeit arbeitet) lautet: Wir haben einen Zustand $s i$ an jedem Punkt $i$ in Raum-Zeit. (Siehe Abbildung 1.) Der Staat $s i$ am Raumzeitpunkt $i$ ist eine gegebene Funktion $F i(s j, s k, \ldots)$ des Zustands an den Punkten $j, k$ In irgendeiner Gegend von $i$:

$$
s_i = F_i(s_j, s_k, \ldots)
$$

### 2. Abschnitt: 3. WAHRSCHEINLICHKEITSSIMULATION

**Kontext:** Ein typisches Beispiel für eine solche Wahrscheinlichkeit könnte eine Differentialgleichung erfüllen, zum Beispiel wenn das Teilchen diffundiert:

$$
\frac{\partial P(x, t)}{\partial t} = - \nabla^2 P(x, t)
$$

### 3. Abschnitt: 3. WAHRSCHEINLICHKEITSSIMULATION

**Kontext:** Wenn wir es getan hätten berechnet Diese Wahrscheinlichkeit müssten wir trotzdem die Integration durchführen

$$
P_A(x_A) = \int P(x_A, x_B) dx_B
$$

### 4. Abschnitt: 3. WAHRSCHEINLICHKEITSSIMULATION

**Kontext:** Sie erfüllt eine Gleichung, so dass bei jedem Zeitsprung

$$
P_{i+1}(\{s\}) = \sum_{\{s'\}} \left[ \prod_i m(s_i | s'_j, s'_k \ldots) \right] P_i(\{s'\})
$$

### 5. Abschnitt: 4. QUANTENCOMPUTER – UNIVERSELLE QUANTENSIMULATOREN

**Kontext:** Die Mathematik der quantenmechanischen Operatoren, die mit diesem Punkt verbunden sind, wäre sehr einfach.

$$
\begin{array}{l}
a = \text{ANNIHILATE} = \begin{array}{c|c|c}
\text{OCC} & \text{ON} & \\
\text{ON} & 0 & 0 \\
\hline
\text{ON} & 1 & 0
\end{array}
= \frac{1}{2}(\sigma_x - i\sigma_y) \\
a^* = \text{CREATE} = \begin{array}{c|c|c}
\hline 0 & 1 & \\
\hline 0 & 0 &
\end{array}
= \frac{1}{2}(\sigma_x + i\sigma_y) \\
n = \text{NUMBER} = \begin{array}{c|c|c}
\hline 1 & 0 & \\
\hline 0 & 0 &
\end{array}
= a^*a = \frac{1}{2}(1 + \sigma_z) \\
\mathbb{1} = \text{IDENTITY} = \begin{array}{c|c|c}
\hline 1 & 0 & \\
\hline 0 & 1 &
\end{array}
\end{array}
$$

### 6. Abschnitt: 4. QUANTENCOMPUTER – UNIVERSELLE QUANTENSIMULATOREN

**Kontext:** Sie haben eine weitere Reihe von Matrizen erfunden, die Pauli $\sigma$ Matrizen:

$$
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \mathbb{1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

### 7. Abschnitt: 5. KÖNNEN QUANTENSYSTEME PROBABILISTISCH VON EINEM KLASSISCHEN COMPUTER SIMULIERT WERDEN?

**Kontext:** Und so wende ich mich bei einer leichten Erhöhung der Komplexität der Gleichungen (und nicht sehr stark) zur Dichtematrix, die für ein einzelnes Teilchen mit Koordinate $x$ im reinen Zustand der Wellenfunktion $\psi(x)$ ist

$$
\rho(x, x') = \psi^*(x)\psi(x')
$$

### 8. Abschnitt: 5. KÖNNEN QUANTENSYSTEME PROBABILISTISCH VON EINEM KLASSISCHEN COMPUTER SIMULIERT WERDEN?

**Kontext:** Zum Beispiel, wenn ein Zustand $\psi(x)$ ist nicht sicher, aber ist $\psi \alpha$ mit der Wahrscheinlichkeit $p \alpha$ dann ist die Dichtematrix die passende gewichtete Summe der Matrix für jeden Zustand $\alpha$:

$$
\rho(x, x') = \sum_\alpha p_\alpha \psi_\alpha^*(x)\psi a(x').
$$

### 9. Abschnitt: 5. KÖNNEN QUANTENSYSTEME PROBABILISTISCH VON EINEM KLASSISCHEN COMPUTER SIMULIERT WERDEN?

**Kontext:** Eine Größe, die Eigenschaften besitzt, die den klassischen Wahrscheinlichkeiten noch ähnlicher sind, ist die Wigner-Funktion, eine einfache Umformulierung der Dichtematrix; für ein

$$W(x, p) = \int \rho \left( x + \frac{y}{2}, x - \frac{y}{2} \right) e^{ipy} dy$$

### 10. Abschnitt: 5. KÖNNEN QUANTENSYSTEME PROBABILISTISCH VON EINEM KLASSISCHEN COMPUTER SIMULIERT WERDEN?

**Kontext:** Wenn Sie zum Beispiel wissen möchten, ob der erste Index positiv ist, wäre die Wahrscheinlichkeit für

$$\text{Prob(first index is } +) = f_{++} + f_{+-} \quad [\text{spin } z \text{ up}]$$

### 11. Abschnitt: 5. KÖNNEN QUANTENSYSTEME PROBABILISTISCH VON EINEM KLASSISCHEN COMPUTER SIMULIERT WERDEN?

**Kontext:** Oder die Wahrscheinlichkeit, dass es keine Übereinstimmung zwischen den Indizes gibt, dass sie unterschiedlich sind,

$$
\operatorname{Prob}(\text{no match}) = f_{+-} + f_{-+} \quad [\text{spin } y \text{ down}]
$$

### 12. Abschnitt: 6. NEGATIVE WAHRSCHEINLICHKEITEN

**Kontext:** Für viele wechselwirkende Spins auf einem Gitter können wir nun eine 'Wahrscheinlichkeit' (die Anführungszeichen erinnern uns daran, dass es noch eine Frage gibt, ob es sich um eine Wahrscheinlichkeit handelt) für korrelierte Möglichkeiten angeben:

$$
F(s_1, s_2, \dots, s_N) \quad (s_i \in \{++, +-, -+, --\})
$$

### 13. Abschnitt: 6. NEGATIVE WAHRSCHEINLICHKEITEN

**Kontext:** Als Nächstes, wenn ich nach der quantenmechanischen Gleichung suche, die mir sagt, was die Änderungen von $F$ mit der Zeit sind sie genau von der Form, die ich oben für die klassische Theorie beschrieben habe:

$$
F_{i+1}(\{s\}) = \sum_{(s')} \left[ \prod_i M(s_i | s'_j, s'_k \dots) \right] F_i(\{s'\})
$$

### 14. Abschnitt: 6. NEGATIVE WAHRSCHEINLICHKEITEN

**Kontext:** Die $M$, die sogenannte 'Wahrscheinlichkeit', von einer Bedingung zur anderen zu wechseln, ist selbst nicht positiv; wenn ich den ganzen Weg zurück in die $f$ Für ein einzelnes Objekt ist es wiederum nicht unbedingt positiv.

$$
f_{++} = 0.6 \quad f_{+-} = -0.1 \quad f_{-+} = 0.3 \quad f_{--} = 0.2
$$

### 15. Abschnitt: 8. ZWEI-PHOTONEN-KORRELATIONSEXPERIMENT

**Kontext:** Quantentheorie und Experiment sind sich einig, dass die Wahrscheinlichkeit $P {OO}$ dass wir beide ein gewöhnliches Photon detektieren, ist

$$P_{OO} = \frac{1}{2} \cos^2(\phi_2 - \phi_1)$$

### 16. Abschnitt: 8. ZWEI-PHOTONEN-KORRELATIONSEXPERIMENT

**Kontext:** Wenn $p {\alpha\beta}$ ist die konjunktive Wahrscheinlichkeit, das Bedingungspaar zu finden $\alpha, \beta$, die Wahrscheinlichkeit $P {OO}$ die wir beide beobachten $O$ Strahlen ist

$$
P_{OO}(\phi_1, \phi_2) = \sum_{\alpha\beta} p_{\alpha\beta} f_\alpha(\phi_1) g_\beta(\phi_2) \quad \sum_{\alpha\beta} p_{\alpha\beta} = 1
$$

### 17. Abschnitt: 8. ZWEI-PHOTONEN-KORRELATIONSEXPERIMENT

**Kontext:** Wenn $p {\alpha\beta}$ ist die konjunktive Wahrscheinlichkeit, das Bedingungspaar zu finden $\alpha, \beta$, die Wahrscheinlichkeit $P {OO}$ die wir beide beobachten $O$ Strahlen ist

$$
P_{OE}(\phi_1, \phi_2) = \sum_{\alpha\beta} p_{\alpha\beta} (1 - f_\alpha(\phi_1)) g_\beta(\phi_2) \quad \text{etc.}
$$

### 18. Abschnitt: 9. DISKUSSION

**Kontext:** Antwort: Nein, sie sind gleich. $P {OO}$ ist die Gemeinsame Wahrscheinlichkeit dass sowohl du als auch ich einen gewöhnlichen Strahl beobachten, und $P {EE}$ ist die Gemeinsame Wahrscheinlichkeit für zwei

$$
P_{OO} + P_{EE} = \cos^2 30^\circ = 3/4
$$

## Abbildungen und Bildverweise

### 1. 2. ZEIT SIMULIEREN

![img-0.jpeg](img-0.jpeg)

**Kontext:** Und dann könnten wir sagen, dass eine 'Computer'-Regel (jetzt würde Computer in Anführungszeichen stehen, weil es nicht die Standardart von Computer ist, die in der Zeit arbeitet) lautet: Wir haben einen Zustand $s i$ an jedem Punkt $i$ in Raum-Zeit. (Siehe Abbildung 1.) Der Staat $s i$ am Raumzeitpunkt $i$ ist eine gegebene Funktion $F i(s j, s k, \ldots)$ des Zustands an den Punkten $j, k$ In irgendeiner Gegend von $i$:

### 2. 7. POLARISATION VON PHOTONEN – ZWEIZUSTANDSSYSTEME

![img-1.jpeg](img-1.jpeg)

**Kontext:** Und dann erscheint der außergewöhnliche Strahl des ersten als der $E-O$ Ray, und dann gibt es noch ein $E-E$ Ray, alles klar.

### 3. 7. POLARISATION VON PHOTONEN – ZWEIZUSTANDSSYSTEME

![img-2.jpeg](img-2.jpeg)

**Kontext:** Und dann erscheint der außergewöhnliche Strahl des ersten als der $E-O$ Ray, und dann gibt es noch ein $E-E$ Ray, alles klar.

### 4. 8. ZWEI-PHOTONEN-KORRELATIONSEXPERIMENT

![img-3.jpeg](img-3.jpeg)

**Kontext:** Die Wahrscheinlichkeit $P {OE}$ das finde ich $O$ und du findest $E$ ist

### 5. 8. ZWEI-PHOTONEN-KORRELATIONSEXPERIMENT

![img-4.jpeg](img-4.jpeg)

**Kontext:** Mit welcher Wahrscheinlichkeit würden wir das gleiche Ergebnis erhalten, dass sie

## Wichtige Tabellen

Im Text wurden keine Markdown-Tabellen gefunden.
## Ergebnisse und Bedeutung

- Übrigens ergänzen sich die Ergebnisse voneinander im rechten Winkel, denn denken Sie daran, es ist immer entweder außergewöhnlich oder gewöhnlich; Also, wenn du dich drehst $90^{\circ}$, was früher ein gewöhnlicher Strahl war, wird zum außergewöhnlichen Strahl.
- Daher hat es in welchem Zustand er sich befindet, ein vorhersehbares Muster, bei dem man entweder eine Vorhersage von gewöhnlich oder von außergewöhnlich hat – drei und drei –, weil sie im rechten Winkel nicht dieselbe Farbe haben.
- Man misst einfach bei $60^{\circ}$, und du wirst weiß finden, und deshalb wirst du weiß oder gewöhnlich für mich vorhersagen.
- Jedes Mal, wenn wir das Experiment durchführen, ist das Muster vielleicht nicht dasselbe.
- Jedes Mal, wenn wir das Experiment durchführen, erhalten wir unterschiedliche Muster; Und es ist einfach: Es gibt nur sechs Punkte, und drei davon sind weiß, und man jagt ihnen auf verschiedene Arten hinterher – alles kann passieren.
- Wenn wir im gleichen Winkel messen, stellen wir immer fest, dass wir bei einer solchen Anordnung das gleiche Ergebnis erzielen würden.
- Angenommen, wir messen nun bei $\phi 2 - \phi 1 = 30^{\circ}$, und fragen: Mit welcher Wahrscheinlichkeit erhalten wir dasselbe Ergebnis?
- All diese Dinge deuten darauf hin, dass es irgendwie wahr ist, dass die physische Welt auf diskrete Weise darstellbar ist, denn jedes Mal, wenn man in so eine Zwickmühle gerät, entdeckt man, dass das Experiment genau das tut, was nötig ist, um den Problemen zu entkommen, die entstehen würden, wenn das elektrische Feld auf null steigt oder man niemals einen Stern jenseits einer bestimmten Entfernung sehen könnte, Weil das Feld unter die Anzahl der Ziffern gefallen wäre, die deine Welt tragen kann.

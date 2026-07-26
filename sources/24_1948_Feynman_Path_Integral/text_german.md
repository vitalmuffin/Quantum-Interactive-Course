R. P. Feynman, Rev. of Mod. Phys., 20, 367

1948

# Raum-Zeit-Ansatz in der nicht-relativistischen Quantenmechanik

R.P. Feynman  
Cornell Universität,  
Ithaca, New York

Nachdruck in "Quantum Electrodynamics", herausgegeben von Julian Schwinger

## Zusammenfassung

Die nicht-relativistische Quantenmechanik wird hier auf eine andere Weise formuliert. Sie ist jedoch mathematisch äquivalent zur bekannten Formulierung. In der Quantenmechanik ist die Wahrscheinlichkeit eines Ereignisses, das auf verschiedene Arten eintreten kann, das absolute Quadrat einer Summe komplexer Beiträge, jeweils eines aus jeder alternativen Richtung. Die Wahrscheinlichkeit, dass ein Teilchen eine Bahn besitzt. $x(t)$ Irgendwo in einem Bereich der Raumzeit liegt das Quadrat einer Summe der Beiträge, einer von jedem Pfad im Bereich. Der Beitrag eines einzelnen Pfades wird als Exponentialfaktor postuliert, dessen (imaginäre) Phase die klassische Wirkung ist (in Einheiten von $\hbar$) für den betreffenden Pfad. Der Gesamtbeitrag aller erreichten Pfade $x, t$ aus der Vergangenheit ist die Wellenfunktion $\psi(x, t)$. Dies erfüllt die Schrödingersche Gleichung. Die Beziehung zur Matrix- und Operatoralgebra wird diskutiert. Anwendungen werden insbesondere angezeigt, um die Koordinaten der Feldoszillatoren aus den Gleichungen der Quantenelektrodynamik zu eliminieren.

## 1. Einleitung

Es ist eine merkwürdige historische Tatsache, dass die moderne Quantenmechanik mit zwei ganz unterschiedlichen mathematischen Formulierungen begann: der Differentialgleichung von

1

Schrödinger und die Matrixalgebra von Heisenberg. Die beiden offenbar unterschiedlichen Ansätze erwiesen sich als mathematisch äquivalent. Diese beiden Standpunkte sollten sich ergänzen und letztlich in Diracs Transformationstheorie zusammengeführt werden.

Diese Arbeit wird im Wesentlichen eine dritte Formulierung der nichtrelativistischen Quantentheorie beschreiben. Diese Formulierung wurde von einigen von Diracs¹,² Bemerkungen zur Beziehung der klassischen Wirkung³ zur Quantenmechanik vorgeschlagen. Eine Wahrscheinlichkeitsamplitude ist mit der gesamten Bewegung eines Teilchens als Funktion der Zeit verbunden, und nicht einfach mit einer Position des Teilchens zu einem bestimmten Zeitpunkt.

Die Formulierung ist mathematisch äquivalent zu den gebräuchlicheren Formulierungen. Es gibt daher keine grundlegend neuen Ergebnisse. Es macht jedoch Freude, alte Dinge aus einer neuen Perspektive zu erkennen. Außerdem gibt es Probleme, bei denen die neue Sichtweise einen deutlichen Vorteil bietet. Wenn beispielsweise zwei Systeme A und B interagieren, können die Koordinaten eines der Systeme, zum Beispiel B, aus den Gleichungen zur Beschreibung der Bewegung von A eliminiert werden. Die Wechselwirkung mit B wird durch eine Änderung der Formel für die Wahrscheinlichkeitsamplitude dargestellt, die mit einer Bewegung von A verbunden ist. Sie ist analog zur klassischen Situation, in der der Effekt von B durch eine Änderung der Bewegungsgleichungen von A dargestellt werden kann (durch die Einführung von Termen, die Kräfte repräsentieren, die auf A wirken). Auf diese Weise können die Koordinaten des Transversals sowie der Längsfeldoszillatoren aus den Gleichungen der Quantenelektrodynamik eliminiert werden.

Darüber hinaus besteht immer die Hoffnung, dass die neue Sichtweise eine Idee zur Änderung der aktuellen Theorien inspiriert, eine notwendige Änderung, um die heutigen Experimente einzubeziehen.

Zunächst diskutieren wir das allgemeine Konzept der Superposition von Wahrscheinlichkeitsamplituden in der Quantenmechanik. Wir zeigen dann, wie dieses Konzept direkt erweitert werden kann, um eine Wahrscheinlichkeitsamplitude für jede Bewegung oder jeden Weg (Position vs. Zeit) in der Raumzeit zu definieren. Die gewöhnliche Quantenmechanik ergibt sich aus dem Postulat, dass diese Wahrscheinlichkeitsamplitude eine Phase hat, die proportional zur klassisch berechneten Wirkung für diesen Weg ist. Dies gilt, wenn die Wirkung das Zeitintegral einer quadratischen Funktion der Geschwindigkeit ist. Die Beziehung zur Matrix- und Operatoralgebra wird so diskutiert, dass

¹P. A. M. Dirac, The Principles of Quantum Mechanics (The Clarendon Press, Oxford, 1935), zweite Auflage, Abschnitt 33; außerdem Physik. Zeits. Sowjetunion 3, 64 (1933).

²P. A. M. Dirac, Pfarrer Mod. Phys. 17, 195 (1945).

³In dieser Arbeit wird der Begriff "Aktion" für das Zeitintegral der Lagrangefunktion entlang eines Pfades verwendet. Wenn dieser Pfad tatsächlich der eines klassischen Teilchens ist, sollte das Integral korrekter als Hamiltons erste Prinzipfunktion bezeichnet werden.

2

bleibt so nah wie möglich an der Sprache der neuen Formulierung. Dies hat keinen praktischen Vorteil, aber die Formeln sind sehr suggestiv, wenn eine Verallgemeinerung auf eine breitere Klasse von Aktionsfunktionalen in Betracht gezogen wird. Abschließend diskutieren wir die Anwendungen der Formulierung. Als konkretes Beispiel zeigen wir, wie die Koordinaten eines harmonischen Oszillators aus den Bewegungsgleichungen eines Systems eliminiert werden können, mit dem er wechselwirkt. Dies kann direkt für die Anwendung in der Quantenelektrodynamik erweitert werden. Eine formale Erweiterung, die die Effekte von Spin und Relativität einschließt, wird beschrieben.

## 2. Die Superposition von Wahrscheinlichkeitsamplituden

Die zu präsentierende Formulierung enthält als wesentliche Idee das Konzept einer Wahrscheinlichkeitsamplitude, die mit einer vollständig spezifizierten Bewegung als Funktion der Zeit verbunden ist. Es lohnt sich daher, das quantenmechanische Konzept der Überlagerung von Wahrscheinlichkeitsamplituden im Detail zu betrachten. Wir werden die wesentlichen Veränderungen der physikalischen Perspektive untersuchen, die durch den Übergang von der klassischen zur Quantenphysik erforderlich sind.

Zu diesem Zweck betrachten wir ein imaginäres Experiment, bei dem wir drei Messungen in der Zeit hintereinander durchführen können: zuerst eine Größe $A$, dann von $B$, und dann von $C$. Es ist wirklich nicht nötig, dass diese unterschiedlich groß sind, und es wird ebenso gut funktionieren, wenn man das Beispiel von drei aufeinanderfolgenden Positionsmessungen berücksichtigt. Angenommen, $a$ ist eines von mehreren möglichen Ergebnissen, die sich aus der Messung ergeben könnten $A$, $b$ ist ein Ergebnis, das aus $B$, und $c$ ist ein Ergebnis, das aus der dritten Messung möglich ist $C$.$^{4}$ Wir nehmen an, dass die Messungen $A$, $B$, und $C$ sind die Art von Messungen, die im quantenmechanischen Fall einen Zustand vollständig spezifizieren. Das ist zum Beispiel der Zustand, für den $B$ hat den Wert $b$ ist nicht entartet.

Es ist allgemein bekannt, dass sich die Quantenmechanik mit Wahrscheinlichkeiten beschäftigt, aber natürlich ist das nicht das Gesamtbild. Um die Beziehung zwischen klassischer und Quantentheorie noch deutlicher darzustellen, könnten wir annehmen, dass wir klassisch auch mit Wahrscheinlichkeiten zu tun haben, aber alle Wahrscheinlichkeiten entweder null oder eins sind. Eine bessere Alternative ist es, sich im klassischen Fall vorzustellen, dass die Wahrscheinlichkeiten im Sinne der klassischen statistischen Mechanik liegen (wobei möglicherweise interne Koordinaten nicht vollständig spezifiziert sind).

Wir definieren $P_{ab}$ als die Wahrscheinlichkeit, dass wenn die Messung $A$ gab das Ergebnis $a$,

$^{4}$Für unsere Diskussion ist es nicht wichtig, dass bestimmte Werte von $a, b$, oder $c$ könnte von der Quantenmechanik ausgeschlossen werden, aber nicht von der klassischen Mechanik. Der Einfachheit halber nehmen wir an, dass die Werte für beide gleich sind, aber die Wahrscheinlichkeit für bestimmte Werte null sein kann.

3

dann die Messung $B$ wird das Ergebnis liefern $b$. Ähnlich gilt: $P_{bc}$ ist die Wahrscheinlichkeit, dass wenn Messung $B$ ergibt das Ergebnis $b$, dann die Messung $C$ gibt $c$. Weiter sollen wir $P_{ac}$ Es gibt die Chance, dass wenn $A$ gibt $a$, dann $C$ gibt $c$. Schließlich bezeichne mit $P_{abc}$ die Wahrscheinlichkeit aller drei, d. h. wenn $A$ gibt $a$, dann $B$ gibt $b$, und $C$ gibt $c$. Wenn die Ereignisse dazwischen $a$ und $b$ sind unabhängig von den dazwischen $b$ und $c$, dann

$$P_{abc} = P_{ab}P_{bc}. \quad (1)$$

Dies gilt laut Quantenmechanik, wenn die Aussage gilt, dass $B$ ist $b$ ist eine vollständige Spezifikation des Bundesstaates.

In jedem Fall erwarten wir die Beziehung

$$P_{ac} = \sum_b P_{abc}. \quad (2)$$

Dies liegt daran, dass bei anfänglicher Messung $A$ gibt $a$ und später stellt sich heraus, dass das System das Ergebnis liefert $c$ Zur Messung $C$ Menge $B$ muss zu diesem Zeitpunkt einen Wert gehabt haben, zwischen $A$ und $C$. Die Wahrscheinlichkeit, dass es so war $b$ ist $P_{abc}$. Wir summieren oder integrieren über alle sich gegenseitig ausschließenden Alternativen für $b$ (symbolisiert durch $\sum_b$).

Der wesentliche Unterschied zwischen klassischer und Quantenphysik liegt nun in Gleichung (2). In der klassischen Mechanik ist es immer wahr. In der Quantenmechanik ist das oft falsch. Wir bezeichnen die quantenmechanische Wahrscheinlichkeit, dass eine Messung von $C$ Ergebnisse in $c$ wenn sie einer Messung von folgt $A$ Geben $a$ von $P_{ac}^q$. Gleichung (2) wird in der Quantenmechanik durch dieses bemerkenswerte Gesetz ersetzt:$^5$ Es existieren komplexe Zahlen $\varphi_{ab}, \varphi_{bc}, \varphi_{ac}$ so dass

$$P_{ab} = |\varphi_{ab}|^2, \quad P_{bc} = |\varphi_{bc}|^2, \quad \text{and} \quad P_{ac}^q = |\varphi_{ac}|^2. \quad (3)$$

Das klassische Gesetz, das durch Kombination von (1) und (2) erhalten wird,

$$P_{ac} = \sum_b P_{ab}P_{bc} \quad (4)$$

wird ersetzt durch

$$\varphi_{ac} = \sum_b \varphi_{ab}\varphi_{bc}. \quad (5)$$

Wenn (5) korrekt ist, ist normalerweise (4) falsch. Der logische Fehler bei der Deduktion (4) bestand natürlich darin, anzunehmen, dass man von $a$ zu $c$ Das System

$^5$Wir haben angenommen $b$ ist ein nicht-entarteter Zustand, und dass daher (1) wahr ist. Vermutlich, wenn in einer Verallgemeinerung der Quantenmechanik (1) nicht wahr wäre, selbst für reine Zustände $b$, (2) könnte erwartet werden, ersetzt zu werden durch: Es gibt komplexe Zahlen $\varphi_{abc}$ so dass $P_{abc} = |\varphi_{abc}|^2$. Das Analogon zu (5) ist dann $\varphi_{ac} = \sum_b \varphi_{abc}$

4

musste eine Bedingung durchlaufen, dass $B$ musste einen bestimmten Wert haben, $b$.

Wenn versucht wird, dies zu überprüfen, d. h. wenn $B$ wird zwischen den Experimenten gemessen $A$ und $C$, dann ist Formel (4) tatsächlich korrekt. Genauer gesagt, wenn das Messgerät $B$ wird eingerichtet und verwendet, aber es wird kein Versuch unternommen, die Ergebnisse der $B$ Messung im Sinne davon, dass nur die $A$ zu $C$ Die Korrelation wird aufgezeichnet und untersucht, dann ist (4) korrekt. Das liegt daran, dass die $B$ Messmaschine hat ihre Aufgabe erfüllt; Wenn wir wollen, könnten wir jederzeit die Zähler ablesen, ohne die Situation weiter zu stören. Die Experimente, die führten $a$ und $c$ können daher je nach Wert von in Gruppen unterteilt werden $b$.

Betrachtet man die Wahrscheinlichkeit aus Häufigkeitssicht (4), ergibt sich einfach aus der Aussage, dass in jedem Experiment $a$ und $c$, $B$ hatte einen gewissen Wert. Die einzige Möglichkeit, wie (4) falsch liegen könnte, ist die Aussage: "$B$ einen gewissen Wert hatte", manchmal bedeutungslos sein muss. Beachten Sie, dass (5) (4) nur unter dem Umstand ersetzt, dass wir keinen Versuch unternehmen, zu messen. $B$, werden wir dazu veranlasst zu sagen, dass die Aussage, "$B$ einen gewissen Wert hatte", bedeutungslos sein kann, wenn wir keinen Versuch unternehmen, zu messen $B^6$.

Daher haben wir unterschiedliche Ergebnisse für die Korrelation von $a$ und $c$, nämlich Gleichung (4) oder Gleichung (5), je nachdem, ob wir versuchen zu messen oder nicht $B$. Egal wie subtil man es versucht, der Versuch zu messen $B$ das System zumindest so weit stören, dass die Ergebnisse von denen von (5) zu denen von (4) geändert werden$^7$. Dass Messungen tatsächlich die notwendigen Störungen verursachen und dass (4) im Wesentlichen falsch sein könnte, wurde von Heisenberg erstmals klar in seinem Unschärfeprinzip formuliert. Das Gesetz (5) ist das Ergebnis der Arbeit von Schrödinger, der statistischen Interpretation von Born und Jordan sowie der Transformationstheorie von Dirac.$^8$

Gleichung (5) ist eine typische Darstellung der Wellennatur der Materie.

$^6$Es hilft nicht zu weisen, dass wir hätten messen können $B$ Hätten wir es uns gewünscht. Tatsache ist, dass wir es nicht taten.

$^7$Wie (4) tatsächlich daraus resultiert, (5) wenn Messungen das System stören, wurde insbesondere von J. von Neumann untersucht (*Mathematische Grundlagen der Quantenmahanik* (Dover Publications, New York, 1943)). Die Wirkung der Störung des Messgeräts besteht darin, die Phase der störenden Komponenten effektiv zu verändern, durch $\theta_b$, sagen wir, so dass (5) wird $\varphi_{ac} = \sum_b e^{i\theta_b} \varphi_{ab} \varphi_{bc}$. Wie von Neumann jedoch zeigt, müssen die Phasenverschiebungen unbekannt bleiben, wenn $B$ so gemessen wird, dass die resultierende Wahrscheinlichkeit $P_{ac}$ ist das Quadrat von $\varphi_{ac}$, gemittelt über alle Phasen, $\theta_b$. Dies ergibt (4).

$^8$Wenn $\mathbf{A}$ und $\mathbf{B}$ sind die Operatoren, die den Messungen entsprechen $A$ und $B$, und wenn $\psi_a$, und $\psi_b$ sind Lösungen von $\mathbf{A}\psi_a = a\psi_a$, und $\mathbf{B}\chi_b = b\chi_b$, dann $\varphi_{ab} = \int \chi_b^* \psi_a dx = (\chi_b^*, \psi_a)$. Somit gilt: $\psi_{ab}$ ist ein Element $(a|b)$ der Transformationsmatrix für die Transformation von einer Darstellung, in der $\mathbf{A}$ diagonal zu einem ist, in dem $\mathbf{B}$ diagonal ist.

5

Hier ist die Chance, ein Teilchen zu finden, von $a$ zu $c$ über mehrere verschiedene Routen (Werte von $b$) kann, wenn kein Versuch unternommen wird, die Route zu bestimmen, als Quadrat einer Summe mehrerer komplexer Größen dargestellt werden – eine für jede verfügbare Route.

Die Wahrscheinlichkeit kann die typischen Interferenzphänomene zeigen, die üblicherweise mit Wellen assoziiert sind, deren Intensität durch das Quadrat der Summe der Beiträge verschiedener Quellen gegeben wird. Das Elektron wirkt sozusagen wie eine Welle, (5), solange kein Versuch unternommen wird, zu überprüfen, dass es sich um ein Teilchen handelt; doch man kann, wenn man möchte, bestimmen, auf welchem Weg es sich bewegt, als wäre es ein Teilchen; Aber wenn man das tut, wirkt (4) und es verhält sich tatsächlich wie ein Teilchen.

Diese Dinge sind natürlich wohlbekannt. Sie wurden bereits viele Male erklärt.$^{9}$ Es scheint sich jedoch lohnenswert zu betonen, dass sie alle einfach direkte Folgen von Gleichung (5) sind, denn es ist im Wesentlichen Gleichung (5), die in meiner Formulierung der Quantenmechanik grundlegend ist.

Die Verallgemeinerung der Gleichungen. (4) und (5) zu einer großen Anzahl von Maßen, zum Beispiel $A, B, C, D, \dots, K$, ist natürlich, dass die Wahrscheinlichkeit der Folge $a, b, c, d, \dots, k$, ist

$$P_{abcd\dots k} = |\varphi_{abcd\dots k}|^2.$$

Die Wahrscheinlichkeit des Ergebnisses $a, c, k$, zum Beispiel, wenn $b, d, \dots$ gemessen werden, ist die klassische Formel:

$$P_{ack} = \sum_b \sum_d \dots P_{abcd\dots k}, \quad (6)$$

während die Wahrscheinlichkeit derselben Folge $a, c, k$ wenn keine Messungen dazwischen vorgenommen werden $A$ und $C$ und zwischen $C$ und $K$ ist

$$P_{ack}^q = |\sum_b \sum_d \dots \varphi_{abcd\dots k}|^2. \quad (7)$$

Die Menge $\varphi_{abcd\dots k}$ wir können die Wahrscheinlichkeitsamplitude für die Bedingung benennen $A = a$, $B = b$, $C = c$, $D = d, \dots, K = k$. (Es ist natürlich als Produkt ausdrückbar $\varphi_{ab}\varphi_{bc}\varphi_{cd}\dots\varphi_{jk}$.)

### 3. Die Wahrscheinlichkeitsamplitude für einen Raum-Zeit-Pfad

Die physikalischen Ideen des letzten Abschnitts können leicht erweitert werden, um eine Wahrscheinlichkeitsamplitude für eine bestimmte, vollständig spezifizierte Raumzeit zu definieren

$^{9}$Siehe zum Beispiel W. Heisenberg, *Die physikalischen Prinzipien der Quantentheorie* (University of Chicago Press, Chicago, 1930), insbesondere Kapitel IV.

6

Weg. Um zu erklären, wie dies geschehen kann, beschränken wir uns auf ein eindimensionales Problem, da die Verallgemeinerung auf mehrere Dimensionen offensichtlich ist.

Angenommen, wir haben ein Teilchen, das verschiedene Werte einer Koordinate annehmen kann $x$. Stellen Sie sich vor, wir führen eine enorme Anzahl aufeinanderfolgender Positionsmessungen vor, sagen wir, getrennt durch ein kleines Zeitintervall $\epsilon$. Dann folgt eine Abfolge von Messungen wie $A, B, C, \dots$ könnte die Abfolge von Messungen der Koordinate sein $x$ zu aufeinanderfolgenden Zeiten $t_1, t_2, t_3, \dots$, wobei $t_{i+1} = t_i + \epsilon$. Sei der Wert, der sich aus der Messung der Koordinate zur Zeit ergeben könnte $t_i$ seien $x_i$. Daher gilt: Wenn $A$ ist eine Messung von $x$ bei $t_1$ dann $x_1$ ist das, was wir zuvor mit bezeichnet haben $a$. Aus klassischer Sicht gelten die sukzessiven Werte, $x_1, x_2, x_3, \dots$ der Koordinate definiert praktisch einen Pfad $x(t)$. Irgendwann erwarten wir, an die Grenze zu gehen $\epsilon \rightarrow 0$.

Die Wahrscheinlichkeit eines solchen Weges ist eine Funktion von $x_1, x_2, \dots, x_i, \dots$, sagen Sie $P(\dots, x_i, x_{i+1}, \dots)$. Die Wahrscheinlichkeit, dass der Weg in einem bestimmten Bereich liegt $R$ der Raumzeit wird klassisch durch Integration erhalten $P$ über diesem Bereich. Daher ist die Wahrscheinlichkeit, dass $x_i$, liegt dazwischen $a_i$ und $b_i$ und $x_{i+1}$ Liegt dazwischen $a_{i+1}$ und so weiter, ist

$$\begin{aligned} \dots \int_{a_i}^{b_i} \int_{a_{i+1}}^{b_{i+1}} \dots P(\dots, x_i, x_{i+1}, \dots) \dots dx, dx_{i+1} \dots &= \\ &= \int_R P(\dots, x_i, x_{i+1}, \dots) \dots dx, dx_{i+1} \dots, \end{aligned} \quad (8)$$

Das Symbol $\int_R$ das heißt, die Integration soll über jene Bereiche der Variablen erfolgen, die im Bereich liegen $R$. Dies ist einfach Gleichung (6) mit $a, b, \dots$ Ersetzt durch $x_1, x_2, \dots$ und Integration ersetzt die Summation.

In der Quantenmechanik ist dies die korrekte Formel für den Fall, dass $x_1, x_2, \dots, x_i, \dots$ wurden tatsächlich alle gemessen, und dann nur jene Pfade, die darin liegen $R$ wurden entführt. Wir würden erwarten, dass das Ergebnis anders wäre, wenn keine so detaillierten Messungen durchgeführt worden wären. Angenommen, es wird eine Messung durchgeführt, die nur bestimmen kann, dass der Weg irgendwo innerhalb liegt. $R$.

Die Messung soll das sein, was wir eine "ideale Messung" nennen könnten. Wir nehmen an, dass aus derselben Messung keine weiteren Details erhalten werden können, ohne das System weiter zu stören. Ich konnte keine genaue Definition finden. Wir versuchen, die zusätzlichen Unsicherheiten zu vermeiden, die gemittelt werden müssen, wenn beispielsweise mehr Informationen gemessen, aber nicht genutzt werden. Wir möchten für alle Gleichung (5) oder (7) verwenden $x_i$ und keinen Restteil haben, über den man im Sinne von Gleichung (4) summieren kann.

7

Wir erwarten, dass die Wahrscheinlichkeit, dass das Teilchen durch unsere "ideale Messung" gefunden wird, tatsächlich in der Region liegt $R$ ist das Quadrat einer komplexen Zahl $|\varphi(R)|^2$. Die Zahl $\varphi(R)$, die wir als Wahrscheinlichkeitsamplitude für die Region bezeichnen können $R$ ist gegeben durch Gleichung (7) mit $a, b, \dots$ Ersetzt durch $x_i, x_{i+1}, \dots$ und Summation ersetzt durch Integration:

$$\varphi(R) = \lim_{\epsilon \rightarrow 0} \int_R \times \Phi(\dots x_i, x_{i+1} \dots) \dots dx_i dx_{i+1} \dots. \quad (9)$$

Die komplexe Zahl $\Phi(\dots x_i, x_{i+1} \dots)$ ist eine Funktion der Variablen $x_i$, und definiert den Weg. Tatsächlich stellen wir uns vor, dass der Zeitabstand $e$ nähert sich Null so an, dass $\Phi$ Im Grunde hängt es vom gesamten Weg ab $x(t)$ und nicht nur auf den Werten von $x_i$, zu bestimmten Zeiten $t_i$, $x_i = x(t_i)$. Wir könnten anrufen $\Phi$ die Wahrscheinlichkeitsamplitudenfunktional von Pfaden $x(t)$.

Wir können diese Ideen in unserem ersten Postulat zusammenfassen:

*I. Wenn eine ideale Messung durchgeführt wird, um zu bestimmen, ob ein Teilchen einen Weg in einem Bereich der Raumzeit hat, dann ist die Wahrscheinlichkeit, dass das Ergebnis bejahend ist, das absolute Quadrat einer Summe komplexer Beiträge, jeweils einer von jedem Pfad im Bereich.*

Die Aussage des Postulats ist unvollständig. Die Bedeutung einer Summe von Begriffen eins für "jeden" Pfad ist mehrdeutig. Die genaue Bedeutung, die in Gleichung (9) gegeben wird, ist folgende: Ein Pfad wird zunächst nur durch die Positionen definiert $x_i$; durch die sie in einer Folge gleichmäßig verteilter Zeiten verläuft, $^{10}$ $t_i = t_{i-1} + \epsilon$. Dann alle Werte der Koordinaten innerhalb $R$ gleich viel zu haben. Die tatsächliche Größe des Gewichts hängt von ab $\epsilon$ und so gewählt werden kann, dass die Wahrscheinlichkeit eines Ereignisses, das sicher ist, auf Einheit normalisiert wird. Es ist vielleicht nicht am besten, dies zu tun, aber wir haben diesen Gewichtungsfaktor als Proportionalitätskonstante im zweiten Postulat belassen. Die Grenze $\epsilon \rightarrow 0$ muss am Ende einer Berechnung durchgeführt werden.

Wenn das System mehrere Freiheitsgrade besitzt, ist der Koordinatenraum $x$ hat mehrere Dimensionen, sodass das Symbol $x$ eine Menge von Koordinaten darstellen $(x^{(1)}, x^{(2)}, \dots, x^{(k)})$ für ein System mit $k$ Freiheitsgrade. Ein Pfad ist eine Folge von Konfigurationen für aufeinanderfolgende Zeiten und wird beschrieben, indem die Konfiguration gegeben wird $x_i$, oder $(x_i^{(1)}, x_i^{(2)}, \dots, x_i^{(k)})$, d. h. der Wert jedes der $k$ Koordinaten für jede Zeit $t_i$. Das Symbol $dx_i$, wird so verstanden werden

$^{10}$Es gibt sehr interessante mathematische Probleme, die versuchen, Unterteilungs- und Limitierungsprozesse zu vermeiden. Eine Art komplexes Maß wird mit dem Raum der Funktionen assoziiert $x(t)$. Unter unerwarteten Umständen können endliche Ergebnisse erzielt werden, da das Maß nicht überall positiv ist, aber die Beiträge der meisten Pfade sich weitgehend aufheben. Diese kuriosen mathematischen Probleme werden durch den Unterteilungsprozess umgangen. Man fühlt sich jedoch, wie Cavalieri sich gefühlt haben muss, als er das Volumen einer Pyramide vor der Erfindung der Analysis berechnete.

8

das Volumenelement in $k$ dimensionaler Konfigurationsraum (zur Zeit $t_i$). Die Aussage der Postulate ist unabhängig vom verwendeten Koordinatensystem.

Das Postulat beschränkt sich auf die Definition der Ergebnisse von Positionsmessungen. Es steht zum Beispiel nicht, was getan werden muss, um das Ergebnis einer Impulsmessung zu definieren. Dies ist jedoch keine wirkliche Einschränkung, da die Messung des Impulses eines Teilchens prinzipiell durch Positionsmessungen anderer Teilchen, z. B. Messindikatoren, durchgeführt werden kann. Eine Analyse eines solchen Experiments wird also bestimmen, was am ersten Teilchen seinen Impuls bestimmt.

#### 4. Die Berechnung der Wahrscheinlichkeitsamplitude für einen Pfad

Das erste Postulat schreibt den Typ mathematischen Rahmens vor, den die Quantenmechanik zur Berechnung von Wahrscheinlichkeiten benötigt. Das zweite Postulat verleiht diesem Rahmen einen bestimmten Inhalt, indem es vorschreibt, wie die wichtige Größe berechnet werden soll $\Phi$ Für jeden Pfad:

*II. Die Wege tragen gleichmäßig viel bei, aber die Phase ihres Beitrags ist die klassische Wirkung (in Einheiten von $\hbar$); d. h. das Zeitintegral der Lagrange-Funktion, die entlang des Pfades genommen wird.*

Das heißt, der Beitrag $\Phi[x(t)]$ aus einem gegebenen Pfad $x(t)$ proportional zu ist $\exp(i/\hbar S[x(t)])$, wobei die Wirkung $S[x(t)] = \int L(\dot{x}(t), x(t)) dt$ ist das Zeitintegral der klassischen Lagrangefunktion $L(\dot{x}, x)$ auf dem betreffenden Weg gefolgt. Der Lagrange-Operator, der eine explizite Funktion der Zeit sein kann, ist eine Funktion von Position und Geschwindigkeit. Wenn wir annehmen, dass es eine quadratische Funktion der Geschwindigkeiten ist, können wir die mathematische Äquivalenz der hier genannten Postulate und die üblichere Formulierung der Quantenmechanik zeigen.

Um das erste Postulat zu interpretieren, war es notwendig, einen Weg zu definieren, indem nur die Abfolge der Punkte angegeben wird $x_i$, durch die der Weg zu aufeinanderfolgenden Zeiten verläuft $t_i$. Zum Berechnen $S = \int L(\dot{x}, x) dt$ Wir müssen den Weg an allen Punkten kennen, nicht nur bei $x_i$. Wir nehmen an, dass die Funktion $x(t)$ im Intervall zwischen $t_i$ und $t_{i+1}$ ist der Weg, dem ein klassisches Teilchen folgt, mit der Lagrangefunktion $L$, die beginnend mit $x_i$, bei $t_i$ Gebiete $x_{i+1}$ bei $t_{i+1}$. Diese Annahme ist erforderlich, um das zweite Postulat für diskontinuierliche Wege zu interpretieren. Die Menge $\Phi(\dots, x_i, x_{i+1}, \dots)$ kann normalisiert werden (für verschiedene $\epsilon$) falls gewünscht, sodass die Wahrscheinlichkeit eines Ereignisses, das sicher ist, auf Einheit normalisiert wird als $\epsilon \rightarrow 0$.

Es ist keine Schwierigkeit, das Aktionsintegral auszuführen, da

9

plötzliche Geschwindigkeitsänderungen zu diesen Zeiten $t_i$ Solange wie $L$ hängt nicht von höheren Zeitableitungen der Position ab als die erste. Außerdem, es sei denn, $L$ so eingeschränkt ist, dass die Endpunkte nicht ausreichen, um den klassischen Pfad zu definieren. Da der klassische Pfad derjenige ist, der die Wirkung zum Minimum macht, können wir schreiben

$$S = \sum_i S(x_{i+1}, x_i), \quad (10)$$

wobei

$$S(x_{i+1}, x_i) = \text{Min.} \int_{t_i}^{t_{i+1}} L(\dot{x}(t), x(t)) dt. \quad (11)$$

So formuliert, besteht der einzige Appell an der klassischen Mechanik darin, uns eine Lagrangefunktion zu liefern. Tatsächlich könnte man Postulat zwei einfach so betrachten, dass es sagt: "$\Phi$ ist der Exponentialwert von $i$ mal das Integral einer reellen Funktion von $x(t)$ und zum ersten Mal abgeleitet." Dann könnten die klassischen Bewegungsgleichungen später als Grenzwert für große Dimensionen abgeleitet werden. Die Funktion von $x$ und $\dot{x}$ dann könnte gezeigt werden, dass sie die klassische Lagrangefunktion innerhalb eines konstanten Faktors ist.

Tatsächlich ist die Summe in (10), selbst für endliche $\epsilon$ ist unendlich und daher bedeutungslos (wegen der unendlichen Ausdehnung der Zeit). Dies spiegelt eine weitere Unvollständigkeit der Postulate wider. Wir müssen uns auf ein endliches, aber willkürlich langes Zeitintervall beschränken.

Kombiniert man die beiden Postulate und verwendet Gleichung (10), erhält man

$$\varphi(R) = \lim_{\epsilon \to 0} \int_R \times \exp \left[ \frac{i}{\hbar} \sum_i S(x_{i+1}, x_i) \right] \cdots \frac{dx_{i+1}}{A} \frac{dx_i}{A} \cdots, \quad (12)$$

wobei wir den Normalisierungsfaktor in einen Faktor aufteilen lassen $1/A$ (dessen genauer Wert wir gleich bestimmen werden) für jeden Moment der Zeit. Die Integration liegt einfach über diesen Werten $x_i, x_{i+1}, \dots$ die in der Region liegen $R$. Diese Gleichung, die Definition (11) von $S(x_{i+1}, x_i)$, und die physikalische Interpretation von $|\varphi(R)|^2$ als die Wahrscheinlichkeit, dass das Teilchen in $R$, vervollständigen unsere Formulierung der Quantenmechanik.

## 5. Definition der Wellenfunktion

Wir zeigen nun die Äquivalenz dieser Postulate zur gewöhnlichen Formulierung der Quantenmechanik. Das machen wir in zwei Schritten. Wir zeigen darin

10

Abschnitt wie die Wellenfunktion aus der neuen Perspektive definiert werden kann. Im nächsten Abschnitt zeigen wir, dass diese Funktion die Schrödingersche Differentialwellengleichung erfüllt.

Wir werden sehen, dass es die Möglichkeit (10) ist, auszudrücken $S$ als Summe, und daher $\Phi$ als Produkt von Beiträgen aufeinanderfolgender Abschnitte des Weges, was die Möglichkeit eröffnet, eine Größe mit den Eigenschaften einer Wellenfunktion zu definieren.

Um das klarzustellen, stellen wir uns vor, wir wählen eine bestimmte Zeit $t$ und die Region zu teilen $R$ in Gleichung (12) in Stücke, Zukunft und Vergangenheit relativ zu $t$. Wir stellen uns vor, dass $R$ kann unterteilt werden in: (a) eine Region $R'$, in irgendeiner Weise im Raum eingeschränkt, aber ganz früher in der Zeit liegend als manche $t'$, so dass $t' < t$; (b) eine Region $R''$ beliebig im Raum eingeschränkt, aber ganz später in der Zeit liegen als $t''$, so dass $t'' > t$; (c) das Gebiet zwischen $t'$ und $t''$ wobei alle Werte von $x$ Koordinaten sind unbeschränkt, d. h. die gesamte Raumzeit zwischen $t'$ und $t''$. Die Region (c) ist nicht absolut notwendig. Sie kann so zeitlich begrenzt gestaltet werden, wie gewünscht. Es ist jedoch praktisch, uns zu erlauben, Variieren zu berücksichtigen $t$ ein bisschen, ohne neu definieren zu müssen $R'$ und $R''$. Dann $|\varphi(R', R'')|^2$ ist die Wahrscheinlichkeit, dass der Weg einnimmt $R'$ und $R''$. Weil $R'$ ist vollständig vorher $R''$, wenn man die Zeit betrachtet $t$ Als Gegenwart können wir dies als die Wahrscheinlichkeit ausdrücken, dass der Pfad in einer Region lag $R'$ und wird in der Region sein $R''$. Wenn wir durch einen Faktor teilen, ist die Wahrscheinlichkeit, dass der Weg in ist $R'$, um die Wahrscheinlichkeit zu renormalisieren, erhalten wir: $|\varphi(R', R'')|^2$ ist die (relative) Wahrscheinlichkeit, dass, wenn das System in einer Region wäre $R'$ Sie wird später in $R''$.

Dies ist natürlich die wichtige Größe zur Vorhersage der Ergebnisse vieler Experimente. Wir bereiten das System auf eine bestimmte Weise vor (z. B. war es in der Region $R'$) und dann eine andere Eigenschaft missen (z. B. ob sie in der Region gefunden wird) $R''$?). Was sagt (12) über die Berechnung dieser Größe, oder besser gesagt der Größe aus. $\varphi(R', R'')$ Von dem es das Quadrat ist?

Nehmen wir in Gleichung (12) an, dass die Zeit $t$ entspricht einem bestimmten Punkt $k$ der Unterteilung der Zeit in Schritte $\epsilon$, d. h. nehmen wir an. $t = t_k$, der Index $k$, natürlich abhängig von der Unterteilung $\epsilon$. Dann kann die Exponentialsumme, die Exponentialsumme ist, in ein Produkt von zwei Faktoren aufgeteilt werden

$$\exp \left[ \frac{i}{\hbar} \sum_{i=k}^{\infty} S(x_{i+1}, x_i) \right] \cdot \exp \left[ \frac{i}{\hbar} \sum_{i=-\infty}^{k-1} S(x_{i+1}, x_i) \right]. \quad (13)$$

Der erste Faktor enthält nur Koordinaten mit Index $k$ oder höher, während die zweite nur Koordinaten mit Index enthält $k$ oder niedriger. Diese Aufteilung ist möglich durch Gleichung (10), die im Wesentlichen daraus resultiert, dass die Lagrangefunktion nur eine Funktion von Positionen und Geschwindigkeiten ist. Erstens, die

11

Integration auf alle Variablen $x_i$ für $i > k$ kann auf dem ersten Faktor ausgeführt werden, was zu einer Funktion von führt. $x_k$ (mal mit dem zweiten Faktor). Als nächstes die Integration aller Variablen $x_i$, für $i < k$ kann auch auf den zweiten Faktor ausgeführt werden, was eine Funktion von $x_k$. Schließlich die Integration auf $x_k$ kann durchgeführt werden. Das heißt, $\varphi(R', R'')$ kann als das Integral über geschrieben werden $x_k$ aus dem Produkt zweier Faktoren. Wir werden diese nennen $\chi^*(x_k, t)$ und $\psi(x_k, t)$:

$$\varphi(R', R'') = \int \chi^*(x, t) \psi(x, t) dx, \quad (14)$$

wobei

$$\psi(x_k, t) = \lim_{\epsilon \to 0} \int_{R'} \times \exp \left[ \frac{i}{\hbar} \sum_{i=-\infty}^{k-1} S(x_{i+1}, x_i) \right] \frac{dx_{k-1}}{A} \frac{dx_{k-2}}{A} \dots, \quad (15)$$

und

$$\chi^*(x_k, t) = \lim_{\epsilon \to 0} \int_{R''} \exp \left[ \frac{i}{\hbar} \sum_{i=k}^{\infty} S(x_{i+1}, x_i) \right] \cdot \frac{1}{A} \frac{dx_{k+1}}{A} \frac{dx_{k+2}}{A} \dots. \quad (16)$$

Das Symbol $R'$ wird auf das Integral für gesetzt $\psi$ um anzuzeigen, dass die Koordinaten über die Region integriert sind $R'$, und für $t_i$ Zwischen $t'$ und $t$, über den gesamten Raum. In ähnlicher Weise ist das Integral für $\chi^*$ ist vorbei $R''$ und über allen Raum für jene Koordinaten, die den Zeiten zwischen entsprechen $t$ und $t''$. Das Sternchen auf $\chi^*$ bezeichnet komplex konjugiert, da es bequemer ist, (16) als komplex konjugiert einer Größe zu definieren, $\chi$.

Die Menge $\psi$ es hängt nur von der Region ab $R'$ Vor dem $t$, und ist vollständig versenkt, wenn dieser Bereich bekannt ist. Es hängt in keiner Weise davon ab, was mit dem System nach der Zeit geschieht $t$. Diese letzteren Informationen sind enthalten in $\chi$. Daher gilt mit $\psi$ und $\chi$ Wir haben die Vergangenheit von den zukünftigen Erfahrungen des Systems getrennt. Dies erlaubt uns, auf konventionelle Weise über das Verhältnis von Vergangenheit und Zukunft zu sprechen. Wenn sich also ein Teilchen in einem Bereich der Raumzeit befand, $R'$ Es kann irgendwann $t$ als in einem bestimmten Zustand oder Zustand beschrieben werden, der nur durch seine Vergangenheit bestimmt und durch die sogenannte Wellenfunktion beschrieben wird $\psi(x, t)$. Diese Funktion enthält alles, was zur Vorhersage zukünftiger Wahrscheinlichkeiten benötigt wird. Denn, nehmen wir an, in einer anderen Situation, die Region $R'$ wären anders gewesen, sagen wir $r'$, und möglicherweise die Lagrangefunktion für frühere Zeiten $t$ wurden ebenfalls verändert. Aber nehmen wir dennoch an, die Menge aus Gleichung (15) wäre gleich gewesen. Dann gilt gemäß (14) die Wahrscheinlichkeit, in einer beliebigen Region zu enden. $R''$ ist dasselbe für $R'$ wie $r'$. Daher werden zukünftige Messungen nicht unterscheiden, ob das System bereits eingenommen hat $R'$ oder $r'$. Somit gilt die

12

Wellenfunktion $\psi(x,t)$ reicht aus, um jene Attribute zu definieren, die aus der vergangenen Geschichte übrig geblieben sind und das zukünftige Verhalten bestimmen.

Ebenso ist die Funktion $\chi(x,t)$ charakterisiert die Erfahrung oder, sagen wir, das Experiment, dem das System unterzogen werden soll. Wenn eine andere Region ist, $r''$ und danach ein anderes Lagrange-Syndrom $t$, und würden dasselbe geben $\chi^*(x,t)$ *Via* Gleichung (16), ebenso wie Region $R''$, dann, egal wie die Vorbereitung ist, $\psi$, Gleichung (14) sagt, dass die Chance, das System zu finden, in $R''$ ist immer dasselbe wie es zu finden in $r''$. Die beiden "Experimente" $R''$ und $r''$ äquivalent sind, da sie die gleichen Ergebnisse liefern. Wir sagen grob gesagt, dass diese Experimente bestimmen sollen, mit welcher Wahrscheinlichkeit das System im Zustand ist $\chi$. Tatsächlich ist diese Terminologie schlecht. Das System ist wirklich im Zustand. $\psi$. Der Grund, warum wir einem Experiment einen Zustand zuordnen können, ist natürlich, dass es für ein ideales Experiment einen eindeutigen Zustand gibt (dessen Wellenfunktion ist $\chi(x,t)$), für die das Experiment mit Sicherheit erfolgreich ist.

Daher können wir sagen: die Wahrscheinlichkeit, dass ein System im Zustand ist $\psi$ wird durch ein Experiment gefunden, dessen charakteristischer Zustand ist $\chi$ (oder, lockerer gesagt, die Chance, dass ein System im Zustand ist $\psi$ Es scheint, als wäre es in $\chi$) ist

$$\left| \int \chi^*(x,t)\psi(x,t)dx \right|^2. \quad (17)$$

Diese Ergebnisse stimmen natürlich mit den Prinzipien der gewöhnlichen Quantenmechanik überein. Sie sind eine Folge der Tatsache, dass die Lagrangefunktion nur eine Funktion von Position, Geschwindigkeit und Zeit ist.

## 6. Die Wellengleichung

Um den Beweis der Äquivalenz mit der gewöhnlichen Formulierung zu vervollständigen, müssen wir zeigen, dass die im vorherigen Abschnitt durch Gleichung (15) definierte Wellenfunktion tatsächlich die Schrödinger-Wellengleichung erfüllt. Tatsächlich werden wir dies nur schaffen, wenn der Lagrange-Operator $L$ in (11) ist eine quadratische, aber möglicherweise inhomogene Form in den Geschwindigkeiten $\dot{x}(t)$. Dies ist jedoch keine Einschränkung, da sie alle Fälle umfasst, für die die Schrödinger-Gleichung experimentell verifiziert wurde.

Die Wellengleichung beschreibt die Entwicklung der Wellenfunktion im Zeitverlauf. Wir können erwarten, dies mit der Feststellung zu bemerken, dass für endliche $\epsilon$, Gleichung (15) erlaubt die Entwicklung einer einfachen rekursiven Relation. Betrachten wir das Erscheinungsbild von Gleichung (15), wenn wir berechnen würden $\psi$ Im nächsten Moment der Zeit:

$$\psi(x_{k+1}, t+\epsilon) = \int_{R'} \exp\left[ \frac{i}{\hbar} \sum_{i=-\infty}^k S(x_{i+1}, x_i) \right] \times \frac{dx_k}{A} \frac{dx_{k-1}}{A} \dots \quad (15')$$

13

Dies ist ähnlich wie (15), abgesehen von der Integration über die zusätzliche Variable $x_k$, und der zusätzliche Term in der Summe im Exponent. Dieser Term bedeutet, dass das Integral von (15') dasselbe ist wie das von (15), mit Ausnahme des Faktors $(1/A)\exp(i/\hbar)S(x_{k+1}, x_k)$. Da dies keine der Variablen enthält $x_i$, für $i$ weniger als $k$, alle Integrationen auf $dx$, bis $dx_{k-1}$ kann ohne diesen Faktor durchgeführt werden. Das Ergebnis dieser Integrationen ist jedoch durch (15) einfach $\psi(x_k, t)$. Daher finden wir aus (15') die Relation

$$\psi(x_{k+1}, t + \epsilon) = \int \exp\left[\frac{i}{\hbar}S(x_{k+1}, x_k)\right] \psi(x_k, t) dx_k / A. \quad (18)$$

Diese Beziehung führt zur Entwicklung von $\psi$ mit der Zeit wird für einfache Beispiele gezeigt, mit geeigneter Wahl von $A$, um äquivalent zur Schrödingerschen Gleichung zu sein. Tatsächlich ist Gleichung (18) nicht exakt, sondern nur im Grenzfall wahr $\epsilon \rightarrow 0$ und wir leiten die Schrödinger-Gleichung ab, indem wir annehmen, dass (18) in erster Ordnung gültig ist $\epsilon$. Die Gleichung (18) *Bedarf* Sei nur für kleine wahr $\epsilon$ zur ersten Ordnung in $\epsilon$. Denn wenn wir die Faktoren in (15) betrachten, die uns über ein endliches Zeitintervall tragen, $T$, die Anzahl der Faktoren ist $T/\epsilon$. Wenn ein Ordnungsfehler $\epsilon^2$ in jeder gemacht wird, akkumuliert sich der resultierende Fehler nicht über die Reihenfolge hinaus $\epsilon^2(T/\epsilon)$ oder $T\epsilon$, der im Limit verschwindet.

Wir werden die Beziehung von (18) zur Schrödingerschen Gleichung veranschaulichen, indem wir sie auf den einfachen Fall eines Teilchens anwenden, das sich in einer Dimension in einem Potential bewegt $V(x)$. Bevor wir dies tun, möchten wir jedoch einige Annäherungen zum Wert besprechen $S(x_{i+1}, x_i)$ gegeben in (11), was für den Ausdruck (18) ausreichend ist.

Der in (11) definierte Ausdruck für $S(x_{i+1}, x_i)$ ist schwer genau für beliebige zu berechnen $\epsilon$ aus der klassischen Mechanik. Tatsächlich ist es nur notwendig, dass ein approximativer Ausdruck für $S(x_{i+1}, x_i)$ in (18) verwendet werden, vorausgesetzt, der Fehler der Näherung ist von einer Ordnung kleiner als der erste in $\epsilon$. Wir beschränken uns auf den Fall, dass die Lagrangefunktion eine quadratische, aber möglicherweise inhomogene Form in den Geschwindigkeiten ist $\dot{x}(t)$. Wie wir später sehen werden, sind die wichtigen Wege diejenigen, für die $x_{i+1} - x_i$ ist von Ordnung $\epsilon^{1/2}$. Unter diesen Umständen genügt es, das Integral in (11) über den klassischen Pfad zu berechnen, den ein *kostenlos* Partikel.$^{11}$ In *kartesische Koordinaten*$^{12}$ Der Weg eines freien Teilchens ist eine Gerade, sodass das Integral von (11) genommen werden kann

$^{11}$Es wird angenommen, dass die 'Kräfte' durch ein Skalar- und Vektorpotential eintreten und nicht in Termen, die das Quadrat der Geschwindigkeit betreffen. Allgemeiner meint man mit einem freien Teilchen eines, bei dem die Lagrangefunktion durch das Weglassen der linearen Terme und der unabhängig von, den Geschwindigkeiten verändert wird.

$^{12}$Allgemeiner gilt für Koordinaten, für die die Terme quadratisch in der Geschwindigkeit in $L(\dot{x}, x)$ erscheinen mit konstanten Koeffizienten.

14

entlang einer geraden Linie. Unter diesen Umständen ist es ausreichend genau, das Integral durch die trapezförmige Regel zu ersetzen

$$S(x_{i+1}, x_i) = \frac{\epsilon}{2} L \left( \frac{x_{i+1} - x_i}{\epsilon}, x_{i+1} \right) + \frac{\epsilon}{2} L \left( \frac{x_{i+1} - x_i}{\epsilon}, x_i \right) \tag{19}$$

oder, wenn es bequemer ist,

$$S(x_{i+1}, x_i) = \epsilon L \left( \frac{x_{i+1} - x_i}{\epsilon}, \frac{x_{i+1} + x_i}{2} \right). \tag{20}$$

Diese sind in einem allgemeinen Koordinatensystem, z. B. kugelförmig, nicht gültig. Eine noch einfachere Näherung kann verwendet werden, wenn zusätzlich kein Vektorpotential oder andere lineare Terme in der Geschwindigkeit vorhanden sind (siehe Seite 376):

$$S(x_{i+1}, x_i) = \epsilon L \left( \frac{x_{i-1} - x_i}{\epsilon}, x_{i+1} \right). \tag{21}$$

Daher gilt für das einfache Beispiel eines Teilchens mit Masse $m$ Bewegung in einer Dimension unter einem Potential $V(x)$, wir können festlegen

$$S(x_{i+1}, x_i) = \frac{m\epsilon}{2} \left( \frac{x_{i+1} - x_i}{\epsilon} \right) - \epsilon V(x_{i+1}). \tag{22}$$

Für dieses Beispiel wird also Gleichung (18)

$$\psi(x_{k+1}, t + \epsilon) = \int \exp \left[ \frac{i\epsilon}{\hbar} \left\{ \frac{m}{2} \left( \frac{x_{k+1} - x_k}{\epsilon} \right)^2 - \right. \right. \\ \left. \left. - V(x_{k+1}) \right\} \right] \psi(x_k, t) dx_k / A. \tag{23}$$

Lass uns anrufen $x_{k+1} = x$ und $x_{k+1} - x_k = \xi$ So dass $x_k = x - \xi$. Dann wird (23)

$$\psi(x, t + \epsilon) = \int \exp \frac{im\xi^2}{\epsilon \cdot 2\hbar} \cdot \exp \frac{-i\epsilon V(x)}{\hbar} \cdot \psi(x - \xi, t) \frac{d\xi}{A}. \tag{24}$$

Das Integral auf $\xi$ konvergieren, wenn $\psi(x, t)$ fällt ausreichend ab, um groß zu sein $x$ (sicher, wenn $\int \psi^*(x) \psi(x) dx = 1$). In der Integration auf $\xi$, da $\epsilon$ ist sehr klein, der Exponentialwert von $im\xi^2/2\hbar\epsilon$ schwingt extrem schnell, außer in der Region um $\xi = 0$ ($\xi$ in Ordnung $(\hbar\epsilon/m)^{1/2}$). Da die Funktion $\psi(x - \xi, t)$ ist eine relativ glatte Funktion von $\xi$ (da $\epsilon$ kann so klein genommen werden, wie gewünscht), trägt der Bereich, in dem die Exponentialwellung schnell schwingt, nur sehr wenig bei.

15

wegen der nahezu vollständigen Aufhebung positiver und negativer Beiträge. Seit nur klein $\xi$ wirksam sind, $\psi(x - \xi, t)$ könnte als Taylor-Serie erweitert werden. Daher gilt:

$$\psi(x, t + \epsilon) = \exp \left( \frac{-i\epsilon V(x)}{\hbar} \right) \times$$

$$\times \int \exp \left( \frac{im\xi^2}{2\hbar\epsilon} \right) \left[ \psi(x, t) - \xi \frac{\partial \psi(x, t)}{\partial x} + \frac{\xi^2}{2} \frac{\partial^2 \psi(x, t)}{\partial x^2} - \dots \right] d\xi / A. \quad (25)$$

Jetzt

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) d\xi = (2\pi\hbar\epsilon i/m)^{1/2},$$

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) \xi d\xi = 0, \quad (26)$$

$$\int_{-\infty}^{\infty} \exp(im\xi^2 / 2\hbar\epsilon) \xi^2 d\xi = (\hbar\epsilon i/m)(2\pi\hbar\epsilon i/m)^{1/2},$$

während das Integral enthält, das enthält $\xi^2$ ist null, für wie das mit $\xi$ es besitzt einen ungewöhnlichen Integranden, und die mit $\xi^4$ sind mindestens von folgender Ordnung $\epsilon$ kleiner als die, die hier aufbewahrt werden.$^{13}$ Wenn wir die linke Seite auf die erste Ordnung in erweitern $\epsilon$ (25) wird

$$\psi(x, t) + \epsilon \frac{\partial \psi(x, t)}{\partial t} = \exp \left( \frac{-i\epsilon V(x)}{\hbar} \right) \frac{(2\pi\hbar\epsilon i/m)^{1/2}}{A} \times \left[ \psi(x, t) + \frac{\hbar\epsilon i}{m} \frac{\partial^2 \psi(x, t)}{\partial x^2} + \dots \right]. \quad (27)$$

Damit sich beide Seiten auf Null Ordnung in einigen können $\epsilon$, müssen wir festlegen

$$A = (2\pi\hbar\epsilon i/m)^{1/2}. \quad (28)$$

Dann erweitern Sie die Exponential, die enthalten ist $V(x)$, wir bekommen

$$\psi(x, t) + \epsilon \frac{\partial \psi}{\partial t} = \left( 1 - \frac{i\epsilon}{\hbar} V(x) \right) \times \left( \psi(x, t) + \frac{\hbar\epsilon i}{2m} \frac{\partial^2 \psi}{\partial x^2} \right). \quad (29)$$

$^{13}$Tatsächlich sind diese Integrale oszillatorisch und nicht definiert, aber sie können durch Verwendung eines Konvergenzfaktors definiert werden. Ein solcher Faktor wird automatisch bereitgestellt durch $\psi(x - \xi, t)$ in (24). Wenn ein formelleres Verfahren gewünscht ist, ersetze es $\hbar$ von $\hbar(1 - i\delta)$, zum Beispiel, wobei $\delta$ eine kleine positive Zahl ist, und dann sei $\delta \to 0$.

16

Stornieren $\psi(x,t)$ von beiden Seiten und im Vergleich der Begriffe mit der ersten Ordnung in $\epsilon$ und multipliziert mit $-\hbar/i$ Man erhält

$$-\frac{\hbar}{i}\frac{\partial\psi}{\partial t}=\frac{1}{2\dot{m}}\left(\frac{\hbar}{i}\frac{\partial}{\partial x}\right)^2\psi+V(x)\psi,\quad(30)$$

was Schrödingers Gleichung für das betreffende Problem ist.

Die Gleichung für $\chi^*$ kann auf die gleiche Weise entwickelt werden, aber mit einem Faktor *Abnahme* Die Zeit um einen Schritt, also $\chi^*$ eine Gleichung wie (30) erfüllt, jedoch mit umgekehrtem Vorzeichen. Indem wir komplexe Konjugate nehmen, können wir schließen, dass $\chi$ erfüllt dieselbe Gleichung wie $\psi$, d. h. ein Experiment kann durch den jeweiligen Zustand definiert werden $\chi$ womit es übereinstimmt.$^{14}$

Dieses Beispiel zeigt, dass der Großteil des Beitrags zu $\psi(x_{k+1},t+\epsilon)$ ergibt sich aus den Werten von $x_k$ in $\psi(x_k,t)$ die ziemlich nah an $x_{k+1}$ (Fern der Ordnung $\epsilon^{1/2}$), sodass die Integralgleichung (23) im Grenzfall durch eine Differentialgleichung ersetzt werden kann. Die 'Geschwindigkeiten' $(x_{k+1}-x_k)/\epsilon$ die wichtig sind, sind sehr hoch, um in Ordnung zu sein $(\hbar/m\epsilon)^{1/2}$ die divergiert als $\epsilon\rightarrow 0$. Die beteiligten Wege sind daher stetig, besitzen jedoch keine Ableitung. Sie gehören zu einem Typ, der aus dem Studium der Brownschen Bewegung vertraut ist.

Gerade diese großen Geschwindigkeiten machen es so notwendig, bei der Näherung vorsichtig zu sein $S(x_{k+1},x_k)$ aus Gleichung (11).$^{15}$ Zum Ersetzen $V(x_{k+1})$ von $V(x_k)$ würde natürlich den Exponenten in (18) durch $i\epsilon[V(x_k)-V(x_{k+1})]/\hbar$ was von Ordnung ist $\epsilon(x_{k+1}-x_k)$, und führt somit zu unwichtigen Termen höherer Ordnung als $\epsilon$ auf der rechten Seite von (29). Aus diesem Grund sind (20) und (21) gleichermaßen zufriedenstellende Näherungen an $S(x_{i+1},x_i)$ wenn kein Vektorpotential vorhanden ist. Ein Term mit linearer Geschwindigkeit, der jedoch aus einem Vektorpotential entsteht, als $A\dot{x}dt$ muss vorsichtiger gehandhabt werden. Hier ein Begriff in $S(x_{k+1},x_k)$ wie zum Beispiel $A(x_{k+1})\times(x_{k+1}-x_k)$ unterscheidet sich von $A(x_k)(x_{k+1}-x_k)$ durch einen Ordnungsbegriff

$^{14}$Dr. Hartland Snyder hat mir in einem privaten Gespräch auf die sehr interessante Möglichkeit hingewiesen, dass es eine Verallgemeinerung der Quantenmechanik geben könnte, bei der die durch Experimente gemessenen Zustände nicht vorbereitet werden können; das heißt, es gäbe keinen Zustand, in den ein System versetzt werden kann, für den ein bestimmtes Experiment Gewissheit für ein Ergebnis liefert. Die Klasse der Funktionen $\chi$ ist nicht identisch mit der Klasse der verfügbaren Zustände $\psi$. Dies würde sich ergeben, wenn zum Beispiel, $\chi$ erfüllt eine andere Gleichung als $\psi$.

$^{15}$Gleichung (18) ist tatsächlich exakt, wenn (11) verwendet wird für $S(x_{i+1},x_i)$ für beliebige $\epsilon$ für Fälle, in denen das Potenzial nicht beinhaltet $x$ auf höhere Potenzen als die Sekunde (z. B. freies Teilchen, harmonischer Oszillator). Es ist jedoch notwendig, einen genaueren Wert von $A$. Man kann definieren $A$ auf diese Weise. Angenommen, klassische Teilchen mit $k$ Freiheitsgrade beginnen mit dem Punkt $x_i,t_i$, mit gleichmäßiger Dichte im Impulsraum. Schreibe die Anzahl der Teilchen mit einer gegebenen Impulskomponente im Bereich $dp$ als $dp/p_1$, mit $p_0$, konstant. Dann $A=(2\pi\hbar i/p_0)^{k/2}\rho^{-1/2}$, wobei $\rho$ ist die Dichte in $k$ dimensionaler Koordinatenraum $x_{i+1}$ dieser Teilchen zur Zeit $t_{i+1}$.

17

$(x_{k+1} - x_k)^2$, und somit der Ordnung $\epsilon$. Ein solcher Term würde zu einer Änderung der resultierenden Wellengleichung führen. Aus diesem Grund ist die Näherung (21) keine ausreichend genaue Näherung zu (11) und eine wie (20), (oder (19), von der sich (20) um Terme höherer Ordnung als $\epsilon$) muss verwendet werden. Wenn $\mathbf{A}$ repräsentiert das Vektorpotential und $\mathbf{p} = (\hbar/i)\nabla$, der Impulsoperator, dann ergibt (20) im Hamiltonoperatoren einen Term $(1/2m)(\mathbf{p} - (e/c)\mathbf{A}) \cdot (\mathbf{p} - e/c)\mathbf{A}$, während (21) ergibt $(1/2m)(\mathbf{p} \cdot \mathbf{p} - (2e/c)\mathbf{A} \cdot \mathbf{p} + (e^2/c^2)\mathbf{A} \cdot \mathbf{A})$. Diese beiden Ausdrücke unterscheiden sich durch $(\hbar e/2imc) \nabla \cdot \mathbf{A}$ was vielleicht nicht null ist. Die Frage ist noch wichtiger im Zusammenhang mit dem Koeffizienten der Terme, die quadratisch in den Geschwindigkeiten sind. In diesen Begriffen sind (19) und (20) keine ausreichend genauen Darstellungen von (11) im Allgemeinen. Wenn die Koeffizienten konstant sind, können (19) oder (20) für (11) eingesetzt werden. Wenn ein Ausdruck wie (19) verwendet wird, zum Beispiel für sphärische Koordinaten, obwohl er keine gültige Näherung an (11) darstellt, erhält man eine Schrödinger-Gleichung, bei der der Hamiltonsche Operator einige der Impulsoperatoren und Koordinaten in falscher Reihenfolge besitzt. Gleichung (11) löst dann die Mehrdeutigkeit in der üblichen Regel auf, die ersetzt wird $p$ und $q$ durch die nichtkommutierenden Größen $(\hbar/i)(\partial/\partial q)$ und $q$ im klassischen Hamiltonoperator $H(p, q)$.

Es ist klar, dass die Aussage (11) unabhängig vom Koordinatensystem ist. Daher ist das einfachste Verfahren, um die Differentialwellengleichung in jedem Koordinatensystem zu finden, zunächst die Gleichungen in kartesischen Koordinaten zu finden und dann das Koordinatensystem auf das gewünschte zu transformieren. Es genügt daher, die Beziehung der Postulate und der Schrödingerschen Gleichung in rechteckigen Koordinaten zu zeigen.

Die hier für eine Dimension gegebene Herleitung kann direkt auf den Fall dreidimensionaler kartesischer Koordinaten für jede beliebige Zahl erweitert werden, $K$, von Teilchen, die durch Potentiale miteinander wechselwirken, und in einem Magnetfeld, das durch ein Vektorpotential beschrieben wird. Die Terme im Vektorpotential erfordern, dass das Quadrat im Exponenten auf die übliche Weise für Gaußsche Integrale vervollständigt wird. Die Variable $x$ muss durch die Menge ersetzt werden $x^{(1)}$ zu $x^{(3K)}$ wobei $x^{(1)}, x^{(2)}, x^{(3)}$ sind die Koordinaten des ersten massenhaften Teilchens $m_1, x^{(4)}, x^{(5)}, x^{(6)}$ der Sekunde der Messe $m_2$, usw. Das Symbol $dx$ wird ersetzt durch $dx^{(1)}dx^{(2)} \dots dx^{(3K)}$, und die Integration über $dx$ wird durch ein ersetzt. $3K$-Faltintegral. Die Konstante $A$ hat in diesem Fall den Wert $A = (2\pi\hbar e i/m_1)^{1/2}(2\pi\hbar e i/m_2)^{1/2} \dots (2\pi\hbar e i/m_K)^{1/2}$. Die Lagrangefunktion ist die klassische Lagrangefunktion für dasselbe Problem, und die daraus resultierende Schrödinger-Gleichung ist die, die dem klassischen Hamiltonoperator entspricht, der aus dieser Lagrangefunktion abgeleitet ist. Die Gleichungen in jedem anderen Koordinatensystem können durch Transformation gewonnen werden. Da dies alle Fälle einschließt, für die Schrödingers Gleichung experimentell überprüft wurde, können wir sagen, dass unsere

18

Postulate sind in der Lage, das zu beschreiben, was durch nichtrelativistische Quantenmechanik beschrieben werden kann, und dabei Spin zu vernachlässigen.

## 7. Diskussion der Wellengleichung

### Die klassische Grenze

Dies vervollständigt die Demonstration der Äquivalenz der neuen und alten Formulierungen. Wir möchten in diesem Abschnitt einige Bemerkungen zur wichtigen Gleichung (18) aufnehmen.

Diese Gleichung gibt die Entwicklung der Wellenfunktion während eines kleinen Zeitintervalls an. Es lässt sich physikalisch leicht als Ausdruck des Huygensschen Prinzips für Materiewellen interpretieren. In der geometrischen Optik erfüllen die Strahlen in einem inhomogenen Medium das Fermatsche Prinzip des Kleinsten *Zeit*. Wir können Huygens' Prinzip in der Wellenoptik folgendermaßen formulieren: Wenn die Amplitude der Welle auf einer gegebenen Fläche bekannt ist, kann die Amplitude an einem Near by Punkt als Summe der Beiträge aller Punkte betrachtet werden. Jeder Beitrag wird phasenweise um einen Betrag verzögert, der proportional zu den *Zeit* Es würde das Licht brauchen, um von der Oberfläche bis zum Punkt entlang des Strahls des kleinsten zu gelangen *Zeit* von geometrischer Optik. Wir können (22) analog betrachten, beginnend mit Hamiltons erstem Prinzip der geringsten *Aktion* für klassische oder 'geometrische' Mechanik. Wenn die Amplitude der Welle $\psi$ ist auf einer gegebenen 'Fläche' bekannt, insbesondere der 'Oberfläche', die aus allen besteht $x$ zu dieser Zeit $t$, seinen Wert an einem bestimmten nahegelegenen Zeitpunkt $t + \epsilon$, ist eine Summe der Beiträge von allen Punkten der Fläche bei $t$. Jeder Beitrag wird phasenweise um einen Betrag verzögert, der proportional zu den *Aktion* Es würde erfordern, von der Oberfläche bis zum Punkt entlang des Pfades der kleinsten Wirkung der klassischen Mechanik zu gelangen. $^{16}$

Tatsächlich ist Huygens' Prinzip in der Optik nicht korrekt. Sie wird durch Kirchhoffs Modifikation ersetzt, die verlangt, dass sowohl die Amplitude als auch ihre Ableitung auf der benachbarten Fläche bekannt sein müssen. Dies ist eine Folge der Tatsache, dass die Wellengleichung in der Optik in der Zeit zweiter Ordnung ist. Die Wellengleichung der Quantenmechanik ist erste Ordnung der Zeit; daher gilt Huygens' Prinzip *ist* Korrekte für Materiewellen, Aktion ersetzt die Zeit.

Die Gleichung kann auch mathematisch mit Größen verglichen werden, die in den üblichen Formulierungen auftreten. In Schrödingers Methode wird die Entwicklung der Wellenfunktion mit der Zeit gegeben durch

$$- \frac{\hbar}{i} \frac{\partial \psi}{\partial t} = \mathbf{H} \psi, \quad (31)$$

---$^{16}$Siehe in diesem Zusammenhang die sehr interessanten Bemerkungen von Schroedinger, Ann. d. Physik **79**, 489 (1926).

19

die die Lösung hat (für beliebige $\epsilon$ wenn $\mathbf{H}$ ist zeitunabhängig)

$$\psi(x, t + \epsilon) = \exp(-i\epsilon\mathbf{H}/\hbar)\psi(x, t). \quad (32)$$

Daher drückt Gleichung (18) den Operator aus $\exp(-i\epsilon\mathbf{H}/\hbar)$ durch einen approximativen Integraloperator für kleine $\epsilon$.

Aus Heisenbergs Sicht betrachtet man die Position zur Zeit $t$, zum Beispiel als Operator $\mathbf{x}$. Die Position $\mathbf{x}'$ zu einem späteren Zeitpunkt $t + \epsilon$ kann in Bezug auf das zu Zeitpunkt ausgedrückt werden $t$ durch die Operatorgleichung

$$\mathbf{x}' = \exp(i\epsilon\mathbf{H}/\hbar)\mathbf{x}\exp(-i\epsilon\mathbf{H}/\hbar). \quad (33)$$

Die Transformationstheorie von Dirac ermöglicht es uns, die Wellenfunktion zur Zeit zu betrachten $t + \epsilon$, $\psi(x', t + \epsilon)$, als Darstellung eines Zustands in einer Darstellung, in der $\mathbf{x}'$ diagonal ist, während $\psi(x, t)$ denselben Zustand in einer Darstellung darstellt, in der $\mathbf{x}$ diagonal ist. Sie sind daher durch die Transformationsfunktion miteinander verbunden $(x'|x)_\epsilon$, die diese Darstellungen miteinander verknüpft:

$$\psi(x', t + \epsilon) = \int (x'|x)_\epsilon\psi(x, t)dx.$$

Daher soll der Inhalt von Gleichung (18) zeigen, dass für kleine $\epsilon$ Wir können festlegen

$$(x'|x)_\epsilon = (1/A)\exp(iS(x', x)/\hbar) \quad (34)$$

mit $S(x', x)$ definiert wie in (11).

Die enge Analogie zwischen $(x', |x)_\epsilon$ und die Menge $\exp(iS(x', x)/\hbar)$ Dirac hat mehrfach darauf hingewiesen.$^{17}$ Tatsächlich sehen wir jetzt, dass die beiden Größen nach hinreichenden Näherungen als proportional zueinander angesehen werden können. Diracs Bemerkungen bildeten den Ausgangspunkt der aktuellen Entwicklung. Die Punkte, die er bezüglich des Übergangs zur klassischen Grenze anspricht $\hbar \rightarrow 0$ sind sehr schön, und ich darf vielleicht entschuldigen, sie hier kurz zu besprechen.

Zuerst stellen wir fest, dass die Wellenfunktion bei $x''$ zu dieser Zeit $t''$ kann aus dem ermittelt werden, dass bei $x'$ zu dieser Zeit $t'$ von

$$\psi(x'', t'') = \lim_{\epsilon \rightarrow 0} \int \dots \int \times \times \exp\left[ \frac{i}{\hbar} \sum_{i=0}^{j-1} S(x_{i+1}, x_i) \right] \times \psi(x', t') \frac{dx_0}{A} \frac{dx_1}{A} \dots \frac{dx_{j-1}}{A}, \quad (35)$$

$^{17}$P. A. M. Dirac, *Die Prinzipien der Quantenmechanik* (The Clarendon Press, Oxford, 1935), zweite Auflage, Abschnitt 33; außerdem Physik. Zeits. Sowjetunion **3**, 64 (1933).

20

wo wir setzen $x_0 \equiv x''$ und $x_j \equiv x''$ wobei $i\epsilon = t'' - t'$ (zwischen den Zeiten) $t'$ und $t''$ wir nehmen an, dass keine Einschränkung für den Integrationsbereich auferlegt wird). Dies lässt sich entweder durch wiederholte Anwendungen von (18) oder direkt aus Gleichung (15) erkennen. Nun fragen wir, als $\hbar \rightarrow 0$ Welche Werte der Zwischenkoordinaten $x_i$, trägt am stärksten zum Integral bei? Diese sind die Werte, die am wahrscheinlichsten durch Experimente gefunden werden und bestimmen somit im Grenzfall den klassischen Pfad. Wenn $\hbar$ sehr klein ist, ist der Exponent eine sehr schnell variierende Funktion einer seiner Variablen $x_i$. Als $x_i$, variiert, die positiven und negativen Beiträge des Exponenten fast aufheben. Die Region, in der $x_i$, trägt am stärksten dazu bei, dass die Phase des Exponenten am wenigsten mit schwankt. $x_i$ (Methode der stationären Phase). Nennen Sie die Summe im Exponent $S$;

$$S = \sum_{i=0}^{j-1} S(x_{i+1}, x_i). \quad (36)$$

Dann verläuft die klassische Bahn ungefähr durch diese Punkte $x_i$ wobei die Änderungsrate von $S$ mit $x_i$, ist klein oder im Grenzfall von klein $\hbar$, null, d. h. die klassische Bahn durchläuft die Punkte, an denen $\partial S/\partial x_i$ für alle $x_i$. Das Limit nehmen $\epsilon \rightarrow 0$, (36) wird im Sinne von (11)

$$S = \int_{t'}^{t''} L(\dot{x}(t), x(t)) dt. \quad (37)$$

Wir sehen dann, dass der klassische Pfad der ist, für den das Integral (37) keine Erstordnungsänderung beim Variieren des Pfades erleidet. Dies ist Hamiltons Prinzip und führt direkt zu den Lagrange-Bewegungsgleichungen.

## 8. Operatoralgebra

### Matrixelemente

Gegeben die Wellenfunktion und die Schrödingersche Gleichung können natürlich alle Mechanismen der Operator- oder Matrixalgebra entwickelt werden. Es ist jedoch recht interessant, diese Konzepte in einer etwas anderen Sprache auszudrücken, die näher an der bei der Darstellung der Postulate verwendeten Sprache steht. Dabei wird bei der Aufklärung der Operatoralgebra wenig gewonnen. Tatsächlich sind die Ergebnisse einfach eine Übersetzung einfacher Operatorgleichungen in eine etwas umständlichere Notation. Andererseits sind die neue Notation und der Standpunkt in bestimmten in der Einleitung beschriebenen Anwendungen sehr nützlich. Darüber hinaus erlaubt die Form der Gleichungen eine natürliche Erweiterung auf eine größere

21

Klasse von Operatoren, die üblicherweise betrachtet werden (z. B. solche, bei denen Größen auf zwei oder mehr verschiedene Zeiten verweisen). Wenn eine Verallgemeinerung auf eine größere Klasse von Aktionsfunktionalen möglich ist, werden die zu entwickelnden Formeln eine wichtige Rolle spielen.

Wir besprechen diese Punkte in den nächsten drei Abschnitten. Dieser Abschnitt beschäftigt sich hauptsächlich mit Definitionen. Wir definieren eine Größe, die wir Übergangselement zwischen zwei Zuständen nennen. Es ist im Wesentlichen ein Matrixelement. Aber anstatt das Matrixelement zwischen einem Zustand zu sein $\psi$ und noch ein weiteres $\chi$ entsprechend dem *Gleiches* Zeit, beziehen sich diese beiden Bundesstaaten auf unterschiedliche Zeiten. Im folgenden Abschnitt wird eine fundamentale Beziehung zwischen Übergangselementen entwickelt, aus der die üblichen Kommutationsregeln zwischen Koordinate und Impuls abgeleitet werden können. Die gleiche Beziehung liefert auch die Newtonsche Bewegungsgleichung in Matrixform. Abschließend diskutieren wir in Abschnitt 10 die Beziehung des Hamiltonoperators zur Operation der Verschiebung in der Zeit.

Wir beginnen damit, ein Übergangselement in Bezug auf die Wahrscheinlichkeit des Übergangs von einem Zustand in einen anderen zu definieren. Genauer gesagt, nehmen wir an, wir haben eine Situation, die der in der Ableitung beschriebenen (17) ähnelt. Die Region $R$ besteht aus einer Region $R'$ Vor dem $t'$, alle Räume dazwischen $t'$ und $t''$ und die Region $R''$ danach $t''$. Wir werden die Wahrscheinlichkeit untersuchen, dass ein System in der Region $R'$ wird später in der Region gefunden $R''$. Dies ist gegeben durch (17). Wir werden in diesem Abschnitt erläutern, wie sie sich mit Veränderungen in der Form der Lagrangefunktion zwischen verändert $t'$ und $t''$. In Abschnitt 10 erläutern wir, wie es sich mit Änderungen in der Vorbereitung ändert $R'$ oder das Experiment $R''$.

Der Zustand zur Zeit $t'$ ist vollständig definiert durch die Präparation $R'$. Sie kann durch eine Wellenfunktion spezifiziert werden $\psi(x', t')$ erhalten wie in (15), aber bis zur jeweiligen Zeit nur Integrale enthalten $t'$. Ebenso ist der für das Experiment charakteristische Zustand (Region $R''$) kann durch eine Funktion definiert werden $\chi(x'', t'')$ erhalten aus (16) mit nur Integralen jenseits $t''$. Die Wellenfunktion $\psi(x'', t'')$ zu dieser Zeit $t''$ kann natürlich auch durch angemessene Nutzung von (15) erreicht werden. Es kann auch von $\psi(x', t')$ von (35). Laut (17) mit $t''$ Verwendet statt $t$, die Wahrscheinlichkeit, gefunden zu werden in $\chi$ Es wurde vorbereitet in $\psi$ ist das Quadrat dessen, was wir die Übergangsamplitude nennen werden. $\int \chi^*(x'', t'') \psi(x'', t'') dx''$. Wir möchten dies ausdrücken: $\chi$ bei $t''$ und $\psi$ bei $t'$. Dies können wir mit Hilfe von (35) erreichen. Daher besteht die Wahrscheinlichkeit, dass ein System im Staat vorbereitet ist $\psi_{t'}$ zu dieser Zeit $t'$ wird danach gefunden werden $t''$ in einem Zustand zu sein $\chi_{t''}$ ist das Quadrat der Übergangsamplitude

$$\langle \chi_{t''} | 1 | \psi_{t'} \rangle_S = \lim_{\epsilon \to 0} \int \dots \int \chi^*(x'', t'') \times \\ \times \exp(iS/\hbar) \psi(x', t') \frac{dx_0}{A} \dots \frac{dx_{j-1}}{A} dx_j, \quad (38)$$

22

wobei wir die Abkürzung (36) verwendet haben.

In der Sprache der gewöhnlichen Quantenmechanik, wenn der Hamiltonoperator H konstant ist, $\psi(x, t'') = \exp[-i(t'' - t')\mathbf{H}/\hbar]\psi(x, t')$ so dass (38) das Matrizenelement von ist $\exp[-i(t'' - t')\mathbf{H}/\hbar]$ Zwischen Staaten $\chi_{t''}$ und $\psi_{t'}$.

Wenn $F$ eine beliebige Funktion der Koordinaten ist $x_i$ für $t' < t_i < t''$, definieren wir das Übergangselement von $F$ Zwischen den Bundesstaaten $\psi$ bei $t'$ und $\chi$ bei $t''$ für die Aktion $S$ als $(x'' \equiv x_j, x' \equiv x_0)$:

$$\langle \chi_{t''} | F | \psi_{t'} \rangle = \lim_{\epsilon \to 0} \int \dots \int \times \chi^*(x'', t'') F(x_0, x_1, \dots x_i) \cdot$$

$$\cdot \exp \left[ \frac{i}{\hbar} \sum_{i=0}^{j-1} S(x_{i+1}, x_i) \right] \psi(x', t') \frac{dx_0}{A} \dots \frac{dx_{j-1}}{A} dx_i. \tag{39}$$

Im Grenzfall $\epsilon \to 0$, $F$ ist eine Funktionalität des Weges $x(t)$.

Wir werden gleich sehen, warum solche Mengen wichtig sind. Es wird leichter zu verstehen sein, wenn wir einen Moment innehalten, um herauszufinden, wozu die Größen in der konventionellen Notation passen. Angenommen $F$ ist einfach $x_k$, wobei $k$ entspricht einer bestimmten Zeit $t = t_k$. Dann auf der rechten Seite von (39) die Integrale aus $x_0$ zu $x_{k-1}$ kann durchgeführt werden, um zu produzieren $\psi(x_k, t)$ oder $\exp[-i(t - t')\mathbf{H}/\hbar]\psi_{t'}$. In ähnlicher Weise gelten die Integrale auf $x_i$ für $j \ge i > k$ Gib $\chi^*(x_k, t)$ oder $\{\exp[-i(t'' - t)\mathbf{H}/\hbar]\chi_{t''}\}$. Daher ist das Übergangselement von $x_k$,

$$\langle \chi_{t''} | F | \psi_{t'} \rangle_S = \int \chi_{t''}^* e^{(i/\hbar)\mathbf{h}(t'' - t)} x e^{-(i/\hbar)\mathbf{H}(t - t')} \psi_{t'} dx =$$
$$= \int \chi^*(x, t) x \psi(x, t) dx \tag{40}$$

ist das Matrixelement von $\mathbf{x}$ zu dieser Zeit $t = t_k$ zwischen dem Zustand, der sich zur Zeit entwickeln würde $t$ von $\psi_{t'}$ bei $t'$ und der Zustand, der sich mit der Zeit entwickeln wird $t$ zu $\chi_{t''}$ bei $t''$. Es ist daher das Matrixelement von $\mathbf{x}(t)$ zwischen diesen Zuständen.

Ebenso gilt gemäß (39) mit $F = x_{k+1}$, das Übergangselement von $x_{k+1}$ ist das Matrixelement von $\mathbf{x}(t + \epsilon)$. Das Übergangselement von $F = (x_{k+1} - x_k)/\epsilon$ ist das Matrixelement von $(\mathbf{x}(t + \epsilon) - \mathbf{x}(t))/\epsilon$ oder von $i(\mathbf{H}\mathbf{x} - \mathbf{x}\mathbf{H})/\hbar$, wie leicht aus (40) gezeigt wird. Wir können dies das Matrixelement der Geschwindigkeit nennen $\dot{x}(t)$.

Angenommen, wir betrachten ein zweites Problem, das sich vom ersten unterscheidet, weil zum Beispiel das Potential um eine kleine Menge erhöht wird $U(\cdot, \mathbf{x}t)$. Dann ersetzt im neuen Problem die Größe $S$ ist $S' = S + \sum_i \epsilon U(x_i, t_i)$. Die Substitution in (38) führt direkt zu

$$\langle \chi_{t''} | 1 | \psi_{t'} \rangle_{S'} = \left\langle \chi_{t''} \left| \exp \frac{i\epsilon}{\hbar} \sum_{i=1}^j U(x_i, t_i) \right| \psi_{t'} \right\rangle_S. \tag{41}$$

23

Daher sind Übergangselemente wie (39) insofern wichtig, als $F$ kann in irgendeiner Weise aus einer Veränderung entstehen $\delta S$ in einem Handlungsausdruck. Mit beobachtbaren Funktionalen bezeichnen wir diese Funktionale $F$ die (möglicherweise indirekt) in Bezug auf die Veränderungen definiert werden kann, die durch mögliche Änderungen der Wirkung entstehen $S$. Die Bedingung, dass ein Funktional beobachtbar sein muss, ähnelt in gewisser Weise der Bedingung, dass ein Operator hermitisch ist. Die beobachtbaren Funktionale sind eine eingeschränkte Klasse, da die Wirkung eine quadratische Funktion der Geschwindigkeiten bleiben muss. Aus einer beobachtbaren Funktion können zum Beispiel weitere abgeleitet werden durch

$$\langle \chi_{t''} | F | \psi_{t'} \rangle_{S'} = \left\langle \chi_{t''} \left| F \exp \frac{i\epsilon}{\hbar} \sum_{i=1}^j U(x_i, t_i) \right| \psi_{t'} \right\rangle_S \quad (42)$$

was aus (39) ermittelt wird.

Übrigens führt (41) direkt zu einer wichtigen Störungsformel. Wenn der Effekt von $U$ klein ist, kann die Exponentialstufe in auf erste Ordnung erweitert werden $U$ und wir finden

$$\langle \chi_{t''} | 1 | \psi_{t'} \rangle_{S'} = \left\langle \chi_{t''} | 1 | \psi_{t'} \right\rangle_S + \frac{i}{\hbar} \langle \chi_{t''} | \sum_i \epsilon U(x_i, t_i) | \psi_{t'} \right\rangle. \quad (43)$$

Von besonderer Bedeutung ist der Fall, dass $\chi_{t''}$ ist ein Zustand, in dem sich $\psi_{t'}$ Wäre es nicht zu finden, wäre es nicht. Für die Störung, $U$ (d.h. $\langle \chi_{t''} | 1 | \psi_{t'} \rangle_S = 0$) Dann

$$\frac{1}{\hbar^2} |\langle \chi_{t''} | \sum_i \epsilon U(x_i, t_i) | \psi_{t'} \rangle_S|^2 \quad (44)$$

ist die Wahrscheinlichkeit eines Übergangs, wie sie durch die Störung in erste Ordnung induziert wird. In der gewöhnlichen Notation,

$$\langle \chi_{t''} | \sum_i \epsilon U(x_i, t_i) | \psi_{t'} \rangle_S = \int \left\{ \int \chi_{t''}^* e^{-(i/\hbar)\mathbf{H}(t''-t)} \mathbf{U} e^{-(i/\hbar)\mathbf{H}(t-t')} \psi_{t'} dx \right\} dt$$

so dass (44) auf den üblichen Ausdruck reduziert wird $^{18}$ für zeitabhängige Störungen.

## 9. Newtons Gleichungen

### Die Kommutationsrelation

In diesem Abschnitt stellen wir fest, dass verschiedene Funktionale identische Ergebnisse liefern können, wenn sie zwischen beliebigen zwei Zuständen genommen werden. Diese Äquivalenz zwischen Funktionalen

$^{18}$P. A. M. Dirac, *Die Prinzipien der Quantenmechanik* (The Clarendon Press, Oxford, 1935), zweite Auflage, Abschnitt 47, Eq. (20)

24

ist die Aussage der Operatorgleichungen in der neuen Sprache.

Wenn $F$ Je nach verschiedenen Koordinaten können wir natürlich ein neues Funktional definieren $\partial F/\partial x_k$ indem man ihn bezüglich einer seiner Variablen differenziert, sagen wir $x_k (0 < k < j)$. Wenn wir berechnen $\langle \chi_{t'} | \partial F/\partial x_k | \psi_{t'} \rangle_S$ durch (39) enthält das Integral auf der rechten Seite $\partial F/\partial x_k$. Der einzige andere Ort, an dem die Variable $x_k$ erscheint in $S$. Daher ist die Integration auf $x_k$ kann in Teilen gespielt werden. Der integrierte Teil verschwindet (unter der Annahme, dass Wellenfunktionen im Unendlichen verschwinden) und bleibt mit der Größe zurück $-F(\partial/\partial x_k)\exp(iS/\hbar)$ im Integral. Allerdings, $(\partial/\partial x_k)\exp(iS/\hbar) = (i/\hbar)(\partial S/\partial x_k)\exp(iS/\hbar)$, also stellt die rechte Seite das Übergangselement von dar $-(i/\hbar)F(\partial S/\partial x_k)$, d.h.,

$$\left\langle \chi_{t'} \left| \frac{\partial F}{\partial x_k} \right| \psi_{t'} \right\rangle_S = -\frac{i}{\hbar} \left\langle \chi_{t'} \left| F \frac{\partial S}{\partial x_k} \right| \psi_{t'} \right\rangle_S. \tag{45}$$

Diese sehr wichtige Relation zeigt, dass zwei verschiedene Funktionale dasselbe Ergebnis für das Übergangselement zwischen beliebigen zwei Zuständen liefern können. Wir sagen, sie seien äquivalent und symbolisieren die Beziehung durch

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \frac{\partial S}{\partial x_k}, \tag{46}$$

Das Symbol $\underset{S}{\leftrightarrow}$ wobei betont wird, dass Funktionale unter einer Aktion nicht unter einer anderen äquivalent sein müssen. Die in (46) genannten Größen müssen nicht beobachtbar sein. Die Äquivalenz ist jedoch wahr. Unter Verwendung von (36) kann man schreiben

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \left[ \frac{\partial S(x_{k+1}, x_k)}{\partial x_k} + \frac{\partial S(x_k, x_{k-1})}{\partial x_k} \right]. \tag{47}$$

Diese Gleichung ist wahr zu null und erster Ordnung in $\epsilon$ und hat als Konsequenz die Kommutationsrelationen von Impuls und Koordinate sowie die newtonschen Bewegungsgleichungen in Matrixform.

Im Fall unseres einfachen eindimensionalen Problems, $S(x_{i+1}, x_i)$ ist durch den Ausdruck (15) gegeben, so dass

$$\partial S(x_{k+1}, x_k)/\partial x_k = -m(x_{k+1} - x_k)/\epsilon,$$

und

$$\partial S(x_k, x_{k-1})/\partial x_k = +m(x_k - x_{k-1})/\epsilon - \epsilon V'(x_k);$$

wobei wir schreiben $V'(x)$ für die Ableitung des Potentials oder der Kraft. Dann wird (47)

$$-\frac{\hbar}{i} \frac{\partial F}{\partial x_k} \underset{S}{\leftrightarrow} F \left[ -m \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - \epsilon V'(x_k) \right]. \tag{48}$$

25

Wenn $F$ hängt nicht von der Variablen ab $x_k$, dies ergibt Newtons Bewegungsgleichungen. Zum Beispiel, wenn $F$ ist konstant, sagen wir Einheit, (48) ergibt einfach (dividiert durch $\epsilon$)

$$0 \leftrightarrow_S -\frac{m}{\epsilon} \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - V'(x_k).$$

Somit ist das Übergangselement von Masse mal Beschleunigung $[(x_{k+1} - x_k)/\epsilon - (x_k - x_{k-1})/\epsilon]/\epsilon$ zwischen beliebigen zwei Zuständen ist gleich dem Übergangselement der Kraft $-V'(x_k)$ zwischen denselben Bundesstaaten. Dies ist der Matrixausdruck des Newtonschen Gesetzes, der in der Quantenmechanik gilt.

Was passiert, wenn $F$ hängt davon ab $x_k$? Zum Beispiel, sei $F = x_k$. Dann ergibt (48), da $\partial F/\partial x_k = 1$,

$$-\frac{\hbar}{i} \leftrightarrow_S x_k \left[ -m \left( \frac{x_{k+1} - x_k}{\epsilon} - \frac{x_k - x_{k-1}}{\epsilon} \right) - \epsilon V'(x_k) \right]$$

oder, indem sie die Ordnungsbedingungen vernachlässigen $\epsilon$,

$$m \left( \frac{x_{k+1} - x_k}{\epsilon} \right) x_k - m \left( \frac{x_k - x_{k-1}}{\epsilon} \right) x_k \leftrightarrow_S \frac{\hbar}{i}. \quad (49)$$

Um eine Gleichung wie (49) in die konventionelle Notation zu übertragen, müssen wir herausfinden, welche Matrix einer Größe wie $x_k x_{k+1}$. Aus einer Studie zu (39) geht klar hervor, dass, wenn $F$ ist gleich , sagen wir, $f(x_k)g(x_{k+1})$, der entsprechende Operator in (40) ist

$$e^{-(i/\hbar)(t'' - t - \epsilon)\mathbf{H}} g(\mathbf{x}) e^{-(i/\hbar)\epsilon\mathbf{H}} f(\mathbf{x}) e^{-(i/\hbar)(t - t')\mathbf{H}},$$

das Matrixelement wird zwischen den Zuständen genommen $\chi_{t''}$ und $\psi_{t'}$. Die Operatoren, die den Funktionen von entsprechen $x_{k+1}$ erscheint links von den Operatoren, die den Funktionen von entsprechen, $x_k$, d.h., *Die Ordnung der Terme in einem Matrixoperatorprodukt entspricht einer zeitlichen Ordnung der entsprechenden Faktoren in einem Funktional*. Wenn das Funktional also so geschrieben werden kann, dass in jedem Term Faktoren zu späteren Zeiten links von Faktoren erscheinen, die zu früheren Termen gehören, kann der entsprechende Operator sofort geschrieben werden, wenn die Reihenfolge der Operatoren gleich bleibt wie im Funktional. $^{19}$ Offensichtlich ist die Reihenfolge der Faktoren in einem Funktional unbedeutend. Die Reihenfolge erleichtert lediglich die Übersetzung in die konventionelle Operatornotation. Gleichung (49) so zu schreiben, wie es für eine einfache Übersetzung gewünscht ist

$^{19}$Dirac hat auch Operatoren untersucht, die Größen enthalten, die sich auf unterschiedliche Zeiten beziehen. Siehe Referenz 2.

26

würde erfordern, dass die Faktoren in der zweiten Amtszeit auf der linken Seite in der richtigen Reihenfolge umgekehrt werden. Wir sehen daher, dass es entspricht

$$\mathbf{px} - \mathbf{xp} = \hbar/i$$

wobei wir geschrieben haben $\mathbf{p}$ für den Operator $m\hat{\mathbf{x}}$.

Die Beziehung zwischen Funktionalen und den entsprechenden Operatoren ist oben in Bezug auf die Ordnung der Faktoren in der Zeit eingestuft. Es sei angemerkt, dass diese Regel besonders sorgfältig eingehalten werden muss, wenn Größen mit Geschwindigkeiten oder höheren Ableitungen beteiligt sind. Das korrekte Funktional, um den Operator darzustellen $(\dot{x})^2$ ist tatsächlich $(x_{k+1} - x_k)/\epsilon(x_k - x_{k-1})/\epsilon$ statt $[(x_{k+1} - x_k)/\epsilon]^2$. Letztere Größe divergiert als $1/\epsilon$ als $\epsilon \to 0$. Dies lässt sich erkennen, indem man den zweiten Term in (49) durch seinen Wert ersetzt $x_{k+1} \cdot m(x_{k+1} - x_k)/\epsilon$ berechnet in einem Augenblick $\epsilon$ später in der Zeit. Dies ändert die Gleichung nicht auf null Ordnung in $\epsilon$. Wir erhalten dann (indem wir teilen durch $\epsilon$)

$$\left(\frac{x_{k+1} - x_k}{\epsilon}\right)^2 \underset{S}{\leftrightarrow} -\frac{\hbar}{im\epsilon}. \tag{50}$$

Dies ergibt das zuvor ausgedrückte Ergebnis, nämlich dass die Wurzel das Quadrat der "Geschwindigkeit" mittelwert ist $(x_{k+1} - x_k)/\epsilon$ zwischen zwei aufeinanderfolgenden Positionen des Pfades ist von Ordnung $\epsilon^{-1/2}$.

Es taugt dann nicht, das Funktional für kinetische Energie zu schreiben, sagen wir, einfach als

$$\frac{1}{2}m[(x_{k+1} - x_k)/\epsilon]^2 \tag{51}$$

für diese Größe ist unendlich als $\epsilon \to 0$. Tatsächlich ist es kein beobachtbarer Funktional.

Man kann die kinetische Energie als beobachtbare Funktion bestimmen, indem man die Änderung der Übergangsamplitude erster Ordnung betrachtet, die durch eine Änderung der Masse des Teilchens verursacht wird. Lass $m$ geändert werden zu $m(1 + \delta)$ Für kurze Zeit, sagen wir $\epsilon$, um herum $t_k$. Die Änderung der Aktion ist $\frac{1}{2}\delta\epsilon m[x_{k+1} - x_k)/\epsilon]^2$ die Ableitung von ergibt einen Ausdruck wie (51). Aber die Veränderung in $m$ verändert die Normalisierungskonstante $1/A$ entsprechend $dx_k$ ebenso wie die Action. Die Konstante wird geändert von $(2\pi\hbar\epsilon i/m)^{-1/2}$ zu $(2\pi\hbar\epsilon i/m(1 + \delta))^{-1/2}$ oder durch $\frac{1}{2}\delta(2\pi\hbar\epsilon i/m)^{-1/2}$ an erste Ordnung in $\delta$. Die Gesamtwirkung der Massenänderung in Gleichung (38) auf die erste Ordnung in $\delta$ ist

$$\langle\chi_{t'}|\frac{1}{2}\delta\epsilon im[(x_{k+1} - x_k)/\epsilon]^2/\hbar + \frac{1}{2}\delta|\psi_{t'}\rangle.$$

27

Wir erwarten die Änderung der Ordnung $\delta$ Dauer eine Zeit lang $\epsilon$ um geordnet zu sein $\delta\epsilon$. Daher wird geteilt durch $\delta\epsilon i/\hbar$, können wir das kinetische Energiefunktional definieren als

$$\mathrm{K.E.} = \frac{1}{2}m[(x_{k+1} - x_k)/\epsilon]^2 + \hbar/2\epsilon i. \tag{52}$$

Dies ist endlich wie $\epsilon \to 0$ im Hinblick auf (50). Durch die Verwendung einer Gleichung, die sich aus der Substitution ergibt $m(x_{k+1} - x_k)/\epsilon$ für $F$ In (48) können wir auch zeigen, dass der Ausdruck (52) gleich ist (Ordnung) $\epsilon$) zu

$$\mathrm{K.E.} = \frac{1}{2}m\left(\frac{x_{k+1} - x_k}{\epsilon}\right)\left(\frac{x_k - x_{k-1}}{\epsilon}\right). \tag{53}$$

Das heißt, der einfachste Weg, beobachtbare Funktionale mit Potenzen der Geschwindigkeiten zu erzeugen, besteht darin, diese durch ein Produkt der Geschwindigkeiten zu ersetzen, wobei jeder Faktor zu einem leicht anderen Zeitpunkt genommen wird.

## 10. Der Hamiltonian

# **Schwung**

Der Hamiltonsche Operator ist von zentraler Bedeutung in der üblichen Formulierung der Quantenmechanik. In diesem Abschnitt werden wir die Funktional untersuchen, die diesem Operator entspricht. Wir könnten das Hamiltonsche Funktional sofort definieren, indem wir die kinetische Energiefunktional (52) oder (53) zur potenziellen Energie addieren. Diese Methode ist künstlich und weist nicht die wichtige Beziehung des Hamiltonoperators zur Zeit auf. Wir definieren das Hamilton-Funktional durch die Veränderungen, die in einem Zustand vorgenommen werden, wenn er zeitlich verschoben ist.

Dazu müssen wir kurz abschweifen, um darauf hinzuweisen, dass die Unterteilung der Zeit in *gleich* Intervalle sind nicht notwendig. Offensichtlich jede Unterteilung in Instants $t_i$ zufriedenstellend sein; Die Grenzen sind als größter Abstand zu betrachten, $t_{i+1} - t_i$ nähert sich Null. Die Gesamtaktion $S$ muss nun als Summe dargestellt werden

$$S = \sum_i S(x_{i+1}, t_{i+1}; x_i, t_i), \tag{54}$$

wobei

$$S(x_{i+1}, t_{i+1}; x_i, t_i) = \int_{t_i}^{t_i+1} L(\dot{x}(t), x(t)) dt, \tag{55}$$

28

das Integral wird entlang des klassischen Pfades zwischen $x_i$, bei $t_i$ und $x_{i+1}$ bei $t_{i+1}$. Für das einfache eindimensionale Beispiel wird dies mit ausreichender Genauigkeit,

$$S(x_{i+1}, t_{i+1}; x_i, t_i) = \left\{ \frac{m}{2} \left( \frac{x_{i+1} - x_i}{t_{i+1} - t_i} \right)^2 - V(x_{i+1}) \right\} (t_{i+1} - t_i); \quad (56)$$

die entsprechende Normalisierungskonstante für Integration auf $dx_i$ ist $A = (2\pi\hbar i(t_{i+1} - t_i)/m)^{-1/2}$.

Die Beziehung von $H$ Der Wandel eines Zustands mit Zeitverschiebung kann nun untersucht werden. Betrachten wir einen Zustand $\psi(t)$ definiert durch eine Raumzeitregion $R'$. Stellen Sie sich nun vor, wir betrachten einen anderen Zustand zur Zeit $t$, $\psi_\delta(t)$, von einer anderen Region bedeckt $R'_\delta$. Angenommen, die Region $R'_\delta$ ist genau dasselbe wie $R'$ außer dass es um eine Zeit früher ist $\delta$, d. h. körperlich in die Vergangenheit verschoben durch eine Zeit $\delta$. Alle Geräte zur Vorbereitung des Systems für $R'_\delta$ ist identisch mit der für $R'$ wird jedoch eine Zeit betrieben $\delta$ Früher. Wenn $L$ hängt explizit von der Zeit ab, auch sie soll verdrängt werden, also der Staat $\psi_\delta$ ergibt sich aus dem $L$ Verwendet für den Staat $\psi$ außer dass die Zeit $t$ in $L_\delta$ wird ersetzt durch $t + \delta$. Wir fragen, wie der Staat vorgeht $\psi_\delta$ unterscheiden von $\psi$? In jeder Messung ist die Wahrscheinlichkeit, das System in einem festen Bereich zu finden, die $R''$ ist anders für $R'$ und $R'_\delta$. Betrachten wir die Änderung im Übergangselement $\langle \chi | 1 | \psi_\delta \rangle_{S_\delta}$ Von The Shift produziert $\delta$. Wir können diese Verschiebung als bewirkt betrachten, indem alle Werte von abgenommen werden $t_i$ von $\delta$ für $i \leq k$ und alle zurückzulassen $t_i$ Fixiert für $i > k$, wo die Zeit $t$ liegt im Intervall zwischen $t_{k+1}$ und $t_k$. $^{20}$ Diese Änderung hat keine Auswirkungen auf $S(x_{i+1}, t_{i+1}; x_i, t_i)$ wie in (55) definiert, solange beide $t_{i+1}$ und $t_i$ um denselben Betrag geändert werden. Andererseits, $S(x_{k+1}, t_{k+1}; x_k, t_k)$ wird geändert zu $S(x_{k+1}, t_{k+1}; x_k, t_k - \delta)$. Die Konstante $1/A$ für die Integration auf $dx_k$, wird ebenfalls geändert zu $(2\pi\hbar i(t_{k+1} - t_k + \delta)/m)^{-1/2}$. Die Wirkung dieser Änderungen auf das Übergangselement wird der ersten Ordnung in $\delta$ von

$$\langle \chi | 1 | \psi \rangle_S - \langle \chi | 1 | \psi_\delta \rangle_{S_\delta} = \frac{i\delta}{\hbar} \langle \chi | H_k | \psi \rangle_S, \quad (57)$$

hier ist die Hamiltonsche Funktional $H_k$ ist definiert durch

$$H_k = \frac{\partial S(x_{k+1}, t_{k+1}; x_k t_k)}{\partial t_k} + \frac{\hbar}{2i(t_{k+1} - t_k)}. \quad (58)$$

$^{20}$Aus Sicht der mathematischen Strenge, wenn $\delta$ endlich ist, als $\epsilon \rightarrow 0$ Man gerät in Schwierigkeiten, wenn zum Beispiel das Intervall $t_{k+1} - t_k$ bleibt endlich. Dies kann durch Annahme ausgeklärt werden $\delta$ um sich mit der Zeit zu verändern und vorher reibungslos eingeschaltet zu werden $t = t_k$ und schaltete sich danach sanft ab $t = t_k$. Dann wird die Zeitvariation von beibehalten $\delta$ fest, lass $\epsilon \rightarrow 0$. Dann suche die Erstordnungsänderung als $\delta \rightarrow 0$. Das Ergebnis ist im Wesentlichen dasselbe wie bei der oben verwendeten groben Methode.

29

Der letzte Term ist auf die Änderung in $1/A$ und dient zur Erhaltung $H_k$ endlich als $\epsilon \to 0$. Zum Beispiel gilt für den Ausdruck (56)

$$H_k = \frac{m}{2} \left( \frac{x_{k+1} - x_k}{t_{k+1} - t_k} \right) + \frac{\hbar}{2i(t_{k+1} - t_k)} + V(x_{k+1}),$$

was einfach die Summe aus dem kinetischen Energiefunktional (52) und der der potenziellen Energie ist $V(x_{k+1})$.

Die Wellenfunktion $\psi_\delta(x, t)$ repräsentiert natürlich denselben Bundesstaat wie $\psi(x, t)$ Wird es nach der Zeit sein $\delta$, d.h., $\psi(x, t + \delta)$. Daher steht (57) in engem Zusammenhang mit der Operatorgleichung (31).

Man könnte auch Veränderungen berücksichtigen, die durch eine Zeitverschiebung im Endzustand verursacht werden $\chi$. Natürlich führt auf diese Weise nichts Neues, denn es ist nur die relative Verschiebung von $\chi$ und $\psi$ Was zählt. Man erhält einen alternativen Ausdruck

$$H_k = - \frac{\partial S(x_{k+1}, t_{k+1}; x_k, t_k)}{\partial t_{k+1}} + \frac{\hbar}{2i(t_{k+1} - t_k)}. \tag{59}$$

Dies unterscheidet sich von (58) nur durch die Ordnungsbedingungen $\epsilon$. Die zeitliche Änderungsrate eines Funktionals kann berechnet werden, indem man den Effekt betrachtet, sowohl den Anfangs- als auch den Endzustand gemeinsam zu verschieben. Dies hat denselben Effekt wie die Berechnung des Übergangselements der Funktional, die sich auf eine spätere Zeit bezieht. Das Ergebnis ist das Analogon zur Operatorgleichung

$$\frac{\hbar}{i} \dot{\mathbf{f}} = \mathbf{H} \mathbf{f} - \mathbf{f} \mathbf{H}.$$

Das Impulsfunktional pt kann analog definiert werden, indem man die durch Verschiebungen der Position verursachten Veränderungen betrachtet:

$$\langle \chi | 1 | \psi \rangle_S - \langle \chi | 1 | \psi_\Delta \rangle_{S\Delta} = \frac{i\Delta}{\hbar} \langle \chi | p_k | \psi \rangle_S.$$

Der Staat $\psi_\Delta$ wird aus einer Region hergestellt $R'_\Delta$ was identisch mit der Region ist $R'$ außer dass er eine Strecke bewegt wird $\Delta$ im Weltraum. (Die Lagrange-Funktion, falls sie explizit von $x$, muss geändert werden zu $L_\Delta = L(\dot{x}, x - \Delta)$ für Zeiten vor $t$.) Man findet $^{21}$

$$p_k = \frac{\partial S(x_{k+1}, x_k)}{\partial x_{k+1}} = - \frac{\partial S(x_{k+1}, x_k)}{\partial x_k}. \tag{60}$$

$^{21}$Wir haben nicht sofort ausgetauscht $p_i$ von (60) in (47), da (47) dann sowohl für null Ordnung als auch für die erste Ordnung in nicht mehr gültig gewesen wäre $\epsilon$. Wir könnten die Kommutationsrelationen ableiten, aber nicht die Bewegungsgleichungen. Die beiden Ausdrücke in (60) stellen die Impulse an jedem Ende des Intervalls dar $t_i$, bis $t_{i+1}$. Sie unterscheiden sich durch $\epsilon V'(x_{k+1})$ wegen der während der Zeit wirkenden Kraft $\epsilon$

30

Da $\psi_\Delta(x, t)$ ist gleich $\psi(x - \Delta, t)$, die enge Verbindung zwischen $p_k$ und die $x$-Ableitung der Wellenfunktion festgelegt ist.

Drehimpulsoperatoren stehen analog zu Rotationen.

Die Ableitung bezüglich von $t_{i+1}$ von $S(x_{i+1}, t_{i+1}; x_i, t_i)$ erscheint in der Definition von $H_i$. Die Ableitung bezüglich von $t_{i+1}$ Definiert $p_i$. Aber die Ableitung bezüglich von $t_{i+1}$ von $S(x_{i+1}, t_{i+1}; x_i, t_i)$ mit der Ableitung bezüglich von $x_{i+1}$, für die Funktion $S(x_{i+1}, t_{i+1}; x_i, t_i)$ definiert durch (55) erfüllt die Hamilton-Jacobi-Gleichung. Somit ist die Hamilton-Jacobi-Gleichung eine Gleichung, die ausdrückt $H_i$, in Bezug auf die $p_i$. Mit anderen Worten, sie drückt die Tatsache aus, dass Zeitverschiebungen von Zuständen mit den Raumverschiebungen derselben Zustände zusammenhängen. Diese Idee führt direkt zu einer Herleitung der Schrödinger-Gleichung, die weitaus eleganter ist als die, die bei der Herleitung von Gleichung (30) gezeigt wird.

## 11. Unzulänglichkeiten der Formulierung

Die hier gegebene Formulierung leidet unter einem ernsthaften Nachteil. Die benötigten mathematischen Konzepte sind neu. Derzeit erfordert es eine unnatürliche und umständliche Unterteilung des Zeitintervalls, um die Bedeutung der Gleichungen klar zu machen. Durch die Verwendung der Notation und Konzepte der Mathematik der Funktionale können erhebliche Verbesserungen erzielt werden. Es wurde jedoch als am besten erachtet, dies bei der ersten Präsentation zu vermeiden. Man benötigt zusätzlich ein geeignetes Maß für den Raum der Argumentfunktionen $x(t)$ von den Funktionalen.$^{22}$

Es ist auch physisch unvollständig. Eine der wichtigsten Eigenschaften der Quantenmechanik ist ihre Invarianz unter unitären Transformationen. Diese entsprechen den kanonischen Transformationen der klassischen Mechanik. Natürlich kann die vorliegende Formulierung, äquivalent zu gewöhnlichen Formulierungen, mathematisch als invariant unter diesen Transformationen nachgewiesen werden. Allerdings wurde sie nicht so formuliert, dass sie es ist *Körperlich* offensichtlich, dass sie invariant ist. Diese Unvollständigkeit zeigt sich eindeutig. Es wurde kein direktes Verfahren beschrieben, um

$^{22}$Es gibt sehr interessante mathematische Probleme, die versuchen, Unterteilungs- und Limitierungsprozesse zu vermeiden. Eine Art komplexes Maß wird mit dem Raum der Funktionen assoziiert $x(t)$. Unter unerwarteten Umständen können endliche Ergebnisse erzielt werden, da das Maß nicht überall positiv ist, aber die Beiträge der meisten Pfade sich weitgehend aufheben. Diese kuriosen mathematischen Probleme werden durch den Unterteilungsprozess umgangen. Man fühlt sich jedoch, wie Cavalieri sich gefühlt haben muss, als er das Volumen einer Pyramide vor der Erfindung der Analysis berechnete.

31

Beschreiben Sie Messungen von Größen, die nicht nur Position sind. Messungen des Impulses, zum Beispiel eines einzelnen Teilchens, können durch Messungen der Positionen anderer Teilchen definiert werden. Das Ergebnis der Analyse einer solchen Situation zeigt jedoch den Zusammenhang zwischen Impulsmessungen und der Fourier-Transformation der Wellenfunktion. Dies ist jedoch eine ziemlich umständliche Methode, um ein so wichtiges physikalisches Ergebnis zu erhalten. Es ist zu erwarten, dass die Postulate verallgemeinert werden können, indem die Idee der "Pfade in einem Bereich der Raumzeit" ersetzt werden $R$" bis "Wege der Klasse" $R$", oder "Wege mit eigenem Eigentum $R$.” Aber welche Eigenschaften welchen physikalischen Messungen entsprechen, wurde nicht allgemein formuliert.

## 12. Eine Möglichkeitsverallgemeinerung

Die Formulierung deutet auf eine offensichtliche Verallgemeinerung hin. Es gibt interessante klassische Probleme, die ein Prinzip der kleinsten Wirkung erfüllen, für die die Wirkung jedoch nicht als Integral einer Funktion von Positionen und Geschwindigkeiten geschrieben werden kann. Die Aktion kann beispielsweise Beschleunigungen beinhalten. Oder, wiederum, wenn Wechselwirkungen nicht momentan sind, kann es das Produkt von Koordinaten zu zwei verschiedenen Zeitpunkten beinhalten, wie zum Beispiel $\int x(t)x(t+T)dt$. Die Aktion kann also nicht in eine Summe kleiner Beiträge wie in (10) aufgeteilt werden. Daher steht keine Wellenfunktion zur Verfügung, um einen Zustand zu beschreiben. Dennoch kann eine Übergangswahrscheinlichkeit definiert werden, um von einer Region zu erhalten $R'$ in einen anderen $R''$. Der Großteil der Theorie der Übergangselemente $\langle \chi_{t''}|F|\psi_{t'} \rangle_S$ kann übernommen werden. Man erfindet einfach ein Symbol, wie zum Beispiel $\langle R''|F|R' \rangle_S$ durch eine Gleichung wie (39), jedoch mit den Ausdrücken (19) und (20) für $\psi$ und $\chi$ ersetzte, und die allgemeinere Aktion ersetzte für $S$. Hamiltonoperator- und Impulsfunktionale können wie in Abschnitt (10) definiert werden. Weitere Details finden Sie in einer Dissertation des Autors.$^{23}$

## 13. Anwendung zur Beseitigung von Feldoszillatoren

Ein Merkmal der vorliegenden Formulierung ist, dass sie einem eine Art Vogelperspektive der Raum-Zeit-Beziehungen in einer gegebenen Situation geben kann. Vorher

$^{23}$Die von J. A. Wheeler und R. P. Feynman beschriebene Elektromagnetismus-Theorie, *Pfarrer Mod. Phys.* **17**, 157 (1945) kann in einem Prinzip der kleinsten Wirkung ausgedrückt werden, das nur die Koordinaten der Teilchen umfasst. Es war der Versuch, diese Theorie ohne Bezug auf die Felder zu quantisieren, der den Autor dazu veranlasste, die hier gegebene Formulierung der Quantenmechanik zu untersuchen. Die Erweiterung der Ideen auf den Fall allgemeinerer Aktionsfunktionen wurde in seiner Doktorarbeit "The principle of least action in the quantum mechanics" entwickelt, die 1942 an der Princeton University eingereicht wurde.

32

Die Integrationen auf der $x$, in einem Ausdruck wie (39) ausgeführt werden, hat man eine Art Format, in das verschiedene $F$ Funktionale können eingefügt werden. Man kann untersuchen, wie das, was im quantenmechanischen System zu verschiedenen Zeiten geschieht, miteinander zusammenhängt. Um diese vagen Bemerkungen etwas klarer zu machen, diskutieren wir ein Beispiel.

In der klassischen Elektrodynamik können die Felder, die beispielsweise die Wechselwirkung zweier Teilchen beschreiben, als eine Menge von Oszillatoren dargestellt werden. Die Bewegungsgleichungen dieser Oszillatoren können gelöst und die Oszillatoren im Wesentlichen eliminiert werden (Lienard- und Wiechert-Potentiale). Die daraus resultierenden Wechselwirkungen beinhalten Beziehungen der Bewegung eines Teilchens zu einem Zeitpunkt und des anderen Teilchens zu einem anderen Zeitpunkt. In der Quantenelektrodynamik wird das Feld erneut als eine Menge von Oszillatoren dargestellt. Aber die Bewegung der Oszillatoren kann nicht berechnet und die Oszillatoren eliminiert werden. Es stimmt, dass die Oszillatoren, die Längswellen repräsentieren, eliminiert werden können. Das Ergebnis ist eine sofortige elektrostatische Wechselwirkung. Die elektrostatische Eliminierung ist sehr lehrreich, da sie die Schwierigkeit der Selbstinteraktion sehr deutlich aufzeigt. Tatsächlich zeigt es das so deutlich, dass es keine Unklarheit bei der Entscheidung gibt, welcher Begriff falsch ist und weggelassen werden sollte. Dieser gesamte Prozess ist nicht relativistisch invariant, ebenso wenig wie der ausgelassene Term. Es scheint sehr wünschenswert zu sein, wenn auch die Oszillatoren, die transversale Wellen repräsentieren, eliminiert werden könnten. Dies stellt ein nahezu unüberwindbares Problem in der konventionellen Quantenmechanik dar. Wir erwarten, dass die Bewegung eines Teilchens $a$ zu einem Zeitpunkt hängt von der Bewegung von ab $b$ zu einem früheren Zeitpunkt, und *umgekehrt*. Eine Wellenfunktion $\psi(x_a, x_b; t)$, kann jedoch nur das Verhalten beider Teilchen gleichzeitig beschreiben. Es gibt keine Möglichkeit, den Überblick zu behalten, was $b$ hat es in der Vergangenheit gemacht, um das Verhalten von $a$. Die einzige Möglichkeit besteht darin, den Zustand der Oszillatormenge bei bei zu spezifizieren $t$, die dazu dienen, sich zu "erinnern", was $b$ (und $a$) gemacht hatte.

Die vorliegende Formulierung ermöglicht die Lösung der Bewegung aller Oszillatoren und deren vollständige Eliminierung aus den Gleichungen, die die Teilchen beschreiben. Das lässt sich leicht machen. Man muss lediglich die Bewegung der Oszillatoren auflösen, bevor man über die verschiedenen Variablen integriert $x_i$, für die Teilchen. Es ist die Integration über $x_i$, die versucht, die vergangene Geschichte in eine einzige Zustandsfunktion zu verdichten. Das wollen wir vermeiden. Natürlich hängt das Ergebnis von den Anfangs- und Endzuständen des Oszillators ab. Wenn sie spezifiziert sind, ist das Ergebnis eine Gleichung für $\langle \chi_{t'} | 1 | \psi_{t'} \rangle$ wie (38), aber enthalten als Faktor, außerdem $\exp(iS/\hbar)$ Eine weitere Funktion $G$ die nur von den Koordinaten abhängt, die die Pfade der Teilchen beschreiben.

Wir zeigen kurz, wie dies in einem sehr einfachen Fall gemacht wird. Angenommen, ein Teilchen, Koordinate $x(t)$, Lagrange-Operator $L(\dot{x}, x)$ wechselwirkt mit einem Oszillator,

33

Koordinate $g(t)$, Lagrange-Operator $\frac{1}{2}(\dot{q}^2 - \omega^2 q^2)$ durch einen Term $\gamma(x,t)q(t)$ im Lagrange-Operator für das System. Hier $\gamma(x,t)$ ist eine beliebige Funktion der Koordinate $x(t)$ des Teilchens und der Zeit. $^{24}$ Angenommen, wir wünschen uns die Wahrscheinlichkeit eines Übergangs von einem Zustand zum Zeitpunkt $t'$, wobei die Wellenfunktion des Teilchens lautet $\psi_{t'}$ und der Oszillator befindet sich im Energielevel $n$, auf einen Zustand bei $t''$ mit dem Teilchen in $\chi_{t''}$ und Oszillator im Level $m$. Dies ist das Quadrat von

$$\langle \chi_{t''} \varphi_m | 1 | \psi_{t'} \varphi_n \rangle_{S_p + S_0 + S_I} = \int \dots \int \varphi_m^*(q_i) \chi_{t''}^*(x_i)$$

$$\times \exp \frac{i}{\hbar} (S_p + S_0 + S_1) \psi_{t'}(x_0) \varphi_n(q_0) \cdot \frac{dx_0}{A} \frac{dq_0}{a} \dots \frac{dx_{j-1}}{A} \frac{dq_{j-1}}{a} dx_i dq_i. \tag{61}$$

Hier $\varphi_n(9q)$ ist die Wellenfunktion für den Oszillator im Zustand $n$, $S_p$ ist die Wirkung

$$\sum_{i=0}^{j-1} S_p(x_{i+1}, x_i)$$

berechnet für das Teilchen, als wäre der Oszillator abwesend,

$$S_0 = \sum_{i=0}^{j-1} \left[ \frac{\epsilon}{2} \left( \frac{q_{i+1} - q_i}{\epsilon} \right)^2 - \frac{\epsilon \omega^2}{2} q_{i+1}^2 \right]$$

die des Oszillators allein, und

$$S_I = \sum_{i=0}^{j-1} \gamma_i q_i$$

(wobei $\gamma_i = \gamma(x_i, t_i)$) ist die Wirkung der Wechselwirkung zwischen Teilchen und Oszillator. Die Normalisierungskonstante, $a$, für den Oszillator ist $(2\pi\epsilon i / \hbar)^{-1/2}$. Nun hängt die Exponentialstufe quadratisch von allen den $q_i$. Daher die Integrationen über alle Variablen $q_i$, für $0 < i < j$ kann leicht ausgeführt werden. Die eine ist die Integration einer Folge von Gaußschen Integralen.

Das Ergebnis dieser Integrationen ist, dass das Schreiben $T = t'' - t'$, $(2\pi i \hbar \sin \omega T / \omega)^{-1/2} \exp i (S_p + Q(q_i, q_0)) / \hbar$, wobei $Q(q_j, q_0)$ go) entpuppt sich als einfach das klassische

$^{24}$Die Verallgemeinerung auf den Fall, dass $\gamma$ hängt von der Geschwindigkeit ab, $\dot{x}$, des Teilchens stellt kein Problem dar.

34

Wirkung für den erzwungenen harmonischen Oszillator (siehe Referenz 15). Ausdrücklich ist es das

$$\begin{array}{l} Q(q_{j},q_{0})=\frac{\omega}{2\sin\omega T}\left[(\cos\omega T)(q_{j}^{2}+q_{0}^{2})-2q_{j}q_{0}\right. \\ +\frac{2q_{0}}{\omega}\int_{t'}^{t''}\gamma(t)\sin\omega(t-t')dt+\frac{2q_{j}}{\omega}\int_{t'}^{t''}\gamma(t)\sin\omega(t''-t)dt \\ \left.-\frac{2}{\omega^{2}}\int_{t'}^{t''}\int_{t'}^{t}\gamma(t)\gamma(s)\sin\omega(t''-t)\times\sin\omega(s-t')dsdt\right]. \end{array}$$

Es wurde so geschrieben, als ob $\gamma(t)$ waren eine kontinuierliche Funktion der Zeit. Die Integrale sollten wirklich in Riemannsche Summen und die Größe aufgeteilt werden $\gamma(x_{i},t_{i})$ Ersatz für $\gamma(t_{i})$. Somit gilt: $Q$ hängt von den Koordinaten des Teilchens zu jeder Zeit durch die $\gamma(x_{i},t_{i})$ und zeitweise auf dem des Oszillators $t'$ und $t''$ Nur. Somit wird die Größe (61)

$$\begin{array}{l} \langle\chi_{t''}\varphi_{m}|1|\psi_{t'}\varphi_{n}\rangle_{Sp+S_{0}+S_{j}}=\int\dots\int\chi_{t''}^{*}(x_{i})G_{mn}\times \\ \times\exp\left(\frac{iS_{p}}{\hbar}\right)\psi_{t'}(x_{0})\frac{dx_{0}}{A}\dots\frac{dx_{j-1}}{A}dx_{i}=\langle\chi_{t''}|G_{mn}|\psi_{t'}\rangle_{S_{p}} \end{array}$$

die nun nur noch die Koordinaten des Teilchens enthält, also die Größe $G_{mn}$ gegeben durch

$$G_{mn}=(2\pi i\hbar\sin\omega T/\omega)^{-1/2}\int\int\varphi_{m}^{*}(q_{i})\times\exp(iQ(q_{i},q_{0})/\hbar)\varphi_{n}(q_{0})dq_{j}dq_{0}.$$

Geht man analog vor, stellt man fest, dass alle Oszillatoren des elektromagnetischen Feldes aus einer Beschreibung der Bewegung der Ladungen eliminiert werden können.

## Statistische Mechanik

### Spin und Relativität

Probleme in der Messtheorie und statistischen Quantenmechanik werden oft vereinfachet, wenn sie aus der hier beschriebenen Perspektive dargestellt werden. Zum Beispiel kann der Einfluss eines störenden Messinstruments prinzipiell ausgegliedert werden, so wie wir es im Detail beim Oszillator getan haben. Die statistische Dichtematrix hat eine ziemlich offensichtliche und nützliche Verallgemeinerung. Sie ergibt sich, wenn man das Quadrat von (38) betrachtet. Es handelt sich um einen Ausdruck ähnlich wie (38), der jedoch Integrationen über zwei Variablenmengen enthält $dx_{i}$, und $dx_{i}'$. Der Exponentialwert

35

wird ersetzt durch $\exp i(S - S')/\hbar$, wobei $S'$ ist dieselbe Funktion von $x_i'$ als $S$ ist von $x_i$. Es ist beispielsweise erforderlich, das Ergebnis der Eliminierung der Feldoszillatoren zu beschreiben, bei dem zum Beispiel der Endzustand der Oszillatoren nicht spezifiziert ist und man nur die Summe aller Endzustände möchte $m$.

Spin kann formell enthalten sein. Die Pauli-Spingleichung kann auf folgende Weise erhalten werden: Man ersetzt den Vektorpotential-Wechselwirkungsterm in $S(x_{i+1}, x_i)$,

$$\frac{e}{2c}(\mathbf{x}_{i+1} - \mathbf{x}_i) \cdot \mathbf{A}(\mathbf{x}_i) + \frac{e}{2c}(\mathbf{x}_{i+1} - \mathbf{x}_i) \cdot \mathbf{A}(\mathbf{x}_{i+1})$$

aus dem Ausdruck (13) durch den Ausdruck

$$\frac{e}{2c}(\sigma \cdot (\mathbf{x}_{i+1} - \mathbf{x}_i))(\sigma \cdot \mathbf{A}(\mathbf{x}_i)) + \frac{e}{2c}(\sigma \cdot \mathbf{A}(\mathbf{x}_{i+1}))(\sigma \cdot (\mathbf{x}_{i+1} - \mathbf{x}_i)).$$

Hier $\mathbf{A}$ ist das Vektorpotential, $\mathbf{x}_{i+1}$ und $\mathbf{x}$, die Vektorpositionen eines Teilchens zu Zeiten $t_{i+1}$ und $t_i$, und $\sigma$ Paulis Spinvektormatrix ist. Die Menge $\Phi$ muss nun ausgedrückt werden als $\Pi_i \exp i S(x_{i+1}, x_i)/\hbar$ denn dies unterscheidet sich vom Exponentialwert der Summe von $S(x_{i+1}, x_i)$. Somit gilt: $\Phi$ ist nun eine Spinmatrix.

Die Klein-Gordon-relativistische Gleichung kann auch formell durch das Hinzufügen einer vierten Koordinate zur Bestimmung eines Pfades gewonnen werden. Man betrachtet einen "Pfad" als durch vier Funktionen bestimmt $x^{(\mu)}(\tau)$ von einem Parameter $\tau$. Der Parameter $\tau$ Jetzt geht es in Schritten $\epsilon$ als die Variable $t$ War vorher dran. Die Größen $x^{(1)}(t), x^{(2)}(t), x^{(3)}(t)$ sind die Raumkoordinaten eines Teilchens und $x^{(4)}(t)$ ist eine entsprechende Zeit. Die verwendete Lagrangefunktion ist

$$\sum_{\mu=1}^{t} [(dx^\mu/d\tau)^2 + (e/c)(dx^\mu/d\tau)\mathbf{A}_\mu],$$

wobei $A_\mu$ ist das 4-Vektor-Potential und die Terme in der Summe für $\mu = 1, 2, 3$ werden mit umgekehrtem Zeichen verzeichnet. Wenn man eine Wellenfunktion sucht, die von $\tau$ periodisch kann gezeigt werden, dass dies die Klein-Gordon-Gleichung erfüllen muss. Die Dirac-Gleichung resultiert aus einer Modifikation der für die Klein-Gordon-Gleichung verwendeten Lagrange-Funktion, die analog zur Modifikation der für die Pauli-Gleichung erforderlichen nichtrelativistischen Lagrange-Dichtung ist. Direkt daraus resultiert das Quadrat des üblichen Dirac-Operators.

Diese Ergebnisse für Spin und Relativität sind rein formal und tragen nichts zum Verständnis dieser Gleichungen bei. Es gibt weitere Möglichkeiten, die Dirac-Gleichung zu erhalten, die ein gewisses Potenzial bieten, eine klarere physikalische Interpretation dieser wichtigen und schönen Gleichung zu geben.

Der Autor dankt aufrichtig für den hilfreichen Rat von Professor und Frau H. C. Corben sowie Professor H. A. Bethe. Er möchte Professor J. A. Wheeler für viele Diskussionen in den frühen Phasen der Arbeit danken.

36
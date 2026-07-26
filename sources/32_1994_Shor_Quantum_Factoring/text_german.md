# Algorithmen für Quantenberechnung: Diskrete Logarithmen und Faktorisierung

Peter W. Shor

AT&T Bell Labs

Raum 2D-149

600 Mountain Ave.

Murray Hill, NJ 07974, USA

## Zusammenfassung

Ein Computer wird allgemein als universelles Rechengerät betrachtet; d. h. es wird angenommen, dass es in der lage ist, jedes physikalische rechnergerät mit einem Rechenzeitaufwand von höchstens einem Polynomfaktor zu simulieren. Es ist nicht klar, ob dies unter Berücksichtigung der Quantenmechanik noch gilt. Mehrere Forscher, beginnend mit David Deutsch, haben Modelle für quantenmechanische Computer entwickelt und deren rechnerische Eigenschaften untersucht. Dieses Paper stellt Las Vegas Algorithmen vor, um diskrete Logarithmen zu finden und ganze Zahlen auf einem Quantencomputer zu faktorisieren, die eine Anzahl von Schritten durchführen, die polynomiell in der Eingabegröße sind, z. B. die Anzahl der Ziffern der zu faktorisierenden Ganzzahl. Diese beiden Probleme gelten im Allgemeinen als schwierig auf einem klassischen Computer und dienen als Grundlage mehrerer vorgeschlagener Kryptosysteme. (Wir geben somit die ersten Beispiele der Quantenkryptoanalyse.)

## 1 Einführung

Seit der Entdeckung der Quantenmechanik empfinden Menschen das Verhalten der Wahrscheinlichkeitsgesetze in der Quantenmechanik als kontraintuitiv. Aufgrund dieses Verhaltens verhalten sich quantenmechanische Phänomene ganz anders als die Phänomene der klassischen Physik, an die wir gewöhnt sind. Feynman scheint der Erste gewesen zu sein, der gefragt hat, welche Auswirkungen das auf die Berechnung hat [13, 14]. Er argumentierte, warum dieses Verhalten es rechnerisch aufwendig machen könnte, die Quantenmechanik auf einem klassischen (oder von Neumann-) Computer zu simulieren. Er schlug auch die Möglichkeit vor, einen Computer auf Basis quantenmechanischer Prinzipien zu verwenden, um dieses Problem zu vermeiden, und stellte damit implizit die umgekehrte Frage: Kann man durch die Verwendung der Quantenmechanik in einem Computer effizienter rechnen als auf einem klassischen Computer? Weitere frühe Arbeiten im Bereich der Quantenmechanik und -informatik wurden von Benioff durchgeführt

[1, 2]. Obwohl er nicht fragte, ob die Quantenmechanik der Berechnung zusätzliche Macht verleihe, zeigte er, dass eine Turingmaschine durch die reversible unitäre Entwicklung eines Quantenprozesses simuliert werden kann, was eine notwendige Voraussetzung für die Quantenberechnung ist. Deutsch [9, 10] war der erste, der ein explizites Modell der Quantenberechnung lieferte. Er definierte sowohl Quanten-Turingmaschinen als auch Quantenschaltungen und untersuchte einige ihrer Eigenschaften.

Der nächste Teil dieses Artikels behandelt, wie Quantenberechnungen mit klassischen Komplexitätsklassen zusammenhängen. Wir geben daher zunächst eine kurze, intuitive Diskussion der Komplexitätsklassen für diejenigen Leser, die diesen Hintergrund nicht haben. Im Allgemeinen gibt es zwei Ressourcen, die die Fähigkeit von Computern zur Lösung großer Probleme einschränken: Zeit und Speicher (d. h. Speicher). Das Analysegebiet der Algorithmen betrachtet die asymptotischen Anforderungen, die Algorithmen für diese Ressourcen stellen, als Funktion der Problemgröße. Theoretische Informatiker klassifizieren Algorithmen im Allgemeinen als effizient, wenn die Anzahl der Schritte der Algorithmen als Polynom in der Größe der Eingabe wächst. Die Klasse von Problemen, die durch effiziente Algorithmen gelöst werden können, ist als P bekannt. Diese Klassifikation hat mehrere schöne Eigenschaften. Zum einen spiegelt er in der Praxis die Leistung von Algorithmen in der Praxis einigermaßen wider (obwohl ein Algorithmus, dessen Laufzeit beispielsweise die Zehntel-Potenz der Eingabegröße ist, nicht wirklich effizient ist). Zum anderen ist diese Klassifikation theoretisch schön, da verschiedene vernünftige Maschinenmodelle dieselbe Klasse P erzeugen. Dieses Verhalten werden wir in der Quantenberechnung wieder sehen, wo verschiedene Modelle für Quantenmaschinen in der Laufzeit um nicht mehr als polynomielle Faktoren variieren.

Es gibt auch andere Klassen der rechnerischen Komplexität, die in diesem Artikel behandelt werden. Eines davon ist PSPACE, das sind Probleme, die mit einer Menge Speicherpolynoms in der Eingabegröße gelöst werden können. Eine weitere wichtige Komplexitätsklasse ist NP, die intuitiv die Klasse der exponentiellen Suchprobleme ist. Dies sind Probleme, die möglicherweise die Suche in einem exponentiellen Größenraum erfordern, um sie zu finden

0272-5428/94 $04,00 © 1994 IEEE

124

die Lösung, für die jedoch die Lösung, einmal gefunden, in polynomieller Zeit verifiziert werden kann (möglicherweise mit einer polynomiellen Menge zusätzlicher unterstützender Beweise). Wir werden außerdem zwei weitere traditionelle Komplexitätsklassen besprechen. Eines davon sind BPP, das sind Probleme, die mit hoher Wahrscheinlichkeit in polynomieller Zeit gelöst werden können, wenn man auf einen Zufallszahlengenerator zugreifen kann. Das andere ist P#P, das sind jene Probleme, die in polynomialer Zeit gelöst werden könnten, wenn Summen von exponentiell vielen Termen effizient berechnet werden könnten (wobei diese Summen die Anforderung erfüllen müssen, dass jeder Term in polynomieller Zeit berechenbar ist). Diese Klassen sind wie folgt miteinander verbunden:

$$\mathrm{P} \subseteq \mathrm{BPP}, \mathrm{NP} \subseteq \mathrm{P}^{\# \mathrm{P}} \subseteq \mathrm{PSPACE}.$$

Die Beziehung zwischen BPP und NP ist nicht bekannt.

Die Frage, ob die Nutzung der Quantenmechanik in einem Computer mehr Rechenleistung ermöglicht, ist bisher nicht zufriedenstellend beantwortet worden. Diese Frage wurde in [11, 6, 7], aber es wurde nicht gezeigt, wie man ein Problem in quantenpolynomischer Zeit löst, das in BPP (der Klasse von Problemen, die in polynomieller Zeit mit beschränkter Fehlerwahrscheinlichkeit gelöst werden können) nicht als lösbar bekannt war. Jüngste Arbeiten zu diesem Problem wurden durch Bernsteins und Vaziranis Artikel angeregt [5] die die Grundlagen für die Quantenberechnungstheorie der Berechnungskomplexität legte. Eines der in dieser Arbeit enthaltenen Ergebnisse war ein Orakelproblem (ein Problem mit einer "Black-Box"-Subroutine), das in polynomieller Zeit auf einer quantenmechanischen Turingmaschine gelöst werden kann und auf einem klassischen Computer superpolynomiale Zeit benötigt. Dies war der erste Hinweis, abgesehen davon, dass niemand wusste, wie man einen Quantencomputer auf einem klassischen Computer ohne exponentielle Verlangsamung simuliert, dass Quantenberechnung eine größere als polynomielle Beschleunigung gegenüber klassischer Berechnung mit einem Zufallszahlengenerator erzielen könnte. Dieses Ergebnis wurde von Simon verbessert [28], der eine viel einfachere Konstruktion eines Orakelproblems gab, das auf einem Quantencomputer polynomielle Zeit benötigt und auf einem klassischen Computer exponentielle Zeit benötigt. Tatsächlich wird dieses Ergebnis, wenn man Simons Orakel als Unterprogramm betrachtet, zu einem Versprechensproblem, das auf einem Quantencomputer polynomiale Zeit benötigt und auf einem klassischen Computer sehr schwierig aussieht. Der in dieser Arbeit gegebene Algorithmus für den "einfachen Fall" des diskreten Logarithos ist direkt analog zu Simons Algorithmus, wobei die Gruppe Z5^5 durch die Gruppe Zp-1 ersetzt wird; Ich konnte diesen Algorithmus erst entdecken, nachdem ich Simons Artikel gesehen hatte.

In einem weiteren Ergebnis in Bernsteins und Vaziranis Arbeit wurde eine bestimmte Klasse von Quanten-Turingmaschinen streng definiert und eine universelle Quanten-Turingmaschine gegeben, die jede andere Quanten-Turingmaschine dieser Klasse simulieren konnte. Leider war nicht klar, ob diese

Quanten-Turingmaschinen konnten andere Klassen von Quanten-Turingmaschinen simulieren, daher war dieses Ergebnis nicht ganz zufriedenstellend. Yao [32] hat die Situation behoben, indem gezeigt wurde, dass Quanten-Turingmaschinen uniforme Familien polynomieller Quantenschaltkreise simulieren und von ihnen simuliert werden können, mit höchstens polynomieller Verlangsamung. Er hat Quanten-Turingmaschinen mit k Köpfen weiter definiert und gezeigt, dass diese Maschinen mit einer Verlangsamung von einem Faktor 2^k simuliert werden können. Dies scheint zu zeigen, dass die Klasse von Problemen, die in polynomieller Zeit auf einer dieser Maschinen gelöst werden können, möglicherweise mit beschränkter Wahrscheinlichkeit ε < 1/3 von Fehler, ist relativ robust. Diese Klasse wird analog zur klassischen Komplexitätsklasse BPP BQP genannt, also jene Probleme, die mit beschränkter Fehlerwahrscheinlichkeit auf einer probabilistischen Turingmaschine gelöst werden können. Diese Klasse BQP könnte als die Klasse von Problemen betrachtet werden, die auf einer Quanten-Turingmaschine effizient lösbar sind.

Da BQP P#P ⊆ PSPACE ⊆ [5], würde jeder nicht-relativisierte Beweis, dass BQP streng größer als BPP ist, das strukturelle Komplexitätsergebnis BPP ⊊ PSPACE implizieren, das noch nicht bewiesen ist. Angesichts dieser Schwierigkeit fallen mir mehrere Ansätze ein; eine davon zeigt, dass BQP ⊆ BPP zu einem Zusammenbruch klassischer Komplexitätsklassen führen würden, die als unterschiedlich gelten. Ein zweiter Ansatz besteht darin, Ergebnisse relativ zu einem Orakel zu beweisen. In Bennett et al. [4] es wird gezeigt, dass es relativ zu einem zufälligen Orakel nicht der Fall ist, dass NP BQP ⊆. Dieser Beweis legt tatsächlich nahe, dass ein Quantencomputer Einwegfunktionen nicht invertieren kann, sondern nur für Einweg-Orakel, also sogenannte "Blackbox"-Funktionen, die als Unterprogramm gegeben sind und in die der Quantencomputer nicht hineinschauen darf. Solche Orakelergebnisse waren in der Vergangenheit irreführend, insbesondere im Fall von IP = PSPACE [15, 27]. Ein dritter Ansatz, den wir verfolgen, besteht darin, in BQP ein gut untersuchtes Problem zu lösen, für das kein polynomieller Zeitalgorithmus bekannt ist. Dies zeigt, dass die zusätzliche Leistung, die durch Quanteninterferenz verliehen wird, zumindest schwer mit klassischer Berechnung zu erreichen ist. Sowohl Bernstein als auch Vazirani [5] und Simon [28] außerdem gab es polynomielle Zeitalgorithmen für Probleme, die in BPP nicht bekannt waren, aber diese Probleme wurden speziell für diesen Zweck erfunden, obwohl Simons Problem nicht konstruiert wirkt und durchaus nützlich sein könnte.

Diskrete Logarithmen und ganzzahlige Faktorisierung sind zwei Zahlentheorie-Probleme, die ausführlich untersucht wurden, für die jedoch keine polynomiellen Zeitalgorithmen bekannt sind [16, 19, 20, 25]. Tatsächlich gelten diese Probleme so weithin als schwierig, dass Kryptosysteme aufgrund ihrer Härte vorgeschlagen wurden, und das RSA-Public-Key-Kryptosystem [26], basierend auf der Härte des Faktorisierens, wird verwendet. Wir zeigen, dass diese Probleme in BQP gelöst werden können.

Derzeit weiß niemand, wie man einen Quantencomputer baut, obwohl es so scheint, als könnte es möglich sein

125

innerhalb der Gesetze der Quantenmechanik. Es wurden einige Vorschläge zu möglichen Entwürfen für solche Computer gemacht [29, 21, 22, 12], aber es wird erhebliche Schwierigkeiten geben, eines dieser Modelle zu bauen [18, 31]. Selbst wenn es möglich wäre, kleine Quantencomputer zu bauen, könnte die Skalierung auf Maschinen, die groß genug sind, um interessante Berechnungen durchzuführen, grundlegende Schwierigkeiten darstellen. Es wird gehofft, dass dieses Papier die Forschung dazu anregen wird, ob es tatsächlich machbar ist, einen Quantencomputer zu bauen.

Auch wenn nie ein Quantencomputer gebaut wird, beleuchtet diese Forschung das Problem, die Quantenmechanik auf einem klassischen Computer zu simulieren. Jede Methode, dies für einen beliebigen Hamiltonoperator zu tun, könnte zwangsläufig einen Quantencomputer simulieren. Daher würde jede allgemeine Methode zur Simulation der Quantenmechanik mit höchstens einer polynomiellen Verlangsamung zu einem polynomiellen Faktorisierungsalgorithmus führen.

## 2 Quantenberechnung

In diesem Abschnitt geben wir eine kurze Einführung in die Quantenberechnung und betonen die Eigenschaften, die wir verwenden werden. Für eine umfassendere Übersicht verweise ich den Leser auf Simons Aufsatz in diesem Bericht [28] oder frühere Arbeiten zur quantenmechanischen Berechnungskomplexitätstheorie [5, 32].

In der Quantenphysik verhält sich ein Experiment so, als würde es alle möglichen Pfade gleichzeitig durchlaufen. Jeder dieser Wege hat eine komplexe Wahrscheinlichkeitsamplitude, die durch die Physik des Experiments bestimmt wird. Die Wahrscheinlichkeit eines bestimmten Ergebnisses des Experiments ist proportional zum Quadrat des Absolutwerts der Summe der Amplituden aller zu diesem Ergebnis führenden Wege. Um über eine Menge von Pfaden zu summieren, müssen die Ergebnisse in jeder Hinsicht identisch sein, d. h. das Universum muss sich im gleichen Zustand befinden. Ein Quantencomputer verhält sich ähnlich. Die Berechnung läuft alle möglichen Pfade gleichzeitig ab, und jeder Pfad ist mit einer komplexen Amplitude verbunden. Um die Wahrscheinlichkeit eines beliebigen Endzustands der Maschine zu bestimmen, addieren wir die Amplituden aller Pfade, die diesen Endzustand erreichen, und quadrieren dann den Absolutwert dieser Summe.

Eine äquivalente Sichtweise auf diesen Prozess besteht darin, sich vorzustellen, dass die Maschine in jedem Schritt der Berechnung in einer Überlagerung von Zuständen ist. Wir werden diese Überlagerung der Zustände als folgt darstellen:

$$\sum_{i} a_{i} |S_{i}\rangle, \tag{2.1}$$

wobei die Amplituden $a_{i}$ komplexe Zahlen sind, so dass $\sum_{i} |a_{i}|^{2} = 1$ und jeder $|S_{i}\rangle$ ist ein Basiszustand der Maschine; In einer Quanten-Turingmaschine wird ein Basiszustand durch das, was auf dem Band geschrieben wird, sowie durch die Position und den Zustand des Kopfes definiert. In einer Quantenschaltung wird ein Basiszustand definiert durch

die Werte der Signale auf allen Drähten auf einer bestimmten Ebene des Stromkreises. Wenn die Maschine in einem bestimmten Schritt untersucht wird, ist die Wahrscheinlichkeit, die Basis zu sehen, der Zustand $|S_{i}\rangle$ ist $|a_{i}|^{2}$; nach dem Heisenbergschen Unschärfeprinzip wird jedoch das Betrachten der Maschine während der Berechnung den Rest der Berechnung stören.

Die Gesetze der Quantenmechanik erlauben nur unitäre Transformationen des Zustands. Eine unitäre Matrix ist eine, deren konjugierte Transponierte gleich ihrem Inversen ist, und wenn Zustandstransformationen durch unitäre Matrizen dargestellt werden, wird sichergestellt, dass die Wahrscheinlichkeit, alle möglichen Ergebnisse zu erhalten, zu eins summiert. Darüber hinaus erlauben die Definitionen von Quanten-Turingmaschine und Quantenschaltung nur lokale unitäre Transformationen, also unitäre Transformationen auf einer festen Bitzahl.

Vielleicht ist ein Beispiel an dieser Stelle informativ. Angenommen, unsere Maschine befindet sich in der Überlagerung von Zuständen

$$\frac{1}{\sqrt{2}} |000\rangle + \frac{1}{2} |100\rangle - \frac{1}{2} |110\rangle \tag{2.2}$$

und wir wenden die unitäre Transformation an

$$\begin{array}{c|cccc} & 00 & 01 & 10 & 11 \\ 00 & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ 01 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\ 10 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ 11 & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \end{array} \tag{2.3}$$

auf die letzten beiden Teile unseres Bundesstaates. Das heißt, wir multiplizieren die letzten beiden Bits der Komponenten des Vektors (2,2) mit der Matrix (2,3). Die Maschine wechselt dann zur Superposition der Zustände

$$\frac{1}{2\sqrt{2}} (|000\rangle + |001\rangle + |010\rangle + |011\rangle) + \frac{1}{2} |101\rangle + \frac{1}{2} |111\rangle. \tag{2.4}$$

Beachten Sie, dass das Ergebnis anders gewesen wäre, wenn wir mit der Superposition der Zustände begonnen hätten

$$\frac{1}{\sqrt{2}} |000\rangle + \frac{1}{2} |100\rangle + \frac{1}{2} |110\rangle, \tag{2.5}$$

die die gleiche Wahrscheinlichkeit hat, sich in einer bestimmten Konfiguration zu befinden, wenn sie beobachtet wird.

Wir geben nun bestimmte Eigenschaften der Quantenberechnung an, die nützlich sein werden. Diese Fakten sind aus der Definition von Quanten-Turingmaschine oder Quantenschaltung nicht sofort ersichtlich und sind sehr nützlich für die Entwicklung von Algorithmen für Quantenmaschinen.

Tatsache 1: Eine deterministische Berechnung ist genau dann auf einem Quantencomputer ausführbar, wenn sie reversibel ist. Aus Ergebnissen zur reversiblen Berechnung [3, 30], wir können jede polynomielle Zeitfunktion berechnen $f(a)$ solange wir die Eingabe behalten, $a$, auf dem Anrufbeantworter. An

126

Löschen $a$ und es durch ersetzen $f(a)$ Wir brauchen zusätzlich, dass $f$ ist eins zu eins und das $a$ ist in polynomieller Zeit berechenbar aus $f(a)$; d.h. dass beides $f$ und $f^{-1}$ sind polynomiell berechenbar.

Fakt 2: Jede unitäre Matrix der Polynomgröße kann mit einer polynomiellen Anzahl elementarer unitärer Transformationen angenähert werden [10, 5, 32] und kann daher in polynomieller Zeit auf einem Quantencomputer angenähert werden. Darüber hinaus ist diese Näherung ausreichend, um höchstens eine beschränkte Fehlerwahrscheinlichkeit in die Ergebnisse der Berechnung einzuführen.

### 3 Unitarische Umwandlungen des Gebäudes

Da sich die Quantenberechnung mit unitären Transformationen beschäftigt, ist es hilfreich, bestimmte nützliche unitäre Transformationen erstellen zu können. In diesem Abschnitt stellen wir einige Techniken zur Konstruktion unitärer Transformationen auf Quantenmaschinen vor, was dazu führt, dass wir zeigen, wie man eine bestimmte unitäre Transformation in polynomieller Zeit konstruiert. Diese Transformationen werden in der Regel als Matrizen angegeben, wobei sowohl Zeilen als auch Spalten nach Zuständen indiziert sind. Diese Zustände entsprechen Darstellungen von ganzen Zahlen auf dem Computer; insbesondere werden die Zeilen und Spalten beginnend mit 0 indiziert, sofern nichts anderes angegeben ist.

Ein Werkzeug, das wir in dieser Arbeit wiederholt verwenden werden, ist die folgende unitäre Transformation, deren Summe eine Fourier-Transformation ergibt. Betrachten wir eine Zahl $a$ mit $0 \le a < q$ für einige $q$ wobei die Anzahl der Bits von $q$ polynomiell ist. Wir führen die Transformation durch, die den Zustand annimmt $|a\rangle$ An den Staat

$$\frac{1}{q^{1/2}} \sum_{b=0}^{q-1} |b\rangle \exp(2\pi i ab/q). \tag{3.1}$$

Das heißt, wir wenden die unitäre Matrix an, deren $(a, b)$'Der Eintrag ist $\frac{1}{q^{1/2}} \exp(2\pi i ab/q)$. Diese Transformation steht im Zentrum unserer Algorithmen, und wir nennen diese Matrix $A_q$. Da wir verwenden werden $A_q$ für $q$ von exponentialer Größe müssen wir zeigen, wie diese Transformation in polynomieller Zeit durchgeführt werden kann. Tatsächlich können wir das nur für glatte Zahlen tun $q$, das heißt, solche mit kleinen Primfaktoren. In diesem Artikel werden wir uns mit glatten Zahlen beschäftigen $q$ die keinen Primpotenzfaktor enthalten, der größer als ist $(\log q)^c$ für einige fest $c$. Es ist auch möglich, diese Transformation in polynomialer Zeit für alle glatten Zahlen durchzuführen $q$; Coppersmith zeigt, wie man das für $q = 2^k$ wobei im Wesentlichen die schnelle Fourier-Transformation verwendet wird, was die Anzahl der Operationen zur Faktorisierung erheblich reduziert [8].

Wenn wir eine Faktorisierung kennen $q = q_1 q_2 q_3 \cdots q_k$ wobei $\gcd(q_1, q_2) = 1$ und wobei $k$ und alle $q_i$ polynomiale Größe haben, zeigen wir, wie die Transformation gebaut wird

$A_q$ in polynomieller Zeit, indem die Komposition des $A_{q_i}$. Dafür benötigen wir zunächst ein Lemma zur Quantenberechnung.

Lemma 3.1 Angenommen, die Matrix $B$ ist eine Blockdiagonale $mn \times mn$ Unitäre Matrix, bestehend aus $n$ identische Einheitsstraße $m \times m$ Matrizen $B'$ entlang der Diagonale und überall sonst 0er. Angenommen weiter, dass die Zustandstransformation $B'$ kann rechtzeitig erledigt werden $T(B')$ auf einer Quanten-Turingmaschine. Dann die Matrix $B$ Kann gemacht werden in $T(B') + (\log mn)^c$ Zeit auf einer quantenmechanischen Turingmaschine, wobei $c$ ist eine Konstante.

Wir nennen diese Matrix $B$ Die direkte Summe von $n$ Kopien von $B'$ und verwenden Sie die Notation $B = \bigoplus_n B'$. Diese Matrix $B$ ist das Tensorprodukt von $B'$ und $I_n$, wobei $I_n$ ist die $n \times n$ Identitätsmatrix.

Beweis: Angenommen, wir haben eine Zahl $a$ auf unserem Band. Wir können reversibel berechnen $\alpha_1$ und $\alpha_2$ von $a$ wobei $a = m\alpha_1 + \alpha_2$. Diese Berechnung löscht $a$ von unserem Band und ersetzt es durch $\alpha_1$ und $\alpha_2$. Jetzt $\alpha_1$ Tells in welchem Block die Reihe $a$ enthalten ist, und $\alpha_2$ gibt an, welche Zeile der Matrix innerhalb dieses Blocks die Zeile ist $a$. Dann können wir uns bewerben $B'$ zu $\alpha_2$ um zu erhalten $\beta_2$ (Löschen $\alpha_2$ im Prozess). Nun kombinieren wir $\alpha_1$ und $\beta_2$ um zu erhalten $b = m\alpha_1 + \beta_2$ ergibt das Ergebnis von $B$ Angewandt auf $a$ (mit der richtigen Amplitude). Die Berechnung von $B'$ Takes $T(B')$ und der Rest der Berechnung ist polynomiell in $\log m + \log n$.

Wir zeigen nun, wie man erhält $A_q$ für glatt $q$. Wir werden verwesen $A_q$ in ein Produkt einer polynomiellen Anzahl unitärer Transformationen, die alle in polynomieller Zeit ausgeführt werden können; Das ermöglicht uns, zu konstruieren $A_q$ in polynomialer Zeit. Angenommen, wir haben $q = q_1 q_2$ mit $\gcd(q_1, q_2) = 1$. Was wir tun werden, ist zu vertreten $A_q = CD$, wobei durch Umordnung der Zeilen und Spalten von $D$ erhalten wir $\bigoplus_{q_1} A_{q_1}$ und die Reihen und Spalten von $C$ erhalten wir $\bigoplus_{q_2} A_{q_2}$. Solange diese Umordnungen der Zeilen und Spalten von $C$ und $D$ in polynomieller Zeit ausführbar sind (d. h. gegebene Zeile $r$, wir können in polynomieller Zeit die Zeile finden $r'$ auf die es genommen wird) und die inversen Operationen ebenfalls in polynomieller Zeit ausführbar sind, können wir durch Verwendung des obigen Lemmats und der Rekursion eine polynomielle Methode erhalten, um auszuführen $A_q$ auf einem Quantencomputer.

Wir müssen jetzt definieren $C$ und $D$ Und überprüfe das. $A_q = CD$. Zur Definition $C$ und $D$ Wir brauchen einige vorläufige Definitionen. Erinnern Sie sich, dass $q = q_1 q_2$ mit $q_1$ und $q_2$ relativ erstklassig. Lass $\omega = \exp(2\pi i/q)$. Lass $u$ sei die Zahl (mod $q$) so dass $u \equiv 0 \pmod{q_1}$ und $u \equiv -1 \pmod{q_2}$. Eine solche Zahl existiert nach dem chinesischen Restsatz und kann in polynomieller Zeit berechnet werden. Wir werden Zeilen- und Spaltenindizes zerlegen $a$, $b$ und $c$ Wie folgt: $a = \alpha_1 q_2 + \alpha_2$, $b = \beta_1 q_1 + \beta_2$, und $c = \gamma_1 q_1 + \gamma_2$. Beachten Sie die Asymmetrie in den Definitionen von $a$, $b$ und $c$.

127

Wir können nun definieren $C$ und $D$:

$$C(a, b) = \left\{ \begin{array}{cl} 0 & \text{if } \alpha_2 \neq \beta_1 \\ \frac{1}{q_1^{1/2}} \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1)} & \text{otherwise,} \end{array} \right. \tag{3.2}$$

und

$$D(b, c) = \left\{ \begin{array}{cl} 0 & \text{if } \beta_2 \neq \gamma_2 \\ \frac{1}{q_2^{1/2}} \omega^{\beta_1 \gamma_1 q_1 - \beta_1 \beta_2 u} & \text{otherwise.} \end{array} \right. \tag{3.3}$$

Es ist leicht zu erkennen, dass $CD(a, c) = C(a, b)D(b, c)$ wobei $b = \alpha_2 q_1 + \gamma_2$ da wir brauchen $\alpha_2 = \beta_1$ und $\beta_2 = \gamma_2$ um Null-Null-Einträge in zu gewährleisten $C(a, b)$ und $D(b, c)$. Jetzt,

$$\begin{array}{l} CD(a, c) = \frac{1}{q_1^{1/2} q_2^{1/2}} \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1) + \beta_1 \gamma_1 q_1 - \beta_1 \beta_2 u} \\ = \frac{1}{q^{1/2}} \omega^{\alpha_1 \gamma_2 q_2 + \alpha_2 \gamma_1 q_1 + \alpha_2 \gamma_2} \\ = \frac{1}{q^{1/2}} \omega^{(\alpha_1 q_2 + \alpha_2)(\gamma_1 q_1 + \gamma_2)} \\ = \frac{1}{q^{1/2}} \omega^{ac} \tag{3.4} \end{array}$$

Also $CD(a, c) = A_q(a, c)$.

Wir werden nun skizzieren, wie wir die Zeilen und Spalten von $C$ um die Matrix zu erhalten $\bigoplus_{q_2} A_{q_1}$. Die Matrix $C$ kann in block-diagonale Form gebracht werden, wobei die Blöcke indexiert sind durch $\alpha_2 = \beta_1$ (da alle Einträge mit $\alpha_2 \neq \beta_1$ sind 0). Lass $u + 1 \equiv tq_2 \pmod q$. Innerhalb eines bestimmten Blocks $\alpha_2 = \beta_1$, sehen die Einträge so aus wie

$$\begin{array}{l} \sqrt{q_1} C(a, b) = \omega^{\alpha_1 \beta_2 q_2 + \beta_1 \beta_2 (u+1)} \\ = \exp(2\pi i(\alpha_1 \beta_2 + \beta_1 \beta_2 t)q_2/q) \\ = \exp(2\pi i(\alpha_1 + \alpha_2 t)\beta_2/q_1). \tag{3.5} \end{array}$$

Wenn wir also die Zeilen innerhalb dieses Blocks so anordnen, dass sie indexiert sind durch $\alpha' \equiv \alpha_1 + \alpha_2 t \pmod q_1$, erhalten wir die Transformation $\alpha' \to \beta_2$ mit Amplitude $\frac{1}{q_1^{1/2}} \exp(2\pi i \alpha' \beta_2 / q_1)$; das heißt, die Transformation, die durch die unitäre Matrix mit der $(\alpha', \beta_2)$ Eintrag gleich $\frac{1}{q_1^{1/2}} \exp(2\pi i \alpha' \beta_2 / q_1)$, was ist $A_{q_1}$. Die Matrix $D$ kann ähnlich umgeordnet werden, um die Matrix zu erhalten $\bigoplus_{q_1} A_{q_2}$.

Wir müssen auch zeigen, wie man eine glatte Methode findet $q$ das dazwischen liegt $n$ und $2n$ in polynomialer Zeit. Sie sind tatsächlich glatt $q$ Viel näher an $n$ als das, aber das ist alles, was wir brauchen. Es ist nicht bekannt, wie man glatte Zahlen findet, die sehr nahe an liegen $n$ in polynomialer Zeit.

Lemma 3.2 Gegeben $n$, gibt es einen polynomiellen Algorithmus, um eine Zahl zu finden $q$ mit $n \le q < 2n$ so dass keine Primkraft größer als $c \log q$ Teilungen $q$, für eine bestimmte Konstante $c$ unabhängig von $n$.

Beweis: Um eine solche zu finden $q$, multipliziere die Primzahlen $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdots p_k$ bis das Produkt größer als ist $n$. Jetzt, wenn das hier

Produkt ist größer als $2n$, teile sie durch die größte Primzahl, die die Zahl größer als hält $n$. Dies ergibt das gewünschte $q$. Zwischen ihnen gibt es immer eine Prime $m$ und $2m$ [17, Satz 418], also $n \le q < 2n$. Der Satz über Primzahlen [17, Satz 6] und einige Berechnungen zeigen, dass die größte Primzahl-Teilung $q$ ist von Größe $O(\log n)$.

Beachte, dass wir Coppersmiths Transformation verwenden $A_{2^k}$ Mit dem $2^k$Die Wurzeln der Einheit setzen wir $q = 2^k$ wobei $k = \lfloor \log_2 n \rfloor + 1$.

## 4 Diskretes Logbuch: der einfache Fall

Das diskrete Logarithmus-Problem lautet: Gegeben eine Primzahl $p$, ein Erzeuger $g$ der multiplikativen Gruppe (mod $p$) und ein $x$ (mod $p$), finden Sie ein $r$ so dass $g^r \equiv x \pmod p$. Wir beginnen damit, einen polynomiellen Algorithmus für diskrete Logitaritümen auf einem Quantencomputer zu geben, falls $p - 1$ ist geschmeidig. Dieser Algorithmus ist analog zu dem Algorithmus in Simons Arbeit [28], mit der Gruppe $Z_2^k$ Ersetzt durch $Z_{p-1}$. Der glatte Fall ist an sich keine interessante Leistung, da es in diesem Fall bereits polynomielle Zeitalgorithmen für klassische Computer gibt [24]; Diesen Fall zu erklären ist jedoch einfacher als entweder der allgemeine Fall des diskreten Logariumos oder des Faktorisierungsalgorithmus, und da die drei Algorithmen ähnlich sind, zeigt dieses Beispiel, wie die komplexeren Algorithmen funktionieren.

Wir beginnen unseren Algorithmus mit $x$, $g$ und $p$ auf dem Band (also im Quantenspeicher unserer Maschine). Wir versuchen zu berechnen $r$ so dass $g^r \equiv x \pmod p$. Da wir sie niemals löschen werden, $x$, $g$, und $p$ sind Konstanten, und wir geben einen Zustand unserer Maschine durch den anderen Inhalt des Bandes an.

Der Algorithmus beginnt damit, Zahlen zu "wählen" $a$ und $b$ (mod $p - 1$) gleichmäßig, sodass der Zustand der Maschine nach diesem Schritt ist

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b\rangle. \tag{4.1}$$

Der Algorithmus berechnet als Nächstes $g^a x^{-b} \pmod p$ reversibel, also müssen wir die Werte beibehalten $a$ und $b$ auf dem Band. Der Zustand der Maschine ist jetzt

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b, g^a x^{-b} \pmod p\rangle. \tag{4.2}$$

Was wir jetzt tun, ist die Transformation zu nutzen $A_{p-1}$ Zur Abbildung $a \to c$ mit Amplitude $\frac{1}{(p-1)^{1/2}} \exp(2\pi i ac / (p-1))$ und $b \to d$ mit Amplitude $\frac{1}{(p-1)^{1/2}} \exp(2\pi i bd / (p-1))$. Wie im vorherigen Abschnitt diskutiert, handelt es sich hierbei um eine unitäre Transformation, und da $p - 1$ glatt ist, es kann erreicht werden

128

in polynomialer Zeit auf einer Quantenmaschine. Dadurch bleibt die Maschine im Zustand

$$\frac{1}{(p-1)^2} \sum_{a,b,c,d=0}^{p-2} \exp \left( \frac{2\pi i}{p-1} (ac+bd) \right) |c, d, g^a x^{-b} \pmod{p} \tag{4.3}$$

Wir berechnen nun die Wahrscheinlichkeit, dass die Berechnung mit der Maschine im Zustand endet $|c, d, y\rangle$ mit $y \equiv g^k \pmod{p}$. Diese Wahrscheinlichkeit ist der Absolutwert des Quadrats der Summe über alle Möglichkeiten, wie die Maschine diesen Zustand erzeugen könnte, oder

$$\left| \frac{1}{(p-1)^2} \sum_{\substack{a,b \\ a-rb \equiv k}} \exp \left( \frac{2\pi i}{p-1} (ac+bd) \right) \right|^2, \tag{4.4}$$

wobei die Summe über alle ist $a, b$ befriedigend $a - rb \equiv k \pmod{p-1}$. Diese Bedingung ergibt sich daraus, dass rechnerische Wege nur dann interfereren können, wenn sie dieselben liefern $y \equiv g^{a-rb} \equiv g^k \pmod{p}$. Wir setzen nun die Gleichung ein $a \equiv k + rb \pmod{p-1}$ im obigen Exponential. Die obige Summe reduziert sich dann auf

$$\left| \frac{1}{(p-1)^2} \sum_{b=0}^{p-2} \exp \left( \frac{2\pi i}{p-1} (kc + b(d+rc)) \right) \right|^2. \tag{4.5}$$

Wenn jedoch gilt: $d+rc \not\equiv 0 \pmod{p-1}$ Die obige Summe ist über eine Menge von $(p-1)^{\text{st}}$ Einheitswurzeln gleichmäßig um den Einheitskreis verteilt, sodass die Wahrscheinlichkeit 0 ist. Wenn $d \equiv -rc$ Die obige Summe liegt über derselben Einheitswurzel $p-1$ Zeiten, geben $(p-1)e^{2\pi i k c / (p-1)}$, also ist die Wahrscheinlichkeit $1 / (p-1)^2$. Wir können überprüfen, ob diese Wahrscheinlichkeiten zu eins summiert werden, indem wir zählen, dass es $(p-1)^2$ Bundesstaaten $|c, -rc, y\rangle$ da es gibt, dass es $p-1$ Wahlmöglichkeiten von $c \pmod{p-1}$ und $p-1$ Wahlmöglichkeiten von $y \not\equiv 0 \pmod{p}$.

Unsere Berechnung erzeugt daher eine Zufallsberechnung $c \pmod{p-1}$ und das entsprechende $d \equiv -rc \pmod{p-1}$. Wenn $c$ und $p-1$ relativ prim sind, können wir finden $r$ nach Division. Weil wir unter allen möglichen Möglichkeiten wählen $c$mit gleicher Wahrscheinlichkeit die Chance, dass $c$ und $p-1$ sind relativ prim ist $\phi(p-1)/(p-1)$, wobei $\phi$ ist der Euler $\phi$-Funktion. Das ist leicht zu überprüfen $\phi(p-1)/(p-1) > 1/\log(p)$. (Eigentlich von [17, Satz 328], Grenze $\phi(p-1)/(p-1) \approx e^{-\gamma}/\log \log p$.) Daher benötigen wir nur eine Anzahl von Experimenten, die polynomiell in sind $\log p$ um zu erhalten $r$ mit hoher Wahrscheinlichkeit. Tatsächlich können wir eine Menge von finden $c$, so dass mindestens einer relativ prim zu jedem Primteiler von ist $p-1$ indem das Experiment nur eine erwartete konstante Anzahl von Zeiten wiederholt wird. Das würde uns auch genügend Informationen geben, um sie zu erhalten $r$.

## 5 Eine Anmerkung zur Präzision

Die Anzahl der Präzisionsbits, die in der Amplitude quantenmechanischer Computer benötigt werden, könnte ein Hindernis für die Praktikabilität darstellen. Die allgemein akzeptierte theoretische Trennlinie zwischen machbar und unmöglich ist, dass polynomielle Genauigkeit (d. h. eine Anzahl von Bits logarithmisch in der Problemgröße) machbar ist und mehr nicht machbar. Das liegt daran, dass bei einem Quantencomputer der Phasenwinkel durch ein physikalisches Gerät berechnet werden müsste, und der Bau solcher Bauelemente mit besserer als polynomieller Genauigkeit erscheint zweifellos unpraktisch. Tatsächlich kann selbst polynomielle Präzision sich als unpraktisch erweisen; Diese als theoretische Trennlinie führt jedoch zu schönen theoretischen Eigenschaften.

Wir müssen daher zeigen, dass die Berechnungen im vorherigen Abschnitt nur polynomielle Genauigkeit in den Amplituden verwenden müssen. Der bloße Akt, den Ausdruck aufzuschreiben $\exp(2\pi i a c / (p-1))$ scheint zu implizieren, dass wir exponentielle Präzision benötigen, da dieser Phasenwinkel exponentiell präzise ist. Glücklicherweise ist das nicht der Fall. Betrachten wir dieselbe Matrix $A_{p-1}$ mit jedem Term $\exp(2\pi i a c / (p-1))$ Ersetzt durch $\exp(2\pi i a c / (p-1) \pm \pi i / 20)$. Jeder positive Fall, d. h. einer, der resultiert in $d \equiv -rc$, wird weiterhin mit fast ebenso hoher Wahrscheinlichkeit wie zuvor auftreten; anstatt hinzuzufügen $p-1$ Amplituden, die exakt denselben Phasenwinkel haben, fügen wir hinzu $p-1$ Amplituden, die nahezu denselben Phasenwinkel haben, und somit wird die Größe der Summe nur um einen konstanten Faktor reduziert. Der Algorithmus liefert somit ein $(c, d)$ mit $d \equiv -rc$ mit konstanter Wahrscheinlichkeit (statt Wahrscheinlichkeit 1).

Erinnern wir uns, dass wir die Matrix erhalten $A_{p-1}$ indem man höchstens multipliziert $\log p$ Matrizen $A_{q_i}$. Außerdem, jeder Eintrag in $A_{p-1}$ ist höchstens das Produkt von $\log p$ Bedingungen. Angenommen, jeder Phasenwinkel wäre höchstens um etwas anderes $\epsilon / \log p$ in der $A_{q_i}$'s. Dann wäre im Produkt jeder Phasenwinkel höchstens um etwas anderes $\epsilon$, was ausreicht, um die Berechnung mit konstanter Erfolgswahrscheinlichkeit durchzuführen. Ein ähnliches Argument zeigt, dass die Größe der Amplituden in der $A_{q_i}$ kann um einen Polynombruch abweichen. Ähnliche Argumente gelten für den allgemeinen Fall der diskreten Logarithm und für die Faktorisierung, um zu zeigen, dass wir auch in diesen Fällen nur polynomielle Genauigkeit für die Amplituden benötigen.

Wir müssen noch zeigen, wie man konstruiert $A_{q_i}$ von einheitlichen Matrizen konstanter Größe mit begrenzter Präzision. Die Argumente sind im Wesentlichen die oben genannten, aber wir werden sie in diesem Artikel nicht darlegen, weil Bennett et al. [4] gezeigt haben, dass es ausreicht, polynomielle Präzision für jede Berechnung auf einer quantenmechanischen Turingmaschine zu verwenden, um mit hoher Wahrscheinlichkeit die Antwort zu erhalten.

Da Präzision leicht der begrenzende Faktor für die Praktikabilität der Quantenberechnung sein könnte, könnte es ratsam sein zu untersuchen, wie viel Präzision tatsächlich benötigt wird für

129

Quantenalgorithmen. Obwohl Bernstein und Vazirani [4] zeigen, dass die Anzahl der benötigten Präzisionsbits niemals größer ist als der Logarithmus der Anzahl der Rechenschritte, die ein Quantencomputer unternimmt; in manchen Algorithmen könnte dies theoretisch weniger erfordern. Interessante offene Fragen sind, ob es möglich ist, diskrete Logarithmen oder Faktorisierung mit weniger als polynomieller Präzision durchzuführen und ob ein Kompromiss zwischen Präzision und Zeit möglich ist.

## 6 Faktorisierung

Der Algorithmus zur Faktorisierung ähnelt dem für den allgemeinen Fall der diskreten Logarithmus, nur etwas einfacher. Ich präsentiere diesen Algorithmus vor dem allgemeinen Fall des diskreten Logarithmus, um die drei Algorithmen in dieser Arbeit in der Reihenfolge ihrer zunehmenden Komplexität zu bestimmen. Leser, die sich für diskretes Logbuch interessieren, können zum nächsten Abschnitt überspringen.

Anstatt einen Quantencomputer-Algorithmus zur Faktorisierung von n zu geben, geben wir einen Quantencomputer-Algorithmus zur Bestimmung der Ordnung eines Elements x in der multiplikativen Gruppe (mod n); das heißt, die kleinste ganze Zahl r, so dass  \( x^{r} \equiv 1 \pmod{n} \) . Es gibt eine randomisierte Reduktion von der Faktorisierung auf die Ordnung eines Elements [23].

Um eine ungerade Zahl n zu faktorisieren, gibt es eine Methode zur Berechnung der Ordnung eines Elements, wählen wir ein zufälliges x und bestimmen die Ordnung  \( r_{x} \)  von x und berechnen  \( \gcd(x^{r_{x}/2}-1,n) \) . Dies liefert nur dann keinen nichttrivialen Teiler von n, wenn  \( r_{x} \)  ist ungerade oder wenn  \( x^{r_{x}/2}\equiv-1\pmod{n} \) . Mit diesem Kriterium kann gezeigt werden, dass der Algorithmus mit mindestens einer Wahrscheinlichkeit einen Faktor n findet  \( 1-1/2^{k} \) , wobei k die Anzahl der verschiedenen Primfaktoren von n ist. Dieses Schema funktioniert also, solange n keine Primpotenz ist; die Faktorisierung von Primpotenzen kann jedoch mit klassischen Methoden effizient erfolgen.

Gegeben x und n, um r zu finden, so dass  \( x^{r} \equiv 1 \pmod{n} \) , machen wir Folgendes. Zuerst finden wir ein glattes q mit  \( 2n^{2} \leq q < 4n^{2} \) . Als Nächstes setzen wir unsere Maschine in die gleichmäßige Überlagerung von Zuständen, die Zahlen repräsentieren  \( a \pmod{q} \) . Dadurch bleibt unsere Maschine im Zustand.

\[
\frac {1}{q ^ {1 / 2}} \sum_ {a = 0} ^ {q - 1} | a \rangle . \tag {6.1}
\]

Wie im Algorithmus für diskrete Logs schreiben wir n, x oder q nicht im Zustand unserer Maschine, da wir diese Werte nie ändern.

Als Nächstes berechnen wir \( x^a \pmod{n} \). Da wir behalten \( x \) und \( a \) auf dem Band kann dies rückgängig gemacht werden. Das lässt unsere Maschine im Zustand zurück

\[
\frac {1}{q ^ {1 / 2}} \sum_ {a = 0} ^ {q - 1} | a, x ^ {a} (\mathrm{mod} n) \rangle . \tag {6.2}
\]

Anschließend führen wir unsere Fourier-Transformation durch \(A_{q}\) Kartierung \(a \to c\)

mit Amplitude \(\frac{1}{q^{1/2}}\exp(2\pi iac/q)\). Dadurch bleibt unsere Maschine im Zustand.

\[
\frac {1}{q} \sum_ {a = 0} ^ {q - 1} \exp (2 \pi i a c / q) | c, x ^ {a} (\mathrm{mod} n) \rangle . \tag {6.3}
\]

Schließlich beobachten wir die Maschine. Es würde ausreichen, nur den Wert von zu betrachten \( c \), aber zur Klarheit nehmen wir an, dass wir beide beobachten \( c \) und \( x^a \pmod{n} \). Wir berechnen nun die Wahrscheinlichkeit, dass unsere Maschine in einem bestimmten Zustand endet \( |c, x^k \pmod{n}\rangle \), wobei wir annehmen können \( 0 \leq k < r \). Summiert man alle möglichen Wege, diesen Zustand zu erreichen, ergibt sich, dass diese Wahrscheinlichkeit lautet

\[
\left| \frac {1}{q} \sum_ {a: x ^ {a} \equiv x ^ {k}} \exp (2 \pi i a c / q) \right| ^ {2}. \tag {6.4}
\]

wobei die Summe über alle ist \(a\), \(0 \leq a < q\), so dass \(x^{a} \equiv x^{k} (\bmod n)\). Denn die Ordnung von \(x\) ist \(r\), diese Summe ist äquivalent über alle \(a\) befriedigend \(a \equiv k (\bmod r)\). Schreiben \(a = br + k\), stellen wir fest, dass die obige Wahrscheinlichkeit ist

\[
\left| \frac {1}{q} \sum_ {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i (b r + k) c / q) \right| ^ {2}. \tag {6.5}
\]

Wir können den Term von ignorieren. \(\exp(2\pi ikc/q)\), da sie aus der Summe herausgerechnet werden kann und den Betrag 1 hat. Wir können auch ersetzen \(rc\) mit \(\{rc\}_q\), wobei \(\{rc\}_q\) ist der Rest, der kongruent ist zu \(rc (\bmod q)\) und liegt im Bereich \(-q/2 < \{rc\}_q \leq q/2\). Damit bleibt der Ausdruck

\[
\left| \frac {1}{q} \sum_ {b = 0} ^ {\lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i b \{r c \} _ {q} / q) \right| ^ {2}. \tag {6.6}
\]

Wir werden nun zeigen, dass, wenn  \( \{rc\}_{q} \)  klein genug ist, werden alle Amplituden in dieser Summe nahezu in die gleiche Richtung gehen, was eine hohe Wahrscheinlichkeit ergibt. Wenn  \( \{rc\}_{q} \)  klein bezüglich q ist, können wir die Änderung der Variablen t = verwenden b/q und approximiere diese Summe mit dem Integral

\[
\left| \int_ {0} ^ {\frac {1}{q} \lfloor (q - k - 1) / r \rfloor} \exp (2 \pi i \{r c \} _ {q} t) d t \right| ^ {2}. \tag {6.7}
\]

Wenn \( |\{rc\}_{q}| \leq r/2 \), diese Größe kann gezeigt werden, dass sie asymptotisch unterhalb begrenzt ist durch \( 4/(\pi^{2}r^{2}) \), und somit zumindest \( 1/3r^{2} \). Die Wahrscheinlichkeit, einen gegebenen Zustand zu sehen \( |c, x^{k} (\text{mod } n)\rangle \) wird somit zumindest \( 1/3r^{2} \) wenn

\[
\frac {- r}{2} \leq \{r c \} _ {q} \leq \frac {r}{2}, \tag {6.8}
\]

130

d. h. wenn es eine gibt $d$ so dass

$$\frac{-r}{2} \leq rc - dq \leq \frac{r}{2}. \tag{6.9}$$

Division durch $rq$ und das Umordnen der Terme ergibt

$$\left| \frac{c}{q} - \frac{d}{r} \right| \leq \frac{1}{2q}. \tag{6.10}$$

Wir wissen es $c$ und $q$. Weil $q \geq 2n^2$, es gibt höchstens einen Bruch $d/r$ mit $r < n$ Das erfüllt die oben genannte Ungleichung. Daher können wir den Bruch erhalten $d/r$ in niedrigsten Termen durch Rundung $c/q$ auf den nächstgelegenen Bruch mit einem Nenner, der kleiner als ist $n$. Dieser Bruch kann in polynomieller Zeit durch eine kontinuierliche Bruchentwicklung von $c/q$, die alle besten Annäherungen von $c/q$ durch Brüche [17, Kapitel X].

Wenn wir den Bruch haben $d/r$ in niedrigsten Termen, und wenn $d$ zufällig relativ prime zu $r$, das wird uns geben $r$. Wir werden nun die Anzahl der Zustände zählen $|c, x^k \pmod{n}\rangle$ die es uns ermöglichen, zu berechnen $r$ auf diese Weise. Es gibt $\phi(r)$ Mögliche Werte für $d$ relativ prime zu $r$, wobei $\phi$ ist Eulers $\phi$ Funktion. Jeder dieser Brüche $d/r$ ist nahe an einem Bruch $c/q$ mit $|c/q - d/r| \leq 1/2q$. Es gibt auch $r$ Mögliche Werte für $x^k$, da $r$ ist die Ordnung von $x$. Somit gibt es $r\phi(r)$ Bundesstaaten $|c, x^k \pmod{n}\rangle$ was es uns ermöglichen würde, zu erhalten $r$. Da jeder dieser Zustände mit einer Wahrscheinlichkeit von mindestens eintritt $1/3r^2$, erhalten wir $r$ mit mindestens einer Wahrscheinlichkeit $\phi(r)/3r$. Unter Verwendung des Theorems, dass $\phi(r)/r > k/\log \log r$ für einige fest $k$ [17, Satz 328], dies zeigt, dass wir finden $r$ mindestens ein $k/\log \log r$ Bruchteil der Zeit, also nur durch Wiederholung dieses Experiments $O(\log \log r)$ Manchmal ist uns eine hohe Erfolgswahrscheinlichkeit sicher.

Beachten Sie, dass wir im Algorithmus für Ordnung viele Eigenschaften der Multiplikation (mod (mod) nicht verwendet haben $n$). Tatsächlich, wenn wir eine Permutation haben $f$ Abbildung der Menge $\{0, 1, 2, \dots, n-1\}$ in sich selbst, so dass es $k$Wiederhole, $f^{(k)}(a)$, ist in Zeitpolynom in berechenbar $\log n$ und $\log k$, wird derselbe Algorithmus in der Lage sein, die Ordnung eines Elements zu bestimmen $a$ unter $f$, d. h. das Minimum $r$ so dass $f^{(r)}(a) = a$.

## 7 Diskretes Logarithmus: der allgemeine Fall

Im allgemeinen Fall finden wir zunächst eine glatte Zahl $q$ so dass $q$ ist nah dran $p$, d. h. mit $p \leq q \leq 2p$ (siehe Lemma 3.2).

Als Nächstes machen wir dasselbe wie im einfachen Fall, nämlich wählen wir $a$ und $b$ einheitlich (Mod) $p-1$), und dann berechnen $g^a x^{-b} \pmod{p}$. Das lässt unsere Maschine im Zustand zurück

$$\frac{1}{p-1} \sum_{a=0}^{p-2} \sum_{b=0}^{p-2} |a, b, g^a x^{-b} \pmod{p}\rangle. \tag{7.1}$$

Wie zuvor verwenden wir die Fourier-Transformation $A_q$ um zu senden $a \to c$ und $b \to d \pmod{q}$, mit Amplitude $\frac{1}{q} \exp(2\pi i(ac+bd)/q)$, was uns den Staat ergibt

$$\frac{1}{(p-1)q} \sum_{a,b=0}^{p-2} \sum_{c,d=0}^{q-1} \exp\left(\frac{2\pi i}{q}(ac+bd)\right) |c, d, g^a x^{-b} \pmod{p}\rangle. \tag{7.2}$$

Beachten Sie, dass wir nun mit zwei Moduli zu tun haben, $p-1$ und $q$. Auch wenn das den Überblick erschwert, werden wir trotzdem in der Lage sein, den Überblick zu behalten $r$ mit einem Algorithmus ähnlich dem einfachen Fall. Die Wahrscheinlichkeit, einen Zustand zu beobachten $|c, d, y\rangle$ mit $y \equiv g^k \pmod{p}$ ist, fast wie zuvor,

$$\left| \frac{1}{(p-1)q} \sum_{\substack{a,b \\ a-rb \equiv k}} \exp\left(\frac{2\pi i}{q}(ac+bd)\right) \right|^2 \tag{7.3}$$

wobei die Summe über alle ist $(a, b)$ so dass $a - rb \equiv k \pmod{p-1}$. Wir verwenden nun die Relation

$$a = br + k - (p-1) \left\lfloor \frac{br+k}{p-1} \right\rfloor \tag{7.4}$$

und setze in den obigen Ausdruck ein, um die Amplitude zu erhalten

$$\frac{1}{(p-1)q} \sum_{b=0}^{p-2} \exp\left(\frac{2\pi i}{q} (brc + kc + bd - c(p-1) \left\lfloor \frac{br+k}{p-1} \right\rfloor)\right). \tag{7.5}$$

Der Absolutwert des Quadrats dieser Amplitude ist die Wahrscheinlichkeit, den Zustand zu beobachten $|c, d, g^k \pmod{p}\rangle$. Wir werden diesen Ausdruck nun analysieren. Erstens ein Faktor von $\exp(2\pi ikc/q)$ kann aus allen Termen herausgenommen und ignoriert werden, da sich dadurch die Wahrscheinlichkeit nicht ändert. Als Nächstes teilen wir den Exponenten in zwei Teile auf und faktorisieren aus $b$ um zu erhalten

$$\frac{1}{(p-1)q} \sum_{b=0}^{p-2} \exp\left(\frac{2\pi i}{q} U\right) \exp\left(\frac{2\pi i}{q} V\right), \tag{7.6}$$

wobei

$$\begin{array}{l} U = bT, \\ T = rc + d - \frac{r}{p-1} \{c(p-1)\}_q, \tag{7.7} \end{array}$$

und

$$V = \left(\frac{kr}{p-1} - \left\lfloor \frac{br+k}{p-1} \right\rfloor\right) \{c(p-1)\}_q. \tag{7.8}$$

Hiermit $\{z\}_q$ wir meinen den Rest von $z \pmod{q}$ mit $-q/2 < \{z\}_q \leq q/2$. Wir werden zeigen, dass wir, wenn wir genügend "gute" Ausgaben erhalten, trotzdem ableiten können $r$, und dass außerdem die Chance, ein "gutes" Ergebnis zu erzielen, konstant ist. Die Idee ist, dass wenn

$$|\{T\}_q| = |rc + d - \frac{r}{p-1} \{c(p-1)\}_q - jq| \leq \frac{1}{2}, \tag{7.9}$$

131

wobei $j$ ist die ganzzahligste Zahl zu $T/q$, dann gilt als $b$ variiert zwischen 0 und $p - 2$, die Phase des ersten Exponentialterms in Gleichung (7.6) variiert höchstens über die Hälfte des Einheitskreises. Außerdem, wenn

$$|\{c(p - 1)\}_q| \le q/20, \tag{7.10}$$

dann $|V|$ ist höchstens immer $q/20$, sodass die Phase des zweiten Exponentialtermes in Gleichung (7.6) niemals weiter als entfernt ist als $\exp(\pi i/10)$ Von 1. Durch die Kombination dieser beiden Beobachtungen zeigen wir, dass, wenn beide Bedingungen erfüllt sind, der Beitrag des entsprechenden Terms zur Wahrscheinlichkeit signifikant ist. Außerdem gelten beide Bedingungen mit konstanter Wahrscheinlichkeit, und eine vernünftige Stichprobe von $c$, für die Bedingung (7.9) gilt, ermöglicht es uns, zu deduktieren $r$.

Wir geben nun eine untere Schranke für die Wahrscheinlichkeit jedes guten Outputs, also ein Output, das die Bedingungen (7,9) und (7,10) erfüllt. Das wissen wir als $b$ reicht von 0 bis $p - 2$, die Phase von $\exp(2\pi i U/q)$ reicht von 0 bis $2\pi i W$ wobei

$$W = \frac{p - 2}{q} \left( rc + d - \frac{r}{p-1} \{c(p - 1)\}_q - jq \right) \tag{7.11}$$

und $j$ ist wie in Gleichung (7.9). Somit ist die Komponente der Amplitude der ersten Exponentialgröße in Gleichung (7,6) in Richtung

$$\exp(\pi i W) \tag{7.12}$$

ist es zumindest $\cos(2\pi |W/2 - Wb/(p - 2)|)$. Nun kann die Phase nach Bedingung (7,10) höchstens um Bedingung variieren $\pi i/10$ aufgrund des zweiten Exponentialwerts $\exp(2\pi i V/q)$. Wendet man diese Variation so an, dass die Komponente in Richtung (7.12) minimiert wird, erhält man, dass die Komponente in dieser Richtung mindestens ist $\cos(2\pi |W/2 - Wb/(p - 2)| + \pi/10)$. Da $p < q$, und aus Bedingung (7.9), $|W| \le 1/2$, wenn man alles zusammensetzt, die Wahrscheinlichkeit, in einen Zustand zu gelangen, $|c, d, y)$ die sowohl Bedingung (7.9) als auch (7.10) erfüllt, mindestens ist

$$\left( \frac{1}{q} \frac{2}{\pi} \int_{\pi/10}^{7\pi/20} \cos t \, dt \right)^2, \tag{7.13}$$

Oder zumindest $.137/q^2$.

Wir zählen nun die Anzahl der Paare $(c, d)$ die Bedingungen (7.9) und (7.10) erfüllen. Die Anzahl der Paare $(c, d)$ so dass (7.9) genau die Anzahl der möglichen ist. $c$'s, denn für jeden $c$ Es gibt genau eine $d$ so dass (7.9) gilt (runden Sie den Bruch auf die nächstgelegene ganze Zahl ab, um dies zu erhalten. $d$). Die Anzahl von $c$'s für die (7.10) gilt ist ungefähr $q/10$. Somit gibt es $q/10$ Paare $(c, d)$ Beide Bedingungen erfüllen. Multiplizieren mit $p - 1$, was die Anzahl der möglichen ist. $y$'s, ergibt ungefähr $pq/10$ Bundesstaaten $|c, d, y)$. Die Kombination dieser Berechnung mit der unteren Schranke für die Wahrscheinlichkeit jedes guten Zustands ergibt uns, dass die Wahrscheinlichkeit, einen guten Zustand zu erhalten, mindestens bei mindestens beträgt $p/80q$, oder zumindest $1/160$ (da $q < 2p$).

Wir wollen uns jetzt erholen $r$ aus einem Paar $c, d$ so dass

$$-\frac{1}{2q} \le \frac{d}{q} + \frac{r}{q} \left( c - \frac{\{c(p - 1)\}_q}{p - 1} \right) \le \frac{1}{2q} \pmod{1}, \tag{7.14}$$

wobei diese Gleichung aus Bedingung (7.9) durch Division durch Teilen durch erhalten wurde $q$. Das Erste, was man beachten sollte, ist, dass der Multiplikator auf $r$ ein Bruch mit Nenner ist $p - 1$, da $q$ gleichmäßig verteilt $c(p - 1) - \{c(p - 1)\}_q$. Daher brauchen wir nur rund $d/q$ auf das nächstgelegene Vielfache von $1/(p - 1)$ und teilen $(\mod p - 1)$ von

$$c' = \frac{c(p - 1) - \{c(p - 1)\}_q}{q} \tag{7.15}$$

um einen Kandidaten zu finden $r$. Um zu zeigen, dass dieses Experiment nur polynomiell wiederholt werden muss, um das richtige Experiment zu finden $r$ Benötigt nur wenige weitere Details. Das Problem ist wieder, dass wir nicht durch eine Zahl teilen können, die nicht relativ prim ist $p - 1$.

Für den allgemeinen Fall des diskreten Logarithmus-Algorithmus wissen wir nicht, dass alle möglichen Werte von $c'$ werden mit angemessener Wahrscheinlichkeit erzeugt; Wir wissen das nur über ein Zehntel von ihnen. Diese zusätzliche Schwierigkeit macht den nächsten Schritt schwieriger als der entsprechende Schritt in den beiden vorherigen Algorithmen. Wenn wir den Rest von $r$ modulo alle Primpotenz-Teilenden $p - 1$, könnten wir den chinesischen Restsatz zur Wiederherstellung verwenden $r$ in polynomialer Zeit. Wir werden diesen Rest nur für Primzahlen größer als 20 finden können, aber mit etwas zusätzlicher Arbeit können wir trotzdem wiederherstellen $r$.

Was wir haben, ist, dass jedes Gut $(c, d)$ Das Paar wird mit mindestens einer Wahrscheinlichkeit erzeugt $.137p/q > 1/16q$, und dass mindestens ein Zehntel des Möglichen ist $c$'s sind in einer guten Situation $(c, d)$ Paar. Aus Gleichung (7.15) folgt, dass diese $c$'s werden von $c/q$ zu $c'/(p - 1)$ durch Rundung auf das nächstgelegene ganzzahlige Vielfache von $1/(p - 1)$. Darüber hinaus das Gute $c$'s sind genau die, in denen $c/q$ ist nah dran $c'/(p - 1)$. So entsteht jedes Gut $c$ entspricht genau einem $c'$. Das möchten wir für jede Prime-Power zeigen $p_t^{n_t}$ Teilung $p - 1$, ein zufälliges Gut $c'$ es ist unwahrscheinlich, dass es das enthält $p_t$. Wenn wir bereit sind, eine große Konstante für den Algorithmus zu akzeptieren, können wir die Primpotenzen unter 20 einfach ignorieren; Wenn wir es wissen $r$ Modulo aller Primpotenzen über 20 können wir alle möglichen Reste für Primzahlen unter 20 mit nur einer (großen) konstanten Erhöhung der Laufzeit ausprobieren. Weil mindestens ein Zehntel der $c$'s waren in einem guten $(c, d)$ Paar, mindestens ein Zehntel der $c'$Das ist gut. Daher gilt für eine Primzahl $p_t^{n_t}$, ein zufälliges Gut $c'$ ist teilbar durch $p_t^{n_t}$ mit höchstens einer Wahrscheinlichkeit $10/p_t^{n_t}$. Wenn wir haben $t$ Gut $c'$ist die Wahrscheinlichkeit, eine Primzahl über 20 zu haben, die alle teilt, daher höchstens höchstens

$$\sum_{\substack{p_t^{n_t} > 20 \\ p_t^{n_t} \le p - 1}} \left( \frac{10}{p_t^{n_t}} \right)^t, \tag{7.16}$$

132

wobei die Summe über alle Primpotenzen größer als 20 ist, die p - 1 teilen. Diese Summe (über alle ganzen Zahlen > 20) konvergiert für t = 2 und verringert sich bei jeder weiteren Erhöhung von t um 1 um mindestens den Faktor 2; Daher ist für eine große Konstante t kleiner als 1/2.

Erinnern Sie sich, dass jedes Gut c' mit mindestens einer Wahrscheinlichkeit erhalten wird 1/16q von jedem Experiment. Da es gibt q/10 Gute C's, nach 160T-Experimenten erhalten wir wahrscheinlich eine Stichprobe von T guten C's, die gleichermaßen aus allen guten C's ausgewählt wurden. So können wir eine Menge von c's finden, so dass alle Primpotenzen p_i^α_Ich > 20, die P-1 teilen, sind relativ prim zu mindestens einem dieser C's. Für jede Primzahl p_i kleiner als 20, haben wir somit höchstens 20 Möglichkeiten für den Rest modulo p_i^α_Ich, wo α_i ist der Exponent auf der Primzahl p_i in der Primfaktorisierung von p - 1. Wir können somit alle Möglichkeiten für Reste modulo Potenzen von Primzahlen kleiner als 20 ausprobieren: Für jede Möglichkeit können wir das entsprechende r mit dem chinesischen Restsatz berechnen und dann prüfen, ob es sich um den gewünschten diskreten Logarithmus handelt.

Dieser Algorithmus verwendet nicht viele Eigenschaften von Z_p, sodass wir denselben Algorithmus verwenden können, um diskrete Logarithmen über anderen Körpern wie Z zu finden_p^α. Was wir brauchen, ist, dass wir die Reihenfolge des Erzeugers kennen und dass wir Elemente in polynomieller Zeit multiplizieren und Inverse nehmen können.

Wenn man diesen Algorithmus tatsächlich programmieren würde (der warten muss, bis ein Quantencomputer gebaut ist), gäbe es viele Möglichkeiten, wie die Effizienz gegenüber der in diesem Artikel gezeigten Effizienz erhöht werden könnte.

### Danksagungen

Ich möchte Jeff Lagarias dafür danken, dass er einen kritischen Fehler in der ersten Version des diskreten Log-Algorithmus gefunden und behoben hat. Ich möchte auch ihm, Charles Bennett, Gilles Brassard, Andrew Odlyzko, Dan Simon, Umesh Vazirani sowie anderen zu zahlreichen Korrespondenten danken, um sie aufzuzählen, für produktive Diskussionen, für Korrekturen und Verbesserungen der frühen Entwürfe dieses Artikels sowie für Hinweise auf die Literatur.

### Quellen

1. P. Benioff, "Quantenmechanische Hamiltonsche Modelle von Turingmaschinen", J. Stat. Phys. Bd. 29, S. 515-546 (1982).

2. P. Benioff, "Quantenmechanische Hamiltonsche Modelle von Turingmaschinen, die keine Energie dissipieren", Phys. Rev. Lett. Bd. 48, S. 1581-1585 (1982).

3. C. H. Bennett, "Logische Reversibilität der Berechnung", IBM J. Res. Develop. Bd. 17, S. 525-532 (1973).

4. C. H. Bennett, E. Bernstein, G. Brassard und U. Vazirani, "Was auf einem Quantencomputer möglich ist", Manuskript (1994).

5. E. Bernstein und U. Vazirani, "Quantenkomplexitätstheorie", in Proc. 25th ACM Symp. on Theory of Computation, S. 11-20 (1993).

6. A. Berthiaume und G. Brassard, "Die quantenmechanische Herausforderung für die Strukturkomplexitätstheorie", in Proc. 7th IEEE Conf. on Structure in Complexity Theory, S. 132-137 (1992).

7. A. Berthiaume und G. Brassard, "Oracle-Quantencomputing", in Proc. Workshop on Physics of Computation, S. 195-199, IEEE Press (1992).

8. D. Coppersmith, "Eine ungefähre Fourier-Transformation, nützlich im Quantenfaktorisierung", IBM Research Report RC 19642 (1994).

9. D. Deutsch, "Quantentheorie, das Church-Turing-Prinzip und der universelle Quantencomputer", Proc. Roy. Soc. Lond. Bd. A400, S. 96-117 (1985).

10. D. Deutsch, "Quantencomputernetzwerke", Proc. Roy. Soc. Lond. Bd. A425, S. 73-90 (1989).

11. D. Deutsch und R. Jozsa, "Schnelle Lösung von Problemen durch Quantenberechnung", Proc. Roy. Soc. Lond. Bd. A439, S. 553-558 (1992).

12. D. P. DiVincenzo, "Zwei-Bit-Gatter sind universell für die Quantenberechnung", Manuscript (1994).

13. R. Feynman, "Physik mit Computern simulieren", International Journal of Theoretical Physics, Bd. 21, Nr. 6/7, S. 467-488 (1982).

14. R. Feynman, "Quantenmechanische Computer", Foundations of Physics, Bd. 16, S. 507-531 (1986). (Ursprünglich erschienen in Optics News, Februar 1985.)

15. L. Fortnow und M. Sipser, "Gibt es interaktive Protokolle für co-NP-Sprachen?" Informieren. Proc. Lett. Bd. 28, S. 249–251 (1988).

16. D. M. Gordon, "Diskrete Logarithmen in GF(p) mit dem Zahlenkörpersieb", SIAM J. Discrete Math. Bd. 6, S. 124-139 (1993).

17. G. H. Hardy und E. M. Wright, Eine Einführung in die Zahlentheorie, fünfte Auflage, Oxford University Press, New York (1979).

18. R. Landauer, "Ist die Quantenmechanik nützlich?" Proc. Roy. Soc. Lond., wird erscheinen (1994).

19. A. K. Lenstra und H. W. Lenstra, Jr., Hrsg., The Development of the Number Field Sieve, Lecture Notes in Mathematics Nr. 1554, Springer-Verlag (1993).

20. H. W. Lenstra, Jr. und C. Pomerance, "Eine strenge Zeitbindung zum Faktorisieren ganzer Zahlen", J. Amer. Math. Soc. Bd. 5, S. 483-516 (1992).

21. S. Lloyd, "Ein potenziell realisierbarer Quantencomputer", Science, Bd. 261, S. 1569–1571 (1993).

133

22. S. Lloyd, "Sich einen Quanten-Supercomputer vorstellen", Science, Bd. 263, S. 695 (1994).

23. G. L. Miller, "Riemanns Hypothese und Tests für Primtalzahl", J. Comp. Sys. Sci. Bd. 13, S. 300-317 (1976).

24. S. Pohlig und M. Hellman, "Ein verbesserter Algorithmus zur Berechnung diskreter Logarithmen über GF(p) und ihre kryptografische Bedeutung," IEEE Trans. Information Theory, Bd. 24, S. 106-110 (1978).

25. C. Pomerance, "Schnelle, rigorose Faktorisierung und diskrete Logarithmus-Algorithmen", in Discrete Algorithms and Complexity (Proc. Japan-US Joint Seminar), S. 119-143, Academic Press (1986).

26. R. L. Rivest, A. Shamir und L. Adleman "Eine Methode zur Gewinnung digitaler Signaturen und Public-Key-Kryptosysteme", Communications ACM, Bd. 21, Nr. 2, S. 120-126 (1978).

27. A. Shamir, "IP = PSPACE", in Proc. 31th Ann. Symp. Foundations of Computer Science, S. 11-15, IEEE Press (1990).

28. D. Simon, "Über die Kraft der Quantenberechnung", in Proc. 35th Ann. Symp. Foundations of Computer Science, IEEE Press (1994).

29. W. G. Teich, K. Obermayer und G. Mahler, "Strukturelle Basis multistationärer Quantensysteme II: Effektive Mehrteilchendynamik", Phys. Rev. B, Bd. 37, S. 8111-8121 (1988).

30. T. Toffoli, "Reversible Computing", in Automata, Languages and Programming, Siebtes Kolloq., Lecture Notes in Computer Science Nr. 84 (J. W. De Bakker und J. van Leeuwen, Hrsg.) S. 632-644, Springer-Verlag (1980).

31. W. G. Unruh, "Kohärenz in Quantencomputern aufrechterhalten", Manuscript (1994).

32. A. Yao, "Quantenschaltungskomplexität", in Proc. 34th Ann. Symp. Foundations of Computer Science, S. 352-361, IEEE Press (1993).

134
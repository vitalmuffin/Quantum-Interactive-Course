# Über die Quantentheorie der Moleküle

M. Borna, J.R. Oppenheimerb

aInstitut für Theoretische Physik, Göttingen

bInstitut für Theoretische Physik, Göttingen

# Zusammenfassung

Es wird gezeigt, dass die vertrauten Komponenten der Terme eines Moleküls; Die Energie der elektronischen Bewegung, der Kernschwingung und der Rotation entsprechen systematisch den Termen einer Potenzreihe in der vierten Wurzel des Verhältnisses von Elektronenmasse zu (durchschnittlicher) Kernmasse. Die Behandlung ergibt unter anderem eine Gleichung für die Rotation, die eine Verallgemeinerung der Behandlung von Kramers und Pauli darstellt (oben mit eingebautem Schwungrad). Außerdem scheint es eine Rechtfertigung für die Überlegungen von Franck und Condon zur Intensität der Bandlinien zu geben. Die Beziehungen sind für das zweiatomige Molekül dargestellt.

# Einleitung

Die Terme der molekularen Spektren bestehen üblicherweise aus Teilen verschiedener Größenordnungen; Der größte Beitrag kommt von der elektronischen Bewegung um die Kerne, dann folgt der Beitrag der Kernschwingung und schließlich der Kernrotation. Die Grundlage für die Möglichkeit einer solchen Klassifikation liegt offensichtlich in den vergleichenden Größen von Kern- und Elektronenmassen. Aus der Sicht der alten Quantentheorie, die stationäre Zustände mit Hilfe der klassischen Mechanik berechnete, ist dies das von Born und Heisenberg angewandte Konzept [1]; Es wurde gezeigt, dass die Energieterme als Terme zunehmender Ordnung bezüglich des Verhältnisses erscheinen $\sqrt{m/M}$, wobei m die elektronische Masse und M die durchschnittliche Kernmasse ist. Dadurch treten jedoch sowohl Kernrotation als auch Schwingung in zweiter Ordnung auf, was empirischen Erkenntnissen widerspricht (für kleine Rotationsquantenzahlen).

Hier wird das Problem aus Sicht der Quantenmechanik neu angegangen.¹ Es wird dann notwendig, unsere Entwicklung in Bezug auf $(m/M)^{1/4}$ statt in Bezug auf $\sqrt{m/M}$, um die natürliche Ordnung der Energieterme zu erhalten. Die Überlegungen werden auch viel einfacher und transparenter als in der alten Theorie. Die Kernschwingungen entsprechen Termen zweiter Ordnung und die Rotationen vierten Ordnung in der Energie, während die Terme erster und dritter Ordnung verschwinden. Das Fehlen der Terme erster Ordnung hängt mit der Existenz einer Gleichgewichtsposition der Kerne zusammen, in der die elektronische Energie stationärer Kerne minimal ist. Die Terme vierter Ordnung der Rotationsbewegung veranschaulichen die Verallgemeinerung der Behandlung von Kramers und Pauli [2] wobei das Verhalten eines Moleküls mit dem eines Tops mit eingebautem Schwungrad verglichen wird. Um die Eigenfunktionen und damit die Übergangswahrscheinlichkeiten nur zur nullten Näherung zu bestimmen, muss die Energieberechnung nach Termen vierten Ordnungen (Rotationen) durchgeführt werden. Man erhält Ausdrücke für die Wahrscheinlichkeiten gleichzeitiger Sprünge der elektronischen, schwingungs- und rotatorischen Quantenzahl, durch die die von Franck entwickelten Darstellungen [3] und von Condon weiter ausgeführt [4] kann eine genaue Interpretation erhalten.

Ursprünglich veröffentlicht als Annalen der Physik, 84, 457-484 (1927)

Übersetzt von S M Blinder mit Änderungen von Brian Sutcliffe und Wolf Geppert

¹Durch die Diskussion der Grundlagen dieser Arbeit mit uns hat uns Dr. P. Jordan mit wertvollen Kommentaren geholfen, für die wir uns danken.

Die Annäherungen höher als vierter Ordnung werden in diesem Werk nicht behandelt; sie entsprechen der Kopplung der drei grundlegenden Bewegungsarten. Eine Berechnung dieses Effekts ist nur für die gleichzeitige Betrachtung aller Degenerationen der elektronischen Bewegung für stationäre Kerne, insbesondere der Heisenberg-Resonanzdegeneration, die aus der Äquivalenz von Elektronen (möglicherweise auch einiger Kerne) entsteht, und in zweiatomigen Molekülen aus der Entartung der Eigenrotation um die internukleare Achse sinnvoll; Diese komplizierten Überlegungen werden hier vernachlässigt.

Als Beispiel betrachten wir diatomische Moleküle im Detail, nicht nur mit der allgemeinen Methode, sondern auch mit einer anderen, die die Trennung der Variablen nutzt, bei der die Rotation selbst in der Näherung der nullten Ordnung signifikant wird, wie Born und Hückel [5] Ich habe es in der älteren Quantentheorie gemacht.

## Teil I. Notation und Definitionen

Wir bezeichnen die Masse und rechteckige Koordinaten der Elektronen mit $m, x_k, y_k, z_k$ und der Kerne durch $M_l, X_l, Y_l, Z_l$. Vermietung $M$ sei ein beliebiger Durchschnittswert von $M_l$, setzen wir

$$\kappa = \left(\frac{m}{M}\right)^{1/4} \tag{1}$$

und

$$M_l = \frac{M}{\mu_l} = \frac{m}{\kappa^4 \mu_l}; \tag{2}$$

die $\mu_l$ als dimensionslose Zahlen von der Größenordnung 1. Sei die potenzielle Energie des Systems als

$$U(x_1, y_1, z_1, x_2, y_2, z_2, \dots; X_1, Y_1, Z_1, X_2, Y_2, Z_2, \dots) = U(x, X) \tag{3}$$

wobei wir mit bezeichnen $x$ die Gesamtheit der elektronischen Koordinaten und durch $X$, die der nuklearen Koordinaten. Die Funktion $U$ hängt nur von den relativen Positionen der Teilchen ab; allerdings verwenden wir seine spezielle Form (Coulombs Gesetz) nicht. Die kinetische Energie der Elektronen wird durch den Operator dargestellt

$$T_E = -\frac{h^2}{8\pi^2 m} \sum_x \sum_k \frac{\partial^2}{\partial x_k^2} \tag{4}$$

wobei das Symbol $\sum_x$ bezeichnet die Summe, die sich aus dem obigen Ausdruck durch zyklische Permutation von ergibt $x, y$ und $z$.

Die kinetische Energie der Kerne ist

$$T_K = -\kappa^4 \frac{h^2}{8\pi^2 m} \sum_x \sum_l \mu_l \frac{\partial^2}{\partial X_l^2}. \tag{5}$$

Die Gesamtenergie wird durch den Operator dargestellt

$$H = H_0 + \kappa^4 H_1 \tag{6}$$

wobei

$$T_E + U = H_0 \left(x, \frac{\partial}{\partial x}; X\right)$$

$$T_K = \kappa^4 H_1 \left(\frac{\partial}{\partial X}\right). \tag{7}$$

Wir führen nun anstelle der rechteckigen Koordinaten der Kerne ein, $3N - 6$ Funktionen

$$\xi_i = \xi_i(X) \tag{8}$$

2

die die relativen Positionen der Kerne zueinander bezeichnen, und 6 Funktionen

$$\theta_i = \theta_i(X) \tag{9}$$

die die Position und Ausrichtung der Kernkonfiguration im Weltraum bestimmen. Man kann die rechteckigen Koordinaten symmetrisch einführen $\bar{X}_l$, $\bar{Y}_l$, $\bar{Z}_l$ der Kerne relativ zu den momentanen Hauptträgheitsachsen; Zwischen diesen gibt es 6 Relationen:

$$\sum_l M_l \bar{X}_l = 0 \cdots \sum_l M_l \bar{Y}_l \bar{Z}_l = 0 \cdots$$

Man kann somit die $\bar{X}_l$ durch die $3N - 6$ unabhängige Parameter $\xi_1, \xi_2, \ldots$:

$$\bar{X}_l = \bar{X}_l(\xi), \ldots$$

Es existieren dann Transformationen zwischen der ursprünglichen und der neuen Koordinate der Form

$$X_l = X_0 + \sum_y \alpha_{xy}(\theta, \phi, \psi) \bar{Y}_l(\xi); \tag{10}$$

$X_0, Y_0, Z_0$ sind die Koordinaten des Massenmittelpunkts und der $\alpha_{xy}$ sind die Koeffizienten der orthogonalen Rotationsmatrix und sind somit bekannte Funktionen der Eulerschen Winkel $\theta, \phi, \psi$. Die Größen $X_0, Y_0, Z_0, \theta, \phi, \psi$ sind die Funktionen bezeichnet durch $\theta_i$ in (9). Durch (10) gilt die $X_l$ sind als Funktionen von bestimmt $\theta_i$ und $\xi_i$; durch Lösen erhält man die Ausdrücke (8) und (9).$^2$

Diese Transformation trennt die Energie natürlich nicht $H$ in Teile, die der Translation, Rotation und Relativbewegung der Kerne entsprechen. Man kann jedoch trennen $H_1$ In drei Teile:

$$H_1 = H_{\xi\xi} + H_{\xi\theta} + H_{\theta\theta}; \tag{11}$$

$H_{\xi\xi}$ linear homogen in der $\frac{\partial^2}{\partial \xi_i \partial \xi_j}$; $H_{\xi\theta}$ enthält die $\frac{\partial}{\partial \xi_i}$; $H_{\theta\theta}$ unabhängig von allen Ableitungen bezüglich der $\xi_i$. Man kann weitere Verallgemeinerungen über diese Operatoren anstellen. Wenn wir den gesamten Operator anwenden $H_1$ zu einer beliebigen Funktion $f(\xi)$ der relativen Kernkoordinaten $\xi_i$, die resultierende Größe $H_1 f(\xi)$ muss unabhängig von der Position im Raum sein, daher von $\theta_i$. Insbesondere gilt in $H_{\xi\xi}$ die Koeffizienten der $\frac{\partial^2}{\partial \xi_i \partial \xi_j}$ Kann sich nicht auf die $\theta_i$. Im Gegensatz dazu erscheinen diese in $H_{\xi\theta}$, assoziiert mit der $\frac{\partial}{\partial \xi_i}$, die $\xi_i$, $\theta_i$ und $\frac{\partial}{\partial \theta_i}$; in $H_{\theta\theta}$ Verbunden mit $\frac{\partial^2}{\partial \theta_i \partial \theta_j}$ die $\frac{\partial}{\partial \theta_i}$, $\xi_i$ und $\theta_i$.

Wir werden diese Operatoren explizit für diatomische Moleküle betrachten.

Das mechanische Problem, das wir lösen müssen, ist

$$(H_0 + \kappa^4 H_1 - W)\psi = 0. \tag{12}$$

Wir werden zeigen, dass jede beliebige Lösung, die einer Kombination von Kernen und Elektronen entspricht, die ein stabiles Molekül bilden, durch eine Entwicklung in einer Potenzreihe in $\kappa$.

# Teil II. Elektronische Bewegung für stationäre Kerne

Wenn man setzt $\kappa = 0$ in (12) erhält man eine Differentialgleichung in der $x_k$ allein, die $X_l$ erscheinen als Parameter:

$$\left\{ H_0 \left( x, \frac{\partial}{\partial x}; X \right) - W \right\} \psi = 0. \tag{13}$$

$^2$Es ist physikalisch bedeutsam, dass diese Lösung im Allgemeinen mit mehrdeutigen Funktionen hergestellt wird; Vergleich [6].

3

Dies stellt die elektronische Bewegung für stationäre Kerne dar. Wir nehmen an, dass dieses Eigenwertproblem gelöst ist. Die Eigenwerte hängen nur von den Funktionen ab $\xi_i$ der $X_i$; Dann kann man das Koordinatensystem verwenden, das durch die Hauptträgheitsachsen definiert ist, d. h. sei $X_i = \bar{X}_i(\xi)$. In diesem Achsensystem hängen die Eigenfunktionen ab, außer von $x_k$, nur auf der $\xi_i$; wenn man jedoch zurück zu den beliebigen raumfesten Achsen transformiert, gilt die $\theta_i$ Mach dich wieder dabei.

Wir benennen die $n$th Eigenwert und die entsprechende normalisierte Eigenfunktion als

$$W = V_n(\xi) \quad \psi = \phi_n(x; \xi, \theta) \tag{14}$$

so dass die Identität

$$\left\{ H_0 \left( x, \frac{\partial}{\partial x}; \xi, \theta \right) - V_n(\xi) \right\} \phi_n(x; \xi, \theta) = 0 \tag{15}$$

ist gültig. Hier nehmen wir an, dass $V_n$ ist ein nichtentarteter Eigenwert. Tatsächlich ist dies nie der Fall, da die Ununterscheidbarkeit der Elektronen die Resonanzentartung einführt, die von Heisenberg und Dirac entdeckt wurde; Für zweiatomige Moleküle gibt es eine zusätzliche Entartung des Drehimpulses um die Achse. Da wir uns hier jedoch nur mit der Systematik des Approximationsverfahrens beschäftigen, werden wir diese Entartungen nicht betrachten. Ihre Betrachtung würde zu säkularen Gleichungen in der höheren Approximation führen.

Das wichtigste Ziel unserer Untersuchung ist der Nachweis, dass die Funktion $V_n(\xi)$ die Rolle eines Potentials für die nukleare Bewegung spielt. Dafür müssen wir mehrere Hilfsformeln haben, die jetzt abgeleitet werden. Es ist notwendig zu zeigen, dass die Matrix, die der Ableitung des Operators entspricht, die der Ableitung entspricht $H_0(x, \frac{\partial}{\partial x}; \xi, \theta)$ bezüglich $\xi_i$, (für konstante $x, \frac{\partial}{\partial x}$) kann mit der Ableitung der Funktion in Beziehung gesetzt werden $V_n(\xi)$.

Anstatt die Ableitung bezüglich der $\xi_i$ direkt ersetzen wir das $\xi_i$ von $\xi_i + \kappa\zeta_i$ und differenzieren bezüglich $\kappa$; der Koeffizient einer Potenz von $\kappa$ ist dann ein homogenes Polynom in $\zeta_i$, diese Koeffizienten sind Ableitungen bezüglich von $\xi_i$. So schreiben wir

$$V_n(\xi + \kappa\zeta) = V_n^{(0)} + \kappa V_n^{(1)} + \kappa^2 V_n^{(2)} + \dots, \tag{16}$$

wobei

$$\begin{array}{l} \text{a)} \quad V_n^{(0)} = V_n(\xi) \\ \text{b)} \quad V_n^{(1)} = \sum_i \zeta_i \frac{\partial V_n}{\partial \xi_i} \\ \text{c)} \quad V_n^{(2)} = \frac{1}{2} \sum_{ij} \zeta_i \zeta_j \frac{\partial^2 V_n}{\partial \xi_i \partial \xi_j}, \end{array} \tag{17}$$

...

und entsprechend

$$\begin{array}{l} H_0 = H_0^{(0)} + \kappa H_0^{(1)} + \kappa^2 H_0^{(2)} + \dots \\ \phi_n = \phi_n^{(0)} + \kappa \phi_n^{(1)} + \kappa^2 \phi_n^{(2)} + \dots \\ \dots \dots \dots \dots \dots \end{array} \tag{18}$$

Man kann nun die Mengen entwickeln $\phi_n^{(1)}, \phi_n^{(2)}$ in den Eigenfunktionen $\phi_n^{(0)}(x; \xi, \theta)$, Einstellung

$$\begin{array}{l} \text{a)} \quad \phi_n^{(1)} = \sum_{n'} u_{nn'}^{(1)} \phi_{n'}^{(0)}, \\ \text{b)} \quad \phi_n^{(2)} = \sum_{n'} u_{nn'}^{(2)} \phi_{n'}^{(0)}. \end{array} \tag{19}$$

4

Daher $u_{nn'}^{(r)}$ ist ein homogenes Polynom von $r$Th. Ordnung in $\zeta_i$, zum Beispiel

$$u_{nn'}^{(1)} = \sum_i \zeta_i \int \overline{\phi_{n'}^{(0)}} \frac{\partial \phi_n^{(0)}}{\partial \xi_i} \mathrm{d}x$$

$$u_{nn'}^{(2)} = \sum_{ij} \zeta_i \zeta_j \int \overline{\phi_{n'}^{(0)}} \frac{\partial^2 \phi_n^{(0)}}{\partial \xi_i \partial \xi_j} \mathrm{d}x. \tag{20}$$

Diese Integrale, in denen $\mathrm{d}x$ bezeichnet das Volumenelement im Konfigurationsraum, sind unabhängig von der Orientierung des Kernsystems im Raum, also unabhängig von der $\theta_i$; man kann sie somit im Hauptachsensystem bewerten.

Wenn jetzt, $F$ bezeichnet einen beliebigen Operator auf der $x_i$, definieren wir das $r$Matrixelement der Th-Ordnung $F$

$$\int \overline{\phi_{n'}^{(0)}} F \phi_n^{(r)} \mathrm{d}x = F_{nn'}^{(r)}. \tag{21}$$

Für $r = 0$ dies wird zum üblichen Matrixelement

$$F_{nn'}^{(0)} = F_{nn'} = \int \overline{\phi_{n'}^{(0)}} F \phi_n^{(0)} \mathrm{d}x. \tag{22}$$

Im Allgemeinen gilt durch (19)

$$F_{nn'}^{(r)} = \sum_{n''} u_{nn''}^{(r)} F_{n''n'}. \tag{23}$$

Verwendung von (15) für $\kappa = 0$

$$(H_0^{(0)} - V_n^{(0)})_{nn'}^{(r)} = u_{nn'}^{(r)} (V_{n'}^{(0)} - V_n^{(0)}). \tag{24}$$

Außerdem erhalten wir durch das Einsetzen von (16) und (18) in (15) folgende Identitäten:

a) $(H_0^{(0)} - V_n^{(0)})\phi_n^{(1)} + (H_0^{(1)} - V_n^{(1)})\phi_n^{(0)} = 0$

b) $(H_0^{(0)} - V_n^{(0)})\phi_n^{(2)} + (H_0^{(1)} - V_n^{(1)})\phi_n^{(1)} + (H_0^{(2)} - V_n^{(2)})\phi_n^{(0)} = 0$

...

Multipliziere diese mit $\overline{\phi_{n'}^{(0)}}$ und integrieren über die $x_i$, aufgrund von (24) finden wir:

a) $u_{nn'}^{(1)}(V_{n'}^{(0)} - V_n^{(0)}) + (H_0^{(1)})_{nn'} - V_n^{(1)}\delta_{nn'} = 0$

b) $u_{nn'}^{(2)}(V_{n'}^{(0)} - V_n^{(0)}) + (H_0^{(1)} - V_n^{(1)})_{nn'} + (H_0^{(2)})_{nn'} - V_n^{(2)}\delta_{nn'} = 0$

...

Aus diesen kann man die $(H_0^{(1)})_{nn'}$, $(H_0^{(2)})_{nn'}$, ..., $i$e Die Matrixelemente $\left(\frac{\partial H_0}{\partial \xi_i}\right)_{nn'}$, $\left(\frac{\partial^2 H_0}{\partial \xi_i \partial \xi_j}\right)_{nn'}$, ... Wir werden diese Formeln später anwenden.$^3$

### Teil III. Aufstellung der Approximativen Gleichungen

Eine beliebige Konfiguration von Elektronen und Kerne kann nicht immer durch ein allgemeines Näherungsverfahren behandelt werden. Wir betrachten hier nur Zustände, die einem stabilen Molekül entsprechen. Wir beginnen mit folgender Frage:

$^3$Das klassische Analogon zur einfachsten Deduktion aus diesen Formeln, nämlich der Identität $(H_0^{(1)})_{nn} = V_n^{(1)}$ was aus (26a) folgt für $n = n'$, findet sich in [7]; Vergleichen Sie insbesondere mit § 4, Formel (11).

5

Gibt es ein System von Werten der relativen Kernkoordinaten? $\xi_i$ so dass die Eigenfunktionen $\psi_n$ des Energieoperators (6), insofern sie von der $\xi_i$, Werte haben, die sich signifikant von Null unterscheiden, nur in einer kleinen Umgebung dieser Menge?

Diese wellenmechanische Anforderung entspricht offensichtlich der klassischen Bedingung, dass die Kerne nur kleine Schwingungen um die Gleichgewichtskonfiguration durchlaufen; die $|\psi_n|^2$ ist die Wahrscheinlichkeit, eine bestimmte Konfiguration gegebener Energie zu finden.

Wir betrachten als das ungestörte System die elektronische Bewegung für eine beliebige, aber fortan feste Kernkonfiguration, $\xi_i$. Wir entwickeln dann alle Größen bezüglich kleiner Änderungen der $\xi_i$, die wir bezeichnen durch $\kappa\zeta_i$; Wir nehmen dann an, dass der "Bereich" der Oszillation so ist, dass $\kappa$ nahe an null liegt, eine Annahme, die nur durch ihren Erfolg gerechtfertigt ist.

Wir haben dann wie in (18), Teil II, die Entwicklung

$$H_0(x, \frac{\partial}{\partial x}; \xi + \kappa\zeta, \theta) = H_0^{(0)} + \kappa H_0^{(1)} + \kappa^2 H_0^{(2)} + \dots, \tag{27}$$

wobei

$$a) \quad H_0^{(0)} = H_0(x, \frac{\partial}{\partial x}; \xi),$$

$$b) \quad H_0^{(1)} = \sum_i \zeta_i \frac{\partial H_0}{\partial \xi_i}, \tag{28}$$

$$c) \quad H_0^{(2)} = \frac{1}{2} \sum_{ij} \zeta_i \zeta_j \frac{\partial^2 H_0}{\partial \xi_i \partial \xi_j},$$

und aus (11) seitdem $\frac{\partial}{\partial \xi} = \frac{1}{\kappa} \frac{\partial}{\partial \zeta}$

$$\kappa^4 H_1(X, \frac{\partial}{\partial X}) = \kappa^4 \left( \frac{1}{\kappa^2} H_{\zeta\zeta} + \frac{1}{\kappa} H_{\zeta\theta} + H_{\theta\theta} \right) \tag{29}$$

$$= \kappa^2 H_{\zeta\zeta}^{(0)} + \kappa^3 \left( H_{\zeta\theta}^{(0)} + H_{\zeta\zeta}^{(1)} \right) + \kappa^4 \left( H_{\theta\theta}^{(0)} + H_{\zeta\theta}^{(1)} + H_{\zeta\zeta}^{(2)} \right) + \dots$$

wobei

$$a) \quad H_{\zeta\zeta}^{(0)} = H_{\zeta\zeta}^{(0)}(\xi, \frac{\partial^2}{\partial \zeta_i \partial \zeta_j})$$

$$b) \quad H_{\zeta\zeta}^{(1)} = \sum_i \zeta_i \frac{\partial H_{\zeta\zeta}^{(0)}}{\partial \xi_i} \tag{30}$$

$$a) \quad H_{\zeta\theta}^{(0)} = H_{\zeta\theta}^{(0)}(\xi, \theta, \frac{\partial}{\partial \zeta}, \frac{\partial}{\partial \theta})$$

$$b) \quad H_{\zeta\theta}^{(1)} = \sum_i \zeta_i \frac{\partial H_{\zeta\theta}^{(0)}}{\partial \xi_i} \tag{31}$$

$$a) \quad H_{\theta\theta}^{(0)} = H_{\theta\theta}^{(0)}(\xi, \theta, \frac{\partial^2}{\partial \theta_i \partial \theta_j})$$

$$b) \quad H_{\theta\theta}^{(1)} = \sum_i \zeta_i \frac{\partial H_{\theta\theta}^{(0)}}{\partial \xi_i} \tag{32}$$

6

Die Argumente $\xi_i$ sind fortan als Konstanten zu betrachten.

Der Gesamtenergieoperator ist dann

$$\begin{array}{l} H = H_0 + \kappa H_0^{(1)} + \kappa^2 \left(H_0^{(2)} + H_{\zeta\zeta}^{(0)}\right) \\ + \kappa^3 \left(H_0^{(3)} + H_{\zeta\theta}^{(0)} + H_{\zeta\zeta}^{(1)}\right) \\ + \kappa^4 \left(H_0^{(4)} + H_{\theta\theta}^{(0)} + H_{\zeta\theta}^{(1)} + H_{\zeta\zeta}^{(2)}\right) + \dots \end{array} \tag{33}$$

Die nachfolgenden Terme haben alle die gleiche Form und können aus dem Term in gebildet werden $\kappa^4$ durch Erhöhung des hochgestellten Index um 1.

Wir entwickeln außerdem die gewünschte Eigenfunktion und den Energieparameter bezüglich $\kappa$ :

$$\begin{array}{l} \psi = \psi^{(0)} + \kappa\psi^{(1)} + \kappa^2\psi^{(2)} + \dots \\ W = W^{(0)} + \kappa W^{(1)} + \kappa^2 W^{(2)} + \dots \end{array} \tag{34}$$

Wir erhalten dann die folgenden Approximationsgleichungen:

$$\begin{array}{l} a) \quad (H_0^{(0)} - W^{(0)})\psi^{(0)} = 0 \\ b) \quad (H_0^{(0)} - W^{(0)})\psi^{(1)} = (W^{(1)} - H_0^{(1)})\psi^{(0)} \\ c) \quad (H_0^{(0)} - W^{(0)})\psi^{(2)} = (W^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)})\psi^{(0)} + (W^{(1)} - H_0^{(1)})\psi^{(1)} \\ d) \quad (H_0^{(0)} - W^{(0)})\psi^{(3)} = (W^{(3)} - H_0^{(3)} - H_{\zeta\theta}^{(0)} - H_{\zeta\zeta}^{(1)})\psi^{(0)} \\ \quad + (W^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)})\psi^{(1)} + (W^{(1)} - H_0^{(1)})\psi^{(2)} \end{array} \tag{35}$$

$$e) \quad (H_0^{(0)} - W^{(0)})\psi^{(4)} = (W^{(4)} - H_0^{(4)} - H_{\theta\theta}^{(0)} - H_{\zeta\theta}^{(1)} - H_{\zeta\zeta}^{(2)})\psi^{(0)} \\ \quad + (W^{(3)} - H_0^{(3)} - H_{\zeta\theta}^{(0)} - H_{\zeta\zeta}^{(1)})\psi^{(1)} \\ \quad + (W^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)})\psi^{(2)} + (W^{(1)} - H_0^{(1)})\psi^{(3)} \\ \dots \dots \dots \dots \dots \dots$$

### Teil IV. Lösung der Approximativen Gleichungen von nullter und erster Ordnung: Gleichgewicht der Kerne

Die Gleichung der nullten Ordnung (35a) beschreibt die elektronische Bewegung für stationäre Kerne, wie sie in Teil II behandelt wird. Aus der normalisierten Eigenlösung $\phi_n^{(0)}(x; \xi, \theta)$ die zum Eigenwert gehören $V_n^{(0)} = V_n(\xi)$, finden wir die allgemeine Lösung in der Form:

$$\psi_n^{(0)} = \chi_n^{(0)}(\zeta, \theta)\phi_n^{(0)}(x; \xi, \theta) \tag{36}$$

wobei $\chi_n^{(0)}$ ist eine bislang willkürliche Funktion der Argumente $\zeta_i, \theta_j$; dies muss einbezogen werden, um Lösungen der folgenden Näherungsgleichungen zu ermöglichen.

Die folgende Näherungsgleichung (35b)

$$(H_0^{(0)} - W^{(0)})\psi^{(1)} = (W^{(1)} - H_0^{(1)})\psi^{(0)} \tag{37}$$

ist nur dann löslich, wenn die rechte Seite orthogonal zu ist $\psi_n^{(0)}$ (relativ zu den elektronischen Koordinaten $x_i$).$^4$

Dies ergibt die Bedingung

$$\left\{\left(H_0^{(1)}\right)_{nn} - W^{(1)}\right\}\chi_n^{(0)}(\zeta, \theta) = 0 \tag{38}$$

$^4$Wir definieren die Orthogonalität zweier Funktionen $f(x)$ und $g(x)$ von $\int \overline{f(x)}g(x)\mathrm{d}x = 0$.

7

wobei $\left(H_{0}^{(1)}\right)_{nn}$ ist das diagonale Matrixelement des Operators $H_{0}^{(1)}$ relativ zu den $x_{i}$, somit durch (28b) eine homogene lineare Funktion von $\zeta_{i}$. Dies muss jedoch gemäß (38) konstant sein, da $\chi_{n}^{(0)}(\zeta,\theta)$ kann nicht identisch verschwinden, ohne dass dasselbe gilt für $\psi_{n}^{(0)}$.

Daraus folgt, dass

$$W^{(1)} = 0, \quad \left(H_{0}^{(1)}\right)_{nn} = 0. \tag{39}$$

Aus (26a) und (17) haben wir jedoch

$$\left(H_{0}^{(1)}\right)_{nn} = V_{n}^{(1)} = \sum_{i} \zeta_{i} \frac{\partial V_{n}}{\partial \xi_{i}}.$$

Also:

$$\frac{\partial V_{n}}{\partial \xi_{i}} = 0. \tag{40}$$

Die Gültigkeit der Fortsetzung unseres Approximationsverfahrens erfordert, dass die relativen nuklearen Koordinaten $\xi_{i}$ darf nicht willkürlich gewählt werden, sondern muss einem Extremum der elektronischen Energie entsprechen $V_{n}(\xi)$. Die Existenz dieses Gesetzes ist daher die Voraussetzung für die Existenz des Moleküls, ein Gesetz, das üblicherweise als selbstverständlich angenommen wird. Wir werden später zeigen, dass es notwendigerweise auch ein Minimum sein muss.

Die Funktion $\chi_{n}^{(0)}(\zeta,\theta)$ bleibt noch unbestimmt. Setting in (37) $W_{n}^{(0)} = V_{n}(\xi)$, $W_{n}^{(1)} = 0$ und $\psi_{n}^{(0)} = \chi_{n}^{(0)}\phi_{n}^{(0)}$ Wir finden die Gleichung, die bestimmt $\phi_{n}^{(1)}$

$$\left(H_{0}^{(0)} - V_{n}^{(0)}\right)\psi_{n}^{(1)} = -H_{0}^{(1)}\phi_{n}^{(0)}\chi_{n}^{(0)}. \tag{41}$$

Eine Lösung davon durch (25a) ist $\psi_{n}^{(1)} = \chi_{n}^{(0)}\phi_{n}^{(1)}$ wobei $\phi_{n}^{(1)}$ ist die Funktion (19a), die durch (18) definiert ist. Die allgemeine Lösung erhält man durch das Hinzufügen einer Lösung $\phi_{n}^{(0)}$ der homogenen Gleichung mit dem noch nicht bestimmten Faktor $\chi_{n}^{(1)}(\xi,\theta)$:

$$\psi_{n}^{(1)} = \chi_{n}^{(0)}\phi_{n}^{(1)} + \chi_{n}^{(1)}\phi_{n}^{(0)}. \tag{42}$$

### Teil V. Lösung der approximativen Gleichungen zweiter und dritter Ordnung: Kernschwingung

Wir erreichen nun die Approximationsgleichung (35c), die nach der Substitution der Lösungen für die niedrigeren Approximationen so lautet

$$\begin{array}{l} \left(H_{0}^{(0)} - V_{n}^{(0)}\right)\psi_{n}^{(2)} = \left(W_{n}^{(2)} - H_{0}^{(2)} - H_{\zeta\zeta}^{(0)}\right)\chi_{n}^{(0)}\phi_{n}^{(0)} \\ \quad - H_{0}^{(1)}\left(\chi_{n}^{(0)}\phi_{n}^{(1)} + \chi_{n}^{(1)}\phi_{n}^{(0)}\right). \tag{43} \end{array}$$

Damit dies lösbar ist, muss die rechte Seite wieder orthogonal zu sein $\phi_{n}^{(0)}$; unter Verwendung der Notation von Teil II ergibt dies aufgrund von (39):

$$\left\{\left(H_{0}^{(2)} + H_{\zeta\zeta}^{(0)}\right)_{nn} + \left(H_{0}^{(1)}\right)_{nn} - W_{n}^{(2)}\right\}\chi_{n}^{(0)} = 0.$$

Sie folgt aus (26b) mit $V_{n}^{(1)} = 0$ dass

$$\left(H_{0}^{(2)}\right)_{nn} + \left(H_{0}^{(1)}\right)_{nn}^{(1)} = V_{n}^{(2)}. \tag{44}$$

Da $H_{\zeta\zeta}^{(0)}$ durch (30a) gilt als unabhängig von $x_{k}$ Wir finden:

$$\left\{H_{\xi\xi}^{(0)} + V_{n}^{(2)} - W_{n}^{(2)}\right\}\chi_{n}^{(0)} = 0. \tag{45}$$

Beachten Sie die Bedeutungen von $H_{\zeta\zeta}^{(0)}$ und $V_{n}^{(2)}$ Gegeben durch (17c) und (30a) sehen wir, dass (45) die Gleichung für die harmonische Kernschwingung darstellt:

$$\left\{H_{\zeta\zeta}^{(0)}\left(\xi_{i}\frac{\partial^{2}}{\partial\zeta_{i}\partial\zeta_{j}}\right) + \frac{1}{2}\sum_{ij}\zeta_{i}\zeta_{j}\frac{\partial^{2}V_{n}}{\partial\xi_{i}\partial\xi_{j}} - W_{n}^{(2)}\right\}\chi_{n}^{(0)} = 0. \tag{46}$$

8

Diese Gleichung zeigt, dass die Funktion $V_n(\xi)$ übernimmt die Rolle einer potenziellen Energie für die Kerne, bis auf Terme zweiter Ordnung. Für die Existenz eines stabilen Moleküls gibt es eine weitere Bedingung, dass das Extremum von $V_n(\xi)$ bestimmt durch (40) muss ein Minimum sein; dann die quadratische Form $V_n^{(2)}$ müssen positiv definit sein, damit alle Freiheitsgrade $\zeta_i$ stabil und um die Gleichgewichtskonfiguration oszillierend sind möglich. Es ist bekannt, dass die Gleichung für die Schwingung (46) durch eine lineare Transformation der $\zeta_i$ zu normalen Koordinaten $\eta_i$. Wenn $\sigma_{ns}^{(0)}(\zeta)$ sei die normierte Eigenlösung von (46), die zum Eigenwert gehört $W_{ns}^{(2)}$, die allgemeine Lösung ist

$$\begin{array}{l} a) \quad W^{(2)} = W_{ns}^{(2)}, \quad \chi_n^{(0)} = \chi_{ns}^{(0)}, \text{ where} \\ b) \quad \chi_{ns}^{(0)} = \rho_{ns}^{(0)}(\theta)\sigma_{ns}^{(0)}(\zeta). \end{array} \tag{47}$$

Der Index $s$ stellt somit die Menge der Schwingungsquantenzahlen dar. $\rho_{ns}^{(0)}$ ist eine bislang unbestimmte Funktion der $\theta_i$, deren Einführung für die Fortsetzung des Verfahrens notwendig ist.

Es ist bekannt, dass $\sigma_{ns}^{(0)}(\zeta)$ ist eine lineare Kombination von Produkten orthogonaler Hermite-Funktionen für die einzelnen normalen Koordinaten $\eta_i$; Diese Funktionen haben die Eigenschaft, dass sie sehr schnell (exponentiell) außerhalb des Grenzwerts der klassischen Schwingung gegen Null nähern. Unsere Substitution von $(\xi + \kappa\zeta)$ gerechtfertigt ist, da es tatsächlich zu einer Lösung führt, bezüglich der $\xi$-Oszillation innerhalb der Grenze, die verschwinden mit $\kappa$. Wir wenden die weitere Eigenschaft der orthogonalen Hermite-Funktionen an, dass sie entweder gerade oder ungerade Funktionen ihres Arguments sind.

Lass $\Phi$ sei ein beliebiger Operator auf der $\zeta_i$. Wir können dann die entsprechende Matrix konstruieren

$$\Phi_{nn'}_{ss'} = \int \overline{\sigma_{n's'}^{(0)}}\Phi\sigma_{ns}^{(0)}\mathrm{d}\zeta \tag{48}$$

wobei $\mathrm{d}\zeta$ ist das Volumenelement im Raum von $\zeta_i$.

Um die Gleichung (43) zu lösen, setzen wir auf der rechten Seite mit (45) ein,

$$\left(W_{ns}^{(2)} - H_{\zeta\zeta}^{(0)}\right)\chi_{ns}^{(0)} = V_n^{(2)}\chi_{ns}^{(0)};$$

(43) wird dann:

$$\left(H_0^{(0)} - V_n^{(0)}\right)\psi_n^{(2)} = \left(V_n^{(2)} - H_0^{(2)}\right)\chi_{ns}^{(0)}\phi_n^{(0)} - H_0^{(1)}\left(\chi_{ns}^{(0)}\phi_n^{(1)} + \chi_{ns}^{(1)}\phi_n^{(0)}\right). \tag{49}$$

Die allgemeine Lösung lautet

$$\psi_n^{(2)} = \chi_{ns}^{(0)}\phi_n^{(2)} + \chi_{ns}^{(1)}\phi_n^{(1)} + \chi_{ns}^{(2)}\phi_n^{(0)}, \tag{50}$$

wobei $\chi_{ns}^{(2)}$ bezeichnet eine neue, unbestimmte Funktion der $\zeta_i, \theta_i$; Dies lässt sich leicht anhand der Identitäten (25) überprüfen.

Wir betrachten nun die Approximationsgleichung dritter Ordnung (35d); Nach der Substitution der bereits bestimmten Größen ergibt sich:

$$\begin{array}{l} \left(H_0^{(0)} - V_n^{(0)}\right)\psi_n^{(3)} = \left(W^{(3)} - H_0^{(3)} - H_{\zeta\theta}^{(0)} - H_{\zeta\zeta}^{(1)}\right)\chi_{ns}^{(0)}\phi_n^{(0)} \\ + \quad \left(W_{ns}^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)}\right)\left(\chi_{ns}^{(0)}\phi_n^{(1)} + \chi_{ns}^{(1)}\phi_n^{(0)}\right) \\ - \quad H_0^{(1)}\left(\chi_{ns}^{(0)}\phi_n^{(2)} + \chi_{ns}^{(1)}\phi_n^{(1)} + \chi_{ns}^{(2)}\phi_n^{(0)}\right). \end{array} \tag{51}$$

Wir können die rechte Seite als Entwicklung in der $\phi_n^{(0)}$; Wir schreiben

$$\left(H_0^{(0)} - V_n^{(0)}\right)\psi_n^{(3)} = W^{(3)}\chi_{ns}^{(0)}\phi_n^{(0)} - \sum_{n'} F_{nn'}^{(3)}\phi_{n'}^{(0)}, \tag{52}$$

wobei

$$F_{nn'}^{(3)} = F_{nn'}^{(3,1)}\chi_{ns}^{(2)} + F_{nn'}^{(3,2)}\chi_{ns}^{(1)} + F_{nn'}^{(3,3)}\chi_{ns}^{(0)}; \tag{53}$$

9

wobei die $F$ sind Operatoren auf $\zeta$ und $\theta$, und

$$\begin{aligned} a) & F_{nn'}^{(3,1)} = \left(H_0^{(1)}\right)_{nn'} \\ b) & F_{nn'}^{(3,2)} = \left(H_{\zeta\zeta}^{(0)} - H_0^{(2)} - W_{ns}^{(2)}\right)_{nn'} + \left(H_0^{(1)}\right)_{nn'}^{(1)}, \end{aligned} \tag{54}$$

wir können sagen $F_{nn'}^{(3,3)}$ nur dass es sich um eine homogene Funktion dritten Grades in der $\xi_i$ und die $\partial/\partial\zeta_i$.

Wenn (52) auflösbar ist, müssen wir

$$W^{(3)}\chi_{ns}^{(0)} - F_{nn}^{(3)} = 0$$

wegen (53) und (54a)

$$F_{nn}^{(3,2)}\chi_{ns}^{(1)} = \left(W^{(3)} - F_{nn}^{(3,3)}\right)\chi_{ns}^{(0)}, \tag{55}$$

wobei durch (54b) und (44)

$$F_{nn}^{(3,2)} = H_{\zeta\zeta}^{(0)} - V_n^{(2)} - W_{ns}^{(2)}.$$

Somit ist (55) die inhomogene Gleichung, die der Schwingungsgleichung (45) entspricht; da (45) die normalisierte Lösung hat $\sigma_{ns}^{(0)}$ die zum Eigenwert gehören $W_{ns}^{(2)}$, (55) ist nur lösbar, wenn die rechte Seite mit multipliziert wird $\overline{\sigma_{ns}^{(0)}}$ hat ein verschwindendes Integral über $\zeta$-Weltraum. Dies ergibt unter Verwendung von (47b) eine Differentialgleichung für $\rho_{ns}^{(0)}(\theta)$:

$$\left(F_{\underset{ss}{nn}}^{(3,3)} - W^{(3)}\right)\rho_{ns}^{(0)} = 0.$$

Allerdings, $F_{nn}^{(3,3)}$ ist ungerade in der $\xi_i$ und $\partial/\partial\zeta_i$ so ist das diagonale Element der $\zeta$-Matrix muss verschwinden. Wenn man auf die normalen Koordinaten transformiert $\eta_i$, $\sigma_{ns}^{(0)}$ wird zu einer Summe von Produkten orthogonaler Hermite-Funktionen, $F_{nn}^{(3,3)}$, ein Polynom ungerade Ordnung in der $\eta_i$ und $\partial/\partial\eta_i$, so dass jeder Term mindestens einen von enthält. $\eta_i$ oder $\partial/\partial\eta_i$ in einer seltsamen Kraft; daher sind alle Terme in der $\zeta$-Matrix verschwindet. Daraus folgt

$$W^{(3)} = 0 \tag{56}$$

und $\rho_{ns}^{(0)}$ bleibt, wie zuvor, unbestimmt.

Nun können wir lösen:

$$\chi_{ns}^{(1)} = S_{ns}^{(1)}\rho_{ns}^{(0)} \tag{57}$$

wobei $S_{ns}^{(1)}$ ist der folgende Operator bezüglich der $\theta_i$:

$$S_{ns}^{(1)} = \sum_{s'}' \frac{F_{nn}^{(3,3)}\sigma_{ns'}^{(0)}}{W_{ns}^{(2)} - W_{ns'}^{(2)}}. \tag{58}$$

Schließlich die Lösung von (52):

$$\psi_n^{(3)} = \sum_{n'}' \frac{F_{nn}^{(3)}\phi_{n'}^{(0)}}{V_n^{(0)} - V_{n'}^{(0)}} \tag{59}$$

und nach (53) hat dies die Form:

$$\psi_n^{(3)} = \sum_{n'}' \left(G_{nn'}^{(3,1)}\chi_{ns}^{(2)}\phi_{n'}^{(0)} + G_{nn'}^{(3,2)}\chi_{ns}^{(1)}\phi_{n'}^{(0)} + G_{nn'}^{(3,3)}\chi_{ns}^{(0)}\phi_{n'}^{(0)}\right), \tag{60}$$

wobei

$$G_{nn'}^{(3,2)} = \frac{F_{nn'}^{(3,2)}}{V_n^{(0)} - V_{n'}^{(0)}}. \tag{61}$$

10

Beachten wir (54), dass wir sehen, dass $G_{nn'}^{(3,1)}$ ist eine Zahl, $G_{nn'}^{(3,2)}$ einen Differentialoperator bezüglich des $\zeta_i$ und $G_{nn'}^{(3,3)}$ ein Operator bezüglich der $\zeta_i$ und $\theta_i$.

Von (26a), Teil II

$$\begin{aligned} \sum_{n'}' G_{nn'}^{(3,1)} \chi_{ns}^{(2)} \phi_{n'}^{(0)} &= \sum \frac{(H_0^{(1)})_{nn'} \phi_{n'}^{(0)} \chi_{ns}^{(2)}}{V_n^{(0)} - V_{n'}^{(0)}} \\ &= \sum_{n'}' u_{nn'}^{(1)} \phi_{n'}^{(0)} \chi_{ns}^{(2)} \\ &= \phi_n^{(1)} \chi_{ns}^{(2)} \end{aligned}$$

Daher

$$\psi_n^{(3)} = \phi_n^{(1)} \chi_{ns}^{(2)} + \sum_{n'}' \left( G_{nn'}^{(3,2)} \chi_{ns}^{(1)} \phi_{n'}^{(0)} + G_{nn'}^{(3,3)} \chi_{ns}^{(0)} \phi_{n'}^{(0)} \right). \tag{62}$$

## Teil VI. Lösung der approximativen Gleichungen vierten und höheren Ordnungs: Rotations- und Kopplungseffekte

Nach der Substitution der bereits bestimmten Größen wird die Approximationsgleichung 4. Ordnung (35e):

$$\begin{aligned} \left( H_0^{(0)} - V_n^{(0)} \right) \psi_n^{(4)} &= \left( W^{(4)} - H_0^{(4)} - H_{\theta\theta}^{(0)} - H_{\zeta\theta}^{(1)} - H_{\zeta\zeta}^{(2)} \right) \chi_{ns}^{(0)} \phi_n^{(0)} \\ &\quad - \left( H_0^{(3)} + H_{\zeta\theta}^{(0)} + H_{\zeta\zeta}^{(1)} \right) \left( \chi_{ns}^{(1)} \phi_n^{(0)} + \chi_{ns}^{(0)} \phi_n^{(1)} \right) \\ &\quad + \left( W_{ns}^{(2)} - H_0^{(2)} - H_{\zeta\zeta}^{(0)} \right) \left( \chi_{ns}^{(2)} \phi_n^{(0)} + \chi_{ns}^{(1)} \phi_n^{(1)} + \chi_{ns}^{(0)} \phi_n^{(2)} \right) \\ &\quad - H_0^{(1)} \left\{ \phi_n^{(1)} \chi_{ns}^{(2)} + \sum_{n'}' \left( G_{nn'}^{(3,2)} \chi_{ns}^{(1)} \phi_{n'}^{(0)} + G_{nn'}^{(3,3)} \chi_{ns}^{(0)} \phi_{n'}^{(0)} \right) \right\}. \end{aligned} \tag{63}$$

Wir entwickeln erneut die rechte Seite in der $\phi_n^{(0)}$:

$$\left( H_0^{(0)} - V_n^{(0)} \right) \psi_n^{(4)} = W^{(4)} \chi_{ns}^{(0)} \phi_n^{(0)} - \sum_{n'}' F_{nn'}^{(4)} \phi_{n'}^{(0)}, \tag{64}$$

wobei

$$F_{nn'}^{(4)} = F_{nn'}^{(4,2)} \chi_{ns}^{(2)} + F_{nn'}^{(4,3)} \chi_{ns}^{(1)} + F_{nn'}^{(4,4)} \chi_{ns}^{(0)}; \tag{65}$$

Hier haben wir

$$F_{nn'}^{(4,2)} = \left( H_{\zeta\zeta}^{(0)} - H_0^{(2)} - W_{ns}^{(2)} \right)_{nn'} + \left( H_0^{(1)} \right)_{nn'}^{(1)} \tag{66}$$

und ist identisch mit $F_{nn'}^{(3,2)}$ (54b). Während $F_{nn'}^{(4,3)}$ ist ungerade Ordnung in der $\zeta_i, \partial/\partial\zeta_i$, $F_{nn'}^{(4,3)}$ ist von gleicher Ordnung. Die Integrierbarkeit von (64) erfordert:

$$W^{(4)} \chi_{ns}^{(0)} - F_{nn}^{(4)} = 0;$$

Das bedeutet, dass nach (65)

$$F_{nn}^{(4,2)} \chi_{ns}^{(2)} = \left( W^{(4)} - F_{nn}^{(4,4)} \right) \chi_{ns}^{(0)} - F_{nn}^{(4,3)} \chi_{ns}^{(1)}. \tag{67}$$

Die linke Seite stimmt erneut mit der Schwingungsgleichung (45) überein wegen (66). Die rechte Seite muss ebenfalls orthogonal zu sein $\sigma_{ns}^{(0)}$. Indem die Ausdrücke für eingesetzt werden $\chi_{ns}^{(0)}$ und $\chi_{ns}^{(1)}$ aus (47b) und (57), und mit dem Symbol

$$(\Phi)_{ss'}^{(1)} = \int \overline{\sigma_{ns}^{(0)}} \Phi S_{ns}^{(1)} \mathrm{d}\zeta = \sum_{s''}' \frac{\left[ \Phi F_{nn}^{(3,3)} \right]_{ss'}}{W_{ns}^{(2)} - W_{ns''}^{(2)}}, \tag{68}$$

11

finden wir

$$\left\{F_{ss}^{(4,4)} + \left(F_{nn}^{(4,3)}\right)_{ss}^{(1)} - W^{(4)}\right\} \rho_{ns}^{(0)} = 0. \tag{69}$$

Diese Gleichung bestimmt schließlich die Funktion $\rho_{ns}^{(0)}(\theta)$, daher die Bewegung der Hauptträgheitsachsen: die Translationen und Rotationen. Der Hauptterm des Operators in (69) ist derjenige, der die zweite Ableitung bezüglich der $\theta_i$; Ein Blick auf (63) zeigt, dass sie aus $H_{\theta\theta}^{(0)}\chi_{ns}^{(0)}\phi_n^{(0)}$, der Term entspricht in $F_{nn}^{(4,4)}$ zu

$$\left(\overline{H_{\theta\theta}^{(0)}}\right)_n = \int \overline{\phi_n^{(0)}} H_{\theta\theta}^{(0)}(\phi_n^{(0)} \dots) dx, \tag{70}$$

wobei wir an die Stelle der Punkte die Funktion einsetzen müssen, auf der bearbeitet wird. Da der Operator (70) unabhängig von der $\zeta_i$, sind die Diagonalelemente der entsprechenden s-Matrix mit ihr identisch. Physisch ist die Tatsache, dass die komplizierten Operatoren $\left(\overline{H_{\theta\theta}^{(0)}}\right)_n$ erscheinen anstelle der einfachen Operatoren $H_{\theta\theta}^{(0)}$ zeigt eine Kopplung zwischen der oberen Bewegung der Kerne und der elektronischen Bewegung an.

Dies sind, wie wir später im Fall des diatomischen Moleküls sehen werden, dieselben Effekte wie Kramers und Pauli [2] Sie haben versucht, dies mit der Annahme eines in der Spitze eingebauten 'Schwungrads' zu demonstrieren. Daher gibt es in (69) Terme, die zum Operator beitragen $H_{\zeta\theta}$; diese entsprechen einer Kopplung der oberen Bewegung mit Drehimpulsen, die eine Folge der Kernschwingung sind. Schließlich gibt es Begriffe, die die $\theta_I$; dies sind die Ergänzungen zur Schwingungsenergie der Ordnung $\kappa^4$.

Da die Translationen immer trivial getrennt werden können, betrachten wir nur die Rotationen. Wenn $r$ sei die Rotationsquantenzahl, so gilt für die Lösung von (70)

$$W^{(4)} = W_{nsr}^{(4)}; \quad \rho_{ns}^{(0)} = \rho_{nsr}^{(0)}(\theta). \tag{71}$$

Dann kann man (67) und schließlich auch (64) lösen. Es bringt nichts, die Formeln explizit aufzuschreiben.

Offensichtlich kann das Verfahren fortgesetzt werden; jedoch wird nichts Neues von Bedeutung erscheinen. Die höheren Approximationen beschreiben Kopplungen zwischen Rotationen, Schwingungen und elektronischen Bewegungen. Quantenzahlen, die nicht die bereits eingeführten sind, treten nicht ein.

Wir fassen nun die Folgen unserer Lösungen zusammen. Das offensichtlichste Ergebnis ist, dass zur vollständigen Bestimmung der Eigenfunktionen zur 0. Ordnung notwendig ist, die Approximationsdifferentialgleichungen in 4. Ordnung zu lösen; Wir haben

$$\psi_{nsr}(x, \zeta, \theta) = \phi_n^{(0)}(x, \xi, \theta) \sigma_{ns}^{(0)}(\zeta) \rho_{nsr}^{(0)}(\theta) + \dots \tag{72}$$

wobei $\phi_n^{(0)}$ ist die Eigenfunktion für elektronische Bewegung stationärer Kerne, $\sigma_{ns}^{(0)}$ dass für Kernschwingungen und $\rho_{nsr}^{(0)}$ Das ist für die Rotation. So sind die Schwingungskoordinaten definiert $\zeta_i$ aus einer Gleichgewichtskonfiguration $\xi_i$ was durch die Anforderung definiert ist, dass in dieser Konfiguration die elektronische Energie $V_n(\xi)$ ist ein Minimum. Die Bestimmung der drei Funktionen $\phi_n^{(0)}$, $\sigma_{ns}^{(0)}$ und $\rho_{nsr}^{(0)}$ ergeben Sie die Energie in 4. Ordnung:

$$W_{nsr} = V_n^{(0)} + \kappa^2 W_{ns}^{(2)} + \kappa^4 W_{nsr}^{(4)} + \dots; \tag{73}$$

wobei $V_n^{(0)}$ ist der Minimalwert der elektronischen Energie, die das Molekül in Ruhe charakterisiert, $W_{ns}^{(2)}$ ist die Energie der Kernschwingung, und $W_{nsr}^{(4)}$ enthält (zusammen mit zusätzlichen Termen für die Schwingungsenergie) die Rotationsenergie. In dieser Näherung (zu $\kappa^4$) die drei grundlegenden Bewegungsarten sind 'getrennt'; Die Kopplung zwischen ihnen beinhaltet Terme höherer Potenzen von $\kappa$.

Gegeben (72) können wir nun Übergangswahrscheinlichkeiten (Intensitäten der Bänder) berechnen.

Das elektrische Moment eines Moleküls $\mathcal{M}$ besteht aus einem nuklearen Teil $\mathcal{P}$ und ein elektronisches Bauteil $p$; die $x$-Komponente ist:

$$\mathcal{M}_x = \mathcal{P}_x + p_x, \quad \text{where} \quad \left\{ \begin{array}{l} \mathcal{P}_x = \sum_l e_l X_l \\ p_x = e \sum_k x_k \end{array} \right. . \tag{74}$$

12

Daher gilt aus der Menge der Matrixelemente bezüglich $x_k$, $\zeta_i$ und $\theta_j$;

$$(p_x)_{n'}^n = \int p_x \phi_n^{(0)} \overline{\phi_n^{(0)}} \mathrm{d}x \tag{75}$$

ist eine Funktion von $\zeta_i$ und $\theta_j$, dann die

$$(p_x)_{n's'}^{ns} = \int (p_x)_{n'}^{n} \sigma_{ns'}^{(0)} \overline{\sigma_{ns'}^{(0)}} \mathrm{d}\zeta$$

$$(\mathcal{P}_x)_{n's'}^{ns} = \int (\mathcal{P}_x) \sigma_{ns}^{(0)} \overline{\sigma_{n's'}^{(0)}} \mathrm{d}\zeta \tag{76}$$

sind Funktionen von $\theta_j$, endlich

$$(p_x)_{n's'r'}^{nsr} = \int (p_x)_{n's'}^{ns} \rho_{nsr}^{(0)} \overline{\rho_{n's'r'}^{(0)}} \mathrm{d}\theta$$

$$(\mathcal{P}_x)_{n's'r'}^{nsr} = \int (\mathcal{P}_x)_{n's'}^{ns} \rho_{nsr}^{(0)} \overline{\rho_{n's'r'}^{(0)}} \mathrm{d}\theta \tag{77}$$

sind numerische Konstanten, die die Strahlung und die Übergangswahrscheinlichkeit für bestimmen $nsr \to n's'r'$. Wir können dieses Schritt-für-Schritt-Verfahren wie folgt interpretieren: für jeden elektronischen Übergang $n \to n'$, da entspricht ein virtueller Oszillator mit Moment $(p_x)_{n'}^n$; Daraus erhält man die Matrix $(p_x)_{n's'}^{ns}$ was einem System von Schwingungsbändern entspricht (Übergänge von $s \to s'$), durch eine Regel (etwas anders als die gewöhnliche), bei der man eine Eigenfunktion der unteren und einer der oberen elektronischen Ebene verwendet (Gleichung (76)). Wir wiederholen das Verfahren für die Linie des Bandes, die dem Übergang entspricht $r \to r'$. Die hier enthaltene Methode zur Bewertung der Intensität der Schwingungsbänder wird zuerst von Franck gegeben [3] und von Condon weiterentwickelt [4].

Diese werden durch Variation der Funktionen bestimmt $V_n(\xi)$ und $V_{n'}(\xi)$; nur in der Umgebung ihrer Minima befinden sich die entsprechenden Eigenfunktionen $\sigma_{ns}^{(0)}$ und $\sigma_{n's'}^{(0)}$ deutlich anders als Null; Ihr Produkt ist nur dann so, wenn sich diese Regionen überschneiden. Wenn die Funktion $V_n(\xi)$ ändert sich nur geringfügig bei einem elektronischen Übergang $n \to n'$, die Bänder, die einer kleinen Änderung von entsprechen $s$ wird intensiv sein; wenn jedoch $V_n(\xi)$ ändert sich stark im Übergang, eine Überlappung der Intervalle, in denen $\sigma_{ns}^{(0)}$ und $\sigma_{n's'}^{(0)}$ nicht verschwinden wird erst möglich, wenn der Unterschied $s - s'$ ist groß. Diese Beziehungen werden von Condon quantitativ diskutiert. Ähnliche Überlegungen gelten für die Rotationen *mutatis mutandis*.

### Teil VII. Spezialfall des zweiatomigen Moleküls

Als Beispiel behandeln wir kurz das zweiatomige Molekül. Neben der Resonanzdegeneration, die eine Folge der Ununterscheidbarkeit der Elektronen ist, gibt es eine zusätzliche Entartung, da es zu jedem Energiewert zwei mögliche Bewegungsmoden gibt, in denen der Drehimpuls um die internukleare Achse entgegengesetzt ausgerichtet ist. Da wir uns hier nicht mit der feinen Struktur der Bänder beschäftigen, werden wir diese Entartung nicht berücksichtigen; Wir beschränken unsere Betrachtung auf Fälle, in denen der Drehimpuls um die Achse verschwindet oder wenn die elektronische Energie unabhängig oder nur geringfügig von der Drehimpulskomponente abhängt.

Für zwei Kerne haben wir nur einen $\xi$ Koordinate, die Kerntrennung und fünf $\theta$ Koordinaten: Die Koordinaten des Schwerpunkts $X_0, Y_0, Z_0$, und die Polarkoordinaten der internuklearen Achse $\theta, \omega$.

Die kinetische Energie der Kerne wird

$$T_K = -\kappa^4 \frac{h^2}{8\pi^2 m} \left\{ \Delta_0 + \frac{\mu}{\xi^2} \frac{\partial}{\partial \xi} \left( \xi^2 \frac{\partial}{\partial \xi} \right) + \frac{\mu}{\xi^2} \Delta_0 \right\} \tag{78}$$

wobei

$$\kappa = \left( \frac{m}{M_1 + M_2} \right)^{1/4} \quad \text{and} \quad \mu = \frac{(M_1 + M_2)^2}{M_1 M_2} \tag{79}$$

13

und

$$\Delta_{0} = \frac{\partial^{2}}{\partial X_{0}^{2}} + \frac{\partial^{2}}{\partial Y_{0}^{2}} + \frac{\partial^{2}}{\partial Z_{0}^{2}},$$

$$\Delta_{\theta} = \frac{1}{\sin^{2}\theta} \frac{\partial^{2}}{\partial \omega^{2}} + \frac{1}{\sin\theta} \frac{\partial}{\partial \theta} \left( \sin\theta \frac{\partial}{\partial \theta} \right). \tag{80}$$

Also:

$$H_{\xi\xi} = -\frac{h^{2}}{8\pi^{2}m} \mu \frac{\partial^{2}}{\partial \xi^{2}},$$

$$H_{\xi\theta} = -\frac{h^{2}}{8\pi^{2}m} \frac{2\mu}{\xi} \frac{\partial}{\partial \xi}, \tag{81}$$

$$H_{\theta\theta} = -\frac{h^{2}}{8\pi^{2}m} \left( \Delta_{0} + \frac{\mu}{\xi^{2}} \Delta_{\theta} \right).$$

Substitution $\xi + \kappa\zeta$ für $\xi$ und entwickelt sich in $\kappa$, finden wir:

$$H_{\zeta\zeta}^{(0)} = -\frac{h^{2}}{8\pi^{2}m} \mu \frac{\partial^{2}}{\partial \zeta^{2}},$$

$$H_{\zeta\zeta}^{(p)} = 0, \quad p = 1, 2, \dots \tag{82}$$

$$H_{\zeta\theta}^{(0)} = -\frac{h^{2}}{8\pi^{2}m} \frac{2\mu}{\xi} \frac{\partial}{\partial \zeta},$$

$$H_{\zeta\theta}^{(1)} = \frac{h^{2}}{8\pi^{2}m} \frac{\mu}{\xi^{2}} \zeta \frac{\partial}{\partial \zeta}, \tag{83}$$

...

$$H_{\theta\theta}^{(0)} = -\frac{h^{2}}{8\pi^{2}m} \left( \Delta_{0} + \frac{\mu}{\xi^{2}} \Delta_{\theta} \right),$$

$$H_{\theta\theta}^{(1)} = \frac{h^{2}}{8\pi^{2}m} \frac{2\mu}{\xi^{3}} \zeta \Delta_{\theta}. \tag{84}$$

...

Die Kerntrennung wird durch die Gleichung bestimmt

$$V_{n}^{\prime} = \frac{\partial V_{n}}{\partial \xi} = 0. \tag{85}$$

Die Gleichung für die Kernschwingung ist

$$\left\{ -\frac{h^{2}}{8\pi^{2}m} \mu \frac{\partial^{2}}{\partial \zeta^{2}} + \frac{1}{2} \zeta^{2} V_{n}^{\prime\prime}(\xi) W_{n}^{(2)} \right\} \chi_{n}^{(0)} = 0. \tag{86}$$

Wenn wir setzen

$$a = \frac{8\pi^{2}m}{h^{2}\mu} W_{n}^{(2)} \quad b = \frac{8\pi^{2}m}{h^{2}\mu} V_{n}^{\prime\prime} \quad \eta = \zeta b^{1/4} \tag{87}$$

Wir haben [8]

$$\left\{ \frac{\partial^{2}}{\partial \eta^{2}} + \left( \frac{a}{\sqrt{b}} - \eta^{2} \right) \right\} \chi_{n}^{(0)} = 0.$$

14

Die Eigenwerte sind

$$a / b ^ { 1 / 2 } = 2 s + 1 \ ( s = 0 , 1 , 2 , \dots ) ,$$

mit Eigenfunktionen

$$\sigma _ { n s } ^ { ( 0 ) } = \exp { - ( \eta ^ { 2 } / 2 ) } H _ { s } ( \eta ) ,$$

wobei $H _ { s }$ ist die $s$Das Hermite-Polynom.

Die Energie der Schwingungen ist folglich:

$$\begin{array} { l l l } { { \kappa ^ { 2 } W _ { n s } ^ { ( 2 ) } } } & { { = } } & { { a \displaystyle \frac { h ^ { 2 } } { 8 \pi ^ { 2 } } \frac { \kappa ^ { 2 } \mu } { m } = ( 2 s + 1 ) b ^ { 1 / 2 } \frac { h ^ { 2 } } { 8 \pi ^ { 2 } } \frac { \kappa ^ { 2 } \mu } { m } } } \\ { { } } & { { = } } & { { \left( s + \displaystyle \frac { 1 } { 2 } \right) \displaystyle \frac { h } { 4 \pi } \sqrt { \kappa ^ { 4 } \displaystyle \frac { \mu } { m } V _ { n } ^ { \prime \prime } } } } \end{array}$$

oder

$$\kappa ^ { 2 } W _ { n s } ^ { ( 2 ) } = \left( s + \frac { 1 } { 2 } \right) h \nu _ { 0 }$$

mit

$$\frac { 1 } { 4 \pi } \sqrt { \kappa ^ { 4 } \frac { \mu } { m } V _ { n } ^ { \prime \prime } } = \frac { 1 } { 4 \pi } \sqrt { \left( \frac { 1 } { M _ { 1 } } + \frac { 1 } { M _ { 2 } } \right) V _ { n } ^ { \prime \prime } } = \nu _ { 0 }$$

die Frequenz des Oszillators.

Wir stellen nun die Gleichung (69) für die Rotation auf und vernachlässigen dabei jede detaillierte Schätzung der Korrektur der Schwingungsenergie. Da $H _ { \xi \theta }$ durch (81) enthält keine Ableitungen bezüglich der $\theta _ { j }$ , wir müssen nur den Term betrachten $\overline { { \left( H _ { \theta \theta } ^ { ( 0 ) } \right) } } _ { n }$ in (69); Alle verbleibenden Terme beziehen wir in die Konstante ein $C _ { n s }$ . Die Rotationsgleichung (69) lautet dann:

$$\left\{ \overline { { \left( H _ { \theta \theta } ^ { ( 0 ) } \right) } } _ { n } + C _ { n s } - W ^ { ( 4 ) } \right\} \rho _ { n s } ^ { ( 0 ) } = 0 .$$

Da wir den translationalen Teil von $H _ { \theta \theta ^ { ( 0 ) } }$ , haben wir durch (70) und (84) für eine beliebige Funktion $f ( \theta )$ :

$$\overline { { \left( H _ { \theta \theta } ^ { ( 0 ) } \right) } } _ { n } f ( \theta ) = - \frac { h ^ { 2 } \mu } { 8 \pi ^ { 2 } m \xi ^ { 2 } } \int \overline { { \phi _ { n } ^ { ( 0 ) } } } \Delta _ { \theta } ( \phi _ { n } ^ { ( 0 ) } f ) \mathrm { d } x$$

und von (80)

$$\Delta _ { \theta } ( \phi _ { n } ^ { ( 0 ) } f ) = \phi _ { n } ^ { ( 0 ) } \Delta _ { \theta } f + f \Delta _ { \theta } \phi _ { n } ^ { ( 0 ) } + 2 \left( \frac { 1 } { \sin ^ { 2 } \theta } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \omega } \frac { \partial f } { \partial \omega } + \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \theta } \frac { \partial f } { \partial \theta } \right) .$$

Daher

$$\begin{array} { l l l } { { \overline { { { \left( H _ { \theta \theta } ^ { ( 0 ) } \right) } } } _ { n } f } } } & { { = } } & { { - \displaystyle \frac { h ^ { 2 } \mu } { 8 \pi ^ { 2 } m \xi ^ { 2 } } \left\{ \Delta _ { \theta } f + f \int \overline { { \phi _ { n } ^ { ( 0 ) } } } \Delta _ { \theta } \phi _ { n } ^ { ( 0 ) } \mathrm { d } x \right. } } \\ { { } } & { { + } } & { { \displaystyle \left. \cdot \frac { 2 } { \sin ^ { 2 } \theta } \frac { \partial f } { \partial \omega } \int \overline { { \phi _ { n } ^ { ( 0 ) } } } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \omega } \mathrm { d } x + 2 \frac { \partial f } { \partial \theta } \int \overline { { \phi _ { n } ^ { ( 0 ) } } } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \theta } \mathrm { d } x \right\} . } } \end{array}$$

Wenn wir schreiben $\Delta _ { \theta }$ In der Form:

$$\Delta _ { \theta } = \frac { \partial ^ { 2 } } { \partial \theta ^ { 2 } } + \mathrm { c t g } \, \theta \frac { \partial } { \partial \theta } + \frac { 1 } { \sin ^ { 2 } \theta } \frac { \partial ^ { 2 } } { \partial \omega ^ { 2 } }$$

Wir sehen, dass es praktisch ist, folgende Notation einzuführen:

$$\begin{array} { l l } { { \overline { { { \Theta _ { n } } } } = \displaystyle \int \overline { { { \phi _ { n } ^ { ( 0 ) } } } } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \theta } \mathrm { d } x , } } & { { \overline { { { \Omega _ { n } } } } = \displaystyle \int \overline { { { \phi _ { n } ^ { ( 0 ) } } } } \frac { \partial \phi _ { n } ^ { ( 0 ) } } { \partial \omega } \mathrm { d } x , } } \\ { { \overline { { { \Theta _ { n } ^ { ( 2 ) } } } } = \displaystyle \int \overline { { { \phi _ { n } ^ { ( 0 ) } } } } \frac { \partial ^ { 2 } \phi _ { n } ^ { ( 0 ) } } { \partial \theta ^ { 2 } } \mathrm { d } x , } } & { { \overline { { { \Omega _ { n } ^ { ( 2 ) } } } } = \displaystyle \int \overline { { { \phi _ { n } ^ { ( 0 ) } } } } \frac { \partial ^ { 2 } \phi _ { n } ^ { ( 0 ) } } { \partial \omega ^ { 2 } } \mathrm { d } x . } } \end{array}$$

15

Diese Größen sind die Diagonalmatrixelemente von $p_{\theta}$, $p_{\omega}$, $p_{\theta}^{2}$ und $p_{\omega}^{2}$ (abgesehen von einem Faktor $\frac{h}{2\pi^{2}}$, $-\frac{h^{2}}{4\pi^{2}}$ jeweils); die ersten beiden bezeichnen den Mittelwert des elektronischen Drehimpulses um ihren entsprechenden Eulerschen Winkel; die zweiten beiden sind der Mittelwert des Quadrats des Drehimpulses der elektronischen Bewegung. Wir schreiben dann explizit für (90):

$$\left\{\left(\frac{\partial^{2}}{\partial\theta^{2}}+2\overline{\Theta_{n}}\frac{\partial}{\partial\theta}+\overline{\Theta_{n}^{(2)}}\right)+\operatorname{ctg}\theta\left(\frac{\partial}{\partial\theta}+\overline{\Theta_{n}}\right)\right.$$ $$\left.\frac{1}{\sin^{2}\theta}\left(\frac{\partial^{2}}{\partial\omega^{2}}+2\overline{\Omega_{n}}\frac{\partial}{\partial\omega}+\overline{\Omega_{n}^{(2)}}\right)+\frac{8\pi^{2}m\xi^{2}}{h^{2}\mu}\left(W^{(4)}-C_{ns}\right)\right\}\rho_{ns}^{(0)}=0 \quad (92)$$

Dies ähnelt sehr der Gleichung von Kramers und Pauli für einen Rotor mit eingebautem Schwungrad; Der Unterschied besteht im Wesentlichen darin, dass sie die Quadrate der Durchschnittswerte verwenden $\overline{\Theta_{n}}^{2}$ und $\overline{\Omega_{n}}^{2}$, statt des Durchschnitts der Quadrate $\overline{\Theta_{n}^{2}}$ und $\overline{\Omega_{n}^{2}}$.

Die Abhängigkeit der Größen in (91) von den Winkeln $\theta$ und $\omega$ kann durch elementare Überlegungen festgestellt werden, wenn angenommen wird, dass zu diesem Zweck die diagonalen Elemente der quantenmechanischen Matrix durch die entsprechenden klassischen Durchschnitte ersetzt werden können. Man kann die Bewegung des elektronischen Drehimpulsvektors in eine unregelmäßige Variation ohne durchschnittliche Rotationen und eine überlagerte gleichmäßige Rotation um die Molekülachse zerlegen. Wir stellen die Variation im Durchschnitt durch einen konstanten Vektor dar; dieser rotiert gleichmäßig um die Achse. Dies zeigt dasselbe Verhalten wie ein symmetrisches Top mit Drehimpulskomponenten bezüglich des top-fixierten Koordinatensystems mit Werten $L$, $M$ und $N$. Daraus können wir die Komponenten des Drehimpulses in der $\theta$, $\omega$ Richtung wie folgt:

$$\begin{array}{l} \Theta = L\cos\gamma - M\sin\gamma \\ \Omega = L\sin\theta\sin\gamma + M\sin\theta\cos\gamma + N\cos\theta, \end{array}$$

wobei $\gamma$ ist der Winkel der Eigenrotation um die Achse. Durchschnitt über $\gamma$, finden wir:⁵

$$\begin{array}{l} \overline{\Theta}=0 \quad \overline{\Omega}=N\cos\theta \\ \overline{\Theta^{2}}=\frac{1}{2}(L^{2}+M^{2}) \quad \overline{\Omega^{2}}=\frac{1}{2}(L^{2}+M^{2})\sin^{2}\theta+N^{2}\cos^{2}\theta. \end{array}$$

Wir identifizieren $N$ mit der Quantenzahl $\rho$ was den Drehimpuls um die Achse ergibt, und $\frac{1}{2}(L^{2}+M^{2})$ und $\frac{1}{2}N^{2}$ mit den Durchschnitten $\overline{p_{\perp}^{2}}$ und $\overline{p_{\parallel}^{2}}$ des gesamten elektronischen Drehimpulses senkrecht und parallel zur Achse; da $N$ konstant ist, $\overline{p_{\parallel}^{2}}=p^{2}$. Wir haben schließlich:

$$\begin{array}{l} \overline{\Theta_{n}}=0 \quad \overline{\Omega_{\mu}}=p\cos\theta \\ \overline{\Theta_{n}^{2}}=\overline{p_{\perp}^{2}} \quad \overline{\Omega^{2}}=\overline{p_{\perp}^{2}}\sin^{2}\theta+p^{2}\cos^{2}\theta. \end{array} \quad (93)$$

Dieses Ergebnis erfordert naturgemäß eine rigorose quantenmechanische Überprüfung; vermutlich $p^{2}$ wird ersetzt durch $p(p+1)$.

Im Eigenwertproblem (92) gilt die Größe $\frac{8\pi^{2}m\xi^{2}}{h^{2}\mu}W^{(4)}$ gleich einer numerischen Funktion der Rotationsquantenzahl ist. $r$, sagen Sie $g_{ns}(r)$; Die Rotationsenergie ist folglich:

$$\kappa^{4}W_{nsr}^{(4)}=\frac{h^{2}\mu\kappa^{4}}{8\pi^{2}m\xi^{2}}g_{ns}(r)=\frac{h^{2}}{8\pi^{2}J}g_{ns}(r), \quad (94)$$

wobei

$$J=\frac{m}{\mu\kappa^{4}}\xi^{2}=\frac{M_{1}M_{2}}{M_{1}+M_{2}}\xi^{2}, \quad (95)$$

⁵Vergleich, zum Beispiel [9]

16

das Trägheitsmoment der Kerne im Gleichgewicht.

Eine Diskussion der höheren Näherung ist bedeutungslos, es sei denn, wir berücksichtigen die Entartungen; Wir werden das hier nicht versuchen.

Wir zeigen nun kurz, dass man das Zweiatomium mit einem völlig anderen Störungsverfahren behandeln kann; das klassische Analogon dieser Behandlung wurde von Born und Hückel durchgeführt [5]. Die Bewegung des elektronischen Systems gilt als unbeeinträchtigt nicht für stationäre Kerne, sondern für eine gleichmäßige Rotation der Kerne.

### Teil VIII. Unabhängige Behandlung des diatomischen Moleküls.

Wir gehen zurück zur Gleichung (12) und schreiben um, wobei wir (11) einsetzen:

$$\left\{H_{0}+\kappa^{4}\left(H_{\xi\xi}+H_{\xi\theta}+H_{\theta\theta}\right)-W\right\}\psi=0.$$

Diatomische Moleküle haben die Besonderheit, dass $H_{\xi\theta}$ ist im Allgemeinen unabhängig von $\theta$. In diesem Fall ermöglicht die Methode die Trennung von den Translationen und Rotationen. Aus (81), wobei die translationalen Begriffe weggelassen werden:

$$\left\{H_{0}-\frac{h^{2}\mu}{8\pi^{2}m}\kappa^{4}\left(\frac{\partial^{2}}{\partial\xi^{2}}+\frac{2}{\xi}\frac{\partial}{\partial\xi}+\frac{1}{\xi^{2}}\Delta_{\theta}\right)-W\right\}\psi=0. \tag{96}$$

Wir setzen

$$\psi=Y_{r}(\theta,\omega)\Psi_{r}(x;\xi), \tag{97}$$

wobei $Y_{r}$ ist eine sphärische Funktion von $r$th Ordnung, die die Gleichung erfüllt:

$$\Delta_{\theta}Y_{r}+r(r+1)Y_{r}=0;$$

Daher finden wir für $\Psi_{r}$ Die Bedingung

$$\left\{H_{0}-\frac{h^{2}\mu}{8\pi^{2}m}\kappa^{4}\left(\frac{\partial^{2}}{\partial\xi^{2}}+\frac{2}{\xi}\frac{\partial}{\partial\xi}-\frac{r(r+1)}{\xi^{2}}\right)-W\right\}\Psi_{r}=0. \tag{98}$$

Wir ersetzen erneut $\xi+\kappa\zeta$ für $\xi$; somit betrachtet man Schwingungen um den Zustand der gleichmäßigen Rotation. Die Energie dieses Zustands wird bezeichnet als:

$$R=\frac{h^{2}\mu\kappa^{2}}{8\pi^{2}m}\frac{r(r+1)}{\xi^{2}}=\frac{h^{2}}{8\pi^{2}J}r(r+1) \tag{99}$$

und Schauplatz

$$W=E+R, \tag{100}$$

finden wir für (98)

$$\left(\mathsf{H}^{(0)}+\kappa\mathsf{H}^{(1)}+\kappa^{2}\mathsf{H}^{(2)}+\cdots-\mathsf{E}\right)\Psi_{r}=0 \tag{101}$$

wobei

$$\mathsf{H}^{(0)}=H_{0}^{(0)}$$

$$\mathsf{H}^{(1)}=H_{0}^{(1)}+\zeta R'$$

$$\mathsf{H}^{(2)}=H_{0}^{(2)}+\frac{1}{2}\zeta^{2}R''-\frac{h^{2}\mu}{8\pi^{2}m}\frac{\partial^{2}}{\partial\zeta^{2}} \tag{102}$$

$$\mathsf{H}^{(3)}=H_{0}^{(3)}+\frac{1}{6}\zeta^{3}R'''-\frac{h^{2}\mu}{8\pi^{2}m}\frac{2}{\zeta}\frac{\partial}{\partial\zeta}$$

$$\cdots;$$

17

$H_0^{(0)}, H_0^{(1)}, \ldots$ sind die zuvor genannten Operatoren. Alle Formeln von Teil II sind unverändert gültig. Die Approximationsgleichungen sind:

$$
\begin{array}{l}
a) \quad \left(\mathsf{H}^{(0)} - \mathsf{E}^{(0)}\right) \Psi_r^{(0)} = 0 \\
b) \quad \left(\mathsf{H}^{(0)} - \mathsf{E}^{(0)}\right) \Psi_r^{(1)} = \left(\mathsf{E}^{(1)} - \mathsf{H}^{(1)}\right) \Psi_r^{(0)} \\
c) \quad \left(\mathsf{H}^{(0)} - \mathsf{E}^{(0)}\right) \Psi_r^{(2)} = \left(\mathsf{E}^{(2)} - \mathsf{H}^{(2)}\right) \Psi_r^{(0)} + \left(\mathsf{E}^{(1)} - \mathsf{H}^{(1)}\right) \Psi_r^{(1)}
\end{array}
\tag{103}
$$

Die erste enthält die Lösung:

$$
\mathsf{E}^{(0)} = V_n(\xi), \quad \Psi_r^{(0)} = \Psi_{rn}^{(0)} = \sigma_{rn}^{(0)}(\zeta) \phi_n^{(0)}(x; \xi),
\tag{104}
$$

wobei $V_n(\xi)$ und $\phi_n^{(0)}(x; \xi)$ sind die zuvor eingeführten Funktionen und $\sigma_{rn}^{(0)}(\zeta)$ ist zunächst willkürlich. Die Bedingung für die Integrabilität von (103b) ist

$$
\left(\mathsf{E}^{(1)} - \mathsf{H}^{(1)}\right) \sigma_{rn}^{(0)}(\zeta) = 0.
$$

Nun, von (26a) (Teil II):

$$
\mathsf{H}_{nn}^{(1)} = \left(H_0^{(1)}\right)_{nn} + \zeta R' = V_n^{(1)} + \zeta R' = \zeta \frac{\partial}{\partial \xi}(V_n + R).
$$

Daher gilt, wie zuvor (Teil IV),

$$
\mathsf{E}^{(1)} = 0, \quad \frac{\partial}{\partial \xi}(V_n + R) = 0.
\tag{105}
$$

Diese Bedingung besagt offensichtlich, dass für die ungestörte Rotation ein Gleichgewicht zwischen der Zentrifugalkraft und der quasi-elektrischen Kraft herrschen muss, die infolge der elektronischen Bewegung einer Verschiebung der Kerne widersteht. Die Zentrifugalkraft ist:

$$
-\left(\frac{1}{M_1} + \frac{1}{M_2}\right) \frac{p_r^2}{\xi^3} = -\left(\frac{1}{M_1} + \frac{1}{M_2}\right) \frac{h^2}{4\pi^2} \frac{r(r+1)}{\xi^3},
$$

wobei der quantenmechanische Wert $\frac{h}{2\pi} \sqrt{r(r+1)}$ für wird der Drehimpuls für ersetzt $p_r$; durch (99) und (95) stimmt dies mit überein. $R'$.

Aus Relation (105): Wie man die Gleichgewichtstrennung berechnet $\xi_r$; hängt von der Rotationsquantenzahl ab $r$. Für kleine Werte der Rotationsenergie $R$, man kann sich entwickeln $\xi_r$ in Potenzen von $\beta$, wobei:

$$
\beta = \kappa^4 \frac{\mu}{m} \frac{h^2}{4\pi^2} r(r+1) = \left(\frac{1}{M_1} + \frac{1}{M_2}\right) \frac{h^2}{4\pi^2} r(r+1);
\tag{106}
$$

Wir finden:⁶

$$
\xi_r = \xi + \frac{1}{\xi^3 V_n''} \beta - \frac{3}{\xi^7 V_n''^2} \left(1 + \frac{\xi}{6} \frac{V_n''}{V_n''}\right) \beta^2 + \cdots
\tag{107}
$$

Da $\beta$ ist von Ordnung $\kappa^4$, verwenden wir systematisches Verfahren nur so viele Terme dieser Menge, wie der Ordnung der Näherung in der Störungsmethode entspricht.

Da wir dies erneut betrachten, werden wir bald sehen, dass dies die gleiche Methode wie zuvor ist, nur vereinfacht durch die vorherige Betrachtung der Rotation. Die Lösung von (103b) lautet:

$$
\Psi_{rn}^{(1)} = \sigma_{rn}^{(0)} \phi_n^{(1)} + \sigma_{rn}^{(1)} \phi_n^{(0)}
\tag{108}
$$

dies entspricht (42); und die Bedingung für die Integrierbarkeit von (102c):

$$
\left\{ \mathsf{H}_{nn}^{(2)} + \left(\mathsf{H}_{nn}^{(1)}\right)_{nn}^{(1)} - \mathsf{E}_n^{(2)} \right\} \sigma_{rn}^{(0)} = 0.
$$

⁶Man kann diese Formel leicht aus den zitierten Arbeiten von Born und Hückel ableiten.

18

Dies ist jedoch die Schwingungsgleichung

$$\left\{ - \frac { h ^ { 2 } \mu } { 8 \pi ^ { 2 } m } \frac { \partial ^ { 2 } } { \partial \zeta ^ { 2 } } + \frac { 1 } { 2 } \zeta ^ { 2 } ( V _ { n } ^ { \prime \prime } + R ^ { \prime \prime } ) - \mathsf { E } _ { n } ^ { ( 2 ) } \right\} \sigma _ { r n } = 0 . \tag { 1 0 9 }$$

Also, wie in Teil VII:

$$\kappa ^ { 2 } \mathsf { E } _ { r n s } ^ { ( 2 ) } = \left( s + \frac { 1 } { 2 } \right) h \nu _ { r } , \tag { 1 1 0 }$$

wobei die Frequenz,

$$\nu _ { r } = \frac { 1 } { 4 \pi } \sqrt { \left( \frac { 1 } { M _ { 1 } } + \frac { 1 } { M _ { 2 } } \right) ( V _ { n } ^ { \prime \prime } + R ^ { \prime \prime } ) } \tag { 1 1 1 }$$

hängt weiterhin von der Rotationsquantenzahl ab $r$, aus dem $R$.

Außerdem, wie in Teil VII,

$$\sigma _ { r n s } ^ { ( 0 ) } = \exp ( - \eta ^ { 2 } / 2 ) H _ { s } ( \eta ) \tag { 1 1 2 }$$

mit

$$\eta = \zeta b ^ { 1 / 4 } , \quad b = \frac { 8 \pi ^ { 2 } } { h ^ { 2 } } \frac { m } { 2 \mu } ( V _ { n } ^ { \prime \prime } + R ^ { \prime \prime } ) .$$

Der Eingriff kann wie üblich fortgesetzt werden. Wir finden $\mathsf { E } ^ { ( 3 ) } = 0$, während $\mathsf { E } ^ { ( 4 ) }$, enthält neben der Abweichung vom harmonischen Schwingungsgesetz auch eine Kopplung mit der elektronischen Bewegung. Eine gründliche Betrachtung der Formeln würde jedoch über den Rahmen dieses Werks hinausgehen, das nur das Prinzip der Entwicklung zeigt; außerdem ist die Berechnung der höheren Approximationen nur dann sinnvoll, wenn die Entartungen berücksichtigt werden.

[1] M. Born und W. Heisenberg Ann. d. Phys. 74 1 (1924)

[2] H. A. Kramers Zeitschr. f. Phys. 13, 343 (1923); H. A. Kramers und W. Pauli Jr., ebd. ebd. 13, 351 (1923)

[3] J. Franck: Übers. Faraday. Soc. (1925)

[4] E. Condon, Phys. Rev. 28 1182 (1926); Proc. Nat. Acad. 13 462 (1927)

[5] M. Born und E. Hückel Phys. Ztschr. 24 1 (1923)

[6] F. Hund Ztschr. f. Phys. 43, 805 (1927)

[7] W. Pauli Ann. d. Phys. 68 177 (1922)

[8] S. E. Schrödinger Ann. d. Phys. 79 361, §3 (1926).

[9] F. Klein und A. Sommerfeld Theorie des Kreisels 1 S. 108

19
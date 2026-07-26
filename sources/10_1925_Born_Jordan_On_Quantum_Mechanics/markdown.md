858

## Zur Quantenmechanik.

Von M. Born und P. Jordan in Göttingen.

(Eingegangen am 27. September 1925.)

Die kürzlich von Heisenberg gegebenen Ansätze werden (zunächst für Systeme von einem Freiheitsgrad) zu einer systematischen Theorie der Quantenmechanik entwickelt. Das mathematische Hilfsmittel ist die Matrizenrechnung. Nachdem diese kurz dargestellt ist, werden die mechanischen Bewegungsgleichungen aus einem Variationsprinzip abgeleitet und der Beweis geführt, daß auf Grund der Heisenbergschen Quantenbedingung der Energiesatz und die Bohrsche Frequenzbedingung aus den mechanischen Gleichungen folgen. Am Beispiel des anharmonischen Oszillators wird die Frage der Eindeutigkeit der Lösung und die Bedeutung der Phasen in den Partialschwingungen erörtert. Den Schluß bildet ein Versuch, die Gesetze des elektromagnetischen Feldes der neuen Theorie einzufügen.

Einleitung. Die kürzlich von Heisenberg¹⁾ in dieser Zeitschrift mitgeteilten Ansätze zu einer neuen Kinematik und Mechanik, die den Grundforderungen der Quantentheorie entsprechen, scheinen uns von großer Tragweite zu sein. Sie bedeuten einen Versuch, den neuen Tatsachen — statt durch mehr oder weniger künstliche und gezwungene Anpassung der alten gewohnten Begriffe — durch die Schaffung eines neuen, wirklich angemessenen Begriffssystems gerecht zu werden. Heisenberg hat die physikalischen Gedanken, die ihn dabei geleitet haben, in so klarer Weise ausgesprochen, daß jede ergänzende Bemerkung überflüssig erscheint. Aber in formaler, mathematischer Hinsicht sind seine Betrachtungen, wie er selbst betont, erst im Anfangsstadium. Er hat seine Hypothesen nur an einfachen Beispielen erläutert und ist nicht zu einer allgemeinen Theorie vorgedrungen. Begünstigt durch den Umstand, daß wir seine Überlegungen schon in statu nascendi kennenlernen durften, haben wir uns nach Abschluß seiner Untersuchungen bemüht, den mathematisch-formalen Gehalt seiner Ansätze zu klären, und legen hier einige unserer Ergebnisse vor. Sie zeigen, daß es tatsächlich möglich ist, auf der von Heisenberg gegebenen Grundlage das Gebäude einer geschlossenen mathematischen Theorie der Quantenmechanik in merkwürdig enger Analogie zur klassischen Mechanik, doch unter Wahrung der für die Quantenerscheinungen kennzeichnenden Züge zu errichten.

Wir beschränken uns dabei zunächst mit Heisenberg auf Systeme von einem Freiheitsgrad, von denen wir annehmen, daß sie — klassisch gesprochen — periodisch sind. Die Verallgemeinerung der

¹⁾ W. Heisenberg, ZS. f. Phys. 33, 879, 1925.

M. Born und P. Jordan, Zur Quantenmechanik.

859

mathematischen Theorie auf Systeme von beliebig vielen Freiheitsgraden sowie auf aperiodische Bewegungen wird uns in der Fortsetzung dieser Abhandlung beschäftigen. In wesentlicher Verallgemeinerung der Heisenbergschen Ansätze werden wir uns weder auf die Behandlung der nicht-relativistischen Mechanik, noch auf das Rechnen mit kartesischen Koordinaten beschränken. Die einzige Beschränkung, die wir uns hinsichtlich der Koordinaten auferlegen, liegt darin, daß sich unsere Betrachtungen auf Librationskoordinaten beziehen, die in der klassischen Theorie periodische Funktionen der Zeit sind. Allerdings scheint es in manchen Fällen naheliegend, andere Koordinaten zu benutzen, beispielsweise beim Rotator den Drehwinkel $\varphi$, der eine lineare Funktion der Zeit wird. So ist auch Heisenberg bei seiner Behandlung des Rotators vorgegangen; es muß jedoch dahingestellt bleiben, ob das dabei angewandte Verfahren vom Standpunkt einer folgerichtigen Quantenmechanik aus gerechtfertigt werden kann.

Die mathematische Grundlage der Heisenbergschen Betrachtung ist das Multiplikationsgesetz der quantentheoretischen Größen, das er durch eine geistreiche Korrespondenzbetrachtung erschlossen hat. Die Ausgestaltung seines Formalismus, die wir hier geben, beruht auf der Bemerkung, daß diese Regel nichts ist, als das den Mathematikern wohlbekannte Gesetz der Multiplikation von Matrizen. Das nach zwei Seiten unendliche, quadratische Schema (mit diskreten oder kontinuierlich laufenden Indizes), die sogenannte Matrix, ist der Repräsentant einer physikalischen Größe, die in der klassischen Theorie als Funktion der Zeit angegeben wird. Die mathematische Methode der neuen Quantenmechanik ist daher gekennzeichnet durch Benutzung einer Matrizenanalysis an Stelle der gewöhnlichen Zahlenanalysis.

Mit dieser Methode haben wir hier die einfachsten Fragen der Mechanik und Elektrodynamik anzufassen versucht. Ein durch Korrespondenzbetrachtungen nahegelegtes Variationsprinzip liefert für die allgemeinste Hamiltonsche Funktion Bewegungsgleichungen in engster Analogie zu den klassischen kanonischen Gleichungen. Die Quantenbedingung zusammengefaßt mit einer aus den Bewegungsgleichungen fließenden Relation erlaubt eine einfache Matrizenschreibweise. Mit ihrer Hilfe gelingt der Beweis der Allgemeingültigkeit des Energiesatzes und der Bohrschen Frequenzbedingung in dem von Heisenberg vermuteten Sinne, ein Beweis, den er auch für die einfachen, von ihm behandelten Beispiele nicht vollständig führen konnte. Auf eines dieser Beispiele kommen wir dann ausführlicher

Zeitschrift für Physik. Bd. XXXIV.

57

860

M. Born und P. Jordan,

zurück, um einen Anhalt zu gewinnen über die Rolle, die die Phasen der Partialschwingungen in der neuen Theorie spielen. Zum Schluß zeigen wir, daß auch die Grundgesetze des elektromagnetischen Feldes im Vakuum sich der neuen Methode zwangslös einfügen, und geben eine Begründung der von Heisenberg gemachten Annahme, daß die Quadrate der Beträge der Elemente der das elektrische Moment eines Atoms darstellenden Matrix ein Maß sind für die Übergangswahrscheinlichkeiten.

### Kapitel I. Matrizenrechnung.

§ 1. Elementare Operationen. Funktionen. Wir rechnen mit quadratischen unendlichen Matrizen¹), die wir hier mit fetten Buchstaben bezeichnen wollen, während schwache Buchstaben stets gewöhnliche Zahlen bedeuten sollen:

$$\boldsymbol{a} = (a(nm)) = \begin{pmatrix} a(00) & a(01) & a(02) \dots \\ a(10) & a(11) & a(12) \dots \\ a(20) & a(21) & a(22) \\ \dots & \dots & \dots & \dots \end{pmatrix}$$

Gleichheit zweier Matrizen bedeutet Gleichheit entsprechender Komponenten:

$$\boldsymbol{a} = \boldsymbol{b} \text{ heißt } a(nm) = b(nm). \quad (1)$$

Addition wird definiert durch Addition entsprechender Komponenten

$$\boldsymbol{a} = \boldsymbol{b} + \boldsymbol{c} \text{ heißt } a(nm) = b(nm) + c(nm). \quad (2)$$

Die Multiplikation wird definiert durch die aus der Determinantentheorie bekannte Regel „Zeilen mal Kolonnen“:

$$\boldsymbol{a} = \boldsymbol{b}\boldsymbol{c} \text{ heißt } a(nm) = \sum_{k=0}^{\infty} b(nk)c(km). \quad (3)$$

Potenzen sind durch wiederholte Multiplikation zu definieren. Es gilt das assoziative Gesetz für die Multiplikation und das distributive für die Verbindung von Addition und Multiplikation:

$$(\boldsymbol{a}\boldsymbol{b})\boldsymbol{c} = \boldsymbol{a}(\boldsymbol{b}\boldsymbol{c}): \quad (4)$$

$$\boldsymbol{a}(\boldsymbol{b} + \boldsymbol{c}) = \boldsymbol{a}\boldsymbol{b} + \boldsymbol{a}\boldsymbol{c}. \quad (5)$$

Dagegen gilt nicht das kommutative Gesetz für die Multiplikation: Die Gleichung $\boldsymbol{a}\boldsymbol{b} = \boldsymbol{b}\boldsymbol{a}$ ist nicht allgemein richtig. Wenn sie gilt,

¹) Man findet Näheres über Matrizenrechnung etwa bei M. Böcher, Einführung in die höhere Algebra: aus dem Englischen von Hans Beck, Leipzig, Teubner, 1910, § 22 bis 25; ferner bei R. Courant und D. Hilbert, Methoden der mathematischen Physik I. Berlin, Springer, 1924, 1. Kap.

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

862

M. Born und P. Jordan,

Summe von endlich oder unendlich vielen Potenzprodukten in den Argumenten $\mathbf{x}_k$ mit Zahlen als Koeffizienten formal dargestellt werden kann. Es können dann auch durch Gleichungen

$$\left. \begin{array}{l} f_1(y_1, \dots, y_n; x_1, \dots, x_n) = 0, \\ \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \end{array} \right\} \quad (12)$$

Funktionen $\mathbf{y}_l(\mathbf{x}_1, \dots, \mathbf{x}_n)$ definiert werden. Um nämlich Funktionen $\mathbf{y}_l$ der oben beschriebenen Form zu erhalten, welche den Gleichungen (12) genügt, hat man nur die $\mathbf{y}_l$ als Reihen, die nach Potenzprodukten der $\mathbf{x}_k$ fortschreiten, anzusetzen und durch Einsetzen in (12) die Koeffizienten der Reihe nach zu bestimmen. Man erkennt, daß sich stets ebenso viele Gleichungen wie Unbekannte ergeben. Die Anzahl der Gleichungen und Unbekannten ist freilich größer, als bei der Anwendung der Methode der unbestimmten Koeffizienten in der gewöhnlichen, mit kommutativer Multiplikation rechnenden Analysis. Man erhält in jeder der Gleichungen (12) nach Einsetzen der Reihen für die $\mathbf{y}_l$ und Zusammenfassung der zusammengehörigen Glieder außer einem Summanden $C'\mathbf{x}_1\mathbf{x}_2$ auch einen Summanden $C''\mathbf{x}_2\mathbf{x}_1$ und hat sowohl $C'$ als auch $C''$ (nicht nur $C' + C''$) zum Verschwinden zu bringen. Dafür treten jedoch auch in der Entwicklung eines jeden $\mathbf{y}_l$ zwei Glieder $\mathbf{x}_1\mathbf{x}_2$ und $\mathbf{x}_2\mathbf{x}_1$ mit zwei verfügbaren Koeffizienten auf.

§ 2. Symbolische Differentiation. Ein später viel benutzter Rechenprozeß, den wir hier näher betrachten wollen, soll als Differentiation einer Matrizenfunktion bezeichnet werden. Es ist jedoch zu beachten, daß dieser Prozeß nur in einigen Punkten ähnliche Eigenschaften besitzt, wie die Differentiation der gewöhnlichen Analysis. Zum Beispiel sind hier die Produktregel der Differentiation oder die Regel für die Differentiation einer Funktion von einer Funktion nicht mehr allgemein in Gültigkeit. Nur dann, wenn alle vorkommenden Matrizen miteinander vertauschbar sind, gelten für diese Differentiation alle Regeln der gewöhnlichen Analysis.

Es sei

$$\mathbf{y} = \prod_{m=1}^s \mathbf{x}_{l_m} = \mathbf{x}_{l_1}\mathbf{x}_{l_2} \dots \mathbf{x}_{l_r} \quad (13)$$

Wir definieren

$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}_k} = \sum_{r=1}^s \delta_{l_r k} \prod_{m=r+1}^s \mathbf{x}_{l_m} \prod_{m=1}^{m=r-1} \mathbf{x}_{l_m}, \quad \begin{cases} \delta_{jk} = 0 \text{ für } j \neq k, \\ \delta_{kk} = 1. \end{cases} \quad (14)$$

In Worten lautet diese Regel: Man denke in dem gegebenen Produkt alle Faktoren einzeln angeschrieben (also z. B. nicht $\mathbf{x}_1^2 \mathbf{x}_2^2$, sondern

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

864

M. Born und P. Jordan,

eines Produkts sind invariant gegen zyklische Vertauschungen der Faktoren. Wegen (16) ist dieser Satz auch aus (10) zu folgern.

Zum Schluß dieser Vorbereitungen sollen den Funktionen $g(pq)$ von zwei Variablen noch einige Worte gewidmet werden. Für

$$y = p^s q^r \quad (18)$$

wird nach (14)

$$\frac{\partial y}{\partial p} = \sum_{l=0}^{s-1} p^{s-1-l} q^r p^l, \quad \frac{\partial y}{\partial q} = \sum_{j=0}^{r-1} q^{r-1-j} p^s q^j. \quad (18')$$

Die allgemeinste zu betrachtende Funktion $g(pq)$ ist nach § 1 darzustellen durch ein lineares Aggregat von Gliedern

$$z = \prod_{j=1}^k (p^{s_j} q^{r_j}). \quad (19)$$

Mit der Abkürzung

$$P_l = \prod_{j=l+1}^k (p^{s_j} q^{r_j}) \prod_{j=1}^{l-1} (p^{s_j} q^{r_j}) \quad (20)$$

können die Ableitungen geschrieben werden:

$$\left. \begin{aligned} \frac{\partial z}{\partial p} &= \sum_{l=1}^k \sum_{m=0}^{s_l-1} p^{s_l-1-m} q^{r_l} P_l p^m, \\ \frac{\partial z}{\partial q} &= \sum_{l=1}^k \sum_{m=0}^{r_l-1} q^{r_l-1-m} P_l p^{s_l} q^m. \end{aligned} \right\} \quad (21)$$

Aus diesen Gleichungen ist eine wichtige Folgerung zu ziehen. Wir betrachten die Matrizen

$$d_1 = q \frac{\partial z}{\partial q} - \frac{\partial z}{\partial q} q, \quad d_2 = p \frac{\partial z}{\partial p} - \frac{\partial z}{\partial p} p. \quad (22)$$

Nach (21) wird

$$d_1 = \sum_{l=1}^k (q^{r_l} P_l p^{s_l} - P_l p^{s_l} q^{r_l}),$$

$$d_2 = \sum_{l=1}^k (p^{s_l} q^{r_l} P_l - q^{r_l} P_l p^{s_l}),$$

und daraus folgt

$$d_1 + d_2 = \sum_{l=1}^k (p^{s_l} q^{r_l} P_l - P_l p^{s_l} q^{r_l}).$$

Hier hebt sich immer das zweite Glied eines Terms gegen das erste des folgenden, und auch das erste und letzte Glied der ganzen Summe zerstören sich. Also wird

$$d_1 + d_2 = 0. \quad (23)$$

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

866

M. Born und P. Jordan,

schieden sind, wenn $k = k_n = k_m$, also $n = m$ ist. Mithin ist $\tilde{p}$ die Reziproke von $p$:

$$\tilde{p} = p^{-1}.$$

Sei nun $a$ eine beliebige Matrix, so ist

$$pa = \left( \sum_k p(nk) a(km) \right) = (a(k_n, m))$$

eine Matrix, die aus $a$ durch die Permutation $\binom{n}{k_n}$ der Zeilen entsteht. und ebenso ist

$$ap^{-1} = \left( \sum_k a(nk) \tilde{p}(km) \right) = (a(n, k_m))$$

die durch Permutieren der Kolonnen entstehende Matrix. Ein und dieselbe Permutation auf Zeilen und Kolonnen angewandt, liefert also die Matrix

$$a' = pap^{-1}.$$

Hieraus folgt ohne weiteres:

$$\begin{aligned} a' + b' &= p(a + b)p^{-1} = (a + b)', \\ a'b' &= pabp^{-1} = (ab)', \end{aligned}$$

womit unsere Behauptung bewiesen ist.

Man sieht also, daß durch Matrizengleichungen irgend eine Reihenfolge oder Rangordnung der Elemente niemals bestimmt werden kann.

Übrigens gilt offenbar der viel allgemeinere Satz, daß jede Matrizengleichung invariant ist gegen Transformationen der Form

$$a' = bab^{-1},$$

wo $b$ eine beliebige Matrix bedeutet. Wir werden freilich später sehen, daß dies für Matrizen-Differentialgleichungen nicht mehr ohne weiteres richtig ist.

# Kapitel II. Dynamik.

§ 3. Die Grundgesetze. Das dynamische System ist zu beschreiben durch die Koordinate $q$ und den Impuls $p$. Sie sollen als Matrizen

$$q = (q(nm)e^{2\pi i r(nm)t}), \quad p = (p(nm)e^{2\pi i r(nm)t}) \quad (24)$$

angesetzt werden. Darin bedeuten die $v(nm)$ die quantentheoretischen Frequenzen, welche den Übergängen zwischen den Zuständen mit den Quantenzahlen $n$ und $m$ zugehören. Die Matrizen (24) sollen Hermitesche sein, d. h. bei Transposition der Matrizen soll jede Komponente in ihren konjugierten Wert übergehen, und zwar soll das für alle reellen $t$ gelten. Wir haben also

$$q(nm)q(mn) = |q(nm)|^2 \quad (25)$$

und

$$v(nm) = -v(mn). \quad (26)$$

Zur Quantenmechanik.

867

Ist $\boldsymbol{q}$ eine kartesische Koordinate, so ist die Größe (25) maßgebend für die Wahrscheinlichkeiten$^{1)}$ der Übergänge $n \rightleftarrows m$.

Wir wollen weiter fordern, daß

$$v(jk) + v(kl) + v(lj) = 0 \quad (27)$$

ist. Mit (26) zusammen kann das so ausgedrückt werden: Es gibt Größen $W_n$, so daß

$$h v(nm) = W_n - W_m \quad (28)$$

wird.

Daraus folgt, mit (2), (3), daß eine Funktion $\boldsymbol{g}(\boldsymbol{p}\boldsymbol{q})$ stets wieder die Form

$$\boldsymbol{g} = (g(nm) e^{2\pi i v(nm)t}) \quad (29)$$

erhält, und zwar geht dabei die Matrix $(g(nm))$ durch eben denselben Prozeß aus den Matrizen $(q(nm))$, $(p(nm))$ hervor, durch den $\boldsymbol{g}$ aus $\boldsymbol{q}$, $\boldsymbol{p}$ erhalten wurde. Wir können deshalb statt der von nun an aufzugebenden Darstellung (24) die kürzere Schreibweise

$$\boldsymbol{q} = (q(nm)), \boldsymbol{p} = (p(nm)) \quad (30)$$

wählen.

Als zeitliche Ableitung der Matrix $\boldsymbol{g} = (g(nm))$ erhalten wir, indem wir uns noch einmal an (24) bzw. (29) erinnern, die Matrix

$$\dot{\boldsymbol{g}} = 2\pi i (v(nm)g(nm)). \quad (31)$$

Wenn, wie wir annehmen wollen, $v(nm) \neq 0$ für $n \neq m$ ist, so bedeutet $\dot{\boldsymbol{g}} = 0$, daß $\boldsymbol{g}$ eine Diagonalmatrix mit $g(nm) = \delta_{nm}g(nn)$ ist.

Eine Differentialgleichung $\dot{\boldsymbol{g}} = \boldsymbol{a}$ ist invariant gegen den Prozeß, bei dem Zeilen und Kolonnen aller Matrizen sowie die Zahlen $W_n$ derselben Permutation unterworfen werden. Um dies einzusehen, betrachten wir die Diagonalmatrix

$$\boldsymbol{W} = (\delta_{nm}W_n);$$

dann ist

$$\boldsymbol{W}\boldsymbol{g} = (\sum_k \delta_{nk} W_n g(km)) = (W_n g(nm)),$$

$$\boldsymbol{g}\boldsymbol{W} = (\sum_k g(nk) \delta_{km} W_k) = (W_m g(nm)),$$

also nach (31)

$$\dot{\boldsymbol{g}} = \frac{2\pi i}{h} ((W_n - W_m)g(nm)) = \frac{2\pi i}{h} (\boldsymbol{W}\boldsymbol{g} - \boldsymbol{g}\boldsymbol{W}).$$

Ist nun $p$ eine Permutationsmatrix, so ist die Transformierte

$$\boldsymbol{W}' = \boldsymbol{p}\boldsymbol{W}\boldsymbol{p}^{-1} = (\delta_{n_k m} W_{n_k})$$

$^{1)}$ Siehe hierzu § 8.

868

M. Born und P. Jordan,

die Diagonalmatrix mit den permutierten $W_n$ in der Diagonale. Man hat daher

$$p \dot{g} p^{-1} = \frac{2 \pi i}{h} (W' g' - g' W') = \dot{g}',$$

wo $g' = p g p^{-1}$ ist und $\dot{g}'$ die nach der Regel (31) mit permutierten $W_n$ gebildete zeitliche Ableitung von $g'$ bedeutet.

Die Zeilen und Kolonnen von $\dot{g}$ erleiden also dieselbe Permutation wie die von $g$, und daraus folgt unsere Behauptung.

Zu beachten ist, daß ein entsprechender Satz für beliebige Transformation der Form $a' = b a b^{-1}$ nicht gilt; denn bei solchen ist $W'$ nicht mehr Diagonalmatrix. Trotz dieser Schwierigkeit scheint uns ein genaues Studium dieser allgemeinen Transformationen unerläßlich, weil es Einblick in die tieferen Zusammenhänge der neuen Theorie verspricht; wir werden später darauf zurückkommen$^{1)}$.

Für den Fall einer Hamiltonschen Funktion der Gestalt

$$H = \frac{1}{2 m} p^2 + U(q)$$

werden wir mit Heisenberg annehmen, daß die Bewegungsgleichungen ebenso wie die klassischen lauten, so daß wir mit der Symbolik von § 2 schreiben können:

$$\left. \begin{aligned} \dot{q} &= \frac{\partial H}{\partial p} = \frac{1}{m} p, \\ \dot{p} &= -\frac{\partial H}{\partial q} = -\frac{\partial U}{\partial q}. \end{aligned} \right\} \quad (32)$$

Es soll versucht werden, durch eine korrespondenzmäßige Betrachtung auch für den allgemeinen Fall einer beliebigen Hamiltonschen Funktion $H(p q)$ zugehörige Bewegungsgleichungen zu bestimmen. Das ist erforderlich in Rücksicht auf die relativistische Mechanik und besonders auf die Behandlung der Bewegung von Elektronen unter Mitwirkung magnetischer Felder. Denn in letzterem Falle kann die Funktion $H$ bei kartesischen Koordinaten nicht mehr dargestellt werden als Summe zweier Funktionen, deren eine nur von den Impulsen und deren andere nur von den Koordinaten abhängt.

Klassisch sind die Bewegungsgleichungen abzuleiten aus dem Wirkungsprinzip

$$\int_{t_0}^{t_1} L dt = \int_{t_0}^{t_1} \{p \dot{q} - H(p q)\} dt = \text{Extremum.} \quad (33)$$

$^{1)}$ Vgl. die demnächst erscheinende Fortsetzung dieser Arbeit.

Zur Quantenmechanik.

869

Denken wir uns darin die Fourierentwicklung von $L$ eingesetzt und nehmen wir den Zeitabschnitt $t_1 - t_0$ hinreichend groß, so wird nur das konstante Glied von $L$ einen Beitrag zum Integral liefern. Die Form, welche das Wirkungsprinzip damit erhält, legt folgende Übertragung in die Quantenmechanik nahe:

Die Diagonalsumme $D(L) = \sum_k L(kk)$ soll zum Extremum gemacht werden:

$$D(L) = D(\boldsymbol{p}\dot{\boldsymbol{q}} - \boldsymbol{H}(\boldsymbol{p}\boldsymbol{q})) = \text{Extremum}, \quad (34)$$

und zwar durch geeignete Wahl von $\boldsymbol{p}$ und $\boldsymbol{q}$ bei festgehaltenen $\boldsymbol{v}(nm)$.

Man erhält also, indem man die Ableitungen von $D(L)$ nach den Elementen von $\boldsymbol{p}$ und $\boldsymbol{q}$ gleich Null setzt, die Bewegungsgleichungen

$$\begin{aligned} 2\pi i \boldsymbol{v}(nm) q(nm) &= \frac{\partial D(\boldsymbol{H})}{\partial p(mn)}, \\ 2\pi i \boldsymbol{v}(mn) p(mn) &= \frac{\partial D(\boldsymbol{H})}{\partial q(mn)}. \end{aligned}$$

Nach (26), (31) und (16) erkennt man, daß diese Bewegungsgleichungen allgemein in der kanonischen Gestalt

$$\left. \begin{aligned} \dot{\boldsymbol{q}} &= \frac{\partial \boldsymbol{H}}{\partial \boldsymbol{p}}, \\ \dot{\boldsymbol{p}} &= -\frac{\partial \boldsymbol{H}}{\partial \boldsymbol{q}} \end{aligned} \right\} \quad (35)$$

geschrieben werden können.

Als Quantenbedingung verwendet Heisenberg eine von Thomas$^{1)}$ und Kuhn$^{2)}$ aufgestellte Beziehung. Die Gleichung

$$J = \oint p \, dq = \int_0^{1/r} p \, \dot{q} \, dt$$

der „klassischen“ Quantentheorie kann, wenn man die Fourierentwicklung von $p$ und $q$

$$p = \sum_{\tau=-\infty}^{\infty} p_\tau e^{2\pi i \nu \tau t}, \quad q = \sum_{\tau=-\infty}^{\infty} q_\tau e^{2\pi i \nu \tau t},$$

heranzieht, umgeformt werden in

$$1 = 2\pi i \sum_{\tau=-\infty}^{\infty} \tau \frac{\partial}{\partial J} (q_\tau p_{-\tau}). \quad (36)$$

$^{1)}$ W. Thomas, Naturw. **13**, 627, 1925.

$^{2)}$ W. Kuhn, ZS. f. Phys. **33**, 408, 1925.

870

M. Born und P. Jordan,

Ist dabei $p = m\dot{q}$, so können die $p_\tau$ durch die $q_\tau$ ausgedrückt werden, und man erhält so diejenige klassische Gleichung, deren korrespondenzmäßige Umformung in eine Differenzengleichung die Beziehung von Thomas und Kuhn ergibt. Da hier die Voraussetzung $p = m\dot{q}$ nicht gemacht werden soll, müssen wir die Gleichung (36) unmittelbar in eine Differenzengleichung übersetzen.

Es soll korrespondieren

$$\sum_{\tau=-\infty}^{\infty} \tau \frac{\partial}{\partial J} (q_\tau p_{-\tau}) \text{ mit } \frac{1}{h} \sum_{\tau=-\infty}^{\infty} (q(n+\tau, n) p(n, n+\tau) - q(n, n-\tau) p(n-\tau, n));$$

dabei sind rechts diejenigen $q(n m)$, $p(n, m)$, die einen negativen Index erhalten, gleich Null zu setzen. Dadurch erhalten wir als korrespondenzmäßige Umformung von (36) die Quantenbedingung

$$\sum_k (p(n k) q(kn) - q(n k) p(kn)) = \frac{h}{2\pi i}. \quad (37)$$

Das sind unendlich viele Gleichungen, nämlich je eine für jedes $n$. Für $p = m\dot{q}$ ergibt das insbesondere

$$\sum_k \nu(kn) |q(n k)|^2 = \frac{h}{8\pi^2 m},$$

was, wie leicht festzustellen, mit der Heisenbergschen Form der Quantenbedingung bzw. der Thomas-Kuhnschen Gleichung übereinstimmt. (37) muß als die sachgemäße Verallgemeinerung dieser Gleichung angesehen werden.

Übrigens erkennt man aus (37), daß die Diagonalsumme $D(pq)$ notwendig unendlich wird. Denn sonst würde aus (10) folgen $D(pq) - D(qp) = 0$, während (37) zu $D(pq) - D(qp) = \infty$ führt. Die betrachteten Matrizen sind also niemals endlich$^{1)}$.

§ 4. Folgerungen. Energie- und Frequenzsatz. Mit den Aufstellungen des vorigen Paragraphen sind die Grundgesetze der neuen Mechanik vollständig gegeben. Alle sonstigen Gesetze der Quantenmechanik, denen Allgemeingültigkeit zugesprochen werden soll, müssen aus ihnen heraus zu beweisen sein. Als solche zu beweisende Sätze kommen in erster Linie in Betracht der Energiesatz und die Bohrsche Frequenzbedingung. Der Energiesatz besagt, daß, wenn $H$ die Energie ist, $\dot{H} = 0$ wird, oder daß $H$ eine Diagonalmatrix ist. Die Diagonal-

$^{1)}$ Auch gehören sie nicht zu der von den Mathematikern bislang fast ausschließlich betrachteten Klasse der „beschränkten“ unendlichen Matrizen.

Zur Quantenmechanik.

871

glieder $H(n n)$ von $\pmb{H}$ werden dann nach Heisenberg als Energieen der verschiedenen Zustände des Systems gedeutet, und die Bohrsche Frequenzbedingung fordert

$$h \nu (n m) = H (n n) - H (m m),$$

oder

$$W_n = H (n n) + \text{konst.}$$

Wir betrachten die Größe

$$d = p q - q p.$$

Nach (11), (35) wird

$$\begin{aligned} \dot{d} &= \dot{p} q + p \dot{q} - \dot{q} p - q \dot{p} \\ &= q \frac{\partial H}{\partial q} - \frac{\partial H}{\partial q} q + p \frac{\partial H}{\partial p} - \frac{\partial H}{\partial p} p. \end{aligned}$$

Nach (22), (23) ist also $\dot{d} = 0$ und $d$ eine Diagonalmatrix. Die Diagonalglieder von $d$ sind aber gerade durch die Quantenbedingung (37) festgelegt. Zusammenfassend erhalten wir unter Benutzung der durch (6) definierten Einheitsmatrix $\pmb{I}$ die Gleichung

$$p q - q p = \frac{h}{2 \pi i} \pmb{I}, \quad (38)$$

die wir die „verschärfte Quantenbedingung“ nennen und auf der alle weiteren Schlüsse beruhen.

Aus der Form dieser Gleichung ist zu entnehmen: Wird aus (38) eine Gleichung ($A$) abgeleitet, so bleibt ($A$) richtig, wenn man $p$ mit $q$ vertauscht und gleichzeitig $h$ durch $-h$ ersetzt. Deshalb braucht z. B. von den Gleichungen

$$p^n q = q p^n + n \frac{h}{2 \pi i} p^{n-1}, \quad (39)$$

$$q^n p = p q^n - n \frac{h}{2 \pi i} q^{n-1} \quad (39')$$

nur eine aus (38) bewiesen zu werden, was durch Induktion leicht auszuführen ist.

Wir wollen jetzt Energie- und Frequenzsatz, wie sie oben ausgesprochen wurden, zunächst beweisen für den Fall

$$H = H_1(p) + H_2(q).$$

Nach den Ausführungen von § 1 können hierin $H_1(p)$ und $H_2(q)$ formal durch Potenzsummen

$$H_1 = \sum_s a_s p^s, \quad H_2 = \sum_s b_s q^s$$

872

M. Born und P. Jordan,

ersetzt werden. Die Formeln (39), (39') lassen dann erkennen, daß

$$\left. \begin{aligned} Hq - qH &= \frac{h}{2\pi i} \frac{\partial H}{\partial p}, \\ Hp - pH &= -\frac{h}{2\pi i} \frac{\partial H}{\partial q} \end{aligned} \right\} \quad (40)$$

wird, und der Vergleich mit den Bewegungsgleichungen (35) liefert

$$\left. \begin{aligned} \dot{q} &= \frac{2\pi i}{h} (Hq - qH), \\ \dot{p} &= \frac{2\pi i}{h} (Hp - pH). \end{aligned} \right\} \quad (41)$$

Wird nun die Matrix $Hg - gH$ kurz mit $\left| \begin{matrix} H \\ g \end{matrix} \right|$ bezeichnet, so gilt

$$\left| \begin{matrix} H \\ ab \end{matrix} \right| = \left| \begin{matrix} H \\ a \end{matrix} \right| b + a \left| \begin{matrix} H \\ b \end{matrix} \right|; \quad (42)$$

daraus ist aber allgemein für $g = g(pq)$

$$\dot{g} = \frac{2\pi i}{h} \left| \begin{matrix} H \\ g \end{matrix} \right| = \frac{2\pi i}{h} (Hg - gH) \quad (43)$$

zu folgern. Denn man braucht zum Beweise nur $\dot{g}$ vermittelst (11), (11') als Funktion von $p, q$ und $\dot{p}, \dot{q}$, sowie $\left| \begin{matrix} H \\ g \end{matrix} \right|$ vermittelst (42) als Funktion von $p, q$ und $\left| \begin{matrix} H \\ p \end{matrix} \right|, \left| \begin{matrix} H \\ q \end{matrix} \right|$ ausgerechnet und dann (41) angewandt zu denken. Setzt man in (43) insbesondere $g = H$, so erhält man

$$\dot{H} = 0. \quad (44)$$

Nachdem somit der Energiesatz bewiesen und $H$ als Diagonalmatrix erkannt ist, erhält (41) die Gestalt

$$\begin{aligned} hv(nm)q(nm) &= (H(nn) - H(mm))q(nm), \\ hv(nm)p(nm) &= (H(nn) - H(mm))p(nm), \end{aligned}$$

woraus die Frequenzbedingung folgt.

Gehen wir nun zu allgemeineren Hamiltonschen Funktionen $H^* = H^*(pq)$ über, so erkennt man leicht an Beispielen, wie etwa $H^* = p^2q$, daß im allgemeinen nicht mehr $\dot{H}^* = 0$ wird. Man sieht jedoch, daß die Hamiltonsche Funktion $H = \frac{1}{2}(p^2q + qp^2)$ dieselben Bewegungsgleichungen wie $H^*$ liefert und daß $\dot{H}$ wieder gleich Null wird. Wir sprechen danach Energie- und Frequenzsatz folgendermaßen aus: Zu jeder Funktion $H^* = H^*(pq)$ gibt es eine Funktion $H = H(pq)$, so daß $H^*$ und $H$ als Hamiltonsche

Zur Quantenmechanik.

873

Funktionen dieselben Bewegungsgleichungen liefern und daß $H$ für diese Bewegungsgleichungen die Rolle der zeitlich konstanten, die Frequenzbedingung erfüllenden Energie übernimmt.

Nach den oben durchgeführten Überlegungen genügt es, zu zeigen, daß die anzugebende Funktion $H$ außer

$$\frac{\partial H}{\partial p} = \frac{\partial H^*}{\partial p}, \quad \frac{\partial H}{\partial q} = \frac{\partial H^*}{\partial q} \quad (45)$$

noch die Gleichungen (40) befriedigt. Nach § 1 ist $H^*$ formal als Summe von Potenzprodukten in $p$ und $q$ darzustellen, und wegen der Linearität der Gleichungen (40), (45) in $H$, $H^*$ werden wir einfach für jeden einzelnen Summanden in $H^*$ den entsprechenden Summanden in $H$ anzugeben haben. Wir brauchen also nur den Fall

$$H^* = \prod_{j=1}^k (p^{r_j} q^{r_j}) \quad (46)$$

zu betrachten. Nach den Bemerkungen von § 2 sind die Gleichungen (45) zu erfüllen, indem $H$ als Linearform derjenigen Potenzprodukte in $p, q$ angesetzt wird, welche aus $H^*$ durch zyklische Vertauschungen der Faktoren entstehen; dabei muß nur die Summe der Koeffizienten gleich 1 gehalten werden. Weniger leicht beantwortet sich die Frage, wie diese Koeffizienten zu wählen sind, damit auch die Gleichungen (40) erfüllt werden. Es möge genügen, hier den Fall $k = 1$, also

$$H^* = p^r q^r \quad (47)$$

zu erledigen.

Die Formel (39) kann verallgemeinert werden zu ¹)

$$p^m q^n - q^n p^m = m \frac{h}{2\pi i} \sum_{l=0}^{n-1} q^{n-1-l} p^{m-l} q^l. \quad (48)$$

Für $n = 1$ ist das wieder (39); allgemein folgt (48) daraus, daß wegen (39)

$$p^m q^{n+1} - q^{n+1} p^m = (p^m q^n - q^n p^m) q + m \frac{h}{2\pi i} q^n p^{m+1}$$

¹) Eine andere Verallgemeinerung wird gegeben durch die Formeln

$$\begin{aligned} p^m q^n &= \sum_{j=0}^{m,n} j! \binom{m}{j} \binom{n}{j} \left(\frac{h}{2\pi i}\right)^j q^{n-j} p^{m-j}, \\ q^n p^m &= \sum_{j=0}^{m,n} j! \binom{m}{j} \binom{n}{j} \left(\frac{-h}{2\pi i}\right)^j p^{m-j} q^{n-j}, \end{aligned}$$

worin $j$ bis zur kleineren der Zahlen $m, n$ wächst.

874

M. Born und P. Jordan.

wird. Vertauschung von $p$ und $q$ mit Vorzeichenwechsel von $h$ ergibt die neue Formel

$$p^m q^n - q^n p^m = n \frac{h}{2\pi i} \sum_{j=0}^{m-1} p^{m-1-j} q^{n-1} p^j. \quad (48')$$

Vergleich mit (48) liefert

$$\frac{1}{s+1} \sum_{l=0}^s p^{s-l} q^r p^l = \frac{1}{r+1} \sum_{j=0}^r q^{r-j} p^s q^j. \quad (49)$$

Wir behaupten nun: Zu $H^*$ nach (47) gehört

$$H = \frac{1}{s+1} \sum_{l=0}^s p^{s-l} q^r p^l. \quad (50)$$

Beweisen müssen wir nur (40), wobei wir uns an Formel (18') aus § 2 zu erinnern haben.

Nun wird nach (50)

$$Hp - pH = \frac{1}{s+1} (q^r p^{s+1} - p^{s+1} q^r),$$

und nach (48) ist das gleichbedeutend mit der unteren Gleichung (40).

Unter Benutzung von (49) erhalten wir ferner

$$Hq - qH = \frac{1}{r+1} (p^s q^{r+1} - q^{r+1} p^s),$$

was nach (48') mit der oberen Gleichung (40) gleichwertig ist. Damit ist der verlangte Beweis vollständig geführt.

Während in der klassischen Mechanik die Energiekonstanz $\dot{H} = 0$ unmittelbar aus den kanonischen Gleichungen abgelesen werden kann, liegt der Energiesatz $\dot{H} = 0$ der Quantenmechanik, wie man sieht, viel weniger an der Oberfläche.

Wie weit seine Beweisbarkeit aus den gemachten Voraussetzungen davon entfernt ist, trivial zu sein, erkennt man, wenn man in engerer Anlehnung an das klassische Beweisverfahren die Konstanz von $H$ einfach durch Ausrechnen von $\dot{H}$ zu beweisen sucht. Man hat zu diesem Zweck zunächst vermittelst (11), (11') $\dot{H}$ als Funktion von $p$, $q$ und $\dot{p}$, $\dot{q}$ darzustellen, worauf für $\dot{p}$, $\dot{q}$ die Werte $-\frac{\partial H}{\partial q}$, $\frac{\partial H}{\partial p}$ einzuführen sind. Das ergibt $\dot{H}$ als Funktion von $p$ und $q$. Die Gleichung (38) bzw. die daraus abgeleiteten, in der Fußnote Seite 873 mitgeteilten Formeln erlauben, diese Funktion in eine Summe von Gliedern $a p^s q^r$ umzurechnen, und zu beweisen ist, daß der Koeffizient $a$ jedes solchen Gliedes verschwindet. Diese Rechnung wird für den allgemeinsten oben in anderer Weise

Zur Quantenmechanik.

875

erledigten Fall so überaus verwickelt¹), daß sie kaum durchführbar scheint. Wenn trotzdem Energie- und Frequenzsatz in so allgemeinem Umfange bewiesen werden konnten, so scheint uns das eine starke Stütze für die Hoffnung zu bieten, daß diese Theorie wirklich tiefe physikalische Gesetze erfaßt.

Zum Schluß sei hier noch ein Ergebnis verzeichnet, das aus den Formeln dieses Paragraphen leicht zu entnehmen ist: Die Gleichungen (35), (37) können ersetzt werden durch (38) und (44) (wo H die Energie bedeutet); die Frequenzen sind dabei aus der Frequenzbedingung zu bestimmen.

Auf die wichtigen Anwendungen, welche dieser Satz gestattet, gehen wir in der Fortsetzung dieser Arbeit ein.

# Kapitel III. Untersuchung des anharmonischen Oszillators.

Der anharmonische Oszillator mit

$$H = \frac{1}{2} p^2 + \frac{\omega_0^2}{2} q^2 + \frac{1}{3} \lambda q^3 \quad (51)$$

ist bereits von Heisenberg eingehend betrachtet worden. Trotzdem soll ihm hier eine erneute Untersuchung gewidmet werden, und zwar mit dem Ziel, die allgemeinste Lösung der Grundgleichungen für diesen Fall festzustellen. Wenn die Grundgleichungen der Theorie wirklich vollständig sind und keiner Ergänzung mehr bedürfen, so werden die Absolutwerte $|q(nm)|$, $|p(nm)|$ der Komponenten von $q$ und $p$ durch sie eindeutig festgelegt sein müssen, und es wird wichtig sein, dies am Beispiel (51) zu prüfen. Dagegen ist zu erwarten, daß bezüglich der Phasen $\varphi_{nm}$, $\psi_{nm}$ in

$$q(nm) = |q(nm)| e^{i\varphi_{nm}},$$

$$p(nm) = |p(nm)| e^{i\psi_{nm}}$$

noch eine Unbestimmtheit bestehen bleibt. Für die Statistik z. B. der Wechselwirkung von Quantenatomen mit äußeren Strahlungsfeldern wird es von grundlegender Bedeutung sein, den Grad dieser Unbestimmtheit genau festzulegen.

§ 5. Harmonischer Oszillator. Der Ausgangspunkt unserer Überlegungen ist die Theorie des harmonischen Oszillators; für kleine $\lambda$

¹) Für den Fall $H = \frac{1}{2m} p^2 + U(q)$ kann sie mit Hilfe von (39') sofort ausgeführt werden.

Zeitschrift für Physik, Bd. XXXIV.

58

876

M. Born und P. Jordan,

kann man die Bewegung nach Gleichung (51) als Störung der harmonischen Schwingung mit der Energie

$$H = \frac{1}{2} p^2 + \frac{\omega_0^2}{2} q^2 \quad (52)$$

auffassen.

Auch bei diesem einfachen Problem ist eine Ergänzung der Heisenberg'schen Betrachtungen notwendig. Dieser entnimmt einer Korrespondenzüberlegung eine wesentliche Aussage über die Form der Lösung; da nämlich klassisch nur eine harmonische Komponente vorhanden ist, setzt Heisenberg eine Matrix an, die nur Übergänge zwischen Nachbarzuständen darstellt, also die Form hat

$$q = \begin{pmatrix} 0 & q^{(01)} & 0 & 0 & 0 & \dots \\ q^{(10)} & 0 & q^{(12)} & 0 & 0 & \dots \\ 0 & q^{(21)} & 0 & q^{(23)} & 0 & \dots \\ \dots & \dots & \dots & \dots & \dots & \dots \end{pmatrix}. \quad (53)$$

Unser Bestreben ist, die ganze Theorie selbständig aufzubauen, ohne aus der klassischen Theorie Hilfe auf Grund des Korrespondenzprinzips heranzuholen. Daher werden wir untersuchen, ob sich nicht die Form (53) der Matrix aus den Grundgleichungen selbst ableiten läßt, bzw., wenn das nicht geht, welche Zusatzforderungen zu stellen sind.

Man sieht ohne weiteres aus dem in § 3 über die Invarianz gegen Permutationen von Zeilen und Kolonnen Gesagten, daß die exakte Form der Matrix (53) niemals aus den Grundgleichungen erschlossen werden kann; denn vertauscht man Zeilen und Kolonnen in gleicher Weise, so bleiben die kanonischen Gleichungen und die Quantenbedingung invariant, also hat man damit eine neue, scheinbar verschiedene Lösung gefunden. Aber alle diese Lösungen sind natürlich nur der Schreibweise, d. h. der Numerierung der Elemente nach verschieden. Wir wollen beweisen, daß durch eine bloße Umnumerierung der Elemente die Lösung stets auf die Form (53) gebracht werden kann. Die Bewegungsgleichung

$$\ddot{q} + \omega_0^2 q = 0 \quad (54)$$

lautet für die Elemente:

$$(v^2 (nm) - v_0^2) q (nm) = 0, \quad (55)$$

wo

$$\omega^0 = 2\pi v_0, \quad h\nu (nm) = W_n - W_m.$$

Aus der verschärften Quantenbedingung

$$pq - qp = \frac{h}{2\pi i} I \quad (56)$$

Zur Quantenmechanik.

877

folgt, daß zu jedem $n$ ein $n'$ existieren muß, so daß $q(nn') \neq 0$ ist; denn gäbe es ein $n$, für das alle $q(nn') = 0$ wären, so wäre das $n$ te Diagonalglied von $pq - qp$ gleich Null, was der Quantenbedingung widerspricht. Danach ergibt (55), daß stets ein $n'$ existiert, für das

$$|W_n - W_{n'}| = h\nu_0$$

ist. Da wir aber in unseren Grundprinzipien angenommen haben, daß für $n \neq m$ immer $W_n \neq W_m$ ist, so können höchstens zwei solche Indizes, $n'$ und $n''$, existieren; denn die zugehörigen $W_{n'}$, $W_{n''}$ sind Lösungen der quadratischen Gleichung

$$(W_n - x)^2 = h^2\nu_0^2;$$

wenn wirklich zwei solche Indizes $n'$, $n''$ existieren, folgt für die zugehörigen Frequenzen

$$\nu(nn') = -\nu(nn''). \quad (57)$$

Nunmehr wird aus (56)

$$\sum_k \nu(kn)|q(nk)|^2 = \nu(n'n)\{|q(nn')|^2 - |q(nn'')|^2\} = \frac{h}{8\pi^2}, \quad (58)$$

und die Energie (52) wird:

$$\begin{aligned} H(nm) &= \frac{1}{2}4\pi^2 \sum_k \{-\nu(nk)\nu(km)q(nk)q(km) + \nu_0^2 q(nk)q(km)\} \\ &= 2\pi^2 \sum_k q(nk)q(km)\{\nu_0^2 - \nu(nk)\nu(km)\}. \end{aligned}$$

Insbesondere gilt für $m = n$:

$$H(nn) = W_n = 4\pi^2 \nu_0^2 (|q(nn')|^2 + |q(nn'')|^2). \quad (59)$$

Es sind nun weiter drei Fälle möglich:

- a) Es gibt kein $n''$ und es ist $W_{n'} > W_n$;
- b) es gibt kein $n''$ und es ist $W_{n'} < W_n$;
- c) es gibt $n''$.

Im Falle b) betrachten wir statt $n$ jetzt $n'$; zu diesem gehören höchstens zwei Indizes $(n')'$ und $(n')'$, und von diesen muß einer gleich $n$ sein. Damit kommen wir auf einen der Fälle a) oder c) zurück und können deshalb b) fortlassen.

Im Falle a) wird $\nu(n'n) = +\nu_0$, und aus (58) folgt:

$$\nu_0 \cdot |q(nn')|^2 = \frac{h}{8\pi^2}, \quad (60)$$

also nach (59):

$$W_n = H(nn) = 4\pi^2 \nu_0^2 |q(nn')|^2 = \frac{1}{2}\nu_0 h.$$

Wegen der Voraussetzung $W_n \neq W_m$ für $n \neq m$ gibt es also höchstens einen Index $n = n_0$, für den der Fall a) vorliegt.

58*

878

M. Born und P. Jordan,

Wenn ein solches $n_0$ existiert, können wir eine Reihe von Zahlen

$$n_0, n_1, n_2, n_3 \dots$$

angeben derart, daß

$$(n_k)' = n_{k+1} \quad \text{und} \quad W_{k+1} > W_k$$

Dann ist jedesmal

$$(n_{k+1})'' = n_k$$

Also wird für $k > 0$ aus (58) und (59):

$$H(n_k, n_k) = 4\pi^2 v_0^2 \{|q(n_k, n_{k+1})|^2 + |q(n_k, n_{k-1})|^2\}, \quad (61)$$

$$\frac{1}{2}h = 4\pi^2 v_0 \{|q(n_k, n_{k+1})|^2 - |q(n_k, n_{k-1})|^2\}. \quad (62)$$

Aus (60) und (62) folgt

$$|q(n_k, n_{k+1})|^2 = \frac{h}{8\pi^2 v_0} (k+1), \quad (63)$$

und dann aus (61)

$$W_{n_k} = H(n_k, n_k) = v_0 h(k + \frac{1}{2}). \quad (64)$$

Nun wollen wir noch sehen, ob es möglich ist, daß es kein $n$ gibt, für das der Fall a) gilt. Wir können dann, mit beliebigem $n_0$ anfangend, $n_0' = n_1$ und $n_0'' = n_{-1}$ bilden; zu jedem von diesen wieder $n_1' = n_2$, $n_1'' = n_0$ und $n_{-1}' = n_0$, $n_{-1}'' = n_{-2}$ usw. Auf diese Weise erhalten wir eine Zahlenreihe

$$\dots n_{-2}, n_{-1}, n_0, n_1, n_2 \dots \quad (65)$$

und es gelten die Gleichungen (61), (62) für jedes $k$ zwischen $-\infty$ und $+\infty$. Das ist aber unmöglich; denn nach (62) bilden die Größen $x_k = |q(n_{k+1}, n_k)|^2$ eine äquidistante Zahlenreihe, und da sie positiv sind, muß es eine kleinste geben. Den entsprechenden Index können wir wieder mit $n_0$ bezeichnen und kommen damit auf den vorigen Fall zurück; es gelten also auch hier die Formeln (63), (64).

Man sieht ferner: jede Zahl $n$ muß unter den Zahlen $n_k$ enthalten sein; denn sonst könnte man mit $n$ als Ausgangsgliede eine neue Reihe (65) bilden, wobei wieder die Formel (60) gilt. Die Ausgangsglieder beider Reihen hätten also dieselben Werte $W_n = H(nn)$, was unmöglich ist.

Damit ist der Beweis geführt, daß die Indizes 0, 1, 2, 3 ... so in eine neue Reihenfolge $n_0, n_1, n_2, n_3 \dots$ umgeordnet werden können, daß die Formeln (63), (64) gelten; in diesen neuen Indizes hat dann die Lösung die Heisenbergsche Form (53). Diese erscheint also als „Normalform“ der allgemeinen Lösung. Sie hat nach (64) die Eigenschaft, daß

$$W_{n_{k+1}} > W_{n_k}$$

Fordert man umgekehrt, daß $W_n = H(nn)$ mit $n$ stets wachsen soll, so wird notwendig $n_k = k$; dieses Prinzip legt also die Normalform

Zur Quantenmechanik.

879

eindeutig fest. Aber hierdurch wird nur die Schreibweise fixiert und die Rechnung übersichtlicher gestaltet; physikalisch ist nichts Neues dadurch gegeben.

Darin liegt ein tiefer Unterschied gegenüber der bisher gebräuchlichen halbklassischen Bestimmung der stationären Zustände. Die klassisch berechneten Bahnen schließen sich kontinuierlich aneinander, wodurch auch in die nachträglich ausgesonderten Quantenbahnen von vornherein eine bestimmte Reihenfolge kommt. Die neue Mechanik stellt sich als wahre Diskontinuumstheorie dar, indem hier von solcher durch den physikalischen Vorgang definierten Reihenfolge der Quantenzustände keine Rede ist, sondern die Quantenzahlen wirklich nichts sind als unterscheidende Indizes, die man nach irgendwelchen praktischen Gesichtspunkten (z. B. nach wachsender Energie $W_n$) ordnen und normieren kann.

§ 6. Anharmonischer Oszillator. Die Bewegungsgleichungen

$$\ddot{\boldsymbol{q}} + \omega_0^2 \boldsymbol{q} + \lambda \boldsymbol{q}^2 = 0 \quad (66)$$

geben zusammen mit der Quantenbedingung folgendes Gleichungssystem für die Elemente:

$$\left. \begin{aligned} (\omega_0^2 - \omega^2(n m)) q(n m) + \lambda \sum_k q(n k) q(k m) &= 0, \\ \sum_k \omega(n k) q(n k) q(k n) &= -\frac{h}{4\pi}. \end{aligned} \right\} \quad (67)$$

Wir suchen es durch Reihenentwicklungen

$$\left. \begin{aligned} \omega(n m) &= \omega^0(n m) + \lambda \omega^{(1)}(n m) + \lambda^2 \omega^{(2)}(n m) + \dots \\ q(n m) &= q^0(n m) + \lambda q^{(1)}(n m) + \lambda^2 q^{(2)}(n m) + \dots \end{aligned} \right\} \quad (68)$$

zu lösen.

Für $\lambda = 0$ hat man den im vorigen Paragraphen behandelten Fall des harmonischen Oszillators; wir schreiben die Lösung (53) in der Form

$$q^0(n m) = a_n \delta_{n, m-1} + \bar{a}_m \delta_{n-1, m}, \quad (69)$$

wo das Überstreichen die konjugiert-komplexe Größe bezeichnen soll. Bildet man das Quadrat und höhere Potenzen der Matrix $\boldsymbol{q}^0 = (q^0(n m))$, so treten Matrizen von ähnlicher Form auf, nämlich Summen von Gliedern

$$(\xi)_{n m}^{(p)} = \xi_n \delta_{n, m-p} + \bar{\xi}_m \delta_{n-p, m}. \quad (70)$$

Daher liegt es nahe, die Lösung in der Form

$$\left. \begin{aligned} q^0(n m) &= (a)_{n m}^{(1)}, \\ q^{(1)}(n m) &= (x)_{n m}^0 + (x')_{n m}^{(2)}, \\ q^{(2)}(n m) &= (y)_{n m}^{(1)} + (y')_{n m}^{(3)}, \\ \dots & \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \end{aligned} \right\} \quad (71)$$

880

M. Born und P. Jordan,

anzusetzen, wobei immer ungerade und gerade Werte des Index $p$ ab wechseln.

In der Tat, setzt man das in die Näherungsgleichungen

$$\lambda : \left\{ \begin{array}{l} \left( \omega_0^2 - \omega^0(nm)^2 \right) q^{(1)}(nm) - 2\omega^0(nm)\omega^{(1)}(nm)q^0(nm) \\ \quad + \sum_k q_0(nk)q^0(km) = 0, \\ \sum_k \left\{ \omega^0(nk) \left( q^0(nk)q^{(1)}(kn) + q^{(1)}(nk)q^0(kn) \right) \right. \\ \quad \left. \left. + \omega^{(1)}(nk)q^0(nk)q^0(kn) \right\} = 0, \end{array} \right. \right\} \quad (72)$$

$$\lambda^2 : \left\{ \begin{array}{l} \left( \omega_0^2 - \omega^0(nm)^2 \right) q^{(2)}(nm) - 2\omega^0(nm)\omega^{(1)}(nm)q^{(1)}(nm) \\ \quad - \left( \omega^{(1)}(nm)^2 + 2\omega^0(nm)\omega^{(2)}(nm) \right) q^0(nm) \\ \quad + \sum_k \left( q^0(nk)q^{(1)}(km) + q^{(1)}(nk)q^0(km) \right) = 0, \\ \sum_k \left\{ \omega^0(nk) \left( q^0(nk)q^{(2)}(km) + q^{(1)}(nk)q^{(1)}(km) \right. \right. \\ \quad \left. \left. + q^{(2)}(nk)q^0(km) \right) + \omega^{(1)}(nk) \left( q^0(nk)q^{(1)}(km) \right. \right. \\ \quad \left. \left. + q^{(1)}(nk)q^0(km) \right) + \omega^{(2)}(nk)q^0(nk)q^0(km) \right\} = 0 \end{array} \right\} \quad (73)$$

ein und beachtet die Multiplikationsregel

$$\left. \begin{array}{l} \sum_k \Omega_{nkm}(\xi)_{nk}^{(p)}(\eta)_{km}^{(q)} = \Omega_{n,n+p,n+p+q} \xi_n \eta_{m+p} \delta_{n,m-p-q} \\ \quad + \Omega_{n,n+p,n+p-q} \xi_n \bar{\eta}_{n+p-q} \delta_{n,m-p+q} \\ \quad + \Omega_{n,n-p,n-p+q} \bar{\xi}_{n-p} \eta_{n-p} \delta_{n,m+p-q} \\ \quad + \Omega_{n,n-p,n-p-q} \bar{\xi}_{n-p} \eta_{n-p-q} \delta_{n,m+p+q} \end{array} \right\} \quad (74)$$

so sieht man, indem man die Faktoren von $\delta_{n,m-s}$ einzeln Null setzt, daß sich durch den Ansatz (71) alle Bedingungen gerade erfüllen lassen und daß höhere Glieder in (71) identisch verschwinden würden.

Im einzelnen gibt die Rechnung folgendes:

Die erste der Gleichungen (72) liefert nach Einsetzen der Ausdrücke (71):

$$\left. \begin{array}{l} 2\omega_0^2 x_n + |a_n|^2 + |a_{n-1}|^2 = 0, \\ - 3\omega_0^2 x_{n'} + a_n a_{n+1} = 0, \\ \omega_{n,n-1}^{(1)} = 0, \end{array} \right\} \quad (75)$$

die zweite ist identisch erfüllt. Man hat also:

$$\left. \begin{array}{l} x_n = - \frac{|a_n|^2 + |a_{n-1}|^2}{2\omega_0^2}, \\ x_n' = \frac{a_n a_{n+1}}{3\omega_0^2}. \end{array} \right\} \quad (76)$$

Zur Quantenmechanik.

881

Die erste der Gleichungen (73) liefert:

$$\left. \begin{aligned} 2 \omega_0 a_n \omega_{n,n+1}^{(2)} + 2 a_n x_{n+1} + 2 a_n x_n + \bar{a}_{n-1} x'_{n-1} + a_{n+1} x'_n &= 0, \\ - 8 \omega_0^2 y'_n + a_n x'_{n+1} + a_{n+2} x'_n &= 0, \\ \omega_{n,n-2}^{(1)} &= 0, \end{aligned} \right\} (77)$$

die zweite Gleichung ist nicht identisch erfüllt, sondern liefert eine Bestimmungsgleichung für $y_n$:

$$\left. \begin{aligned} a_n \bar{y}_n + \bar{a}_n y_n - a_{n-1} \bar{y}_{n-1} - \bar{a}_{n-1} y_{n-1} + 2 |x'|^2 - 2 |x'_{n-2}|^2 \\ - \frac{\omega_{n,n+1}^{(2)}}{\omega_0} |a_n|^2 - \frac{\omega_{n,n-1}^{(2)}}{\omega_0} |a_{n-1}|^2 &= 0. \end{aligned} \right\} (78)$$

Die Lösung lautet:

$$\left. \begin{aligned} \omega_{n,n+1}^{(2)} &= \frac{1}{3 \omega_0^3} (|a_{n+1}|^2 + |a_{n-1}|^2 + 3 |a_n|^2), \\ y'_n &= \frac{1}{12 \omega_0^4} a_n a_{n+1} a_{n+2}. \end{aligned} \right\} (79)$$

Setzt man ferner zur Abkürzung

$$\eta_n = a_n \bar{y}_n + \bar{a}_n y_n, \quad (80)$$

so bestimmt sich $\eta$ aus der Gleichung

$$\left. \begin{aligned} \eta_n - \eta_{n-1} &= \frac{1}{\omega_0^4} (|a_n|^4 - |a_{n-1}|^4 + \frac{1}{9} |a_n|^2 |a_{n+1}|^2 \\ - \frac{1}{9} |a_{n-1}|^2 |a_{n-2}|^2). \end{aligned} \right\} (81)$$

Die Ausdrücke (76) und (79) zeigen, daß die Größen $x_n, x'_n, y'_n$ sich durch die Lösung der nullten Näherung $a_n$ ausdrücken. Ihre Phasen sind also durch die des harmonischen Oszillators festgelegt. Anders scheint es bei der Größe $y_n$ zu liegen; denn zwar ist $\eta_n$ aus (81) eindeutig zu bestimmen, aber dann läßt sich $y_n$ aus (80) nicht völlig festlegen. Es ist wahrscheinlich, daß bei der folgenden Näherung eine ergänzende Bestimmungsgleichung für $y_n$ entsteht; wir müssen diese Frage hier offen lassen, möchten aber auf ihre prinzipielle Bedeutung für die Geschlossenheit der ganzen Theorie hinweisen. Denn es kommt für alle statistischen Fragen durchaus darauf an, ob unsere Vermutung richtig ist, daß von den Phasen der $q(nm)$ eine in jeder Zeile (oder in jeder Kolonne) der Matrix unbestimmt bleibt.

Zum Schluß wollen wir die expliziten Formeln angeben, die man erhält, wenn man die vorher (§ 5) gefundene Lösung des harmonischen

882

M. Born und P. Jordan,

Oszillators einsetzt. Diese lautet in der Normalform nach (63):

$$a_n = \sqrt{C(n+1)} e^{i\varphi_n}, \quad C = \frac{h}{4\pi\omega_0} = \frac{h}{8\pi^2 v_0}. \quad (82)$$

Damit erhält man nach (76), (79), (81):

$$\left. \begin{aligned} x_n &= -\frac{C}{2\omega_0^3}(2n+1), \\ x_n' &= \frac{C}{3\omega_0^3}\sqrt{(n+1)(n+2)}e^{i(\varphi_n + \varphi_{n+1})}, \\ y_n &= \frac{\sqrt{C^3}}{12\omega_0^4}\sqrt{(n+1)(n+2)(n+3)}e^{i(\varphi_n + \varphi_{n+1} + \varphi_{n+2})}; \\ &\omega_{n,n-1}^{(1)} = 0, \quad \omega_{n,n-2}^{(1)} = 0, \\ &\omega_{n,n-1}^{(2)} = -\frac{5}{3}\frac{C}{\omega_0^3}n; \end{aligned} \right\} \quad (83) \quad (84)$$

also

$$\eta_n - \eta_{n-1} = \frac{11}{9}\frac{C^2}{\omega_0^4}(2n+1),$$

$$\eta_n = a_n\bar{y}_n + \bar{a}_n y_n = \frac{11}{9}\frac{C^2}{\omega_0^4}(n+1)^2.$$

Setzt man $y_n = |y_n|e^{i\psi_n}$, so wird

$$|y_n|\cos(\varphi_n - \psi_n) = \frac{\eta_n}{2|a_n|} = \frac{11}{18}\frac{\sqrt{C^3}}{\omega_0^4}\sqrt{n+1}^3. \quad (85)$$

Mehr läßt sich in dieser Näherung über $y_n$ nicht aussagen.

Wir wollen aber die Schlußformeln unter der Annahme $\psi_n = \varphi_n$ ausschreiben. Dann lauten sie (bis auf Glieder von höherer als zweiter Ordnung in $\lambda$):

$$\left. \begin{aligned} \omega(n,n-1) &= \omega_0 - \lambda^2\frac{5}{3}\frac{C}{\omega_0^3}n + \dots, \\ \omega(n,n-2) &= 2\omega_0 + \dots; \end{aligned} \right\} \quad (86)$$

$$\left. \begin{aligned} q(n,n) &= -\lambda\frac{C}{\omega_0^3}(2n+1) + \dots, \\ q(n,n-1) &= \sqrt{Cn}e^{i\varphi_{n-1}}\left(1 + \lambda^2\frac{11}{18}\frac{Cn}{\omega_0^4} + \dots\right), \\ q(n,n-2) &= \lambda\frac{C}{3\omega_0^3}\sqrt{n(n-1)}e^{i(\varphi_{n-1} + \varphi_{n-2})} + \dots, \\ q(n,n-3) &= \lambda^2\frac{\sqrt{C^3}}{12\omega_0^4}\sqrt{n(n-1)(n-2)}e^{i(\varphi_{n-1} + \varphi_{n-2} + \varphi_{n-3})} + \dots \end{aligned} \right\} \quad (87)$$

Zur Quantenmechanik.

883

Wir haben auch die Energie direkt ausgerechnet und gefunden:

$$W_n = h\nu_0\left(n + \frac{1}{2}\right) - \lambda^2 \frac{5}{3} \frac{C^2}{\omega_0^2} \left(n(n+1) + \frac{17}{30}\right) + \cdots \quad (88)$$

Die Frequenzbedingung ist in der Tat erfüllt, denn man hat mit Rücksicht auf (82):

$$W_n - W_{n-1} = h\nu_0 - \lambda^2 \frac{2 C^2}{\omega_0^2} n + \cdots = \frac{h}{2\pi} \omega(n, n-1),$$

$$W_n - W_{n-2} = 2h\nu_0 + \cdots = \frac{h}{2\pi} \omega(n, n-2).$$

An die Formel (88) kann man mit Heisenberg die Bemerkung knüpfen, daß schon in den Gliedern niederster Ordnung eine Abweichung von der klassischen Theorie vorhanden ist, die man durch Einführung einer „halbzahligen“ Quantenzahl $n' = n + \frac{1}{2}$ formal beheben kann. Übrigens stimmen unsere Ausdrücke $\omega(n, n-1)$ nach (86) und die klassischen Frequenzen genau überein. Denn die klassische Energie ist ¹):

$$W_n^{(kl)} = h\nu_0 n - \lambda^2 \cdot \frac{5}{3} \frac{C^2}{\omega_0^2} n^2 + \cdots,$$

also die klassische Frequenz:

$$\begin{aligned} \omega_{kl} &= \frac{1}{h} \frac{\partial W_n^{(kl)}}{\partial n} = h\nu_0 - \lambda^2 \frac{5}{3} \frac{C^2}{\omega_0^2} n + \cdots \\ &= \omega_{qu}(n, n-1) = \frac{1}{h} \left( W_n^{(qu)} - W_{n-1}^{(qu)} \right). \end{aligned}$$

Wir haben schließlich geprüft, daß der Ausdruck (88) auch aus der Kramers-Bornschen Störungsformel erhalten werden kann (bis auf die additive Konstante).

#### Kapitel IV. Bemerkungen zur Elektrodynamik.

Nach Heisenberg sollen die Quadrate der Absolutwerte $|q(nm)|^2$ der Elemente von $\boldsymbol{q}$ für den Fall, daß $\boldsymbol{q}$ kartesische Koordinate ist, maßgebend für die Sprungwahrscheinlichkeiten sein. Wir möchten hier zum Schluß noch ausführen, in welcher Weise diese Annahme aus allgemeineren Überlegungen heraus eine Begründung erhalten kann. Notwendig ist dazu ein Eingehen auf die Frage, wie die Grundgleichungen der Elektrodynamik im Sinne der neuen Theorie umzudeuten sind. Wir möchten aber betonen, daß die hier mitgeteilten Überlegungen nur vorläufigen Charakter haben; sie sollen unsere grundsätzliche Stellungnahme zu der Aufgabe erkennen lassen. Eine ausführliche Behandlung der hier

¹) S. M. Born, Atommechanik (Berlin 1925), 4. Kapitel, § 42, S. 294; in der Formel (6) ist $a = 1/3$ zu setzen, um mit unserem Ansatz in Übereinstimmung zu kommen.

884

M. Born und P. Jordan,

auftretenden Fragen soll später gegeben werden, wobei vor allem das Verhältnis der dargelegten Theorie zur Theorie der Lichtquanten erörtert werden wird.

Wir wollen hier nur solche Punkte zur Sprache bringen, die ohne Eingehen auf die exakte Form der Quantenbedingung für Systeme von mehreren Freiheitsgraden gewonnen werden können. Daß man dabei in der Elektrodynamik bereits ziemlich weit kommt, kann man durch folgende Überlegung einsehen. Der elektromagnetisch schwingende Hohlraum stellt ein System von unendlich vielen Freiheitsgraden dar. Trotzdem reichen die in den vorangehenden Kapiteln entwickelten Grundsätze, die sich ja nur auf Systeme von einem Freiheitsgrad beziehen, zu seiner Behandlung aus, weil er, nach Eigenschwingungen analysiert, in ein System ungekoppelter Oszillatoren übergeht. Es ist kaum ein Zweifel möglich, wie man dieses System zu behandeln hat. Dabei erweist sich der Umstand, daß die elektromagnetischen Grundgleichungen linear sind (Superpositionsprinzip), von besonderer Bedeutung; denn daraus folgt, daß die Ersatz-Oszillatoren harmonisch sind, und gerade beim harmonischen Oszillator besteht — im Gegensatz zum Verhalten anderer Systeme — die Gültigkeit des Energiesatzes unabhängig von der Quantenbedingung: Aus

$$H = \frac{1}{2}(p^2 + \omega_0^2 q^2)$$

folgt

$$\begin{aligned} \dot{H} &= \frac{1}{2}(\dot{p}p + p\dot{p} + \omega_0^2 \dot{q}q + \omega_0^2 q\dot{q}) \\ &= \frac{1}{2}\omega_0^2(-qp - pq + pq + qp) \\ &= 0. \end{aligned}$$

Man wird daher erwarten, daß in entsprechender Weise die Integralsätze der Elektrodynamik des Vakuums (Energie- und Impulssatz) ganz allgemein aus den matrizenmäßig umgedeuteten Maxwellschen Gleichungen allein ohne Eingehen auf die Quantenbedingung zu gewinnen sind. Indem wir dies zeigen, gewinnen wir zugleich das Mittel, die Heisenbergsche Behauptung von der Bedeutung der $|q(nm)|^2$ zu begründen.

§ 7. Maxwellsche Gleichungen, Energie- und Impulssatz. Wir wollen verabreden, daß Vektoren; wie üblich, stets durch deutsche Buchstaben bezeichnet werden, während die Unterscheidung von Zahlen und Matrizen durch Schwach- und Fettdruck beibehalten wird. Die Maßeinheiten wählen wir im Anschluß an das Lehrbuch von Abraham¹).

Die elektromagnetischen Vorgänge im Vakuum wird man darstellen können als Superposition ebener Wellen. In einer solchen ebenen Welle

¹) M. Abraham, Theorie der Elektrizität, II. Leipzig 1914.

Zur Quantenmechanik.

885

werden wir die elektrische und die magnetische Feldstärke $\mathfrak{E}$, $\mathfrak{H}$ als Matrizen ansehen, deren Elemente harmonisch schwingende ebene Wellen sind, also z. B. bei geeigneter Lage des Koordinatensystems

$$\mathfrak{E} = \left( \mathfrak{E}(nm) e^{2\pi i r (nm) \left( t - \frac{x}{c} \right)} \right). \quad (89)$$

Freilich muß damit gerechnet werden, daß $n, m$ sich im allgemeinen nicht mehr auf eine diskrete Menge von Werten beschränken und auch nicht mehr einzelne Zahlen, sondern Zahlensysteme (Vektoren) bezeichnen.

Die Maxwellschen Gleichungen wird man als Matrizengleichungen beibehalten:

$$\text{rot } \mathfrak{H} - \frac{1}{c} \dot{\mathfrak{E}} = 0, \quad \text{rot } \mathfrak{E} + \frac{1}{c} \dot{\mathfrak{H}} = 0. \quad (90)$$

Die Differentiationen nach $x, y, z, t$ sind dabei in jedem einzelnen Element der Matrix ausgeführt zu denken$^{1)}$.

Wir wollen nun den Energie-Impulssatz ableiten; dazu ist es notwendig, einige Bemerkungen über die Multiplikation von Matrizenvektoren vorauszuschicken.

Wir definieren das skalare Produkt durch

$$(\mathfrak{A}, \mathfrak{B}) = \mathfrak{A}\mathfrak{B} = \mathfrak{A}_x \mathfrak{B}_x + \mathfrak{A}_y \mathfrak{B}_y + \mathfrak{A}_z \mathfrak{B}_z, \quad (91)$$

das Vektorprodukt durch

$$[\mathfrak{A}\mathfrak{B}]_x = \mathfrak{A}_y \mathfrak{B}_z - \mathfrak{A}_z \mathfrak{B}_y. \quad (92)$$

Da die Matrizenmultiplikation nicht kommutativ ist, gelten die Beziehungen

$$\mathfrak{A}\mathfrak{B} = \mathfrak{B}\mathfrak{A}, \quad [\mathfrak{A}\mathfrak{B}] = -[\mathfrak{B}\mathfrak{A}]$$

im allgemeinen nicht.

Dagegen behaupten wir:

$$\text{div } [\mathfrak{A}\mathfrak{B}] = (\text{rot } \mathfrak{A}, \mathfrak{B}) - (\mathfrak{A}, \text{rot } \mathfrak{B}). \quad (93)$$

Wir definieren nun die Energichte $\mathcal{W}$ (als skalare Matrix) durch

$$\mathcal{W} = \frac{1}{8\pi} (\mathfrak{E}^2 + \mathfrak{H}^2). \quad (94)$$

Dann wird nach (11)

$$8\pi \dot{\mathcal{W}} = \mathfrak{E}\dot{\mathfrak{E}} + \dot{\mathfrak{E}}\mathfrak{E} + \mathfrak{H}\dot{\mathfrak{H}} + \dot{\mathfrak{H}}\mathfrak{H},$$

und nach (90):

$$\frac{8\pi}{c} \mathcal{W} = (\mathfrak{E}, \text{rot } \mathfrak{H}) + (\text{rot } \mathfrak{H}, \mathfrak{E}) - (\mathfrak{H}, \text{rot } \mathfrak{E}) - (\text{rot } \mathfrak{E}, \mathfrak{H}),$$

$^{1)}$ Unter Umständen ist eine andere Auffassung des elektromagnetischen Feldes erforderlich, bei der die räumlichen Koordinaten nicht als Zahlen, sondern selbst wieder als Matrizen erscheinen; das hat eine entsprechende Änderung der Bedeutung der räumlichen Differenzialquotienten in den Maxwellschen Gleichungen zur Folge. Wir kommen hierauf in der Fortsetzung der Arbeit zurück.

886

M. Born und P. Jordan,

also nach (93) $\dot{\mathbf{W}} + \text{div } \mathbf{S} = 0,$ (95)

wo $\mathbf{S} = \frac{c}{8\pi} ([\mathbf{E}\mathbf{H}] - [\mathbf{H}\mathbf{E}]).$ (96)

Das ist der Poyntingsche Satz für die Matrizenelektrodynamik; $\mathbf{S}$ bedeutet den Strahlvektor.

In ähnlicher Weise läßt sich der Impulssatz ableiten: Man definiert die Maxwellschen Spannungen durch:

$$\left. \begin{aligned} T_{xx} &= \frac{1}{8\pi} (\mathbf{E}_x^2 - \mathbf{E}_y^2 - \mathbf{E}_z^2) + (\mathbf{H}_x^2 - \mathbf{H}_y^2 - \mathbf{H}_z^2), \\ T_{yz} &= \frac{1}{8\pi} (\mathbf{E}_y\mathbf{E}_z + \mathbf{E}_z\mathbf{E}_y + \mathbf{H}_y\mathbf{H}_z + \mathbf{H}_z\mathbf{H}_y) \end{aligned} \right\} \quad (97)$$

und die Impulsdichte der Strahlung durch

$$\mathbf{g} = \frac{1}{c^2} \mathbf{S} = \frac{1}{8\pi c} ([\mathbf{E}\mathbf{H}] - [\mathbf{H}\mathbf{E}]). \quad (98)$$

Dann erhält man durch ähnliche Rechnung:

$$\dot{\mathbf{g}}_x = \frac{\partial T_{xx}}{\partial x} + \frac{\partial T_{xy}}{\partial y} + \frac{\partial T_{xz}}{\partial z}. \quad (99)$$

Natürlich gewinnen diese Beziehungen an Übersichtlichkeit, wenn man die vierdimensionale Darstellungsweise der Relativitätstheorie benutzt. Eine systematische Behandlung der vierdimensionalen Vektoranalysis und der Relativitätstheorie auf der Basis der Matrizentheorie mit ihrer nicht-kommuntativen Multiplikation soll an anderer Stelle gegeben werden.

§ 8. Kugelwellen. Strahlung eines Dipols. Indem wir unser Ziel, die Strahlung eines Oszillators zu berechnen, verfolgen, müssen wir jetzt Kugelwellen ins Auge fassen.

Hierzu werden wir den Hertzschen Vektor $\mathbf{3}$ als Matrizenvektor einführen; aus $\mathbf{3}$ gewinnt man $\mathbf{E}$ und $\mathbf{H}$ vermöge der Gleichungen:

$$\mathbf{E} = \text{grad div } \mathbf{3} - \frac{1}{c^2} \dot{\mathbf{3}}, \quad \mathbf{H} = \frac{1}{c} \text{ rot } \dot{\mathbf{3}}. \quad (100)$$

In der klassischen Theorie ist für eine Kugelwelle $\mathbf{3}$ proportional mit

$$\frac{1}{r} e^{2\pi i r \left(t - \frac{r}{c}\right)}.$$

Nun läßt sich bekanntlich dieser Ausdruck als Superposition ebener Wellen schreiben$^{1)}$, auf Grund der Identität

$$\frac{e^{i\pi r}}{r} = \frac{i\pi}{2\pi} \int e^{i\pi (r s)} d\omega; \quad (101)$$

$^{1)}$ Siehe etwa P. Debye, Ann. d. Phys. 30, 755, 1909; Formel (7''), S. 758.

Zur Quantenmechanik.

887

dabei ist $r$ der Zahlenvektor vom Zentrum der Kugelwelle zum Aufpunkt, $\mathfrak{s}$ ein Einheitsvektor, $d\omega = d\mathfrak{s}_x d\mathfrak{s}_y d\mathfrak{s}_z$. Mithin läßt sich auch in unserer Theorie aus ebenen Wellen, dargestellt durch Matrizen der Form (89), mittels Integration über die Richtung der Wellennormale die Darstellung einer Kugelwelle gewinnen:

$$\mathfrak{J} = \left( e \mathfrak{q} (n m) \frac{e^{2\pi i r (n m) \left( t - \frac{r}{c} \right)}}{r} \right); \quad (102)$$

dabei stellt die Matrix $e \mathfrak{q} = (e \mathfrak{q} (n m))$ das elektrische Moment dar, das die Welle erregt.

Die Rechnungen, die von hier zur Bestimmung des elektronagnetischen Feldes und der Ausstrahlung führen, sind dieselben wie in der klassischen Theorie, da $r$ als Zahlenvektor mit jeder Matrix vertauscher ist. Man erhält

$$\left. \begin{array}{l} \mathfrak{H} = - \frac{e}{c^2} \frac{1}{r^2} [r \ddot{\mathfrak{q}}], \\ \mathfrak{E} = \frac{e}{c^2} \frac{1}{r^2} [r [r \ddot{\mathfrak{q}}]] \end{array} \right\} \quad (103)$$

und daraus

$$\mathfrak{S} = \frac{e}{4\pi c^2} \frac{r}{r} [r \ddot{\mathfrak{q}}]. \quad (104)$$

Die Integration über alle Raumrichtungen erfolgt in derselben Weise wie in der klassischen Theorie. Das Resultat für die pro Sekunde ausgestrahlte Energie lautet:

$$\int \mathfrak{S} d\mathfrak{f} = \frac{2e^2}{3c^3} \ddot{\mathfrak{q}}^2. \quad (105)$$

Um die mittlere Ausstrahlung zu erhalten, hat man diesen Ausdruck über die Zeit zu mitteln; dadurch entsteht die Diagonalmatrix:

$$\frac{2e^2}{3c^3} \ddot{\mathfrak{q}}^2. \quad (106)$$

Schwingt der Oszillator in einer festen Richtung, so können wir den Matrizenvektor $\mathfrak{q}$ durch den Matrizenskalar $\mathfrak{q} = (q (n m))$ ersetzen; dann wird die Ausstrahlung

$$\frac{2e^2}{3c^3} \ddot{\mathfrak{q}}^2 = \frac{32\pi^4 e^2}{3c^3} \left( \sum_k v (n k)^4 |q (n k)|^2 \right). \quad (107)$$

Wir können hier noch keine vollständige Theorie der Ausstrahlung geben, aus der man zwangsläufig auf die Zuordnung der einzelnen Glieder dieser Reihe zu den stationären Zuständen schließen könnte; denn dazu wäre eine genaue Untersuchung der Rückwirkung der Strahlung auf den Oszillator nötig, also eine Theorie der Dämpfung. Darauf werden wir später zurückkommen. Hier wollen wir nur prüfen, ob die Ausstrahlung wirklich durch die Größen $|q (n k)|^2$ bestimmt wird; der Ausdruck (107)

888

M. Born und P. Jordan, Zur Quantenmechanik.

zeigt, daß das der Fall ist, aber zugleich sehen wir, daß die hingeschriebene Größe nicht die gesamte, von einem stationären Zustand ausgehende spontane Strahlung ist. Denn die spontanen Übergänge erfolgen immer nur nach Zuständen kleinerer Energie, oder bei geeigneter Numerierung nach Zuständen kleinerer Quantenzahl. Wir können nun in ganz formaler Weise angeben, wie sich dieser Umstand in unserer Theorie ausdrücken wird; dazu bilden wir nicht den Mittelwert, sondern die Diagonalsumme der Strahlungsmatrix (105); das gibt

$$D \left( \frac{2 e^2}{3 c^3} \ddot{\boldsymbol{q}}^2 \right) = \frac{32 \pi^4 e^2}{3 c^3} \sum_{n k} v(n k)^4 |q(n k)|^2. \quad (108)$$

Hier können wir rechter Hand umsummieren und schreiben:

$$\frac{64 \pi^4 e^2}{3 c^3} \sum_n \left( \sum_{k < n} v(n k)^4 \cdot |q(n k)|^2 \right). \quad (109)$$

Damit ist die gewünschte Zuordnung erreicht: Zu jedem Zustand $n$ gehört die Strahlung, die den Übergängen zu allen Zuständen $k < n$ entspricht, jede mit der aus der klassischen Theorie bekannten Intensität. Das stimmt mit der Erfahrung überein, wenn man voraussetzt, daß die Indizes $n$ nach wachsenden Energien $W_n$ geordnet sind.

Damit ist Heisenbergs Annahme in dem oben gekennzeichneten, beschränkten Sinne gerechtfertigt.

Es sei gleich hier betont, daß diese Feststellung bezüglich der Sprungwahrscheinlichkeiten unabhängig ist von der Voraussetzung der Nichtentartung des Systems, d. h. der Verschiedenheit aller $W_n$. Zum Schluß heben wir noch hervor, daß mit den Übergangswahrscheinlichkeiten auch die statistischen Gewichte der Zustände festgelegt sind, und zwar muß jedem der durch eine Zeile und Spalte bzw. ein Diagonalglied von $\boldsymbol{W}$ gekennzeichneten Zustände das gleiche statistische Gewicht zugeschrieben werden. Daß dieses Ergebnis (in seiner Verallgemeinerung auf Systeme von mehreren Freiheitsgraden) von selbst auf das Grundprinzip der Bose-Einsteinschen Lichtquantenstatistik führt, soll später erläutert werden.

Anmerkung bei der Korrektur. Die angekündigte Verallgemeinerung der Theorie auf mehrere Freiheitsgrade ist inzwischen gemeinsam mit Herrn W. Heisenberg ausgearbeitet worden und wird in der Fortsetzung dieser Arbeit dargestellt werden. Dort werden auch verschiedene schon hier berührte Punkte ausführlicher erörtert werden, die inzwischen weiter geklärt werden konnten.
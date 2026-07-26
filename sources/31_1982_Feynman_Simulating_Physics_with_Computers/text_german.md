*International Journal of Theoretical Physics, Bd. 21, Nr. 6/7, 1982*

# Physik mit Computern simulieren

**Richard P. Feynman**

*Fachbereich Physik, California Institute of Technology, Pasadena, Kalifornien 91107*

*Erhalten am 7. Mai 1981*

## 1. EINLEITUNG

Im Programm steht, dass dies eine Keynote-Rede ist – und ich weiß nicht, was eine Keynote-Rede ist. Ich beabsichtige in keiner Weise, vorzuschlagen, was in diesem Treffen als Keynote der Themen oder Ähnliches enthalten sein sollte. Ich habe meine eigenen Dinge zu sagen und zu besprechen, und es gibt keine Andeutung, dass jemand über dasselbe oder Ähnliches sprechen muss. Worüber ich also sprechen möchte, ist das, was Mike Dertouzos vorgeschlagen hat, worüber niemand sprechen würde. Ich möchte über das Problem sprechen, Physik mit Computern zu simulieren, und das meine ich auf eine bestimmte Weise, die ich erklären werde. Der Grund dafür ist etwas, das ich von Ed Fredkin gelernt habe, und mein ganzes Interesse an diesem Thema wurde von ihm inspiriert. Es geht darum, etwas über die Möglichkeiten von Computern zu lernen und auch etwas über Möglichkeiten in der Physik. Wenn wir annehmen, dass wir alle physikalischen Gesetze perfekt kennen, müssen wir natürlich nicht auf Computer achten. Es ist ohnehin interessant, sich mit der Vorstellung zu beschäftigen, dass wir etwas über physikalische Gesetze lernen können; und wenn ich es hier entspannt betrachte (schließlich bin ich hier und nicht zu Hause), gebe ich zu, dass wir nicht alles verstehen.

Die erste Frage ist: Welche Art von Computer werden wir verwenden, um Physik zu simulieren? Die Computertheorie wurde so weit entwickelt, dass sie erkennt, dass sie keinen Unterschied macht; Wenn du zu einem *Universalrechner*, es spielt keine Rolle, wie es hergestellt wird, wie es tatsächlich hergestellt wird. Daher ist meine Frage: Kann Physik von einem universellen Computer simuliert werden? Ich hätte gerne die Elemente dieses Computers *lokal miteinander verbunden*, und denke daher an zelluläre Automaten als Beispiel (aber ich möchte es nicht erzwingen). Aber ich möchte, dass etwas mit dem

467

0020-7748/82/0600-0467\$03.00/0 © 1982 Plenum Verlagsgesellschaft

468

Feyman

Lokalität der Interaktion. Ich möchte nicht an einen sehr riesigen Computer mit willkürlichen Verbindungen im gesamten Gerät denken.

Welche Art von Physik werden wir nun nachahmen? Zuerst werde ich die Möglichkeit beschreiben, die Physik in der klassischen Approximation zu simulieren, etwas, das üblicherweise durch lokale Differentialgleichungen beschrieben wird. Aber die physikalische Welt ist quantenmechanisch, und daher ist das eigentliche Problem die Simulation der Quantenphysik – worüber ich eigentlich sprechen möchte, aber darauf komme ich später noch ein. Was für eine Art von Simulation meine ich? Es gibt natürlich eine Art approximative Simulation, bei der man numerische Algorithmen für Differentialgleichungen entwirft und dann den Computer verwendet, um diese Algorithmen zu berechnen und eine ungefähre Vorstellung davon zu bekommen, was die Physik eigentlich tun sollte. Das ist ein interessantes Thema, aber nicht das, worüber ich sprechen möchte. Ich möchte über die Möglichkeit sprechen, dass es eine *Genau* Simulation, die der Computer machen wird *Genau* Dasselbe wie die Natur. Wenn dies bewiesen werden soll und die Art des Computers so ist, wie ich es bereits erklärt habe, dann wird es notwendig sein, dass *Alles* das in einem endlichen Volumen von Raum und Zeit geschieht, müsste mit einer endlichen Anzahl logischer Operationen exakt analytierbar sein. Die derzeitige physikalische Theorie ist offenbar nicht so. Er erlaubt es, dass der Raum in infinitesimale Entfernungen hinabsteigt, Wellenlängen unendlich groß werden, Terme in unendlicher Reihenfolge summiert werden und so weiter; und daher ist das physikalische Recht falsch, wenn diese Aussage richtig ist.

So gut, wir haben bereits einen Vorschlag, wie wir physikalische Gesetze modifizieren könnten, und das ist genau der Grund, warum ich solche Probleme gerne erforsche. Als Beispiel könnten wir die Vorstellung, dass der Raum stetig ist, in die Idee ändern, dass der Raum vielleicht ein einfaches Gitter ist und alles diskret ist (sodass wir ihn in eine endliche Anzahl von Ziffern einordnen können) und dass die Zeit disstetig springt. Schauen wir uns nun an, was für eine physikalische Welt es wäre oder welches Berechnungsproblem wir hätten. Zum Beispiel wäre die erste Schwierigkeit, dass die Lichtgeschwindigkeit leicht von der Richtung abhängt, und es könnten andere Anisotropien in der Physik geben, die wir experimentell nachweisen könnten. Es könnten sehr kleine Anisotropien sein. Physikalisches Wissen ist natürlich immer unvollständig, und man kann immer sagen, wir versuchen, etwas zu entwerfen, das Experiment derzeit übertrifft, aber Anisotropien in irgendeinem Maßstab vorhersagt, die später gefunden werden. Das ist in Ordnung. Das wäre gute Physik, wenn man etwas vorhersagen könnte, das mit allen bekannten Fakten übereinstimmt, und eine neue Tatsache vorschlagen könnte, die wir nicht erklärt haben, aber ich habe keine konkreten Beispiele. Ich habe also nichts dagegen, dass es prinzipiell anistropisch ist, es ist eine Frage, wie anistropisch es ist. Wenn du mir sagst, dass es so und so anistrostisch ist, erzähle ich dir von dem Experiment mit dem Lithiumatom, das zeigt, dass die Anisotropie weniger ist als diese Menge und dass diese Theorie von dir unmöglich ist.

Physik mit Computern simulieren

469

Ein weiterer Punkt, der früh vorgeschlagen wurde, war, dass Naturgesetze reversibel sind, aber Computerregeln nicht. Doch das stellte sich als falsch heraus; Die Computerregeln können reversibel sein, und es war eine sehr, sehr nützliche Sache, das zu bemerken und zu entdecken. (Anmerkung der Redaktion: siehe Beiträge von Bennett, Fredkin und Toffoli, diese Proceedings). Dies ist ein Ort, an dem sich die Beziehung zwischen Physik und Berechnung in die andere Richtung gedreht hat und uns etwas über die Möglichkeiten der Berechnung erzählt hat. Das ist also ein interessantes Thema, weil es uns etwas über Computerregeln erzählt, und *Might* Erzählen Sie uns etwas über Physik.

Die Simulationsregel, die ich mir wünschen würde, ist, dass die Anzahl der Computerelemente, die zur Simulation eines großen physikalischen Systems benötigt werden, nur proportional zum Raumzeitvolumen des physikalischen Systems sein darf. Ich will keine Explosion. Das heißt, wenn du sagst, ich möchte so viel Physik erklären, kann ich es genau machen und brauche einen Computer in einer bestimmten Größe. Wenn die Verdoppelung von Raum und Zeit bedeutet, dass ich ein *exponentiell* größerer Computer betrachte ich das als gegen die Regeln (ich erfinde die Regeln, das darf ich). Beginnen wir mit ein paar interessanten Fragen.

## 2. ZEIT SIMULIEREN

Zuerst möchte ich über das Simulieren von Zeit sprechen. Wir gehen davon aus, dass es diskret ist. Du weißt, dass wir keine unendliche Genauigkeit bei physikalischen Messungen haben, sodass Zeit auf einer Skala von weniger als diskret sein könnte $10^{-27}$ sec. (Du müsstest es zumindest so haben, um Konflikte mit Experimenten zu vermeiden – aber mach es $10^{-41}$ sec. wenn du willst, und dann hast du uns!)

Eine Art, wie wir Zeit simulieren – zum Beispiel bei zellulären Automaten – ist, zu sagen, dass "der Computer von Zustand zu Zustand wechselt." Aber eigentlich benutzt man Intuition, die die Idee von Zeit beinhaltet – man geht von Zustand zu Zustand. Und deshalb wird die Zeit (übrigens, wie der Raum im Fall von zellulären Automaten) überhaupt nicht simuliert, sondern im Computer nachgebildet.

Eine interessante Frage stellt sich: 'Gibt es eine Möglichkeit, es zu simulieren, anstatt es zu imitieren?' Nun, es gibt eine Sichtweise auf die Welt, die als Raum-Zeit-Ansicht bezeichnet wird, indem man sich vorstellt, dass die Punkte von Raum und Zeit sozusagen alle im Voraus angelegt sind. Und dann könnten wir sagen, dass eine 'Computer'-Regel (jetzt würde Computer in Anführungszeichen stehen, weil es nicht die Standardart von Computer ist, die in der Zeit arbeitet) lautet: Wir haben einen Zustand $s_i$ an jedem Punkt $i$ in Raum-Zeit. (Siehe Abbildung 1.) Der Staat $s_i$ am Raumzeitpunkt $i$ ist eine gegebene Funktion $F_i(s_j, s_k, \ldots)$ des Zustands an den Punkten $j, k$ In irgendeiner Gegend von $i$:

$$
s_i = F_i(s_j, s_k, \ldots)
$$

470

Feynman

![img-0.jpeg](img-0.jpeg)

Abb. 1.

Sie werden sofort feststellen, dass, wenn diese spezielle Funktion so ist, dass der Wert der Funktion bei i nur die wenigen Punkte im Rückstand in der Zeit umfasst, also vor dieser Zeit i, ich nur den zellulären Automaten neu beschrieben habe, weil das bedeutet, dass man einen gegebenen Punkt aus Punkten zu früheren Zeiten berechnet und ich den nächsten berechnen kann, und so weiter,  und ich kann das in dieser bestimmten Reihenfolge durchgehen. Aber denken wir einfach an eine allgemeinere Art von Computer, denn wir könnten eine allgemeinere Funktion haben. Denken wir also darüber nach, ob wir einen größeren Fall der Allgemeingültigkeit von Verbindungen von Punkten in der Raumzeit haben könnten. Wenn F von allen Punkten sowohl in der Zukunft als auch in der Vergangenheit abhängt, was dann? So könnte die Physik funktionieren. Ich werde erwähnen, wie unsere Theorien im Moment laufen. In vielen physikalischen Theorien hat sich herausgestellt, dass die mathematischen Gleichungen ziemlich vereinfacht werden, wenn man sich so etwas vorstellt – indem man Positronen als Elektronen vorstellt, die in der Zeit zurückfliegen, und andere Dinge, die Objekte vorwärts und rückwärts verbinden. Die wichtige Frage wäre: Wenn dieser Computer aufgebaut wäre, gibt es dann tatsächlich einen organisierten Algorithmus, mit dem eine Lösung ausgearbeitet, also berechnet werden könnte? Angenommen, du kennst diese Funktion F_I, und es ist auch eine Funktion der Variablen in der Zukunft. Wie würdest du Zahlen so anlegen, dass sie automatisch die obige Gleichung erfüllen? Es ist vielleicht nicht möglich. Im Fall des zellulären Automaten ist das so, denn aus einer bestimmten Reihe bekommt man die nächste Zeile und dann die nächste, und es gibt eine organisierte Methode, das zu machen. Es ist eine interessante Frage, ob es Umstände gibt, in denen man Funktionen erhält, für die man nicht zumindest sofort eine organisierte Struktur finden kann. Vielleicht eine Art Annäherung oder so etwas, aber es ist eine interessante, andere Art von Berechnung.

Frage: "Reduziert sich das nicht auf den gewöhnlichen Randwert, im Gegensatz zur Anfangswert-Berechnung?"

Antwort: "Ja, aber denken Sie daran, das ist der Computer selbst, den ich beschreibe."

Es scheint tatsächlich, dass klassische Physik kausal ist. Man kann, was die Informationen der Vergangenheit betrifft, wenn man sowohl Impuls als auch Position einbezieht, oder

Physik mit Computern simulieren

471

Die Position zu zwei verschiedenen Zeiten in der Vergangenheit (so oder so braucht man an jedem Punkt zwei Informationen) berechnet prinzipiell die Zukunft. Also ist klassische Physik *Lokal*, *Kausal*, und *Reversibel*, und daher offenbar recht anpassungsfähig (abgesehen von der Diskretheit und so weiter, die ich bereits erwähnt habe) für Computersimulationen. Damit haben wir anscheinend prinzipiell keine Schwierigkeiten.

### 3. WAHRSCHEINLICHKEITSSIMULATION

Wenn wir uns der Quantenmechanik zuwenden, wissen wir sofort, dass wir hier offenbar nur die Möglichkeit haben, Wahrscheinlichkeiten vorherzusagen. Darf ich sofort sagen, damit du weißt, wohin ich wirklich gehen will, dass wir immer (geheim, geheim, nah... Die Türen!) Wir hatten schon immer große Schwierigkeiten, die Weltanschauung, die die Quantenmechanik darstellt, zu verstehen. Zumindest tue ich das, denn ich bin ein alter genug Mann, dass ich noch nicht so weit gekommen bin, dass mir das alles offensichtlich ist. Okay, ich werde immer noch nervös dabei. Und deshalb sind einige der jüngeren Schüler ... Du weißt ja, wie es immer ist: Jede neue Idee dauert ein oder zwei Generationen, bis klar wird, dass es kein wirkliches Problem gibt. Mir ist noch nicht klar geworden, dass es kein wirkliches Problem gibt. Ich kann das eigentliche Problem nicht definieren, daher vermute ich, dass es kein wirkliches Problem gibt, aber ich bin mir ziemlich sicher, dass es kein wirkliches Problem gibt. Deshalb erforsche ich gerne Dinge. Kann ich etwas daraus lernen, diese Frage zu Computern zu stellen – ob das vielleicht ein Rätsel darüber ist, wie die Weltanschauung der Quantenmechanik ist? Ich weiß also, dass Quantenmechanik offenbar Wahrscheinlichkeit beinhaltet – und deshalb möchte ich über die Simulation der Wahrscheinlichkeit sprechen.

Eine Möglichkeit, einen Computer zu haben, der eine probabilistische Theorie simuliert, also etwas, das eine Wahrscheinlichkeit enthält, wäre, die Wahrscheinlichkeit zu berechnen und diese Zahl dann so zu interpretieren, dass sie die Natur darstellt. Angenommen, ein Teilchen hat eine Wahrscheinlichkeit $P(x, t)$ zu sein bei $x$ zu einer Zeit $t$. Ein typisches Beispiel für eine solche Wahrscheinlichkeit könnte eine Differentialgleichung erfüllen, zum Beispiel wenn das Teilchen diffundiert:

$$
\frac{\partial P(x, t)}{\partial t} = - \nabla^2 P(x, t)
$$

Jetzt könnten wir diskretisieren $t$ und $x$ und vielleicht sogar die Wahrscheinlichkeit selbst und diese Differentialgleichung lösen, wie wir jede beliebige Feldgleichung lösen, und einen Algorithmus dafür entwickeln, um sie durch Diskretisierung exakt zu machen. Zuerst gäbe es ein Problem mit der diskretisierenden Wahrscheinlichkeit. Wenn du nur vorhast zu nehmen $k$ Ziffern würde bedeuten, dass wenn die Wahrscheinlichkeit geringer ist, dass $2^{-k}$ wenn etwas passiert, sagen Sie, es passiert überhaupt nicht. In der Praxis machen wir das. Wenn die

472

Feyman

Die Wahrscheinlichkeit für etwas ist $10^{-700}$, sagen wir, dass es nicht passieren wird, und wir werden nicht oft erwischt. Also könnten wir uns das erlauben. Aber die eigentliche Schwierigkeit ist diese: Wenn wir viele Teilchen hätten, haben wir $R$ Teilchen zum Beispiel in einem System, dann müssten wir die Wahrscheinlichkeit einer Situation beschreiben, indem wir die Wahrscheinlichkeit angeben, diese Teilchen an Punkten zu finden $x_1, x_2, \dots, x_R$ Zur damaligen Zeit $t$. Das wäre eine Beschreibung der Wahrscheinlichkeit des Systems. Und deshalb bräuchtest du eine $k$-Ziffernzahl für jede Konfiguration des Systems, für jede Anordnung von $R$ Werte von $x$. Und daher gilt: $N$ Punkte im Weltraum bräuchten wir $N^R$ Konfigurationen. Tatsächlich, aus unserer Sicht, dass es an jedem Punkt im Raum Informationen wie elektrische Felder usw. gibt, $R$ wird von derselben Ordnung sein wie $N$ Wenn die Anzahl der Informationsbits gleich ist wie die Anzahl der Punkte im Raum, müsste man daher etwas wie so etwas haben wie $N^N$ Konfigurationen, die beschrieben werden sollen, um die Wahrscheinlichkeit herauszuholen, und das ist zu groß für unseren Computer, wenn die Größe des Computers in der richtigen Ordnung ist $N$.

Wir betonen, wenn eine Beschreibung eines isolierten Naturteils mit $N$ Variablen erfordern eine allgemeine Funktion von $N$ Variablen und wenn ein Computer dies stimuliert, indem er diese Funktion tatsächlich berechnet oder speichert, dann verdoppelt man die Größe der Natur ($N \rightarrow 2N$) ein exponentiell explosives Wachstum der Größe des simulierenden Computers erfordern würde. Es ist daher laut den festgelegten Regeln unmöglich, durch Berechnung der Wahrscheinlichkeit zu simulieren.

Gibt es eine andere Möglichkeit? Welche Art von Simulation können wir haben? Wir können nicht erwarten, die Wahrscheinlichkeit von Konfigurationen für eine probabilistische Theorie zu berechnen. Aber die andere Möglichkeit, eine probabilistische Natur zu simulieren, die ich als Probabilistische bezeichnen werde. $\mathfrak{N}$ Im Moment könnte es noch dazu dienen, die probabilistische Natur durch einen Computer zu simulieren $\mathcal{C}$ Das ist selbst probabilistisch, bei dem man immer die letzten zwei Ziffern jeder Zahl zufällig generiert oder etwas Schlimmes damit macht. Es wird also zu dem, was ich einen probabilistischen Computer nenne, bei dem die Ausgabe keine eindeutige Funktion der Eingabe ist. Und dann versucht man, es so herauszufinden, dass es die Natur in diesem Sinne simuliert: dass $\mathcal{C}$ geht von einem Zustand – Anfangszustand, wenn man so will – zu einem Endzustand mit dem *Gleiches* Wahrscheinlichkeit, dass $\mathfrak{N}$ geht vom entsprechenden Anfangszustand zum entsprechenden Endzustand. Natürlich, wenn man die Maschine aufbaut und die Natur das machen lässt, wird der Nachahmer nicht dasselbe tun, sondern nur mit derselben Wahrscheinlichkeit. Ist das nicht gut? Nein, das ist in Ordnung. Woher weißt du, wie hoch die Wahrscheinlichkeit ist? Sehen Sie, die Natur ist unberechenbar; Wie erwartest du, das mit einem Computer vorherzusagen? Man kann es nicht – es ist unvorhersehbar, wenn es probabilistisch ist. Aber was man in einem probabilistischen System wirklich tut, ist, das Experiment in der Natur eine große Anzahl von Mal zu wiederholen. Wenn du dasselbe Experiment im Computer eine große Anzahl von Mal wiederholst (und das dauert natürlich nicht länger als dasselbe in der Natur), ergibt es die Frequenz eines bestimmten Endzustands proportional zur Anzahl der Male, mit ungefähr derselben Rate (plus

Physik mit Computern simulieren

473

oder minus die Quadratwurzel von $n$ und all das) so wie es in der Natur geschieht. Mit anderen Worten, wir könnten uns einen probabilistischen Simulator probabilistischer Natur vorstellen und vollkommen zufrieden damit sein, bei dem die Maschine nicht genau das tut, was die Natur tut, aber wenn man eine bestimmte Art von Experiment ausreichend oft wiederholt, um die Wahrscheinlichkeit der Natur zu bestimmen, dann führt man das entsprechende Experiment am Computer durch,  Du bekommst die entsprechende Wahrscheinlichkeit mit der entsprechenden Genauigkeit (mit derselben Art von Genauigkeit wie Statistiken).

Denken wir nun über die Eigenschaften eines lokalen probabilistischen Computers nach, denn ich werde sehen, ob ich damit die Natur nachahmen kann (mit 'Natur' meine ich jetzt die Quantenmechanik). Eine der Eigenschaften ist, dass man feststellen kann, wie es sich in einer lokalen Region verhält, indem man einfach ignoriert, was es in allen anderen Regionen tut. Angenommen, es gibt Variablen im System, die die ganze Welt beschreiben $(x_A, x_B)$—die Variablen $x_A$ du interessiert bist, sie sind 'hier in der Nähe'; $x_B$ sind das gesamte Ergebnis der Welt. Wenn du die Wahrscheinlichkeit wissen willst, dass hier etwas passiert, müsstest du diese erhalten, indem du die Gesamtwahrscheinlichkeit aller möglichen Möglichkeiten über integrierst $x_B$. Wenn wir es getan hätten *berechnet* Diese Wahrscheinlichkeit müssten wir trotzdem die Integration durchführen

$$
P_A(x_A) = \int P(x_A, x_B) dx_B
$$

Das ist ein harter Job! Aber wenn wir *imitiert* Die Wahrscheinlichkeit, das ist sehr einfach: Man muss nichts tun, um die Integration durchzuführen, man ignoriert einfach die Werte von $x_B$ Schau dir einfach die Region an. $x_A$. Und deshalb hat es das Merkmal der Natur: Wenn es lokal ist, kann man herausfinden, was in einer Region passiert, nicht durch Integration oder eine zusätzliche Operation, sondern einfach, indem man ignoriert, was anderswo passiert, was keine Operation ist, gar nichts.

Ein weiterer Aspekt, den ich betonen möchte, ist, dass die Gleichungen eine Form haben werden, zweifellos ungefähr wie folgt. Sei jeder Punkt $i = 1, 2, \ldots, N$ im Raum sei in einem Zustand $s_i$ ausgewählt aus einer Small-State-Menge (die Größe dieser Menge sollte vernünftig sein, zum Beispiel bis zu $2^5$). Und sei die Wahrscheinlichkeit, eine Konfiguration zu finden, $\{s_i\}$ (eine Menge von Werten des Zustands $s_i$ an jedem Punkt $i$) eine Zahl sein $P(\{s_i\})$. Sie erfüllt eine Gleichung, so dass bei jedem Zeitsprung

$$
P_{i+1}(\{s\}) = \sum_{\{s'\}} \left[ \prod_i m(s_i | s'_j, s'_k \ldots) \right] P_i(\{s'\})
$$

wobei $m(s_i | s'_j, s'_k \ldots)$ ist die Wahrscheinlichkeit, dass wir in den Zustand wechseln $s_i$ An der Spitze $i$

474

Feyrman

wenn die Nachbarn Werte haben $s_j', s_k', \ldots$, wobei $j, k$ usw. sind Punkte in der Nähe von $i$. Als $j$ Zieht weit weg von $i, m$ wird immer weniger sensibel für $s_j'$. Bei jeder Änderung des Zustands an einem bestimmten Punkt $i$ wird von dem, was es war, zu einem Bundesstaat werden. $s$ mit einer Wahrscheinlichkeit $m$ das hängt nur von den Zuständen der Umgebung ab (die so definiert sein kann, dass der Punkt eingeschlossen wird $i$ selbst). Dies ergibt die Wahrscheinlichkeit eines Übergangs. Es ist dasselbe wie bei einem zellulären Automaten; Nur ist es nicht eindeutig, sondern eine Wahrscheinlichkeit. Sag mir die Umgebung, und ich sage dir nach einem nächsten Moment die Wahrscheinlichkeit, dass dieser Punkt im Zustand ist $s$. Und so wird es funktionieren, okay? So erhält man eine mathematische Gleichung dieser Art.

Jetzt gehe ich explizit zur Frage, wie wir mit einem Computer – einem universellen Automaten oder so etwas – die quantenmechanischen Effekte simulieren können. (Die übliche Formulierung ist, dass die Quantenmechanik eine Art Differentialgleichung für eine Funktion besitzt $\psi$.) Wenn du ein einzelnes Teilchen hast, $\psi$ ist eine Funktion von $x$ und $t$, und diese Differentialgleichung könnte simuliert werden, genau wie meine vorherige probabilistische Gleichung. Das wäre in Ordnung, und man hat gesehen, wie Menschen kleine Computer gebaut haben, die die Schröedinger-Gleichung für ein einzelnes Teilchen simulieren. Aber die vollständige Beschreibung der Quantenmechanik für ein großes System mit $R$ Teilchen ist durch eine Funktion gegeben $\psi(x_1, x_2, \ldots, x_R, t)$ die wir die Amplitude nennen, um die Teilchen zu finden. $x_1, \ldots, x_R$, und daher kann sie aufgrund zu vieler Variablen nicht mit einem normalen Computer mit einer Anzahl von Elementen simuliert werden, die proportional zu sind $R$ oder proportional zu $N$. Wir hatten dieselben Probleme mit der Wahrscheinlichkeit in der klassischen Physik. Und daher ist das Problem: Wie können wir die Quantenmechanik simulieren? Es gibt zwei Möglichkeiten, wie wir das angehen können. Wir können unsere Regel darüber aufgeben, was der Computer war, wir können sagen: Lass den Computer selbst aus quantenmechanischen Elementen bestehen, die quantenmechanischen Gesetzen gehorchen. Oder wir wenden uns ab und sagen: Lass den Computer weiterhin derselbe Typ sein, den wir zuvor bedacht haben – ein logischer, universeller Automat; Können wir diese Situation nachahmen? Und ich werde meinen Vortrag hier trennen, denn er verzweigt sich in zwei Teile.

## 4. QUANTENCOMPUTER – UNIVERSELLE QUANTENSIMULATOREN

Der erste Zweig, den man vielleicht als Randbemerkung bezeichnen könnte, lautet: Kann man es mit einer neuen Art von Computer machen – einem Quantencomputer? (Ich komme gleich auf den anderen Zweig zurück.) Soweit ich das beurteilen kann, stellt sich heraus, dass man dies mit einem Quantensystem, mit Quantencomputerelementen, simulieren kann. Es ist keine Turing-Maschine, sondern eine Maschine einer anderen Art. Wenn wir die Kontinuität des Raums außer Acht lassen und ihn diskret machen, und so weiter, als Näherung (so wie wir uns im klassischen Fall erlaubt haben), scheint es tatsächlich so zu sein

Physik mit Computern simulieren

475

Es sei wahr, dass alle verschiedenen Feldtheorien dasselbe haben *Art* von Verhalten, und kann offenbar in jeder Hinsicht simuliert werden, mit kleinen Gitterwerken aus Spins und anderen Dingen. Es wurde immer wieder festgestellt, dass die Phänomene der Feldtheorie (wenn die Welt in einem diskreten Gitter besteht) von vielen Phänomenen in der Festkörpertheorie gut nachgeahmt werden (was einfach die Analyse eines Gitters von Kristallatomen ist, und im Fall der Art des Festkörpers meine ich, dass jedes Atom einfach ein Punkt ist, dem Zahlen zugeordnet sind,  mit quantenmechanischen Regeln). Zum Beispiel die Spinwellen in einem Spin-Gitter, die Bose-Teilchen in der Feldtheorie imitieren. Ich glaube daher, dass es stimmt, dass man mit einer geeigneten Klasse von Quantenmaschinen jedes Quantensystem imitieren könnte, einschließlich der physischen Welt. Aber ich weiß nicht, ob die allgemeine Theorie dieser Intersimulation von Quantensystemen jemals ausgearbeitet wurde, und deshalb stelle ich das als ein weiteres interessantes Problem vor: die Klassen verschiedener Arten quantenmechanischer Systeme zu ermitteln, die wirklich intersimulierbar sind – die äquivalent sind – wie es im Fall klassischer Computer gemacht wurde. Es wurde festgestellt, dass es eine Art universellen Computer gibt, der alles kann, und es macht kaum einen Unterschied, wie genau er gestaltet ist. Genauso sollten wir versuchen herauszufinden, welche Arten von quantenmechanischen Systemen gegenseitig intersimulierbar sind, und versuchen, eine bestimmte Klasse oder einen Charakter dieser Klasse zu finden, der alles simuliert. Was ist mit anderen Worten der universelle Quantensimulator? (unter der Annahme dieser Diskretisierung von Raum und Zeit). Wenn man diskrete Quantensysteme hätte, welche anderen diskreten Quantensysteme sind exakte Nachahmer davon, und gibt es eine Klasse, mit der alles verglichen werden kann? Ich glaube, es ist ziemlich einfach, diese Frage zu beantworten und den Kurs zu finden, aber ich habe es einfach noch nicht gemacht.

Angenommen, wir versuchen folgende Vermutung: Dass jedes endliche quantenmechanische System beschrieben werden kann *Genau*, genau imitiert, indem angenommen wird, dass wir ein anderes System haben, so dass an jedem Punkt der Raumzeit dieses System nur zwei mögliche Basiszustände hat. Entweder ist dieser Punkt besetzt oder unbesetzt – das sind die beiden Zustände. Die Mathematik der quantenmechanischen Operatoren, die mit diesem Punkt verbunden sind, wäre sehr einfach.

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

476

Feynman

Es gäbe einen Operator $a$ die *vernichtet* wenn der Punkt besetzt ist, ändert er sich zu unbesetzt. Es gibt einen konjugierten Operator $a^*$ Was das Gegenteil bewirkt: Wenn es unbewohnt ist, besetzt es es. Da ist noch ein anderer Operator $n$ genannt die *Anzahl* zu fragen: Ist da etwas? Die kleinen Matrizen sagen dir, was sie tun. Wenn es da ist, nimmt N eine Eins und lässt sie in Ruhe, wenn sie nicht da ist, passiert nichts. Das entspricht mathematisch dem Produkt der anderen beiden. Und dann ist da noch die Identität, $\mathbb{1}$, die wir immer einbauen müssen, um unsere Mathematik zu vervollständigen – es bringt überhaupt nichts!

Übrigens sind auf der rechten Seite der obigen Formeln dieselben Operatoren in Matrizen geschrieben, die die meisten Physiker praktischer finden, weil sie hermitisch sind, was es ihnen zu erleichtern scheint. Sie haben eine weitere Reihe von Matrizen erfunden, die Pauli $\sigma$ Matrizen:

$$
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \mathbb{1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

Und diese werden genannt *Spin*—Dreh eine Hälfte—also sagen manchmal, man spreche von einem Spin-Halb-Gitter.

Die Frage ist: Wenn wir einen Hamiltonoperator schreiben würden, der nur diese Operatoren enthält, lokal mit entsprechenden Operatoren an den anderen Raumzeitpunkten gekoppelt, könnten wir dann jedes quantenmechanische System imitieren, das diskret ist und eine endliche Anzahl von Freiheitsgraden besitzt? Ich weiß fast sicher, dass wir das für jedes quantenmechanische System tun könnten, das Bose-Teilchen beinhaltet. Ich bin mir nicht sicher, ob Fermi-Teilchen durch ein solches System beschrieben werden könnten. Deshalb lasse ich das offen. Nun, das ist ein Beispiel dafür, was ich mit einem allgemeinen quantenmechanischen Simulator meinte. Ich bin mir nicht sicher, ob das ausreicht, weil ich mir nicht sicher bin, ob es Fermi-Partikel beseitigt.

## 5. KÖNNEN QUANTENSYSTEME PROBABILISTISCH VON EINEM KLASSISCHEN COMPUTER SIMULIERT WERDEN?

Nun ist die nächste Frage, die ich aufwerfen möchte, natürlich die interessante, nämlich: Kann ein Quantensystem probabilistisch von einem klassischen (ich nehme an) universellen Computer probabilistisch simuliert werden? Mit anderen Worten: Ein Computer, der die gleichen Wahrscheinlichkeiten wie das Quantensystem liefert. Wenn man den Computer als die klassische Art betrachtet, die ich bisher beschrieben habe (nicht die Quantenart, die im letzten Abschnitt beschrieben wurde) und es keine Änderungen in irgendwelchen Gesetzen gibt, und es gibt keinen Hokuspokus, dann lautet die Antwort ganz sicher: Nein! Dies wird als das Problem der versteckten Variablen bezeichnet: Es ist unmöglich, die Ergebnisse der Quantenmechanik mit einem klassischen universellen Bauelement darzustellen. Um ein wenig darüber zu erfahren, sage ich, versuchen wir, die Quantengleichungen so ähnlich wie möglich zu betrachten

Physik mit Computern simulieren

477

mit klassischen Gleichungen möglich, damit wir sehen können, wie schwierig es ist und was passiert. Nun, erstens können wir das nicht simulieren $\psi$ auf die übliche Weise. Wie ich bereits erklärt habe, gibt es zu viele Variablen. Unsere einzige Hoffnung ist, dass wir Wahrscheinlichkeiten simulieren, dass unser Computer Dinge mit der gleichen Wahrscheinlichkeit tut, wie wir sie in der Natur beobachten, wie sie vom quantenmechanischen System berechnet wird. Kannst du einen zellulären Automaten oder Ähnliches mit derselben Wahrscheinlichkeit nachahmen, was die Natur tut, wobei ich annehme, dass die Quantenmechanik korrekt ist, oder zumindest nachdem ich Raum und Zeit diskretisiert habe, ist es richtig, und schaue, ob ich das kann. Ich muss darauf hinweisen, dass man die Wahrscheinlichkeiten, die Ergebnisse, direkt mit der korrekten Quantenwahrscheinlichkeit erzeugen muss. Direkt, weil wir keine Möglichkeit haben, alle Zahlen zu speichern, müssen wir das Phänomen einfach direkt nachahmen.

Es stellt sich also heraus, dass eine andere Sache, anstelle der Wellenfunktion, eine Sache namens die *Dichtematrix*, ist dafür viel nützlicher. Es ist für die mathematischen Gleichungen nicht so nützlich, da es komplizierter ist als die Gleichungen für $\psi$, aber ich werde mir keine Sorgen um mathematische Komplikationen machen oder darüber, welche Berechnung am einfachsten ist, denn mit Computern müssen wir nicht so sorgfältig darauf achten, es auf die einfachste Weise zu machen. Und so wende ich mich bei einer leichten Erhöhung der Komplexität der Gleichungen (und nicht sehr stark) zur Dichtematrix, die für ein einzelnes Teilchen mit Koordinate $x$ im reinen Zustand der Wellenfunktion $\psi(x)$ ist

$$
\rho(x, x') = \psi^*(x)\psi(x')
$$

Dies besitzt eine besondere Eigenschaft, die eine Funktion von zwei Koordinaten ist. $x, x'$. Das Vorhandensein von zwei Größen $x$ und $x'$ Mit jeder Koordinate assoziiert ist analog zu der Tatsache, dass man in der klassischen Mechanik zwei Variablen haben muss, um den Zustand zu beschreiben, $x$ und $\hat{x}$. Zustände werden durch ein Gerät zweiter Ordnung beschrieben, das zwei Informationen enthält ('Position' und 'Geschwindigkeit'). Wir müssen also zwei Informationsstücke haben, die mit einem Teilchen verbunden sind, analog zur klassischen Situation, um Konfigurationen zu beschreiben. (Ich habe die Dichtematrix für ein Teilchen geschrieben, aber natürlich gibt es das Analoge für $R$ Teilchen, eine Funktion von $2R$ Variablen).

Diese Größe besitzt viele der mathematischen Eigenschaften einer Wahrscheinlichkeit. Zum Beispiel, wenn ein Zustand $\psi(x)$ ist nicht sicher, aber ist $\psi_\alpha$ mit der Wahrscheinlichkeit $p_\alpha$ dann ist die Dichtematrix die passende gewichtete Summe der Matrix für jeden Zustand $\alpha$:

$$
\rho(x, x') = \sum_\alpha p_\alpha \psi_\alpha^*(x)\psi a(x').
$$

Eine Größe, die Eigenschaften besitzt, die den klassischen Wahrscheinlichkeiten noch ähnlicher sind, ist die Wigner-Funktion, eine einfache Umformulierung der Dichtematrix; für ein

478

Feynman

Einzelteilchen

$$W(x, p) = \int \rho \left( x + \frac{y}{2}, x - \frac{y}{2} \right) e^{ipy} dy$$

Wir betonen ihre Ähnlichkeit und nennen sie "Wahrscheinlichkeit" in Anführungszeichen statt Wigner-Funktion. Beobachten Sie diese Angebote genau, wenn sie fehlen, meinen wir die tatsächliche Wahrscheinlichkeit. Wenn "Wahrscheinlichkeit" alle mathematischen Eigenschaften einer Wahrscheinlichkeit hätte, könnten wir die Anführungszeichen entfernen und simulieren. $W(x, p)$ ist die "Wahrscheinlichkeit", dass das Teilchen Position hat $x$ und Impuls $p$ (per $dx$ und $dp$). Welche Eigenschaften hat sie, die einer gewöhnlichen Wahrscheinlichkeit ähneln?

Es hat die Eigenschaft, dass man, wenn es viele Variablen gibt und die "Wahrscheinlichkeiten" einer endlichen Region kennen wollen, die anderen Variablen einfach ignorieren (durch Integration). Außerdem ist die Wahrscheinlichkeit, ein Teilchen zu finden, bei $x$ ist $\int W(x, p)dp$. Wenn du übersetzen kannst $W$ als Wahrscheinlichkeit zu finden $x$ und $p$, das wäre eine erwartete Gleichung. Ebenso gilt die Wahrscheinlichkeit von $p$ es würde erwartet werden, $\int W(x, p)dx$. Diese beiden Gleichungen sind korrekt, und daher würde man hoffen, dass vielleicht $W(x, p)$ ist die Wahrscheinlichkeit zu finden $x$ und $p$. Und die Frage ist dann, ob wir ein Gerät bauen können, das dies simuliert $W$? Denn dann würde es gut funktionieren.

Da die von mir genannten Quantensysteme am besten durch Spin-One-Half repräsentiert wurden (besetzt versus unbesetzt oder Spin One-Half ist dasselbe), versuchte ich, dasselbe für Spin-One-Half-Objekte zu machen, und es ist ziemlich einfach. Obwohl zuvor ein Objekt nur zwei Zustände hatte, besetzt und unbesetzt, erfordert die vollständige Beschreibung – um Dinge als Funktion der Zeit zu entwickeln – doppelt so viele Variablen, was bedeutet, dass an jedem Punkt zwei Slots besetzt oder unbesetzt sind (bezeichnet durch $+$ und $-$ im Folgenden), analog zu den $x$ und $\hat{x}$, oder die $x$ und $p$. Man findet also vier Zahlen, vier "Wahrscheinlichkeiten". $\{f_{++}, f_{+-}, f_{-+}, f_{--}\}$ die sich genau so verhalten, und ich muss erklären, warum sie nicht exakt gleich sind, aber sie verhalten sich genau wie Wahrscheinlichkeiten, Dinge in dem Zustand zu finden, in dem beide Symbole oben sind, eines oben und eines unten und so weiter. Zum Beispiel die Summe $f_{++} + f_{+-} + f_{-+} + f_{--}$ von den vier "Wahrscheinlichkeiten" ist 1. Sie werden sich erinnern, dass ein Objekt jetzt zwei Indizes hat, zwei plus/minus Indizes oder zwei Einsen und Nullen an jedem Punkt, obwohl das Quantensystem nur einen hatte. Wenn Sie zum Beispiel wissen möchten, ob der erste Index positiv ist, wäre die Wahrscheinlichkeit für

$$\text{Prob(first index is } +) = f_{++} + f_{+-} \quad [\text{spin } z \text{ up}]$$

Das heißt, dir ist der zweite Index egal. Die Wahrscheinlichkeit, dass der erste Index negativ ist, ist

$$\text{Prob(first index is } -) = f_{-+} + f_{--}, \quad [\text{spin } z \text{ down}]$$

Physik mit Computern simulieren

479

Diese beiden Formeln sind in der Quantenmechanik genau korrekt. Siehst du, ich halte mich zurück, ob 'Wahrscheinlichkeit' oder nicht $f$ Es kann wirklich eine Wahrscheinlichkeit ohne Angebote sein. Aber wenn ich Wahrscheinlichkeit ohne Anführungszeichen auf die linke Seite schreibe, sichere ich mich nicht ab; Das ist wirklich die quantenmechanische Wahrscheinlichkeit. Hier wird das völlig in Ordnung interpretiert. Ebenso kann die Wahrscheinlichkeit, dass der zweite Index positiv ist, durch die Erträge erhalten werden

$$
\operatorname{Prob}(\text{second index is } +) = f_{++} + f_{-+} \quad [\text{spin } x \text{ up}]
$$

und ebenso

$$
\operatorname{Prob}(\text{second index is } -) = f_{+-} + f_{--} \quad [\text{spin } x \text{ down}]
$$

Du könntest auch weitere Fragen zum System stellen. Vielleicht möchten Sie wissen: Wie wahrscheinlich ist es, dass beide Indizes positiv sind? Du bekommst Ärger. Aber du könntest auch andere Fragen stellen, mit denen du keine Probleme bekommst und die tatsächlich korrekte Antworten geben. Man kann zum Beispiel fragen, wie wahrscheinlich ist es, dass die beiden Indizes gleich sind? Das wäre ja

$$
\operatorname{Prob}(\text{match}) = f_{++} + f_{--} \quad [\text{spin } y \text{ up}]
$$

Oder die Wahrscheinlichkeit, dass es keine Übereinstimmung zwischen den Indizes gibt, dass sie unterschiedlich sind,

$$
\operatorname{Prob}(\text{no match}) = f_{+-} + f_{-+} \quad [\text{spin } y \text{ down}]
$$

Alles völlig in Ordnung. All diese Wahrscheinlichkeiten sind korrekt und ergeben Sinn und haben eine präzise Bedeutung im Spin-Modell, wie sie in den oben genannten eckigen Klammern gezeigt wird. Es gibt weitere 'Wahrscheinlichkeits'-Kombinationen, weitere lineare Kombinationen davon $f$Die auch physikalisch sinnvolle Wahrscheinlichkeiten ergeben, aber darauf werde ich jetzt nicht eingehen. Es gibt andere lineare Kombinationen, zu denen Sie Fragen stellen können, aber Sie scheinen keine Fragen zu einer Person stellen zu können $f$.

## 6. NEGATIVE WAHRSCHEINLICHKEITEN

Für viele wechselwirkende Spins auf einem Gitter können wir nun eine 'Wahrscheinlichkeit' (die Anführungszeichen erinnern uns daran, dass es noch eine Frage gibt, ob es sich um eine Wahrscheinlichkeit handelt) für korrelierte Möglichkeiten angeben:

$$
F(s_1, s_2, \dots, s_N) \quad (s_i \in \{++, +-, -+, --\})
$$

480

Feynman

Als Nächstes, wenn ich nach der quantenmechanischen Gleichung suche, die mir sagt, was die Änderungen von $F$ mit der Zeit sind sie genau von der Form, die ich oben für die klassische Theorie beschrieben habe:

$$
F_{i+1}(\{s\}) = \sum_{(s')} \left[ \prod_i M(s_i | s'_j, s'_k \dots) \right] F_i(\{s'\})
$$

Aber jetzt haben wir $F$ anstelle von $P$. Die $M(s_i | s'_j, s'_k \dots)$ scheint als die 'Wahrscheinlichkeit' pro Zeiteinheit oder pro Zeitsprung interpretiert zu werden, dass der Zustand bei $i$ wird zu $s_i$ wenn die Nachbarn in Konfiguration sind $s'$. Wenn du eine Wahrscheinlichkeit erfinden kannst. $M$ So schreibst du die Gleichungen entsprechend der normalen Logik, das sind die korrekten Gleichungen, die reellen, korrekten, quantenmechanischen Gleichungen dafür. $F$, und deshalb würdest du sagen: Okay, ich kann es mit einem probabilistischen Computer nachahmen!

Es gibt nur eine Sache, die nicht stimmt. Diese Gleichungen können leider nicht auf der Grundlage der sogenannten 'Wahrscheinlichkeit' interpretiert werden, oder dieser probabilistische Computer kann sie nicht simulieren, weil die $F$ ist nicht unbedingt positiv. Manchmal ist es negativ! Die $M$, die sogenannte 'Wahrscheinlichkeit', von einer Bedingung zur anderen zu wechseln, ist selbst nicht positiv; wenn ich den ganzen Weg zurück in die $f$ Für ein einzelnes Objekt ist es wiederum nicht unbedingt positiv.

Ein Beispiel für Möglichkeiten hier sind

$$
f_{++} = 0.6 \quad f_{+-} = -0.1 \quad f_{-+} = 0.3 \quad f_{--} = 0.2
$$

Die Summe $f_{++} + f_{+-}$ 0,5 ist, das ist eine 50%ige Chance, den ersten Index positiv zu finden. Die Wahrscheinlichkeit, den ersten Index negativ zu finden, ist die Summe $f_{-+} + f_{-+}$ Das sind auch 50 %. Die Wahrscheinlichkeit, den zweiten Index positiv zu finden, ist die Summe $f_{++} + f_{-+}$ was neun Zehntel ist, die Wahrscheinlichkeit, es negativ zu finden, ist $f_{+-} + f_{--}$ Das ist ein Zehntel, völlig in Ordnung, es ist entweder Plus oder Minus. Die Wahrscheinlichkeit, dass sie übereinstimmen, beträgt acht Zehntel, die Wahrscheinlichkeit, dass sie nicht übereinstimmen, plus zwei Zehntel; jede physische Wahrscheinlichkeit ist positiv. Aber das Original $f$'s sind nicht positiv, und darin liegt die große Schwierigkeit. Der einzige Unterschied zwischen einer probabilistischen klassischen Welt und den Gleichungen der Quantenwelt besteht darin, dass es irgendwie so aussieht, als müssten die Wahrscheinlichkeiten negativ werden, und dass wir, soweit ich weiß, nicht wissen, wie man simuliert. Okay, das ist das grundlegende Problem. Ich kenne die Antwort darauf nicht, aber ich wollte erklären, dass ich, wenn ich mein Bestes versuche, die Gleichungen so ähnlich wie möglich an das zu machen, was von einem klassischen probabilistischen Computer nachahmbar wäre, in Schwierigkeiten gerate.

Physik mit Computern simulieren

481

## 7. POLARISATION VON PHOTONEN – ZWEIZUSTANDSSYSTEME

Ich möchte Ihnen zeigen, warum solche Minuszeichen nicht vermieden werden können oder zumindest, dass Sie irgendeine Art von Schwierigkeiten haben. Ihr habt wahrscheinlich alle dieses Beispiel des Einstein-Podolsky-Rosen-Paradoxons gehört, aber ich werde dieses kleine Beispiel eines physikalischen Experiments erklären, das durchgeführt werden kann und bereits durchgeführt wurde, das die Antworten liefert, die die Quantentheorie vorhersagt, und die Antworten sind wirklich richtig, es gibt keinen Fehler, wenn man das Experiment macht, kommt es tatsächlich heraus. Und ich werde das Beispiel der Polarisationen von Photonen verwenden, das ein Beispiel für ein Zwei-Zustanden-System ist. Wenn ein Photon kommt, kann man sagen, es ist entweder $x$ polarisiert oder $y$ polarisiert. Das kann man herausfinden, indem man ein Stück Calcit hineingibt, und das Photon durch den Calcit entweder in eine Richtung oder in eine andere Richtung hinausgeht – eigentlich leicht getrennt – und dann setzt man ein paar Spiegel ein, das ist nicht wichtig. Man bekommt zwei Strahlen, zwei Orte nach draußen, wo das Photon hingehen kann. (Siehe Abbildung 2.)

Wenn man ein polarisiertes Photon einsetzt, geht es zu einem Strahl, dem gewöhnlichen Strahl, oder einem anderen, dem außergewöhnlichen. Wenn man dort Detektoren platziert, stellt man fest, dass jedes Photon, das man einsetzt, entweder zu 100 % in einem oder dem anderen herauskommt und nicht halb und halb. Entweder findet man ein Photon in einem oder im anderen. Die Wahrscheinlichkeit, es im gewöhnlichen Strahl zu finden, plus die Wahrscheinlichkeit, es im außergewöhnlichen Strahl zu finden, beträgt immer 1 – diese Regel muss man haben. Das funktioniert. Außerdem wird es an beiden Detektoren nie gefunden. (Wenn man zwei Photonen eingefügt hätte, hätte man das bekommen können, aber man reduziert die Intensität – es ist eine technische Sache, man findet sie nicht in beiden Detektoren.)

Nun das nächste Experiment: Trennung in 4 polarisierte Strahlen (siehe Abbildung 3). Man setzt zwei Kalksteine in eine Reihe, sodass ihre Achsen einen relativen Winkel haben $\phi$Ich habe zufällig den zweiten Calcit in zwei Positionen gezeichnet, aber es macht keinen Unterschied, ob man dasselbe Stück verwendet oder nicht, wie es einem passt. Nimm den gewöhnlichen Strahl von einem und führe ihn durch ein anderes Stück Calcit und schaue auf seinen gewöhnlichen Strahl, den ich den gewöhnlich-gewöhnlichen nenne $(O-O)$ Strahl, oder schau dir seinen außergewöhnlichen Strahl an, ich habe das gewöhnliche-außergewöhnliche $(O-E)$ Ray. Und dann erscheint der außergewöhnliche Strahl des ersten als der $E-O$ Ray, und dann gibt es noch ein $E-E$ Ray, alles klar. Jetzt kannst du fragen, was passiert.

![img-1.jpeg](img-1.jpeg)

Abb. 2.

482

Feynman

![img-2.jpeg](img-2.jpeg)

Abb. 3.

Folgendes findest du. Wenn ein Photon eintritt, stellt man immer fest, dass nur einer der vier Zähler ausgelöst wird.

Wenn das Photon ist $O$ Aus dem ersten Calcit ergibt der zweite Calcit $O-O$ mit Wahrscheinlichkeit $\cos^2\phi$ oder $O-E$ mit der komplementären Wahrscheinlichkeit $1-\cos^1\phi=\sin^2\phi$. Ebenso gilt ein $E$ Photon ergibt ein $E-O$ mit der Wahrscheinlichkeit $\sin^2\phi$ oder ein $E-E$ mit der Wahrscheinlichkeit $\cos^2\phi$.

### 8. ZWEI-PHOTONEN-KORRELATIONSEXPERIMENT

Wenden wir uns nun dem Zwei-Photonen-Korrelationsexperiment zu (siehe Abbildung 4).

Was passieren kann, ist, dass ein Atom zwei Photonen in entgegengesetzte Richtung emittiert (z. B. die $3s \to 2p \to 1s$ Übergang im H-Atom). Sie werden gleichzeitig beobachtet (sagen wir, von dir und mir) durch zwei Kalzite, die auf gestellt sind $\phi_1$ und $\phi_2$ Auf die vertikale Seite. Quantentheorie und Experiment sind sich einig, dass die Wahrscheinlichkeit $P_{OO}$ dass wir beide ein gewöhnliches Photon detektieren, ist

$$P_{OO} = \frac{1}{2} \cos^2(\phi_2 - \phi_1)$$

Die Wahrscheinlichkeit $P_{EE}$ dass wir beide einen außergewöhnlichen Strahl beobachten, ist dasselbe

$$P_{EE} = \frac{1}{2} \cos^2(\phi_2 - \phi_1)$$

Die Wahrscheinlichkeit $P_{OE}$ das finde ich $O$ und du findest $E$ ist

$$P_{OE} = \frac{1}{2} \sin^2(\phi_2 - \phi_1)$$

![img-3.jpeg](img-3.jpeg)

Abb. 4.

Physik mit Computern simulieren

483

und schließlich die Wahrscheinlichkeit $P_{EO}$ das ich messe $E$ und du misst $O$ ist

$$
P_{EO} = \frac{1}{2} \sin^2(\phi_2 - \phi_1)
$$

Beachte, dass du immer aus deiner eigenen Maßstab vorhersagen kannst, was ich bekommen werde, $O$ oder $E$. Für jede Achse $\phi_1$ die ich gewählt habe, setze einfach deine Achse $\phi_2$ zu $\phi_1$, dann

$$
P_{OE} = P_{EO} = 0
$$

und ich muss alles bekommen, was du bekommst.

Mal sehen, wie es für eine *Lokal* Probabilistischer Computer. Photon 1 muss sich in irgendeinem Zustand befinden $\alpha$ mit der Wahrscheinlichkeit $f_\alpha(\phi_1)$, der bestimmt, dass es als gewöhnlicher Strahl durchgeht. [die Wahrscheinlichkeit, dass es durchgehen würde als $E$ ist $1 - f_\alpha(\phi_1)$]. Ebenso befindet sich Photon 2 in einer Bedingung $\beta$ mit Wahrscheinlichkeit $g_\beta(\phi_2)$. Wenn $p_{\alpha\beta}$ ist die konjunktive Wahrscheinlichkeit, das Bedingungspaar zu finden $\alpha, \beta$, die Wahrscheinlichkeit $P_{OO}$ die wir beide beobachten $O$ Strahlen ist

$$
P_{OO}(\phi_1, \phi_2) = \sum_{\alpha\beta} p_{\alpha\beta} f_\alpha(\phi_1) g_\beta(\phi_2) \quad \sum_{\alpha\beta} p_{\alpha\beta} = 1
$$

ebenso

$$
P_{OE}(\phi_1, \phi_2) = \sum_{\alpha\beta} p_{\alpha\beta} (1 - f_\alpha(\phi_1)) g_\beta(\phi_2) \quad \text{etc.}
$$

Die Bedingungen $\alpha$ Bestimmen Sie, wie sich die Photonen entwickeln. Es gibt eine Art Korrelation der Bedingungen. Eine solche Formel kann die oben genannten Quantenergebnisse für keine reproduzieren $p_{\alpha\beta}, f_\alpha(\phi_1), g_\beta(\phi_2)$ wenn es reelle Wahrscheinlichkeiten sind – das ist alles positiv, obwohl es einfach ist, wenn es "Wahrscheinlichkeiten" sind – negativ für einige Bedingungen oder Winkel. Wir analysieren nun, warum das so ist.

Ich weiß nicht, um welche Bedingungen es sich handelt, aber für jede Bedingung ist die Wahrscheinlichkeit $f_\alpha(\phi)$ ob es außergewöhnlich oder gewöhnlich in irgendeiner Richtung ist, muss entweder eins oder null sein. Sonst konnte man es auf der anderen Seite nicht vorhersagen. Du könntest nicht mit Sicherheit vorhersagen, was ich bekomme, es sei denn, jedes Mal, wenn das Photon hierher kommt, ist es absolut bestimmt, in welche Richtung es sich entwickeln wird. Daher gibt es in welchem Zustand sich das Photon befindet, eine verborgene Variable im Inneren, die bestimmt, ob es gewöhnlich oder außergewöhnlich ist. Diese Bestimmung erfolgt deterministisch, nicht probabilistisch; sonst können wir nicht erklären, dass du vorhersagen konntest, was ich bekommen werde *Genau*. Nehmen wir also an, dass so etwas passiert. Angenommen, wir diskutieren Ergebnisse nur für Winkel, die Vielfache von sind $30^\circ$.

484

Feynman

Auf jedem Diagramm (Abbildung 5) sind die Winkel zu sehen $0^{\circ}$, $30^{\circ}$, $60^{\circ}$, $90^{\circ}$, $120^{\circ}$, und $150^{\circ}$. Ein Teilchen kommt zu mir heraus, und es befindet sich in irgendeinem Zustand, also wofür es geben wird $0^{\circ}$, für $30^{\circ}$, usw. werden alle vom Staat vorhergesagt – bestimmt –. Nehmen wir an, dass in einem bestimmten Zustand die Vorhersage für festgelegt wird $0^{\circ}$ ist, dass es außergewöhnlich sein wird (schwarzer Punkt), für $30^{\circ}$ Es ist auch außergewöhnlich, denn $60^{\circ}$ es ist gewöhnlich (weißer Punkt) und so weiter (Abbildung 5a). Übrigens ergänzen sich die Ergebnisse voneinander im rechten Winkel, denn denken Sie daran, es ist immer entweder außergewöhnlich oder gewöhnlich; Also, wenn du dich drehst $90^{\circ}$, was früher ein gewöhnlicher Strahl war, wird zum außergewöhnlichen Strahl. Daher hat es in welchem Zustand er sich befindet, ein vorhersehbares Muster, bei dem man entweder eine Vorhersage von gewöhnlich oder von außergewöhnlich hat – drei und drei –, weil sie im rechten Winkel nicht dieselbe Farbe haben. Ebenso muss das Teilchen, das zu dir kommt, wenn sie getrennt werden, dasselbe Muster haben, denn du kannst bestimmen, was ich bekomme, indem du deins messst. Welche Umstände auch immer auftreten, die Muster müssen die gleichen sein. Also, wenn ich wissen will, werde ich weiß bei $60^{\circ}$? Man misst einfach bei $60^{\circ}$, und du wirst weiß finden, und deshalb wirst du weiß oder gewöhnlich für mich vorhersagen. Jedes Mal, wenn wir das Experiment durchführen, ist das Muster vielleicht nicht dasselbe. Jedes Mal, wenn wir ein Paar Photonen herstellen und dieses Experiment immer wieder wiederholen, muss es nicht dasselbe sein wie Abbildung 5a. Nehmen wir an, dass beim nächsten Experiment mein Photon sein wird $O$ oder $E$ für jeden Winkel wie in Abbildung 5c. Dann sieht dein Muster aus wie Abbildung 5d. Aber was auch immer es ist, dein Muster muss genau mein Muster sein – sonst könntest du nicht genau vorhersagen, was ich bekomme, indem du den entsprechenden Winkel messst. Und so weiter. Jedes Mal, wenn wir das Experiment durchführen, erhalten wir unterschiedliche Muster; Und es ist einfach: Es gibt nur sechs Punkte, und drei davon sind weiß, und man jagt ihnen auf verschiedene Arten hinterher – alles kann passieren. Wenn wir im gleichen Winkel messen, stellen wir immer fest, dass wir bei einer solchen Anordnung das gleiche Ergebnis erzielen würden.

Angenommen, wir messen nun bei $\phi_2 - \phi_1 = 30^{\circ}$, und fragen: Mit welcher Wahrscheinlichkeit erhalten wir dasselbe Ergebnis? Versuchen wir zunächst dieses Beispiel hier (Abbildung 5a, 5b). Mit welcher Wahrscheinlichkeit würden wir das gleiche Ergebnis erhalten, dass sie

![img-4.jpeg](img-4.jpeg)

Abb. 5.

Physik mit Computern simulieren

485

Beide sind weiß oder beide schwarz? Die Sache kommt so heraus: Angenommen, ich sage: Nachdem sie herausgekommen sind, wähle ich zufällig eine Richtung, ich sage dir, du sollst messen $30^\circ$ rechts von dieser Richtung. Und egal, was ich bekomme, du würdest etwas anderes bekommen, wenn die Nachbarn anders wären. (Wir würden dasselbe bekommen, wenn die Nachbarn gleich wären.) Wie groß ist die Chance, dass du das gleiche Ergebnis wie ich bekommst? Die Wahrscheinlichkeit ist die Anzahl der Male, in denen der Nachbar dieselbe Farbe hat. Wenn man eine Minute nachdenkt, stellt man fest, dass es in zwei Dritteln der Fälle, im Fall von Abbildung 5a, dieselbe Farbe hat. Der schlimmste Fall wäre black/white/black/white/black/white, und dort wäre die Wahrscheinlichkeit eines Matches null (Abbildung 5c,d). Wenn man alle acht möglichen unterschiedlichen Fälle betrachtet, stellt man fest, dass die größte mögliche Antwort zwei Drittel ist. Man kann in einer klassischen Methode wie dieser nicht anordnen, dass die Übereinstimmung bei $30^\circ$ wird größer als zwei Drittel sein. Aber die quantenmechanische Formel sagt voraus $\cos^2 30^\circ$ (oder $3/4$)—und Experimente stimmen dem zu—und darin liegt die Schwierigkeit.

Das ist alles. Das ist die Schwierigkeit. Deshalb scheint die Quantenmechanik von einem lokalen klassischen Computer nicht nachahmbar zu sein.

Ich habe mich immer damit beschäftigt, die Schwierigkeit der Quantenmechanik immer kleiner zu machen, um mir immer mehr Sorgen um dieses spezielle Objekt zu machen. Es erscheint fast lächerlich, dass man es auf eine numerische Frage pressen kann, dass eine Sache größer ist als eine andere. Aber da hast du es – es ist größer, als jedes logische Argument hervorbringen kann, wenn man diese Art von Logik hat. Jetzt sagen wir 'diese Art von Logik'; welche anderen Möglichkeiten gibt es? Vielleicht gibt es keine Möglichkeiten, aber vielleicht gibt es sie. Es ist interessant, die Möglichkeiten zu diskutieren. Ich erwähnte etwas über die Möglichkeit der Zeit – dass Dinge nicht nur von der Vergangenheit, sondern auch von der Zukunft beeinflusst werden und dass unsere Wahrscheinlichkeiten daher in gewissem Sinne 'illusorisch' sind. Wir haben nur die Informationen aus der Vergangenheit und versuchen, den nächsten Schritt vorherzusagen, aber in Wirklichkeit hängt das von der nahen Zukunft ab, auf die wir nicht eingehen können, oder so ähnlich. Eine sehr interessante Frage ist der Ursprung der Wahrscheinlichkeiten in der Quantenmechanik. Anders ausgedrückt ist: Wir haben die Illusion, dass wir jedes Experiment durchführen können, das wir wollen. Wir alle stammen jedoch aus demselben Universum, haben uns mit ihm weiterentwickelt und haben eigentlich keine 'wirkliche' Freiheit. Denn wir gehorchen bestimmten Gesetzen und stammen aus einer bestimmten Vergangenheit. Ist es irgendwie so, dass wir mit den Experimenten korreliert sind, die wir durchführen, sodass die scheinbaren Wahrscheinlichkeiten nicht so aussehen, wie sie aussehen sollten, wenn man annimmt, dass sie zufällig sind? Es gibt alle möglichen Fragen wie diese, und was ich versuche, ist, diejenigen, die über Computersimulationsmöglichkeiten nachdenken, dazu zu bringen, dem viel Aufmerksamkeit zu schenken, die wirklichen Antworten der Quantenmechanik so gut wie möglich zu verarbeiten und zu sehen, ob ihr nicht eine andere Sichtweise erfinden könnt, als die Physiker erfinden mussten, um das zu beschreiben. Tatsächlich haben die Physiker keine

486

Feynman

Gute Sichtweise. Jemand murmelte etwas über ein Vielweltenbild, und dieses Vielweltenbild sagt, dass die Wellenfunktion $\psi$ ist das, was real ist, und verdammt die Torpedos, wenn es so viele Variablen gibt, $N^R$. All diese verschiedenen Welten und jede Anordnung von Konfigurationen ist genau da, genau wie unsere Anordnung von Konfigurationen, wir sitzen zufällig in dieser hier. Es ist möglich, aber ich bin nicht sehr zufrieden damit.

Deshalb möchte ich sehen, ob es einen anderen Ausweg gibt, und ich möchte betonen oder die Frage hierher bringen, denn die Entdeckung von Computern und das Denken über Computer haben sich in vielen Bereichen des menschlichen Denkens als äußerst nützlich erwiesen. Zum Beispiel haben wir nie wirklich verstanden, wie schlecht unser Sprachverständnis ist, die Grammatiktheorie und all das, bis wir versucht haben, einen Computer zu bauen, der Sprache verstehen kann. Wir haben versucht, viel über Psychologie zu lernen, indem wir versucht haben, zu verstehen, wie Computer funktionieren. Es gibt interessante philosophische Fragen zu Denken, Beziehung, Beobachtung, Messung und so weiter, über die Computer uns angeregt haben, mit neuen Denkformen neu nachzudenken. Und alles, was ich tat, war, zu hoffen, dass das Computer-Denken uns neue Ideen bringen würde, falls es wirklich welche gibt. Ich weiß nicht, vielleicht ist Physik absolut in Ordnung, so wie sie ist. Das Programm, das Fredkin immer vorantreibt, um eine Computersimulation der Physik zu finden, scheint mir ein ausgezeichnetes Programm zu sein, das man verfolgen kann. Er und ich haben wunderbare, intensive und endlose Diskussionen geführt, und mein Argument ist immer, dass der eigentliche Nutzen davon in der Quantenmechanik liegt, und daher muss die volle Aufmerksamkeit und Akzeptanz der quantenmechanischen Phänomene – die Herausforderung, quantenmechanische Phänomene zu erklären – in das Argument eingebracht werden, und daher müssen diese Phänomene bei der Analyse der Situation sehr gut verstanden werden. Und ich bin mit all den Analysen nicht zufrieden, die nur mit der klassischen Theorie einhergehen, denn die Natur ist nicht klassisch, verdammt, und wenn man eine Simulation der Natur machen will, sollte man sie besser quantenmechanisch machen, und verdammt noch mal, das ist ein wunderbares Problem, denn es sieht nicht so einfach aus. Danke.

## 9. DISKUSSION

*Frage:* Um es zu interpretieren: Sie sprachen zunächst von der Wahrscheinlichkeit von A gegeben B gegenüber der Wahrscheinlichkeit von A und B gemeinsam – das ist die Wahrscheinlichkeit, dass ein Beobachter das Ergebnis sieht und dem anderen eine Wahrscheinlichkeit zuweist; Und dann hast du das Paradoxon des quantenmechanischen Ergebnisses angesprochen, dass $3/4$, und dieses Wesen $2/3$. Sind das wirklich dieselben Wahrscheinlichkeiten? Ist nicht die eine eine gemeinsame Wahrscheinlichkeit und die andere eine bedingte?

*Antwort:* Nein, sie sind gleich. $P_{OO}$ ist die *Gemeinsame Wahrscheinlichkeit* dass sowohl du als auch ich einen gewöhnlichen Strahl beobachten, und $P_{EE}$ ist die *Gemeinsame Wahrscheinlichkeit* für zwei

Physik mit Computern simulieren

487

Außergewöhnliche Strahlen. Die Wahrscheinlichkeit, dass unsere Beobachtungen übereinstimmen, ist

$$
P_{OO} + P_{EE} = \cos^2 30^\circ = 3/4
$$

*Frage:* Hängt das in gewissem Sinne von der Annahme ab, wie viel Information vom Photon oder vom Teilchen zugänglich ist? Und zweitens, um Ihre Frage der Vorhersage zu nehmen, Ihr Kommentar zur Vorhersage, erinnert in gewissem Sinne an die philosophische Frage: Gibt es irgendeine Bedeutung für die Frage, ob es freien Willen oder Prädestination gibt? nämlich die Korrelation zwischen Beobachter und Experiment, und die Frage ist: Ist es möglich, einen Test zu konstruieren, bei dem die Vorhersage dem Beobachter gemeldet werden kann, oder ist die Fähigkeit, Informationen darzustellen, bereits verbraucht? Und ich vermute, dass Sie bereits alle Informationen aufgebraucht haben, sodass diese Vorhersage außerhalb des Bereichs der Theorie liegt.

*Antwort:* All diese Dinge verstehe ich nicht; Tiefgründige Fragen, tiefgründige Fragen. Allerdings haben Physiker eine ziemlich dumme Art, all diese Dinge zu vermeiden. Sie sagen einfach: Schau mal, Freund, du nimmst ein Paar Zähler und legst sie an die Seite deines Calcits und zählst, wie oft du das Zeug bekommst, und es kommt 75 % der Zeit heraus. Dann sagt man: Kann ich das mit einem Gerät imitieren, das die gleichen Ergebnisse liefert und lokal funktioniert, und man versucht, eine Art Methode dafür zu erfinden, und wenn man es im normalen Denken macht, stellt man fest, dass man nicht mit der gleichen Wahrscheinlichkeit dorthin kommt. Daher ist eine neue Art von Denken notwendig, aber Physiker, die etwas einfältig sind, betrachten nur die Natur und wissen nicht, wie sie auf diese neue Weise denken sollen.

*Frage:* Zu Beginn Ihres Vortrags haben Sie darüber gesprochen, verschiedene Dinge diskretisiert zu machen, um eine echte physikalische Berechnung durchzuführen. Und doch scheint es mir, dass es Unterschiede zwischen Dingen wie Raum und Zeit sowie Wahrscheinlichkeiten gibt, die an einem Ort existieren könnten, oder Energie, oder einem Feldwert. Siehst du einen Grund, zwischen Quantisierung oder Diskretisierung von Raum und Zeit und der Diskretisierung spezifischer Parameter oder Werte zu unterscheiden, die existieren könnten?

*Antwort:* Ich möchte ein paar Kommentare abgeben. Du hast Quantisierung oder Diskretisierung gesagt. Das ist sehr gefährlich. Quantentheorie und Quantisierung sind eine sehr spezifische Art von Theorie. Diskretisieren ist das richtige Wort. Quantisierung ist eine andere Art von Mathematik. Wenn wir von Diskretisierung sprechen ... natürlich habe ich darauf hingewiesen, dass wir die Gesetze der Physik ändern müssen. Denn die physikalischen Gesetze, wie sie jetzt geschrieben sind, haben im klassischen Grenzfall überall eine stetige Variable, Raum und Zeit. Wenn du zum Beispiel in deiner Theorie ein elektrisches Feld haben würdest, dann könnte das elektrische Feld nicht (wenn es imizitierbar, berechenbar mit einer endlichen Anzahl von Elementen sein soll) ein

488

Feynman

Eine unendliche Anzahl möglicher Werte, es müsste digitalisiert werden. Man könnte mit einer Theorie durchkommen, indem man Dinge ohne elektrisches Feld neu beschreibt, aber angenommen, man hätte für einen Moment entdeckt, dass man das nicht kann, und möchte es mit einem elektrischen Feld beschreiben, dann müsste man sagen, dass zum Beispiel, wenn Felder kleiner als eine bestimmte Menge sind,  Sie sind überhaupt nicht da oder so. Und das sind sehr interessante Probleme, aber leider sind sie keine guten Probleme für die klassische Physik, denn wenn man das Beispiel eines Sterns hundert Lichtjahre entfernt nimmt und eine Welle erzeugt, die zu uns kommt, und sie wird immer schwächer, und schwächer, und schwächer, und schwächer, und schwächer, das elektrische Feld sinkt, runter, runter, wie tief können wir dann messen? Du stellst einen Zähler raus und findest "klunk", und eine Weile passiert nichts, "klack" und eine Weile nichts. Es ist überhaupt nicht diskretisiert, man kann ein so winziges Feld nie messen, man findet kein winziges Feld, man muss kein so winziges Feld imitieren, denn die Welt, die man zu imitieren versucht, die physische Welt, ist nicht die klassische Welt, und sie verhält sich anders. Das spezielle Beispiel der Diskretisierung des elektrischen Feldes ist ein Problem, das ich als Physiker nicht als grundsätzlich schwierig ansehen würde, weil es nur bedeutet, dass Ihr Feld so klein geworden ist, dass ich besser sowieso Quantenmechanik verwenden sollte, und Sie also die falschen Gleichungen haben und das falsche Problem gelöst haben! So würde ich das beantworten. Denn wenn man sich vorstellt, das elektrische Feld käme aus einigen 'Einsen' oder so etwas, wäre das tiefste, was man erreichen könnte, ein volles, aber genau das sehen wir: Man erhält ein vollständiges Photon. All diese Dinge deuten darauf hin, dass es irgendwie wahr ist, dass die physische Welt auf diskrete Weise darstellbar ist, denn jedes Mal, wenn man in so eine Zwickmühle gerät, entdeckt man, dass das Experiment genau das tut, was nötig ist, um den Problemen zu entkommen, die entstehen würden, wenn das elektrische Feld auf null steigt oder man niemals einen Stern jenseits einer bestimmten Entfernung sehen könnte,  Weil das Feld unter die Anzahl der Ziffern gefallen wäre, die deine Welt tragen kann.
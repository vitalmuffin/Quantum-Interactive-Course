361

### 3. Quantisierung als Eigenwertproblem; von E. Schrödinger.

(Erste Mitteilung.)

§ 1. In dieser Mitteilung möchte ich zunächst an dem einfachsten Fall des (nichtrelativistischen und ungestörten) Wasserstoffatoms zeigen, daß die übliche Quantisierungsvorschrift sich durch eine andere Forderung ersetzen läßt, in der kein Wort von „ganzen Zahlen“ mehr vorkommt. Vielmehr ergibt sich die Ganzzahligkeit auf dieselbe natürliche Art, wie etwa die Ganzzahligkeit der *Knotenzahl* einer schwingenden Saite. Die neue Auffassung ist verallgemeinerungsfähig und rührt, wie ich glaube, sehr tief an das wahre Wesen der Quantenvorschriften.

Die übliche Form der letzteren knüpft an die Hamiltonsche partielle Differentialgleichung an:

$$(1) \quad H\left(q, \frac{\partial S}{\partial q}\right) = E.$$

Es wird von dieser Gleichung eine Lösung gesucht, welche sich darstellt als *Summe* von Funktionen je einer einzigen der unabhängigen Variablen $q$.

Wir führen nun für $S$ eine neue unbekannte $\psi$ ein derart, daß $\psi$ als ein *Produkt* von eingriffigen Funktionen der einzelnen Koordinaten erscheinen würde. D. h. wir setzen

$$(2) \quad S = K \lg \psi.$$

Die Konstante $K$ muß aus dimensionellen Gründen eingeführt werden, sie hat die Dimension einer *Wirkung*. Damit erhält man

$$(1') \quad H\left(q, \frac{K}{\psi} \frac{\partial \psi}{\partial q}\right) = E.$$

Wir suchen nun *nicht* eine Lösung der Gleichung ($1'$), sondern wir stellen folgende Forderung. Gleichung ($1'$) läßt sich bei Vernachlässigung der Massenveränderlichkeit stets, bei Berücksichtigung derselben wenigstens dann, wenn es sich um das *Einelektronenproblem* handelt, auf die Gestalt bringen: quadratische

362

E. Schrödinger.

Form von $\psi$ und seinen ersten Ableitungen $= 0$. Wir suchen solche reelle im ganzen Konfigurationenraum eindeutige endliche und zweimal stetig differenzierbare Funktionen $\psi$, welche das über den ganzen Konfigurationenraum erstreckte Integral der eben genannten quadratischen Form$^{1)}$ zu einem *Extremum* machen. *Durch dieses Variationsproblem ersetzen wir die Quantenbedingungen.*

Wir werden für $H$ zunächst die Hamiltonsche Funktion der Keplerbewegung nehmen und zeigen, daß die aufgestellte Forderung für *alle positiven*, aber nur für eine *diskrete Schar von negativen E-Werten* erfüllbar ist. D. h. das genannte Variationsproblem hat ein diskretes und ein kontinuierliches Eigenwertspektrum. Das diskrete Spektrum entspricht den Balmerschen Termen, das kontinuierliche den Energien der Hyperbelbahnen. Damit numerische Übereinstimmung bestehe, muß $K$ den Wert $h/2\pi$ erhalten.

Da für die Aufstellung der Variationsgleichungen die Koordinatenwahl belanglos ist, wählen wir rechtwinkelige kartesische. Dann lautet (1') in unserem Fall ($e$, $m$ sind Ladung und Masse des Elektrons):

$$(1'') \quad \left( \frac{\partial \psi}{\partial x} \right)^2 + \left( \frac{\partial \psi}{\partial y} \right)^2 + \left( \frac{\partial \psi}{\partial z} \right)^2 - \frac{2m}{K^2} \left( E + \frac{e^2}{r} \right) \psi^2 = 0 \quad . \\ r = \sqrt{x^2 + y^2 + z^2} \ .$$

Und unser Variationsproblem lautet

$$(3) \quad \begin{cases} \delta J = \delta \iiint dx \, dy \, dz \left[ \left( \frac{\partial \psi}{\partial x} \right)^2 + \left( \frac{\partial \psi}{\partial y} \right)^2 + \left( \frac{\partial \psi}{\partial z} \right)^2 - \right. \\ \left. - \frac{2m}{K^2} \left( E + \frac{e^2}{r} \right) \psi^2 \right] = 0 \ , \end{cases}$$

das Integral erstreckt über den ganzen Raum. Man findet daraus in gewohnter Weise

$$(4) \quad \begin{cases} \frac{1}{2} \delta J = \int df \, \delta \psi \, \frac{\partial \psi}{\partial n} - \iiint dx \, dy \, dz \, \delta \psi \left[ \Delta \psi + \right. \\ \left. + \frac{2m}{K^2} \left( E + \frac{e^2}{r} \right) \psi \right] = 0 \ . \end{cases}$$

Es muß also erstens

$$(5) \quad \Delta \psi + \frac{2m}{K^2} \left( E + \frac{e^2}{r} \right) \psi = 0$$

1) Es entgeht mir nicht, daß diese Formulierung nicht ganz eindeutig ist.

Quantisierung als Eigenwertproblem.

363

und zweitens muß das über die unendlich ferne geschlossene Oberfläche zu erstreckende Integral.

$$(6) \quad \int df \, \delta\psi \, \frac{\partial\psi}{\partial n} = 0 \ .$$

(Es wird sich herausstellen, daß wir wegen dieser letzteren Forderung unser Variationsproblem noch durch eine Forderung über das Verhalten von $\delta\psi$ im Unendlichen zu ergänzen haben, damit auch das oben behauptete *kontinuierliche* Eigenwertspektrum wirklich existiere. Doch davon später.)

Die Lösung von (5) läßt sich (*zum Beispiel*) in räumlichen Polarkoordinaten $r$, $\vartheta$, $\varphi$ bewerkstelligen, indem man $\psi$ als *Produkt* je einer Funktion von $r$, von $\vartheta$, von $\varphi$ ansetzt. Die Methode ist sattsam bekannt. Für die Abhängigkeit von den Polarwinkeln ergibt sich eine *Kugelflächenfunktion* für die Abhängigkeit von $r$ — die Funktion wollen wir $\chi$ nennen — erhält man leicht die Differentialgleichung:

$$(7) \quad \frac{d^2\chi}{dr^2} + \frac{2}{r} \frac{d\chi}{dr} + \left( \frac{2mE}{K^2} + \frac{2me^2}{K^2r} - \frac{n(n+1)}{r^2} \right) \chi = 0 \ . \\ n = 0, 1, 2, 3 \dots$$

Die Beschränkung von $n$ auf ganze Zahlen ist bekanntlich *notwendig*, damit die Abhängigkeit von den Polarwinkeln *eindeutig* werde. — Wir benötigen Lösungen von (7), die für alle nicht-negativen reellen $r$-Werte endlich bleiben. Nun hat$^{1)}$ die Gleichung (7) in der komplexen $r$-Ebene *zwei* Singularitäten, bei $r = 0$ und $r = \infty$, von denen die zweite eine „Stelle der Unbestimmtheit“ (wesentlich singuläre Stelle) *aller* Integrale ist, die erste hingegen nicht (für kein Integral). Diese beiden Singularitäten bilden gerade die *Randpunkte unseres reellen Intervalls*. In einem solchen Falle weiß man nun, daß die Forderung des *Endlichbleibens* in den Randpunkten für die Funktion $\chi$ einer *Randbedingung* gleichkommt. Die Gleichung hat *im allgemeinen* überhaupt kein Integral, das in *beiden* Randpunkten endlich bleibt, sondern ein solches Integral existiert

1) Für die Anleitung zur Behandlung der Gleichung (7) bin ich Hermann Weyl zu größtem Dank verpflichtet. Ich verweise für die im folgenden nicht bewiesenen Behauptungen auf L. Schlesinger, Differentialgleichungen (Sammlung Schubert Nr. 13, Göschen 1900, besonders Kap. 3 und 5.)

364

E. Schrödinger.

nur für gewisse ausgezeichnete Werte der in der Gleichung auftretenden Konstanten. Diese ausgezeichneten Werte gilt es zu bestimmen.

Der eben hervorgehobene Sachverhalt ist der *springende Punkt* in der ganzen Untersuchung.

Wir betrachten zunächst die singuläre Stelle $r = 0$. Die sogenannte *determinierende Fundamentalgleichung*, welche das Verhalten der Integrale an dieser Stelle bestimmt, ist

$$(8) \quad \varrho(\varrho - 1) + 2\varrho - n(n + 1) = 0$$

mit den Wurzeln

$$(8') \quad \varrho_1 = n, \quad \varrho_2 = -(n + 1) .$$

Die beiden kanonischen Integrale an dieser Stelle gehören also zu den Exponenten $n$ und $-(n + 1)$. Von ihnen ist, da $n$ nicht negativ ist, nur das erste für uns brauchbar. Es wird, da es zu dem *größeren* Exponenten gehört, durch eine gewöhnliche Potenzreihe dargestellt, die mit $r^n$ beginnt. (Das andere Integral, das uns nicht interessiert, kann, wegen der ganzzahligen Differenz zwischen den Exponenten, einen Logarithmus enthalten.) Da der nächste singuläre Punkt erst im Unendlichen liegt, konvergiert die genannte Potenzreihe beständig und stellt eine *Ganze Transzendente* dar. Wir stellen also fest:

*Die gesuchte Lösung ist eine (bis auf einen belanglosen konstanten Faktor) eindeutig bestimmte Ganze Transzendente, die bei $r = 0$ zum Exponenten $n$ gehört.*

Es handelt sich jetzt darum, das Verhalten dieser Funktion im *Unendlichen* der positiven reellen Achse zu untersuchen. Dazu vereinfachen wir die Gleichung (7) durch die Substitution

$$(9) \quad \chi = r^\alpha U ,$$

worin $\alpha$ so gewählt wird, daß das Glied mit $1/r^2$ fortfällt. Dazu muß $\alpha$ einen der beiden Werte $n$, $-(n + 1)$ erhalten, wie man leicht nachrechnet. Gleichung (7) nimmt dann die Form an:

$$(7') \quad \frac{d^2 U}{dr^2} + \frac{2(\alpha + 1)}{r} \frac{dU}{dr} + \frac{2m}{K^2} \left( E + \frac{e^2}{r} \right) U = 0 .$$

*Ihre* Integrale gehören bei $r = 0$ zu den Exponenten 0 und $-2\alpha - 1$. Für den ersten $\alpha$-Wert, $\alpha = n$, ist das *erste*, für

Quantisierung als Eigenwertproblem.

365

den zweiten $\alpha$-Wert, $\alpha = -(n + 1)$, ist das zweite dieser Integrale eine Ganze Transzendente und führt nach (9) auf die gesuchte Lösung, die ja eindeutig ist. Wir verlieren also nichts, wenn wir uns auf einen der beiden $\alpha$-Werte beschränken. Wir wählen

$$(10) \quad \alpha = n \ .$$

Unsere Lösung $U$ gehört dann also bei $r = 0$ zum Exponenten 0. Gleichung (7') bezeichnen die Mathematiker als Laplacesche Gleichung. Der allgemeine Typus ist

$$(7'') \quad U'' + \left( \delta_0 + \frac{\delta_1}{r} \right) U' + \left( \varepsilon_0 + \frac{\varepsilon_1}{r} \right) U = 0 \ .$$

Bei uns haben die Konstanten die Werte

$$(11) \quad \delta_0 = 0, \ \delta_1 = 2(\alpha + 1), \ \varepsilon_0 = \frac{2mE}{K^2}, \ \varepsilon_1 = \frac{2me^2}{K^2} \ .$$

Dieser Gleichungstypus ist aus dem Grunde verhältnismäßig einfach zu behandeln, weil die sogenannte Laplacesche Transformation, die im allgemeinen wieder eine Gleichung zweiter Ordnung ergibt, hier auf die erste Ordnung führt, die durch Quadraturen lösbar ist. Dies gestattet eine Darstellung der Lösungen von (7'') selbst durch Integrale im Komplexen. Ich führe hier nur das Endergebnis an.¹⁾ Das Integral

$$(12) \quad U = \int_L e^{z_r} (z - c_1)^{\alpha_1 - 1} (z - c_2)^{\alpha_2 - 1} \, dz$$

ist eine Lösung von (7'') für einen Integrationsweg $L$, für den

$$(13) \quad \int_L \frac{d}{dz} \left[ e^{z_r} (z - c_1)^{\alpha_1} (z - c_2)^{\alpha_2} \right] dz = 0 \ .$$

Die Konstanten $c_1, c_2, \alpha_1, \alpha_2$ haben folgende Werte. $c_1$ und $c_2$ sind die Wurzeln der quadratischen Gleichung

$$(14) \quad z^2 + \delta_0 z + \varepsilon_0 = 0$$

und

$$(14') \quad \alpha_1 = \frac{\varepsilon_1 + \delta_1 c_1}{c_1 - c_2}, \quad \alpha_2 = \frac{\varepsilon_1 + \delta_1 c_2}{c_2 - c_1} \ .$$

¹⁾ Vgl. L. Schlesinger, a. a. O. Die Theorie verdankt man H. Poincaré und J. Horn.

366

E. Schrödinger.

Im Falle der Gleichung (7') wird also nach (11) und (10)

$$(14') \begin{cases} c_1 = + \sqrt{\frac{-2mE}{K^2}}, & c_2 = - \sqrt{\frac{-2mE}{K^2}}; \\ \alpha_1 = \frac{me^2}{K \sqrt{-2mE}} + n + 1, & \alpha_2 = - \frac{me^2}{K \sqrt{-2mE}} + n + 1. \end{cases}$$

Die Integraldarstellung (12) gestattet nicht nur, das asymptotische Verhalten der Gesamtheit von Lösungen, wenn $r$ in bestimmter Weise ins Unendliche geht, zu überblicken, sondern auch, dieses Verhalten für eine *bestimmte* Lösung anzugeben, was immer viel schwieriger ist.

Wir wollen nun zunächst den Fall, daß $\alpha_1$ und $\alpha_2$ reelle ganze Zahlen sind, *ausschließen*. Der Fall tritt, wenn er eintritt, stets für beide Größen gleichzeitig ein und zwar dann und nur dann, wenn

$$(15) \quad \frac{me^2}{K \sqrt{-2mE}} = \text{reelle ganze Zahl} .$$

Wir nehmen also jetzt an, daß (15) nicht erfüllt ist.

Das Verhalten der Gesamtheit von Lösungen für eine bestimmte Art des Unendlichwerdens von $r$ — wir wollen stets denken für realpositives Unendlichwerden — wird alsdann$^{1)}$ charakterisiert durch das Verhalten der beiden linear unabhängigen Lösungen, die durch folgende *zwei Spezialisierungen* des Integrationsweges $L$ erhalten werden, und die wir $U_1$ und $U_2$ nennen wollen. *Beide* Male komme $z$ aus dem Unendlichen und gehe auf demselben Wege dorthin zurück, und zwar in solcher Richtung, daß

$$(16) \quad \lim_{z \to \infty} e^{zr} = 0 ,$$

d.h. der Realteil von $zr$ soll negativ unendlich werden. Hierdurch wird der Bedingung (13) genügt. *Dazwischen* werde im *einen* Falle (Lösung $U_1$) die Stelle $c_1$, im *anderen* Falle (Lösung $U_2$) die Stelle $c_2$ je einmal umlaufen.

Diese beiden Lösungen werden nun für sehr große realpositive $r$-Werte *asymptotisch* (im Sinne Poincarés) dargestellt durch

1) Wenn (15) erfüllt ist, wird mindestens der eine von den beiden im Text beschriebenen Integrationswegen unbrauchbar, da er ein verschwindendes Ergebnis liefert.

Quantisierung als Eigenwertproblem.

967

$$(17) \begin{cases} U_1 \sim e^{c_1 r} r^{-\alpha_1} (-1)^{\alpha_1} (e^{2\pi i \alpha_1} - 1) \Gamma(\alpha_1)(c_1 - c_2)^{\alpha_2 - 1}, \\ U_2 \sim e^{c_2 r} r^{-\alpha_2} (-1)^{\alpha_2} (e^{2\pi i \alpha_2} - 1) \Gamma(\alpha_2)(c_2 - c_1)^{\alpha_1 - 1}, \end{cases}$$

wobei wir uns hier mit dem ersten Glied der nach ganzen negativen Potenzen von $r$ fortschreitenden asymptotischen Reihen begnügen.

Wir haben nun die beiden Fälle $E \geq 0$ zu unterscheiden. Sei zunächst

1. $E > 0$. Wir bemerken erstens, daß hierdurch das Nichtzutreffen von (15) eo ipso gewährleistet ist, weil diese Größe reinimaginär wird. Ferner werden nach (14") auch $c_1$ und $c_2$ reinimaginär. Die Exponentialfunktionen in (17) sind also, da $r$ reell ist, endlichbleibende periodische Funktionen. Die Werte von $\alpha_1$ und $\alpha_2$ nach (14") zeigen, daß $U_1$ und $U_2$ beide wie $r^{-n-1}$ gegen Null gehen. Dasselbe muß also von unserer ganzen transzendenten Lösung $U$ gelten, deren Verhalten wir suchen, wie immer sie sich aus $U_1$ und $U_2$ linear zusammensetzen möge. Ferner lehrt (9) mit Beachtung von (10), daß die Funktion $\chi$, d. i. die ganze transzendente Lösung der ursprünglich vorliegenden Gleichung (7), immer noch wie $1/r$ gegen Null geht, da sie aus $U$ durch Multiplikation mit $r^n$ entsteht. Wir können also aussprechen:

Die Eulersche-Differenzialgleichung (5) unseres Variationsproblems hat für jedes positive $E$ Lösungen, die im ganzen Raum eindeutig endlich und stetig sind und im Unendlichen unter beständigen Oszillationen wie $1/r$ gegen Null gehen. — Von der Oberflächenbedingung (6) wird noch zu sprechen sein.

2. $E < 0$. In diesem Fall ist die Möglichkeit (15) nicht eo ipso ausgeschlossen, doch halten wir vorläufig an ihrem verabredeten Ausschluß fest. Dann wächst nach (14") und (17) $U_1$ für $r = \infty$ über alle Grenzen, $U_2$ dagegen verschwindet exponentiell. Unsere Ganze Transzendente $U$ (und dasselbe gilt von $\chi$) wird also dann und nur dann endlich bleiben, wenn $U$ mit $U_2$ bis auf einen numerischen Faktor identisch ist. Das ist aber nicht der Fall. Man erkennt das so: wählt man in (12) für den Integrationsweg $L$ einen geschlossenen Umlauf um beide Punkte $c_1$ und $c_2$, welcher Umlauf wegen der Ganzzahligkeit der Summe $\alpha_1 + \alpha_2$ dann wirklich auf der Riemannschen Fläche des Integranden geschlossen ist, mithin eo ipso der

368

E. Schrödinger.

Bedingung (13) genügt, so läßt sich leicht zeigen, daß das Integral (12) alsdann *unsere Ganze Transzendente U* darstellt. Es läßt sich nämlich in eine Reihe nach positiven Potenzen von $r$ entwickeln, die jedenfalls für hinreichend kleine $r$ konvergiert, daher der Differentialgleichung (7') genügt, daher mit derjenigen für $U$ zusammenfallen muß. Also: $U$ wird durch (12) dargestellt, wenn $L$ ein geschlossener Umlauf um beide Punkte, $c_1$ und $c_2$, ist. Dieser geschlossene Umlauf läßt sich aber so verzerren, daß er aus den beiden früher betrachteten Integrationswegen, die zu $U_1$ und $U_2$ gehören, *additiv kombiniert* erscheint und zwar *mit nicht verschwindenden Faktoren*, etwa 1 und $e^{2\pi i a_1}$. Daher kann $U$ nicht mit $U_2$ übereinstimmen, sondern muß auch $U_1$ enthalten. W. z. b. w.

Unsere Ganze Transzendente $U$, die unter den Lösungen von (7') allein für die Problemlösung in Betracht kommt, bleibt also unter den gemachten Voraussetzungen für große $r$ *nicht* endlich. — Vorbehaltlich der *Vollständigkeitsuntersuchung*, d. h. des Nachweises, daß unser Verfahren *alle* linear unabhängigen Problemlösungen finden läßt, dürfen wir also aussprechen:

*Für negative $E$, welche der Bedingung (15) nicht genügen, hat unser Variationsproblem keine Lösung.*

Wir haben jetzt nur noch diejenige diskrete Schar von negativen $E$-Werten zu untersuchen, welche *der Bedingung (15) genügen*. $\alpha_1$ und $\alpha_2$ sind dann also beide ganzzahlig. Von den zwei Integrationswegen, welche uns früher das Fundamentalsystem $U_1$, $U_2$ geliefert haben, muß sicherlich der erste abgeändert werden, um Nichtverschwindendes zu liefern. Denn $\alpha_1 - 1$ ist sicherlich positiv, die Stelle $c_1$ ist also jetzt weder ein Verzweigungspunkt noch ein Pol des Integranden, sondern eine gewöhnliche Nullstelle. Es kann auch die Stelle $c_2$ regulär werden, wenn nämlich auch $\alpha_2 - 1$ nicht negativ ist. In *jedem* Falle aber lassen sich zwei passende Integrationswege leicht angeben und die Integration auf ihnen sogar in geschlossener Form durch bekannte Funktionen ausführen, so daß das Verhalten der Lösungen vollkommen überblickt wird.

Sei nämlich

$$(15') \quad \frac{m e^2}{K \sqrt{-2 m E}} = l; \quad l = 1, 2, 3, 4 \dots$$

Quantisierung als Eigenwertproblem.

369

Dann ist nach (14'')

$$(14'') \quad \alpha_1 - 1 = l + n, \quad \alpha_2 - 1 = -l + n.$$

Man hat nun die beiden Fälle zu unterscheiden $l \leqslant n$ und $l > n$. Sei zunächst

a) $l \leqslant n$. Dann verlieren $c_2$ und $c_1$ jedweden singulären Charakter, gewinnen aber dafür die Eignung, als Anfangs- oder Endpunkte des Integrationsweges zu fungieren, behufs Erfüllung der Bedingung (13). Ein dritter hiefür geeigneter Punkt ist das Negativreellunendliche. Jeder Weg zwischen zweien dieser drei Punkte liefert eine Lösung und von diesen drei Lösungen sind je zwei linear unabhängig, wie man leicht bestätigt, indem man die Integrale in geschlossener Form ausrechnet. Im besonderen wird die *ganze transzendente Lösung* durch den Integrationsweg von $c_1$ nach $c_2$ geliefert. Denn daß dieses Integral für $r = 0$ regulär bleibt, erkennt man sofort, ohne es auszurechnen. Ich betone das, weil die wirkliche Ausrechnung eher geeignet ist, diesen Sachverhalt zu verschleiern. Dagegen zeigt *sie*, daß das Integral für positiv unendlich große $r$ über alle Grenzen wächst. *Endlich* bleibt für große $r$ eines von den beiden *anderen* Integralen, das aber dafür für $r = 0$ unendlich wird.

Wir erhalten also im Falle $l \leqslant n$ *keine* Problemlösung.

b) $l > n$. Dann ist nach (14'') $c_1$ eine Nullstelle, $c_2$ ein Pol mindestens erster Ordnung des Integranden. Zwei unabhängige Integrale werden dann geliefert: das eine durch den Weg, der von $z = -\infty$, vorsichtshalber mit Vermeidung des Pols, zur Nullstelle führt; das andere durch das *Residuum* im Pol. *Letzteres* ist die Ganze Transzendente. Wir wollen seinen ausgerechneten Wert angeben, aber gleich mit $r^n$ multipliziert, wodurch wir nach (9) und (10) die Lösung $\chi$ der ursprünglich vorliegenden Gleichung (7) erhalten. (Die belanglose multiplikative Konstante ist willkürlich adjustiert.) Man findet:

$$(18) \chi = f \left( r \frac{\sqrt{-2mE}}{K} \right); \quad f(x) = x^n e^{-x} \sum_{k=0}^{l-n-1} \frac{(-2x)^k}{k!} \binom{l+n}{l-n-1-k}.$$

Man erkennt, daß dies wirklich eine brauchbare Lösung ist, da sie für alle reellen nichtnegativen $r$ endlich bleibt. Durch

Annalen der Physik. IV. Folge. 79.

24

370

E. Schrödinger.

ihr exponentielles Verschwinden im Unendlichen wird überdies die Oberflächenbedingung (6) verbürgt. Wir fassen die Resultate für negative $E$ zusammen:

*Bei negativem $E$ hat unser Variationsproblem dann und nur dann Lösungen, wenn $E$ der Bedingung (15) genügt. Der ganzen Zahl $n$, welche die Ordnung der in der Lösung auftretenden Kugelflächenfunktion angibt, dürfen dann immer nur Werte kleiner als $l$ erteilt werden (wovon stets mindestens einer zur Verfügung steht). Der von $r$ abhängige Teil der Lösung wird durch (18) gegeben.*

Durch Abzählung der Konstanten in den Kugelflächenfunktionen (bekanntlich $2n + 1$) findet man ferner:

*Die gefundene Lösung enthält für eine zulässige Kombination $(n, l)$ genau $2n + 1$ willkürliche Konstanten; für einen vorgegebenen $l$-Wert also $l^2$ willkürliche Konstanten.*

Wir haben damit die eingangs aufgestellten Behauptungen über das Eigenwertspektrum unseres Variationsproblems in den Hauptzügen bestätigt, immerhin bestehen noch Lücken.

Erstens der Nachweis der Vollständigkeit des gesamten nachgewiesenen Systems von Eigenfunktionen. Damit will ich mich in dieser Note nicht befassen. Nach anderweitigen Erfahrungen darf man vermuten, daß uns keine Eigenwerte entgangen sind.

Zweitens ist jetzt daran zu erinnern, daß die für positives $E$ nachgewiesenen Eigenfunktionen nicht ohne weiteres das Variationsproblem in der Form, in der es anfangs gestellt wurde, lösen, weil sie im Unendlichen nur wie $1/r$, $\frac{\partial \psi}{\partial r}$ auf einer großen Kugel also nur wie $1/r^2$ gegen Null geht. Das Oberflächenintegral (6) bleibt daher gerade noch von der Ordnung des $\delta \psi$ im Unendlichen. Wünscht man also das kontinuierliche Spektrum wirklich mit zu erhalten, so muß man dem Problem noch eine Bedingung hinzufügen: etwa daß $\delta \psi$ im Unendlichen verschwinden, oder wenigstens, daß es einem konstanten Wert zustreben soll, unabhängig von der Richtung, in der man ins räumlich Unendliche geht; in letzterem Fall bringen die Kugelflächenfunktionen das Oberflächenintegral zum Verschwinden.

Quantisierung als Eigenwertproblem.

371

§ 2. Die Bedingung (15) ergibt

$$(19) \quad - E_i = \frac{me^4}{2K^2l^2} .$$

Es ergeben sich also die wohlbekannten Bohrschen Energie-niveaus, die den Balmertermen entsprechen, wenn man der Konstante $K$, die wir in (2) aus dimensionellen Gründen einführen mußten, den Wert erteilt

$$(20) \quad K = \frac{h}{2\pi} .$$

Dann wird ja

$$(19') \quad - E_i = \frac{2\pi^2me^4}{h^2l^2} .$$

Unser $l$ ist die Hauptquantenzahl. $n+1$ hat Analogie mit der Azimutalquantenzahl, die weitere Aufspaltung dieser Zahl bei der näheren Bestimmung der Kugelflächenfunktionen kann mit der Aufspaltung des Azimutalquants in ein „äquatoriales“ und ein „polares“ Quant in Analogie gesetzt werden. Diese Zahlen bestimmen *hier* das System der Knotenlinien auf der Kugel. Auch die „radiale Quantenzahl“, $l-n-1$ bestimmt genau die Zahl der „Knotenkugeln“, denn man kann sich leicht überzeugen, daß die Funktion $f(x)$ in (18) genau $l-n-1$ positive reelle Wurzeln hat. — Die positiven $E$-Werte entsprechen dem Kontinuum der hyperbolischen Bahnen, denen man in gewissem Sinn die radiale Quantenzahl $\infty$ zuschreiben kann. Dem entspricht, daß, wie wir gesehen haben, die betreffenden Lösungsfunktionen unter *beständigen* Oszillationen ins Unendliche hinaus laufen.

Von Interesse ist noch, daß der Bereich, innerhalb dessen die Funktionen (18) merklich von Null verschieden sind und innerhalb dessen sich ihre Oszillationen abspielen, jedenfalls von der *allgemeinen Größenordnung* der großen Achse der zugeordneten Ellipse ist. Der Faktor, mit dem multipliziert der Radiusvektor als Argument der konstantenfreien Funktion $f$ auftritt, ist — selbstverständlich — das Reziproke einer Länge, und diese Länge ist

$$(21) \quad \frac{K}{\sqrt{-2mE}} = \frac{K^2l}{me^2} = \frac{h^2l}{4\pi^2me^2} = \frac{a_l}{l} ,$$

wo $a_l$ die Halbachse der $l$-ten Ellipsenbahn. (Die Gleichungen folgen aus (19) zusammen mit der bekannten Beziehung $E_i = -\frac{e^2}{2a_l}$).

24\*

372

E. Schrödinger.

Die Größe (21) gibt die Größenordnung des Wurzelbereiches für kleinzahliges $l$ und $n$; denn dann darf angenommen werden, daß die Wurzeln von $f(x)$ von der Größenordnung Eins sind. Das ist natürlich nicht mehr der Fall, wenn die Koeffizienten des Polynoms große Zahlen sind. Ich möchte auf die genauere Abschätzung der Wurzeln jetzt nicht eingehen, glaube aber, daß obige Behauptung sich dabei ziemlich genau bestätigen wird.

§ 3. Es liegt natürlich sehr nahe, die Funktion $\psi$ auf *einen Schwingungsvorgang* im Atom zu beziehen, dem die den Elektronenbahnen heute vielfach bezweifelte Realität in höherem Maße zukommt als ihnen. Ich hatte auch ursprünglich die Absicht, die neue Fassung der Quantenvorschrift in dieser mehr anschaulichen Art zu begründen, habe aber dann die obige neutral mathematische Form vorgezogen, weil sie das Wesentliche klarer zutage treten läßt. Als das Wesentliche erscheint mir, daß in der Quantenvorschrift nicht mehr die geheimnisvolle „Ganzzahligkeitsforderung“ auftritt, sondern diese ist sozusagen einen Schritt weiter zurückverfolgt: sie hat ihren Grund in der Endlichkeit und Eindeutigkeit einer gewissen Raumfunktion.

Ich möchte auch jetzt noch nicht näher auf die Erörterung der Vorstellungsmöglichkeiten über diesen Schwingungsvorgang eingehen, bevor etwas kompliziertere Fälle in der neuen Fassung mit Erfolg durchgerechnet sind. Es ist nicht ausgemacht, daß dieselbe in ihren Ergebnissen ein bloßer Abklatsch der üblichen Quantentheorie sein wird. Z. B. führt das relativistische Keplerproblem, wenn man es genau nach der eingangs gegebenen Vorschrift durchrechnet, merkwürdigerweise auf *halbzahlige Teilquanten* (Radial- und Azimutquant).

Immerhin seien zu der Schwingungsvorstellung hier noch einige Bemerkungen erlaubt. Vor allem möchte ich nicht unerwähnt lassen, daß ich die Anregung zu diesen Überlegungen in erster Linie den geistvollen Thèses des Hrn. Louis de Broglie¹⁾ verdanke und dem Nachdenken über die räumliche Verteilung jener „Phasenwellen“, von denen er gezeigt hat, daß ihrer stets eine *ganze Zahl*, entlang der Bahn gemessen, auf jede

¹⁾ L. de Broglie, Ann. de Physique (10) 3. S. 22. 1925 (Thèses, Paris 1924)

Quantisierung als Eigenwertproblem.

373

Periode oder Quasiperiode des Elektrons entfallen. Der Hauptunterschied ist, daß de Broglie an fortschreitende Wellen denkt, während wir, wenn wir unseren Formeln die Schwingungsvorstellung unterlegen, auf stehende Eigenschwingungen geführt werden. Ich habe kürzlich¹) gezeigt, daß man die Einsteinsche Gastheorie auf die Betrachtung solcher stehender Eigenschwingungen, für welche man das Dispersionsgesetz der de Broglieschen Phasenwellen ansetzt, gründen kann. Die obigen Betrachtungen für das Atom hätten sich als Verallgemeinerung jener Überlegungen am Gasmodell darstellen lassen.

Faßt man die einzelnen Funktionen (18), multipliziert mit einer Kugelflächenfunktion der Ordnung $n$, als die Beschreibung von Eigenschwingungsvorgängen auf, dann muß die Größe $E$ etwas mit der Frequenz des betreffenden Vorganges zu tun haben. Nun ist man gewöhnt, daß bei Schwingungsproblemen der „Parameter“ (gewöhnlich $\lambda$ genannt) dem Quadrat der Frequenz proportional ist. Aber erstens würde ein solcher Ansatz im vorliegenden Fall gerade für die *negativen E*-Werte zu *imaginären* Frequenzen führen, zweitens sagt dem Quantentheoretiker sein Gefühl, daß die Energie der Frequenz selbst und nicht ihrem Quadrat proportional sein muß.

Der Widerspruch löst sich folgendermaßen. Für den „Parameter“ $E$ der Variationsgleichung (5) ist ja vorläufig *kein natürliches Nullniveau* festgelegt, besonders da die unbekannte Funktion $\psi$ außer mit $E$ noch mit einer Funktion von $r$ multipliziert erscheint, die, unter entsprechender Änderung des Nullniveaus von $E$, um eine Konstante abgeändert werden kann. Folglich ist die „Erwartung des Schwingungstheoretikers“ dahin zu berichtigen, daß nicht $E$ selbst — das, was wir bisher so nannten und auch weiter so nennen wollen — sondern $E$ vermehrt um eine gewisse Konstante dem Quadrat der Frequenz proportional erwartet wird. Sei diese Konstante nun *sehr groß* im Vergleich zu den Beträgen aller vorkommenden negativen $E$-Werte [die ja durch (15) beschränkt sind]. Dann werden erstens die Frequenzen *reell*, zweitens aber werden unsere $E$-Werte, da sie nur relativ kleinen Frequenzunterschieden entsprechen, tatsächlich sehr angenähert diesen Frequenzunter-

1) Erscheint demnächst in der Physik. Zeitschr.

374

E. Schrödinger.

schieden proportional. Das hinwiederum ist alles, was das „natürliche Gefühl“ des Quantentheoretikers verlangen kann, solange das Nullniveau der *Energie* nicht festgelegt ist.

Die Auffassung, daß die Frequenz des Schwingungsvorganges etwa durch

$$(22) \quad \nu = C' \sqrt{C + E} = C' \sqrt{C} + \frac{C'}{2\sqrt{C}} E + \dots$$

gegeben sei, wo $C$ eine gegen alle $E$ sehr große Konstante, hat aber noch einen anderen sehr schätzenswerten Vorzug. *Sie vermittelt ein Verständnis für die Bohrsche Frequenzbedingung.* Nach der letzteren sind doch die *Emissionsfrequenzen* den *E-Differenzen* proportional, also nach (22) auch den Differenzen der Eigenfrequenzen $\nu$ jener hypothetischen Schwingungsvorgänge. Und zwar sind die Eigenfrequenzen alle sehr groß gegen die Emissionsfrequenzen, stimmen unter sich nahe überein. Die Emissionsfrequenzen erscheinen demnach als tiefe „Differenztöne“ der mit viel höherer Frequenz erfolgenden Eigenschwingungen selbst. Daß beim Hinüberwandern der Energie aus der einen in die andere Normalschwingung *irgendetwas* — ich meine die Lichtwelle — in Erscheinung tritt, dem als *Frequenz* jene *Frequenzdifferenz* zukommt, ist sehr verständlich; man braucht sich nur vorzustellen, daß die Lichtwelle ursächlich verknüpft ist mit den während des Überganges an jeder Raumstelle notwendig auftretenden *Schwebungen* und daß die Frequenz des Lichtes bestimmt wird durch die Häufigkeit, mit der das Intensitätsmaximum des Schwebungsvorganges pro Sekunde wiederkehrt.

Es mag Bedenken erregen, daß diese Schlüsse sich auf die Beziehung (22) in ihrer *näherungsweisen* Gestalt (nach Entwicklung der Quadratwurzel) gründen, wodurch die Bohrsche Frequenzbedingung selbst scheinbar den Charakter einer Näherungsformel erhält. Das ist aber nur scheinbar und wird völlig vermieden, wenn man die *relativistische* Theorie entwickelt, durch welche überhaupt erst ein tieferes Verständnis vermittelt wird. Die große additive Konstante $C$ hängt natürlich aufs innigste zusammen mit der Ruhenergie $mc^2$ des Elektrons. Auch das scheinbar *nochmalige* und *unabhängige* Auftreten der Konstante $h$ [die doch schon durch (20) eingeführt war] in der Frequenzbedingung wird durch die relativistische Theorie auf-

Quantisierung als Eigenwertproblem.

375

geklärt bzw. vermieden. Aber leider begegnet ihre einwandfreie Durchführung vorläufig noch gewissen, oben berührten Schwierigkeiten.

Es ist kaum nötig, hervorzuheben, um wie vieles sympathischer die Vorstellung sein würde, daß bei einem Quantenübergang die Energie aus einer Schwingungsform in eine andere übergeht, als die Vorstellung von den springenden Elektronen. Die Änderung der Schwingungsform kann sich stetig in Raum und Zeit vollziehen, sie kann gern solange dauern, als erfahrungsgemäß (Kanalstrahlversuche von W. Wien) der Emissionsprozeß dauert: und gleichwohl werden, wenn während dieses Übergangs das Atom für verhältnismäßig kurze Zeit einem elektrischen Feld ausgesetzt wird, das die Eigenfrequenzen verstimmt, die Schwebungsfrequenzen sogleich mitverstimmt werden, und zwar gerade nur solange als das Feld einwirkt. Diese experimentell festgestellte Tatsache bereitet bekanntlich dem Verständnis bisher die größten Schwierigkeiten, man vergleiche etwa die Diskussion in dem bekannten Lösungsversuch von Bohr-Kramers-Slater.

Im übrigen darf man in der Freude über das menschliche Näherrücken all dieser Dinge doch nicht vergessen, daß die Vorstellung, das Atom schwinge, wenn es nicht strahlt, jeweilig in Form *einer* Eigenschwingung, daß, sage ich, diese Vorstellung, *wenn* sie festgehalten werden muß, sich doch immer noch sehr stark von dem *natürlichen* Bild eines schwingenden Systems entfernt. Denn ein makroskopisches System verhält sich ja bekanntlich nicht so, sondern liefert im allgemeinen ein Potpourri seiner Eigenschwingungen. Man darf aber seine Ansicht in diesem Punkt nicht voreilig festlegen. Auch ein Potpourri von Eigenschwingungen am einzelnen Atom würde nichts verschlagen, sofern dabei ja auch keine anderen Schwebungsfrequenzen auftreten als diejenigen, zu deren Emission das Atom erfahrungsgemäß *unter Umständen* befähigt ist. Auch die gleichzeitige wirkliche Aussendung vieler von diesen Spektrallinien durch dasselbe Atom widerspricht keiner Erfahrung. Man könnte sich also gut denken, daß bloß im Normalzustand (und näherungsweise in gewissen „metastabilen“ Zuständen) das Atom mit *einer* Eigenfrequenz schwingt und eben aus diesem Grunde *nicht* strahlt, weil nämlich keine Schwebungen auftreten.

376 E. Schrödinger. Quantisierung als Eigenwertproblem.

Die Anregung bestünde in einer gleichzeitigen Erregung einer oder mehrerer anderer Eigenfrequenzen, wodurch dann Schwebungen entstehen, welche die Lichtemission hervorrufen.

Unter allen Umständen möchte ich glauben, daß die zur gleichen Frequenz gehörigen Eigenfunktionen im allgemeinen alle gleichzeitig angeregt sind. Mehrfachheit der Eigenwerte entspricht nämlich in der Sprache der bisherigen Theorie der Entartung. Der Reduktion der Quantisierung entarteter Systeme dürfte die willkürliche Aufteilung der Energie auf die zu einem Eigenwert gehörigen Eigenfunktionen entsprechen.

# Zusatz bei der Korrektur am 28. II. 1926.

Für den Fall der klassischen Mechanik konservativer Systeme läßt sich die Variationsaufgabe schöner, als eingangs geschehen, ohne ausdrückliche Beziehung auf die Hamiltonsche partielle Differentialgleichung folgendermaßen formulieren. Sei $T(q, p)$ die kinetische Energie als Funktion der Koordinaten und Impulse, $V$ die potentielle Energie, $d\tau$ das Volumelement des Konfigurationenraums „rationell gemessen“, d. h. nicht einfach das Produkt $dq_1, dq_2 \dots dq_n$, sondern noch dividiert durch die Quadratwurzel aus der Diskriminante der quadratischen Form $T(q, p)$. (Vgl. Gibbs, Statistische Mechanik.) Dann soll $\psi$ das „Hamiltonsche Integral“

$$(23) \quad \int d\tau \left\{ K^2 T\left(q, \frac{\partial \psi}{\partial q}\right) + \psi^2 V \right\}$$

stationär machen unter der normierenden Nebenbedingung

$$(24) \quad \int \psi^2 d\tau = 1.$$

Die Eigenwerte dieses Variationsproblems sind bekanntlich die stationären Werte des Integrals (23) und liefern nach unserer These die Quantenniveaus der Energie.

Zu (14') sei noch bemerkt, daß man in der Größe $\alpha_2$ im wesentlichen den bekannten Sommerfeldschen Ausdruck $-\frac{B}{\sqrt{A}} + \sqrt{C}$ vor sich hat (vgl. „Atombau“, 4. Aufl., S. 775).

Zürich, Physikalisches Institut der Universität.

(Eingegangen 27. Januar 1926.)

Druck von Metzger & Wittig in Leipzig.
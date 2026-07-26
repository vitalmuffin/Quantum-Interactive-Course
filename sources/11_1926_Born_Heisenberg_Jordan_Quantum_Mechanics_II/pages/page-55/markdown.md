Zur Quantenmechanik. II.

611

raumstrahlung, daß man auf ein Versagen dieser Theorie schon beim einfachen Problem des harmonischen Oszillators schließen muß.

Wir wollen nun das Schwankungsquadrat $\overline{\Delta}^2$ aus den Interferenzen gemäß der Quantenmechanik berechnen. Zur Vermeidung rechnerischer Komplikationen, die das Wesen der Sache nicht berühren, beziehen wir uns auf den denkbar einfachsten Fall, nämlich eine eingespannte schwingende Saite. Es können übrigens alle wesentlichen Punkte der Rechnung ohne weiteres auf allgemeinere Fälle übertragen werden. Zunächst werde die klassische Behandlungsweise erläutert.

Die Länge der Saite sei $l$ und $u(x, t)$ die seitliche Auslenkung. Bei Einführung der durch

$$u(x, t) = \sum_{k=1}^{\infty} q_k(t) \sin k \frac{\pi}{l} x, \quad (41)$$

oder

$$q_k(t) = \frac{2}{l} \int_0^l u(x, t) \sin k \frac{\pi}{l} x \cdot dx \quad (41')$$

gegebenen Fourierkoeffizienten $q_k(t)$ als Koordinaten geht die Energie der Saite in eine Quadratsumme über. Es wird nämlich bei geeigneter Wahl der Einheiten

$$H = \frac{1}{2} \int_0^l \left\{ u^2 + \left( \frac{\partial u}{\partial x} \right)^2 \right\} dx = \frac{l}{4} \sum_{k=1}^{\infty} \left\{ \dot{q}_k(t)^2 + \left( k \frac{\pi}{l} \right)^2 q_k(t)^2 \right\}. \quad (42)$$

Für die Energie $E$ auf einem Abschnitt $(0, a)$ der Saite erhalten wir allgemeiner

$$E = \frac{1}{2} \int_0^a \sum_{j,k=1}^{\infty} \left\{ \dot{q}_j \dot{q}_k \sin j \frac{\pi}{l} x \sin k \frac{\pi}{l} x + q_j q_k j k \left( \frac{\pi}{l} \right)^2 \cos j \frac{\pi}{l} \cos k \frac{\pi}{l} x \right\} dx. \quad (43)$$

Nehmen wir in (43), Kap. 4, nur die Glieder mit $j = k$, so erhalten wir unter der ausdrücklichen Voraussetzung, daß alle in Betracht kommenden Wellenlängen klein gegen $a$ seien, gerade den Wert $\frac{a}{l} H$. Man sieht daraus: Die Differenz

$$\Delta = E - \bar{E},$$

worin der Querstrich die Mitteilung über die Phasen $\varphi_k$ in

$$q_k = a_k \cos(\omega_k t + \varphi_k); \quad \omega_k = k \frac{\pi}{l} \quad (44)$$
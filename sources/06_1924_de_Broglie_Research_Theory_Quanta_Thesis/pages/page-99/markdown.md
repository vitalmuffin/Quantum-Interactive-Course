RECHERCHES SUR LA THÉORIE DES QUANTA

119

on peut effectuer le calcul de l'énergie libre par la méthode de Planck comme pour un gaz ordinaire et, en identifiant le résultat avec l'expression ci-dessus, on trouve $A = 1$.

Dans le cas général, il faut employer une méthode plus détournée. Considérons le $p^a$ terme de la série de Planck :

$$u_{\nu p} d\nu = A \cdot \frac{8\pi}{c^3} h\nu^3 e^{-p \frac{h\nu}{kT}} d\nu.$$

On peut l'écrire aussi :

$$A \frac{8\pi}{c^3 p} \nu^2 e^{-p \frac{h\nu}{kT}} d\nu \ p \cdot h\nu$$

ce qui permet de dire :

« Le rayonnement noir peut être considéré comme le mélange d'une infinité de gaz chacun caractérisé par une valeur entière $p$ et jouissant de la propriété suivante : le nombre des états possibles d'une unité gazeuse située dans un élément de volume $dxdydz$ et ayant une énergie comprise entre $ph\nu$ et $ph(\nu + d\nu)$ est égal à $\frac{8\pi}{c^3 p} \nu^2 d\nu dxdydz$. » Dès lors, on peut calculer l'énergie libre par la méthode du premier paragraphe. On obtient :

$$\begin{aligned} F &= \sum_1^\infty F_p = -kT \sum_1^\infty \log \left[ \frac{1}{n_p!} \left( V \int_0^\infty \frac{8\pi}{c^3 p} \nu^2 e^{-p \frac{h\nu}{kT}} d\nu \right)^{n_p} \right] \\ &= -kT \sum_1^\infty n_p \log \left[ \frac{e}{n_p} V \int_0^{+\infty} \frac{8\pi}{c^3 p} \nu^2 e^{-p \frac{h\nu}{kT}} d\nu \right] \end{aligned}$$

où

$$n_p = V \int_0^{+\infty} A \frac{8\pi}{p c^3} \nu^2 e^{-p \frac{h\nu}{kT}} d\nu = A \cdot \frac{16\pi}{c^3} \frac{k^3 T^3}{h^3} \cdot \frac{1}{p^4} \cdot V.$$

Donc :

$$F = -A \frac{16\pi}{c^3 h^3} k^4 T^4 \log \left( \frac{e}{A} \right) \sum_1 \frac{1}{p^4} \cdot V$$
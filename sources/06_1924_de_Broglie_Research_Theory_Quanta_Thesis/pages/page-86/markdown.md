106

LOUIS DE BROGLIE

L'entropie maxima est déterminée par la relation : δS = 0.
La méthode des coefficients indéterminés nous apprend que,
pour réaliser cette condition il faut satisfaire à l'équation :

$$\sum_{1}^{m} \left[ \log n_i + \eta + \beta s_i \right] \delta n_i = 0$$

où η et β sont des constantes, et cela quelque soient les
δηi.

On en conclut que la distribution la plus probable, la
seule réalisée dans la pratique, est régie par la loi :

$$n_i = \alpha e^{-\beta s_i} \quad (\alpha = e^{-\eta})$$

C'est la distribution dite « canonique ». L'entropie thermodynamique du système correspondant à cette distribution
la plus probable, est donnée par :

$$S = k \mathfrak{H} \log \mathfrak{H} - \sum_{1}^{m} \left[ k \alpha e^{-\beta s_i} (\log \alpha - \beta s_i) \right]$$

ou puisque

$$\sum_{1}^{m} n_i = \mathfrak{H}$$

et

$$\sum_{1}^{m} s_i n_i = \text{énergie totale E}$$

$$S = k \mathfrak{H} \log \frac{\mathfrak{H}}{\alpha} + k \beta E = k \mathfrak{H} \log \sum_{1}^{m} e^{-\beta s_i} + k \beta E$$

Pour déterminer β nous emploierons la relation thermodynamique :

$$\frac{1}{T} = \frac{dS}{dE} = \frac{\partial S}{\partial \beta} \cdot \frac{\partial \beta}{\partial E} + \frac{\partial S}{\partial E}$$
$$= -k \mathfrak{H} \frac{\sum_{1}^{m} s_i e^{-\beta s_i}}{\sum_{1}^{m} e^{-\beta s_i}} \frac{d\beta}{dE} + k E \frac{d\beta}{dE} + k \beta$$
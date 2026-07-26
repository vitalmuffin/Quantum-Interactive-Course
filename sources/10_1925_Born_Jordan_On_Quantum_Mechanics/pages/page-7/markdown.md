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
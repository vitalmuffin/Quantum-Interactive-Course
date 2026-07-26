612

M. Born, W. Heisenberg und P. Jordan,

bedeutet, geht aus (43), Kap. 4, hervor, indem die Summanden mit $j = k$ ausgelassen werden. Dieses Phasenmittel ist mit dem Zeitmittel identisch. Man erhält dann durch Ausführung der Integration

$$\Delta = \frac{1}{4} \sum_{\substack{j,k=1 \\ j \neq k}}^{\infty} \left\{ \dot{q}_j \dot{q}_k K_{jk} + j k q_j q_k \left( \frac{\pi}{l} \right)^2 K'_{jk} \right\} \quad (45)$$

mit

$$\begin{aligned} K_{jk} &= \frac{\sin(j-k)\frac{\pi}{l}a}{(j-k)\frac{\pi}{l}} - \frac{\sin(j+k)\frac{\pi}{l}a}{(j+k)\frac{\pi}{l}} \\ &= \frac{\sin(\omega_j - \omega_k)a}{\omega_j - \omega_k} - \frac{\sin(\omega_j + \omega_k)a}{\omega_j + \omega_k}, \\ K'_{jk} &= \frac{\sin(j-k)\frac{\pi}{l}a}{(j-k)\frac{\pi}{l}} + \frac{\sin(j+k)\frac{\pi}{l}a}{(j+k)\frac{\pi}{l}} \\ &= \frac{\sin(\omega_j - \omega_k)a}{\omega_j - \omega_k} + \frac{\sin(\omega_j + \omega_k)a}{\omega_j + \omega_k}. \end{aligned} \quad (45')$$

Das Quadrat $\overline{\Delta}^2$ soll in Rücksicht auf die spätere quantenmechanische Rechnung ausführlich angeschrieben werden. Es ist

$$\Delta^2 = (\Delta_1 + \Delta_2)^2 = \Delta_1^2 + \Delta_2^2 + \Delta_1\Delta_2 + \Delta_2\Delta_1 \quad (46)$$

mit

$$\begin{aligned} \Delta_1^2 + \Delta_2^2 &= \frac{1}{16} \sum_{\substack{j,k=1 \\ j \neq k}}^{\infty} \sum_{\substack{i,\kappa=1 \\ i \neq \kappa}}^{\infty} \left\{ \dot{q}_j \dot{q}_k \dot{q}_i \dot{q}_\kappa K_{jk} K_{i\kappa} \right. \\ &\quad + j k i \kappa \left( \frac{\pi}{l} \right)^4 q_j q_k q_i q_k K'_{jk} K'_{ik}; \end{aligned} \quad (46')$$

$$\begin{aligned} \Delta_1\Delta_2 + \Delta_2\Delta_1 &= \frac{1}{16} \sum_{\substack{j,k=1 \\ j \neq k}}^{\infty} \sum_{\substack{i,\kappa=1 \\ i \neq \kappa}}^{\infty} \left( \frac{\pi}{l} \right)^4 \left\{ j k q_j q_k \dot{q}_i \dot{q}_\kappa K'_{jk} K_{i\kappa} \right. \\ &\quad + i \kappa \dot{q}_j \dot{q}_k q_i q_\kappa K_{jk} K'_{i\kappa} \}. \end{aligned} \quad (46'')$$

Aus (44), Kap. 4, folgt $\overline{\Delta_1\Delta_2 + \Delta_2\Delta_1} = 0$ und

$$\overline{\Delta}^2 = \overline{\Delta_1^2} + \overline{\Delta_2^2} = \frac{1}{8} \sum_{j,k=1}^{\infty} \left\{ \overline{q}_j^2 \overline{q}_k^2 K_{jk}^2 + j^2 k^2 \left( \frac{\pi}{l} \right)^4 \overline{q}_j^2 \overline{q}_k^2 K'_{jk}^2 \right\}. \quad (47)$$

Lassen wir nun die Seitenlänge $l$ sehr groß werden, so rücken die $\omega_k$ nach (44), Kap. 4, immer enger zusammen, so daß die Summe (47) in ein Integral übergeht:

$$\overline{\Delta}^2 = \overline{\Delta_1^2} + \overline{\Delta_2^2} = \frac{1}{8} \int_{0}^{\infty} \int_{0}^{\infty} d\omega_j d\omega_k \frac{l^2}{\pi^2} \left\{ \overline{q}_j^2 \overline{q}_k^2 K_{jk}^2 + j^2 k^2 \left( \frac{\pi}{l} \right)^4 \overline{q}_j^2 \overline{q}_k^2 K'_{jk}^2 \right\}. \quad (47')$$
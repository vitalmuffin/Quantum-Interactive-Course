138

E. Schrödinger

Gl. (41), bei festem $x_a, y_a, z_a$. Bei dieser Integration fallen rechter Hand alle Glieder fort bis auf drei, und man erhält:

$$(42) \begin{cases} \frac{\partial}{\partial t} \left[ e_a \int \psi \bar{\psi} \, dx' \right] = \frac{h e_a}{4 \pi i m_a} \left\{ \frac{\partial}{\partial x_a} \left[ \int \left( \bar{\psi} \frac{\partial \psi}{\partial x_a} - \psi \frac{\partial \psi}{\partial x_a} \right) dx' \right] + \right. \\ \left. + \frac{\partial}{\partial y_a} \left[ \int \left( \bar{\psi} \frac{\partial \psi}{\partial y_a} - \psi \frac{\partial \psi}{\partial y_a} \right) dx' \right] + \cdot \right\} \\ = \frac{h e_a}{4 \pi i m_a} \text{div}_a \left[ \int (\bar{\psi} \text{grad}_a \psi - \psi \text{grad}_a \bar{\psi}) \, dx' \right]. \end{cases}$$

In dieser Gleichung haben div und grad die gewöhnliche dreidimensional-euklidische Bedeutung und es sind $x_a, y_a, z_a$ als kartesische Koordinaten des wirklichen Raumes aufzufassen. Die Gleichung ist die Kontinuitätsgleichung der Ladungsdichte die „vom $\alpha$-ten Massenpunkt herrührt“. Bildet man die übrigen analog und addiert alle, so erhält man die pauschale Kontinuitätsgleichung. Es ist natürlich zu betonen, daß, wie stets in solchen Fällen, die Auffassung der Integrale rechter Hand als Komponenten der Stromdichte nicht absolut zwangsläufig ist, weil ein divergenzfreier Vektor hinzutreten könnte.

Um ein Beispiel zu geben, erhält man für das konservative Einelektronenproblem, wenn $\psi$ durch

$$(43) \quad \psi = \sum_k c_k u_k e^{2 \pi i v_k t + i \vartheta_k} \quad (c_k, \vartheta_k \text{ reelle Konstante})$$

gegeben ist als Stromdichte $J$

$$(44) \begin{cases} J = \frac{h e_l}{2 \pi m_l} \sum_{(k,l)} c_k c_l (u_l \text{grad } u_k - u_k \text{grad } u_l) \\ \cdot \sin [2 \pi (v_k - v_l) t + \vartheta_k - \vartheta_l]. \end{cases}$$

Man sieht, und das gilt allgemein für konservative Systeme — daß, wenn nur eine einzige Eigenschwingung erregt ist, die Stromkomponenten verschwinden und die Verteilung der Elektrizität zeitlich konstant wird; welch letzteres man ja auch unmittelbar übersieht, da $\psi \bar{\psi}$ zeitlich konstant wird. Das trifft auch dann noch zu, wenn zwar mehrere Eigenschwingungen erregt sind, aber alle zum selben Eigenwert gehören. Dagegen braucht die Stromdichte dann nicht mehr zu verschwinden, sondern es kann und wird im allgemeinen eine stationäre Stromverteilung vorliegen. Da im ungestörten Normalzustand das eine oder das andere jedenfalls zutrifft, kann man in gewissem Sinne von einer Rückkehr zu elektrostatischen und magneto-
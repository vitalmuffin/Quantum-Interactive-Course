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
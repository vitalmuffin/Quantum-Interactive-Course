We expect the change of order $\delta$ lasting for a time $\epsilon$ to be of order $\delta\epsilon$. Hence, dividing by $\delta\epsilon i/\hbar$, we can define the kinetic energy functional as

$$\mathrm{K.E.} = \frac{1}{2}m[(x_{k+1} - x_k)/\epsilon]^2 + \hbar/2\epsilon i. \tag{52}$$

This is finite as $\epsilon \to 0$ in view of (50). By making use of an equation which results from substituting $m(x_{k+1} - x_k)/\epsilon$ for $F$ in (48) we can also show that the expression (52) is equal (to order $\epsilon$) to

$$\mathrm{K.E.} = \frac{1}{2}m\left(\frac{x_{k+1} - x_k}{\epsilon}\right)\left(\frac{x_k - x_{k-1}}{\epsilon}\right). \tag{53}$$

That is, the easiest way to produce observable functionals involving powers of the velocities is to replace these powers by a product of velocities, each factor of which is taken at a slightly different time.

## 10. The Hamiltonian

# **Momentum**

The Hamiltonian operator is of central importance in the usual formulation of quantum mechanics. We shall study in this section the functional corresponding to this operator. We could immediately define the Hamiltonian functional by adding the kinetic energy functional (52) or (53) to the potential energy. This method is artificial and does not exhibit the important relationship of the Hamiltonian to time. We shall define the Hamiltonian functional by the changes made in a state when it is displaced in time.

To do this we shall have to digress a moment to point out that the subdivision of time into *equal* intervals is not necessary. Clearly, any subdivision into instants $t_i$ will be satisfactory; the limits are to be taken as the largest spacing, $t_{i+1} - t_i$ approaches zero. The total action $S$ must now be represented as a sum

$$S = \sum_i S(x_{i+1}, t_{i+1}; x_i, t_i), \tag{54}$$

where

$$S(x_{i+1}, t_{i+1}; x_i, t_i) = \int_{t_i}^{t_i+1} L(\dot{x}(t), x(t)) dt, \tag{55}$$

28
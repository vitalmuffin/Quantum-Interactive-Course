Simulating Physics with Computers

475

be true that all the various field theories have the same *kind* of behavior, and can be simulated in every way, apparently, with little latticeworks of spins and other things. It's been noted time and time again that the phenomena of field theory (if the world is made in a discrete lattice) are well imitated by many phenomena in solid state theory (which is simply the analysis of a latticework of crystal atoms, and in the case of the kind of solid state I mean each atom is just a point which has numbers associated with it, with quantum-mechanical rules). For example, the spin waves in a spin lattice imitating Bose-particles in the field theory. I therefore believe it's true that with a suitable class of quantum machines you could imitate any quantum system, including the physical world. But I don't know whether the general theory of this intersimulation of quantum systems has ever been worked out, and so I present that as another interesting problem: to work out the classes of different kinds of quantum mechanical systems which are really intersimulatable—which are equivalent—as has been done in the case of classical computers. It has been found that there is a kind of universal computer that can do anything, and it doesn't make much difference specifically how it's designed. The same way we should try to find out what kinds of quantum mechanical systems are mutually intersimulatable, and try to find a specific class, or a character of that class which will simulate everything. What, in other words, is the universal quantum simulator? (assuming this discretization of space and time). If you had discrete quantum systems, what other discrete quantum systems are exact imitators of it, and is there a class against which everything can be matched? I believe it's rather simple to answer that question and to find the class, but I just haven't done it.

Suppose that we try the following guess: that every finite quantum mechanical system can be described *exactly*, imitated exactly, by supposing that we have another system such that at each point in space-time this system has only two possible base states. Either that point is occupied, or unoccupied—those are the two states. The mathematics of the quantum mechanical operators associated with that point would be very simple.

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
where the sum is over all prime powers greater than 20 that divide p - 1. This sum (over all integers > 20) converges for t = 2, and goes down by at least a factor of 2 for each further increase of t by 1; thus for some large constant t it is less than 1/2.

Recall that each good c' is obtained with probability at least 1/16q from any experiment. Since there are q/10 good c''s, after 160t experiments, we are likely to obtain a sample of t good c''s chosen equally likely from all good c''s. Thus, we will be able to find a set of c''s such that all prime powers p_i^α_i > 20 dividing p - 1 are relatively prime to at least one of these c''s. For each prime p_i less than 20, we thus have at most 20 possibilities for the residue modulo p_i^α_i, where α_i is the exponent on prime p_i in the prime factorization of p - 1. We can thus try all possibilities for residues modulo powers of primes less than 20: for each possibility we can calculate the corresponding r using the Chinese remainder theorem, and then check to see whether it is the desired discrete logarithm.

This algorithm does not use very many properties of Z_p, so we can use the same algorithm to find discrete logarithms over other fields such as Z_p^α. What we need is that we know the order of the generator, and that we can multiply and take inverses of elements in polynomial time.

If one were to actually program this algorithm (which must wait until a quantum computer is built) there are many ways in which the efficiency could be increased over the efficiency shown in this paper.

### Acknowledgements

I would like to thank Jeff Lagarias for finding and fixing a critical bug in the first version of the discrete log algorithm. I would also like to thank him, Charles Bennett, Gilles Brassard, Andrew Odlyzko, Dan Simon, Umesh Vazirani, as well as other correspondents too numerous to list, for productive discussions, for corrections to and improvements of early drafts of this paper, and for pointers to the literature.

### References

1. P. Benioff, "Quantum mechanical Hamiltonian models of Turing machines," J. Stat. Phys. Vol. 29, pp. 515-546 (1982).

2. P. Benioff, "Quantum mechanical Hamiltonian models of Turing machines that dissipate no energy," Phys. Rev. Lett. Vol. 48, pp. 1581-1585 (1982).

3. C. H. Bennett, "Logical reversibility of computation," IBM J. Res. Develop. Vol. 17, pp. 525-532 (1973).

4. C. H. Bennett, E. Bernstein, G. Brassard and U. Vazirani, "What is feasible on a quantum computer," manuscript (1994).

5. E. Bernstein and U. Vazirani, "Quantum complexity theory," in Proc. 25th ACM Symp. on Theory of Computation, pp. 11-20 (1993).

6. A. Berthiaume and G. Brassard, "The quantum challenge to structural complexity theory," in Proc. 7th IEEE Conf. on Structure in Complexity Theory, pp. 132-137 (1992).

7. A. Berthiaume and G. Brassard, "Oracle quantum computing," in Proc. Workshop on Physics of Computation, pp. 195-199, IEEE Press (1992).

8. D. Coppersmith, "An approximate Fourier transform useful in quantum factoring," IBM Research Report RC 19642 (1994).

9. D. Deutsch, "Quantum theory, the Church-Turing principle and the universal quantum computer," Proc. Roy. Soc. Lond. Vol. A400, pp. 96-117 (1985).

10. D. Deutsch, "Quantum computational networks," Proc. Roy. Soc. Lond. Vol. A425, pp. 73-90 (1989).

11. D. Deutsch and R. Jozsa, "Rapid solution of problems by quantum computation," Proc. Roy. Soc. Lond. Vol. A439, pp. 553-558 (1992).

12. D. P. DiVincenzo, "Two-bit gates are universal for quantum computation," manuscript (1994).

13. R. Feynman, "Simulating physics with computers," International Journal of Theoretical Physics, Vol. 21, No. 6/7, pp. 467-488 (1982).

14. R. Feynman, "Quantum mechanical computers," Foundations of Physics, Vol. 16, pp. 507-531 (1986). (Originally appeared in Optics News, February 1985.)

15. L. Fortnow and M. Sipser, "Are there interactive protocols for co-NP languages?" Inform. Proc. Lett. Vol. 28, pp. 249-251 (1988).

16. D. M. Gordon, "Discrete logarithms in GF(p) using the number field sieve," SIAM J. Discrete Math. Vol. 6, pp. 124-139 (1993).

17. G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers, Fifth Edition, Oxford University Press, New York (1979).

18. R. Landauer, "Is quantum mechanics useful?" Proc. Roy. Soc. Lond., to appear (1994).

19. A. K. Lenstra and H. W. Lenstra, Jr., eds., The Development of the Number Field Sieve, Lecture Notes in Mathematics No. 1554, Springer-Verlag (1993).

20. H. W. Lenstra, Jr. and C. Pomerance, "A rigorous time bound for factoring integers, J. Amer. Math. Soc. Vol. 5, pp. 483-516 (1992).

21. S. Lloyd, "A potentially realizable quantum computer," Science, Vol. 261, pp. 1569-1571 (1993).

133
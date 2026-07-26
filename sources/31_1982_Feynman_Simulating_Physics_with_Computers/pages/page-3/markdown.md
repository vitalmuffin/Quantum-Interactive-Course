Simulating Physics with Computers

469

Another thing that had been suggested early was that natural laws are reversible, but that computer rules are not. But this turned out to be false; the computer rules can be reversible, and it has been a very, very useful thing to notice and to discover that. (Editors' note: see papers by Bennett, Fredkin, and Toffoli, these Proceedings). This is a place where the relationship of physics and computation has turned itself the other way and told us something about the possibilities of computation. So this is an interesting subject because it tells us something about computer rules, and *might* tell us something about physics.

The rule of simulation that I would like to have is that the number of computer elements required to simulate a large physical system is only to be proportional to the space-time volume of the physical system. I don't want to have an explosion. That is, if you say I want to explain this much physics, I can do it exactly and I need a certain-sized computer. If doubling the volume of space and time means I'll need an *exponentially* larger computer, I consider that against the rules (I make up the rules, I'm allowed to do that). Let's start with a few interesting questions.

## 2. SIMULATING TIME

First I'd like to talk about simulating time. We're going to assume it's discrete. You know that we don't have infinite accuracy in physical measurements so time might be discrete on a scale of less than $10^{-27}$ sec. (You'd have to have it at least like to this to avoid clashes with experiment—but make it $10^{-41}$ sec. if you like, and then you've got us!)

One way in which we simulate time—in cellular automata, for example—is to say that 'the computer goes from state to state.' But really, that's using intuition that involves the idea of time—you're going from state to state. And therefore the time (by the way, like the space in the case of cellular automata) is not simulated at all, it's imitated in the computer.

An interesting question comes up: 'Is there a way of simulating it, rather than imitating it?' Well, there's a way of looking at the world that is called the space-time view, imagining that the points of space and time are all laid out, so to speak, ahead of time. And then we could say that a 'computer' rule (now computer would be in quotes, because it's not the standard kind of computer which operates in time) is: We have a state $s_i$ at each point $i$ in space-time. (See Figure 1.) The state $s_i$ at the space time point $i$ is a given function $F_i(s_j, s_k, \ldots)$ of the state at the points $j, k$ in some neighborhood of $i$:

$$
s_i = F_i(s_j, s_k, \ldots)
$$
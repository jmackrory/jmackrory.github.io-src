Title: Physics Studies
Author: Jonathan Mackrory
Date: Oct 22, 2018


# Graduate Physics Study

I worked on two main projects during my Ph.D, 
which were undertaken in close collaboration with my advisor Dan Steck and others. 
Both projects rely on numerical Monte Carlo simulations to compute quantum effects 
relevant to modern experiments in single atoms. 
I want to touch a little on what we did, what attracted me to the work,
and why I'm leaving.

## Continuous Quantum Position Measurement

The first project considered continuous quantum measurement of single atoms.
Modern experimental apparatus can trap and cool atoms using a combination of lasers and 
magnetic fields. It is then possible to interact repeatedly with the same atom. 
In particular, it's possible to shine light on an atom, detect the resulting fluorescence,
and image the resulting light to measure where the atom is.
This in effect is a measurement of the atom's position, where the strength of the 
position measurement depends on the imaging system, strength of the lasers, and thus varies 
as a function of position.
As for the actual work, you can simulate the measurement process by 
randomly sampling from the possible outcomes (detection, no-detection) at each time step ,
and thus build up a "quantum trajectory" for the atom.  This is only one possible history,
so one must average over all such possible trajectories consistent with the data.

## Casimir Worldlines

I pivoted mostly towards work on the Casimir effect around 2011.
The Casimir effect is a tiny attractive force between materials like glass, metals and atoms.
Amazingly enough it's a macroscopic effect arising due to quantum field theory. 
The Casimir effect is a generalization of the van der Waals force 
between molecules that you might be familiar with from chemistry. 
The Casimir force arises due to quantum fluctuations in vacuum electromagnetic fields
(i.e. there's still a force even with no photons).
So far, so abstract.  This force is relevant at the micron scale that a lot of 
experiments take place where it is an important background. 
The related van der Waals force has also been shown to be how geckos stick to surfaces.

The worldline method is a method for calculating Casimir forces using closed random walks
which can be thought of as the spatial trajectories of a vacuum fluctuation.
The original method considered a scalar field with idealized surfaces.
We aimed to extend this to electromagnetism (which is a vector field),
and consider more realistic materials. 

So it turns out this is really hard, but we got part way. 
Even in a planar geometry there's a host of difficulties. 
For more details see my Ph.D. thesis for the whole gloomy tale.

So this touched on a couple cool things: it uses monte Carlo simulations,
it relies on path integrals, and there's analogies between dielectrics and curved surfaces.
I got to read up on quantum mechanics on curved manifolds, a whole lot of complicated math,
all for something that ties into an experiment. 
Pity I'm a fucking moron and couldn't seal the deal.

Why leave this behind?
Frankly, I'm terrible at this.  There's far smarter people people working on more interesting problems.
Learning physics has been great, and going to grad school meant I heard the Gospel of the Renormalization Group,
which unified the sweep of physics, and I've had the chance to interact with brilliant students and faculty.
But ultimately, it's time to acknowledge that I don't really care that much about quantum physics,
the applications are perpetually 20 years away, 
I'm not that good enough at it, and it's time to move on.

But don't worry, I'll be much better at data science.  Honest. 

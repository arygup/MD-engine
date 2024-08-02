import numpy as np
import Box
from PBC import pbc 
from Energy import pe_sys, F
import Propagator
import copy


# X += t*a


def minisation(sim,particles):
        X = copy.copy(particles.X)
        V = copy.copy(particles.V)
        L = particles.L
        n = particles.n
        s = sim.s 
        t = sim.t
        PE = sim.PE 
        acc = np.zeros((n,3))
        for l in X:
            acc -= F(X-l)
        PE[0] = pe_sys(X)
        for j in range(1,s):
            PE[j] = pe_sys(X)
            if(PE[j] > PE[j-1]):
                return j,PE[j-1],X
            X += t*V + 0.5*t*t*acc
            acc2 = np.zeros((n,3))
            for l in X:
                acc2 -= F(X-l)
            acc+=acc2
            V += 0.5*acc*t
            acc = acc2
            pbc(X,V,L)   
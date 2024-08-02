import numpy as np
import Box
from PBC import pbc 
from Energy import pe_sys, ke_sys, F
import matplotlib.pyplot as plt


class Propagator:
    def __init__(self,s,t):
        self.s = s
        self.t = t
        self.H = np.zeros(s)
        self.KE = np.zeros(s)
        self.PE = np.zeros(s)
        self.PLTX = np.zeros(s)
        self.PLTV = np.zeros(s)
        self.sigma = 10
        self.nu = 10
        self.tau = 10
        self.ke_T = 10

    def run(self,particles,thermostat):
        X = particles.X
        V = particles.V
        L = particles.L
        n = particles.n
        s = self.s 
        t = self.t
        KE = self.KE 
        PE = self.PE 
        PLTX = self.PLTX 
        PLTV = self.PLTV 
        ke_T = self.ke_T
        sigma = self.sigma
        nu = self.nu
        tau = self.tau
        acc = np.zeros((n,3))
        for l in X:
            acc -= F(X-l)
        for j in range(s):
            KE[j] = ke_sys(V)
            PE[j] = pe_sys(X)
            PLTX[j] = (X[0][0] + X[1][0])
            PLTV[j] = V[0][0] + V[1][0]
            X += t*V + 0.5*t*t*acc
            acc2 = np.zeros((n,3))
            for l in X:
                acc2 -= F(X-l)
            acc+=acc2
            V += 0.5*acc*t
            acc = acc2
            thermostat(V,t,sigma,nu,ke_T,tau)
            pbc(X,V,L)   
        self.H = KE + PE
        self.KE = KE
        self.PE = PE
        self.PLTX = PLTX
        self.PLTV = PLTV
        particles.update(X,V)



    def plot0th(self):
        x1 = np.linspace(0, 1, self.s)
        plt.plot(x1, self.PLTV,color='red')
        plt.plot(x1, self.PLTX)
        plt.savefig('0th.png')
        plt.close()

    def plot(self):
        x1 = np.linspace(0, 1, self.s)
        plt.plot(x1, self.H,color='green')
        plt.plot(x1, self.PE,color='purple')
        plt.plot(x1, self.KE, color='red')   
        plt.savefig('energy.png')
        plt.close()

    def plotMin(self,j,minE):
        x1 = np.linspace(0, 1, self.s)
        plt.plot(x1, self.PE,color='purple')
        plt.plot(j, minE,'ro')   
        plt.savefig('Minenergy.png')
        plt.close()

    def plotPS(self):
        plt.scatter(self.PLTV, self.PLTX)
        plt.savefig('PS.png')
        plt.close()


def createSim(s,t):
    v = Propagator(s,t)
    return v
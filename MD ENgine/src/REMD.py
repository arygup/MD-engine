import numpy as np
import Box
from PBC import pbc 
from Energy import pe_sys, ke_sys, F
import matplotlib.pyplot as plt


class REMD:
    def __init__(self,s,t):
        self.s = s
        self.t = t
        self.H = np.zeros(s)
        self.KE = np.zeros(s)
        self.PE = np.zeros(s)
        self.PLTX = np.zeros(s)
        self.PLTV = np.zeros(s)
        self.H2 = np.zeros(s)
        self.KE2 = np.zeros(s)
        self.PE2 = np.zeros(s)
        self.PLTX2 = np.zeros(s)
        self.PLTV2 = np.zeros(s)
        self.sigma = 10
        self.nu = 10
        self.tau = 10
        self.ke_T2 = 10
        self.sigma2 = 10
        self.nu2 = 10
        self.tau2 = 10
        self.ke_T2 = 10

    def run(self,particles,particles2,thermostat):
        n = particles.n
        s = self.s 
        t = self.t
        count = 0
        X = particles.X
        V = particles.V
        L = particles.L
        KE = self.KE 
        PE = self.PE 
        PLTX = self.PLTX 
        PLTV = self.PLTV 
        X2 = particles2.X
        V2 = particles2.V
        L2 = particles2.L
        KE2 = self.KE2 
        PE2 = self.PE2 
        PLTX2 = self.PLTX2 
        PLTV2 = self.PLTV2 
        ke_T = self.ke_T
        sigma = self.sigma
        nu = self.nu
        tau = self.tau
        ke_T2 = self.ke_T2
        sigma2 = self.sigma2
        nu2 = self.nu2
        tau2 = self.tau2

        acc = np.zeros((n,3))
        for l in X:
            acc -= F(X-l)
        acc3 = np.zeros((n,3))
        for l in X2:
            acc3 -= F(X2-l)
        for j in range(s):
            KE[j] = ke_sys(V)
            PE[j] = pe_sys(X)
            KE2[j] = ke_sys(V2)
            PE2[j] = pe_sys(X2)
            PLTX[j] = X[0][0]
            PLTV[j] = V[0][0]
            PLTX2[j] = X2[0][0]
            PLTV2[j] = V2[0][0]
            X += t*V + 0.5*t*t*acc
            X2 += t*V2 + 0.5*t*t*acc3
            acc2 = np.zeros((n,3))
            acc4 = np.zeros((n,3))
            for l in X:
                acc2 -= F(X-l)
            acc+=acc2
            for l in X2:
                acc4 -= F(X2-l)
            acc3+=acc4
            V += 0.5*acc*t
            acc = acc2
            V2 += 0.5*acc3*t
            acc3 = acc4
            thermostat(V,t,sigma,nu,ke_T,tau)
            pbc(X,V,L) 
            thermostat(V2,t,sigma2,nu2,ke_T2,tau2)
            pbc(X2,V2,L2)   
            if(PE[j] > PE2[j]):
                count = count + 1
                Z = X
                X = X2
                X2 = Z
                Z = V
                V = V2
                V2 = Z
                Z = acc
                acc = acc3
                acc3 = Z

        self.H = KE + PE
        self.KE = KE
        self.PE = PE
        self.PLTX = PLTX
        self.PLTV = PLTV
        particles.update(X,V)
        self.H2 = KE2 + PE2
        self.KE2 = KE2
        self.PE2 = PE2
        self.PLTX2 = PLTX2
        self.PLTV2 = PLTV2
        particles.update(X2,V2)
        return count

    def plot0th(self):
        x1 = np.linspace(0, 1, self.s)
        plt.plot(x1, self.PLTV,color='red')
        plt.plot(x1, self.PLTX)
        plt.savefig('T_Lowth.png')
        plt.close()
        plt.plot(x1, self.PLTV2,color='red')
        plt.plot(x1, self.PLTX2)
        plt.savefig('T_Highth.png')
        plt.close()

    def plot(self):
        x1 = np.linspace(0, 1, self.s)
        plt.plot(x1, self.H,color='green')
        plt.plot(x1, self.PE,color='purple')
        plt.plot(x1, self.KE, color='red')   
        plt.savefig('T_Low.png')
        plt.close()
        plt.plot(x1, self.H2,color='green')
        plt.plot(x1, self.PE2,color='purple')
        plt.plot(x1, self.KE2, color='red')
        plt.savefig('T_High.png')
        plt.close()

def createREMD(s,t):
    v = REMD(s,t)
    return v
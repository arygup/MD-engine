import numpy as np
from Energy import ke_sys

def Anderson(V,t,sigma,nu,ke_T,tau):
    prob_col = t*nu
    prob = np.random.uniform(0, 1, len(V))
    V[prob <= prob_col] = np.random.normal(0, sigma,3)
    V -= np.mean(V)
    
def Velocity_rescale(V,t,sigma,nu,ke_T,tau):
    v_scale = np.sqrt(ke_T/ke_sys(V))
    V *= v_scale
    V -= np.mean(V)
    
def Berendsen(V,t,sigma,nu,ke_T,tau):
    v_scale = np.sqrt(1 + (t/tau)*((ke_T/ke_sys(V)) -1))
    V *= v_scale
    V -= np.mean(V)

def Non(V,t,sigma,nu,ke_T,tau):
    return 0

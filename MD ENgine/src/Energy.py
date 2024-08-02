import numpy as np
from sympy import symbols, diff, lambdify
import math
#import autograd.numpy as np
#from autograd import grad

k = 0.1
def pe(x):
    return 0.5*k*x*x
    #return 5*x*x*x*x - 2*x*x + 0.2


#Force calculations from PE
x = symbols('x')
f = pe(x)
force = diff(f, x)
F = lambdify(x, force)

# def pe(x):
#     if x <= -1.25:
#         return 4*np.pi**2*(x+1.25)**2
#     if x > -1.25 and x <= -0.25:
#         return 2*(1+np.sin(2*np.pi*x))
#     if x > -0.25 and x <= 0.75:
#         return 3*(1+np.sin(2*np.pi*x))
#     if x > 0.75 and x <= 1.75: 
#         return 4*(1+np.sin(2*np.pi*x))
#     if x > 1.75: 
#         return 8*np.pi**2*(x-1.75)**2
    
# Forc = grad(pe)
# F = np.vectorize(Forc)


def ke_sys(V):
    return np.sum(V**2) * 0.5
    
def pe_sys(X):
    te = 0
    for l in X:
        te += pe(np.sqrt(np.sum((X-l)**2)))
    return te*0.5



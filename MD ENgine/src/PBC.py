import numpy as np

def pbc(X,V,L):
    V[X >= L] *= -1
    V[X <= 0] *= -1
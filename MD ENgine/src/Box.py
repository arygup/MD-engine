import numpy as np

class Box:
    def __init__(self,n,L):
        self.X = np.random.uniform(0.001,L,(n,3))
        self.V = np.zeros((n,3))
        self.L = L
        self.n = n
    
    def update(self,X,V):
        self.X = X
        self.V = V

def createBox(n,l):
    v = Box(n,l)
    return v



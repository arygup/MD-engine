import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./src')
import Box
import Propagator
import REMD
from Thermostats import Anderson, Berendsen, Velocity_rescale, Non
from Energy import pe_sys,F
from Minimisation import minisation
from REMD import createREMD


# Set up for box 
particles = Box.createBox(2,10)  # n,L
particles.X = np.array([[0.0,0.0000,0.0000],[8.0,0.0000,0.0000]])
print(particles.X)
sim = Propagator.createSim(10000, 0.01) # s, t
#p2 = Box.createBox(particles.n,particles.L)
#remd = REMD.createREMD(100,0.01) 

# Calculate some sigma for Anderson, sigma = square root of KbT
sim.sigma = 0.1*np.sqrt((pe_sys(particles.X)*2)/9)
sim.nu = 7
#remd.sigma = 10*np.sqrt((pe_sys(particles.X)*2)/9)
#remd.sigma2 = 1.1*remd.sigma
#remd.nu = 7
#remd.nu2 = 7
# Berendsen & Velocity rescale, constant temp T lets assume the KE & tau for Berendsen 
sim.ke_T = pe_sys(particles.X)/4.5
sim.tau = 10*sim.t
#remd.ke_T = pe_sys(particles.X)/4.5
#remd.tau = 10*remd.t
#remd.ke_T2 = 1.1*remd.ke_T
#remd.tau = 1.1*remd.tau


# Run Minimisation 
#j,pefound,Y = minisation(sim,particles)
#j,pefound,X = minisation(remd,particles)
#particles.update(X,particles.V)


# Run simulation 
sim.run(particles,Anderson)
print(particles.X)
sim.plot()
#sim.plot0th()
#sim.plotMin(j/sim.s,pefound)
sim.plotPS()
#count = remd.run(particles,p2,Anderson)
#print("number of exhanges: ", count)
#print("range of motion :", min(remd.PLTX),min(remd.PLTX2), max(remd.PLTX), max(remd.PLTX2))
#remd.plot()
#remd.plot0th()

# print("minimisation pe found: ", pefound)
# print("actual min pe:", np.min(sim.PE))
# sim.plotMin((j-1)/sim.s,pefound)
#sim.plot0th()


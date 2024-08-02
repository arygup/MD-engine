Sure! Here's a README file for your simulation project:

---

# Molecular Dynamics Simulation

This project implements a molecular dynamics simulation framework using Python. The framework allows the creation of particle systems, simulation of their dynamics, and the application of various thermostats for temperature control.

## Features

- **Particle System Creation**: Initialize a system of particles in a box.
- **Simulation Propagation**: Run the simulation using different propagation techniques.
- **Thermostats**: Apply various thermostats such as Anderson, Berendsen, and Velocity Rescale.
- **Energy Calculation**: Compute potential energy and forces.
- **Minimization**: Perform energy minimization.
- **Visualization**: Plot and visualize the simulation results.

## Dependencies

- `matplotlib`
- `numpy`

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/molecular-dynamics-simulation.git
cd molecular-dynamics-simulation
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

1. **Setup the Box**: Create a box with particles and set their initial positions.

```python
import numpy as np
import Box

particles = Box.createBox(2, 10)  # n: number of particles, L: box length
particles.X = np.array([[0.0, 0.0, 0.0], [8.0, 0.0, 0.0]])
print(particles.X)
```

2. **Create Simulation**: Initialize the simulation parameters.

```python
import Propagator

sim = Propagator.createSim(10000, 0.01)  # s: steps, t: time step
```

3. **Set Thermostat Parameters**: Calculate sigma for the Anderson thermostat and other parameters.

```python
from Energy import pe_sys

sim.sigma = 0.1 * np.sqrt((pe_sys(particles.X) * 2) / 9)
sim.nu = 7
sim.ke_T = pe_sys(particles.X) / 4.5
sim.tau = 10 * sim.t
```

4. **Run Minimization** (optional): Perform energy minimization.

```python
# from Minimisation import minisation

# j, pefound, Y = minisation(sim, particles)
# particles.update(Y, particles.V)
```

5. **Run Simulation**: Execute the simulation with a chosen thermostat.

```python
from Thermostats import Anderson

sim.run(particles, Anderson)
print(particles.X)
```

6. **Plot Results**: Visualize the simulation results.

```python
sim.plot()
sim.plotPS()
```

## Example

The following example sets up a box with 2 particles, initializes the simulation parameters, applies the Anderson thermostat, and visualizes the results.

```python
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./src')
import Box
import Propagator
from Thermostats import Anderson
from Energy import pe_sys

# Set up the box
particles = Box.createBox(2, 10)
particles.X = np.array([[0.0, 0.0, 0.0], [8.0, 0.0, 0.0]])
print(particles.X)

# Create simulation
sim = Propagator.createSim(10000, 0.01)

# Set thermostat parameters
sim.sigma = 0.1 * np.sqrt((pe_sys(particles.X) * 2) / 9)
sim.nu = 7
sim.ke_T = pe_sys(particles.X) / 4.5
sim.tau = 10 * sim.t

# Run simulation
sim.run(particles, Anderson)
print(particles.X)

# Plot results
sim.plot()
sim.plotPS()
```
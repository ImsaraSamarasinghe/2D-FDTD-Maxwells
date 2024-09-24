# 2D Electromagnetic Wave Propagation Simulation

This project simulates the propagation of an electromagnetic wave in 2D using the finite-difference time-domain (FDTD) method. It visualizes the evolution of the electric field \( E_x \) over time in a grid, which is updated dynamically and saved as an animation.

## Features
- Simulation of electromagnetic wave propagation in 2D using FDTD.
- Visualization of the \( E_x \) component of the electric field.
- Animated output saved as a `.gif` file.

## Requirements
Before running the code, ensure that you have the following Python libraries installed:
- `numpy`
- `matplotlib`
- `pillow` (for saving the animation as a GIF)

You can install the dependencies via pip:

```bash
pip install numpy matplotlib pillow
```

## Simulation Details
- **Grid Setup:** The simulation uses a square grid of the size *200 x 200* with a spatial step of *dx = dz = 0.005*.
- **Time Steps:** The number of time steps is set to 350 *(nt = 350)*.
- **Wave Source:** A Gaussian pulse centered at the grid midpoint is used as the wave source.
- **Boundary Conditions:** Simple absorbing boundary conditions are applied to prevent reflections from the edges.
- **Wave Equation:** The electric and magnetic fields are updated according to the 2D Maxwell’s equations using finite differences.

## Code Overview
1. **Field Initialisation:**
   -`Hy`,`Ex` and `Ez` are the magnetic and electric field components initalised to zero
2. **Meshgrid Creation:**
   -`X` and `Y` are used to create a grid for plotting the wave in 3D.
3. **Wave Propogation**:
   -The core of the simulation is an update function that calculates the new values for `Hy`, `Ex` and `Ez` at each time step using finite differences.
4. **Boundary Conditions:**
   -The electric field components are updated to simulate absorbing boundary conditions.
5. **Visualization:**
   -A 3D surface plot of `Ex` is updated at each time step.
   -The animation is created using `matplotlib.animation.FuncAnimation` and saved as `wave_2d_Ex.gif`

## Running the Simulation
To run the simulation, simply execute the Python script. The animation will be saved as `wave_2d_Ex.gif` in the current directory.

```bash
python wave_simulation.py
```

## Output
The output is a GIF animation of the electric field `Ex`, which shows the propogation of an electromagnetic wave in a 2d grid.

![](https://github.com/ImsaraSamarasinghe/2D-FDTD-Maxwells/blob/main/wave_2d_Hy.gif)

## Aknowledgements
This project is based on the FDTD method for solving Maxwell's equations in 2D, often used in computational electromagnetics simulations.

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

# Parameters
x_start = 0
x_end = 2
z_start = 0
z_end = 2

nx = 200
nz = nx
nt = 350
source_posx = int(nx / 2)
source_posz = int(nz / 2)

dx = 0.005
dz = dx
c0 = 3e8
dt = 0.5 * dx / c0

t0 = 20
spread = 8

# Initialize fields
Hy = np.zeros((nx, nx))
Ex = np.zeros((nx, nx))
Ez = np.zeros((nx, nx))

x = np.linspace(x_start, x_end, nx)
z = np.linspace(z_start, z_end, nz)

# Create meshgrid for plotting
X, Y = np.meshgrid(x, z)

# Set up the figure and axis
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Update function for animation
def update(t):
    global Hy, Ex, Ez
    Hy[1:-1, 1:-1] = Hy[1:-1, 1:-1] - c0 * dt / dz * (Ex[1:-1, 1:-1] - Ex[1:-1, :-2]) + c0 * dt / dx * (Ez[1:-1, 1:-1] - Ez[:-2, 1:-1])
    Ex[source_posx, source_posz] = math.exp(-0.5 * ((t - t0) / spread) ** 2)
    Ex[1:-1, 1:-1] = Ex[1:-1, 1:-1] - c0 * dt / dz * (Hy[1:-1, 2:] - Hy[1:-1, 1:-1])
    Ez[1:-1, 1:-1] = Ez[1:-1, 1:-1] + c0 * dt / dx * (Hy[2:, 1:-1] - Hy[1:-1, 1:-1])

    # set B.C.s
    Ex[0, :] = Ex[1, :]  # Left boundary
    Ex[-1, :] = Ex[-2, :]  # Right boundary
    Ex[:, 0] = Ex[:, 1]  # Bottom boundary
    Ex[:, -1] = Ex[:, -2]  # Top boundary

    # Update the contour plot with the new Ex values
    ax.clear()  # Clear the previous frame
    ax.plot_surface(X, Y, Ex, cmap='viridis')
    # Set axis limits and labels
    ax.set_zlim(-0.05, 0.05)  # Adjust based on the expected range of Ex
    ax.set_xlabel('Z')
    ax.set_ylabel('X')
    ax.set_zlabel('Ex')

    return ax

# Create the animation
anim = FuncAnimation(fig, update, frames=nt, blit=False)

# Save the animation as a gif
anim.save('wave_2d_Ex.gif', writer='pillow', fps=30)


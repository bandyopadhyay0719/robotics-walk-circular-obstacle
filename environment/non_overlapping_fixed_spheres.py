import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from environment.Spheres import Sphere


def plot_sphere(ax, center, radius):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='b')


def create_spheres(ax):
    spheres = [
        ([2, 2, 1], 1),
        ([3, 3, 3], 0.5),
        ([5, 4, 5], 1),
        ([5, 3, 3], 1),
        ([2, 4, 4], 1)
    ]
    # fig = plt.figure(figsize=(10, 10))
    # ax = fig.add_subplot(111, projection='3d')

    # Define the centers and radii of the spheres

    for center, radius in spheres:
        plot_sphere(ax, center, radius)
        Sphere.spheres.append(Sphere(center, radius))

    # Set aspect ratio, labels, and show plot
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
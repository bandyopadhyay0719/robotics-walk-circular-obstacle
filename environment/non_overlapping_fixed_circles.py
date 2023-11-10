import matplotlib.pyplot as plt
import numpy as np
from walk.Circles import Circle


def plot_circle(center_in, radius_in):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = center_in[0] + radius_in * np.cos(theta)
    y = center_in[1] + radius_in * np.sin(theta)
    plt.plot(x, y)


def create_circles(plt, axes):
    circles = [
        ((2, 2), 1),
        ((6, 2), 0.8),
        ((4, 5), 1.2),
        ((8, 6), 1.5),
        ((2, 7), 0.7),
        ((4.5, 8.5), 0.7)
    ]
    # plt.figure(figsize=(8, 8))
    # for center, radius in circles:
    #     plot_circle(center, radius)
    #
    # plt.gca().set_aspect('equal', adjustable='box')
    # plt.xlim(0, 10)
    # plt.ylim(0, 10)
    # plt.xlabel('X')
    # plt.ylabel('Y')

    for center, radius in circles:

        circle = plt.Circle(center, radius, fill=True, color='b')
        Circle.circles.append(Circle(center, radius))
        axes.add_patch(circle)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
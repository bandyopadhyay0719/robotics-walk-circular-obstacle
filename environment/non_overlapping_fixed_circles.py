import matplotlib.pyplot as plt
import numpy as np
from walk.Circles import Circle

def plot_circle(center_in, radius_in):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = center_in[0] + radius_in * np.cos(theta)
    y = center_in[1] + radius_in * np.sin(theta)
    plt.plot(x, y)


def create_circles(plt, axes):
    # if is_random:
    #     Circle.circles = create_circles_random(start, end, min_radius= 0.3, max_radius= 2)

    circles = [
        ((2, 2), 1),
        ((6, 2), 0.8),
        ((4, 5), 1.2),
        ((8, 6), 1.5),
        ((2, 7), 0.7),
        ((4.5, 8.5), 0.7)
    ]


    for center, radius in circles:

        circle = plt.Circle(center, radius, fill=True, color='b')
        Circle.circles.append(Circle(center, radius))
        axes.add_patch(circle)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
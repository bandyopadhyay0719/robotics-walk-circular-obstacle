from walk.Circles import Circle
from walk.intersect import is_point_within_circle
import matplotlib.pyplot as plt
import numpy as np
import random

Circle.circles = []

start = np.array((1, 1))
end = np.array((7, 7))


def create_circles_random(start_in, end_in, min_radius, max_radius):
    i = 0
    if start_in[0] > end_in[0]:
        xsmall_end = end_in[0]
        xbig_end = start_in[0]
    else:
        xsmall_end = start_in[0]
        xbig_end = end_in[0]

    if start_in[1] > end_in[1]:
        ysmall_end = end_in[1]
        ybig_end = start_in[1]
    else:
        ysmall_end = start_in[1]
        ybig_end = end_in[1]
    while i < 10:

        x = random.randint(xsmall_end, xbig_end)
        y = random.randint(ysmall_end, ybig_end)
        r = random.uniform(min_radius, max_radius)
        if i == 0:
            Circle.circles.append(Circle((x, y), r))
            i += 1
        else:
            if not is_point_within_circle(start_in, (x, y), r + 0.2) and not is_point_within_circle(end_in, (x, y), r):
                if not Circle.if_intersecting((x, y), r + 0.2, Circle.circles):
                    Circle.circles.append(Circle((x, y), r))
                    i += 1

    return Circle.circles


def draw_circles(circle_list):
    for circle in circle_list:
        center = circle.center
        radius = circle.radius
        draw_circle = plt.Circle(center, radius, color="darkorange")
        # Create a new plot and add the circle directly
        plt.gca().add_patch(draw_circle)


def find_largest_radius(circles):
    largest_radius = 0
    for circle in circles:
        if circle.radius > largest_radius:
            largest_radius = circle.radius
    return largest_radius


def dimensions(start_point, end_point, r):
    plt.gca().set_aspect("equal")
    if start_point[0] < end_point[0]:
        plt.xlim(start_point[0] - .1 - r, end_point[0] + .1 + r)
    else:
        plt.xlim(end_point[0] - .1 - r, start_point[0] + .1 + r)

    if start_point[1] < end_point[1]:
        plt.ylim(start_point[1] - .1 - r, end_point[1] + .1 + r)
    else:
        plt.ylim(end_point[1] - .1 - r, start_point[1] + .1 + r)


circles_list = create_circles_random(start, end, 0.3, 3)

draw_circles(circles_list)

radius = find_largest_radius(circles_list)
dimensions(start, end, radius)

plt.show()

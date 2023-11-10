import matplotlib.pyplot as plt
import numpy as np
from utilities import *


def walk(start, end, circle_center, circle_radius, h, alpha, plt, axes):
    vector = end - start
    walk_vector = alpha * h * (vector / np.linalg.norm(vector))

    next_start = start + walk_vector
    intersections = intersection_points(start, end, circle_center, circle_radius)
    intersection = first_intersection_point(intersections, start)
    if is_point_within_object(next_start, circle_center, circle_radius):
        if intersection is not None:
            plot_point(intersection, plt, axes)
            normal_vector = find_normal_vector(start, end, circle_center, circle_radius)
            if normal_vector is not None:
                next_start = start + h * alpha * normal_vector
                plot_point(next_start, plt, axes)
    else:
        if np.linalg.norm(next_start - end) > (alpha * h):
            plot_point(next_start, plt, axes)
    return next_start


def run_robot(start_point, end_point, center, radius):
    fig = plt.figure()
    if len(start_point) == 2:
        ax = fig.add_subplot(111, aspect='equal')
    else:
        ax = fig.add_subplot(111, projection='3d')
    plot_circle_or_sphere(center, radius, start_point, end_point, plt, ax)
    plot_point(start_point, plt, ax)
    plot_point(end_point, plt, ax)
    if is_point_within_object(start_point, center, radius):
        print("Start point is within circle, can't proceed")
        return
    if is_point_within_object(end_point, center, radius):
        print("End point is within circle, can't proceed")
        return

    while np.linalg.norm(start_point - end_point) > (alpha * h):
        start_point = walk(start_point, end_point, center, radius, h, alpha, plt, ax)
    print("complete")



start_vector = np.array((7,7,7))
end_vector = np.array((2,7,2))

circle_radius_value = 1
circle_center_value = (4,6.5,4)

run_robot(start_vector, end_vector, circle_center_value, circle_radius_value)

plt.show()

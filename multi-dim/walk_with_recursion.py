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
                # plt.plot(next_start[0], next_start[1], color='purple', marker='o', linestyle='dashed', linewidth=2,
                #          markersize=1)
                walk(next_start, end, circle_center, circle_radius, h, alpha, plt, axes)
    else:
        if np.linalg.norm(next_start - end) > (alpha * h):
            plot_point(next_start, plt, axes)
            # plt.plot(next_start[0], next_start[1], color='teal', marker='o', linestyle='dashed', linewidth=2,
            #          markersize=1)

            walk(next_start, end, circle_center, circle_radius, h, alpha, plt, axes)
        else:
            print("complete")


def run_robot(start_point, end_point, center, radius):
    fig = plt.figure()
    if len(start_point) == 2:
        ax = fig.add_subplot(111, aspect='equal')
    else:
        ax = fig.add_subplot(111, projection='3d')
    plot_circle_or_sphere(center, radius, start_point, end_point, plt, ax)
    s_color = "gold"
    e_color = "red"
    plot_point(start_point, plt, ax)
    plot_point(end_point, plt, ax)
    # plt.plot(start_point[0], start_point[1], color=s_color, marker='o', linestyle='dashed', linewidth=2, markersize=7)
    # plt.plot(end_point[0], end_point[1], color=e_color, marker='o', linestyle='dashed', linewidth=2, markersize=7)
    if is_point_within_object(start_point, center, radius):
        print("Start point is within circle, can't proceed")
        return
    if is_point_within_object(end_point, center, radius):
        print("End point is within circle, can't proceed")
        return

    walk(start_point, end_point, center, radius, h, alpha, plt, ax)


start_vector = np.array((4,7))
end_vector = np.array((4,2))

circle_radius_value = 1
circle_center_value = (4,4)
run_robot(start_vector, end_vector, circle_center_value, circle_radius_value)

plt.show()

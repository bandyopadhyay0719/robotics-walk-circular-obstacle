import matplotlib.pyplot as plt
import numpy as np
from intersect import intersecting
from intersect import is_point_within_circle
from calculations import normal
from calculations import normal_right
from calculations import line_through_circle_center


def walk(start, end, circle_center, circle_radius, h, alpha):
    vector = end - start
    walk_vector = alpha * h * (vector / np.linalg.norm(vector))

    next_start = start + walk_vector
    # if is_point_within_circle(next_start, circle_center, circle_radius) and intersecting(next_start, end, circle_center,
    #                                                                                      circle_radius) is not None:
    intersection = intersecting(start, end, circle_center, circle_radius)
    if is_point_within_circle(next_start, circle_center, circle_radius):
        if intersection is not None:


            # intersection = intersecting(next_start, end, circle_center, circle_radius)
            plt.plot(intersection[0], intersection[1], color='pink', marker='o', linestyle='dashed', linewidth=2,
                     markersize=1)

            normal_vector = normal(start, end, circle_center, circle_radius)
            if normal_vector is not None:
                next_start = start + h * alpha * normal_vector

                plt.plot(next_start[0], next_start[1], color='purple', marker='o', linestyle='dashed', linewidth=2,
                         markersize=1)
                walk(next_start, end, circle_center, circle_radius, h, alpha)
    else:
        if np.linalg.norm(next_start - end) > (alpha * h):
            plt.plot(next_start[0], next_start[1], color='teal', marker='o', linestyle='dashed', linewidth=2,
                     markersize=1)

            walk(next_start, end, circle_center, circle_radius, h, alpha)
        else:
            print("complete")


def walk_right(start, end, circle_center, circle_radius, h, alpha):
    vector = end - start
    walk_vector = alpha * (vector / np.linalg.norm(vector))

    next_start = start + h * walk_vector

    if is_point_within_circle(next_start, circle_center, circle_radius) and intersecting(next_start, end, circle_center,
                                                                                         circle_radius) is not None:

        if not line_through_circle_center(start, end, circle_center) and intersecting(next_start, end, circle_center,
                                                                                      circle_radius) is not None:
            intersection = intersecting(next_start, end, circle_center, circle_radius)
            # print(intersection)
            plt.plot(intersection[0], intersection[1], color='purple', marker='o', linestyle='dashed', linewidth=2,
                     markersize=1)

            normal_vector = normal_right(next_start, end, circle_center, circle_radius)
            # print(normal_vector)
            if normal_vector is not None:
                next_start = start + h * normal_vector

                # plt.plot(next_start[0], next_start[1], color='purple', marker='o', linestyle='dashed', linewidth=2,
                #          markersize=1)

            walk_right(next_start, end, circle_center, circle_radius, h, alpha)
        else:
            print("Error")

    else:
        if np.linalg.norm(next_start - end) > (alpha * h):
            plt.plot(next_start[0], next_start[1], color='teal', marker='o', linestyle='dashed', linewidth=2,
                     markersize=1)

            walk_right(next_start, end, circle_center, circle_radius, h, alpha)

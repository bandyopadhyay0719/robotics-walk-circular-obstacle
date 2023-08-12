import matplotlib.pyplot as plt
import numpy as np
from intersect import intersecting
from intersect import is_point_within_circle


def normal(start, end, circle_center, circle_radius):
    circle_vector = np.array(circle_center)

    intersection = intersecting(start, end, circle_center, circle_radius)
    # plt.plot(intersection[0], intersection[1], color='pink', marker='o', linestyle='dashed', linewidth=2,
    #          markersize=1)

    intersection_vector = np.array(intersection)

    # intersection_to_center = circle_vector - intersection_vector
    intersection_to_center = intersection_vector - circle_vector

    normal_vector = np.array([-intersection_to_center[1], intersection_to_center[0]])
    dot_product = dot(normal_vector, intersection_vector)
    print('dot_product', dot_product)

    if dot_product < 0:
        if not (start[0] >= end[0] or start[1] >= end[1]):
            normal_vector = np.array([intersection_to_center[1], -intersection_to_center[0]])
            print("2")
    else:
        if (start[0] >= end[0] or start[1] >= end[1]):
            normal_vector = np.array([intersection_to_center[1], -intersection_to_center[0]])
            print("1")

    # if start[0] > end[0]:
    #     normal_vector = np.array([normal_vector[0], -normal_vector[1]])
    # elif start[1] > end[1]:
    #     normal_vector = np.array([normal_vector[0], -normal_vector[1]])
    # elif start[0] == end[0]:
    #     normal_vector = np.array([-normal_vector[0], normal_vector[1]])

    vector_magnitude = np.linalg.norm(normal_vector)

    unit_vector = (normal_vector / vector_magnitude)

    return unit_vector


def normal_right(start, end, circle_center, circle_radius):
    # circle_vector = np.array(circle_center)
    #
    # intersection = intersecting(start, end, circle_center, circle_radius)
    # # plt.plot(intersection[0], intersection[1], color='pink', marker='o', linestyle='dashed', linewidth=2,
    # #          markersize=1)
    #
    # intersection_vector = np.array(intersection)
    # intersection_to_center = circle_vector - intersection_vector
    #
    # normal_vector = np.array([intersection_to_center[1], -intersection_to_center[0]])
    #
    # if(start[0]>end[0]):
    #
    #     normal_vector = np.array(normal_vector[0], -normal_vector[1])
    #
    # elif(start[1]>end[1]):
    #     normal_vector = np.array(normal_vector[0], -normal_vector[1])
    #
    # elif(start[0]==end[0]):
    #     normal_vector = normal_vector = np.array(-normal_vector[0], normal_vector[1])
    #
    #
    # normal_vector = .01 * normal_vector / np.linalg.norm(normal_vector)

    norm = normal(start, end, circle_center, circle_radius)
    print('norm ------', norm)
    normal_vector = np.array([-norm[0], -norm[1]])

    # plt.arrow(intersection[0], intersection[1], normal_vector[0], normal_vector[1], head_width=0.001, head_length=0.001, fc="green", ec='yellow')
    return normal_vector


def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def magnitudes(v1, v2):
    return np.linalg.norm(v1) * np.linalg.norm(v2)


# def right_or_left(start, end, circle_center, circle_radius):
#     circle_vector = np.array(circle_center)
#
#     intersection = intersecting(start, end, circle_center, circle_radius)
#     # plt.plot(intersection[0], intersection[1], color='pink', marker='o', linestyle='dashed', linewidth=2, markersize=1)
#
#     intersection_vector = np.array(intersection)
#     intersection_to_center = circle_vector - intersection_vector
#
#     normal_vector = np.array([-intersection_to_center[1], intersection_to_center[0]])
#
#     # normal_vector = .01 * normal_vector / np.linalg.norm(normal_vector)
#
#     if np.arccos(dot(normal_vector, intersection_vector)/np.linalg.norm(dot(normal_vector, intersection_vector))) > 0:
#         return True
#     return False


def line_through_circle_center(start, end, circle_center):
    through_center = False
    if (end[0] - start[0]) != 0:
        slope = (end[1] - start[1]) / (end[0] - start[0])
        intercept = start[1] - slope * start[0]
        if circle_center[1] == slope * circle_center[0] + intercept:
            through_center = True
    else:
        if start[0] == circle_center[0]:
            through_center = True

    return through_center

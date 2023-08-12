import matplotlib.pyplot as plt
import numpy as np
from intersect import intersecting
from execute import walk
from intersect import is_point_within_circle

start = np.array((2, 2))
end = np.array((7,7))

circle_radius = 1
circle_center = (4,4)










h = .1  # increment
alpha = .1  # step length


def run_robot(start_point, end_point, center, radius):
    draw_circle = plt.Circle(center, radius, color="darkorange")
    # Create a new plot and add the circle directly
    plt.gca().add_patch(draw_circle)
    s_color = "gold"
    e_color = "red"
    plt.plot(start_point[0], start_point[1], color=s_color, marker='o', linestyle='dashed', linewidth=2, markersize=7)
    plt.plot(end_point[0], end_point[1], color=e_color, marker='o', linestyle='dashed', linewidth=2, markersize=7)
    if is_point_within_circle(start_point, circle_center, circle_radius):
        print("Start point is within circle, can't proceed")
        return
    if is_point_within_circle(end_point, circle_center, circle_radius):
        print("End point is within circle, can't proceed")
        return


    walk(start_point, end_point, center, radius, h, alpha)
    # if line_through_circle_center(start_point, end_point, center):
    #     print("hi")
    #     walk(start_point, end_point, center, radius, h, alpha)
    # else:
    #     if intersecting(start_point, end_point, center, radius) is not None:
    #         intersection = intersecting(start_point, end_point, center, radius)
    #         if right_or_left(start_point, end_point, center, radius):
    #             walk(start_point, end_point, center, radius, h, alpha)
    #             print("Left")
    #         else:
    #             walk_right(start_point, end_point, center, radius, h, alpha)
    #             print("Right")
    #     else:
    #         walk(start_point, end_point, center, radius, h, alpha)
    #         print("No intersection")

    # plt.plot(start_point[0], start_point[1], color=s_color, marker='o', linestyle='dashed', linewidth=2, markersize=7)
    # plt.plot(end_point[0], end_point[1], color=e_color, marker='o', linestyle='dashed', linewidth=2, markersize=7)

    # draw_circle = plt.Circle(center, radius, color="darkorange")

    # Set the aspect ratio of the plot
    plt.gca().set_aspect("equal")

    if start_point[0] < end_point[0]:
        plt.xlim(start_point[0] - 1, end_point[0] + 1)
    else:
        plt.xlim(end_point[0] - 1, start_point[0] + 1)

    if start_point[1] < end_point[1]:
        plt.ylim(start_point[1] - 1, end_point[1] + 1)
    else:
        plt.ylim(end_point[1] - 1, start_point[1] + 1)


run_robot(start, end, circle_center, circle_radius)

plt.show()

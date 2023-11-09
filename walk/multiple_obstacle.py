import matplotlib.pyplot as plt
import numpy as np
from intersect import intersecting
from Circles import Circle
from intersect import distance
from intersect import is_point_within_circle
from calculations import normal
import random
from intersect import is_point_within_circle
import sys

Circle.circles = []

start = np.array((7,7))
end = np.array((1,1))

sys.setrecursionlimit(4000)

i = 0
while i< 10:
    if(start[0]>end[0]):
        xsmall_end = end[0]
        xbig_end = start[0]
    else:
        xsmall_end = start[0]
        xbig_end = end[0]

    if(start[1]>end[1]):
        ysmall_end = end[1]
        ybig_end = start[1]
    else:
        ysmall_end = start[1]
        ybig_end = end[1]

    x = random.randint(xsmall_end, xbig_end)
    y = random.randint(ysmall_end, ybig_end)
    r = random.uniform(.5,1.2)
    if i==0:
        Circle.circles.append(Circle((x,y), r))
        i+=1
    else:
        if not is_point_within_circle(start, (x,y), r) and not is_point_within_circle(end, (x,y), r):
            if not Circle.if_intersecting((x,y), r, Circle.circles):
                Circle.circles.append(Circle((x,y), r))
                i+=1

# for i in range(5):
#     x = random.randint(start[0], end[0])
#     y = random.randint(start[1], end[1])
#     r = random.uniform(.5,1.2)
#     if not Circle.if_intersecting((x,y), r, Circle.circles):
#         Circle.circles.append(Circle((x,y), r))


for c in Circle.circles:
    center = c.center
    print(center)
    radius = c.radius
    print(radius)

def next_intersection(start, end, circle_list):
    intersection = (200000000, 20000000000)
    circle = 0
    if intersection is not None:
        for i in range(len(circle_list)):
            c = circle_list[i]
            min_distance = distance(start, intersection)
            temp_intersection = intersecting(start, end, c.center, c.radius)
            if temp_intersection is not None:
                temp_distance = distance(start, temp_intersection)
                if(temp_distance<min_distance):
                    intersection=temp_intersection
                    circle = i
        return circle_list[circle]


def walk_multiple(start, end, circle_list, h, alpha):
    vector = end - start
    walk_vector = alpha * h * (vector / np.linalg.norm(vector))

    next_start = start + walk_vector
    # if is_point_within_circle(next_start, circle_center, circle_radius) and intersecting(next_start, end, circle_center,
    #                                                                                      circle_radius) is not None:
    if next_intersection(start, end, circle_list) is not None:
        circle = next_intersection(start, end, circle_list)
        circle_center = circle.center
        circle_radius = circle.radius

        intersection = intersecting(start, end, circle_center, circle_radius)
    else:
        intersection = None

    if intersection is not None and is_point_within_circle(next_start, circle_center, circle_radius):
        if intersection is not None:
            # intersection = intersecting(next_start, end, circle_center, circle_radius)
            plt.plot(intersection[0], intersection[1], color='pink', marker='o', linestyle='dashed', linewidth=2,
                     markersize=1)

            normal_vector = normal(start, end, circle_center, circle_radius)
            if normal_vector is not None:
                next_start = start + h * alpha * normal_vector

                plt.plot(next_start[0], next_start[1], color='purple', marker='o', linestyle='dashed', linewidth=2,
                         markersize=1)
                walk_multiple(next_start, end, circle_list, h, alpha)

    else:
        if np.linalg.norm(next_start - end) > (alpha * h):
            plt.plot(next_start[0], next_start[1], color='teal', marker='o', linestyle='dashed', linewidth=2,
                     markersize=1)

            walk_multiple(next_start, end, circle_list, h, alpha)
        else:
            print("complete")


h=.1
alpha = .1

def run_robot_multiple(start_point, end_point, circle_list):
    for circle in circle_list:
        center = circle.center
        radius = circle.radius
        draw_circle = plt.Circle(center, radius, color="darkorange")
        # Create a new plot and add the circle directly
        plt.gca().add_patch(draw_circle)
    s_color = "gold"
    e_color = "red"
    plt.plot(start_point[0], start_point[1], color=s_color, marker='o', linestyle='dashed', linewidth=2, markersize=7)
    plt.plot(end_point[0], end_point[1], color=e_color, marker='o', linestyle='dashed', linewidth=2, markersize=7)
    # if is_point_within_circle(start_point, circle_center, circle_radius):
    #     print("Start point is within circle, can't proceed")
    #     return
    # if is_point_within_circle(end_point, circle_center, circle_radius):
    #     print("End point is within circle, can't proceed")
    #     return


    walk_multiple(start_point, end_point, circle_list, h, alpha)
    plt.gca().set_aspect("equal")

    if start_point[0] < end_point[0]:
        plt.xlim(start_point[0] - 1, end_point[0] + 1)
    else:
        plt.xlim(end_point[0] - 1, start_point[0] + 1)

    if start_point[1] < end_point[1]:
        plt.ylim(start_point[1] - 1, end_point[1] + 1)
    else:
        plt.ylim(end_point[1] - 1, start_point[1] + 1)

run_robot_multiple(start, end, Circle.circles)


plt.show()
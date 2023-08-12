import numpy as np

import math


def intersecting(line_start, line_end, circle_center, circle_radius):
    # Calculate the direction vector of the line
    x2 = line_end[0]
    y2 = line_end[1]
    x1 = line_start[0]
    y1 = line_start[1]
    cx = circle_center[0]
    cy = circle_center[1]
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the coefficients for the quadratic equation
    a = dx**2 + dy**2
    b = 2 * (dx * (x1 - cx) + dy * (y1 - cy))
    c = cx**2 + cy**2 + x1**2 + y1**2 - 2 * (cx * x1 + cy * y1) - circle_radius**2

    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    if discriminant == 0:
        # One intersection point (line is tangent to the circle)
        t = -b / (2 * a)
        intersection_x = x1 + t * dx
        intersection_y = y1 + t * dy
        return [(intersection_x, intersection_y)]
    elif discriminant > 0:
        # Two intersection points
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)
        intersection1_x = x1 + t1 * dx
        intersection1_y = y1 + t1 * dy
        intersection2_x = x1 + t2 * dx
        intersection2_y = y1 + t2 * dy
        intersection_point_1 = (intersection1_x, intersection1_y)
        intersection_point_2 = (intersection2_x, intersection2_y)
        if distance(intersection_point_1, line_start) > distance(intersection_point_2, line_start):
            return intersection_point_2
        else:
            return intersection_point_1

def intersecting2(start_point, end_point, center, circle_radius):
    a = end_point[0] ** 2 + end_point[1] ** 2
    b = 2 * (end_point[0] * (start_point[0] - center[0]) + end_point[1] * (start_point[1] - center[1]))
    c = (start_point[0] - center[0]) ** 2 + (start_point[1] - center[1]) ** 2 - circle_radius ** 2

    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c



    if discriminant >= 0:



        #The vector intersects or is tangent to the circle
        t1 = (-b + np.sqrt(discriminant)) / (2 * a)
        t2 = (-b - np.sqrt(discriminant)) / (2 * a)

        intersection_point_1 = start_point + t1
        intersection_point_2 = start_point + t2
        if distance(intersection_point_1, start_point) > distance(intersection_point_2, start_point):
            return intersection_point_2
        else:
            return intersection_point_1


# def intersecting(start_point, end_point, center, circle_radius):
#     x1 = start_point[0]
#     y1 = start_point[1]
#     x2 = end_point[0]
#     y2 = end_point[1]
#     m = (y2 - y1)/(x2 - x1)
#     c = y1 - m * x1
#     a = -m
#     b = 1
#     x = center[0]
#     y = center[1]
#     dist = ((abs(a * x + b * y + c)) /
#             math.sqrt(a * a + b * b))

def is_point_within_circle(p, center, radius):
    x = p[0]
    y = p[1]

    if ((x - center[0]) ** 2 + (y - center[1]) ** 2) < radius ** 2:
        return True
    return False


def distance(v1, v2):
    x = v2[0] - v1[0]
    y = v2[1] - v1[1]
    return np.sqrt(x ** 2 + y ** 2)


"""
start_point = np.array((1,1))
end_point = np.array((7,7))

v = end_point-start_point

radius = 1
center = (2,2)

print(intersecting(start_point, end_point, center, radius))
print(is_point_within_circle((2,2), center, radius))
"""

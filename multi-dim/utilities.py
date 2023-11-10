import numpy as np
import math
from environment.non_overlapping_fixed_spheres import *
from environment.non_overlapping_fixed_circles import *
from walk.Circles import Circle
from environment.Spheres import Sphere

h = .1  # increment
alpha = .1  # step length


def create_environment(start_point, plt_in, axes):
    if len(start_point) == 2:
        create_circles(plt_in, axes)
    else:
        create_spheres(axes)


def is_start_in_object(start, object_list):
    for object in object_list:
        if is_point_within_object(start, object.center, object.radius):
            return True
    return False


def plot_circle_or_sphere(center, radius, start_point, end_point, plt, axes):
    if len(center) == 2:
        circle = plt.Circle(center, radius, fill=True, color='b')
        axes.add_patch(circle)
        if start_point[0] < end_point[0]:
            plt.xlim(start_point[0] - 5, end_point[0] + 5)
        else:
            plt.xlim(end_point[0] - 5, start_point[0] + 5)

        if start_point[1] < end_point[1]:
            plt.ylim(start_point[1] - 5, end_point[1] + 5)
        else:
            plt.ylim(end_point[1] - 5, start_point[1] + 5)

        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlabel('X')
        plt.ylabel('Y')

    elif len(center) == 3:
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
        y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
        z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
        axes.plot_surface(x, y, z, color='b')
        plt.xlabel('X')
        plt.ylabel('Y')
        axes.set_zlabel('Z')


def plot_point(point, plt, axes, color_of_point = "lightseagreen", point_size = 1):
    if len(point) == 2:
        plt.plot(point[0], point[1], color=color_of_point, marker='o', linestyle='dashed', linewidth=2,
                 markersize=point_size)

    elif len(point) == 3:
        axes.scatter(point[0], point[1], point[2], color=color_of_point, marker='*', linestyle='dashed', linewidth=2, s=point_size)


def intersection_points(start_point, end_point, center, radius):
    # Calculate direction vector of the line
    direction = end_point - start_point
    # Calculate coefficients for the quadratic equation
    a = np.dot(direction, direction)
    b = 2 * np.dot(direction, start_point - center)
    c = np.dot(start_point - center, start_point - center) - radius ** 2
    # Calculate discriminant
    discriminant = b ** 2 - 4 * a * c

    # Check if there are real solutions
    if discriminant >= 0:
        # Calculate t values for the intersections
        t1 = (-b + np.sqrt(discriminant)) / (2 * a)
        t2 = (-b - np.sqrt(discriminant)) / (2 * a)

        # Calculate intersection points
        intersection_point_1 = start_point + t1 * direction
        intersection_point_2 = start_point + t2 * direction
        return [intersection_point_1, intersection_point_2]
    else:
        return []


def is_point_within_object(in_point, in_center, in_radius):
    distance = math.sqrt(sum((p - c) ** 2 for p, c in zip(in_point, in_center)))
    return distance <= in_radius


def is_next_step_within_object(in_point, in_center, in_radius):
    next_step = in_point + find_unit_vector(in_point) * h * alpha
    distance = math.sqrt(sum((p - c) ** 2 for p, c in zip(next_step, in_center)))
    return distance <= in_radius


def distance_between_points(v1, v2):

    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensionality")
    squared_diff = sum((x - y) ** 2 for x, y in zip(v1, v2))

    return math.sqrt(squared_diff)


def first_intersection_point(intersections, start_point):
    if len(intersections) != 0:
        if distance_between_points(intersections[0], start_point) > distance_between_points(intersections[1],
                                                                                            start_point):
            return intersections[1]
        else:
            return intersections[0]


def find_normal_vector(start, end, circle_center, circle_radius):
    circle_vector = np.array(circle_center)

    intersections = intersection_points(start, end, circle_center, circle_radius)
    intersection = first_intersection_point(intersections, start)
    intersection_vector = np.array(intersection)

    intersection_to_center = intersection_vector - circle_vector
    normal_vector = calculate_normal_vector(intersection_to_center)
    direction_vector = end - start

    direct_normal_dot_product = dot_product(direction_vector, normal_vector)

    if direct_normal_dot_product < 0:
        normal_vector = opposite_direction(normal_vector)

    vector_magnitude = np.linalg.norm(normal_vector)

    unit_vector = (normal_vector / vector_magnitude)

    return unit_vector


def find_unit_vector(vector):
    vector_magnitude = np.linalg.norm(vector)
    unit_vector = (vector / vector_magnitude)
    return unit_vector


def opposite_direction(vector):
    return np.array([-component for component in vector])


def calculate_normal_vector(vector):
    if len(vector) == 2:
        a, b = vector
        normal_vector = [-b, a]
        return normal_vector
    elif len(vector) == 3:
        a, b, c = vector
        # Define a vector that is orthogonal to the input vector
        if a != 0 or b != 0:
            orthogonal_vector = [-b, a, 0]
        else:
            orthogonal_vector = [0, 0, 1]
        # Calculate the cross product to get the normal vector
        normal_vector = [b * orthogonal_vector[2] - c * orthogonal_vector[1],
                         c * orthogonal_vector[0] - a * orthogonal_vector[2],
                         a * orthogonal_vector[1] - b * orthogonal_vector[0]]

        return normal_vector


def is_reverse_direction(start_point, end_point):
    if len(start_point) == 3 and len(end_point) == 3:
        origin = np.zeros(3)
    else:
        origin = np.zeros(2)
    if distance_between_points(origin, start_point) > distance_between_points(origin, end_point):
        return True
    else:
        return False


def is_downward_vector(start_point, end_point):
    direction_vector = end_point - start_point
    return direction_vector[1] < 0


def is_forward_upward_vector(start, end):
    direction_vector = end - start
    if len(start) == 2 and len(end) == 2:
        return direction_vector[0] > 0 and direction_vector[1] > 0
    else:
        return direction_vector[0] > 0 and direction_vector[1] > 0 and direction_vector[2] > 0


def is_horizontal_vector(start, end):
    direction_vector = end - start
    return direction_vector[1] == 0


def is_vertical_vector(start, end):
    direction_vector = end - start
    return direction_vector[0] == 0


def is_moving_left(start_point, end_point):
    direction_vector = end_point - start_point
    return direction_vector[0] < 0


def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimensionality")

    return sum(x * y for x, y in zip(vector1, vector2))


# Example usage
original_vector = [1, 2, 3]

opposite_vector = opposite_direction(original_vector)
print(f"The vector of opposite direction to {original_vector} is: {opposite_vector}")

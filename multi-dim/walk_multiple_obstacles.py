from utilities import *


def next_intersection_object(start, end, object_list):
    next_intersection_point = None
    object_to_return = None
    for i in range(len(object_list)):

        object = object_list[i]

        intersections = intersection_points(start, end, object.center, object.radius)
        first_intersection = first_intersection_point(intersections, start)
        if next_intersection_point is None or (first_intersection is not None and
                                               (distance_between_points(start,
                                                                        next_intersection_point) > distance_between_points(
                                                   start,
                                                   first_intersection))):
            object_to_return = object
            next_intersection_point = first_intersection
    return object_to_return


def walk_multiple(start_point, end_point, object_list, h, alpha, axes):
    vector = end_point - start_point
    walk_vector = alpha * h * (vector / np.linalg.norm(vector))
    next_start = start_point + walk_vector

    object = next_intersection_object(start_point, end_point, object_list)
    object_center = object.center
    object_radius = object.radius

    intersections = intersection_points(start_point, end_point, object_center, object_radius)
    intersection = first_intersection_point(intersections, start_point)

    if is_next_step_within_object(next_start, object_center, object_radius):
        if is_point_within_object(end_point, object_center, object_radius):
            return end_point
        if intersection is not None:
            plot_point(intersection, plt, axes)
            normal_vector = find_normal_vector(start_point, end_point, object_center, object_radius)
            if normal_vector is not None:
                next_start = start_point + h * alpha * normal_vector
                plot_point(next_start, plt, axes)
    else:
        if np.linalg.norm(next_start - end_point) > (alpha * h):
            plot_point(next_start, plt, axes, "steelblue")
    return next_start


def run_robot(start_point, end_point):
    fig = plt.figure()
    if len(start_point) == 2:
        ax = fig.add_subplot(111, aspect='equal')
    else:
        ax = fig.add_subplot(111, projection='3d')

    create_environment(start_point, plt, ax)

    point_size = 10
    if len(start_point) == 2:
        if is_start_in_object(start_point, Circle.circles):
            start_point = end_point
    else:
        point_size = 100
        if is_start_in_object(start_point, Sphere.spheres):
            start_point = end_point

    plot_point(start_point, plt, ax, "green", point_size)
    plot_point(end_point, plt, ax, "red", point_size)

    while np.linalg.norm(start_point - end_point) > (alpha * h):
        if len(start_point) == 2:
            start_point = walk_multiple(start_point, end_point, Circle.circles, h, alpha, ax)
        else:
            start_point = walk_multiple(start_point, end_point, Sphere.spheres, h, alpha, ax)
    print("complete")


end_vector = np.array((1, 1, 1))
start_vector = np.array((6, 6, 6))

run_robot(start_vector, end_vector)

plt.show()

from Spheres import Sphere
import matplotlib.pyplot as plt
import numpy as np
import random

Sphere.spheres = []
start_point = np.array((-2, -2, -2))
end_point = np.array((30, 30, 30))


def is_point_in_sphere(p, center, sphere_radius):
    x = p[0]
    y = p[1]
    z = p[2]

    if ((x - center[0]) ** 2 + (y - center[1]) ** 2 + (z - center[2]) ** 2) < sphere_radius ** 2:
        return True
    return False


def create_spheres(start, end, min_radius, max_radius):
    i = 0
    if start[0] > end[0]:
        xsmall_end = end[0]
        xbig_end = start[0]
    else:
        xsmall_end = start[0]
        xbig_end = end[0]

    if start[1] > end[1]:
        ysmall_end = end[1]
        ybig_end = start[1]
    else:
        ysmall_end = start[1]
        ybig_end = end[1]

    if start[2] > end[2]:
        zsmall_end = end[2]
        zbig_end = start[2]
    else:
        zsmall_end = start[2]
        zbig_end = end[2]

    while i < 10:

        x = random.randint(xsmall_end, xbig_end)
        y = random.randint(ysmall_end, ybig_end)
        z = random.randint(zsmall_end, zbig_end)
        r = random.uniform(min_radius, max_radius)

        if i == 0:
            Sphere.spheres.append(Sphere((x, y, z), r))
            i += 1
        else:
            if not is_point_in_sphere(start, (x, y, z), r + 0.2) and not is_point_in_sphere(end, (x, y, z), r):
                if not Sphere.if_intersecting((x, y, z), r + 0.2, Sphere.spheres):
                    Sphere.spheres.append(Sphere((x, y, z), r))
                    i += 1
                    print(x)
                    print(y)
                    print(z)
                    print(r)

    return Sphere.spheres


def draw_spheres(spheres, r):
    fig = plt.figure()
    axes = fig.add_subplot(111, projection='3d')
    for sphere in spheres_list:
        center = sphere.center

        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = center[0] + r * np.outer(np.cos(u), np.sin(v))
        y = center[1] + r * np.outer(np.sin(u), np.sin(v))
        z = center[2] + r * np.outer(np.ones(np.size(u)), np.cos(v))
        axes.plot_surface(x, y, z, color='b')
        plt.xlabel('X')
        plt.ylabel('Y')
        axes.set_zlabel('Z')


def find_largest_radius(spheres):
    largest_radius = 0
    for sphere in spheres:
        if sphere.radius > largest_radius:
            largest_radius = sphere.radius
    return largest_radius


spheres_list = create_spheres(start_point, end_point, 1, 10)
radius = find_largest_radius(spheres_list)

draw_spheres(spheres_list, radius)

dimensions(start, end, radius)

plt.show()

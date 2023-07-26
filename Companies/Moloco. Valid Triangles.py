import math
import itertools


def dist(point1, point2):
    # calculate Euclidean distance
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def count_triangles(vertices):
    # Step 1
    # compute all pairwise distances
    distances = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            distances.append((i, j, dist(vertices[i], vertices[j])))

    # sort distances by the third element in the tuple (i.e., the distance)
    distances.sort(key=lambda x: x[2])
    print(distances)
    # Step 2
    # for each point, compute the number of triangles that can be formed with it
    num_triangles = 0
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            for k in range(j + 1, len(vertices)):
                # check if these three points can form a triangle
                print(i, j, k, distances[i], distances[j], distances[k])
                if distances[i][2] + distances[j][2] > distances[k][2]:
                    num_triangles += 1
    return num_triangles

def count_triangles2(vertices):
    # Step 1
    # compute all pairwise distances
    # distances = []
    # for i in range(len(vertices)):
    #     for j in range(i + 1, len(vertices)):
    #         distances.append((i, j, dist(vertices[i], vertices[j])))
    #
    # # sort distances by the third element in the tuple (i.e., the distance)
    # distances.sort(key=lambda x: x[2])
    # print(distances)
    # # Step 2
    # # for each point, compute the number of triangles that can be formed with it
    num_triangles = 0
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            for k in range(j + 1, len(vertices)):
                # check if these three points can form a triangle
                dists = [dist(vertices[i], vertices[j]) , dist(vertices[i], vertices[k]) , dist(vertices[j], vertices[k])]
                if sum(dists) - max(dists) > max(dists):
                    num_triangles += 1

    return num_triangles

# vertices = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5)]
vertices = [(0, 0), (1, 0), (0, 1), (1, 0)]
print(count_triangles2(vertices))  # prints 10
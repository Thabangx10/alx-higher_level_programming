#!/usr/bin/python3
"""Pascal Triangle function
"""

def pascal_triangle(n):
    """Return:
             a list of intefers(size n) that represent a triangle
    """

    if n<= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i +1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles

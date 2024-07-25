#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal tri of n
    """
    tri = []
    if n <= 0:
        return tri
    tri = [[1]]
    for k in range(1, n):
        row = [1]
        for j in range(1, len(tri[k - 1])):
            row.append(tri[k - 1][j - 1] + tri[k - 1][j])
        row.append(1)
        tri.append(row)
    return tri
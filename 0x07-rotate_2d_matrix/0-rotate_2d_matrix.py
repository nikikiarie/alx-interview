#!/usr/bin/python3
"""Module to rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix """
    a = len(matrix)

    for x in range(a):
        for z in range(x, a):
            matrix[x][z], matrix[z][x] = matrix[z][x], matrix[x][z]

    for r in matrix:
        r.reverse()


def print_matrix(matrix):
    """print function for 2D matrix."""
    for r in matrix:
        print(r)
    print()


def build_matrix(a):
    """Create an n x n matrix"""
    matrix = []
    cnt = 1
    for _ in range(a):
        r = [cnt + x for x in range(a)]
        matrix.append(r)
        cnt += a
    return matrix

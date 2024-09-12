#!/usr/bin/python3
"""Module to rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()


def print_matrix(matrix):
    """print function for 2D matrix."""
    for row in matrix:
        print(row)
    print()


def build_matrix(n):
    """Create an n x n matrix"""
    matrix = []
    count = 1
    for _ in range(n):
        row = [count + i for i in range(n)]
        matrix.append(row)
        count += n
    return matrix

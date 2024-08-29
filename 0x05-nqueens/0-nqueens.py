#!/usr/bin/python3
""" Nqueens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be y number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

num = int(sys.argv[1])


def queens(num, z=0, y=[], v=[], c=[]):
    """ find likely positions """
    if z < num:
        for x in range(num):
            if x not in y and z + x not in v and z - x not in c:
                yield from queens(num, z + 1, y + [x], v + [z + x], c + [z - x])
    else:
        yield y


def find(num):
    """
    find
    """
    e = []
    z = 0
    for m in queens(num, 0):
        for g in m:
            e.append([z, g])
            z += 1
        print(e)
        e = []
        z = 0


find(num)
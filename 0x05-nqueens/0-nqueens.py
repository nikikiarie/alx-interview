#!/usr/bin/python3
"""
Nqueens problem
"""
import sys


def backtrack(e, ag, columns, positive, negative, cord):
    """
    function to get solution
    """
    if e == ag:
        arr = []
        for a in range(len(cord)):
            for b in range(len(cord[a])):
                if cord[a][b] == 1:
                    arr.append([a, b])
        print(arr)
        return

    for j in range(ag):
        if j in columns or (e + j) in positive or (e - j) in negative:
            continue

        columns.add(j)
        positive.add(e + j)
        negative.add(e - j)
        cord[e][j] = 1

        backtrack(e+1, ag, columns, positive, negative, cord)

        columns.remove(j)
        positive.remove(e + j)
        negative.remove(e - j)
        cord[e][j] = 0


def nqueens(ag):
    """
    Nqueens problem
    Args:
        ag (int): queens number
    Return:
        List each queen for all
        possible solutions
    """
    columns = set()
    pos_diag = set()
    neg_diag = set()
    cord = [[0] * ag for i in range(ag)]

    backtrack(0, ag, columns, pos_diag, neg_diag, cord)


if __name__ == "__main__":
    ag = sys.argv
    if len(ag) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        o = int(ag[1])
        if o < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(o)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
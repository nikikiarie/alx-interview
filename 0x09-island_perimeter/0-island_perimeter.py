#!/usr/bin/python3
"""Island perimeter module.
"""


def island_perimeter(grid):
    """perimeter of an island with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    z = len(grid)
    for a, r in enumerate(grid):
        y = len(r)
        for b, unit in enumerate(r):
            if unit == 0:
                continue
            linits = (
                a == 0 or (len(grid[a - 1]) > b and grid[a - 1][b] == 0),
                b == y - 1 or (y > b + 1 and r[b + 1] == 0),
                a == z - 1 or (len(grid[a + 1]) > b and grid[a + 1][b] == 0),
                b == 0 or r[b - 1] == 0,
            )
            perimeter += sum(linits)
    return perimeter

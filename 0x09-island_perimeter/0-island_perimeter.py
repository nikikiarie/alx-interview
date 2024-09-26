def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row_index in range(rows):
        for col_index in range(cols):
            if grid[row_index][col_index] == 1:
                perimeter += 4
                if row_index > 0 and grid[row_index - 1][col_index] == 1:
                    perimeter -= 2
                if col_index > 0 and grid[row_index][col_index - 1] == 1:
                    perimeter -= 2

    return perimeter

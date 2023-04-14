# pylint: disable=missing-docstring
# Optional challenge from leWagon
# updated README explanes the function

def sudoku_solver(grid):
    """Sudoku solver"""
    # 1. Check input grid correctness
    if not isinstance(grid, list) or len(grid) < 9:
        return "invalid grid"
    for line in grid:
        if len(line) < 9:
            return "invalid grid"

    # 2. Solve iterating tentative solutions in empty slots
    slot = find_empty(grid)
    if not slot:
        return grid
    row, col = slot
    for i in range(1,10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if sudoku_solver(grid):
                return grid

            grid[row][col] = 0
    return False

def find_empty(grid):
    for i, val in enumerate(grid):
        for j in range(len(grid[0])):
            if val[j] == 0:
                return (i, j)  # row, col
    return None

def valid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i, val in enumerate(grid):
        if val[pos[1]] == num and pos[0] != i:
            return False
    # Check box (organize grid in 9 blocks and check inside)
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False
    return True

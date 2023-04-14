This **Sudoku Solver** goal is simple: given a Sudoku **9x9 grid**, with a few numbers in the grid, find the missing numbers to create a valid grid!

![](https://i.ibb.co/nDj9RFk/largeprintsudoku.jpg)

## Function

The function `sudoku_solver(grid)` takes a sudoku grid represented by a Python list of lists as an argument and returns a grid filled with the right digits.

## Data Model

**Input** type :

```python
grid = [
    [7,0,0,  0,0,9,  0,0,0],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  4,0,0],
    [0,5,0,  0,4,6,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,6,  0,0,0,  0,0,5],
    [2,0,0,  5,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,3,0]
]
```

The **zeros** represent empty slots that need to be filled with the correct numbers.

The **output** grid returned by your function should also be represented as a Python list of list:

```python
grid_solution = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]
```

## Trivia

The function uses a simple backtracking strategy
<br>
[📚[Documentation] Backtracking](https://en.wikipedia.org/wiki/Backtracking)

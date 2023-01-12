import time

start_time = time.time()

def empty_space(sudoku):
  for r in range(9):
    for c in range(9):
      if sudoku[r][c] == -1: 
        return r,c
  
  return None, None 


def guess_valid(sudoku, guess, row, col):

  row_val = sudoku[row] 
  if guess in row_val:
    return False

  col_val = [sudoku[i][col] for i in range(9)] 
  if guess in col_val:
    return False 

  row_start = (row // 3) *3
  col_start = (col // 3) *3

  for r in range(row_start, row_start+3):
    for c in range(col_start, col_start+3):
      if sudoku[r][c] == guess:
        return False

  return True


def puzzle_solver(sudoku):
    row, col = empty_space(sudoku)
    if row is None:
        return True

    possibilities = [i for i in range(1,10) if guess_valid(sudoku, i, row, col)]
    for guess in possibilities:
        sudoku[row][col] = guess
        if puzzle_solver(sudoku):
            return True
    sudoku[row][col] = -1 
    return False



grid = [
  [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
  [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
  [-1, -1, -1,  7, 1, 9,  -1, 8, -1,],

  [-1, 5, -1,  -1, 6, 8,  -1, -1, -1,],
  [2, -1, 6,  -1, -1, 3,  -1, -1, -1,],
  [-1, -1, -1,  -1, -1, -1,  -1, -1, 4,],

  [5, -1, -1,  -1, -1, -1,  -1, -1, -1,],
  [6, 7, -1,  1, -1, 5,  -1, 4, -1,],
  [1, -1, 9,  -1, -1, -1,  2, -1, -1,]
]

print(puzzle_solver(grid))

for row in grid:
    for val in row:
        print(f"{val:3}", end="")
    print()

end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed: ", elapsed_time)
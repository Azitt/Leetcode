## N-Queens######################
def is_valid_move(proposed_row, proposed_col, solution):
    for i in range(0, proposed_row):
        old_row = i
        old_col = solution[i]
        diagonal_offset = proposed_row - old_row
        if (old_col == proposed_col or
            old_col == proposed_col - diagonal_offset or
                old_col == proposed_col + diagonal_offset):
            return False
            
    return True

# Recursive worker function
def solve_n_queens_rec(n, solution, row, results):
    if row == n:
        results.append(solution[:])
        return

    for i in range(0, n):
        valid = is_valid_move(row, i, solution)
        if valid:
            solution[row] = i
            solve_n_queens_rec(n, solution, row + 1, results)

# Function to solve N-Queens problem
def solve_n_queens(n):
    results = []
    solution = [-1] * n
    solve_n_queens_rec(n, solution, 0, results)
    return len(results)

n = 4
print(solve_n_queens(n))

## word search#########################
def dfs(row,col,word,index,grid):
   if len(word) == index:
        return True 
   if row < 0 or row >= len(grid) or col <0 or col >= len(grid[0]) or grid[row][col] != word[index]:
       return False 
   tmp = grid[row][col]
   grid[row][col] = '*' 
   for r_offset, c_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
       if dfs(row+r_offset,col+c_offset,word,index+1,grid):
           return True
       
   grid[row][col] = tmp
   return False
   
def word_search(grid,word):
    row = len(grid)
    col = len(grid[0])
    for r in range(row):
        for c in range(col):
           if dfs(r,c,word,0,grid):
               return True
    return False       
                    

grid = [["N","W","L","I","M"],["V","I","L","Q","O"],["O","L","A","T","O"],["R","T","A","I","N"],["O","I","T","N","C"]] 
word = "LATIN" 
print(word_search(grid,word))          
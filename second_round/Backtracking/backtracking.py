## N-Queens############################################
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

## word search#######################################
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

### House Robber III#################################
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
from BinaryTree import *

def rob(root):
   return max(heist(root))

def heist(root):
    if root == None: 
        return [0, 0]
    
    left_subtree = heist(root.left) 
    right_subtree  = heist(root.right)
    include_root = root.data + left_subtree[1] + right_subtree[1] 
    exclude_root = max(left_subtree) + max(right_subtree)
 

    return [include_root, exclude_root]

houses = [9,7,11,1,8,10,12]  
houses_tree = [TreeNode(9),TreeNode(7),TreeNode(11),TreeNode(1),TreeNode(8),TreeNode(10),TreeNode(12)] 
tree = BinaryTree(houses_tree)
rob(tree.root)
## Restore IP Addresses#################################
def valid(segment):
    segment_length = len(segment)
    if segment_length > 3:
        return False

    return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

# this function will append the current list of segments to the list of results.
def update_segment(s, curr_dot, segments, result):
    segment = s[curr_dot + 1:len(s)]

    if valid(segment): 
        segments.append(segment)
        result.append('.'.join(segments))
        segments.pop() 

def backtrack(s, prev_dot, dots, segments, result):

    size = len(s)

    for curr_dot in range(prev_dot + 1, min(size - 1, prev_dot + 4)):
        segment = s[prev_dot + 1:curr_dot + 1]
        if valid(segment):
            segments.append(segment)

            if dots - 1 == 0:
                update_segment(s, curr_dot, segments, result)
            else:
                backtrack(s, curr_dot, dots - 1, segments, result)

            segments.pop()

def restore_ip_addresses(s):

    result, segments = [], []
    backtrack(s, -1, 3, segments, result)
    return result  

s= "010010"
print(restore_ip_addresses(s))
s= "25525511135"
print(restore_ip_addresses(s))

##Flood Fill#######################################################################

def flood_fill_rec(grid, sr, sc, target,value):
    
    if sr < 0 or sr>= len(grid) or sc < 0 or sc >= len(grid[0]) or grid[sr][sc] !=value:
        return 
    grid[sr][sc] = target
    for roffset,coloffset in [(0,1),(1,0),(0,-1),(-1,0)]:
        flood_fill_rec(grid, sr + roffset, sc + coloffset, target,value)
        
def flood_fill(grid, sr, sc, target):
    
    if grid[sr][sc]==target:
        return grid
    value = grid[sr][sc]
    flood_fill_rec(grid, sr, sc, target,value)
    return grid

grid = [[1,1,0,1,0],[0,0,0,0,1],[0,0,0,1,1],[1,1,1,1,0],[1,0,0,0,0]]
sr,sc,target = 4,3,3 
print(flood_fill(grid, sr, sc, target))

## Sudoku Solver#####################################################
def is_valid(row,col,board,digit):
    for i in range(9):
        if board[row][i]==digit or board[i][col]==digit:
          return False
    startrow = row - row%3
    startcol = col - col%3
    for i in range(3):
        for j in range(3):
            if board[i+startrow][j+startcol] == digit:
                return False
    return True        
def solve_sudoku(board):
    row = len(board)
    column = len(board[0])
    
    for i in range(row):
        for j in range(column):
            if board[i][j] == ".":
             for digit in "123456789":
                if is_valid(i,j,board,digit): ## we check if we can put the digit at location i,j in the board###############
                    board[i][j] = digit 
                    if solve_sudoku(board): ## we call board one more time because for example if we put board[0][0] = 1 now we have a new board we need to check form i = 0, j = 0 which number we can put
                        return board
                    board[i][j] = "."
             return None
    return board    

board = [[".",".",".",".",".",".",".","7","."],["2","7","5",".",".",".","3","1","4"],[".",".",".",".","2","7",".","5","."],["9","8",".",".",".",".",".","3","1"],[".","3","1","8",".","4",".",".","."],[".",".",".","1",".",".","8",".","5"],["7",".","6","2",".",".","1","8","."],[".","9",".","7",".",".",".",".","."],["4","1",".",".",".","5",".",".","7"]]            
print(solve_sudoku(board)) 

## Matchsticks########################################################
def matchstick_rec(four_side_length,match_sort,target_slength,index_matches,index_slength):
    if index_matches==(len(match_sort)):
        return all(side==target_slength for side in four_side_length)
    for i in range(4):
     if (four_side_length[i] + match_sort[index_matches])<= target_slength:
         four_side_length[i] += match_sort[index_matches]
         if matchstick_rec(four_side_length,match_sort,target_slength,index_matches+1,i):
             return True
         four_side_length[i] -= match_sort[index_matches]
    return False   
                  
         
def matchstick_to_square(matchsticks):
 if len(matchsticks) < 4 or sum(matchsticks)%4 !=0:
     return False
 match_sort = sorted(matchsticks)
 target_slength = sum(matchsticks)//4
 for s in match_sort:
     if s > target_slength:
         return False
 four_side_length = [0,0,0,0]
 return matchstick_rec(four_side_length,match_sort,target_slength,0,0)       
    
matchsticks = [1,1,2,2,2]
print(matchstick_to_square(matchsticks))

               
               
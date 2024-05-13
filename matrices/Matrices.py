## Set Matrix Zeros #########################
def matrices(mat):
    n = len(mat)
    m = len(mat[0])
    fcol = False  # when we found 0 at first column we don't make the column zero because we wanna check the value from other row at the same column first
    frow = False  # the same rule here
    for j in range(m):
        if mat[0][j] == 0:
            frow = True
            
    for i in range(n):
        if mat[i][0] == 0:
            fcol = True
  
    for i in range(1,n):
        for j in range(1,m):
            if mat[i][j] == 0:
                mat[0][j],mat[i][0] = 0,0
    # after we check all elements and make the first column and row of the element == 0 0 we check the rest of row and columns            
    for i in range(1,n):
        if mat[i][0] == 0:
            for j in range(1,m):
                mat[i][j] =0
    for j in range(1,m):
        if mat[0][j] == 0:
            for i in range(1,n):
                mat[i][j] = 0
    if fcol:
        for i in range(n):
            mat[i][0] = 0
    if frow:
        for j in range(m):
            mat[0][j] = 0        
                                               
               
    return mat        

mat= [[1,2,3],[4,5,6],[7,0,9]] 
print(matrices(mat))

###Rotate image ###########################################
def rotate_image(matrix):
    n = len(matrix)
    for row in range(n // 2):
        for col in range(row, n - row - 1):
            matrix[row][col], matrix[col][n - 1 - row] = matrix[col][n - 1 - row], matrix[row][col]
            matrix[row][col], matrix[n - 1 - row][n - 1 - col] = matrix[n - 1 - row][n - 1 - col], matrix[row][col]
            matrix[row][col], matrix[n - 1 - col][row] = matrix[n - 1 - col][row], matrix[row][col] 
    return matrix

mat= [[1,2,3],[4,5,6],[7,0,9]]    
print(rotate_image(mat))

## Spiral Matrix#############################################
def Spiral_Matrix(mat):
    direction = 1
    result = []
    row,col = 0,-1
    n = len(mat)
    m = len(mat[0])
    while m > 0 and n> 0:
     for _ in range(m):
        col += direction
        result.append(mat[row][col])
     n -=1    
     for _ in range(n):
        row += direction
        result.append(mat[row][col]) 
     m -= 1    
     direction *= -1
    
    return result 
mat = [[3,1,1],[15,12,13],[4,14,12],[10,5,11]]
print(Spiral_Matrix(mat)) 

## Where Will the Ball Fall ################
def find_exit_column(grid):
    result = [-1]*len(grid[0])
    
    for col in range(len(grid[0])):
        current_col = col
        for row in range(len(grid)):
            next_col = current_col + grid[row][current_col]
            
            if next_col < 0 or next_col > len(grid[0]) - 1 or grid[row][current_col] != grid[row][next_col]:
                break
            if row== len(grid) - 1:
                result[col]=next_col
            next_col = current_col
    return result 
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]] 
print(find_exit_column(grid))          
          
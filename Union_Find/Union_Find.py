## Redundant Connection ############################
from union_findclass import *
def Redundant_Connection(edges):
    graph = UnionFind(len(edges))
    for e0, e1 in edges:
        if not graph.union(e0,e1):
            return [e0,e1]
edges = [[1, 2], [1, 3], [2, 3]] 
print(Redundant_Connection(edges))       

## Number of Islands ################################
from union_findclass_grid import *
def num_islands(grid):
    union_find = UnionFind_grid(grid)
    rows,cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                grid[r][c] = '0'

                if r - 1 >= 0 and grid[r - 1][c] == '1':
                    union_find.union(r * cols + c, (r - 1) * cols + c)
                if r + 1 < rows and grid[r + 1][c] == '1':
                    union_find.union(r * cols + c, (r + 1) * cols + c)
                if c - 1 >= 0 and grid[r][c - 1] == '1':
                    union_find.union(r * cols + c, r * cols + c - 1)
                if c + 1 < cols and grid[r][c + 1] == '1':
                    union_find.union(r * cols + c, r * cols + c + 1)
                       
    count = union_find.get_count()                       
    return count                         

grid = [["1","1","1"],["0","1","0"],["1","0","0"],["1","0","1"]] 
print(num_islands(grid))  

## Most Stones Removed with Same Row or Column ################
## Maximum stones that can be removed=total stones−number of groups ###########cd ..

import collections
from collections import defaultdict
from union_findclass_stone import *


def remove_stones(stones):
    offset = 100
    stone = UnionFind()

    for x, y in stones:
        stone.union(x, (y + offset))  
    print(stone.parents)
    groups = set()
    for i in stone.parents:
        a = stone.find(i)
        print(a)
        groups.add(a)
    print(groups)
    return len(stones) - len(groups)   

stones = [[0, 1], [0, 3], [1, 2], [2, 3]]
print(remove_stones(stones))

## Longest Consecutive Sequence ################
from union_findclass_Longestc import UnionFind

def longest_consecutive_sequence(nums):
    union_find = UnionFind(nums) 
    for num in nums:
        if  num + 1 in union_find.parent:
            union_find.union(num,num+1)  
    return union_find.max_length

nums = [99,2,1,3,5]
print(longest_consecutive_sequence(nums)) 
        
## Last Day Where You Can Still Cross ################
from union_findclass_lastday import UnionFind

def last_day_to_cross(rows, cols, water_cells):
    
    day = 0
    matrix = [[0  for _ in range(cols)] for _ in range(rows)]
    left_node, right_node = 0, rows*cols + 1
    water_directions = [(0,-1),(-1,0),(0,1),(1,0),(-1,1),(-1,-1),(1,-1),(1,1)]
    # convert the water_cells from array start from index 1 to array starts from index 0 for the convenience
    water_cells = [(r-1,c-1) for r,c in water_cells]
    uf=union_find=UnionFind(rows*cols + 2)
    
    for row , col in water_cells:
        matrix[row][col] = 1
        for dr,dc in water_directions:
            if 0<=(row+dr) < rows and 0<=(col+dc)<cols and matrix[row+dr][col+dc]==1:
             uf.union(find_index(row,col,cols),find_index(row+dr,col+dc,cols))
            
        if col == 0:
            uf.union(find_index(row,col,cols),left_node)
        if col == cols - 1:
            uf.union(find_index(row,col,cols),right_node)  
        if uf.find_parent(left_node) == uf.find_parent(right_node):
            break
        day += 1
    return day           

def find_index(curr_row,curr_col,cols):
    return curr_row*cols + (curr_col + 1)

water_cells = [[3,2],[1,1],[1,2],[3,3],[2,3],[1,3],[2,1],[2,2],[3,1]] 
rows,cols =3,3
print(last_day_to_cross(rows, cols, water_cells))  

## Regions Cut by Slashes #####################
from union_findclass__RegCut import UnionFind 

def regions_by_slashes(grid):
    N = len(grid)
    find_union = UnionFind(4 * N * N)

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            root = 4 * (r * N + c)

            if val in '/ ':
                find_union.union(root + 0, root + 1)
                find_union.union(root + 2, root + 3)

            if val in '\\ ':
                find_union.union(root + 0, root + 2)
                find_union.union(root + 1, root + 3)

            if r + 1 < N:
                find_union.union(root + 3, (root + 4 * N) + 0)

            if r - 1 >= 0:
                find_union.union(root + 0, (root - 4 * N) + 3)
            
            if c + 1 < N:
                find_union.union(root + 2, (root + 4) + 1)

            if c - 1 >= 0:
                find_union.union(root + 1, (root - 4) + 2)

    return sum(find_union.find(x) == x for x in range(4 * N * N)) 
                    

grid = ["/\\\\","\\\\/"]
print(regions_by_slashes(grid))                     
                        
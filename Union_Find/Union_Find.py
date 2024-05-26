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
    
class UnionFind_grid():
    def __init__(self,grid):
        self.parent = []
        self.rank = rank=[]
        self.count = 0
        n = len(grid[0])
        for i in range(len(grid)):
         for j in range(n):
            if grid[i][j] == '1':
                self.count += 1
                self.parent.append(i * n + j)
            else:
                self.parent.append(-1)    
            self.rank.append(1)
            
    def find_parent(self,v):
        if self.parent[v] != v:
            return self.find_parent(self.parent[v]) 
        return self.parent[v] 
          
    def union_norank(self,v1,v2):        
        p1,p2 = self.find_parent(v1), self.find_parent(v2)
        
        # If both parents are the same, a cycle exists and v1,v2 is the redundant edge
        if p1==p2:
            return False
        else:
            self.parent[p1] = p2
        return True  
    
    def union(self,v1,v2):        
        p1,p2 = self.find_parent(v1), self.find_parent(v2)
        
        # If both parents are the same, a cycle exists and v1,v2 is the redundant edge
        if p1 != p2:
            
         if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
         elif self.rank[p1] < self.rank[p2]:
             self.parent[p1] = p2
         else:
            self.parent[p2] = p1
            self.rank[p1] += 1   
         self.count -= 1  
         
    def get_count(self):
        return self.count       
        
        
        
                
class UnionFind():
    def __init__(self,n):
        self.parent = []
        self.rank = rank=[1]*(n+1)
        for i in range(n+1):
            self.parent.append(i)
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
        if p1==p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]    
        return True    
        
        
        
                
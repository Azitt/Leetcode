class UnionFind():
    def __init__(self,n):
        self.parent = []
        for i in range(n):
            self.parent.append(i)
            
    def find_parent(self,v):
        if self.parent[v] != v:
            return self.find_parent(self.parent[v]) 
        return self.parent[v] 
          
    def union(self,v1,v2):        
        p1,p2 = self.find_parent(v1), self.find_parent(v2)     
        self.parent[p1] = p2
         
    
    
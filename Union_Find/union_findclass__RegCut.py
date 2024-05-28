class UnionFind():
    def __init__(self,n):
        self.parent = list(range(n))#[0] * n
        self.rank = [1] * n
        # for i in range(n):
        #     self.parent[i] = i
    
    def find(self,v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]          
     
    def union(self,v1,v2):        
        p1,p2 = self.find(v1), self.find(v2)
               
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]    
 
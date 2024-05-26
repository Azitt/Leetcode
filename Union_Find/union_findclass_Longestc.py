class UnionFind:
    # Constructor
    def __init__(self,nums):
        self.parent = {num:num for num in nums}
        self.size = {num:1 for num in nums}
        self.max_length = 1
         
        
    # Function to find which group a particular element belongs.
    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]

    # Function to join two coordinates into a single one.
    def union(self, num1,num2):
        num1_root = self.find(num1)
        num2_root = self.find(num2)
        if num1_root != num2_root:
         if self.size[num1_root] < self.size[num2_root]:
             num1_root,num2_root = num2_root, num1_root
         self.parent[num2_root] = num1_root
         self.size[num1_root] += self.size[num2_root]
         self.max_length = max(self.max_length,self.size[num1_root])
         
        
        
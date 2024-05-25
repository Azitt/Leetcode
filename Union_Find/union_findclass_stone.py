class UnionFind:
    # Constructor
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        
    # Function to find which group a particular element belongs.
    def find(self, coordinate):
        if coordinate != self.parents[coordinate]:
            self.parents[coordinate] = self.find(self.parents[coordinate])
        return self.parents[coordinate]

    # Function to join two coordinates into a single one.
    def union(self, x, y):
        # Set the parent of each node to itself 
        # if not already present in the dictionary

        self.parents.setdefault(x, x)
        self.parents.setdefault(y, y)

        # Set the ranks of each node to 0 
        # if not already present in the dictionary
        self.ranks.setdefault(x, 0)
        self.ranks.setdefault(y, 0)

        # Compare the ranks of the two nodes 
        # to decide which should be the parent

        if self.ranks[x] > self.ranks[y]:
            self.parents[self.find(y)] = self.find(x)
        elif self.ranks[y] > self.ranks[x]:
            self.parents[self.find(x)] = self.find(y)
        
         # If the rankss are equal, choose one node 
         # as the parent and increment its ranks
        else:
            self.parents[self.find(x)] = self.find(y)
            self.ranks[y] += 1
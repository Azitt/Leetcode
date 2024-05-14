## Network Delay Time ############################
from queue import PriorityQueue
from collections import defaultdict

def network_delay_time(times, n, k):
    adjacencydict = defaultdict(list)
    visited = set()
    pq = PriorityQueue()
    for node in times:
        adjacencydict[node[0]].append((node[1],node[2]))
    # pq save the delay time of each node to k node, we put 0 for delay time of node k itself 
    pq.put((0,k))
    delay = 0  # To store the delay time
    while not pq.empty():
        time,node = pq.get()
        
        if node in visited:
            continue
        
        delay = max(delay,time)
        visited.add(node)
        for neighbour in adjacencydict[node]:
            n_node, n_time = neighbour
            if n_node not in visited:
                new_time = time + n_time
                pq.put((new_time,n_node))
    if len(visited)==n:
        return delay
    return -1        
                

times, n, k = [[1,2,5],[1,3,10],[1,4,15]], 4,1  
print(network_delay_time(times, n, k))

## Paths in Maze That Lead to Same Room ############################### 
from collections import defaultdict

def number_of_paths(n, corridors):
    adjacentrymat = defaultdict(set)
    counter = 0
    for room1, room2 in corridors:
        adjacentrymat[room1].add(room2)
        adjacentrymat[room2].add(room1)
        print(adjacentrymat)
        counter += len(adjacentrymat[room1].intersection(adjacentrymat[room2]))
        print(counter,room1,room2)
    return counter    
        

n, corridors = 5, [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]
print(number_of_paths(n, corridors))  

## clone graph ##########################################################
# how to create a new copy of graph without affecting the original one
from graph_utility import *
class Node:
  def __init__(self, d):
    self.data = d
    self.neighbors = []
    
def clone_helper(root, nodes_completed):
    cloned_node = Node(root.data)
    nodes_completed[root] = cloned_node
    for p in root.neighbors:
        x = nodes_completed.get(p)
        if not x:
           cloned_node.neighbors += [clone_helper(p,nodes_completed)] 
        else:
           cloned_node.neighbors += [x] 
    return cloned_node       
                       
def clone(root):
   nodes_completed = {}
   return clone_helper(root,nodes_completed)     

data =[[2,3],[1,3],[1,2]]
node1 = create_graph(data) 
cloned_root = clone(node1)
print("\t Cloned Graph: ", create_2D_list(cloned_root), "\n", sep="")
print_graph(node1)  

## Graph Valid Tree ###############################

from collections import defaultdict 
def valid_tree(n, edges):
    if len(edges) != n-1:
        return False
    adjacenarylist = defaultdict(list)
    adjacenarylist = [[] for _ in range(n)]
    for e0,e1 in edges:
        adjacenarylist[e0].append(e1)
        adjacenarylist[e1].append(e0)
    visited = set()
    stack = []
    visited.add(0)
    stack.append(0)
    while stack:
        popped_node = stack.pop()
        for n_node in adjacenarylist[popped_node]:
            if n_node not in visited:
                visited.add(n_node)
                stack.append(n_node)
   
    return len(visited) == n   
        
n, edges = 5, [[0,1],[0,2],[0,3],[3,4]]
print(valid_tree(n, edges))

## bus roote #########################################
from collections import deque
from collections import defaultdict 
def minimum_buses(routes, src, dest):
    adjacenarylist = defaultdict(list)
    for i, stations in enumerate(routes):
        for s in stations:
            adjacenarylist[s].append(i)
    d = deque()
    visited_bus = set()
    d.append((src,0))
    
    while d :
        print(d)
        deque_s,deque_i = d.popleft()
        if deque_s == dest:
            return deque_i
        for bus in adjacenarylist[deque_s]:
            if bus not in visited_bus:
                for s in routes[bus]:
                   d.append((s,deque_i+1)) 
                visited_bus.add(bus) 
    return -1                           

routes, src, dest = [[2,5,7],[4,6,7]],2,6 
print(minimum_buses(routes, src, dest))   

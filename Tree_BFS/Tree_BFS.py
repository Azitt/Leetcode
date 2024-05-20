class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
from BinaryTree import *  
from collections import deque      
## Level Order Traversal of Binary Tree ##############
def level_order_traversal(root):
    queues = [deque(), deque()]
    current_queue = queues[0]
    next_queue = queues[1]
    # current_queue = deque()
    # next_queue = deque()
    result = ""
    current_queue.append((root))
    level_number = 0
    while current_queue:
        popped_node = current_queue.popleft()
        result += str(popped_node.data)
        if popped_node.left:
            next_queue.append(popped_node.left)
        if popped_node.right:
            next_queue.append(popped_node.right) 
        if not current_queue:
            level_number += 1    
            if next_queue: 
                result += ":"   
            # current_queue, next_queue = next_queue,current_queue  # this is the same as next line
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]
           
        else:
            result += ","  
    return result              

list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes) 
print(level_order_traversal(tree.root)) 

## 2nd solution Level Order Traversal of Binary Tree ##############  
def level_order_traversal2(root):
    result = []
    if not root:
        result = "None"
        return result
    current_q = deque()
    current_q.append(root)
    while current_q:
        
        level_size = len(current_q)
        level_node = []
        for _ in range(level_size):
           popped = current_q.popleft() 
           level_node.append(str(popped.data))
           if popped.left:
            current_q.append(popped.left)
           if popped.right:
            current_q.append(popped.right)
        
        result.append(", ".join(level_node)) 
   
    return ":".join(result)            
list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes) 
print(level_order_traversal2(tree.root)) 

## Binary Tree Zigzag Level Order Traversal######################
def binary_zigzag(root):
   current_q = deque()
   reverse = False
   current_q.append(root)
   results = []
   while current_q:
       
       level_size = len(current_q)
       results.insert(len(results), [])
       for _ in range(level_size):
          if not reverse:
           popped = current_q.popleft()
           print("popped1",popped.data)
           if popped.left:
            current_q.append(popped.left)
           if popped.right:
            current_q.append(popped.right)
          else:
              
           popped = current_q.pop()
           print("popped2",popped.data)
           if popped.right:
            current_q.appendleft(popped.right)
           if popped.left:
            current_q.appendleft(popped.left)
          results[len(results) - 1].append(popped.data) 
          print(results)  
       reverse = not(reverse)     
           
   return results                 
list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes) 
print(binary_zigzag(tree.root))

##  Populating Next Right Pointers in Each Node #############################
class EduTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
from EduBinaryTree import *
def populate_next_pointers(root):
    if not root:
        return root
    mostleft = root
    while mostleft.left:
      curr = mostleft
      while curr:         
        curr.left.next = curr.right 
        if curr.next:
            curr.right.next = curr.next.left
        curr = curr.next
      mostleft = mostleft.left 
    return root            

list_of_nodes = [EduTreeNode(3), EduTreeNode(2), EduTreeNode(17), EduTreeNode(1), EduTreeNode(4), EduTreeNode(19), EduTreeNode(5)]   
tree = EduBinaryTree(list_of_nodes) 
print(populate_next_pointers(tree.root)) 

## Vertical Order Traversal of a Binary Tree ###############
from collections import defaultdict, deque

def vertical_order(root): 
           
 curr = deque()
 hash_map = defaultdict(list)
 curr_index = 0
 min_col, max_col = 0, 0
 curr.append((root,curr_index))
 while curr:
   node, column = curr.popleft()
   if node is not None:
       hash_map[column].append(node.data)
       min_col = min(min_col,column)
       max_col = max(max_col,column)
       curr.append((node.left,column-1)) 
       curr.append((node.right,column+1))
 return[hash_map[i] for i in range(min_col,max_col+1)]  
    
list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes) 
print(vertical_order(tree.root))  

## Symmetric Tree ##############################
def is_symmetric(root):
   if not root:
       return False
   curr = deque()
   curr.append(root.left) 
   curr.append(root.right)
   while curr:       
       left = curr.popleft()
       right = curr.popleft()
       if left == None and right == None:
           continue
       if left == None or right== None:
           return False
       if left.data != right.data:
           return False
       curr.append(left.left)
       curr.append(right.right)
       curr.append(left.right)
       curr.append(right.left)
   return True     
list_of_nodes = [TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(4), TreeNode(3)]   
tree = BinaryTree(list_of_nodes) 
print(is_symmetric(tree.root))

##  Word Ladder #########################

## my solution, second solution is better ###############################

def count_diffs(s1, s2):
        count = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                count += 1
        return count
    
def word_ladder(src, dest, words): 
    words_set = set(words)
    q = deque()
    counter = 1
    q.append(src)
    while q:
        for _ in range(len(q)):
         popped_w = q.popleft()
         if popped_w == dest :
             return counter
         for w in list(words_set):
             if count_diffs(popped_w,w) == 1:
                 q.append(w)
                 words_set.remove(w)
        print(q)         
        counter += 1
        
    return 0   
  
src,dest,words = "hit", "cog", ["hot","dot","lot","log","cog"] 
print(word_ladder(src, dest, words))

## second solution which is better ###############################
def word_ladder2(src, dest, words): 
    words_set = set(words)
    
    if dest not in words_set:
        return 0
    q = deque()
    counter = 0
    q.append(src)
    while q:
        counter += 1
        for _ in range(len(q)):
         popped_w = q.popleft()
         for i in range(len(popped_w)):
             alpha = "abcdefghijklmnopqrstuvwxyz"
             for c in alpha:
               temp = list(popped_w)               
               temp[i] = c
               temp = "".join(temp)
               if temp == dest:
                    return counter + 1

               if temp in words_set:
                 q.append(temp)
                 words_set.remove(temp)
            
    return 0  
src,dest,words = "hit", "cog", ["hot","dot","lot","log","cog"] 
print(word_ladder2(src, dest, words))

## Connect All Siblings of a Binary Tree #######################
def connect_all_siblings(root):
    if not root:
        return None

    queue = deque([root])

    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        
        # Variable to store the first node of the next level
        next_level_first_node = None
        
        # Iterate over all nodes in the current level
        for i in range(level_size):
            # Get the current node
            node = queue.popleft()
            
            # Store the first node of the next level
            if i == 0:
                next_level_first_node = node.left if node.left else node.right
            
            # If this is not the last node in the queue, point its next to the next node in the queue
            if i < level_size - 1:
                node.next = queue[0]
            
            # Point the rightmost node's next to the first node of the next level
            if i == level_size - 1 and next_level_first_node:
                node.next = next_level_first_node
            
            # Add children of the current node to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root                      

list_of_nodes = [EduTreeNode(3), EduTreeNode(2), EduTreeNode(17), EduTreeNode(1), EduTreeNode(4), EduTreeNode(19), EduTreeNode(5)]   
tree = EduBinaryTree(list_of_nodes) 
print(connect_all_siblings(tree.root))         
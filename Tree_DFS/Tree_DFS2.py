class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from BinaryTree import * 
## Build Binary Tree from Preorder and Inorder Traversal#####
def build_tree_helper(p_order,i_order,left,right,p_index,hash_map):
    if left> right:
        return None
    curr = p_order[p_index[0]]
    root = TreeNode(curr)
    p_index[0] += 1
    
    if left ==right:
        return root
    in_index = hash_map[curr]
    root.left =  build_tree_helper(p_order,i_order,left,in_index-1,p_index,hash_map)
    root.right =  build_tree_helper(p_order,i_order,in_index+1,right,p_index,hash_map)
    return root
    
def build_tree(p_order,i_order):
    p_index = [0]
    hash_map ={}
    for i in range(len(p_order)):
        hash_map[i_order[i]] = i
            
    return build_tree_helper(p_order,i_order,0,len(p_order)-1,p_index,hash_map)    

p_order = [3,9,20,15,7]
i_order = [9,3,15,20,7]
build_tree(p_order,i_order)

## Binary Tree Right Side View ######################
def right_side_view_helper(root,result,level):
   
    if not root:
        return None
    
    if len(result) == level:
     result.append(root.data)
    right_side_view_helper(root.right,result,level+1)
    right_side_view_helper(root.left,result,level+1) 
    return result
def right_side_view(root):
    
    if not root:
        return []
    result,level = [],0
    return right_side_view_helper(root,result,level)

list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes)
print(right_side_view(tree.root))

## Lowest Common Ancestor in a Binary Tree ########
class Solution:
 def __init__(self):
     self.ca = None
     
 def lowest_common_ancester(self,root,p,q):
      self.lowest_common_ancester_rec(root,p,q)
      return self.ca
 def lowest_common_ancester_rec(self,current_node,p,q):
    if not current_node:
        return False
    
    mid, left, right = False,False,False
    
    if current_node == p or current_node == q:
        mid = True
    left = self.lowest_common_ancester_rec(current_node.left,p,q)  
    
    if not self.ca:
        right =  self.lowest_common_ancester_rec(current_node.right,p,q) 
    
    if mid + left + right >= 2:
         self.ca = current_node
             
    return mid or left or right

list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes)
solution = Solution() 
ans = solution.lowest_common_ancester(tree.root,tree.find(19),tree.find(5))
print(ans.data)

## Validate Binary Search Tree #####################
import math
def validate_binary_tree_rec(root,prev):
    if not root:
        return True
    
    if not validate_binary_tree_rec(root.left,prev):
        return False 
    if root.data <= prev[0]:
        return False
    prev[0] = root.data
    
    return validate_binary_tree_rec(root.right,prev)
    
def validate_binary_tree(root):
    prev = [-math.inf]
    return validate_binary_tree_rec(root,prev)         

list_of_nodes = [TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4)]   
tree = BinaryTree(list_of_nodes)
print(validate_binary_tree(tree.root))

## Maximum Depth of Binary Tree #######################
def max_tree_depth_rec(root,depth_count):
    
    if not root:
        return depth_count
    
    depth_left = max_tree_depth_rec(root.left,depth_count+1)
    depth_right = max_tree_depth_rec(root.right,depth_count+1)
   
    
    return max(depth_left,depth_right)
    
def max_tree_depth(root):
    depth_count = 0
    return max_tree_depth_rec(root,depth_count)

list_of_nodes = [TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4)]   
tree = BinaryTree(list_of_nodes)
print(max_tree_depth(tree.root))

## Kth Smallest Element in a BST #######################
def k_smallest_element_rec(root,k,k_count,result):
    if not root or k_count[0]>= k:
        return 
    k_smallest_element_rec(root.left,k,k_count,result)
    k_count[0] += 1
    if k_count[0] == k:
        result[0] = root.data
        return 
    k_smallest_element_rec(root.right,k,k_count,result)    
      
        
def k_smallest_element(root,k):
    k_count = [0]  # using a list to pass by reference
    result = [None]
    k_smallest_element_rec(root,k,k_count,result)
    return result[0]

list_of_nodes = [TreeNode(15), TreeNode(10), TreeNode(20), TreeNode(8), TreeNode(12), TreeNode(16), TreeNode(25)]   
tree = BinaryTree(list_of_nodes)
print(k_smallest_element(tree.root,4))    
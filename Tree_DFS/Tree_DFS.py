## flatten binart tree to linkedlist###########################
#Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
from BinaryTree import *  
## my solution which use more space and simpler to understand##################      
def flatten_tree_rec(root,result):
    if not root:
        return
    result.append(root.data)
    flatten_tree_rec(root.left,result)
    flatten_tree_rec(root.right,result)
    return result
    
def flatten_tree(root):
    result = []
    return flatten_tree_rec(root,result)

list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes)
print(flatten_tree(tree.root))

## their solution which is harder to underestand but use less space and modify tree in place###############
def flatten_tree(root):
    if not root:
        return
    current = root
    while current:
        if current.left:
            last = current.left
            while last.right:
              last = last.right  
            last.right = current.right
            current.right = current.left
            current.left = None
        current = current.right
    return root            
list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes)
print(flatten_tree(tree.root))
## Diameter of Binary Tree #########################
def diameter_of_binaryTree_helper(root,diameter):
    if not root:
        return 0, diameter
    lh, diameter = diameter_of_binaryTree_helper(root.left,diameter)
    rh, diameter = diameter_of_binaryTree_helper(root.right,diameter)
    
    diameter = max(diameter,lh+rh)
    return max(lh,rh) + 1, diameter

def diameter_of_binaryTree(root):
    
    if not root:
        return 0
    diameter = 0
    _, diameter = diameter_of_binaryTree_helper(root,diameter)
    return diameter

list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes)
print(diameter_of_binaryTree(tree.root))
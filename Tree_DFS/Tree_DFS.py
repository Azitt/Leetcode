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

## serialize and Deserialize Binary Tree ############################
Marker = "M"
m = 1
def serialize_rec(node, stream):
    global m
    if node is None:
        stream.append(Marker + str(m))
        m += 1
        return
    stream.append(node.data)
    serialize_rec(node.left,stream)  ## preorder travelsal
    serialize_rec(node.right,stream)
    
    return stream
def serialize(root):
    
    stream = []
    return serialize_rec(root,stream)

def deserialize_helper(stream):
    val = stream.pop()
    if type(val) is str and val[0]==Marker:
        return None
    node = TreeNode(val)
    node.left = deserialize_helper(stream)
    node.right = deserialize_helper(stream)
    
    return node

def deserialize(stream):
    stream.reverse() ## to fetch the root first
    return deserialize_helper(stream)

list_of_nodes = [TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)]   
tree = BinaryTree(list_of_nodes)
ostream = serialize(tree.root)
print(ostream)
deserialized_root = deserialize(ostream)

## Invert Binary Tree ##########################
def mirror_binary_tree(root):
    if root is None:
        return None
    if root.left:
     mirror_binary_tree(root.left)
     
    if root.right: 
     mirror_binary_tree(root.right)
    root.left, root.right = root.right, root.left
    return root
 
list_of_nodes = [TreeNode(20), TreeNode(50), TreeNode(200), TreeNode(75), TreeNode(25), TreeNode(300)]   
tree = BinaryTree(list_of_nodes)
mirror_binary_tree(tree.root)

## Binary Tree Maximum Path Sum #######################
## we takes a node as an argument and computes a maximum contribution that this node and one or none of its subtrees can add####
def max_contrib(root):
    
    if not root:
        return 0
    max_left = max_contrib(root.left)
    max_right = max_contrib(root.right)
    
    left_subtree = 0
    right_subtree = 0
    
    if max_left > 0:
        left_subtree = max_left
    if max_right >0:
        right_subtree = max_right
         
    value_new_path = root.data +  left_subtree +  right_subtree
    max_sum = max_contrib.max_sum
    max_contrib.max_sum = max(max_sum,value_new_path) 
    
    return root.data + max(left_subtree,right_subtree)    
    
        
def max_path_sum(root):
    max_contrib.max_sum = float("-inf") 
    max_contrib(root)
    return max_contrib.max_sum   

list_of_nodes = [TreeNode(20), TreeNode(50), TreeNode(200), TreeNode(75), TreeNode(25), TreeNode(300)]   
tree = BinaryTree(list_of_nodes)
print(max_path_sum(tree.root))

## Convert Sorted Array to Binary Search Tree####################
def sorted_array_to_bst_helper(nums,low,high):
    if low > high:
        return None

    mid = low +(high - low)//2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst_helper(nums,low,mid-1)
    root.right = sorted_array_to_bst_helper(nums,mid+1,high)
    return root    

def sorted_array_to_bst(nums): 
    low = 0
    high = len(nums) - 1
    return sorted_array_to_bst_helper(nums,low,high)       

nums = [1,2,3,4,5,6,7]
print(sorted_array_to_bst(nums))               
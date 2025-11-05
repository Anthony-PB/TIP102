from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Problem 1:
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# root = TreeNode("Trunk")
# opal = TreeNode("Opal")
# gran_smith = TreeNode("Granny Smith")
# crab = TreeNode("Crab")
# gala = TreeNode("Gala")
# fuji = TreeNode("Fuji")
# mc = TreeNode("Mcintosh")
# mc.left = fuji
# mc.right = opal
# root.left = mc
# root.right = gran_smith
# gran_smith.left = crab
# gran_smith.right = gala

# # Using print_tree() included at the top of this page
# print_tree(root)

# # Expected Result: ['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']

# Problem 2:
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# # Leaf nodes have an integer value.
# # The root has a string value of either "+", "-", "*", or "/".
# def calculate_yield(root):
#     if not root.left and not root.right:
#         return root.val
#     left_val = calculate_yield(root.left)
#     right_val = calculate_yield(root.right)

#     if root.val == "+":
#         return right_val + left_val
#     if root.val == "-":
#         return right_val - left_val
#     if root.val == "*":
#         return right_val * left_val
#     if root.val == "/":
#         return right_val/left_val

# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))

# 12
# Problem 3 and 4
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
# # If there is no right child, return only the root node value
# # Iteratively
# def right_vine(root):
#     if not root.right:
#         return [root.val]

#     result = []
#     current = root

#     while current:
#         result.append(current.val)
#         current = current.right

#     return result   
        
# # Recursively
# def right_vine(root):
#     if not root.right:
#         return [root.val]
#     return [root.val] + right_vine(root.right)






# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# ['Root', 'Node2', 'Leaf3']
# ['Root']

# Problem 5
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def count_leaves(root):
#     if root is None:
#         return 0
#     if root.right == None and root.left == None:
#         return 1
#     return count_leaves(root.right) + count_leaves(root.left)

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(count_leaves(oak1))
# print(count_leaves(oak2))

# # 3
# # 1

# Problem 6

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
# L -> R -> S
def survey_tree(root):
    #if root.right == None and root.left == None:
    #    return [root.val]
    res = []
    if root.left:
        res = res + survey_tree(root.left)
    if root.right:
        res = res + survey_tree(root.right)
    res = res + [root.val]
    return res
    

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

# ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]

# Problem 7

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvest_berries(root, threshold):
  pass
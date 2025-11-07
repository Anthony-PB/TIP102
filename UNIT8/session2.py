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

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

# DO NOT COMMENT OUT THE LINES ABOVE

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right

# # Traverse tree and return total number of nodes that have a odd value
# def count_odd_splits(root):
#     if(not root):
#         return 0
#     if(root.val % 2 == 0):
#         return count_odd_splits(root.left) + count_odd_splits(root.right)
#     else:
#         return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)

# """
#       2
#      / \
#     /   \
#    3     5
#   / \     \
#  6   7     12
# """

# # Using build_tree() function included at top of page
# values = [2, 3, 5, 6, 7, None, 12]
# monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))

# # Problem 2:
# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def find_flower(inventory, name):
#     if not inventory:
#         return False
#     if inventory.val == name:
#         return True
    
#     if name < inventory.val:
#         return find_flower(inventory.left, name)
#     else:
#         return find_flower(inventory.right, name)


# """
#          Rose
#         /    \
#       Lily   Tulip
#      /  \       \
#   Daisy  Lilac  Violet
# """

# # using build_tree() function at top of page
# values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
# garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 

# # True
# # False

# # Problem 3
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def non_bst_find_flower(root, name):
#     if root is None:
#         return False
    
#     if root.val == name:
#         return True

#     return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

# """
#          Daisy
#         /    \
#       Lily   Tulip
#      /  \       \
#   Rose  Violet  Lilac
# """

# # using build_tree() function at top of page
# values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
# garden = build_tree(values)

# print(non_bst_find_flower(garden, "Lilac"))  
# print(non_bst_find_flower(garden, "Sunflower")) 

# # True
# # False

# # Problem 4
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def add_plant(collection, name):
#     if(not collection):
#         return TreeNode(name)
#     if(collection.val <= name):
#         collection.right = add_plant(collection.right, name)
#     else:
#         collection.left = add_plant(collection.left, name)
#     return collection

# """
#             Money Tree
#         /              \
# Fiddle Leaf Fig    Snake Plant
# """

# # Using build_tree() function at the top of page
# values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(add_plant(collection, "Aloe"))

# # ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

# # Explanation: 
# # Tree should have the following structure:
# #            Money Tree
# #         /              \
# #  Fiddle Leaf Fig   Snake Plant
# #    /
# #  Aloe
# Problem 5

# """
# Inorder: L, C, R


# """

# class TreeNode:
#     def __init__(self, key, value, left=None, right=None):
#         self.key = key      # Plant rarity
#         self.val = value      # Plant name
#         self.left = left
#         self.right = right


# def sort_plants(collection):

#     if not collection:
#         return []
    
#     left = sort_plants(collection.left)
#     current = [(collection.val, collection.key)]
#     right = sort_plants(collection.right)

#     return left + current + right

# """
#          (3, "Monstera")
#         /               \
#    (1, "Pothos")     (5, "Witchcraft Orchid")
#         \                 /
#   (2, "Spider Plant")   (4, "Hoya Motoskei")
# """

# # Using build_tree() function at the top of page
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))

# # [(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]

class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def pick_plant(inventory, budget):
    plant = None

    while inventory:
        if inventory.key < budget:
            plant = inventory

"""
               (50, "Fiddle Leaf Fig")
             /                       \
    (25, "Monstera")           (70, "Snake Plant")
       /        \                   /         \
(15, "Aloe")  (40, "Pothos")  (60, "Fern")  (80, "ZZ Plant")
"""

# Using build_tree() function at the top of page
values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

print(pick_plant(inventory, 50)) 
print(pick_plant(inventory, 25)) 
print(pick_plant(inventory, 15)) 

# Pothos
# Aloe
# None
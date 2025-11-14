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



# # Problem 1:
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# # A balanced display is a binary tree in which the difference in the height of the two subtrees of every node never exceeds one.
# def is_balanced(root):
#     # Difference between trees should be 1 or 0 | -1 means not balanced
#     def helper(display):
#         if not display:
#             return 0
#         leftH = helper(display.left)
#         if(leftH == -1):
#             return -1
#         rightH = helper(display.right)
#         if(rightH == -1):
#             return -1
#         if(abs(leftH-rightH) > 1):
#             return -1
#         return 1 + max(leftH, rightH)
#     return helper(root) != -1
    
    
    


# """
#       🎂
#      /  \
#    🥮   🍩
#        /  \  
#      🥖    🧁

# """
# # Using build_tree() function included at top of page
# baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
# display1 = build_tree(baked_goods)

# """
#           🥖
#          /  \
#        🧁    🧁
#        /       \  
#       🍪       🍪
#      /           \
#     🥐           🥐  

# """
# baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
# display2 = build_tree(baked_goods)


# print(is_balanced(display1)) 
# print(is_balanced(display2))

# # True
# # False

# # Problem 2:
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def sum_each_days_orders(orders):
#     if orders is None:
#         return []
#     res = []
#     queue = deque([orders])
#     while queue:
#         sum = 0
#         for i in range(len(queue)):
#             curr = queue.popleft()
#             # Add value to sum
#             sum += curr.val
#             # Add Children to Queue
#             if(curr.left):
#                 queue.append(curr.left)
#             if(curr.right):
#                 queue.append(curr.right)
#         # One level traversed so append sum to result
#         res.append(sum)
        
#     return res
# """
#       4
#      / \
#     2   6
#    / \  
#   1   3
# """

# # Using build_tree() function included at top of page
# order_sizes = [4, 2, 6, 1, 3]
# orders = build_tree(order_sizes)

# print(sum_each_days_orders(orders))

# # [4, 8, 4]

# Problem 3:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweet_difference(chocolates):
    if not chocolates: 
        return []

        result = []
        queue = deque([chocolates])

        while queue:
            level

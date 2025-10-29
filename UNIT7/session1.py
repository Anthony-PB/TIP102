"""
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count
def count_suits_recursive(suits):
    if(not suits):
        return 0
    return 1 + count_suits_recursive(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))
"""

#One minute my laptop got stuck i will joing back in 2 min : pavan (got it)

# def sum_stones(stones):
#     if not stones:
#         return 0
#     return stones[0]+sum_stones(stones[1:])

# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

# # 105
# # 68
"""
def count_suits_iterative(suits):
    res = set()
    for suit in suits:
        res.add(suit)
    return len(res)

res = set()
def count_suits_recursive(suits):
    if(not suits):
        return len(res)
    res.add(suits[0])
    return count_suits_recursive(suits[1:])
# Example Usage:

print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

# Example Output:

# 2
# 2


def fibonacci_growth(n):
    
    if n == 0:
        return 0
    elif n==1:
        return 1
    
    return fibonacci_growth(n-1) +fibonacci_growth(n-2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))
"""
"""
# base case four to the power of zero is one
# recursive 
# positive -> mulitply by 4 and pass it with reduced power by one
# negative -> reciprocal and pass it with negative of power
def power_of_four(n):
    if n == 0:
        return 1
    elif n>0:
        return 4*power_of_four(n-1)
    else:
        return 1/power_of_four(-1*n)

print(power_of_four(2))
print(power_of_four(-2))
"""

# def strongest_avenger(strengths):
    
#     if len(strengths) ==   1:
#         return strengths[0]
    
#     # to find the max one
#     max_strenght = strongest_avenger(strengths[1:])
    
#     return strengths[0] if strengths[0]>max_strenght else max_strenght



# #Example Usage:

# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75, 85, 60, 90]))
#Example Output:

#100
#Example 1 Explanation: The maximum strength among the Avengers is 100.

#90
#Example 2 Explanation: The maximum strength among the Avengers is 90.

# def count_deposits(resources):
#     if(not resources):
#         return 0
#     if(resources[0] == 'V'):
#         return 1 + count_deposits(resources[1:])
#     else:
#         return count_deposits(resources[1:])
# #Example Usage:

# print(count_deposits("VVVVV"))
# print(count_deposits("VXVYGA"))
#Example Output:

# 5
# 2
# Example 2 Explanation: There are two characters "V" in the string "VXVYGA", 
# therefore there are two vibranium deposits in the string.

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# base 1 -> mission 1 empty return mission 2
# base 2 -> vice versa
# recursive if mission1 value is lesser, add it to the list and recurse_merge(m1.next,m2)
# vice versa
# def merge_missions(mission1, mission2):
#     if not mission1:
#         return mission2
#     if not mission2:
#         return mission1
#     if mission1.value < mission2.value:
#         mission1.next = merge_missions(mission1.next,mission2)
#         return mission1
#     else:
#         mission2.next = merge_missions(mission2.next,mission1)
#         return mission2

# mission1 = Node(1, Node(2, Node(4)))
# mission2 = Node(1, Node(3, Node(4)))

# print_linked_list(merge_missions(mission1, mission2))
# # 1 -> 1 -> 2 -> 3 -> 4 -> 4


# Problem 1: Counting the Layers of a Sandwich
# You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. Each layer is represented by a nested list. Given a list of lists sandwich where each list [] represents a sandwich layer, write a recursive function count_layers() that returns the total number of sandwich layers.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# def count_layers(sandwich):
#     if(len(sandwich) < 2):
#         return len(sandwich)
#     return 1 + count_layers(sandwich[1])
# # Example Usage:

# sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
# sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))
# # Example Output:

# 4
# 5

#base case -> if nothing return nothing
#recursive -> take last el + recursivefunc(everything but the last)
def reverse_orders(orders):
    order_list = orders.split()
    if not order_list:
        return ""
    else:
        return order_list[-1] + " " + reverse_orders(" ".join(order_list[:-1]))


# Example Usage:

print(reverse_orders("Bagel Sandwich Coffee"))
# Coffee Sandwich Bagel
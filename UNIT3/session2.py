"""
    Implement a sparse vector class.
    Must have a contructor and a method called dot product.
"""

"""
    We want to store the actual useful entries in a dictionary to be space efficient?
"""

class BadSparseVector:

    def __init__(self, size, entries):
        # Size is a integer.
        # Entries is a list?
        self.size = size
        self.entries = entries

    # Instance method
    def dotProduct(self, vec1):
        res = 0
        for i in range(self.size):
            current = self.entries[i]
            if(current != 0):
                res += current * vec1[i]
        return res
class SparseVector:
    def __init__(self, entries):
        nonzero_indices = {}
        # Size is a integer.
        # Entries is a list?
        for i in range(len(entries)):
            current = entries[i]
            if(current != 0):
                nonzero_indices[i] = entries[i]
        self.entries = nonzero_indices
        #self.size = len(nonzero_indices)

    # If vec1 was a list.
    def dotProduct(self, vec1):
        res = 0
        for i in self.entries.keys():
            current = self.entries[i]
            if(i < len(vec1)):
                res += current * vec1[i]
        return res
    # If vec1 was a sparseVector itself ->
        def get(self, index):
            if index < 0 or index >= self.size:
                raise IndexError("Index out of bounds for the vector.")
            return self.entries.get(index, 0)
        def dotProduct(self, vec1):
        res = 0
        for i in self.entries.keys():
            current = self.entries[i]
            if(i < vec1.size):
                res += current * vec1.get(i)
        return res

# Problem 1
"""
You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array costs, where costs[i] is the cost of the ith supply item.

There is a special discount available during the expedition. If you purchase the ith item, you will receive a discount equivalent to costs[j], where j is the minimum index such that j > i and costs[j] <= costs[i]. If no such j exists, you will not receive any discount.

Return an integer array final_costs where final_costs[i] is the final cost you will pay for the ith supply item, considering the special discount.
"""

def final_supply_costs(costs):

  n = len(costs)
  final_costs = list(costs)
  stack = []

  for i, current_cost in enumerate(costs):
    while stack and costs[stack[-1]] >= current_cost:
      prev_index = stack.pop()
      final_costs[prev_index] = costs[prev_index] - current_cost
    stack.append(i)
  return final_costs
        


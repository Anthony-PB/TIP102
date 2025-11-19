from collections import deque
"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
'''provided for this problem
# Add your code here

flights = {
    "JFK":["LAX", "DFW"],
    "LAX":["JFK"],
    "DFW":["ATL", "JFK"],
    "ATL":["DFW"]
}


print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])


# ['JFK', 'LAX', 'DFW', 'ATL']
# [['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
# ['LAX', 'DFW']
'''
'''

def bidirectional_flights(flights):
    total = len(flights)
    for i in range(total):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True
    
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

'''
'''
# i = source
# n[i][j] = 1 or 0
    # 1 -> i to j works
def get_direct_flights(flights, source):
    direct_flights=[]
    
    # flights is n by n
    for des in range(len(flights)):
        if flights[source][des]==1:
            direct_flights.append(des)
    return direct_flights

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))

# [0, 1, 3]
# []
'''
'''
# flights[i] = [a, b] -> a to b flight AND b to a flight
def get_adj_dict(flights):
    res = {}
    for a, b in flights:
        if a not in res:
            res[a] = []
        res[a].append(b)
        if b not in res:
            res[b] = []
        res[b].append(a)
    return res
        

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))


# {
#     'Cape Town': ['Addis Ababa', 'Cairo'],
#     'Addis Ababa': ['Cape Town', 'Lagos'],
#     'Lagos': ['Cairo', 'Addis Ababa'],
#     'Cairo': ['Lagos', 'Nairobi', 'Cape Town'],
#     'Nairobi': ['Cairo']
# }
'''
'''
def find_center(terminals):
    count = {}
    n = len(terminals)
    for i in range(n):
        for j in terminals[i]:
            if j not in count:
                count[j] = 0
            else:
                count[j] += 1
                if(count[j] == n-1):
                    return j

    
    return terminals



terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))

# 2
# 1
'''
# BFS through flights with the origin of traversal being the "start" node
from collections import queue
def get_all_destinations(flights, start):
    queue = deque()
    visited = set([start])
    layovers = []
    while queue:
        current = queue.popleft()
        layovers

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))

# ['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
# 'Reykjavik']
# ['Helsinki', 'Cairo', 'New York', 'Reykjavik']


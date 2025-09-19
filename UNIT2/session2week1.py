



# Live Demo Question:
# NaNaNa Batman!
def nanana_batman(x):
    res = []
    for i in range(x):
        res.append("na")
    print("".join(res) + " batman!")

nanana_batman(10)

def maxConsecutiveOnes(nums):
    l = 0
    n = len(nums)
    res = 0
    for r in range(n):
        if(nums[r] == 0):
            l = r + 1
        res = max(res, r - l + 1)
    return res

test1 = [1,1,1,1,1]
"""
print(maxConsecutiveOnes(test1))
"""

# Problem Set Advanced:
    #  Problem 1: Balanced Art Collection
# Input: array of int
# Output: length of longest subsequence of input where the most expensive and least expensive differ by 1
# Possible Plan:
# 
"""
art_pieces1 = [1,3,2,2,5,2,3,7] # 5
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

Plan:
given differ = 1 so min,max num in arr will x,x+1
use counter get freq of each num in arr
then iter through the counter 


"""

from collections import Counter
def find_balanced_subsequence(art_pieces):
    cnt = Counter(art_pieces)
    print(cnt)
    res = 0
    for x,c in cnt.items():
        if x+1 in cnt:
            res = max(res, c+cnt[x+1])
    return res
    
        
print(find_balanced_subsequence([1,1,2,3,4]))


# Input: art_pieces: array of ints
# Output: boolean
def is_authentic_collection(art_pieces):
    n = len(art_pieces)-1
    if n < 1:
        return False
    if max(art_pieces) > n:
        return False
    cnt = Counter(art_pieces)
    for i in range(1,n):
        if cnt[i]!= 1:
            return False
    if cnt[n]!= 2:
        return False
    return True
"""
collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]
collection4 = [1, 2, 3, 4, 5, 5, 8]
collection5 = []

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
print(is_authentic_collection(collection4))
print(is_authentic_collection(collection5))
"""

# Problem 3: Gallery Wall
def organize_exhibition(collection):
    cnt = Counter(collection)
    mx = max(cnt.values())
    res = [[] for _ in range(mx)]
    print(res)
    # For each unique painting in the collection array, we are starting from the "top"/0th row of our res array and adding all paintings at once. (One for each row.)
    for w in cnt:
        for j in range(cnt[w]):
            res[j].append(w)
    return res

"""
collection3 = ["p1", "p2", "p3", "p4", "p1"]
print(organize_exhibition(collection3))

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))
"""
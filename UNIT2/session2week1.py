
from collections import Counter


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

# Problem 4: Gallery Subdomain Traffic
def subdomain_visits(cpdomains):
    cnt = {}
    for domain in cpdomains:
        # Default splits by whitespace
        num, domain = domain.split()
        num = int(num)
        all_subdomains = domain.split('.')
        for i in range(len(all_subdomains)):
            subdomain = ".".join(all_subdomains[i:])
            if subdomain not in cnt:
                cnt[subdomain] = 0
            cnt[subdomain] += num
    res = []
    for domain, num in cnt.items():
        res.append(f"{num} {domain}" )
    return res

"""
cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))
"""

"""
Random Notes from slides:
Dictionaries use hash functions-> h(x) = (x * 31) % 4

How do you solve collisions?
-> Chaining (Store the key,value in a linked list) (not great if we have too many collisions) (only ok if our hash function is goated)
-> You can also use open addressing-> you essentially just look for the next open slot in the dictionary.

Average Case is O(1) -> as the hash function will give you the address where the corresponding value is stored!

Instructor Demo:
def freqGrocery(fruitList):
    res = {}
    for i in range(len(fruitList)):
        if fruitList[i] not in res:
            res[fruitList[i]] = 1
        else:
            res[fruitList[i]]++
    return res
    or
    return Counter(fruitList)

Group Anagrams->
You can use counter for each word and compare or you can sort each string and then compare!
Heavily reliant on built-in functions
"""
# Problem 5: Beautiful Collection
"""
Helper Method Approach ->
Each artist is a character
Beauty of a collection is defined by the freq difference between the most frequest character and the least frequest character. (This is our helper)
We also need to get every possible substring from our input collection
"""
def beauty_sum(collection):
    def beauty(string):
        cnt = Counter(list(string))
        return max(cnt) - min(cnt)
    def substrings(string):
        n = len(string)
        res = 0
        for i in range(n):
            for j in range(i,n):
                
        return res
    return substring(collection)





# Diff Problem set in the same UNIT 2

# # Captain Blackbeard has a treasure map with several clues that point to different locations on an island. 
# # Each clue is associated with a specific location and the number of treasures buried there. 
# # Given a dictionary treasure_map where keys are location names and values are integers representing the 
# # number of treasures buried at those locations, write a function total_treasures() that returns the total 
# # number of treasures buried on the island.
# """
# Understanding:
# Input: Dictionary -> keys are locations and values are ints representing treasure
# Output: Sum of all treasure available

# Planning:
# get values and sum values

# Implemenation: 
# Get the sum of the values via sum(teasure_map.values())
# """

# def total_treasures(treasure_map):
#     return sum(treasure_map.values())
#     # pass
# # Example Usage:

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2)) 
# # Example Output:

# # 15
# # 50

# Problem 2: Pirate Message Check
# Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew.
#  She will know she can trust the message if it contains all of the letters in the alphabet. 
# Given a string message containing only lowercase English letters and whitespace, write a function 
# can_trust_message() that returns True if the message contains every letter of the English alphabet at
#  least once, and False otherwise.

# Understanding: To check if there are all the alphabets in the given string using set()

# Planning: create a set, alpha_set and check the len of the set to make sure it is of len 26 

# Implementation: 

# def can_trust_message(message):
#     char_set = set(message)
#     return len(char_set) == 27
#     # pass
# # Example Usage:
# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))
# Example Output:

# True
# False


# Problem 3: Find All Duplicate Treasure Chests in an Array
# Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the
#  range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, 
# representing the treasure chests that have duplicates.

# Understanding:
# Which "chests"/integers in chests have duplicates (2 occurrences)
# Planning:
# Use Counter too count the frequencies
# Implementation:
# ->

# from collections import Counter
# def find_duplicate_chests(chests):
#     res = []
#     chest_count = Counter(chests)

#     for k, v in chest_count.items():
#         if v == 2:
#             res.append(k)
#     return res  
# #     # pass

# # # Example Usage:

# # chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# # chests2 = [1, 1, 2]
# # chests3 = [1]

# # print(find_duplicate_chests(chests1))
# # print(find_duplicate_chests(chests2))
# # print(find_duplicate_chests(chests3))
# # # Example Output:

# # # [2, 3]
# # # [1]
# # # []

# Problem 4: Booby Trap
# Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped.
#  The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the 
# trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every 
# letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one 
# letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to 
# balance the pirate code.

# Given a 0-indexed string code consisting of only lowercase English letters, 
# write a function can_make_balanced() that returns True if it's possible to remove one 
# letter so that the frequency of all remaining letters is equal, and False otherwise.

# '''
# Understanding:
# Only one char in code is allowed to differ by one.
# Retus a bolean
# Planning:


# Implement:
# '''
# from collections import Counter
# def can_make_balanced(code):
#     count_chars = Counter(code)
#     char_set = set(count_chars.values())
#     char_set = list(char_set)
#     if len(char_set) == 2:
#         return abs(char_set[0] - char_set[1]) == 1
#     else:
#         return False
                
# # Example Usage:

# code1 = "arghh"
# code2 = "haha"

# print(can_make_balanced(code1)) 
# print(can_make_balanced(code2)) 
# # Example Output:

# True
# Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

# False
# Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2, or vice versa. 


# Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an 
# island. Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword 
# already has plenty of loot, and their ship is nearly full. They want to find two distinct locations on the map 
# such that the sum of the gold amounts at these two locations is exactly equal to the amount of space left on 
# their ship.

# Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, 
# return the indices of the two locations whose gold amounts add up to the target.

# Assume that each input has exactly one solution, and you may not use the same location twice. You can return the
#  answer in any order.

# '''
# Understanding:

# Planning:

# Implement:
# '''

# def find_treasure_indices(gold_amounts, target):
#     freq_map = {}
    
#     for i in range(len(gold_amounts)):
#         complement = target - gold_amounts[i]
#         if complement in freq_map:
#             return [freq_map[complement], i]
#         freq_map[gold_amounts[i]] = i
#     return []

# # Example Usage:

# gold_amounts1 = [2, 7, 11, 15]
# target1 = 9

# gold_amounts2 = [3, 2, 4]
# target2 = 6

# gold_amounts3 = [3, 3]
# target3 = 6

# print(find_treasure_indices(gold_amounts1, target1))  
# print(find_treasure_indices(gold_amounts2, target2))  
# print(find_treasure_indices(gold_amounts3, target3))  
# # Example Output:

# # [0, 1]
# # [1, 2]
# # [0, 1]

# Problem 6: Organize the Pirate Crew
# Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.

# You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in. For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.

# Return a list of groups such that each pirate i is in a group of size group_sizes[i].

# Each pirate should appear in exactly one group, and every pirate must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

# def organize_pirate_crew(group_sizes):
#     pass
# Example Usage:

# group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
# group_sizes2 = [2, 1, 3, 3, 3, 2]

# print(organize_pirate_crew(group_sizes1))
# print(organize_pirate_crew(group_sizes2)) 
# Example Output:

# [[5], [0, 1, 2], [3, 4, 6]]
# [[1], [0, 5], [2, 3, 4]]


# Problem 8:
"""


def find_difference(signals1, signals2):
    if(not signals1):
        return [list(set(signals2))]
    if(not signals2):
        return [list(set(signals1))]
    s1 = set(signals1)
    s2 = set(signals2)

    diff1 = s1.difference(s2)
    diff2 = s2.difference(s1)

    # Here we can see that .difference on a set simply gets the between s1 and s2 where we keep

    return [list(diff1), list(diff2)]

"""

# Problem 6: Counting Divisible Collections in the Gallery
# You have a list of integers collection_sizes representing the sizes of different art collections in your gallery and are trying to determine how to group them to best fit in your space. 
# Given an integer k write a function count_divisible_collections() that returns the number of non-empty subarrays (contiguous parts of the array) where the sum of the sizes is divisible by k.

def count_divisible_collections(collection_sizes, k):
    count = 0
    n = len(collection_sizes)
    for i in range(0,n):
        for j in range(i,n):
            nSum = sum(collection_sizes[i:j+1])
            if(nSum % k == 0):
                count = count + 1

    return count



nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  
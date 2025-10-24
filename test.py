"""
Problem #1
Given a string s consisting of English letters (lowercase and/or uppercase) and digits, return all possible strings that can be formed by changing the case of the letters in s. You may not alter the order of characters in the string, and digits should remain unchanged.
Input: s = "a1b2"
Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
Input: s = "3z4"
Output: ["3z4", "3Z4"]
Input: s = "12345"
Output: ["12345"]
"""
# Understanding:
# We want to essentially treat each letter character as a binary where it can either be lowercase or uppercase
# Input -> String
# Output -> List of strings

# Match:
# BFS
# List to store our current results

# Plan:
# Empty List to start res = [""]
# for char in s: (index access or for each)
# next_results = []
# if digit append digit to element
# else if 
# res.append()
# res.append()
# res = next_results
# Return res


# Time Complexity: O(n * 2^L)
# Space Complexity: O(2^n)

def possible_string(s):
    res = [""]
    for i in range(len(s)):
        next_results = []
        curr_char = s[i]
        if(curr_char.isdigit()):
            for element in res:
                next_results.append(element + curr_char)
        else:
            for element in res:
                next_results.append(element + curr_char.lower())
                next_results.append(element + curr_char.upper())
        res = next_results
    return res

print(possible_string("a1b2"))
print(possible_string("abbc"))
        
        
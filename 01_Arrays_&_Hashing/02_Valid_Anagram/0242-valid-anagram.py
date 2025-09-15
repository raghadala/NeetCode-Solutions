"""
Problem: LeetCode 242 - Valid Anagram 

Key Idea:
To determine if two given strings are anagrams of each other, we can compare their character frequencies. An anagram of a string contains the same characters with the same frequency, just arranged differently. We can use a hash map (dictionary in Python) to keep track of the character frequencies for each string. If the character frequencies of both strings match, then they are anagrams.

Time Complexity:
The time complexity of this approach is O(n), where n is the length of the input strings. We need to traverse both strings once to build the character frequency maps.

Space Complexity:
The space complexity is O(1) because the hash map will have at most 26 entries (one for each lowercase English letter) regardless of the input string lengths. Therefore, the space complexity is constant.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            # access ith element and get the value its at right now, then add 1 to it if it exists else 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # return True if count is the same
        return countS == countT

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT, countS = {}, {}

        if len(s) == len(t):
            for i in t:
                if i in countT:
                    countT[i] +=1 
                else:
                    countT[i] = 1
            
            for i in s:
                if i in countS:
                    countS[i] +=1 
                else:
                    countS[i] = 1
            return countS == countT
        else: 
            return False

# Time: O(n)
# Space: O(1) (fixed alphabet) or O(k) (general alphabet).


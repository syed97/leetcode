'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
'''

# O(n) solution - using sorting and linear search
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        t = sorted(t)
        s = sorted(s)
        # initial check
        if len(s) != len(t):
            return False
        count = 0
        for i in range(len(s)):
            if s[i] == t[i]:
                count += 1
        if count == len(s):
            return True
        else:
            return False

# O(n) solution - using frequency hash map. Increase count of letter when iterating over first string
# and decrese the count when iterating over second string to track occurrences
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}
        for i in range(len(s)):
            if s[i] in set_s:
                set_s[s[i]] += 1
            else:
                set_s[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in set_s:
                set_s[t[i]] -= 1
            else:
                return False
        # iterate over dictionary and check for zero vals
        for val in set_s.values():
            if val != 0:
                return False
        return True
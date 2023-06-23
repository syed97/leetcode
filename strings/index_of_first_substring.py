'''
 Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

# brute force search - 0((n-m+1)*m) ~ O(n*m)
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            count = 0
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                else:
                    count += 1
                if count == len(needle):
                    return i
        return -1


                
# a solution exists using KMP algorithm as well - more optimized O(n+m) but not intuitive


sol1 = Solution1()
haystack = "a"
needle = "a"
print(sol1.strStr(haystack, needle))
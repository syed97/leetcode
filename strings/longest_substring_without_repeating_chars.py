'''
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

# brute force approach - O(n^2)
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_count = 1
        for i in range(len(s)-1):
            count = 1
            st = set(s[i])
            for j in range(i+1,len(s)):
                if s[j] in st:
                    break
                else:
                    count += 1
                    st.add(s[j])
                if count > max_count:
                    max_count = count
        return max_count
                
'''
sliding window approach O(n) - iterate over each element and update sliding window using left pointer if a duplicate is encountered.
The tricky part was to remember to increase left pointer until the duplicate no longer existed e.g. tricky in the case of pweekew.
Hence, had to add while loop.

Approach is to essentially use left, right pointers to represent a sliding window which gets updated one cnountering duplicates
and hence the count of the window would also be updated.
'''


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_count = 0
        seen = set()
        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            count = r-l+1
            max_count = max(max_count,count)
        return max_count

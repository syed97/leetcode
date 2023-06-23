'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

# solution using left and right pointers
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        mod_s = []
        for i in range(len(s)):
            if s[i].isalnum():
                mod_s.append(s[i])

        left = 0
        right = len(mod_s) - 1

        while left <= right:
            if mod_s[left] == mod_s[right]:
                left += 1
                right -=1 
            else:
                return False
        return True


# solution using string reversal
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        s = ''.join(char for char in s if char.isalnum()).lower()
        # Check if string is equal to its reverse
        return s == s[::-1]

                
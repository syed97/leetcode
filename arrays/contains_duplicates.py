'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# brute force search - O(n^2) tiem and O(1) space
class Solution1:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False

# O(nlogn) time and O(1) space - sort array and check value at next index for duplicate
class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_s = sorted(nums)
        for i in range(len(nums_s)-1):
            if nums_s[i] == nums_s[i+1]:
                return True
        return False

# O(n) time complexity, O(n) space complexity - uses hash map/dictionary for storing 
# duplicates. Note: instead of uising hash map/dictionary, you can use hash set/set() in Python
class Solution3:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                return True
            else:
                dic[nums[i]] = i
        return False


nums = [1,1,1,3,3,4,3,2,4,2]
sol1 = Solution1()
sol2 = Solution2()
sol3 = Solution3()

print(sol1.containsDuplicate(nums))
print(sol2.containsDuplicate(nums))
print(sol3.containsDuplicate(nums))
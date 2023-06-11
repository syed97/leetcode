'''
Given an integer array nums, find the subarray with the largest sum,
and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

# O(n^2) - brute force search for all subarrays and their sums
class Solution1:
     def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i,len(nums)):
                curr_sum += nums[j]
                if curr_sum > max_sum:
                    max_sum = curr_sum
        return max_sum

# O(n) solution using Kadane's algorithm - as we move across the array, we compute the subarray sum
# till that point using cur_sum. If the current sum is negative, we reset it to zero as we essentially
# wamt to discard the effect of the negative terms in the subarray as they don't positively impact our max sum.
# We then return the max sum
class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            # print("i: ", i, "nums[i]: ", nums[i])
            # print("cs: ", cur_sum)
            max_sum = max(cur_sum, max_sum)
            # print("ms: ", max_sum)
        return max_sum
                

sol = Solution2()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))
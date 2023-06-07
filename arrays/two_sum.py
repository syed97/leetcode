'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
# O(n^2) solution - brute force/two loops
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res

# O(n) solution - using hash map/dictionary
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        d = {}
        for i in range(len(nums)):
            if (target - nums[i]) in d.keys():
                res.append(i)
                res.append(d[target - nums[i]])
            else:
                d[nums[i]] = i
        return res      

# O(nlogn) solution - two pointers approach. We first sort the array and then assign two pointers
# at either end of the array. We then check the sum of values at both indices. If the sum is less
# than the target then we increment the left pointer as we know the target would be greater the current sum.
# If the sum is greater than the target then we decrement the right pointer so we can move nearer to the target.
class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted = nums.sort()
        left=0
        right=len(nums)-1
        while left<right:
            sum = nums[left] + nums[right]
            if sum ==  target:
                return [left,right]
            elif sum < target:
                left += 1
            else:
                right -= 1

# run solutions
sol1 = Solution1()
sol2 = Solution2()
sol3 = Solution3()

print(sol1.twoSum([0,2,4,5], 6))    
print(sol2.twoSum([0,2,4,5], 6))    
print(sol3.twoSum([0,2,4,5], 6))    
   
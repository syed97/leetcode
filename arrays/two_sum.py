# O(n^2) solution
class Solution:
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

sol1 = Solution()
sol2 = Solution2()

print(sol1.twoSum([0,2,4,5], 6))    
print(sol2.twoSum([0,2,4,5], 6))    
  
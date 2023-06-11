'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# brute force - O(n^2) solution
class Solution1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        prod = 1
        for i in range(len(nums)):
            for k in range(len(nums)):
                if k != i:
                    prod *= nums[k]
            res.append(prod)
            prod = 1
        return res

# using prefix and postfix arrays - O(n) time but O(n) extra memory as we create the 
# new prefix and postfix arrays. We calculate prefix and postfix with the help of running 
# products of the prefix/postfix values and the input array values
class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # create prefix array
        prefix = [1]*len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i]
        print("pre: ", prefix)

        # create postfix array
        postfix = [1]*len(nums)
        postfix[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i]
        print("post: ",postfix)

        out = [1]*len(nums)
        out[0] = postfix[1]
        out[-1] = prefix[-2]
        for i in range(1,len(nums)-1):
            out[i] = prefix[i-1]*postfix[i+1]
        print("out: ", out)
        return out


# O(n) time and O(1) extra memory as we don't create intermediary arrays. instead, we do two passes over
# the input array to caluclate prefix and postfix products
class Solution3:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            out[i] = out[i] * postfix
            postfix *= nums[i]
        return out
    
# similar solutions as those above - copied from a leetcode submission for reference
class Solution4:
    def productExceptSelf1(self, nums: list[int]) -> list[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1] # left[i] 
        print(left)
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        print(right)
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        return result
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        right = 1
        for j in range(len(nums)-2, -1, -1):
            right *= nums[j+1]
            result[j] *= right
        return result


sol = Solution1()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))
nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))

sol = Solution2()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))
nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))

sol = Solution3()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))
nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))

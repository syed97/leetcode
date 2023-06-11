'''
TO DO
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
Return any such subsequence as an integer array of length k.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
'''

def maxSub(nums, k):
    g_sum = 0
    for i in range(k):
        ss = [nums[i]]
        for j in range(i+1,len(nums)):
            ss.append(nums[j])
            print(ss)
            if len(ss) == k:
                break

        #         print("m: ", m)
        #         print(i,j,m)
                # print([nums[j], nums[m]])
    return "done"

nums = [2,1,3,3]; k = 2
print(maxSub(nums, k))           

            
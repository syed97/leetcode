'''
Given an array of positive integers, and a positive number k, find the maximum sum of any contiguous subarray of size k.
Input: [3, 5, 2, 1, 7], k=2
Output: 8
'''

# brute force approach - O(n*k)
def findMaxSum(arr, k):
    window_sum = 0
    total_sum = 0
    for i in range(len(arr)-k+1):
        for j in range(i,i+k):
            window_sum += arr[j]
        if window_sum > total_sum:
            total_sum = window_sum
        window_sum = 0
    return total_sum

# sliding window appraoch - O(n): only have to iterate over input array once.
# The sliding window handles the rest of the sum tracking
def findMaxSumSliding(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # moving and updating sliding window
    for i in range(len(arr)-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)
    return max_sum


# run solutions
arr = [3, 5, 2, 1, 7] 
k=2
print(findMaxSum(arr,k))

arr = [2, 5, 2, -1, 7] 
k=3
print(findMaxSum(arr,k))

arr = [3, 5, 2, 1, 7] 
k=2
print(findMaxSumSliding(arr,k))

arr = [2, 5, 2, -1, 7] 
k=3
print(findMaxSumSliding(arr,k))
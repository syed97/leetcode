# testing out the sliding window algo

# Given an array of positive integers, and a positive number k, find the maximum sum of any contiguous subarray of size k.
# Input: [3, 5, 2, 1, 7], k=2
# Output: 8

def findMaxSum(input, k):
    window_sum = 0
    total_sum = 0
    for i in range(len(input)-k+1):
        window_sum = input[i] + input[i+k-1]
        # print(i, i+k-1)
        # print(input[i], input[i+k-1])
        # print(window_sum)
        if window_sum > total_sum:
            total_sum = window_sum
    return total_sum
    
input = [3, 5, 2, 1, 7]
k = 2

print(findMaxSum(input, k))

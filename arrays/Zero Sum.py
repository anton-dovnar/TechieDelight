'''

Given an integer array, check if it contains a contiguous subarray having zero-sum.

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: True
Explanation: The subarrays with zero-sum are

[3, 4, -7]
[4, -7, 3]
[-7, 3, 1, 3]
[3, 1, -4]
[3, 1, 3, 1, -4, -2, -2]
[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

Input : [4, -7, 1, -2, -1]
Output: False
Explanation: The subarray with zero-sum doesn't exist.

'''

def has_zero_sum_subarray(nums: list[int]) -> bool:
    previous_sums = set()
    current_sum = 0
    
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in previous_sums:
            return True
        previous_sums.add(current_sum)
    return False

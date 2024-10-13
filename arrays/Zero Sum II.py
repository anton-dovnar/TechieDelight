'''

Given an integer array, find all contiguous subarrays with zero-sum.

Input : [4, 2, -3, -1, 0, 4]
Output: {(0), (-3, -1, 0, 4)}

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: {(3, 4, -7, 3, 1, 3, 1, -4, -2, -2), (3, 4, -7), (3, 1, 3, 1, -4, -2, -2), (3, 1, -4), (-7, 3, 1, 3), (4, -7, 3)}

Input : [0, 0]
Output: {(0), (0, 0)}

Input : [1, 2, 3]
Output: {}

Note: Since an input can have multiple subarrays with zero-sum, the solution should return a set of tuples containing all the distinct subarrays.

'''
from collections import defaultdict


def get_all_zero_sum_subarrays(nums: list[int]) -> set[tuple[int]]:
    subarrays = set()
    previous_sums_map = defaultdict(list)
    previous_sums_map[0] = [-1]
    current_sum = 0
    
    for index, num in enumerate(nums):
        current_sum += num
        
        if current_sum in previous_sums_map:
            start_indices = previous_sums_map[current_sum]
            for start_index in start_indices:
                subarray = tuple(nums[start_index + 1 : index + 1])
                subarrays.add(subarray)
                
        previous_sums_map[current_sum].append(index)
        
    return subarrays

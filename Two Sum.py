'''
Given an unsorted integer array, find a pair with the given sum in it.

• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()
'''

from typing import Optional


def find_pair(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    seen_so_far = set()
    for num in nums:
        diff = target - num
        if diff in seen_so_far:
            return diff, num
        seen_so_far.add(num)
    return None

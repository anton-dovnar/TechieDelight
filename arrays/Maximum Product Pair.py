'''

Given an integer array, find a pair with the maximum product in it.

Each input can have multiple solutions. The output should match with either one of them.

Input : [-10, -3, 5, 6, -2]
Output: (-10, -3) or (-3, -10) or (5, 6) or (6, 5)

Input : [-4, 3, 2, 7, -5]
Output: (3, 7) or (7, 3)

If no pair exists, the solution should return an empty tuple.

Input : [1]
Output: ()

'''


def find_pair(nums: list[int]) -> tuple[int, int]:
    if len(nums) < 2:
        return tuple()

    first_max = second_max = float('-inf')
    first_min = second_min = float('inf')

    for num in nums:
        if num > first_max:
            second_max, first_max = first_max, num
        elif num > second_max:
            second_max = num

        if num < first_min:
            second_min, first_min = first_min, num
        elif num < second_min:
            second_min = num

    if second_max == float('-inf') or second_min == float('inf'):
        return tuple()

    return (first_max, second_max) if first_max * second_max > first_min * second_min else (first_min, second_min)

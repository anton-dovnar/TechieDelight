'''

Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

Input : [1, 0, 1, 0, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]

Input : [1, 1]
Output: [1, 1]

'''


def sort_array(nums: list[int]) -> list[int]:
    slow_pointer = 0

    for fast_pointer in range(len(nums)):
        if nums[fast_pointer] == 0:
            nums[slow_pointer] = 0
            slow_pointer += 1

    for i in range(slow_pointer, len(nums)):
        nums[i] = 1

    return nums

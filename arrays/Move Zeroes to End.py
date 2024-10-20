'''

Given an integer array, in-place move all zeros present in it to the end. The solution should maintain the relative order of items in the array and should not use constant space.

Input : [6, 0, 8, 2, 3, 0, 4, 0, 1]
Output: [6, 8, 2, 3, 4, 1, 0, 0, 0]

'''

def rearrange(nums: list[int]) -> None:
    fast_pointer = 1
    slow_pointer = 0

    while fast_pointer < len(nums):
        if nums[slow_pointer] == 0 and nums[fast_pointer] != 0:
            nums[slow_pointer], nums[fast_pointer] = nums[fast_pointer], nums[slow_pointer]
            slow_pointer += 1
        if nums[slow_pointer] != 0:
            slow_pointer += 1
        fast_pointer += 1

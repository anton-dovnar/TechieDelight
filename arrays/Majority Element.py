'''

Given an integer array of size `n`, return the element which appears more than `n/2` times. Assume that the input always contain the majority element.

Input : [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
Output: 2

Input : [1, 3, 1, 1]
Output: 1

'''


def find_majority_element(nums: list[int]) -> int:
    """ Boyer–Moore majority vote algorithm. """

    majority = -1
    count = 0

    for num in nums:
        if count == 0:
            majority = num

        count += 1 if num == majority else -1

    return majority

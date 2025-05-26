from typing import List

class Solution:
    """
    LeetCode 16: 3Sum Closest

    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.

    The approach is similar to 3Sum:
      - Sort the array.
      - For each index, use two pointers to find the closest sum for the remaining two numbers.
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        result = 0

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < closest:
                    closest = abs(curr_sum - target)
                    result = curr_sum
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum  # Exact match

        return result
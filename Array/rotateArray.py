from typing import List

class Solution:
    """
    LeetCode 189: Rotate Array

    Given an array, rotate the array to the right by k steps, where k is non-negative.

    The solution uses array reversal to achieve O(1) extra space and O(n) time.
    """

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # In case k > n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse the whole array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the rest
        reverse(k, n - 1)
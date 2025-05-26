from typing import List
from collections import deque

class Solution:
    """
    LeetCode 239: Sliding Window Maximum

    Given an array nums and an integer k, find the maximum value in each sliding window of size k.

    The solution uses a deque to store indices of useful elements for each window.
    The deque always stores indices in decreasing order of their corresponding values in nums.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # Stores indices

        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()
            # Remove indices whose corresponding values are less than nums[i]
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            # The front of the deque is the max in the current window
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
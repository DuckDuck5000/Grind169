from typing import List

class Solution:
    """
    LeetCode 525: Contiguous Array

    Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

    The solution uses a hash map to store the first occurrence of each count difference (0s - 1s).
    """

    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        count_index = {0: -1}  # count: first index

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_index:
                max_len = max(max_len, i - count_index[count])
            else:
                count_index[count] = i
        return max_len
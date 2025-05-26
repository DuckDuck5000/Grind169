from typing import List

class Solution:
    """
    LeetCode 128: Longest Consecutive Sequence

    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    The algorithm should run in O(n) time.

    The solution uses a set to allow O(1) lookups and expands from each number only if it's the start of a sequence.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if 'num' is the start of a sequence
            if num - 1 not in num_set:
                length = 1
                current = num
                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest
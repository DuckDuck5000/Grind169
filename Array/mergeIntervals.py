from typing import List

class Solution:
    """
    LeetCode 56: Merge Intervals

    Given an array of intervals where intervals[i] = [start, end],
    merge all overlapping intervals and return an array of the merged intervals.
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                # Overlapping intervals, merge them
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged
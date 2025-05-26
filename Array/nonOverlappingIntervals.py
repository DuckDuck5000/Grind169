from typing import List

class Solution:
    """
    LeetCode 435: Non-overlapping Intervals

    Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

    The solution sorts intervals by end time and uses a greedy approach to count overlaps.
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                count += 1  # Overlap, need to remove this interval
            else:
                prev_end = intervals[i][1]  # No overlap, update end

        return count
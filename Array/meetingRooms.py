from typing import List

class Solution:
    """
    LeetCode 252: Meeting Rooms

    Given an array of meeting time intervals consisting of start and end times,
    determine if a person could attend all meetings (no overlaps).

    Return True if a person can attend all meetings, otherwise False.
    """

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            # If the current meeting starts before the previous one ends, return False
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
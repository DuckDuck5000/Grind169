from typing import List
import heapq

class Solution:
    """
    LeetCode 253: Meeting Rooms II

    Given an array of meeting time intervals consisting of start and end times,
    find the minimum number of conference rooms required.

    **Difference from Meeting Rooms I:**
    - Meeting Rooms I asks if a person can attend all meetings (i.e., are there any overlaps?).
    - Meeting Rooms II asks for the minimum number of rooms needed to accommodate all meetings (i.e., what is the maximum number of overlapping meetings at any time?).

    The solution uses a min-heap to track the end times of ongoing meetings.
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort meetings by start time
        intervals.sort(key=lambda x: x[0])
        # Min-heap to track the earliest end time
        heap = []

        for interval in intervals:
            # If the room due to free up the earliest is free, reuse it
            if heap and interval[0] >= heap[0]:
                heapq.heappop(heap)
            # Add the current meeting's end time to the heap
            heapq.heappush(heap, interval[1])

        # The size of the heap is the number of rooms needed
        return len(heap)
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
    
# ...existing code...

def test_erase_overlap_intervals():
    solution = Solution()
    
    # Test case 1: Basic overlapping intervals
    assert solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    
    # Test case 2: Multiple overlapping intervals
    assert solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
    
    # Test case 3: No overlapping intervals
    assert solution.eraseOverlapIntervals([[1,2],[2,3],[3,4]]) == 0
    
    # Test case 4: Empty input
    assert solution.eraseOverlapIntervals([]) == 0
    
    # Test case 5: Single interval
    assert solution.eraseOverlapIntervals([[1,2]]) == 0
    
    # Test case 6: Complex overlapping case
    assert solution.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) == 2
    
    # Test case 7: Negative numbers
    assert solution.eraseOverlapIntervals([[-3,0],[-2,1],[-1,2]]) == 1
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_erase_overlap_intervals()
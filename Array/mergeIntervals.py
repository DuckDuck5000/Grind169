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
    
# ...existing code...

def test_merge_intervals():
    solution = Solution()
    
    # Test case 1: Basic overlapping intervals
    assert solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    
    # Test case 2: Completely overlapping intervals
    assert solution.merge([[1,4],[4,5],[2,3]]) == [[1,5]]
    
    # Test case 3: No overlapping intervals
    assert solution.merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]
    
    # Test case 4: Single interval
    assert solution.merge([[1,1]]) == [[1,1]]
    
    # Test case 5: Empty input
    assert solution.merge([]) == []
    
    # Test case 6: Multiple overlapping intervals
    assert solution.merge([[1,4],[4,5],[2,3],[3,6]]) == [[1,6]]
    
    # Test case 7: Intervals with negative numbers
    assert solution.merge([[-2,3],[-1,2],[1,4]]) == [[-2,4]]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_merge_intervals()

from typing import List
class Solution:
    """
    LeetCode 84: Largest Rectangle in Histogram
    
    Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
    return the area of the largest rectangle in the histogram.
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # pairs: (index, height)
        max_area = 0
        
        # Process all bars, including a virtual bar of height 0 at the end
        for i, h in enumerate(heights + [0]):
            start = i
            
            # Pop taller bars and calculate their areas
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                area = width * height
                max_area = max(max_area, area)
                start = index
                
            # Push current bar with the earliest possible start position
            stack.append((start, h))
            
        return max_area
    
def test_largest_rectangle():
    solution = Solution()
    
    # Test case 1: Regular histogram
    assert solution.largestRectangleArea([2,1,5,6,2,3]) == 10
    
    # Test case 2: Ascending heights
    assert solution.largestRectangleArea([1,2,3,4,5]) == 9
    
    # Test case 3: Descending heights
    assert solution.largestRectangleArea([5,4,3,2,1]) == 9
    
    # Test case 4: All same height
    assert solution.largestRectangleArea([2,2,2,2]) == 8
    
    # Test case 5: Single bar
    assert solution.largestRectangleArea([1]) == 1
    
    # Test case 6: Empty histogram
    assert solution.largestRectangleArea([]) == 0
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_rectangle()

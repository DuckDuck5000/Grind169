from typing import List

class Solution:
    """
    LeetCode 11: Container With Most Water

    Given n non-negative integers a1, a2, ..., an where each represents a point at coordinate (i, ai),
    n vertical lines are drawn such that the two endpoints of the line i is at (i, ai).
    Find two lines, which together with the x-axis forms a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    The optimal solution uses the two-pointer technique.
    """

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area between the two pointers
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
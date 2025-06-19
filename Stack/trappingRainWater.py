class Solution:
    """
    LeetCode 42: Trapping Rain Water
    
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.
    
    Solution uses two pointers approach:
    - Keep track of left_max and right_max heights
    - For each position, water trapped = min(left_max, right_max) - height[i]
    """
    
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        
        while left < right:
            # Update the maximum heights seen from left and right
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # If left wall is smaller, calculate water for left pointer
            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            # If right wall is smaller, calculate water for right pointer
            else:
                water += right_max - height[right]
                right -= 1
                
        return water
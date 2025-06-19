"""
Partition Equal Subset Sum

Problem Description:
------------------
Given an integer array nums, return true if you can partition the array into two subsets
such that the sum of elements in both subsets is equal.

Examples:
--------
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: Array can be partitioned into [1,5,5] and [11]

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: Array cannot be partitioned into equal sum subsets

Approach:
--------
1. If total sum is odd, return false (can't partition equally)
2. Use dynamic programming to find if subset sum equals total_sum/2
3. dp[i][j] represents if sum j can be achieved using first i numbers
4. Time Complexity: O(n * target) where target = sum(nums)/2
5. Space Complexity: O(target) using optimized 1D DP array
"""

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # If sum is odd, can't partition equally
        if total_sum % 2:
            return False
        
        target = total_sum // 2
        dp = set([0])
        
        for num in nums:
            # Add num to all existing sums
            next_dp = dp.copy()
            for t in dp:
                next_dp.add(t + num)
            dp = next_dp
            
            # Early return if target found
            if target in dp:
                return True
        
        return target in dp

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Can be partitioned
    nums1 = [1,5,11,5]
    assert solution.canPartition(nums1) == True, "Test case 1 failed"
    
    # Test case 2: Cannot be partitioned
    nums2 = [1,2,3,5]
    assert solution.canPartition(nums2) == False, "Test case 2 failed"
    
    # Test case 3: Single element (cannot be partitioned)
    nums3 = [1]
    assert solution.canPartition(nums3) == False, "Test case 3 failed"
    
    # Test case 4: Equal numbers
    nums4 = [1,1]
    assert solution.canPartition(nums4) == True, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
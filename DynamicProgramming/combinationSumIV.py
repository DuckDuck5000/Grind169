"""
Combination Sum IV

Problem Description:
------------------
Given an array of distinct integers nums and a target integer target, return the number
of possible combinations that add up to target. The order of integers in each combination
matters (different sequences are counted separately).

Examples:
--------
Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation: The possible combinations are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Example 2:
Input: nums = [9], target = 3
Output: 0

Approach:
--------
1. Use dynamic programming bottom-up approach
2. dp[i] represents number of combinations that sum to i
3. For each target sum i, try adding each number from nums
4. Time Complexity: O(target * len(nums))
5. Space Complexity: O(target)
"""

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # Initialize dp array with 0s
        dp = [0] * (target + 1)
        dp[0] = 1  # Empty combination
        
        # For each sum from 1 to target
        for curr_sum in range(1, target + 1):
            # Try adding each number from nums
            for num in nums:
                if curr_sum >= num:
                    dp[curr_sum] += dp[curr_sum - num]
        
        return dp[target]

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Multiple combinations
    nums1 = [1,2,3]
    target1 = 4
    assert solution.combinationSum4(nums1, target1) == 7, "Test case 1 failed"
    
    # Test case 2: No possible combinations
    nums2 = [9]
    target2 = 3
    assert solution.combinationSum4(nums2, target2) == 0, "Test case 2 failed"
    
    # Test case 3: Single number, exact target
    nums3 = [1]
    target3 = 1
    assert solution.combinationSum4(nums3, target3) == 1, "Test case 3 failed"
    
    # Test case 4: Multiple numbers, small target
    nums4 = [1,2,3]
    target4 = 2
    assert solution.combinationSum4(nums4, target4) == 2, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
"""
Maximum Subarray

Problem Description:
------------------
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Examples:
--------
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Approach:
--------
1. Use Kadane's Algorithm
2. Keep track of current sum and maximum sum
3. At each position, decide whether to:
   - Start new subarray (current number)
   - Extend existing subarray (current sum + number)
4. Time Complexity: O(n)
5. Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize variables
        curr_sum = max_sum = nums[0]
        
        # Iterate through array starting from second element
        for num in nums[1:]:
            # Either extend previous subarray or start new one
            curr_sum = max(num, curr_sum + num)
            # Update maximum sum if current sum is larger
            max_sum = max(max_sum, curr_sum)
            
        return max_sum

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Mixed positive and negative numbers
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    assert solution.maxSubArray(nums1) == 6, "Test case 1 failed"
    
    # Test case 2: Single element
    nums2 = [1]
    assert solution.maxSubArray(nums2) == 1, "Test case 2 failed"
    
    # Test case 3: All positive numbers
    nums3 = [5,4,-1,7,8]
    assert solution.maxSubArray(nums3) == 23, "Test case 3 failed"
    
    # Test case 4: All negative numbers
    nums4 = [-2,-1,-3,-4]
    assert solution.maxSubArray(nums4) == -1, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
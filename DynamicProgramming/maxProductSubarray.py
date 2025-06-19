"""
Maximum Product Subarray

Problem Description:
------------------
Given an integer array nums, find a subarray that has the largest product, and return
the product.

Examples:
--------
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Approach:
--------
1. Keep track of both maximum and minimum products ending at current position
2. Minimum product is needed because negative * negative = positive
3. At each step, consider:
   - Current number alone
   - Current number * previous max
   - Current number * previous min
4. Time Complexity: O(n)
5. Space Complexity: O(1)
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        curr_max = curr_min = result = nums[0]
        
        for num in nums[1:]:
            # Store previous max for use in min calculation
            temp_max = curr_max
            
            # Calculate new max and min
            curr_max = max(num, max(curr_max * num, curr_min * num))
            curr_min = min(num, min(temp_max * num, curr_min * num))
            
            # Update global maximum
            result = max(result, curr_max)
        
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular case with positive and negative numbers
    nums1 = [2,3,-2,4]
    assert solution.maxProduct(nums1) == 6, "Test case 1 failed"
    
    # Test case 2: All negative numbers
    nums2 = [-2,0,-1]
    assert solution.maxProduct(nums2) == 0, "Test case 2 failed"
    
    # Test case 3: Single element
    nums3 = [-3]
    assert solution.maxProduct(nums3) == -3, "Test case 3 failed"
    
    # Test case 4: Contains zeros
    nums4 = [-2,3,-4,0,5,-6]
    assert solution.maxProduct(nums4) == 24, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
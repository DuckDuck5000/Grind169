"""
First Missing Positive

Problem Description:
------------------
Given an unsorted integer array nums, return the smallest missing positive integer.
Must run in O(n) time and use O(1) auxiliary space.

Examples:
--------
Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: Numbers 1 and 2 are present, so 3 is the first missing positive

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is present, 2 is missing, so 2 is the answer

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: 1 is missing, so it's the answer

Approach:
--------
1. Use array as its own hash table
2. Mark presence of number i at index i-1
3. Scan array for first position where value doesn't match position
4. Time Complexity: O(n)
5. Space Complexity: O(1)
"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Modify the array to ignore non-positive and numbers > n
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Step 2: Mark presence of each number in its correct position
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                # Mark presence by making number at index (num-1) negative
                nums[num - 1] = -abs(nums[num - 1])
        
        # Step 3: Find first positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all numbers 1 to n exist, return n + 1
        return n + 1

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Missing number in middle
    nums1 = [3,4,-1,1]
    assert solution.firstMissingPositive(nums1) == 2, "Test case 1 failed"
    
    # Test case 2: Missing first positive
    nums2 = [7,8,9,11,12]
    assert solution.firstMissingPositive(nums2) == 1, "Test case 2 failed"
    
    # Test case 3: No missing number until end
    nums3 = [1,2,3]
    assert solution.firstMissingPositive(nums3) == 4, "Test case 3 failed"
    
    # Test case 4: Array with duplicates
    nums4 = [1,1]
    assert solution.firstMissingPositive(nums4) == 2, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
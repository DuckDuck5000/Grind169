"""
Subsets

Problem Description:
------------------
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
--------
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Approach:
--------
1. Use backtracking to generate all subsets
2. For each number, we have two choices:
   - Include it in current subset
   - Skip it and move to next number
3. Time Complexity: O(2^n)
4. Space Complexity: O(n) for recursion stack
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, curr: List[int]) -> None:
            # Add current subset to result
            result.append(curr[:])
            
            # Try including each remaining number
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        result = []
        backtrack(0, [])
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Three numbers
    nums1 = [1,2,3]
    result1 = solution.subsets(nums1)
    assert len(result1) == 8, "Test case 1 failed: wrong number of subsets"
    assert [] in result1, "Test case 1 failed: missing empty subset"
    assert [1,2,3] in result1, "Test case 1 failed: missing full set"
    
    # Test case 2: Single number
    nums2 = [0]
    result2 = solution.subsets(nums2)
    assert result2 == [[],[0]], "Test case 2 failed"
    
    # Test case 3: Empty array
    nums3 = []
    result3 = solution.subsets(nums3)
    assert result3 == [[]], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
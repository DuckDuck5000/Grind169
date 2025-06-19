"""
Permutations

Problem Description:
------------------
Given an array nums of distinct integers, return all possible permutations.
You can return the answer in any order.

Examples:
--------
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Approach:
--------
1. Use backtracking to generate all permutations
2. For each position, try all available numbers
3. Track used numbers to avoid duplicates
4. Time Complexity: O(n!)
5. Space Complexity: O(n) for recursion stack
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path: List[int], used: set) -> None:
            # Base case: path length equals nums length
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            # Try each number
            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)
                    backtrack(path, used)
                    path.pop()
                    used.remove(num)
        
        result = []
        backtrack([], set())
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Three numbers
    nums1 = [1,2,3]
    result1 = solution.permute(nums1)
    assert len(result1) == 6, "Test case 1 failed: wrong number of permutations"
    assert all(sorted(p) == [1,2,3] for p in result1), "Test case 1 failed: invalid permutations"
    
    # Test case 2: Two numbers
    nums2 = [0,1]
    result2 = solution.permute(nums2)
    assert len(result2) == 2, "Test case 2 failed: wrong number of permutations"
    assert all(sorted(p) == [0,1] for p in result2), "Test case 2 failed: invalid permutations"
    
    # Test case 3: Single number
    nums3 = [1]
    result3 = solution.permute(nums3)
    assert result3 == [[1]], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
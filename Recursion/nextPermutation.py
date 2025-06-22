"""
Next Permutation

Problem Description:
------------------
Implement next permutation, which rearranges numbers into the lexicographically next 
greater permutation of numbers. If such arrangement is not possible, it must rearrange 
it as the lowest possible order (i.e., sorted in ascending order).

Examples:
--------
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Approach:
--------
1. Find first pair from right where nums[i] < nums[i+1]
2. Find smallest number larger than nums[i] from right
3. Swap these numbers
4. Reverse suffix starting from i+1
5. Time Complexity: O(n)
6. Space Complexity: O(1)
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        inversionPoint = len(nums)-2
        
        while inversionPoint >= 0 and nums[inversionPoint] >= nums[inversionPoint+1]:
            inversionPoint -= 1
        
        if inversionPoint != -1:
            for i in reversed(range(inversionPoint+1, len(nums))):
            
                if nums[i] > nums[inversionPoint]:
                
                    nums[inversionPoint], nums[i] = nums[i], nums[inversionPoint]
                    break
        nums[inversionPoint +1 :] = reversed(nums[inversionPoint + 1:])
            

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular case
    nums1 = [1,2,3]
    solution.nextPermutation(nums1)
    assert nums1 == [1,3,2], "Test case 1 failed"
    
    # Test case 2: Descending order
    nums2 = [3,2,1]
    solution.nextPermutation(nums2)
    assert nums2 == [1,2,3], "Test case 2 failed"
    
    # Test case 3: With duplicates
    nums3 = [1,1,5]
    solution.nextPermutation(nums3)
    assert nums3 == [1,5,1], "Test case 3 failed"
    
    # Test case 4: Single element
    nums4 = [1]
    solution.nextPermutation(nums4)
    assert nums4 == [1], "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()

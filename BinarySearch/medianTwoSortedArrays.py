"""
Median of Two Sorted Arrays

Problem Description:
------------------
Given two sorted arrays nums1 and nums2 of sizes m and n respectively, find the median 
of the two sorted arrays.

The overall run time complexity should be O(log(m+n)).

Examples:
--------
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0
Explanation: Merged array = [1,2,3], median is 2

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
Explanation: Merged array = [1,2,3,4], median is (2 + 3)/2 = 2.5

Approach:
--------
1. Use binary search on smaller array
2. Find partition points that divide arrays into left and right halves
3. Compare elements around partition points
4. Time Complexity: O(log(min(m,n)))
5. Space Complexity: O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partition points
            partitionX = (left + right) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            # Get elements around partition points
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we found the right partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # If total length is even
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            
            # Adjust partition
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1
                
        raise ValueError("Input arrays are not sorted")

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Odd total length
    assert solution.findMedianSortedArrays(
        [1,3],
        [2]
    ) == 2.0, "Test case 1 failed"
    
    # Test case 2: Even total length
    assert solution.findMedianSortedArrays(
        [1,2],
        [3,4]
    ) == 2.5, "Test case 2 failed"
    
    # Test case 3: One empty array
    assert solution.findMedianSortedArrays(
        [],
        [1]
    ) == 1.0, "Test case 3 failed"
    
    # Test case 4: Arrays with different sizes
    assert solution.findMedianSortedArrays(
        [1,2,3,4,5],
        [6,7,8]
    ) == 4.5, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
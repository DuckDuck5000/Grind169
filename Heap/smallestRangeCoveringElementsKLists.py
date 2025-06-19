"""
Smallest Range Covering Elements from K Lists

Problem Description:
------------------
You have k lists of sorted integers. Find the smallest range that includes at least 
one number from each of the k lists.

Examples:
--------
Example 1:
Input: nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4,10,15,24,26], 24 is in range [20,24]
List 2: [0,9,12,20], 20 is in range [20,24]
List 3: [5,18,22,30], 22 is in range [20,24]

Example 2:
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

Approach:
--------
1. Use min heap to track smallest elements from each list
2. Track current maximum among heap elements
3. Update range when finding smaller difference
4. Time Complexity: O(N * log(k)) where N is total elements, k is number of lists
5. Space Complexity: O(k)
"""

import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize heap with first element from each list
        heap = [(row[0], i, 0) for i, row in enumerate(nums) if row]
        heapq.heapify(heap)
        
        # Initialize range
        range_start = float('-inf')
        range_end = float('inf')
        current_max = max(row[0] for row in nums if row)
        
        while heap:
            # Get minimum element
            current_min, list_index, num_index = heapq.heappop(heap)
            
            # Update range if current range is smaller
            if current_max - current_min < range_end - range_start:
                range_start = current_min
                range_end = current_max
            
            # If any list is exhausted, we're done
            if num_index + 1 >= len(nums[list_index]):
                break
                
            # Add next element from the same list
            next_num = nums[list_index][num_index + 1]
            current_max = max(current_max, next_num)
            heapq.heappush(heap, (next_num, list_index, num_index + 1))
        
        return [range_start, range_end]

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular case
    nums1 = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    assert solution.smallestRange(nums1) == [20,24], "Test case 1 failed"
    
    # Test case 2: All lists same
    nums2 = [[1,2,3],[1,2,3],[1,2,3]]
    assert solution.smallestRange(nums2) == [1,1], "Test case 2 failed"
    
    # Test case 3: Single element lists
    nums3 = [[1],[2],[3]]
    assert solution.smallestRange(nums3) == [1,3], "Test case 3 failed"
    
    # Test case 4: Two lists
    nums4 = [[1,2,3],[4,5,6]]
    assert solution.smallestRange(nums4) == [3,4], "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
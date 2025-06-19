from typing import List
from collections import deque

class Solution:
    """
    LeetCode 239: Sliding Window Maximum

    Given an array nums and an integer k, find the maximum value in each sliding window of size k.

    The solution uses a deque to store indices of useful elements for each window.
    The deque always stores indices in decreasing order of their corresponding values in nums.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # Stores indices

        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()
            # Remove indices whose corresponding values are less than nums[i]
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            # The front of the deque is the max in the current window
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result

def test_sliding_window_maximum():
    solution = Solution()
    
    # Test case 1: Basic sliding window
    assert solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    
    # Test case 2: Window size equals array length
    assert solution.maxSlidingWindow([1,2,3,4], 4) == [4]
    
    # Test case 3: Window size 1
    assert solution.maxSlidingWindow([1,2,3], 1) == [1,2,3]
    
    # Test case 4: Decreasing sequence
    assert solution.maxSlidingWindow([7,6,5,4], 2) == [7,6,5]
    
    # Test case 5: Increasing sequence
    assert solution.maxSlidingWindow([1,2,3,4,5], 3) == [3,4,5]
    
    # Test case 6: Array with negative numbers
    assert solution.maxSlidingWindow([-7,2,4,-1], 2) == [2,4,4]
    
    # Test case 7: Array with duplicates
    assert solution.maxSlidingWindow([1,1,1,1], 2) == [1,1,1]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_sliding_window_maximum()
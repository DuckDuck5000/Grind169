from typing import List

class Solution:
    """
    LeetCode 128: Longest Consecutive Sequence

    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    The algorithm should run in O(n) time.

    The solution uses a set to allow O(1) lookups and expands from each number only if it's the start of a sequence.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if 'num' is the start of a sequence
            if num - 1 not in num_set:
                length = 1
                current = num
                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest
    

# ...existing code...

def test_longest_consecutive():
    solution = Solution()
    
    # Test case 1: Basic sequence
    assert solution.longestConsecutive([100,4,200,1,3,2]) == 4  # [1,2,3,4]
    
    # Test case 2: Multiple sequences
    assert solution.longestConsecutive([1,2,0,1,3,4,7,8,9]) == 5  # [0,1,2,3]
    
    # Test case 3: Empty array
    assert solution.longestConsecutive([]) == 0
    
    # Test case 4: Single element
    assert solution.longestConsecutive([1]) == 1
    
    # Test case 5: Duplicate elements
    assert solution.longestConsecutive([1,2,2,3,4]) == 4  # [1,2,3,4]
    
    # Test case 6: Negative numbers
    assert solution.longestConsecutive([-5,-4,-3,1,2,3]) == 3  # [-5,-4,-3]
    
    print("All test cases passed!")

if __name__ == "__main__":
    print("Testing longest consecutive sequence...")
    test_longest_consecutive()
    print("All tests passed!")py
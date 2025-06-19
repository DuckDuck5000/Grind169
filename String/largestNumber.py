from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert to strings for easier comparison
        str_nums = [str(num) for num in nums]
        
        # Custom comparator
        def compare(a: str, b: str) -> int:
            # Compare which concatenation gives larger number
            if a + b > b + a:
                return -1    # a should come before b
            elif a + b < b + a:
                return 1     # b should come before a
            else:
                return 0     # order doesn't matter
        
        # Sort using custom comparator
        str_nums.sort(key=cmp_to_key(compare))
        
        # Handle edge case of all zeros
        if str_nums[0] == '0':
            return '0'
            
        # Join the sorted strings
        return ''.join(str_nums)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular numbers
    nums1 = [10,2]
    print(f"Test 1: {nums1}")
    print(f"Result: {solution.largestNumber(nums1)}")  # Expected: "210"
    
    # Test Case 2: Numbers with multiple digits
    nums2 = [3,30,34,5,9]
    print(f"\nTest 2: {nums2}")
    print(f"Result: {solution.largestNumber(nums2)}")  # Expected: "9534330"
    
    # Test Case 3: Array with zeros
    nums3 = [0,0]
    print(f"\nTest 3: {nums3}")
    print(f"Result: {solution.largestNumber(nums3)}")  # Expected: "0"
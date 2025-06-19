class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        # If array is not rotated
        if nums[right] > nums[left]:
            return nums[0]
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if mid is the minimum
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # Check if mid + 1 is the minimum
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # Decide which half to search
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[0]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Regular rotated array
    nums1 = [3,4,5,1,2]
    result1 = solution.findMin(nums1)
    assert result1 == 1, f"Expected 1 but got {result1}"
    
    # Test case 2: Not rotated array
    nums2 = [1,2,3,4,5]
    result2 = solution.findMin(nums2)
    assert result2 == 1, f"Expected 1 but got {result2}"
    
    # Test case 3: Array with repeated elements at rotation point
    nums3 = [4,5,6,7,0,1,2]
    result3 = solution.findMin(nums3)
    assert result3 == 0, f"Expected 0 but got {result3}"
    
    # Test case 4: Single element array
    nums4 = [1]
    result4 = solution.findMin(nums4)
    assert result4 == 1, f"Expected 1 but got {result4}"
    
    print("All test cases passed!")
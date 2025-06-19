class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                # Check if target is in right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Regular rotated array
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    result1 = solution.search(nums1, target1)
    assert result1 == 4, f"Expected 4 but got {result1}"
    
    # Test case 2: Target not found
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    result2 = solution.search(nums2, target2)
    assert result2 == -1, f"Expected -1 but got {result2}"
    
    # Test case 3: Single element array
    nums3 = [1]
    target3 = 1
    result3 = solution.search(nums3, target3)
    assert result3 == 0, f"Expected 0 but got {result3}"
    
    # Test case 4: Not rotated array
    nums4 = [1,2,3,4,5]
    target4 = 3
    result4 = solution.search(nums4, target4)
    assert result4 == 2, f"Expected 2 but got {result4}"
    
    # Test case 5: Empty array
    nums5 = []
    target5 = 5
    result5 = solution.search(nums5, target5)
    assert result5 == -1, f"Expected -1 but got {result5}"
    
    print("All test cases passed!")
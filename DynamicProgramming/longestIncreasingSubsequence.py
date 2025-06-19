class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        # sub array stores the smallest number for each length
        sub = [nums[0]]
        
        for num in nums[1:]:
            if num > sub[-1]:
                # If current number is larger than all elements, append it
                sub.append(num)
            else:
                # Binary search to find the insertion position
                left, right = 0, len(sub) - 1
                while left < right:
                    mid = (left + right) // 2
                    if sub[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                # Replace the first element larger than or equal to num
                sub[left] = num
                
        return len(sub)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = set()
        nums.sort()
        for i in range(0, len(nums)):
            j = i +1 
            k = len(nums)-1
            
            while j < k:
                
                target = nums[i] + nums[j]
                
                if target + nums[k] == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif target + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
            
        return output
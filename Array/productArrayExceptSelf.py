class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = 1
        for i in range(0, len(nums)):
            output.append(prod)
            prod *= nums[i]
        prod = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= prod
            prod *= nums[j]
        return output
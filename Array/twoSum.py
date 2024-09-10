class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)
        for index, val in enumerate(nums):
            comp = target-val
            if comp in hashMap: return [index, hashMap[comp]]
            hashMap[val] = index
        return [-1, -1]
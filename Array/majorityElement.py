class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        for key, val in counts.items():
            if val > n // 2: return key
        return -1
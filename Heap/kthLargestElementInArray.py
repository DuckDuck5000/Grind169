class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
        while k > 0:
            num = heappop(heap)
            k -= 1
        return -1*num
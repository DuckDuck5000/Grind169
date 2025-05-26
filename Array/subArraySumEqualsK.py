from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1

        for num in nums:
            curr_sum += num
            count += sum_freq[curr_sum - k]
            sum_freq[curr_sum] += 1

        return count
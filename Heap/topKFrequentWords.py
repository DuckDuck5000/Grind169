class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        output = []
        for key, val in Counter(words).items():
            heapq.heappush(heap, [-1*val, key])
        while k > 0:
            output.append(heapq.heappop(heap)[1])
            k -= 1
        return output
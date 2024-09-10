class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        heap = []
        for x, y in points:
            dis = sqrt(x**2 + y**2)
            heapq.heappush(heap, [dis, [x,y]])
        while k > 0:
            dis, points = heapq.heappop(heap)
            output.append(points)
            k -= 1
        return output
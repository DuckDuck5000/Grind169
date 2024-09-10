class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        output = []
        heap = []
        for num in arr:
            heapq.heappush(heap, [abs(num-x), num])
        while k > 0:
            k -= 1
            output.append(heapq.heappop(heap)[1])
        return sorted(output)
## Binary search is faster way

class Solution:
    def findClosestElements(self, A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) / 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]
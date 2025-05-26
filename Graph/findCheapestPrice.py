from typing import List
import heapq
from collections import defaultdict

class Solution:
    """
    LeetCode 787: Cheapest Flights Within K Stops

    Find the cheapest price from src to dst with at most k stops.
    """

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))

        heap = [(0, src, 0)]  # (cost, city, stops)
        visited = dict()  # (city, stops): cost

        while heap:
            cost, city, stops = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops > k:
                continue
            # Only proceed if this is the best (fewest stops) we've seen for this city
            if (city, stops) in visited and visited[(city, stops)] <= cost:
                continue
            visited[(city, stops)] = cost
            for neighbor, price in adj[city]:
                heapq.heappush(heap, (cost + price, neighbor, stops + 1))
        return -1
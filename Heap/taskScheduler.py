"""
Task Scheduler - Heap Solution

Problem Description:
------------------
Given tasks and cooling period n, schedule tasks with minimum intervals.
Uses max heap to always process most frequent tasks first.

Approach:
--------
1. Use max heap to track task frequencies
2. Use queue to track cooling tasks
3. Process most frequent tasks first
4. Time Complexity: O(N * log(26)) where N is number of tasks
5. Space Complexity: O(1) for heap and queue
"""

from collections import Counter
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Count frequencies and create max heap
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        cooling = deque()  # (count, available_time)
        
        while max_heap or cooling:
            # Increment time
            time += 1
            
            # Process task from heap if available
            if max_heap:
                count = heapq.heappop(max_heap) + 1  # Add 1 because using negative
                if count < 0:
                    cooling.append((count, time + n))
            
            # Check if any cooling tasks can be added back to heap
            if cooling and cooling[0][1] == time:
                heapq.heappush(max_heap, cooling.popleft()[0])
                
        return time

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular case with cooling
    tasks1 = ["A","A","A","B","B","B"]
    n1 = 2
    assert solution.leastInterval(tasks1, n1) == 8, "Test case 1 failed"
    
    # Test case 2: No cooling needed
    tasks2 = ["A","A","A","B","B","B"]
    n2 = 0
    assert solution.leastInterval(tasks2, n2) == 6, "Test case 2 failed"
    
    # Test case 3: Single task repeated
    tasks3 = ["A","A","A"]
    n3 = 1
    assert solution.leastInterval(tasks3, n3) == 5, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
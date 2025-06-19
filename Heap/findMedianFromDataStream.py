"""
Find Median from Data Stream

Problem Description:
------------------
Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object
- void addNum(int num) adds the integer num from the data stream to the data structure
- double findMedian() returns the median of all elements so far

Examples:
--------
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0

Approach:
--------
1. Use two heaps: max heap for lower half, min heap for upper half
2. Keep heaps balanced or max heap one element larger
3. Time Complexity: O(log n) for addNum, O(1) for findMedian
4. Space Complexity: O(n)
"""

import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for lower half (multiply by -1 to simulate max heap)
        self.small = []
        # Min heap for upper half
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to max heap first
        heapq.heappush(self.small, -num)
        
        # Ensure all elements in small <= large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If odd number of elements
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If even number of elements
        return (-self.small[0] + self.large[0]) / 2

def run_tests():
    """Test cases with assertions"""
    medianFinder = MedianFinder()
    
    # Test case 1: Adding numbers and finding median
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.5, "Test case 1 failed"
    
    # Test case 2: Adding more numbers
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2.0, "Test case 2 failed"
    
    # Test case 3: Adding number smaller than median
    medianFinder.addNum(0)
    assert medianFinder.findMedian() == 1.5, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
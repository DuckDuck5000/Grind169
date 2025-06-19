"""
Maximum Profit in Job Scheduling

Problem Description:
------------------
Given n jobs where each job has a start time, end time, and profit. Find the maximum profit 
you can get by scheduling non-overlapping jobs.

Examples:
--------
Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: Schedule jobs 1 and 4 (50 + 70 = 120)

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: Schedule jobs 1, 3, and 5 (20 + 100 + 60 = 150)

Approach:
--------
1. Sort jobs by end time
2. Use binary search to find non-overlapping jobs
3. Use dynamic programming to track maximum profit
4. Time Complexity: O(nlogn)
5. Space Complexity: O(n)
"""

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        n = len(startTime)
        # Create list of jobs and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # dp[i] represents maximum profit up to index i
        dp = [0] * n
        
        # Base case: first job
        dp[0] = jobs[0][2]  # profit of first job
        
        for i in range(1, n):
            # Current job's profit
            current_profit = jobs[i][2]
            
            # Find latest non-overlapping job using binary search
            prev_job = self.find_last_non_overlapping_job(jobs, i)
            
            # Add profit from previous non-overlapping job if exists
            if prev_job != -1:
                current_profit += dp[prev_job]
            
            # Maximum profit is either including current job or excluding it
            dp[i] = max(current_profit, dp[i-1])
            
        return dp[-1]
    
    def find_last_non_overlapping_job(self, jobs: list[tuple], current_idx: int) -> int:
        current_start = jobs[current_idx][0]
        left, right = 0, current_idx - 1
        last_valid = -1
        
        while left <= right:
            mid = (left + right) // 2
            if jobs[mid][1] <= current_start:  # Non-overlapping job found
                last_valid = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return last_valid

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular case
    assert solution.jobScheduling(
        [1,2,3,3],
        [3,4,5,6],
        [50,10,40,70]
    ) == 120, "Test case 1 failed"
    
    # Test case 2: All jobs overlap
    assert solution.jobScheduling(
        [1,2,3,4,6],
        [3,5,10,6,9],
        [20,20,100,70,60]
    ) == 150, "Test case 2 failed"
    
    # Test case 3: Single job
    assert solution.jobScheduling(
        [1],
        [2],
        [5]
    ) == 5, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
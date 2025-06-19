class Solution:
    def climbStairs(self, n: int) -> int:
        # Handle base cases
        if n <= 2:
            return n
        
        # Initialize dp array
        dp = [0] * (n + 1)
        dp[1] = 1  # One way to climb 1 stair
        dp[2] = 2  # Two ways to climb 2 stairs
        
        # Fill dp array
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: n = 2
    assert solution.climbStairs(2) == 2, "Test case 1 failed"
    
    # Test case 2: n = 3
    assert solution.climbStairs(3) == 3, "Test case 2 failed"
    
    # Test case 3: n = 4
    assert solution.climbStairs(4) == 5, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
"""
Coin Change

Problem Description:
------------------
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money. Return the fewest number of coins 
needed to make up that amount. Return -1 if amount cannot be made up by any combination.

Examples:
--------
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: Cannot make amount 3 with given coins

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed for zero amount

Approach:
--------
1. Use bottom-up dynamic programming
2. For each amount from 1 to target, calculate minimum coins needed
3. For each coin, try using it if it doesn't exceed current amount
4. Time Complexity: O(amount * len(coins))
5. Space Complexity: O(amount)
"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize dp array with amount + 1 (impossible value)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        # Calculate minimum coins for each amount from 1 to target
        for curr_amount in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                if coin <= curr_amount:
                    dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount - coin])
        
        # Return -1 if amount cannot be made, otherwise return minimum coins
        return dp[amount] if dp[amount] != amount + 1 else -1

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular case
    coins1 = [1,2,5]
    assert solution.coinChange(coins1, 11) == 3, "Test case 1 failed"
    
    # Test case 2: Impossible amount
    coins2 = [2]
    assert solution.coinChange(coins2, 3) == -1, "Test case 2 failed"
    
    # Test case 3: Zero amount
    coins3 = [1]
    assert solution.coinChange(coins3, 0) == 0, "Test case 3 failed"
    
    # Test case 4: Multiple solutions, want minimum
    coins4 = [1,2,5]
    assert solution.coinChange(coins4, 4) == 2, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
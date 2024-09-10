class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minStock = inf
        for price in prices:
            minStock = min(minStock, price)
            maxProfit = max(maxProfit, price-minStock)
        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 9999
        profit = 0
        
        for price in prices:
            min_val = min(price, min_val)
            profit = max(profit, price - min_val)
            
        return profit

            
# Last updated: 6/19/2025, 10:37:36 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = 0
        for price in prices:
            if buy > price:
                buy = price
            elif price - buy > sell:
                sell = price - buy
        
        return sell

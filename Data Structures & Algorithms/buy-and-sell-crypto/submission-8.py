class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        low = prices[0]
        for i in prices:
            total = max(i-low,total)
            low = min(i,low)
        return total

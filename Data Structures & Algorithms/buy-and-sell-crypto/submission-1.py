class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxp = 0

        for i,price in enumerate(prices):
            if price < min:
                min = price
            elif price >maxp and i!= 0:
                maxp = max(maxp,price-min)
        return maxp
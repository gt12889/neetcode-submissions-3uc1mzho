class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        mini = prices[0]
        for i,price in enumerate(prices):
            if i ==0:
                continue
            diff = price - mini
            maximum = max(diff,maximum)
            mini = min(price,mini)
        return maximum

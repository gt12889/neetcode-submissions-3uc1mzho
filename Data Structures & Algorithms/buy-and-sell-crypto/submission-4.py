class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0]
        for i in prices:
            diff = i-mini
            maxi = max(diff,maxi)
            mini = min(i,mini)
        return maxi
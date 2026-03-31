class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0]
        for n in prices:
            #diff = 0
            if n < mini:
                mini = n
            else:
                maxi = max(n-mini, maxi)
        return maxi
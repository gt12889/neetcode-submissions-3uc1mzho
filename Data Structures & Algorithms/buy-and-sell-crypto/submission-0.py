class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0
    
        for current in prices:
            if min_price>current:
                min_price = current
            else:
                max_price = max(max_price,current-min_price)
        return max_price
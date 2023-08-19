class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leng = len(prices)
        maxProfit = -inf
        minBuy = inf

        for i in range(leng-1):
            minBuy = min(prices[i],minBuy)
            profit = prices[i+1]-minBuy 
            maxProfit = max(maxProfit, profit)
        
        if maxProfit < 0:
            return 0
        return maxProfit

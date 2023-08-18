class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leng = len(prices)
        minBuy = inf
        maxProfit = -inf

        # i = leng-1
        # while i > 0:
        #     maxSell = max(prices[i], maxSell)
        #     profit = maxSell-prices[i-1]
        #     maxProfit = max(profit, maxProfit)
        #     i -= 1

        i = 0
        while i < leng-1:
            minBuy = min(prices[i], minBuy)
            profit = prices[i+1]-minBuy
            maxProfit = max(maxProfit,profit)
            i += 1
        
        if maxProfit < 0:
            return 0
        return maxProfit
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        sell = 1
        maxProfit = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell]-prices[buy]
                maxProfit = max(profit, maxProfit)
            else:
                buy = sell
            sell += 1
        
        return maxProfit
                
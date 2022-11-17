class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [cost[0],cost[1]]
        
        for i in range(2,len(cost)):
            minStep = min(minCost[i-1], minCost[i-2])
            minCost.append(minStep + cost[i])
        
        return min(minCost[-1], minCost[-2])
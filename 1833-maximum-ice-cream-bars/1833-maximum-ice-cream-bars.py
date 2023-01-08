class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cost = 0
        bars = 0

        for c in costs:
            if c + cost <= coins:
                cost += c 
                bars += 1


        return bars

'''
costs = [5,6,10,1,3,4,2] --> [1,2,3,4,5,6,10]
coins = 10 

c = 1
cost = 1
bars = 1

c = 2
cost = 3
bars = 2

c = 3
cost = 6
bars = 3

c = 4
cost = 10
bars = 4 

return 4
'''
        

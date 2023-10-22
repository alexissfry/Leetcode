class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0 

        i = 0
        while i<len(colors)-1:
            if colors[i] == colors[i+1]:
                color = colors[i]
                running = neededTime[i]
                maxTime = running 
                i+=1
                while i < len(colors) and colors[i] == color:
                    maxTime = max(maxTime,neededTime[i])
                    running += neededTime[i]
                    i += 1 
                cost += running-maxTime
            else:
                i+=1
        return cost

'''
colors = "abaac", neededTime = [1,2,3,4,5], len = 5

i=2
color = "a"
running = 3
maxTime = 3 

i=3
maxTime = 4
running = 7 

i = 4
cost = 3
'''
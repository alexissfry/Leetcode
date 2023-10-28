class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        #Build out a tree/graph to represent managers and their employees 
        relations = {}

        for i in range(n):
            if manager[i] in relations:
                relations[manager[i]].append(i)
            else:
                relations[manager[i]] = []
                relations[manager[i]].append(i)

        #Find the longest path from root of the headID manager to the furthest away employee, this will give the total time it takes to inform all employees 

        def dfs(currID):
            #If we are at an employee that has no subordinates, stop searching 
            if currID not in relations:
                return informTime[currID]
            
            totTime = 0
            for e in relations[currID]:
                totTime = max(dfs(e),totTime)
            
            return totTime + informTime[currID]

        return dfs(headID)
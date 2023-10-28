class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        relations = {}

        for i in range(n):
            boss = manager[i]
            if boss in relations:
                relations[boss].append(i)
            else:
                relations[boss] = []
                relations[boss].append(i)

        def dfs(currID):
            if currID not in relations:
                return 0

            totTime = 0
            for ids in relations[currID]:
                totTime = max(totTime, dfs(ids))
            
            return totTime + informTime[currID]


        return dfs(headID)

        

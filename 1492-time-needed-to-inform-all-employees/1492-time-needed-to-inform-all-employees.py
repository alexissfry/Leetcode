class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        relation = {}
        path = -1 

        for i in range(n):
            if manager[i] in relation:
                relation[manager[i]].append(i) 
            else:
                relation[manager[i]] = []
                relation[manager[i]].append(i)

        def dfs(node):
            if node not in relation:
                return 0

            maxLen = 0
            for n in relation[node]:
                maxLen = max(maxLen,dfs(n))

            return maxLen + informTime[node]
          
        return dfs(headID)
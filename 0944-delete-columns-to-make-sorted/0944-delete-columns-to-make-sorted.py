class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        numChar = len(strs[0])
        colDel = set()

        for i in range(len(strs)-1):
            j = 0
            while j < numChar:
                if strs[i][j] > strs[i+1][j]:
                    colDel.add(j)
                j +=1 
        
        return len(colDel)
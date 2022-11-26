class Solution:
    def maxDepth(self, s: str) -> int:

        currDep = 0
        maxDep = 0

        for c in s:
            if c is "(":
                currDep += 1
                maxDep = max(maxDep, currDep)
            elif c is ")":
                currDep -= 1

        return maxDep
                
'''
test = "(1+(2*3)+((8)/4))+1"
currDep = 0, maxDep = 3
'''
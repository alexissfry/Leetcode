class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictNums = {}
        occur = set()
        
        for i in arr:
            if i in dictNums:
                dictNums[i] += 1
            else:
                dictNums[i] = 1
        
        for i in dictNums.values():
            if i in occur:
                return False
            occur.add(i)
        
        return True 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictNums = Counter(arr)
        occur = set()
        
        for i in dictNums.values():
            if i in occur:
                return False
            occur.add(i)
        
        return True 
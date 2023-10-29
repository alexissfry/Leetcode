class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chars = set()

        def overlap(chars, s):
            prev = set()

            for c in s:
                if c in chars or c in prev:
                    return True 
                prev.add(c)
            return False
        
        def backtrack(i):
            if i == len(arr):
                return len(chars)
            
            res = 0
            if not overlap(chars, arr[i]):
                for c in arr[i]:
                    chars.add(c)
                res = backtrack(i+1)
                for c in arr[i]:
                    chars.remove(c)
            
            return max(res, backtrack(i+1))
        
        return backtrack(0)



        
        
        
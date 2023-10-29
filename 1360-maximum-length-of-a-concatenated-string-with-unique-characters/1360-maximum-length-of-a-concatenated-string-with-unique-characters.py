class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def overlap(s, chars):
            prev = set()
            for c in s:
                if c in chars or c in prev:
                    return True 
                prev.add(c)
            return False 

        chars = set()
        def backtrack(i):
            if i == len(arr):
                return len(chars)

            res = 0
            if not overlap(arr[i],chars):
                for c in arr[i]:
                    chars.add(c)
                res = backtrack(i+1)
                for c in arr[i]:
                    chars.remove(c)
            return max(res, backtrack(i+1))

        return backtrack(0)
            

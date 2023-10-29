class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chars = set()

        def overlap(chars, s):
            c = Counter(chars) + Counter(s)
            return max(c.values()) > 1
        
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



        
        
        
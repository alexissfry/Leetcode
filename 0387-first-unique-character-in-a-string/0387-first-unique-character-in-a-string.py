class Solution:
    def firstUniqChar(self, s: str) -> int:
        rep = {}
        
        for i in s:
            if i in rep:
                rep[i] += 1
            else:
                rep[i] = 1
        
        for idx, c in enumerate(s):
            if rep[c] == 1:
                return idx     
        
        return -1
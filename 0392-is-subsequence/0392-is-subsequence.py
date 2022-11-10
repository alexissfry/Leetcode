class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:       
        a = len(s)
        b = len(t)
        
        if a>b:
            return False
        if a == 0:
            return True 
        
        i,j = 0,0
        
        while (i<a and j<b):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i==a
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        sub = len(s)
        stringy = len(t)
        
        if sub > stringy:
            return False
        if sub == 0:
            return True
        
        i, j = 0, 0 
        while (i<sub) and (j<stringy):
            if s[i] == t[j]:
                i += 1 
            j+= 1
        
        return i == sub
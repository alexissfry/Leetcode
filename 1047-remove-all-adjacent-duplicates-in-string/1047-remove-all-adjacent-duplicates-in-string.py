class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                s = s[0:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i += 1
        
        return s
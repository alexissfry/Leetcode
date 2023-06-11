class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        result = ""
        len1 = len(word1)
        len2 = len(word2)
        
        while i < len1 and i < len2:
            result += word1[i]
            result += word2[i]
            i += 1
            
        if i<len(word1):
            result += word1[i:]
        if i<len(word2):
            result += word2[i:]
        
        return result
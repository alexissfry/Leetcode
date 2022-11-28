class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        
        word1 = {}
        word2 = {}
        
        for c in s:
            if c in word1:
                word1[c] += 1
            else:
                word1[c] = 1
        
        for c in t:
            if c in word2:
                word2[c] += 1
            else:
                word2[c] = 1
                
        return word1 == word2
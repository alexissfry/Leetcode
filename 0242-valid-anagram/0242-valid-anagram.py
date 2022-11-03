class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        
        word1 = {}
        word2 = {}
        
        for i in s:
            if i in word1:
                word1[i] += 1
            else:
                word1[i] = 1
        
        for j in t:
            if j in word2:
                word2[j] += 1
            else:
                word2[j] = 1
                
        return word1 == word2
    
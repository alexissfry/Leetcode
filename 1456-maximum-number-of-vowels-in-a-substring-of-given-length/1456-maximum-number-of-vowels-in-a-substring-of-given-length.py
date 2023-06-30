class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vows = set()
        vows.update("a", "e", "i", "o", "u")
        currVows = 0
        
        for i in range(k):
            currVows += int(s[i] in vows)
        maxVows = currVows
            
        for j in range(k, len(s)):
            currVows += int(s[j] in vows)
            currVows -= int(s[j-k] in vows)
            maxVows = max(currVows,maxVows)

        return maxVows
        
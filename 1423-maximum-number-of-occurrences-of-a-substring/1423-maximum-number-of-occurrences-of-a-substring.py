class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        counter = {}

        for i in range(len(s)-minSize+1):
            sub = s[i:i+minSize]
            currentChars = set(sub)

            if len(currentChars) <= maxLetters:
                if sub in counter:
                    counter[sub] += 1 
                else:
                    counter[sub] = 1
            
        maxOccur = 0

        for c in counter.values():
            maxOccur = max(maxOccur, c)

        return maxOccur
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        longest = 0
        middle = -1
        
        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        for j in counter.values():
            if j%2 == 0:
                longest += j
            elif j%2 == 1:
                middle = True
                longest += j-1
        
        if middle == True:
            longest += 1 
        
        return longest
                
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        result = ""
        

        for i in range(0,len(words)-1):
            result += words[i] + " "

        result += words[-1]
    
        return result
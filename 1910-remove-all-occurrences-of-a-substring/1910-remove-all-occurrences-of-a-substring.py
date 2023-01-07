class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        def helper(word,p):
            index = word.find(p)

            if index == -1:
                return word
            
            word = word[:index] + word[index+len(p):]
            value = helper(word,p)
            return value
        
        return helper(s, part)      
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minLen = 201
        prefix = ""

        for string in strs:
            if len(string) < minLen:
                minLen = len(string)

        for i in range(0,minLen):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return prefix  
            prefix += c
        
        return prefix
            
        
# testcase: ["cat","car","cab"] --> prefix = "ca"
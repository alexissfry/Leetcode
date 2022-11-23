class Solution(object):
                
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def parse(s):
            stackS = [] 

            for c in s:
                if c == '#':
                    if stackS:
                        stackS.pop()
                else:
                    stackS.append(c)
            return stackS
                    
        return parse(s) == parse(t)

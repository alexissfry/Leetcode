class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stackS = []
        stackT = []
        
        for c1 in s:
            if c1 == '#':
                if stackS:
                    stackS.pop()
            else:
                stackS.append(c1)
                
        for c2 in t:
            if c2 == '#':
                if stackT:
                    stackT.pop()
            else:
                stackT.append(c2)
                
                
        return stackS == stackT
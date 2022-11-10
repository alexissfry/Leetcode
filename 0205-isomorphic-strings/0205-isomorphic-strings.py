class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        StoT = {}
        TtoS = {}
        
        for c1, c2 in zip(s,t):
            if c1 not in StoT:
                StoT[c1] = c2
            if c2 not in TtoS:
                TtoS[c2] = c1
            if StoT[c1] != c2 or TtoS[c2] != c1:
                    return False
                
        return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        StoT = dict()
        TtoS = dict()

        for c1, c2 in zip(s,t):
            if (c1 in StoT and StoT[c1] != c2) or (c2 in TtoS and TtoS[c2] != c1):
                return False 

            StoT[c1] = c2
            TtoS[c2] = c1

        return True



        
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = set()
        rep = set()

        for i in range(len(s)-9):
            curr = s[i:i+10]
            if (curr in seq):
                rep.add(curr)
            else:
                seq.add(curr)
        
        return rep
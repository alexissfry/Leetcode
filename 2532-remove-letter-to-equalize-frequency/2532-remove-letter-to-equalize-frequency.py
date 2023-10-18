class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        counter = {}
        for c in word:
            if c in counter:
                counter[c] += 1 
            else:
                counter[c] = 1

        seen = {}
        for i in counter.values():
            if i in seen:
                seen[i] += 1 
            else:
                seen[i] = 1
        
        if len(seen) == 2:
            f1,f2 = min(seen.keys()),max(seen.keys())

            return (f1+1 == f2 and seen[f2]==1) or (f1 == 1 and seen[f1]==1)
        if len(seen) == 1:
            return list(seen.keys())[0] == 1 or list(seen.values())[0] == 1

        return False

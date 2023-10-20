class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.Counter(s)
        seen = set()
        count = 0
        
        for c,f in freq.items():
            while f>0 and f in seen:
                f -= 1 
                count += 1
            seen.add(f)

        return count 



        
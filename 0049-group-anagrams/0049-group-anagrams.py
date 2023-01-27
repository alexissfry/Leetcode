class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        
        for s in strs:
            curr = "".join(sorted(s))
            
            if curr not in ana:
                ana[curr] = []
                
            ana[curr].append(s)
        
        return list(ana.values())
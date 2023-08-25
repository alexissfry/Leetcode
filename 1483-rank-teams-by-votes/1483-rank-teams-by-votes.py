class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        voteCount = {}

        for v in votes: 
            for i in range(len(v)):
                if v[i] in voteCount:
                    voteCount[v[i]][i] += -1 
                else:
                    voteCount[v[i]] = [0] * len(v)
                    voteCount[v[i]][i] = -1 
        
        candidates = []

        for a,b in voteCount.items():
            candidates.append((b,a))

        candidates.sort()

        result = ""
        for c in candidates:
            result += c[1]
        
        return result
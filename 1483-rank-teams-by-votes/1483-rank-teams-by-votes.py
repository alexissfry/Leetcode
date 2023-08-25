class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        voteCount = {}

        for v in votes:
            for i in range(len(v)):
                if v[i] in voteCount:
                    voteCount[v[i]][i] -= 1
                else:
                    voteCount[v[i]] = [0] * len(v)
                    voteCount[v[i]][i] = -1

        print(voteCount)
        
        allTallies = []
        for a,b in voteCount.items():
            allTallies.append((b,a))

        allTallies.sort()
        result = "" 
        print(allTallies)
        for n in range(0,len(allTallies)):
            result += allTallies[n][1]
        
        return result

                

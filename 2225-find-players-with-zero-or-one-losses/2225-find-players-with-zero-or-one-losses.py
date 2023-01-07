class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        answer = [[],[]]

        for m in matches:
            if m[1] in losers:
                losers[m[1]] += 1
            else:
                losers[m[1]] = 1   
            
            if m[0] not in losers:
                losers[m[0]] = 0


        for p, v in losers.items():
            if v == 1:
                answer[1].append(p)
            if v == 0:
                answer[0].append(p)
                
        answer[0].sort() #nlogn time complexity 
        answer[1].sort() #nlogn time complexity 

        return answer 
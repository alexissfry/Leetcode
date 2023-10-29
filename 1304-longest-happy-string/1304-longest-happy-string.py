from heapq import heapify, heappop, heappush

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
    # hint: greedy and counter
        res = []
        count = {"a":a, "b":b, "c":c}
        pq = []

        for k,v in count.items():
            if v != 0:
                pq.append((-v,k))
                
        heapify(pq)

        while pq:
            count1, char1 = heappop(pq)
            if len(res) >= 2 and res[-1]==res[-2]==char1:
                if len(pq) == 0:
                    break
                else:
                    #try the next most frequent letter
                    count2, char2 = heappop(pq)
                    res.append(char2)

                    if count2 + 1 != 0:
                        heappush(pq,(count2+1, char2))
                    heappush(pq,(count1,char1))
            else:
                res.append(char1)

                if count1 + 1 != 0:
                        heappush(pq,(count1+1, char1))

        return ''.join(res)


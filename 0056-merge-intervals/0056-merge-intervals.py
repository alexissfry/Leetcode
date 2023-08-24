class Solution:
    '''
    Given list of intervals, each start time and end time 
    --> [[1,10],[5,10],[8,200]], intervals are inclusive 
    Merge any of intervals that overlap and return the final intervals back 

    testcase1 = [[1,10],[5,10],[8,200]] --> [[1,200]]
    testcase2 = [[20,40], [6,10], [8,10], [30,39]] --> [[6,10], [20,40]]
    edgecase1 = [] --> []
        --> intervals cannot be invalid, like [10,1]
        --> no empty intervals, all will have two integers 
        --> possible to have no intervals 

    1. sort inter 
    2. find the min start interval
    3. max end interval 
    4. when the max end interval < start interval 
    '''

    def merge(self, inter: List[List[int]]) -> List[List[int]]:

        if len(inter) == 0:
            return []

        inter.sort()
        startInter = 0
        minStart = inter[0][0]
        endInter = 0
        maxEnd = inter[0][1]
        result = [[minStart,maxEnd]]
        intervals = 0

        for i in range(1, len(inter)):
            current = inter[i]
            startInter = current[0]
            endInter = current[1]

            if maxEnd < startInter:
                result.append([0,0])
                intervals += 1 
                minStart = startInter
                maxEnd = endInter
            else:
                minStart = min(minStart,startInter)
                maxEnd = max(maxEnd,endInter)
                
            result[intervals][0] = minStart
            result[intervals][1] = maxEnd
        
        return result

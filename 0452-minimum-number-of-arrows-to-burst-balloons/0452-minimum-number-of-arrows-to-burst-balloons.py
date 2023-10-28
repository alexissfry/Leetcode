class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        Have all x_start and x_end positions 
        Find all possible interval overlaps between all the balloons
        For each interval, we will need to use one arrow

        [[10,16],[2,8],[1,6],[7,12]] --> 
        [[1,6],[2,8],[7,12],[10,16]]
        [[2,6],[10,12]]
        '''
        points.sort()
        intervals = [points[0]]


        for p in range(1,len(points)):
            if points[p][0] > intervals[-1][1]:
                intervals.append(points[p])
            else:
                newInterval = [max(intervals[-1][0],points[p][0]),min(intervals[-1][1],points[p][1])]
                intervals.pop()
                intervals.append(newInterval)

        return len(intervals)
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        for i in range(0,len(stones)):
            stones[i] = -stones[i]        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
            
            if max1 != max2:
                heapq.heappush(stones, max1-max2)
        
        if len(stones) != 0:
            return -stones[0]
        
        return 0
            
            
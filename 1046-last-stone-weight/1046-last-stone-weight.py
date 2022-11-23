
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            
            if max1 == max2:
                stones.remove(max2)
            else:
                stones.remove(max2)
                stones.append(max1-max2)
        
        if len(stones) != 0:
            return stones[0]
        
        return 0
            
            
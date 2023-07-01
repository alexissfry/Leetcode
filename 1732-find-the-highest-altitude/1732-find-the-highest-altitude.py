class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        maxAlt = 0
        
        for n in gain:
            
            alt += n
            
            if alt > maxAlt:
                maxAlt = alt
                
        return maxAlt 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        valid = 0
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftSide = (i==0) or (flowerbed[i-1]==0)
                rightSide = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                
                if leftSide and rightSide:
                    flowerbed[i] = 1 
                    valid += 1
                    
        return valid >= n
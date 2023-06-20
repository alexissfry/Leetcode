class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
            
        result = []
        maxCandy = candies[0]
        
        for c in candies:
            if c > maxCandy:
                maxCandy = c
        
        for i in candies:
            if i+extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)
            print(i+extraCandies)
                
        return result
            
            
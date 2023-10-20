class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negCount = 0
        
        for n in nums:
            if n==0:
                return 0 
            
            if n < 0:
                negCount += 1

        if negCount%2==1:
            return -1
        return 1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxOnes = 0
        currOnes = 0
        avail = k
        i = 0
        
        while i < len(nums):
            
            if nums[i] == 1:
                currOnes += nums[i]
            elif avail == 0:
                while nums[i-currOnes] == 1:
                    currOnes -= 1
            else:
                currOnes += 1
                avail -= 1
                
            maxOnes = max(maxOnes, currOnes)
            i += 1
        
        return maxOnes
                
                
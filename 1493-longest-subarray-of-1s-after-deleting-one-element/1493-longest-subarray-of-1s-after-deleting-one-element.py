class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxOnes = 0
        currOnes = 0
        
        for i in range(len(nums)):
            
            if nums[i] == 1:
                currOnes += nums[i]
                maxOnes = max(maxOnes, currOnes)
            elif k == 0:
                while nums[i-currOnes] == 1:
                    currOnes -= 1
            else:
                currOnes += 1
                k -= 1
                maxOnes = max(maxOnes, currOnes)
        
        return maxOnes
    
    def longestSubarray(self, nums: List[int]) -> int:
        return self.longestOnes(nums,1) - 1
    
        
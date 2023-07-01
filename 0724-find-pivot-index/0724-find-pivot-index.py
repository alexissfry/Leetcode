class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totSum = sum(nums)
        runningSum = 0
        
        for i,n in enumerate(nums):
            
            if runningSum == totSum-(runningSum + n):
                return i
            
            runningSum += n
        
        return -1
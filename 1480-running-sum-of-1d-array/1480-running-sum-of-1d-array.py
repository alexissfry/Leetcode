class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        currentSum = 0
        
        for i in range(len(nums)):
            currentSum += nums[i] 
            nums[i] = currentSum
            
        return nums
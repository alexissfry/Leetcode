class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#the brute force algorithm would take two nested for loops and have a running sum of numbers and keep track of the maximum sum until you've iterated through the whole array 
        maxSum = nums[0]
        currSum = 0
        
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i 
            maxSum = max(currSum, maxSum)
            
        return maxSum
    
'''
nums = [5,4,-1,7,8]
i=5, currSum=5, maxSum=5
i=4, currSum=9, maxSum=9
i=-1, currSum=8, maxSum=9
i=7, currSum=15, maxSum=15
i=8, currSum=23, maxSum=23
'''
                
        
        
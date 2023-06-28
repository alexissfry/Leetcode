class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # find sum of first k elements
        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            # adjust the window's sum as you iterate 
            currSum += nums[i] - nums[i - k]    
            # update max 
            maxSum = max(maxSum, currSum)

        return maxSum/k

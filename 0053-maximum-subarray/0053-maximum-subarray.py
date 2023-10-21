class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0] 

        for i in range(1,len(nums)): 
            nums[i] = max(nums[i-1]+nums[i],nums[i])

            maxSum = max(maxSum, nums[i])

        return maxSum 
'''
input: nums array of integers 
output: index where the sumLeft = sumRight 
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totSum = 0

        for n in nums:
            totSum += n

        left = 0
        right = totSum 
        for i in range(len(nums)):
            if i > 0:
                left += nums[i-1]
            right -= nums[i]

            if left == right:
                return i 

        return -1


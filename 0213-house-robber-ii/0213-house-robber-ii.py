class Solution:
    def rob(self, nums: List[int]) -> int:

        def getRobbed(nums):
            robbed = [0] * len(nums)
            robbed[0] = nums[0]
            robbed[1] = max(nums[0],nums[1])

            for i in range(2,len(nums)):
                robbed[i] = max(robbed[i-1], robbed[i-2]+nums[i])

            return robbed

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        return max(getRobbed(nums[1:])[-1], getRobbed(nums[:len(nums)-1])[-1])


class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(nums):
        
            maxStart = max(nums[0],nums[1])
            money = [nums[0], maxStart]

            for i in range(2,len(nums)):
                money.append(max(money[i-2]+nums[i],money[i-1]))

            return money[-1]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        return max(dp(nums[1:]), dp(nums[:-1]))
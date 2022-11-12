class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        maxRob = [nums[0],max(nums[0],nums[1])]
        
        for i in range(2, len(nums)):
            rob = max(maxRob[i-1],maxRob[i-2]+nums[i])
            
            maxRob.append(rob)
        
        return maxRob[-1]
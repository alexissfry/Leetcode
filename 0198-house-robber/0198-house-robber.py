class Solution:
    def rob(self, nums: List[int]) -> int:
        path = [0] * len(nums)

        if len(path) == 1:
            return nums[0]

        path[0] = nums[0]
        path[1] = max(nums[0],nums[1])
        print(path)

        for i in range(2,len(nums)):
            path[i] = max(path[i-1], nums[i]+path[i-2])
        
        return path[-1]
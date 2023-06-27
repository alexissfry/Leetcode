class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[nonzero]
                nums[nonzero] = nums[i]
                nums[i] = temp
                
                nonzero += 1
            
        
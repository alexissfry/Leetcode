class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                #j=i
                #while j > nonzero:
                temp = nums[nonzero]
                nums[nonzero] = nums[i]
                nums[i] = temp
                    #j -= 1
                nonzero += 1
            
        
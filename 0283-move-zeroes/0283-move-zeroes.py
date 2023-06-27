class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                j=i
                while j > nonzero:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
                    j -= 1
                nonzero += 1
            
        
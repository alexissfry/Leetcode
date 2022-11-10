class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left = 0
        
        for i,n in enumerate(nums):
            left += n
            right = tot - left
            
            if left-n == right:
                return i
        
        return -1
            
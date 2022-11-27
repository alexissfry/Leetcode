class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = []
        
        for i in range(len(nums)-1):
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    sols.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
                    
        return set(sols) 
                
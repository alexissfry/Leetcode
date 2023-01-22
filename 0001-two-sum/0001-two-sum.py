class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        
        for i, n in enumerate(nums):
            complement = target - n
            
            if n in tracker:
                return [i, tracker[n]]
            else:
                tracker[complement] = i
                

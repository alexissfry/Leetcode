class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in history:
                return [i, history[complement]]
            else:
                history[num] = i
                
        return []
    
    
        


        
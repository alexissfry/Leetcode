class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        
        for i, e in enumerate(nums):
            comp = target - e
            if comp in history:
                return [i,history[comp]]
            else:
                history[e] = i 
            
        return []
    
    
        


        
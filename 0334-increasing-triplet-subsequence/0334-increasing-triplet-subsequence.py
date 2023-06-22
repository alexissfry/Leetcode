class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
    
        smallest = float('inf')  # Initialize smallest to positive infinity
        second_smallest = float('inf')  # Initialize second_smallest to positive infinity
        
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= second_smallest:
                second_smallest = n
            else: 
                return True 
                
        return False
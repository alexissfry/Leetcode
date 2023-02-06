class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        result = [1]*leng
        
        pre = 1
        post = 1 
        
        for i in range(leng):
            result[i] *= pre
            pre *= nums[i]
            result[leng-i-1] *= post
            post *= nums[leng-i-1]
        
        return result 
        
        
        
            
            
        
        
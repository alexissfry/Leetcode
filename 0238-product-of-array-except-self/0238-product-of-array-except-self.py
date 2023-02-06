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
        
'''
[1,2,3,4]

i = 0
result=[1,1,1,1]
pre = 1
result=[1,1,1,1]
post = 4

i = 1 
result=[1,1,1,1]
pre = 2
result=[1,1,4,1]
post = 12

i = 2
result=[1,1,8,1]
pre = 6
result=[1,12,8,1]
post = 24

i = 3
result=[1,12,8,6]
pre = 6
result=[24,12,4,1]
post = 24
'''
        
        
            
            
        
        
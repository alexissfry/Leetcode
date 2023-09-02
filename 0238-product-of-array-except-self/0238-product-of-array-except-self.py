class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leng = len(nums)
        products = [1]*leng

        for i in range(1,leng):
            products[i] = products[i-1]*nums[i-1]
        
        right = nums[-1]

        for i in range(leng-2,-1,-1):
            products[i] *= right 
            right *= nums[i]

        return products 


        
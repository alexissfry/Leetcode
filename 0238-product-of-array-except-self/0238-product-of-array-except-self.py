class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        answer = [1] * len(nums)

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            answer[j] *= postfix
            postfix *= nums[j]

        return answer
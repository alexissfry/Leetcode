class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        maxLen = 0

        for i in range(len(nums)):
            for j in range(0, i):
                d = nums[i]-nums[j]

                dp[(i,d)] = 1 + dp.get((j,d), 0) 

                maxLen = max(maxLen, dp[(i,d)])

        return maxLen+1

'''
[1, 2, 0, 1, 2, 3]
[... j... i]

dp[(j,d)] = x # there is a longest arithmetic subsequence of length x ending at nums[j] with difference d
AND I know that nums[i]-nums[j] = d

dp[(i,d)] = the longest arithmetic subsequence that ends at nums[i] with a difference of d
'''


        

        
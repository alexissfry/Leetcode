class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # clarifying questions:
        # are A and a considered the same character? or are we told all upper or lower?
        
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    # continue the subsequence, all of the valid matches before this point
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 
        print(dp)
        return dp[-1][-1]

        